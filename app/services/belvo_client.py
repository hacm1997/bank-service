import base64
import requests
from django.conf import settings

class BelvoClient:
    _instance = None  # To implement Singleton and avoid multiple unnecessary instances

    #Create a new instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BelvoClient, cls).__new__(cls)
            cls._instance.base_url = "https://sandbox.belvo.com/api"
            auth_str = f"{settings.BELVO_USERNAME}:{settings.BELVO_PASSWORD}"
            auth_encoded = base64.b64encode(auth_str.encode()).decode()
            cls._instance.headers = {
                "Authorization": f"Basic {auth_encoded}",
                "Content-Type": "application/json"
            }
        return cls._instance

    def get(self, endpoint, params=None):
        # Generic method for making GET requests to the Belvo API
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else None
