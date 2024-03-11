# Zoho CRM Middleware

This project serves as a middleware for interacting with the Zoho CRM API. It handles OAuth token management, ensuring that tokens are refreshed as needed and provides a simplified interface for other applications to retrieve data from Zoho CRM without directly managing authentication.

## Dependencies

- Python 3.6+
- FastAPI
- Uvicorn
- requests
- python-dotenv

## Setup

1. Install the required Python packages:

```bash
pip install fastapi uvicorn requests python-dotenv
```

2. Set up the .env file in the roor dir with the values of your credentials:
``` bash
ZOHO_CLIENT_ID=your_client_id
ZOHO_CLIENT_SECRET=your_client_secret
ZOHO_API_DOMAIN=https://www.zohoapis.com
ZOHO_API_REFRESH=https://accounts.zoho.com
```

3. Start the FastAPI server:
```bash
uvicorn main:app --reload
```
