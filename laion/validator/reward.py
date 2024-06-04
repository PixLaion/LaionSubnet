# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import torch
import bittensor as bt
from typing import List
from utils.midjourney import fetchImage
from utils.hf_dataset import upload_datasets
from constants import ORIGINAL_COMPETITION_ID

def reward(query: str, response: List[str]) -> float:
    """
    Reward the miner response to the dummy request. This method returns a reward
    value for the miner, which is used to update the miner's score.

    Returns:
    - float: The reward value for the miner.
    """
    score = 0
    prompt = None
    urls = []
    discordUrl = ""

    print(f"query {ORIGINAL_COMPETITION_ID}")
    if query == ORIGINAL_COMPETITION_ID:
        taskId = response['taskId']

        if taskId == None: 
            return score, prompt, urls
        
        urls, prompt, discordUrl = fetchImage(taskId)

        bt.logging.info(f"{taskId} downloaded for {urls}")
        score = 1.0 if prompt == response['prompt'] else 0

    return score, prompt, urls, discordUrl


def get_rewards(
    self,
    query: str,
    responses
) -> torch.FloatTensor:
    """
    Returns a tensor of rewards for the given query and responses.

    Args:
    - query (int): The query sent to the miner.
    - responses (List[float]): A list of responses from the miner.

    Returns:
    - torch.FloatTensor: A tensor of rewards for the given query and responses.
    """
    # Get all the reward results by iteratively calling your reward() function.
    imageUrls = []
    prompts = []
    scores = []
    discordUrls = []
    indexes = []

    for response in responses:
        score, prompt, urls, discordUrl = reward(query, response)
        i = 1
        scores.append(score)
        for url in urls:
            prompts.append(prompt)
            discordUrls.append(discordUrl)
            imageUrls.append(url)
            indexes.append(i)
            i += 1

    upload_datasets(imageUrls, prompts, discordUrls, indexes)

    return torch.FloatTensor(scores).to(self.device)
