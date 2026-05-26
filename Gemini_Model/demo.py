import os
from google import genai
from dotenv import load_dotenv 

load_dotenv()

client = genai.Client()

prompt = input("Enter Your Prompt : ")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents = prompt
)
print("The response is : ")
print("-------------")
print("-------------")
print(response.text)
