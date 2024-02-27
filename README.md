<div align="center">

# **CORTEX_D** <!-- omit in toc -->

</div>




## Running Validator on testnet

```python
. my-env/bin/activate
```

```python
python neurons/validator.py --subtensor.network test --netuid 18 --wallet.name test_validator --wallet.hotkey default --logging.debug
```

## Running miner on testnet

```python
. my-env/bin/activate
```

```python
python neurons/miner.py --subtensor.network test --netuid 18 --wallet.name test_miner1 --wallet.hotkey default --logging.debug
```