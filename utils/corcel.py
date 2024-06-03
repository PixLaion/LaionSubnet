import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.corcel.io/cortext/text"

def generate_prompt(content="Generate a short prompt for realistic image", num_prompts=1):
    payload = {
        "model": "cortext-ultra",
        "stream": False,
        "miners_to_query": num_prompts,
        "top_k_miners_to_query": 40,
        "ensure_responses": True,
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": os.getenv("CORCEL_TOKEN")
    }

    response = requests.post(url, json=payload, headers=headers)

    response_list = json.loads(response.text)
    # Extracting list of choices/delta/content string from the data
    choices_content_list = [choice['delta']['content'] for item in response_list for choice in item['choices']]
    ans = []
    for item in choices_content_list:
        prompt = item[1:-1]
        ans.append(prompt)
    return ans

