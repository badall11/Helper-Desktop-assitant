from openai import OpenAI

client = OpenAI(
    api_key = "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"
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a helpful assistant skilled in general tasks like alexa and google cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# ✅ Print the AI's reply
print(completion.choices[0].message.content)