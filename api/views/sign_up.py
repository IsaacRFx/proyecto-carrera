import os
import urllib.request

from django.core.files import File
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import TechUser
from api.serializers.user import UserSignUpSerializer


class SignUpView(APIView):
    def post(self, request):
        image_url = "https://res.cloudinary.com/dt4b5tkwd/image/upload/v1666084085/dev/default-profile-picture1_ypxtk1.jpg"
        result = urllib.request.urlretrieve(image_url, 'default.jpg')
        DEFAULT_PROFILE_PICTURE = File(open(result[0], "rb"))
        
        data = request.data

        serializer = UserSignUpSerializer(data=data, many=False)
        if serializer.is_valid():
            USER_EMAIL = data["email"]
            USER_PASSWORD = data["password"]
            new_user = TechUser.objects.create_user(
                email=USER_EMAIL,
                password=USER_PASSWORD,
                identifier_number=data["identifier_number"],
                profile_picture=DEFAULT_PROFILE_PICTURE,
                first_name=data["first_name"],
                last_name=data["last_name"],
                gender=data["gender"],
            )
            os.remove('default.jpg')
            new_user.save()
            serializer = UserSignUpSerializer(new_user)
            refresh = RefreshToken.for_user(new_user)
            return Response(
                {"message": "Sign up successful", "user": serializer.data, "access":str(refresh.access_token)},
                status.HTTP_201_CREATED,
            )
        return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)

class SignUpAdminView(APIView):
    def post(self, request):
        image_url = "https://res.cloudinary.com/dt4b5tkwd/image/upload/v1666084085/dev/default-profile-picture1_ypxtk1.jpg"
        result = urllib.request.urlretrieve(image_url, 'default.jpg')
        DEFAULT_PROFILE_PICTURE = File(open(result[0], "rb"))
        
        data = request.data

        serializer = UserSignUpSerializer(data=data, many=False)
        if serializer.is_valid():
            USER_EMAIL = data["email"]
            USER_PASSWORD = data["password"]
            new_user = TechUser.objects.create_user(
                email=USER_EMAIL,
                password=USER_PASSWORD,
                identifier_number=data["identifier_number"],
                profile_picture=DEFAULT_PROFILE_PICTURE,
                first_name=data["first_name"],
                last_name=data["last_name"],
                gender=data["gender"],
                role=1,
                is_superuser=True,
                is_staff=True,
            )
            os.remove('default.jpg')
            new_user.save()
            refresh = RefreshToken.for_user(new_user)
            return Response(
                {"message": "Sign up successful", "user": serializer.data, "access":str(refresh.access_token)},
                status.HTTP_201_CREATED,
            )
        return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
