from django.urls import path
from .views import RegisterUserView, VerifyUserEmailView, ResendCodeView, LoginUserView, TestAuthenticationView, PasswordResetRequestView, PasswordResetConfirm, SetNewPassword

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-user/', VerifyUserEmailView.as_view(), name='verify_user'),
    path('resend-code/', ResendCodeView.as_view(), name='resend_code'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('test-login/', TestAuthenticationView.as_view(), name="test_login"),
    path('password-reset/', PasswordResetRequestView.as_view(), name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name="password-reset-confirm"),
    path('set-new-password/', SetNewPassword.as_view(), name="set-new-password"),
]
