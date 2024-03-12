from fastapi import FastAPI, HTTPException
import os
import requests
from modules.tokenhandler import tokenHandler
from validator.validator import QueryParameters
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

def urlConstructor(queryParameters: QueryParameters):
    if (queryParameters.word):
        return searchUsingCriteria(queryParameters, 'word')
    if (queryParameters.cig):
        return searchUsingCriteria(queryParameters, 'cig')
    if (queryParameters.phone):
        return searchUsingCriteria(queryParameters, 'phone')
    if (queryParameters.email):
        return searchUsingCriteria(queryParameters, 'email')

def searchUsingCriteria(query: QueryParameters, criteria_type: str):
    base_url = 'https://www.zohoapis.com/crm/v2/Contacts/search?criteria='
    criteria = getattr(query, criteria_type, None)
    if criteria:
        #print("We are searching by:", criteria_type, ":", criteria)
        return f"{base_url}{criteria}"
    return base_url[:-14]

def accessToken():
    access_token = tokenHandler.getAccessToken()
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 3400
    }

def query(access_token):
    headers = {"Authorization": f"Zoho-oauthtoken {access_token().access_token}"}
    response = requests.get(f"{os.getenv('ZOHO_API_DOMAIN')}/crm/v3/users?type=AllUsers", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        #devolvemos exactamente lo que estamos leyendo para un debuggin en postman/burno/apiconfigdeconfianza.
        raise HTTPException(status_code=response.status_code, detail=response.json())
    

@app.post("/crm/token")


@app.post("/crm/query")
async def getData(queryParameters: QueryParameters):
    access = accessToken()
    headers = {"Authorization": f"Zoho-oauthtoken {access["access_token"]}"}
    logging.info("urlsConstructor returned: " + urlConstructor(queryParameters))
    return urlConstructor(queryParameters)
