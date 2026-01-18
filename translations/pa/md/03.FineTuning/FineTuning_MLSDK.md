<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:16:40+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "pa"
}
-->
## Azure ML ਸਿਸਟਮ ਰਜਿਸਟਰੀ ਤੋਂ chat-completion ਕੰਪੋਨੈਂਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਡਲ ਨੂੰ ਫਾਈਨ ਟਿਊਨ ਕਰਨ ਦਾ ਤਰੀਕਾ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਅਸੀਂ Phi-3-mini-4k-instruct ਮਾਡਲ ਦੀ ਫਾਈਨ ਟਿਊਨਿੰਗ ਕਰਾਂਗੇ ਤਾਂ ਜੋ ultrachat_200k ਡੇਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ 2 ਲੋਕਾਂ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਪੂਰੀ ਕੀਤੀ ਜਾ ਸਕੇ।

![MLFineTune](../../../../translated_images/pa/MLFineTune.928d4c6b3767dd35.webp)

ਇਹ ਉਦਾਹਰਨ ਤੁਹਾਨੂੰ ਦਿਖਾਏਗੀ ਕਿ ਕਿਵੇਂ Azure ML SDK ਅਤੇ Python ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ ਟਿਊਨਿੰਗ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ ਅਤੇ ਫਿਰ ਫਾਈਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਰੀਅਲ ਟਾਈਮ ਇੰਫਰੈਂਸ ਲਈ ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ‘ਤੇ ਡਿਪਲੋਇ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

### ਟ੍ਰੇਨਿੰਗ ਡੇਟਾ

ਅਸੀਂ ultrachat_200k ਡੇਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ। ਇਹ UltraChat ਡੇਟਾਸੈੱਟ ਦਾ ਬਹੁਤ ਹੀ ਫਿਲਟਰ ਕੀਤਾ ਹੋਇਆ ਵਰਜਨ ਹੈ ਅਤੇ ਇਸਨੂੰ Zephyr-7B-β, ਇੱਕ ਅਧੁਨਿਕ 7b ਚੈਟ ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਲਈ ਵਰਤਿਆ ਗਿਆ ਸੀ।

### ਮਾਡਲ

ਅਸੀਂ Phi-3-mini-4k-instruct ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ ਤਾਂ ਜੋ ਦਿਖਾਇਆ ਜਾ ਸਕੇ ਕਿ ਕਿਸ ਤਰ੍ਹਾਂ ਯੂਜ਼ਰ ਚੈਟ-ਕੰਪਲੀਸ਼ਨ ਟਾਸਕ ਲਈ ਮਾਡਲ ਨੂੰ ਫਾਈਨ ਟਿਊਨ ਕਰ ਸਕਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਇਹ ਨੋਟਬੁੱਕ ਕਿਸੇ ਖਾਸ ਮਾਡਲ ਕਾਰਡ ਤੋਂ ਖੋਲ੍ਹਿਆ ਹੈ, ਤਾਂ ਉਸ ਖਾਸ ਮਾਡਲ ਦਾ ਨਾਮ ਬਦਲਣਾ ਯਾਦ ਰੱਖੋ।

### ਟਾਸਕ

- ਫਾਈਨ ਟਿਊਨ ਕਰਨ ਲਈ ਮਾਡਲ ਚੁਣੋ।
- ਟ੍ਰੇਨਿੰਗ ਡੇਟਾ ਚੁਣੋ ਅਤੇ ਖੋਜੋ।
- ਫਾਈਨ ਟਿਊਨਿੰਗ ਜੌਬ ਨੂੰ ਕਨਫਿਗਰ ਕਰੋ।
- ਫਾਈਨ ਟਿਊਨਿੰਗ ਜੌਬ ਚਲਾਓ।
- ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਮੁਲਾਂਕਣ ਮੈਟ੍ਰਿਕਸ ਦੀ ਸਮੀਖਿਆ ਕਰੋ।
- ਫਾਈਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਰਜਿਸਟਰ ਕਰੋ।
- ਫਾਈਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਰੀਅਲ ਟਾਈਮ ਇੰਫਰੈਂਸ ਲਈ ਡਿਪਲੋਇ ਕਰੋ।
- ਸਰੋਤ ਸਾਫ਼ ਕਰੋ।

## 1. ਪਹਿਲਾਂ ਦੀਆਂ ਲੋੜਾਂ ਸੈੱਟ ਕਰੋ

- ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ
- AzureML ਵਰਕਸਪੇਸ ਨਾਲ ਕਨੈਕਟ ਕਰੋ। SDK ਪ੍ਰਮਾਣਿਕਤਾ ਸੈੱਟਅਪ ਬਾਰੇ ਹੋਰ ਜਾਣੋ। ਹੇਠਾਂ <WORKSPACE_NAME>, <RESOURCE_GROUP> ਅਤੇ <SUBSCRIPTION_ID> ਨੂੰ ਬਦਲੋ।
- azureml ਸਿਸਟਮ ਰਜਿਸਟਰੀ ਨਾਲ ਕਨੈਕਟ ਕਰੋ
- ਇੱਕ ਵਿਕਲਪਿਕ ਐਕਸਪੇਰੀਮੈਂਟ ਨਾਮ ਸੈੱਟ ਕਰੋ
- ਕਮਪਿਊਟ ਚੈੱਕ ਕਰੋ ਜਾਂ ਬਣਾਓ।

> [!NOTE]
> ਲੋੜ ਹੈ ਕਿ ਇੱਕ ਸਿੰਗਲ GPU ਨੋਡ ਵਿੱਚ ਕਈ GPU ਕਾਰਡ ਹੋ ਸਕਦੇ ਹਨ। ਉਦਾਹਰਨ ਵਜੋਂ, Standard_NC24rs_v3 ਦੇ ਇੱਕ ਨੋਡ ਵਿੱਚ 4 NVIDIA V100 GPUs ਹਨ ਜਦਕਿ Standard_NC12s_v3 ਵਿੱਚ 2 NVIDIA V100 GPUs ਹਨ। ਇਸ ਜਾਣਕਾਰੀ ਲਈ ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਵੇਖੋ। ਪ੍ਰਤੀ ਨੋਡ GPU ਕਾਰਡ ਦੀ ਗਿਣਤੀ ਹੇਠਾਂ ਦਿੱਤੇ ਗਏ param gpus_per_node ਵਿੱਚ ਸੈੱਟ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਮੁੱਲ ਨੂੰ ਠੀਕ ਸੈੱਟ ਕਰਨ ਨਾਲ ਨੋਡ ਵਿੱਚ ਸਾਰੇ GPUs ਦੀ ਵਰਤੋਂ ਯਕੀਨੀ ਬਣੇਗੀ। ਸਿਫਾਰਸ਼ੀ GPU ਕਮਪਿਊਟ SKUs ਇੱਥੇ ਅਤੇ ਇੱਥੇ ਮਿਲ ਸਕਦੇ ਹਨ।

### Python ਲਾਇਬ੍ਰੇਰੀਜ਼

ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਚਲਾਕੇ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ। ਨਵੇਂ ਵਾਤਾਵਰਣ ਵਿੱਚ ਚਲਾਉਂਦੇ ਸਮੇਂ ਇਹ ਵਿਕਲਪਿਕ ਕਦਮ ਨਹੀਂ ਹੈ।

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure Machine Learning (Azure ML) ਸੇਵਾ ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਨ ਲਈ ਹੈ। ਇਹ ਕੀ ਕਰਦਾ ਹੈ, ਇਸ ਦਾ ਵੇਰਵਾ:

    - ਇਹ azure.ai.ml, azure.identity, ਅਤੇ azure.ai.ml.entities ਪੈਕੇਜਾਂ ਤੋਂ ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ। ਨਾਲ ਹੀ time ਮੋਡੀਊਲ ਵੀ।

    - ਇਹ DefaultAzureCredential() ਨਾਲ ਪ੍ਰਮਾਣਿਕਤਾ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ, ਜੋ Azure ਕਲਾਉਡ ਵਿੱਚ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਵਿਕਸਿਤ ਕਰਨ ਲਈ ਸਧਾਰਣ ਪ੍ਰਮਾਣਿਕਤਾ ਅਨੁਭਵ ਦਿੰਦਾ ਹੈ। ਜੇ ਇਹ ਫੇਲ੍ਹ ਹੋ ਜਾਵੇ, ਤਾਂ InteractiveBrowserCredential() ਨਾਲ ਇੰਟਰਐਕਟਿਵ ਲੌਗਿਨ ਪ੍ਰੰਪਟ ਦਿੰਦਾ ਹੈ।

    - ਫਿਰ ਇਹ from_config ਮੈਥਡ ਨਾਲ MLClient ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ, ਜੋ ਡਿਫਾਲਟ ਕਨਫਿਗ ਫਾਈਲ (config.json) ਤੋਂ ਕਨਫਿਗਰੇਸ਼ਨ ਪੜ੍ਹਦਾ ਹੈ। ਜੇ ਇਹ ਫੇਲ੍ਹ ਹੋ ਜਾਵੇ, ਤਾਂ subscription_id, resource_group_name, ਅਤੇ workspace_name ਹੱਥੋਂ ਦੇ ਕੇ MLClient ਬਣਾਉਂਦਾ ਹੈ।

    - ਇਹ ਇੱਕ ਹੋਰ MLClient ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ, ਜੋ Azure ML ਰਜਿਸਟਰੀ "azureml" ਲਈ ਹੈ। ਇਹ ਰਜਿਸਟਰੀ ਮਾਡਲ, ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪਾਈਪਲਾਈਨ ਅਤੇ ਇਨਵਾਇਰਨਮੈਂਟਸ ਨੂੰ ਸਟੋਰ ਕਰਦੀ ਹੈ।

    - ਇਹ experiment_name ਨੂੰ "chat_completion_Phi-3-mini-4k-instruct" ਸੈੱਟ ਕਰਦਾ ਹੈ।

    - ਇਹ ਇੱਕ ਵਿਲੱਖਣ ਟਾਈਮਸਟੈਂਪ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਮੌਜੂਦਾ ਸਮੇਂ (ਸੈਕਿੰਡਾਂ ਵਿੱਚ) ਨੂੰ ਇੰਟੀਜਰ ਅਤੇ ਫਿਰ ਸਟਰਿੰਗ ਵਿੱਚ ਬਦਲ ਕੇ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਟਾਈਮਸਟੈਂਪ ਵਿਲੱਖਣ ਨਾਮ ਅਤੇ ਵਰਜਨ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. ਫਾਈਨ ਟਿਊਨ ਕਰਨ ਲਈ ਫਾਊਂਡੇਸ਼ਨ ਮਾਡਲ ਚੁਣੋ

1. Phi-3-mini-4k-instruct 3.8B ਪੈਰਾਮੀਟਰਾਂ ਵਾਲਾ, ਹਲਕਾ, ਅਧੁਨਿਕ ਖੁੱਲ੍ਹਾ ਮਾਡਲ ਹੈ ਜੋ Phi-2 ਲਈ ਵਰਤੇ ਗਏ ਡੇਟਾਸੈੱਟਾਂ ‘ਤੇ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਇਹ ਮਾਡਲ Phi-3 ਮਾਡਲ ਪਰਿਵਾਰ ਦਾ ਹਿੱਸਾ ਹੈ, ਅਤੇ ਮਿਨੀ ਵਰਜਨ ਦੋ ਵੈਰੀਅੰਟਾਂ ਵਿੱਚ ਆਉਂਦਾ ਹੈ: 4K ਅਤੇ 128K, ਜੋ ਕਿ ਇਸਦੀ ਸਮਰਥਿਤ ਸੰਦਰਭ ਲੰਬਾਈ (ਟੋਕਨ ਵਿੱਚ) ਹੈ। ਸਾਡੇ ਖਾਸ ਮਕਸਦ ਲਈ ਮਾਡਲ ਨੂੰ ਫਾਈਨ ਟਿਊਨ ਕਰਨ ਦੀ ਲੋੜ ਹੈ। ਤੁਸੀਂ ਇਹ ਮਾਡਲ AzureML Studio ਦੇ ਮਾਡਲ ਕੈਟਾਲੌਗ ਵਿੱਚ ਚੈਟ-ਕੰਪਲੀਸ਼ਨ ਟਾਸਕ ਨਾਲ ਫਿਲਟਰ ਕਰਕੇ ਵੇਖ ਸਕਦੇ ਹੋ। ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਅਸੀਂ Phi-3-mini-4k-instruct ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹਾਂ। ਜੇ ਤੁਸੀਂ ਇਹ ਨੋਟਬੁੱਕ ਕਿਸੇ ਹੋਰ ਮਾਡਲ ਲਈ ਖੋਲ੍ਹਿਆ ਹੈ, ਤਾਂ ਮਾਡਲ ਦਾ ਨਾਮ ਅਤੇ ਵਰਜਨ ਅਨੁਸਾਰ ਬਦਲੋ।

    > [!NOTE]
    > ਮਾਡਲ id ਪ੍ਰਾਪਰਟੀ ਜੋ ਫਾਈਨ ਟਿਊਨਿੰਗ ਜੌਬ ਨੂੰ ਇਨਪੁਟ ਵਜੋਂ ਦਿੱਤੀ ਜਾਵੇਗੀ। ਇਹ AzureML Studio ਮਾਡਲ ਕੈਟਾਲੌਗ ਵਿੱਚ ਮਾਡਲ ਵੇਰਵੇ ਪੰਨੇ ‘ਤੇ Asset ID ਫੀਲਡ ਵਜੋਂ ਵੀ ਉਪਲਬਧ ਹੈ।

2. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure Machine Learning (Azure ML) ਸੇਵਾ ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਦਾ ਹੈ। ਇਹ ਕੀ ਕਰਦਾ ਹੈ:

    - ਇਹ model_name ਨੂੰ "Phi-3-mini-4k-instruct" ਸੈੱਟ ਕਰਦਾ ਹੈ।

    - ਇਹ registry_ml_client ਦੇ models ਪ੍ਰਾਪਰਟੀ ਦੇ get ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Azure ML ਰਜਿਸਟਰੀ ਤੋਂ ਦਿੱਤੇ ਮਾਡਲ ਦਾ ਨਵਾਂ ਵਰਜਨ ਲੈਦਾ ਹੈ। get ਮੈਥਡ ਨੂੰ ਦੋ ਆਰਗੁਮੈਂਟ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ: ਮਾਡਲ ਦਾ ਨਾਮ ਅਤੇ ਇੱਕ ਲੇਬਲ ਜੋ ਦੱਸਦਾ ਹੈ ਕਿ ਨਵਾਂ ਵਰਜਨ ਲੈਣਾ ਹੈ।

    - ਇਹ ਕਨਸੋਲ ‘ਤੇ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦਾ ਨਾਮ, ਵਰਜਨ ਅਤੇ id ਦਿਖਾਇਆ ਜਾਂਦਾ ਹੈ ਜੋ ਫਾਈਨ ਟਿਊਨਿੰਗ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ। ਸਟਰਿੰਗ ਦੇ format ਮੈਥਡ ਨਾਲ ਇਹ ਜਾਣਕਾਰੀ ਸੁਨੇਹੇ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਹਨਾਂ ਤਿੰਨਾਂ ਨੂੰ foundation_model ਆਬਜੈਕਟ ਦੀਆਂ ਪ੍ਰਾਪਰਟੀਆਂ ਵਜੋਂ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. ਜੌਬ ਲਈ ਕਮਪਿਊਟ ਬਣਾਓ

ਫਾਈਨ ਟਿਊਨ ਜੌਬ ਸਿਰਫ GPU ਕਮਪਿਊਟ ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ। ਕਮਪਿਊਟ ਦਾ ਆਕਾਰ ਮਾਡਲ ਦੀ ਵੱਡਾਈ ‘ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ ਅਤੇ ਜ਼ਿਆਦਾਤਰ ਮਾਮਲਿਆਂ ਵਿੱਚ ਸਹੀ ਕਮਪਿਊਟ ਚੁਣਨਾ ਔਖਾ ਹੁੰਦਾ ਹੈ। ਇਸ ਸੈੱਲ ਵਿੱਚ ਅਸੀਂ ਯੂਜ਼ਰ ਨੂੰ ਸਹੀ ਕਮਪਿਊਟ ਚੁਣਨ ਲਈ ਮਦਦ ਕਰਾਂਗੇ।

> [!NOTE]
> ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਪਿਊਟ ਸਭ ਤੋਂ ਅਨੁਕੂਲ ਸੰਰਚਨਾ ਨਾਲ ਕੰਮ ਕਰਦੇ ਹਨ। ਸੰਰਚਨਾ ਵਿੱਚ ਕੋਈ ਵੀ ਬਦਲਾਅ Cuda Out Of Memory ਗਲਤੀ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦਾ ਹੈ। ਐਸੇ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਕਮਪਿਊਟ ਨੂੰ ਵੱਡੇ ਆਕਾਰ ਵਿੱਚ ਅੱਪਗ੍ਰੇਡ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।

> [!NOTE]
> ਹੇਠਾਂ compute_cluster_size ਚੁਣਦੇ ਸਮੇਂ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਕਮਪਿਊਟ ਤੁਹਾਡੇ ਰਿਸੋਰਸ ਗਰੁੱਪ ਵਿੱਚ ਉਪਲਬਧ ਹੈ। ਜੇ ਕੋਈ ਖਾਸ ਕਮਪਿਊਟ ਉਪਲਬਧ ਨਹੀਂ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਕਮਪਿਊਟ ਸਰੋਤਾਂ ਲਈ ਐਕਸੈਸ ਦੀ ਬੇਨਤੀ ਕਰ ਸਕਦੇ ਹੋ।

### ਫਾਈਨ ਟਿਊਨਿੰਗ ਸਹਾਇਤਾ ਲਈ ਮਾਡਲ ਦੀ ਜਾਂਚ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure ML ਮਾਡਲ ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਦਾ ਹੈ। ਇਹ ਕੀ ਕਰਦਾ ਹੈ:

    - ਇਹ ast ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ, ਜੋ Python ਦੇ ਅਬਸਟ੍ਰੈਕਟ ਸਿੰਟੈਕਸ ਗ੍ਰੈਮਰ ਦੇ ਟ੍ਰੀਜ਼ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨ ਦਿੰਦਾ ਹੈ।

    - ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ foundation_model ਆਬਜੈਕਟ (ਜੋ Azure ML ਵਿੱਚ ਮਾਡਲ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ) ਕੋਲ finetune_compute_allow_list ਨਾਮ ਦਾ ਟੈਗ ਹੈ ਜਾਂ ਨਹੀਂ। Azure ML ਵਿੱਚ ਟੈਗ ਕੀ-ਵੈਲਯੂ ਜੋੜੇ ਹੁੰਦੇ ਹਨ ਜੋ ਮਾਡਲਾਂ ਨੂੰ ਫਿਲਟਰ ਅਤੇ ਸੋਰਟ ਕਰਨ ਲਈ ਬਣਾਏ ਜਾਂਦੇ ਹਨ।

    - ਜੇ finetune_compute_allow_list ਟੈਗ ਮੌਜੂਦ ਹੈ, ਤਾਂ ਇਹ ast.literal_eval ਫੰਕਸ਼ਨ ਨਾਲ ਟੈਗ ਦੀ ਵੈਲਯੂ (ਸਟ੍ਰਿੰਗ) ਨੂੰ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ Python ਲਿਸਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ। ਇਸ ਲਿਸਟ ਨੂੰ computes_allow_list ਵੈਰੀਏਬਲ ਵਿੱਚ ਸੈੱਟ ਕਰਦਾ ਹੈ। ਫਿਰ ਇਹ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਕਿ ਲਿਸਟ ਵਿੱਚੋਂ ਕਮਪਿਊਟ ਬਣਾਉਣਾ ਚਾਹੀਦਾ ਹੈ।

    - ਜੇ finetune_compute_allow_list ਟੈਗ ਮੌਜੂਦ ਨਹੀਂ ਹੈ, ਤਾਂ computes_allow_list ਨੂੰ None ਸੈੱਟ ਕਰਦਾ ਹੈ ਅਤੇ ਸੁਨੇਹਾ ਦਿੰਦਾ ਹੈ ਕਿ ਇਹ ਟੈਗ ਮਾਡਲ ਦੇ ਟੈਗਾਂ ਦਾ ਹਿੱਸਾ ਨਹੀਂ ਹੈ।

    - ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਮਾਡਲ ਦੇ ਮੈਟਾਡੇਟਾ ਵਿੱਚ ਖਾਸ ਟੈਗ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ, ਜੇ ਮੌਜੂਦ ਹੋਵੇ ਤਾਂ ਉਸਦੀ ਵੈਲਯੂ ਨੂੰ ਲਿਸਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਅਤੇ ਯੂਜ਼ਰ ਨੂੰ ਫੀਡਬੈਕ ਦਿੰਦਾ ਹੈ।

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### ਕਮਪਿਊਟ ਇੰਸਟੈਂਸ ਦੀ ਜਾਂਚ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure ML ਸੇਵਾ ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਦਾ ਹੈ ਅਤੇ ਕਮਪਿਊਟ ਇੰਸਟੈਂਸ ‘ਤੇ ਕਈ ਜਾਂਚਾਂ ਕਰਦਾ ਹੈ। ਇਹ ਕੀ ਕਰਦਾ ਹੈ:

    - ਇਹ compute_cluster ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਨਾਮ ਵਾਲਾ ਕਮਪਿਊਟ ਇੰਸਟੈਂਸ Azure ML ਵਰਕਸਪੇਸ ਤੋਂ ਲੈਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ। ਜੇ ਕਮਪਿਊਟ ਇੰਸਟੈਂਸ ਦੀ provisioning state "failed" ਹੈ, ਤਾਂ ValueError ਉਠਾਉਂਦਾ ਹੈ।

    - ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ computes_allow_list None ਨਹੀਂ ਹੈ। ਜੇ ਨਹੀਂ, ਤਾਂ ਲਿਸਟ ਵਿੱਚ ਸਾਰੇ ਕਮਪਿਊਟ ਆਕਾਰ ਨੂੰ ਲੋਅਰਕੇਸ ਕਰਦਾ ਹੈ ਅਤੇ ਵੇਖਦਾ ਹੈ ਕਿ ਮੌਜੂਦਾ ਕਮਪਿਊਟ ਆਕਾਰ ਲਿਸਟ ਵਿੱਚ ਹੈ ਜਾਂ ਨਹੀਂ। ਜੇ ਨਹੀਂ, ਤਾਂ ValueError ਉਠਾਉਂਦਾ ਹੈ।

    - ਜੇ computes_allow_list None ਹੈ, ਤਾਂ ਇਹ ਵੇਖਦਾ ਹੈ ਕਿ ਮੌਜੂਦਾ ਕਮਪਿਊਟ ਆਕਾਰ unsupported GPU VM ਆਕਾਰਾਂ ਦੀ ਲਿਸਟ ਵਿੱਚ ਹੈ ਜਾਂ ਨਹੀਂ। ਜੇ ਹੈ, ਤਾਂ ValueError ਉਠਾਉਂਦਾ ਹੈ।

    - ਇਹ ਵਰਕਸਪੇਸ ਵਿੱਚ ਉਪਲਬਧ ਸਾਰੇ ਕਮਪਿਊਟ ਆਕਾਰਾਂ ਦੀ ਲਿਸਟ ਲੈਂਦਾ ਹੈ। ਫਿਰ ਹਰ ਇੱਕ ਆਕਾਰ ਲਈ ਜਾਂਚ ਕਰਦਾ ਹੈ ਕਿ ਕੀ ਇਸਦਾ ਨਾਮ ਮੌਜੂਦਾ ਕਮਪਿਊਟ ਆਕਾਰ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ। ਜੇ ਮੇਲ ਖਾਂਦਾ ਹੈ, ਤਾਂ ਇਸ ਕਮਪਿਊਟ ਆਕਾਰ ਲਈ GPU ਦੀ ਗਿਣਤੀ ਲੈਂਦਾ ਹੈ ਅਤੇ gpu_count_found ਨੂੰ True ਕਰਦਾ ਹੈ।

    - ਜੇ gpu_count_found True ਹੈ, ਤਾਂ ਕਮਪਿਊਟ ਇੰਸਟੈਂਸ ਵਿੱਚ GPU ਦੀ ਗਿਣਤੀ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ। ਜੇ False ਹੈ, ਤਾਂ ValueError ਉਠਾਉਂਦਾ ਹੈ।

    - ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ Azure ML ਵਰਕਸਪੇਸ ਵਿੱਚ ਕਮਪਿਊਟ ਇੰਸਟੈਂਸ ਦੀ provisioning state, ਆਕਾਰ ਦੀ ਸਹੀ ਲਿਸਟ ਵਿੱਚ ਮੌਜੂਦਗੀ ਅਤੇ GPU ਗਿਣਤੀ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ।

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. ਮਾਡਲ ਦੀ ਫਾਈਨ ਟਿਊਨਿੰਗ ਲਈ ਡੇਟਾਸੈੱਟ ਚੁਣੋ

1. ਅਸੀਂ ultrachat_200k ਡੇਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ। ਡੇਟਾਸੈੱਟ ਵਿੱਚ ਚਾਰ ਸਪਲਿਟ ਹਨ, ਜੋ Supervised fine-tuning (sft) ਲਈ موزوں ਹਨ। Generation ranking (gen)। ਪ੍ਰਤੀ ਸਪਲਿਟ ਉਦਾਹਰਨਾਂ ਦੀ ਗਿਣਤੀ ਹੇਠਾਂ ਦਿੱਤੀ ਗਈ ਹੈ:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. ਅਗਲੇ ਕੁਝ ਸੈੱਲ ਫਾਈਨ ਟਿਊਨਿੰਗ ਲਈ ਬੁਨਿਆਦੀ ਡੇਟਾ ਤਿਆਰੀ ਦਿਖਾਉਂਦੇ ਹਨ:

### ਕੁਝ ਡੇਟਾ ਰੋਜ਼ ਵੇਖੋ

ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਇਹ ਨਮੂਨਾ ਤੇਜ਼ੀ ਨਾਲ ਚੱਲੇ, ਇਸ ਲਈ train_sft, test_sft ਫਾਈਲਾਂ ਵਿੱਚ ਪਹਿਲਾਂ ਹੀ ਛਾਂਟੀ ਹੋਈਆਂ ਪੰਕਤੀਆਂ ਦਾ 5% ਸੇਵ ਕਰੋ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਫਾਈਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਘੱਟ ਸਹੀਤਾ ਵਾਲਾ ਹੋਵੇਗਾ, ਇਸ ਲਈ ਇਸਨੂੰ ਅਸਲ ਦੁਨੀਆ ਵਿੱਚ ਵਰਤਣਾ ਨਹੀਂ ਚਾਹੀਦਾ।

download-dataset.py ultrachat_200k ਡੇਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰਨ ਅਤੇ ਡੇਟਾਸੈੱਟ ਨੂੰ ਫਾਈਨਟਿਊਨ ਪਾਈਪਲਾਈਨ ਕੰਪੋਨੈਂਟ ਲਈ ਉਪਯੋਗੀ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਕਿਉਂਕਿ ਡੇਟਾਸੈੱਟ ਵੱਡਾ ਹੈ, ਇਸ ਲਈ ਸਾਡੇ ਕੋਲ ਸਿਰਫ਼ ਡੇਟਾਸੈੱਟ ਦਾ ਹਿੱਸਾ ਹੈ।

1. ਹੇਠਾਂ ਦਿੱਤਾ ਸਕ੍ਰਿਪਟ ਸਿਰਫ 5% ਡੇਟਾ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ। ਇਸਨੂੰ dataset_split_pc ਪੈਰਾਮੀਟਰ ਨੂੰ ਚਾਹੀਦੇ ਪ੍ਰਤੀਸ਼ਤ ਵਿੱਚ ਬਦਲ ਕੇ ਵਧਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

    > [!NOTE]
    > ਕੁਝ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦੇ ਵੱਖ-ਵੱਖ ਭਾਸ਼ਾ ਕੋਡ ਹੁੰਦੇ ਹਨ, ਇਸ ਲਈ ਡੇਟਾਸੈੱਟ ਵਿੱਚ ਕਾਲਮ ਨਾਮ ਵੀ ਉਸੇ ਅਨੁਸਾਰ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।

1. ਡੇਟਾ ਇਸ ਤਰ
IMPORTANT RULES:
1. ਅਨੁਵਾਦ ਦੇ ਆਲੇ-ਦੁਆਲੇ '''markdown ਜਾਂ ਹੋਰ ਕਿਸੇ ਵੀ ਟੈਗ ਨੂੰ ਨਾ ਜੋੜੋ
2. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਅਨੁਵਾਦ ਬਹੁਤ ਜ਼ਿਆਦਾ ਸ਼ਾਬਦਿਕ ਨਾ ਲੱਗੇ
3. ਟਿੱਪਣੀਆਂ ਦਾ ਵੀ ਅਨੁਵਾਦ ਕਰੋ
4. ਇਹ ਫਾਈਲ Markdown ਫਾਰਮੈਟ ਵਿੱਚ ਲਿਖੀ ਗਈ ਹੈ - ਇਸਨੂੰ XML ਜਾਂ HTML ਵਾਂਗ ਨਾ ਸਮਝੋ
5. ਅਨੁਵਾਦ ਨਾ ਕਰੋ:
   - [!NOTE], [!WARNING], [!TIP], [!IMPORTANT], [!CAUTION]
   - ਵੈਰੀਏਬਲ ਨਾਮ, ਫੰਕਸ਼ਨ ਨਾਮ, ਕਲਾਸ ਨਾਮ
   - ਪਲੇਸਹੋਲਡਰ ਜਿਵੇਂ @@INLINE_CODE_x@@ ਜਾਂ @@CODE_BLOCK_x@@
   - URLs ਜਾਂ ਪਾਥ
6. ਸਾਰੇ ਮੂਲ Markdown ਫਾਰਮੈਟਿੰਗ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖੋ
7. ਸਿਰਫ ਅਨੁਵਾਦਿਤ ਸਮੱਗਰੀ ਵਾਪਸ ਕਰੋ, ਕਿਸੇ ਹੋਰ ਟੈਗ ਜਾਂ ਮਾਰਕਅੱਪ ਦੇ ਬਿਨਾਂ
ਕਿਰਪਾ ਕਰਕੇ ਨਤੀਜਾ ਖੱਬੇ ਤੋਂ ਸੱਜੇ ਲਿਖੋ।

- ਇਹ head ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ DataFrame ਦੀਆਂ ਪਹਿਲੀਆਂ 5 ਕਤਾਰਾਂ ਦਿਖਾਈਆਂ ਜਾ ਸਕਣ। ਜੇ DataFrame ਵਿੱਚ 5 ਤੋਂ ਘੱਟ ਕਤਾਰਾਂ ਹਨ, ਤਾਂ ਇਹ ਸਾਰੀਆਂ ਕਤਾਰਾਂ ਦਿਖਾਏਗਾ।

- ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ JSON Lines ਫਾਈਲ ਨੂੰ DataFrame ਵਿੱਚ ਲੋਡ ਕਰ ਰਿਹਾ ਹੈ ਅਤੇ ਪਹਿਲੀਆਂ 5 ਕਤਾਰਾਂ ਨੂੰ ਪੂਰੇ ਕਾਲਮ ਟੈਕਸਟ ਨਾਲ ਦਿਖਾ ਰਿਹਾ ਹੈ।

```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. ਮਾਡਲ ਅਤੇ ਡੇਟਾ ਨੂੰ ਇਨਪੁਟ ਵਜੋਂ ਵਰਤ ਕੇ fine tuning ਜੌਬ ਸਬਮਿਟ ਕਰੋ

ਉਹ ਜੌਬ ਬਣਾਓ ਜੋ chat-completion pipeline ਕੰਪੋਨੈਂਟ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। fine tuning ਲਈ ਸਾਰੇ ਸਮਰਥਿਤ ਪੈਰਾਮੀਟਰਾਂ ਬਾਰੇ ਹੋਰ ਜਾਣੋ।

### Fine tune ਪੈਰਾਮੀਟਰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ

1. Fine tune ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ 2 ਸ਼੍ਰੇਣੀਆਂ ਵਿੱਚ ਵੰਡਿਆ ਜਾ ਸਕਦਾ ਹੈ - ਟ੍ਰੇਨਿੰਗ ਪੈਰਾਮੀਟਰ, optimization ਪੈਰਾਮੀਟਰ

1. ਟ੍ਰੇਨਿੰਗ ਪੈਰਾਮੀਟਰ ਟ੍ਰੇਨਿੰਗ ਦੇ ਪੱਖਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਨ ਜਿਵੇਂ -

    - ਵਰਤਣ ਵਾਲਾ optimizer, scheduler
    - fine tune ਨੂੰ optimize ਕਰਨ ਲਈ ਮੈਟ੍ਰਿਕ
    - ਟ੍ਰੇਨਿੰਗ ਕਦਮਾਂ ਦੀ ਗਿਣਤੀ, ਬੈਚ ਸਾਈਜ਼ ਆਦਿ
    - Optimization ਪੈਰਾਮੀਟਰ GPU ਮੈਮੋਰੀ ਨੂੰ optimize ਕਰਨ ਅਤੇ ਕੰਪਿਊਟ ਸਰੋਤਾਂ ਦੀ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਵਰਤੋਂ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ।

1. ਹੇਠਾਂ ਕੁਝ ਪੈਰਾਮੀਟਰ ਦਿੱਤੇ ਗਏ ਹਨ ਜੋ ਇਸ ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਆਉਂਦੇ ਹਨ। optimization ਪੈਰਾਮੀਟਰ ਹਰ ਮਾਡਲ ਲਈ ਵੱਖਰੇ ਹੁੰਦੇ ਹਨ ਅਤੇ ਮਾਡਲ ਨਾਲ ਪੈਕੇਜ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਤਾਂ ਜੋ ਇਹ ਵੱਖ-ਵੱਖਤਾਵਾਂ ਸੰਭਾਲ ਸਕਣ।

    - deepspeed ਅਤੇ LoRA ਨੂੰ ਯੋਗ ਕਰੋ
    - mixed precision training ਨੂੰ ਯੋਗ ਕਰੋ
    - multi-node training ਨੂੰ ਯੋਗ ਕਰੋ


> [!NOTE]
> Supervised finetuning ਨਾਲ alignment ਖੋ ਜਾਣ ਜਾਂ catastrophic forgetting ਹੋ ਸਕਦੀ ਹੈ। ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ ਇਸ ਸਮੱਸਿਆ ਦੀ ਜਾਂਚ ਕਰੋ ਅਤੇ finetune ਕਰਨ ਤੋਂ ਬਾਅਦ alignment ਸਟੇਜ ਚਲਾਓ।

### Fine Tuning ਪੈਰਾਮੀਟਰ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਲਈ fine-tuning ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰ ਰਿਹਾ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ ਇਹ ਹੈ:

    - ਇਹ ਡਿਫਾਲਟ ਟ੍ਰੇਨਿੰਗ ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਟ੍ਰੇਨਿੰਗ epochs ਦੀ ਗਿਣਤੀ, ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਮੁਲਾਂਕਣ ਲਈ ਬੈਚ ਸਾਈਜ਼, ਲਰਨਿੰਗ ਰੇਟ, ਅਤੇ ਲਰਨਿੰਗ ਰੇਟ scheduler ਦੀ ਕਿਸਮ।

    - ਇਹ ਡਿਫਾਲਟ optimization ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰਦਾ ਹੈ ਜਿਵੇਂ Layer-wise Relevance Propagation (LoRa) ਅਤੇ DeepSpeed ਲਾਗੂ ਕਰਨ ਦੀ ਸਥਿਤੀ, ਅਤੇ DeepSpeed ਦਾ ਸਟੇਜ।

    - ਇਹ ਟ੍ਰੇਨਿੰਗ ਅਤੇ optimization ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਇੱਕ dict ਵਿੱਚ ਜੋੜਦਾ ਹੈ ਜਿਸਨੂੰ finetune_parameters ਕਹਿੰਦੇ ਹਨ।

    - ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ foundation_model ਕੋਲ ਕੋਈ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਡਿਫਾਲਟ ਪੈਰਾਮੀਟਰ ਹਨ ਜਾਂ ਨਹੀਂ। ਜੇ ਹਨ, ਤਾਂ ਇਹ ਚੇਤਾਵਨੀ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਅਤੇ finetune_parameters dict ਨੂੰ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਡਿਫਾਲਟ ਨਾਲ ਅਪਡੇਟ ਕਰਦਾ ਹੈ। ast.literal_eval ਫੰਕਸ਼ਨ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਡਿਫਾਲਟ ਨੂੰ ਸਟਰਿੰਗ ਤੋਂ Python dict ਵਿੱਚ ਬਦਲਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ ਅੰਤਿਮ fine-tuning ਪੈਰਾਮੀਟਰਾਂ ਦਾ ਸੈੱਟ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਜੋ ਚਲਾਉਣ ਲਈ ਵਰਤੇ ਜਾਣਗੇ।

    - ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਲਈ fine-tuning ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰ ਰਿਹਾ ਹੈ ਅਤੇ ਡਿਫਾਲਟ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਨਾਲ ਓਵਰਰਾਈਡ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦੇ ਰਿਹਾ ਹੈ।

```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Training Pipeline

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਇੱਕ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰ ਰਿਹਾ ਹੈ ਜੋ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਟ੍ਰੇਨਿੰਗ pipeline ਲਈ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਂਦਾ ਹੈ, ਅਤੇ ਫਿਰ ਇਸ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਕੇ ਡਿਸਪਲੇ ਨਾਮ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ ਇਹ ਹੈ:

1. get_pipeline_display_name ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ ਫੰਕਸ਼ਨ ਟ੍ਰੇਨਿੰਗ pipeline ਨਾਲ ਸੰਬੰਧਿਤ ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਂਦਾ ਹੈ।

1. ਫੰਕਸ਼ਨ ਦੇ ਅੰਦਰ, ਇਹ ਕੁੱਲ ਬੈਚ ਸਾਈਜ਼ ਦੀ ਗਿਣਤੀ ਕਰਦਾ ਹੈ ਜੋ ਪ੍ਰਤੀ-ਡਿਵਾਈਸ ਬੈਚ ਸਾਈਜ਼, gradient accumulation ਕਦਮਾਂ ਦੀ ਗਿਣਤੀ, ਪ੍ਰਤੀ ਨੋਡ GPUs ਦੀ ਗਿਣਤੀ, ਅਤੇ fine-tuning ਲਈ ਵਰਤੇ ਗਏ ਨੋਡਾਂ ਦੀ ਗਿਣਤੀ ਨੂੰ ਗੁਣਾ ਕਰਕੇ ਮਿਲਦੀ ਹੈ।

1. ਇਹ ਹੋਰ ਪੈਰਾਮੀਟਰ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਲਰਨਿੰਗ ਰੇਟ scheduler ਦੀ ਕਿਸਮ, DeepSpeed ਲਾਗੂ ਹੋਣ ਦੀ ਸਥਿਤੀ, DeepSpeed ਸਟੇਜ, Layer-wise Relevance Propagation (LoRa) ਲਾਗੂ ਹੋਣ ਦੀ ਸਥਿਤੀ, ਮਾਡਲ ਚੈਕਪੌਇੰਟਾਂ ਦੀ ਸੰਖਿਆ ਦੀ ਸੀਮਾ, ਅਤੇ ਵੱਧ ਤੋਂ ਵੱਧ ਸੀਕੁਐਂਸ ਲੰਬਾਈ।

1. ਇਹ ਸਾਰੇ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਹਾਈਫਨ ਨਾਲ ਜੁੜੇ ਇੱਕ ਸਟਰਿੰਗ ਵਿੱਚ ਬਣਾਉਂਦਾ ਹੈ। ਜੇ DeepSpeed ਜਾਂ LoRa ਲਾਗੂ ਹੈ, ਤਾਂ ਸਟਰਿੰਗ ਵਿੱਚ "ds" ਨਾਲ DeepSpeed ਸਟੇਜ ਜਾਂ "lora" ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ। ਨਹੀਂ ਤਾਂ "nods" ਜਾਂ "nolora" ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ।

1. ਫੰਕਸ਼ਨ ਇਹ ਸਟਰਿੰਗ ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੋ ਟ੍ਰੇਨਿੰਗ pipeline ਲਈ ਡਿਸਪਲੇ ਨਾਮ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ।

1. ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਇਸਨੂੰ ਕਾਲ ਕਰਕੇ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਪ੍ਰਿੰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

1. ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਟ੍ਰੇਨਿੰਗ pipeline ਲਈ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਫਿਰ ਇਸਨੂੰ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Pipeline ਦੀ ਸੰਰਚਨਾ

ਇਹ Python ਸਕ੍ਰਿਪਟ Azure Machine Learning SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ pipeline ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਅਤੇ ਸੰਰਚਿਤ ਕਰ ਰਿਹਾ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ ਇਹ ਹੈ:

1. ਇਹ Azure AI ML SDK ਤੋਂ ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ।

1. ਇਹ ਰਜਿਸਟਰੀ ਤੋਂ "chat_completion_pipeline" ਨਾਮਕ pipeline ਕੰਪੋਨੈਂਟ ਲੈਦਾ ਹੈ।

1. ਇਹ `@pipeline` ਡੈਕੋਰੇਟਰ ਅਤੇ `create_pipeline` ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ pipeline ਜੌਬ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ। pipeline ਦਾ ਨਾਮ `pipeline_display_name` ਰੱਖਿਆ ਗਿਆ ਹੈ।

1. `create_pipeline` ਫੰਕਸ਼ਨ ਦੇ ਅੰਦਰ, ਇਹ ਲਿਆਇਆ pipeline ਕੰਪੋਨੈਂਟ ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਇਨਿਸ਼ੀਅਲਾਈਜ਼ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਮਾਡਲ ਪਾਥ, ਵੱਖ-ਵੱਖ ਸਟੇਜਾਂ ਲਈ ਕੰਪਿਊਟ ਕਲੱਸਟਰ, ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਟੈਸਟਿੰਗ ਲਈ ਡੇਟਾਸੈੱਟ ਸਪਲਿਟ, fine-tuning ਲਈ GPUs ਦੀ ਗਿਣਤੀ, ਅਤੇ ਹੋਰ fine-tuning ਪੈਰਾਮੀਟਰ।

1. ਇਹ fine-tuning ਜੌਬ ਦੇ ਆਉਟਪੁੱਟ ਨੂੰ pipeline ਜੌਬ ਦੇ ਆਉਟਪੁੱਟ ਨਾਲ ਮੈਪ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ fine-tuned ਮਾਡਲ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਰਜਿਸਟਰ ਕੀਤਾ ਜਾ ਸਕੇ, ਜੋ ਮਾਡਲ ਨੂੰ ਆਨਲਾਈਨ ਜਾਂ ਬੈਚ ਐਂਡਪੌਇੰਟ 'ਤੇ ਡਿਪਲੋਇ ਕਰਨ ਲਈ ਲਾਜ਼ਮੀ ਹੈ।

1. ਇਹ `create_pipeline` ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਕੇ pipeline ਦਾ ਇੱਕ ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ।

1. ਇਹ pipeline ਦੀ `force_rerun` ਸੈਟਿੰਗ ਨੂੰ `True` ਕਰਦਾ ਹੈ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਪਿਛਲੇ ਜੌਬਾਂ ਦੇ cached ਨਤੀਜੇ ਵਰਤੇ ਨਹੀਂ ਜਾਣਗੇ।

1. ਇਹ pipeline ਦੀ `continue_on_step_failure` ਸੈਟਿੰਗ ਨੂੰ `False` ਕਰਦਾ ਹੈ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਜੇ ਕੋਈ ਵੀ ਕਦਮ ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ pipeline ਰੁਕ ਜਾਵੇਗਾ।

1. ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ Azure Machine Learning SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ chat completion ਟਾਸਕ ਲਈ ਮਸ਼ੀਨ ਲਰਨਿੰਗ pipeline ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਅਤੇ ਸੰਰਚਿਤ ਕਰ ਰਿਹਾ ਹੈ।

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### ਜੌਬ ਸਬਮਿਟ ਕਰੋ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ pipeline ਜੌਬ ਨੂੰ Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ ਸਬਮਿਟ ਕਰ ਰਿਹਾ ਹੈ ਅਤੇ ਫਿਰ ਜੌਬ ਦੇ ਪੂਰਾ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰ ਰਿਹਾ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ ਇਹ ਹੈ:

    - ਇਹ workspace_ml_client ਦੇ jobs ਆਬਜੈਕਟ ਦੀ create_or_update ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ pipeline ਜੌਬ ਸਬਮਿਟ ਕਰਨ ਲਈ। ਚਲਾਉਣ ਵਾਲਾ pipeline pipeline_object ਨਾਲ ਦਿੱਤਾ ਗਿਆ ਹੈ ਅਤੇ ਜੌਬ ਜਿਸ ਐਕਸਪੇਰੀਮੈਂਟ ਹੇਠ ਚਲਾਇਆ ਜਾ ਰਿਹਾ ਹੈ ਉਹ experiment_name ਨਾਲ ਦਿੱਤਾ ਗਿਆ ਹੈ।

    - ਫਿਰ ਇਹ workspace_ml_client ਦੇ jobs ਆਬਜੈਕਟ ਦੀ stream ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ pipeline ਜੌਬ ਦੇ ਪੂਰਾ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰਨ ਲਈ। ਉਡੀਕ ਕਰਨ ਵਾਲਾ ਜੌਬ pipeline_job ਆਬਜੈਕਟ ਦੇ name ਐਟ੍ਰਿਬਿਊਟ ਨਾਲ ਦਿੱਤਾ ਗਿਆ ਹੈ।

    - ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ pipeline ਜੌਬ ਨੂੰ Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ ਸਬਮਿਟ ਕਰ ਰਿਹਾ ਹੈ ਅਤੇ ਫਿਰ ਜੌਬ ਦੇ ਪੂਰਾ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰ ਰਿਹਾ ਹੈ।

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. fine tuned ਮਾਡਲ ਨੂੰ ਵਰਕਸਪੇਸ ਨਾਲ ਰਜਿਸਟਰ ਕਰੋ

ਅਸੀਂ fine tuning ਜੌਬ ਦੇ ਆਉਟਪੁੱਟ ਤੋਂ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਾਂਗੇ। ਇਹ fine tuned ਮਾਡਲ ਅਤੇ fine tuning ਜੌਬ ਦੇ ਵਿਚਕਾਰ lineage ਟਰੈਕ ਕਰੇਗਾ। fine tuning ਜੌਬ, ਅੱਗੇ, foundation ਮਾਡਲ, ਡੇਟਾ ਅਤੇ ਟ੍ਰੇਨਿੰਗ ਕੋਡ ਨਾਲ lineage ਟਰੈਕ ਕਰਦਾ ਹੈ।

### ML ਮਾਡਲ ਰਜਿਸਟਰ ਕਰਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰ ਰਿਹਾ ਹੈ ਜੋ Azure Machine Learning pipeline ਵਿੱਚ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਸੀ। ਇਹਦਾ ਵੇਰਵਾ ਇਹ ਹੈ:

    - ਇਹ Azure AI ML SDK ਤੋਂ ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ।

    - ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ pipeline ਜੌਬ ਤੋਂ trained_model ਆਉਟਪੁੱਟ ਉਪਲਬਧ ਹੈ ਜਾਂ ਨਹੀਂ, ਜਿਸ ਲਈ workspace_ml_client ਦੇ jobs ਆਬਜੈਕਟ ਦੀ get ਮੈਥਡ ਕਾਲ ਕਰਦਾ ਹੈ ਅਤੇ ਉਸਦੇ outputs ਐਟ੍ਰਿਬਿਊਟ ਤੱਕ ਪਹੁੰਚਦਾ ਹੈ।

    - ਇਹ pipeline ਜੌਬ ਦੇ ਨਾਮ ਅਤੇ ਆਉਟਪੁੱਟ ("trained_model") ਦੇ ਨਾਮ ਨਾਲ ਇੱਕ ਮਾਡਲ ਪਾਥ ਬਣਾਉਂਦਾ ਹੈ।

    - ਇਹ fine-tuned ਮਾਡਲ ਲਈ ਇੱਕ ਨਾਮ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਮੂਲ ਮਾਡਲ ਨਾਮ ਦੇ ਨਾਲ "-ultrachat-200k" ਜੋੜ ਕੇ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਸਾਰੇ ਸਲੈਸ਼ ਨੂੰ ਹਾਈਫਨ ਨਾਲ ਬਦਲ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ।

    - ਇਹ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨ ਲਈ Model ਆਬਜੈਕਟ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦਾ ਪਾਥ, ਮਾਡਲ ਦੀ ਕਿਸਮ (MLflow ਮਾਡਲ), ਮਾਡਲ ਦਾ ਨਾਮ ਅਤੇ ਵਰਜਨ, ਅਤੇ ਮਾਡਲ ਦਾ ਵੇਰਵਾ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ।

    - ਇਹ workspace_ml_client ਦੇ models ਆਬਜੈਕਟ ਦੀ create_or_update ਮੈਥਡ ਕਾਲ ਕਰਕੇ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਦਾ ਹੈ।

    - ਇਹ ਰਜਿਸਟਰਡ ਮਾਡਲ ਨੂੰ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

1. ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰ ਰਿਹਾ ਹੈ ਜੋ Azure Machine Learning pipeline ਵਿੱਚ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਸੀ।

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. fine tuned ਮਾਡਲ ਨੂੰ ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ 'ਤੇ ਡਿਪਲੋਇ ਕਰੋ

ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਇੱਕ ਟਿਕਾਊ REST API ਦਿੰਦੇ ਹਨ ਜੋ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਮਾਡਲ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

### Endpoint ਪ੍ਰਬੰਧਨ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਰਜਿਸਟਰਡ ਮਾਡਲ ਲਈ managed online endpoint ਬਣਾਉਂਦਾ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ ਇਹ ਹੈ:

    - ਇਹ Azure AI ML SDK ਤੋਂ ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ।

    - ਇਹ online endpoint ਲਈ ਇੱਕ ਵਿਲੱਖਣ ਨਾਮ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ "ultrachat-completion-" ਸਟਰਿੰਗ ਨਾਲ ਟਾਈਮਸਟੈਂਪ ਜੋੜ ਕੇ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ ManagedOnlineEndpoint ਆਬਜੈਕਟ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ endpoint ਦਾ ਨਾਮ, ਵੇਰਵਾ, ਅਤੇ authentication ਮੋਡ ("key") ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ।

    - ਇਹ workspace_ml_client ਦੀ begin_create_or_update ਮੈਥਡ ਕਾਲ ਕਰਕੇ online endpoint ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ wait ਮੈਥਡ ਨਾਲ ਬਣਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਪੂਰੀ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰਦਾ ਹੈ।

1. ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਰਜਿਸਟਰਡ ਮਾਡਲ ਲਈ managed online endpoint ਬਣਾਉਂਦਾ ਹੈ।

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> ਤੁਸੀਂ ਇੱਥੇ deployment ਲਈ ਸਮਰਥਿਤ SKU ਦੀ ਸੂਚੀ ਵੇਖ ਸਕਦੇ ਹੋ - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML ਮਾਡਲ ਡਿਪਲੋਇ ਕਰਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਇੱਕ ਰਜਿਸਟਰਡ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਨੂੰ Azure Machine Learning ਵਿੱਚ managed online endpoint 'ਤੇ ਡਿਪਲੋਇ ਕਰ ਰਿਹਾ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ ਇਹ ਹੈ:

    - ਇਹ ast ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ, ਜੋ Python abstract syntax grammar ਦੇ ਟ੍ਰੀਜ਼ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨ ਦਿੰਦਾ ਹੈ।

    - ਇਹ deployment ਲਈ instance type "Standard_NC6s_v3" ਸੈੱਟ ਕਰਦਾ ਹੈ।

    - ਇਹ foundation model ਵਿੱਚ inference_compute_allow_list ਟੈਗ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ। ਜੇ ਇਹ ਮੌਜੂਦ ਹੈ, ਤਾਂ ਇਹ ਟੈਗ ਮੁੱਲ ਨੂੰ ਸਟਰਿੰਗ ਤੋਂ Python ਲਿਸਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਅਤੇ inference_computes_allow_list ਨੂੰ ਸੈੱਟ ਕਰਦਾ ਹੈ। ਨਹੀਂ ਤਾਂ ਇਸਨੂੰ None ਕਰਦਾ ਹੈ।

    - ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ
- ਇਹ sample_score.json ਨਾਮ ਦੀ ਫਾਈਲ ਖੋਲ੍ਹਦਾ ਹੈ

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### ਐਂਡਪੌਇੰਟ ਨੂੰ ਕਾਲ ਕਰਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਕਾਲ ਕਰ ਰਿਹਾ ਹੈ ਤਾਂ ਜੋ ਇੱਕ JSON ਫਾਈਲ ਨੂੰ ਸਕੋਰ ਕੀਤਾ ਜਾ ਸਕੇ। ਇਹਦਾ ਵੇਰਵਾ ਇਸ ਤਰ੍ਹਾਂ ਹੈ:

    - ਇਹ workspace_ml_client ਓਬਜੈਕਟ ਦੀ online_endpoints ਪ੍ਰਾਪਰਟੀ ਦੇ invoke ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ। ਇਹ ਮੈਥਡ ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਰਿਕਵੇਸਟ ਭੇਜਣ ਅਤੇ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ endpoint_name ਅਤੇ deployment_name ਆਰਗੁਮੈਂਟਸ ਨਾਲ ਐਂਡਪੌਇੰਟ ਅਤੇ ਡਿਪਲੋਇਮੈਂਟ ਦੇ ਨਾਮ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਐਂਡਪੌਇੰਟ ਦਾ ਨਾਮ online_endpoint_name ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਹੈ ਅਤੇ ਡਿਪਲੋਇਮੈਂਟ ਦਾ ਨਾਮ "demo" ਹੈ।

    - ਇਹ request_file ਆਰਗੁਮੈਂਟ ਨਾਲ JSON ਫਾਈਲ ਦਾ ਪਾਥ ਦਿੰਦਾ ਹੈ ਜਿਸਨੂੰ ਸਕੋਰ ਕਰਨਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਫਾਈਲ ਦਾ ਪਾਥ ./ultrachat_200k_dataset/sample_score.json ਹੈ।

    - ਇਹ ਐਂਡਪੌਇੰਟ ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਨੂੰ response ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਕਰਦਾ ਹੈ।

    - ਇਹ ਕੱਚਾ ਜਵਾਬ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

1. ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਕਾਲ ਕਰਕੇ JSON ਫਾਈਲ ਨੂੰ ਸਕੋਰ ਕਰਦਾ ਹੈ ਅਤੇ ਜਵਾਬ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਮਿਟਾਓ

1. ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਮਿਟਾਉਣਾ ਨਾ ਭੁੱਲੋ, ਨਹੀਂ ਤਾਂ ਤੁਸੀਂ ਐਂਡਪੌਇੰਟ ਵੱਲੋਂ ਵਰਤੇ ਗਏ ਕੰਪਿਊਟ ਲਈ ਬਿਲਿੰਗ ਮੀਟਰ ਚੱਲਦਾ ਰਹੇਗਾ। ਇਹ Python ਕੋਡ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਮਿਟਾ ਰਿਹਾ ਹੈ। ਇਸਦਾ ਵੇਰਵਾ ਇਸ ਤਰ੍ਹਾਂ ਹੈ:

    - ਇਹ workspace_ml_client ਓਬਜੈਕਟ ਦੀ online_endpoints ਪ੍ਰਾਪਰਟੀ ਦੇ begin_delete ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ। ਇਹ ਮੈਥਡ ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਮਿਟਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ name ਆਰਗੁਮੈਂਟ ਨਾਲ ਮਿਟਾਉਣ ਵਾਲੇ ਐਂਡਪੌਇੰਟ ਦਾ ਨਾਮ ਦਿੰਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਐਂਡਪੌਇੰਟ ਦਾ ਨਾਮ online_endpoint_name ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਹੈ।

    - ਇਹ wait ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਮਿਟਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਪੂਰੀ ਹੋਣ ਤੱਕ ਇੰਤਜ਼ਾਰ ਕੀਤਾ ਜਾ ਸਕੇ। ਇਹ ਇੱਕ ਬਲਾਕਿੰਗ ਓਪਰੇਸ਼ਨ ਹੈ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਸਕ੍ਰਿਪਟ ਮਿਟਾਉਣ ਦੇ ਖਤਮ ਹੋਣ ਤੱਕ ਅੱਗੇ ਨਹੀਂ ਵਧੇਗਾ।

    - ਸਾਰ ਵਿੱਚ, ਇਹ ਕੋਡ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਮਿਟਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ ਅਤੇ ਉਸਦੇ ਪੂਰੇ ਹੋਣ ਦਾ ਇੰਤਜ਼ਾਰ ਕਰਦਾ ਹੈ।

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।