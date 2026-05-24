import os
from google import genai

client = genai.Client()

prompt = input("Enter Your Prompt : ")
# Check and use a current model (e.g., gemini-2.5-flash)
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents = prompt
)
print("The response is : ")
print("-------------")
print("-------------")
print(response.text)
