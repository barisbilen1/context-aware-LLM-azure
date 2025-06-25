from openai import AzureOpenAI
from numpy import dot
from numpy.linalg import norm
import numpy as np

client = AzureOpenAI(azure_endpoint="endpoint_url",
api_version="2024-02-15-preview",
api_key="api_key")

# Configure your Azure OpenAI credentials

# Your embedding model deployment name
embedding_model = "text-embedding-ada-002"  # Change to your deployment name

# Read the text from output.txt (your resume)
with open("output.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

# Get embedding from Azure OpenAI
response = client.embeddings.create(input=resume_text,
                                model=embedding_model)

# Extract the embedding vector
resume_embedding = response.data[0].embedding

# Print embedding (optional — this is a long array of numbers)
print(f"Embedding generated! Vector length: {len(resume_embedding)}")

### Embedding completed, now provide it along with the prompt to the model

#
# === Take a User Question ===
question = input("\nAsk a question about your resume: ")

# Create embedding for the question
question_response = client.embeddings.create(
    input=question,
    model=embedding_model
)
question_embedding = question_response.data[0].embedding


# === Cosine Similarity Function ===
def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))


# Compute similarity
similarity = cosine_similarity(np.array(question_embedding), np.array(resume_embedding))
print(f"\nSimilarity Score: {similarity:.4f}")


# === If Similar, Ask GPT ===
if similarity > 0.6:
    print("✅ Question is relevant to the resume. Asking GPT...\n")

    messages = [
        {
            "role": "system",
            "content": "You are an assistant that answers questions based on the user's resume. Only use the resume provided to answer questions."
        },
        {
            "role": "user",
            "content": f"Resume:\n{resume_text}\n\nQuestion:\n{question}"
        }
    ]

    chat_model = "o4-mini-baris"  # Your chat deployment name

    # had to create another client because o4-mini is not supported in westeurope region.
    client2 = AzureOpenAI(azure_endpoint="endpoint_url",
   api_version="2024-12-01-preview",
   api_key="api_key")


    chat_response = client2.chat.completions.create(
        model=chat_model,
        messages=messages,
        temperature=1
    )

    answer = chat_response.choices[0].message.content
    print(f"💡 GPT Answer: {answer}")

else:
    print("Question is not relevant enough to the resume based on similarity.")




# where did this guy study? in which country and continent?