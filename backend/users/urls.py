from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SignupView, HomeView, UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # Get access + refresh tokens
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh access token
    path('api/token/', csrf_exempt(TokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('api/token/refresh/', csrf_exempt(TokenRefreshView.as_view()), name='token_refresh'),
]