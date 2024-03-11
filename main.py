from fastapi import FastAPI, HTTPException
import os
import requests
from modules.tokenhandler import tokenHandler
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/crm/data")
def loginToCrm():
    access_token = tokenHandler.getAccessToken()
    headers = {"Authorization": f"Zoho-oauthtoken {access_token}"}
    response = requests.get(f"{os.getenv('ZOHO_API_DOMAIN')}/crm/v3/settings/modules", headers=headers)
    print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        #devolvemos exactamente lo que estamos leyendo para un debuggin en postman/burno/apiconfigdeconfianza.
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
