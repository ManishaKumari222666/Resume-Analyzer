from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")

print("Chat Starts Here : type 'endchat' to end the chat")
userInput = input("User : ")

while userInput != "endchat":
    response = chat.send_message(userInput)
    print("Bot : ", response.text)
    userInput = input("User : ")
    