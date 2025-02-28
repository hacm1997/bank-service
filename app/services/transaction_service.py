from app.services.belvo_client import BelvoClient

class TransactionService:
    def __init__(self):
        self.client = BelvoClient()

    def get_transactions(self, account_id, link_id):
        return self.client.get("transactions", {"link": link_id, "account": account_id})
