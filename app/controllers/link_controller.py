from rest_framework.response import Response
from rest_framework.views import APIView
from app.services.link_service import LinkService
from rest_framework import status
from app.serializers.link_serializer import LinkSerializer

class LinkController(APIView):
    def __init__(self):
        self.link_service = LinkService()

    def get(self, request):
        try:
            # get asociated links
            banks = self.link_service.get_links()
            if not banks:
                return Response({"error": "No available links asociated to bank were found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(banks, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "Error processing request", "detalle": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            # Extract validated data
            institution = serializer.validated_data["institution"]
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            
            result = self.link_service.post_link(institution, username, password)

            if result is None:
                return Response({"error": "Link can not created"}, status=status.HTTP_404_NOT_FOUND)

            return Response(result, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)