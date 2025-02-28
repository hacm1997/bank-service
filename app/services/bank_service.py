from app.services.belvo_client import BelvoClient

class BankService:
    
    def __init__(self):
        self.client = BelvoClient()

    def get_banks(self):
        return self.client.get("institutions", {"page_size": 10})
    
    def get_accounts(self, link_id):
        return self.client.get("accounts", {"link": link_id})
