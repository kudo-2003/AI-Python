from openai import OpenAI
import os
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the FIFA World Cup in 1998?"}
    ]
)

print(completion.choices[0].message)