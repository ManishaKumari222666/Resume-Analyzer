from google import genai

client = genai.Client()

print("Chat Starts Here : type 'endchat' to end the chat")
chat_history = []
userInput = input("User : ")

while userInput != "endchat":
    chat_history.append("userInput: " + userInput)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents = chat_history,
        config = genai.types.GenerateContentConfig(
            system_instruction = "answer should be in 10 words",
            temperature = 0.1
        )
    )
    chat_history.append("Bot: " + response.text)
    print("Bot : ", response.text)
    userInput = input("User : ")