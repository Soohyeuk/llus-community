from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SignupView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]