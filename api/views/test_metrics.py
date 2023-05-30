from django.apps import apps
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import KuderTest, TechUser
from api.serializers.test_metrics import KuderTestSerializer
from api.serializers.user import UserSignUpSerializer

def validate_user(request, user_id):
    user = TechUser.objects.get(id=user_id)
    try:
        user = TechUser.objects.get(id=user_id)
    except TechUser.DoesNotExist:
        return False

    # if not request.user.id == user.id:
    #     return False
    return user

class KuderView(APIView):
    def get(self, request, user_id):
        user = validate_user(request, user_id)

        if user is False:
            return Response(
                {"error": "You are not authorized to perform this action"},
                status.HTTP_401_UNAUTHORIZED,
            )
        try:
            kuder = KuderTest.objects.filter(user=user).last()
            if kuder is None:
                return Response(
                    {"message": "No kuder test found"}, status.HTTP_404_NOT_FOUND
                )
            serializer = KuderTestSerializer(kuder)
            return Response({"message": serializer.data}, status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id):
        data = request.data
        user = validate_user(request, user_id)

        if user is False:
            return Response(
                {"error": "You are not authorized to perform this action"},
                status.HTTP_401_UNAUTHORIZED,
            )

        try:
            item = KuderTest.objects.create(
                user=user,
                result=data["result"],
            )
            item.save()
            return Response(
                {
                    "message": "Kuder test saved",
                    "test": {"id": item.id, "result": item.result},
                },
                status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
