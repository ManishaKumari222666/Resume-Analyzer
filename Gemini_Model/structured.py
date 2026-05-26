from google import genai
from pydantic import BaseModel
from enum import Enum

class Rating(Enum):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"

class TouristPlaces(BaseModel):
    name: str
    description: str
    rating: Rating

client = genai.Client()

prompt = "List a few of the most popular tourist attractions in India."

response = client.models.generate_content(
    model='gemini-2.5-flash',   
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[TouristPlaces]
    }
)
print(response.text)