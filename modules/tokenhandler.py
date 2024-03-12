from datetime import datetime, timedelta
import requests
import os
import logging

class TokenHandler:
    def __init__(self):
        self.access_token = None
        self.token_expiry = datetime.utcnow()

    def getAccessToken(self):
        if datetime.utcnow() >= self.token_expiry:
            self.generateNew()
            #print(f"New token generated: {self.access_token}")
            logging.info("Access token generated")
            print(self.access_token)
        return self.access_token
    
    def generateNew(self):
        url = f"{os.getenv('ZOHO_API_REFRESH')}/oauth/v2/token"
        params = {
            'refresh_token': os.getenv('ZOHO_REFRESH_TOKEN'),
            'client_id': os.getenv('ZOHO_CLIENT_ID'),
            'client_secret': os.getenv('ZOHO_CLIENT_SECRET'),
            'grant_type': 'refresh_token'
        }
        
        response = requests.post(url, data=params)
        #print (response.text)
        if response.status_code == 200:
            data = response.json()
            #print("ESTA ES LA DATA", data)
            self.access_token = data['access_token']
            #10ms/10s/10m... simplemente que no cumpla la hora, sea menor el renew...
            if 'expires_in' in data:
                self.token_expiry = datetime.utcnow() + timedelta(seconds=data['expires_in']-30)
        else:
            print("Failed to refresh token:")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")
            raise Exception(f"Failed to refresh token, server returned status code {response.status_code}")
        

    
    def _askForNewRefreshToken(self):
        pass

#init directo en la class al importar, solo hay 1 instancia
tokenHandler = TokenHandler()