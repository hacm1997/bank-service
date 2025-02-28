from app.services.belvo_client import BelvoClient

class LinkService:
    def __init__(self):
        self.client = BelvoClient()

    def get_links(self):
        return self.client.get("links")
    
    def post_link(self, institution: str, username: str, password: str):
        data = {
            "institution": institution,
            "username": username,
            "password": password
        }
        return self.client.post("links", data)
