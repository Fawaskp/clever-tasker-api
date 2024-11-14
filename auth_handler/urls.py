from django.urls import path
from .views import EmailPasswordLoginView, SendOTPView, OTPLoginView, SignupView,ValidateToken

urlpatterns = [
    path('validate-token/',ValidateToken.as_view(),name='validate-token'),
    path('signup/', SignupView.as_view(), name='sign-up'),
    path('login/password/', EmailPasswordLoginView.as_view(), name='email-password-login'),
    path('login/otp/', SendOTPView.as_view(), name='otp-login'),
    path('login/otp/verify/', OTPLoginView.as_view(), name='otp-verify'),
]
