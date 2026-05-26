import os
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv 

load_dotenv()

client = genai.Client()

image = Image.open("../images/cat.jpg")

response = client.models.generate_content_stream(
    model='gemini-2.5-flash',
    contents = [image, "Tell me about this image"],
    config = types.GenerateContentConfig(
        system_instruction = "Response should be in 1000 words, be funny",
        temperature = 0.1
    )
)

for chunk in response:
    print(chunk.text, end="--\n--")

# print("The response is : ")
# print("-------------")
# print("-------------")
# print(response.text)
