import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer

# ✅ HomeView: Sends a friendly JSON message with available endpoints
class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the API. Available endpoints: /signup, /login, /profile/{id}, /logout, /refresh"}, status=200)

# ✅ SignupView: Handles user registration
class SignupView(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print("📥 Received Signup Data:", json.dumps(request.data, indent=2))  # ✅ Log incoming request data

        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            print("❌ Django Error:", str(e))  # ✅ Print exact error message for debugging
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)  # ✅ Send error message to frontend
