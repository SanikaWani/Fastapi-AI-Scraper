from fastapi import Request, HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('SECRET_KEY')

def authenticate_key(secret_key: str):
    if secret_key != key:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid secret key")

def is_authenticated(request: Request) -> bool:
    return request.session.get("authenticated", False)

def login_user(request: Request):
    request.session["authenticated"] = True

def logout_user(request: Request):
    request.session.clear()