from django.urls import path
from .views import EmailPasswordLoginView, SendOTPView, OTPLoginView, SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='sign-up'),
    path('login/password/', EmailPasswordLoginView.as_view(), name='email-password-login'),
    path('login/otp/', SendOTPView.as_view(), name='otp-login'),
    path('login/otp/verify/', OTPLoginView.as_view(), name='otp-verify'),
]
