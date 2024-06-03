from utils.corcel import generate_prompt
import pandas as pd
import requests
import json
import time
import requests
import os
from datetime import datetime
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

headers = {
    "X-API-KEY": os.getenv("GO_API_KEY"),
}

def generateMJImage(prompt=""):
    try:
        data = {
            "prompt": prompt,
            "process_mode": "fast"
        }
        response = requests.post("https://api.midjourneyapi.xyz/mj/v2/imagine", headers=headers, data=json.dumps(data))
        print(response.json())
        return response.json()['task_id']
    except Exception as e:
        print("error", e)
        return ""


def fetchImage(taskId, path="temp/midjourney/text2img"):
    fileNames = []
    prompt = ""
    while True:
        # Send a GET request to ID URL
        time.sleep(4)

        fetchUrl = "https://api.midjourneyapi.xyz/mj/v2/fetch"
        data = { "task_id": taskId }
        response = requests.post(fetchUrl, data=json.dumps(data))

        # # Check if the request was successful
        res = response.json()
        if response.status_code == 200:
            if res['status'] == "finished" :

                urls = saveImage(res['task_result']['discord_image_url'], path)
                prompt = res['meta']['task_request']['prompt']
                fileNames = urls
                break
            elif res['status'] == "failed" :
                break
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
            break


    return fileNames, prompt

def saveImage(url, path):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        with open(f"{path}/{timestamp}.png", "wb") as file:
            file.write(res.content)
        
        urls = splitImage(f"{path}/{timestamp}.png", path)
        return urls
    return []

def splitImage(url, path):
    urls = []
    img = Image.open(url)  # Replace with your image path

    # Calculate the width and height of each split
    width, height = img.size
    split_width = width // 2
    split_height = height // 2

    # Split the image into 2x2 grid
    top_left = img.crop((0, 0, split_width, split_height))
    top_right = img.crop((split_width, 0, width, split_height))
    bottom_left = img.crop((0, split_height, split_width, height))
    bottom_right = img.crop((split_width, split_height, width, height))

    # Save each of the split images
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    top_left.save(f"{path}/{timestamp}_1.png")
    top_right.save(f"{path}/{timestamp}_2.png")
    bottom_left.save(f"{path}/{timestamp}_3.png")
    bottom_right.save(f"{path}/{timestamp}_4.png")

    urls.append(f"{path}/{timestamp}_1.png")
    urls.append(f"{path}/{timestamp}_2.png")
    urls.append(f"{path}/{timestamp}_3.png")
    urls.append(f"{path}/{timestamp}_4.png")

    return urls

if __name__ == "__main__":
    prompt = generate_prompt()
    taskId = generateMJImage(prompt[0])
    
    urls, prompt = fetchImage(taskId)
    prompts = [prompt, prompt, prompt, prompt]
    df = pd.DataFrame({
        "image_path": urls,
        "prompt": prompts
    })

    df.to_parquet("temp/1.parquet")


    print(prompt, urls)
