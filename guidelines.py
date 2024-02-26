import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.apikey = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

print("Qual a sua pergunta para o ChatGPT?")
question = input("Pergunta: ")

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": f"{question}"},
    ]
)

result = response.choices[0].message.content

print(f"Perguntamos ao ChatGPT: {question}")
print(f"Aqui está sua resposta: {result}")