from app.services.belvo_client import BelvoClient

class TransactionService:
    def __init__(self):
        self.client = BelvoClient()

    def get_transactions(self, account_id, link_id, page_size=10, page_number=1):
        return self.client.get("transactions", {"link": link_id, "account": account_id, "page_size": page_size, "page": page_number})
    
    def get_transaction_details(self, transaction_id):
        return self.client.get(f"transactions/{transaction_id}/")

