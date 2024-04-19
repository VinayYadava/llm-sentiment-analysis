import requests
from utils import load_config
import sys

config=load_config()
URL="https://api.openai.com/v1/completions"
MAX_TOKEN=50
LLM_API_KEY=""
LLM_PROVIDER="openai"
MODEL_NAME=""
supported_llms=["openai"]
prompt="Why are you awesome?"

if LLM_PROVIDER not in supported_llms:
    print(f"kindly choose valid llm supported from \n{supported_llms}.")
    sys.exit()

if LLM_PROVIDER=='openai':
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {LLM_API_KEY}"
    }


payload = {
    "prompt":prompt,
    "max_token":MAX_TOKEN,
    "model":MODEL_NAME
}

response = requests.post(
    url=URL,
    headers=headers,
    json=payload
    )


generated_response = response.json()["choices"][0]["text"].strip()

print(generated_response)