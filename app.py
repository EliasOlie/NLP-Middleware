from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from application.routes.nlp_polarity_router import nlp_route
from application.routes.user_router import user_route

origins = [
    '*'
]

app = FastAPI()
app.include_router(nlp_route)
app.include_router(user_route)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def say_hi():
    return {"Message": "This is the landing page, for routes overview check out /docs"}