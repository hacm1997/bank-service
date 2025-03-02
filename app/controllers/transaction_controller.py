from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app.services.transaction_service import TransactionService
from rest_framework.permissions import IsAuthenticated

class TransactionController(APIView):
    permission_classes = [IsAuthenticated]
    def __init__(self):
        self.transaction_service = TransactionService()

    def get(self, request, link_id=None, account_id=None, transaction_id=None):
        try:
            page_size = request.query_params.get("page_size", 10)
            page = request.query_params.get("page", 1)
            try:
                page_size = int(page_size)
                page = int(page)
                if link_id and account_id:            
                    # Get transaction of specified account
                    transactions = self.transaction_service.get_transactions(account_id, link_id, page_size, page)
                    return Response(transactions, status=status.HTTP_200_OK)
                else:
                    transaction = self.transaction_service.get_transaction_details(transaction_id)
                    if transaction is None:
                        return Response({"error": "Transaction could not be obtained"}, status=status.HTTP_404_NOT_FOUND)
                    return Response(transaction, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"error": "page_size and page must be integers"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": "Error processing request", "detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )