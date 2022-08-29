from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from app.bots.bots import webhook_handler
from core.settings import DEBUG


@api_view(["GET"])
@permission_classes([])
def webhook(request):
    if DEBUG:
        print("webhook path:", request.path)

    webhook_handler(request.data)
    return Response({"message": "Ok"}, status.HTTP_200_OK)
