from rest_framework import serializers
from django.core.cache import cache
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email','name', 'password','password2']
        
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }
    
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Passwords aren't matching.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2', None)
        user = User.objects.create_user(**validated_data)
        return user
    

class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        otp = attrs.get('otp')

        cached_otp = str(cache.get(f'otp_{email}'))
        if not cached_otp or cached_otp != otp:
            raise AuthenticationFailed('The OTP is invalid or expired')
        cache.delete(f'otp_{email}')
        user = User.objects.get(email=email)
        attrs['user'] = user
        return attrs