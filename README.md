Building a "context-aware" chat model using Azure OpenAI service. My application can take a local pdf as an input from the user, and can answer questions based on the file provided. Takes 5 min to deploy if your models (chat model and embedding model) and API endpoint are ready.

How to use:
1) Create a virtual environment and install the dependencies in requirements.txt
2) Enter the path to your file that you want to enrich your chat model with, and run it to produce output.txt which is the string representation of the pdf file.
3) Enter the deployment names of your models to line 13 and 68 in prompt.py (also the endpoints and API key), and run the prompt.py in terminal, and enter your prompt. You will get your answer based on the file you provided, so, the chatgpt model is so-called context-aware.

Did not explore this further as there are many solutions available for this in the market already, but it has been a good learning for me.