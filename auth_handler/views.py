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
import random


User = get_user_model()


class SignupView(views.APIView):
    '''
    View for Signup/registration for users.
    '''
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            subject = "Welcome to Clever space"
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

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access': access_token, 'refresh': str(refresh)})


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
        subject = "Your OTP Code for Clever space"
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
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'access': access_token, 'refresh': str(refresh)})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)