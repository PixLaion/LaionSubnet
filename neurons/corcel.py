import requests
import json
url = "https://api.corcel.io/cortext/text"

def generate_prompt(num_prompts=1):
    payload = {
        "model": "cortext-ultra",
        "stream": False,
        "miners_to_query": num_prompts,
        "top_k_miners_to_query": 40,
        "ensure_responses": True,
        "messages": [
            {
                "role": "user",
                "content": "Generate prompt to generate image related food."
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "095148c1-6cc9-4221-b37d-acd01a44"
    }

    response = requests.post(url, json=payload, headers=headers)

    response_list = json.loads(response.text)
    # Extracting list of choices/delta/content string from the data
    choices_content_list = [choice['delta']['content'] for item in response_list for choice in item['choices']]
    return choices_content_list

