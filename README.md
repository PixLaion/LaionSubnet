<div align="center">

# **Bittensor PixLaion**
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

</div>

## Introduction

**Bittensor PixLaion:** Creating High-Quality Image Datasets with Midjourney API on Hugging Face

Welcome to PixLaion, an innovative tool hosted on the Bittensor network, designed to facilitate the creation of image datasets using the Midjourney API. This tool is perfect for machine learning practitioners, data scientists, and AI enthusiasts who require large, categorized image datasets for model training and analysis.

### Key Features

- **Automated Dataset Generation:** Utilizes the Midjourney API to generate and categorize images based on prompts.
- **High-Quality Images:** Produces datasets with high-resolution images suitable for various AI applications.
- **Prompt Customization:** Allows for dynamic prompt updates to refine categories and improve dataset quality.
- **Scalability:** Capable of storing millions of images, enabling extensive model training.
- **Integration with Hugging Face:** Seamlessly uploads datasets to Hugging Face for easy access and sharing.

### Advantages

- **Rapid Dataset Creation:** Quickly assembles vast image datasets with prompts, significantly reducing the time required for manual compilation.
- **Custom Categorization:** Easily creates categories by updating the prompt generator on the validator, enhancing dataset organization.
- **Decentralized Infrastructure:** Leverages the Bittensor network for robust and reliable dataset generation and storage.
- **Community Engagement:** Engages with the community through real-time monitoring channels and applications for continuous improvement and support.

---

## Installation

**Requirements:** Python 3.10.12 or higher

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pixlaion.git
   ```
2. Install the requirements:
   ```
   cd pixlaion
   python -m pip install -r requirements.txt
   python -m pip install -e .
   ```

---

## Preparing Your Environment

Before running a miner or validator, ensure to:

- [Create an account and purchase an API key on goapi.ai](https://goapi.ai).

### Environment Variables Configuration

For setting up the necessary environment variables for your miner or validator, please refer to the [Environment Variables Guide](./docs/env_variables.md).

## Running the Miner

  ```
  python -m neurons/miners/miner.py 
      --netuid 25
      --subtensor.network finney
      --wallet.name <your miner wallet>
      --wallet.hotkey <your validator hotkey>
      --axon.port 14000
  ```

## Running the Validator API with Automatic Updates

These validators are designed to run and update themselves automatically. To run a validator, follow these steps:

1. Install this repository, you can do so by following the steps outlined in [the installation section](#installation).
2. Configure your API key from goapi.ai in the environment settings.
3. Follow the instructions in the [Validator Setup Guide](./docs/running_a_validator.md) to start your validator.

### Detailed Setup Instructions

For step-by-step guidance on setting up and running a miner, validator, or operating on the testnet or mainnet, refer to the following guides:
- [Miner Setup](./docs/running_a_miner.md)
- [Validator Setup](./docs/running_a_validator.md)
- [Testnet Operations](./docs/running_on_testnet.md)
- [Mainnet Operations](./docs/running_on_mainnet.md)
- [Using the Image Datasets](https://pixlaion.ai/howtouse)
- [Roadmap](https://pixlaion.ai/roadmap)

---

## Real-time Datasets Monitoring

Stay updated with the progress of dataset generation and access the latest datasets through our monitoring channels:

- [Discord Channel](https://discord.gg/yourdiscordlink)
- [PixLaion Datasets](https://pixlaion.ai/datasets)

</div>
