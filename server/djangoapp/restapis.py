# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"
    
    request_url = backend_url+endpoint+"?"+params

    print(f"GET FROM {request_url}")

    try:
        response = requests.get(request_url)
        return response.json()
    except:
        print("Network error occurred")
    

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    
    try:
        response = sentiment_analyzer_url+"analyze/"+text

        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurrede")

# Add code for retrieving sentiments

# post review helper function
def post_review(data_dict):
    request_url = backend_url + "/insert_review"

    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())

        return response.json()
    except:
        print("Network Exception")
        return {"status": 502, "message": "Connection lost"}
