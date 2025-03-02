from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework.views import APIView
from rest_framework import status
from app.serializers.user_serializer import UserSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()

class RegisterController(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginConstroller(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            update_last_login(None, user)

            response = JsonResponse({"message": "Login successful"})
            
            # Config secury cookies
            response.set_cookie(
                key="access_token",
                value=str(refresh.access_token),
                httponly=True,
                secure=True,
                samesite="Lax",
                max_age=60 * 60 * 24,
            )

            response.set_cookie(
                key="refresh_token",
                value=str(refresh),
                httponly=True,
                secure=True,
                samesite="Lax",
                max_age=60 * 60 * 24 * 7,
            )

            return response

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutController(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        response = JsonResponse({"message": "Logout successful"})

        # Delete token cookies
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response
    
class UserProfileController(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"username": user.username}, status=200)
