from .serializers import UserSerializer, LoginSerializer
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, logout
from .models import User
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound

User = get_user_model()

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the API. Available endpoints: /signup, /login, /profile/{id}, /logout, /refresh"}, status=200)
  

class SignupView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow all users to log in

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # JWT token generation
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Django session management
            request.session['user_id'] = user.id
            request.session['role'] = user.role  # Store role if necessary
            login(request, user)  # Log user in (Django session)

            return Response({
                'access': access_token,
                'refresh': str(refresh),
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'role': user.role,
                    'school': user.school,
                    'grad_date': user.grad_date,
                      'english_name': user.english_name,  
                    'us_phone_number': user.us_phone_number,  
                    'birth_date': user.birth_date,  
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise NotFound(detail="User not found")

        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

# LogoutView remains the same, as it doesn't depend on user fields
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Clear Django session
            request.session.flush()
            logout(request)  # Log user out (Django session)

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)