from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from dotenv import load_dotenv
from pypdf import PdfReader
import os

# Load environment variables
load_dotenv()

# Initialize Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Initialize FastAPI
app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route
@app.get("/")
def home():
    return {"message": "FastAPI + Groq Backend Running"}

# AI Chat Route
@app.post("/chat")
def chat(data: dict):

    user_message = data.get("message")

    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    ai_response = response.choices[0].message.content

    return {
        "response": ai_response
    }
@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):

    # Save uploaded PDF
    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Extract PDF text
    reader = PdfReader(file_location)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    # AI Prompt
    prompt = f"""
    Analyze this resume for a Python Developer role.

    Give:
    1. ATS Score out of 100
    2. Python skills detected
    3. Missing skills
    4. Strengths
    5. Weaknesses
    6. Suggestions to improve
    7. Suitable job roles

    Resume:
    {resume_text}
    """

    # Groq Response
    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    ai_response = response.choices[0].message.content

    return {
        "analysis": ai_response
    }