from huggingface_hub import HfApi, HfFolder, upload_file

from datasets import Dataset, DatasetDict
from PIL import Image
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import os
import io
from utils.midjourney import load_image

load_dotenv()

api = HfApi()
token = os.getenv("HF_ACCESS_TOKEN")
HfFolder.save_token(token)

def upload_datasets(imageUrls, prompts, discordUrls, indexes):
    df = pd.DataFrame({
        "discordUrl": discordUrls,
        "prompt": prompts,
        "image_path": imageUrls,
        "indexes": indexes
    })
    
    df['image'] = df['image_path'].apply(load_image)

    current_timestamp = datetime.now()
    timestamp_string = current_timestamp.strftime("%Y%m%d%H%M%S")
    df.to_parquet(f"temp/{timestamp_string}.parquet")

    upload_file(
        path_or_fileobj=f"temp/{timestamp_string}.parquet",
        path_in_repo=f"{timestamp_string}.parquet",
        repo_id="PixLaion/test_dataset",
        token=token,
        repo_type="dataset"
    )

if __name__ == "__main__":
    upload_datasets(["asdf"], ["test"])