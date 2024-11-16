from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.core.cache import cache
from .serializers import OTPVerifySerializer,SignupSerializer
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .token import generate_custom_token
import random

User = get_user_model()

class ValidateToken(APIView):
    def get(self, request):
        return Response({'message': 'Valid token'})


class SignupView(views.APIView):
    '''
    View for Signup/registration for users.
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            subject = "Welcome to CleverTasker"
            message = "Thank you for signing up..!"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

            return Response({'detail': 'User registered successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailPasswordLoginView(views.APIView):
    '''
    This view handles the login using email and password.
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            return Response({'detail': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        access_token,refresh_token = generate_custom_token(user)

        return Response({'access': access_token, 'refresh': refresh_token})


class SendOTPView(views.APIView):
    '''
    This view handles OTP verification of E-mail/OTP-based login.
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        otp = random.randint(1000,9999)
        cache.set(f'otp_{email}', otp, timeout=300) #generating an otp with 5 minute(300seconds) expiration time
        print(otp)
        subject = "Your OTP Code for CleverTasker"
        message = f"Your OTP code is: {otp}. It will expire in 5 minutes."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

        return Response({'detail': 'OTP sent successfully'}, status=status.HTTP_200_OK)


class OTPLoginView(views.APIView):
    '''
    This view handles OTP sending of E-mail/OTP-based login.
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            access_token, refresh_token = generate_custom_token(user)
            return Response({'access': access_token, 'refresh': refresh_token})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    '''
    This view handles user logout.
    '''

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token is None:
            return Response({'detail': 'Refresh token is required to logout.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            if 'blacklisted' in str(e):
                return Response({'detail': 'Already logged out.'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'detail': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)