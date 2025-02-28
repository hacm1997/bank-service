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
            # Obtener lista de bancos
            banks = self.bank_service.get_banks()
            if not banks:
                return Response({"error": "No available banks were found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(banks, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "Error al procesar la solicitud", "detalle": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
