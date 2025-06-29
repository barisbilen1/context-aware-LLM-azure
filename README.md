# What is it?
Building a "context-aware" chat model using Azure OpenAI service. My application can take a local pdf as an input from the user, and can answer questions based on the file provided. Takes 5 min to deploy if your models (chat model and embedding model) and API endpoint are ready.

# How to use it?
1) Create a virtual environment and install the dependencies in requirements.txt
2) Enter the path to your file that you want to enrich your chat model with, in config.yml.
3) Enter the deployment names of your models as well as the endpoints and API keys in conn_config.yml, and run the prompt.py in terminal, and enter your question. You will get your answer based on the file you provided, so, the chatgpt model is so-called context-aware.

Did not explore this further as there are many solutions available for this in the market already, but it has been a good learning for me.
