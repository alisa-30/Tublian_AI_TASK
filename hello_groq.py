import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

print("Ask a question (or type 'exit' to quit )")
ch = input()
while ch.lower()!="exit":
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": ch,
            }
        ],
        model="llama3-8b-8192",
        temperature=1,
        max_tokens=1024,
    )
    print(chat_completion.choices[0].message.content)
    print("Ask a question (or type 'exit' to quit )")
    ch = input()


