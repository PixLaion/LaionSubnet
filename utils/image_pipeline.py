import requests
import json
import time
import requests
from datetime import datetime

headers = {
    "API-Key": "eZFxj03s17QvKowQWb0Luo6kG85yq2vMr32lRTL1K8gJ5qk8OeoRgZNOevuiholE"
}

def generateSDImage(prompt="photo of a man", samples=1) : 
    data = {
        "model_id":  "sd1.5",
        "prompt": prompt,
        "negative_prompt": "error, cropped, worst quality, low quality, duplicate, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, blurry, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck",
        "num_inference_steps": 30,
        "refiner": False,
        "samples": samples,
        "guidance_scale": 7.5,
        "width": 512,
        "height": 512,
        "seed": 12345,
        "safety_checker": True
    }

    response = requests.post("https://api.imagepipeline.io/sd/text2image/v1", headers=headers, data=json.dumps(data))
    statusUrl = "https://api.imagepipeline.io/sd/text2image/v1/status/" + response.json()['id']
    fns = saveImagePipleline(statusUrl)

    return fns

def generateSDXLImage(prompt="", samples=1) : 
    data = {
        "model_id":  "d961a274-658c-4889-8c1a-bf85416cb1c1",
        "prompt": prompt,
        "negative_prompt": "error, cropped, worst quality, low quality, duplicate, bad proportions, incomplete subject",
        "num_inference_steps": 30,
        "refiner": True,
        "samples": samples,
        "guidance_scale": 7.5,
        "width": 768,
        "height": 768,
        "safety_checker": True,
        "seed": 12345,
    }

    response = requests.post("https://api.imagepipeline.io/sdxl/text2image/v1", headers=headers, data=json.dumps(data))
    statusUrl = "https://api.imagepipeline.io/sdxl/text2image/v1/status/" + response.json()['id']
    fns = getUrls(statusUrl)

    return fns

def getUrls(statusUrl):
    while True:
        # Send a GET request to ID URL
        response = requests.get(statusUrl, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            if response.json()['status'] == "SUCCESS" :
                return response.json()['download_urls']
                break
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
            break

        time.sleep(1)

    return []

def saveImagePipleline(statusUrl):
    fileNames = []
    while True:
        # Send a GET request to ID URL
        response = requests.get(statusUrl, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            if response.json()['status'] == "SUCCESS" :
            # Open a file in binary write mode
                files = response.json()['download_urls']
                for i, image in enumerate(files):
                    res = requests.get(image, headers=headers)
                    if res.status_code == 200:
                        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                        with open(f"{timestamp}_{i}.png", "wb") as file:
                            file.write(res.content)
                        fileNames.append(image)
                break
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
            break

        time.sleep(1)

    return fileNames

# generate 4 images using SD1.5
# generateSDImage(
#     prompt="woman wearing traditional Russian clothes, forest in the background, photorealistic, 8k quality",
#     samples=4)

# generate 4 images using SDXL
# urls = generateSDXLImage(
#     prompt="woman wearing traditional Russian clothes, forest in the background, photorealistic, 8k quality",
#     samples=4)

# print(urls)