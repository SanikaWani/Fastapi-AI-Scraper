from pydantic import BaseModel, HttpUrl

class ScrapingInput(BaseModel):
    url: HttpUrl

class ScrapingOutput(BaseModel):
    industry: str
    company_size: str
    location: str
