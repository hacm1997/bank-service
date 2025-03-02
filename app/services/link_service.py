from app.services.belvo_client import BelvoClient

class LinkService:
    def __init__(self):
        self.client = BelvoClient()

    def get_links(self, page_size=10, page_number=1):
        return self.client.get("links", {"page_size": page_size, "page": page_number})
    
    def post_link(self, institution: str, username: str, password: str):
        data = {
            "institution": institution,
            "username": username,
            "password": password
        }
        return self.client.post("links", data)
    
    def delete_link(self, link_id: str):
        return self.client.delete("links", link_id)
