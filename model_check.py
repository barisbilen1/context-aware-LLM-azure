
from openai import AzureOpenAI

client = AzureOpenAI(azure_endpoint="endpoint_url",
api_version="2023-05-15",
api_key="api_key")

models = client.models.list()

for model in models:
    print(model)
