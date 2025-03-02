from rest_framework.response import Response
from rest_framework.views import APIView
from app.services.bank_service import BankService
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class BankController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.bank_service = BankService()
        #self.transaction_service = TransactionService()

    def get(self, request):
        try:
            page_size = request.query_params.get("page_size", 10)
            page = request.query_params.get("page", 1)

            try:
                page_size = int(page_size)
                page = int(page)
            except ValueError:
                return Response({"error": "page_size y page deben ser números enteros"}, status=status.HTTP_400_BAD_REQUEST)

            banks = self.bank_service.get_banks(page_size, page)
            if not banks:
                return Response({"error": "No available banks were found"}, status=status.HTTP_404_NOT_FOUND)

            return Response(banks, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "Error al procesar la solicitud", "detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
