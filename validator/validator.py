from pydantic import BaseModel

class QueryParameters(BaseModel):
    version: str
    module: str
    query: str
    email: str
    phone: str
    word: str
    cig: str



