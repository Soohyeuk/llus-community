import json # Allows you to format and print incomin JSON data for debugging
from rest_framework.response import Response # Provides a standardized way to return API response in DJango REST framework
from rest_framework import status #Imports status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated

# ✅ HomeView: Sends a friendly JSON message with available endpoints
class HomeView(APIView): # This creates a vie that extends Django REST Framework's API view. Handles HTTP requests
    def get(self, request): # Handles GET reuest when a user visits the API root
        return Response({"message": "Welcome to the API. Available endpoints: /signup, /login, /profile/{id}, /logout, /refresh"}, status=200)

# ✅ SignupView: Handles user registration
class SignupView(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print("Received Signup Data:", json.dumps(request.data, indent=2))  

        try:
            return super().create(request, *args, **kwargs) 
        except Exception as e:
            print("❌ Django Error:", str(e))  #  Print exact error message for debugging
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)  # Send error message to frontend

class UserLoginView(APIView) : # A new class based view specifically for login. Extends API view because login logic is custom
    def post(self, request, *args, **kwargs): #Login requests a POST request (because we send a username/password)
        username = request.data.get("username") # Get username from request
        password = request.data.get("password") # Get password from request

        if not username or not password:
            return Response({"error:" "Both username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=username, password=password) # Checks if username and passwords are correct)

        if user is not None:
            login(request,user) # Creates a session for the logged-in user
            return Response({"message": "Login Successful!", "user" : user.username}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        return Response({"message":f"Hello, {request.user.username}! You are logged in,"})
        
