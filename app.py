from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from auth import is_authenticated, login_user, logout_user, authenticate_key
from scraping import scrape_homepage
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Add the session middleware
app.add_middleware(SessionMiddleware, secret_key=os.getenv('SECRET_KEY'))

templates = Jinja2Templates(directory="templates")

# GET endpoint to render the HTML form
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    authenticated = is_authenticated(request)  # Check if user is authenticated
    return templates.TemplateResponse("index.html", {
        "request": request,
        "authenticated": authenticated,
        "message": "Please authenticate first." if not authenticated else None,
        "result": None
    })

# POST endpoint to authenticate using secret key
@app.post("/authenticate", response_class=HTMLResponse)
async def authenticate(request: Request, secret_key: str = Form(...)):
    try:
        authenticate_key(secret_key)  # This function checks the secret key
        login_user(request)  # Mark the user as authenticated
        return templates.TemplateResponse("index.html", {
            "request": request,
            "authenticated": True,  # User is now authenticated
            "message": "Authentication successful!",
            "result": None
        })
    except HTTPException as e:
        # Pass the exception to the response to handle 401 Unauthorized
        raise e
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "authenticated": False,
            "message": f"Unexpected error: {str(e)}",
            "result": None
        })

# POST endpoint to scrape the website using the input URL
@app.post("/scrape", response_class=HTMLResponse)
async def scrape_website(request: Request, url: str = Form(...)):
    if not is_authenticated(request):
        raise HTTPException(status_code=401, detail="Unauthorized access")

    try:
        # Perform scraping
        result = scrape_homepage(url)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "authenticated": True,
            "message": "Scraping successful!",
            "result": result
        })
    except ValueError as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "authenticated": True,
            "message": f"Scraping error: {str(e)}",
            "result": None
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "authenticated": True,
            "message": f"Unexpected error: {str(e)}",
            "result": None
        })

# Endpoint to log out the user
@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    logout_user(request)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "authenticated": False,
        "message": "Logged out successfully.",
        "result": None
    })
