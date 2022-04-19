import json
import os
import requests

from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from decouple import config
from application.models.UserRouteModels import CreateUser, UserRead, UpdateUser, LoginUser

user_route = APIRouter(
    prefix='/user',
    tags=['User operations']
)

try:
    AUTH_ROUTE = os.environ["AUTH_ROUTE"]
except KeyError:
    AUTH_ROUTE = config("AUTH_ROUTE")

#Create user

@user_route.post('/create')
def create_new_user(user_req: CreateUser):
    payload = json.dumps(
        {
            "user_name": user_req.user_name, 
            "user_email": user_req.user_email,
            "user_password": user_req.user_password
        }
    )
    
    r = requests.post(f'{AUTH_ROUTE}/user/create', data=payload)
    
    return JSONResponse(status_code=r.status_code, content=r.json())

#Read logged user

@user_route.get('/', response_model=UserRead or None)
def read_user(token: str or None = Header(None)):
    r = requests.get(f'{AUTH_ROUTE}/user/', headers={'accept':'application/json', 'Authorization': f"Bearer {token}"})
    return JSONResponse(status_code=r.status_code, content=r.json())

#Update logged user

@user_route.put('/change')
def update_user(user_input: UpdateUser, token: str or None = Header(None)):
    payload = json.dumps({
        "field": user_input.field,
        "value": user_input.value
    })
    
    r = requests.put(f'{AUTH_ROUTE}/user/edit', data=payload, headers={'accept':'application/json', 'Authorization': f"Bearer {token}"})
    return JSONResponse(status_code=r.status_code, content=r.json())

#Delete logged user

@user_route.get('/delete')
def delete_user(token: str or None = Header(None)): #<- O frontend deve fazer a verificação se o desejo do usuário é realmente deletar e então deletar
    r = requests.get(f'{AUTH_ROUTE}/user/delete',headers={'accept':'application/json', 'Authorization': f"Bearer {token}"})
    return JSONResponse(status_code=r.status_code, content=r.json())
    
#Create Api_key for user    

@user_route.get('/getkey')
def generate_apikey(token: str or None = Header(None)):
    r = requests.get(f'{AUTH_ROUTE}/user/keys',headers={'accept':'application/json', 'Authorization': f"Bearer {token}"})
    return JSONResponse(status_code=r.status_code, content=r.json())

# login
@user_route.post('/login')
def login_user(user_input: LoginUser):
    payload = json.dumps({
        "useremail": user_input.useremail,
        "password": user_input.password
    })
    
    r = requests.post(f'{AUTH_ROUTE}/security/login', data=payload)
    return JSONResponse(status_code=r.status_code, content=r.json())