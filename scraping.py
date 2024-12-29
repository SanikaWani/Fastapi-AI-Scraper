import requests
from bs4 import BeautifulSoup
import re
from models import ScrapingOutput

# Function to extract industries based on keywords
def extract_industries(text: str) -> list:
    # Expanded list of industries
    industry_keywords = [
        'software', 'technology', 'finance', 'healthcare', 'marketing', 'e-commerce', 
        'education', 'manufacturing', 'energy', 'retail', 'automotive', 'real estate', 
        'construction', 'telecommunications', 'transportation', 'media', 'government', 
        'non-profit', 'pharmaceutical', 'hospitality', 'food', 'biotechnology', 'consulting'
    ]
    industries_found = []
    for keyword in industry_keywords:
        if keyword in text.lower():
            industries_found.append(keyword.capitalize())
    return industries_found if industries_found else ["Unknown"]

# Function to extract company size based on patterns
def extract_company_size(text: str) -> str:
    # Example patterns for company sizes like "100-500 employees", "Small", etc.
    size_keywords = [
        r"(\d{1,3}-\d{1,3})",  # E.g., "100-500 employees"
        r"(\d{1,3})",           # E.g., "100 employees"
        r"(small|medium|large)", # Keywords like small, medium, large
    ]
    for pattern in size_keywords:
        match = re.search(pattern, text.lower())
        if match:
            return match.group(0).capitalize()
    return "Unknown"

# Function to extract locations based on country names
def extract_locations(text: str) -> list:
    # Expanded list of countries (this list can be modified as needed)
    location_keywords = [
        'usa', 'canada', 'uk', 'india', 'germany', 'france', 'australia', 'japan', 'brazil', 
        'china', 'south korea', 'mexico', 'italy', 'spain', 'russia', 'south africa', 'new zealand',
        'argentina', 'sweden', 'switzerland', 'norway', 'finland', 'netherlands', 'belgium', 'poland', 
        'denmark', 'austria', 'ireland', 'portugal', 'singapore', 'malaysia', 'taiwan', 'thailand',
        'egypt', 'turkey', 'saudi arabia', 'united arab emirates', 'korea', 'colombia', 'chile', 
        'peru', 'vietnam', 'philippines', 'pakistan', 'bangladesh', 'kazakhstan', 'algeria', 'morocco', 
        'romania', 'ukraine', 'serbia', 'croatia', 'latvia', 'lithuania', 'estonia', 'georgia', 'armenia'
    ]
    locations_found = []
    for keyword in location_keywords:
        if keyword in text.lower():
            locations_found.append(keyword.capitalize())
    return locations_found if locations_found else ["Unknown"]

def scrape_homepage(url: str) -> ScrapingOutput:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Invalid Url")
    
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()  # Extract all the text content from the page

    # Dynamically extract values using the helper functions
    industries = extract_industries(text)
    company_size = extract_company_size(text)
    locations = extract_locations(text)

    return ScrapingOutput(industry=', '.join(industries), company_size=company_size, location=', '.join(locations))
