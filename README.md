# FastAPI Web Scraping Application

## **Overview**

This project is a **FastAPI-based web application** that provides functionality for authenticating users and performing web scraping on a provided URL. The application extracts details such as **industry**, **company size**, and **location** from the website's homepage. A simple web interface is used for input and output, and the application ensures secure session management.

### **Features**

- **User Authentication**: Users must authenticate using a secret key before accessing the scraping functionality.
- **Web Scraping**: Extract industry, company size, and location details from a provided URL.
- **Session Management**: Sessions are managed securely using `SessionMiddleware`.
- **Error Handling**: Provides detailed error messages for authentication, scraping, and invalid inputs.

---

## **Prerequisites**

Ensure the following are installed on your system before running the application:

- Python 3.8 or later
- Pip (Python package manager)

---

## **Installation**

### **Step 1: Clone the Repository**

```bash
git clone <repository_url>
cd <repository_name>
```

### **Step 2: Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Set Up Environment Variables**

Create a `.env` file in the root directory and add the following:

```
SECRET_KEY=your_secret_key_here
```

---

## **Usage**

### **Step 1: Run the Application**

```bash
uvicorn app:app --reload
```

### **Step 2: Access the Application**

Open your web browser and navigate to:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **How to Use the Application**

### **1. Authentication**

- Enter your **secret key** to authenticate.
- After successful authentication, you will see a form to input a URL for scraping.

### **2. Web Scraping**

- Enter the **URL** of the website you want to scrape.
- Click "Submit" to view the extracted **industry**, **company size**, and **location** details.

### **3. Logout**

- Click the **logout button** to end your session and clear the authentication.

---

## **Project Structure**

```plaintext
.
├── app.py              # Main FastAPI application
├── auth.py             # Authentication and session management
├── scraping.py         # Web scraping logic
├── models.py           # Data models for input and output validation
├── requirements.txt    # Python dependencies
├── templates/          # Jinja2 HTML templates
│   └── index.html      # Main HTML template
└── .env                # Environment variables
```

---

## **API Endpoints**

### **1. `GET /`**

- Renders the main HTML form.
- If the user is not authenticated, prompts for authentication.

### **2. `POST /authenticate`**

- Authenticates the user using the provided secret key.

**Request Body**:

- `secret_key` (form data): The secret key for authentication.

**Responses**:

- `200 OK`: Successful authentication.
- `401 Unauthorized`: Invalid secret key.

### **3. `POST /scrape`**

- Scrapes the provided URL for **industry**, **company size**, and **location** details.

**Request Body**:

- `url` (form data): The URL to scrape.

**Responses**:

- `200 OK`: Returns the scraping results.
- `401 Unauthorized`: User not authenticated.
- `400 Bad Request`: Invalid URL or scraping failed.

### **4. `GET /logout`**

- Logs out the user and clears the session.

**Responses**:

- `200 OK`: Successfully logged out.

---

## **Error Handling**

- `401 Unauthorized`: Occurs when an unauthenticated user attempts to access protected endpoints.
- `400 Bad Request`: Triggered if an invalid URL is provided.
- `500 Internal Server Error`: Captures unexpected errors during scraping or authentication.

---

## **Built With**

- **FastAPI**: Web framework for building APIs.
- **Jinja2**: Templating engine for rendering HTML.
- **Requests**: Library for making HTTP requests.
- **BeautifulSoup**: Library for web scraping.
- **Pydantic**: Data validation and parsing.
