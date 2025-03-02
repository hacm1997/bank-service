from rest_framework.response import Response
from rest_framework.views import APIView
from app.services.account_service import AccountService
from rest_framework import status
from app.services.kpi_service import KPIService
from app.services.transaction_service import TransactionService


class AccountController(APIView):
    def __init__(self):
        self.acount_service = AccountService()
        self.transaction_service = TransactionService()

    def get(self, request, link_id=None, account_id=None):
        if link_id and account_id:            
            # Get transaction of specified account
            transactions = self.transaction_service.get_transactions(account_id, link_id)
            if transactions is None:
                return Response({"error": "No se pudieron obtener transacciones"})
            kpi = KPIService.calculate_balance(transactions['results'])

            return Response({"kpi": kpi, "transactions": transactions['results']}, status=status.HTTP_200_OK)
        else:
            accounts = self.acount_service.get_accounts(link_id)
            if accounts is None:
                return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

            return Response(accounts, status=status.HTTP_200_OK)