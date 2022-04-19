import json
import os
from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
import requests
from application.models.NlpPolarity import PolarityReq
from decouple import config

try:
    AUTH_ROUTE = os.environ["AUTH_ROUTE"]
    CORE_ROUTE = os.environ["CORE_ROUTE"]
except KeyError: 
    AUTH_ROUTE = config("AUTH_ROUTE")
    CORE_ROUTE = config("CORE_ROUTE")

nlp_route = APIRouter(
    prefix='/nlp',
    tags=['Nlp polarity prossesing']
)

#Get polarity of phrase 

@nlp_route.post('/')# <- Better Error Messages
def process_phrase(req: PolarityReq, token: str or None = Header(None)):
    r = requests.post(f'{AUTH_ROUTE}/user/proceed', headers={'accept':'application/json', 'Authorization': f"Bearer {token}"})
    if r.status_code == 200:
        proc_out = requests.post(f"{CORE_ROUTE}/phrase/polarity", data=json.dumps({"phrase": req.phrase}))
        return JSONResponse(status_code=200, content=proc_out.json())
    else:
        return JSONResponse(status_code=r.status_code, content=r.json())