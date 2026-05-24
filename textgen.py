import os
from google import genai
from google.genai import types

# Set your API key in your environment
# os.environ["GEMINI_API_KEY"] = "AIzaSyB6Edcu0fXb3B2gyzuGOGvpd9LGS0mM7gc"

client = genai.Client()

prompt = input("Enter Your Prompt : ")
# Check and use a current model (e.g., gemini-2.5-flash)
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents = prompt,
    config = types.GenerateContentConfig(
        system_instruction = "Do not think about Football, your response should be within 50 words",
        temperature = 0.2
    )
)
print("The response is : ")
print("-------------")
print("-------------")
print(response.text)
