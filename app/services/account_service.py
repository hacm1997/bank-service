from app.services.belvo_client import BelvoClient

class AccountService:
    def __init__(self):
        self.client = BelvoClient()
    
    def get_accounts(self, link_id: str):
        return self.client.get("accounts", {"link": link_id})
    
    def get_account_by_id(self, account_id: str, link_id: str):
        return self.client.get("accounts", {"id": account_id})
