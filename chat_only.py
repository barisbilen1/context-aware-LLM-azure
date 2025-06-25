from openai import AzureOpenAI

# === Azure OpenAI Client Setup ===
client = AzureOpenAI(azure_endpoint="endpoint_url",
api_version="2024-12-01-preview",
api_key="api_key")

# === Chat Loop ===
chat_history = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chat ended.")
        break

    chat_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="o4-mini-baris",  # Replace with your exact deployment name
            messages=chat_history,
            temperature=1
        )

        reply = response.choices[0].message.content
        print(f"AI: {reply}")

        chat_history.append({"role": "assistant", "content": reply})

    except Exception as e:
        print(f"Error: {e}")
        break
