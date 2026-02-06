## ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ chat-completion ਕੰਪੋਨੈਂਟਸ ਨੂੰ Azure ML ਸਿਸਟਮ ਰਜਿਸਟਰੀ ਤੋਂ ਮਾਡਲ ਨੂੰ ਫਾਇਨ ਟਿਊਨ ਕਰਨ ਲਈ

ਇਸ ਉਦਾਹਰਣ ਵਿੱਚ ਅਸੀਂ Phi-3-mini-4k-instruct ਮਾਡਲ ਨੂੰ 2 ਲੋਕਾਂ ਦੇ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਪੂਰੀ ਕਰਨ ਲਈ ultrachat_200k ਡੇਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਇਨ ਟਿਊਨ ਕਰਨਗੇ।

![MLFineTune](../../../../translated_images/pa/MLFineTune.928d4c6b3767dd35.webp)

ਉਦਾਹਰਣ ਤੁਹਾਨੂੰ ਦਿਖਾਏਗਾ ਕਿ ਕਿਸ ਤਰ੍ਹਾਂ ਅਜ਼ੂਰ ML SDK ਅਤੇ Python ਵਰਤ ਕੇ ਫਾਇਨ ਟਿਊਨਿੰਗ ਕੀਤੀ ਜਾਵੇ ਅਤੇ ਫਿਰ ਫਾਇਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਨੂੰ ਰੀਅਲ ਟਾਈਮ ਇਨਫਰਿੰਸ ਲਈ ਔਨਲਾਈਨ ਏਂਡਪੌਇੰਟ 'ਤੇ ਡਿਪਲੌਇ ਕੀਤਾ ਜਾਵੇ।

### ਟ੍ਰੇਨਿੰਗ ਡੇਟਾ

ਅਸੀਂ ultrachat_200k ਡੇਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ। ਇਹ UltraChat ਡੇਟਾਸੈੱਟ ਦਾ ਇੱਕ ਬਹੁਤ ਛਨਾ ਹੋਇਆ ਵਰਜਨ ਹੈ ਅਤੇ Zephyr-7B-β ਨੂੰ ਟਰੇਨ ਕਰਨ ਲਈ ਵਰਤਿਆ ਗਿਆ ਸੀ, ਜੋ ਕਿ ਇੱਕ ਉੱਚ ਦਰਜੇ ਦਾ 7b ਚੈਟ ਮਾਡਲ ਹੈ।

### ਮਾਡਲ

ਅਸੀਂ Phi-3-mini-4k-instruct ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ ਇਹ ਦਿਖਾਉਣ ਲਈ ਕਿ ਵਰਤੋਂਕਾਰ ਕਿਵੇਂ ਚੈਟ-ਕੰਪਲੀਸ਼ਨ ਟਾਸਕ ਲਈ ਮਾਡਲ ਨੂੰ ਫਾਇਨ ਟਿਊਨ ਕਰ ਸਕਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਇਹ ਨੋਟਬੁੱਕ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਕਾਰਡ ਤੋਂ ਖੋਲ੍ਹਿਆ ਹੈ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਉਸ ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਨਾਮ ਨਾਲ ਬਦਲੋ।

### ਟਾਸਕ

- ਫਾਇਨ ਟਿਊਨ ਕਰਨ ਲਈ ਮਾਡਲ ਚੁਣੋ।
- ਟ੍ਰੇਨਿੰਗ ਡੇਟਾ ਚੁਣੋ ਅਤੇ ਖੋਜ ਕਰੋ।
- ਫਾਇਨ ਟਿਊਨ ਜੌਬ ਲਈ ਕੰਫਿਗਰ ਕਰੋ।
- ਫਾਇਨ ਟਿਊਨ ਜੌਬ ਚਲਾਓ।
- ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਇਵਾਲੂਏਸ਼ਨ ਮੈਟ੍ਰਿਕਸ ਦੀ ਸਮੀਖਿਆ ਕਰੋ।
- ਫਾਇਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਰਜਿਸਟਰ ਕਰੋ।
- ਰੀਅਲ ਟਾਈਮ ਇਨਫਰਿੰਸ ਲਈ ਫਾਇਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਡਿਪਲੌਇ ਕਰੋ।
- ਸਰੋਤਾਂ ਨੂੰ ਸਾਫ਼ ਕਰੋ।

## 1. ਪੂਰਵ-ਆਵਸ਼ਕਤਾਵਾਂ ਸੈਟਅਪ ਕਰੋ

- ਡਿਪੈਂਡੰਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ
- AzureML ਵਰਕਸਪੇਸ ਨਾਲ ਕਨੈਕਟ ਕਰੋ। ਸੈਟਅਪ SDK ਪ੍ਰਮਾਣਿਕਤਾ ਬਾਰੇ ਹੋਰ ਜਾਣੋ। ਹੇਠਾਂ <WORKSPACE_NAME>, <RESOURCE_GROUP> ਅਤੇ <SUBSCRIPTION_ID> ਬਦਲੋ।
- azureml ਸਿਸਟਮ ਰਜਿਸਟਰੀ ਨਾਲ ਕਨੈਕਟ ਕਰੋ
- ਇੱਕ ਵਿਕਲਪਿਕ ਐਕਸਪੇਰੀਮੈਂਟ ਨਾਮ ਸੈੱਟ ਕਰੋ
- ਕੰਪਿਊਟ ਚੈੱਕ ਕਰੋ ਜਾਂ ਬਣਾਓ।

> [!NOTE]
> ਲੋੜ ਹੈ ਕਿ ਇੱਕ ਗ੍ਰਾਫਿਕਸ ਪ੍ਰੋਸੈਸਿੰਗ ਯੂਨਿਟ (GPU) ਨੋਡ ਵਿੱਚ ਕਈ GPU ਕਾਰਡ ਹੋ ਸਕਦੇ ਹਨ। ਉਦਾਹਰਣ ਵਜੋਂ, Standard_NC24rs_v3 ਦੇ ਇੱਕ ਨੋਡ ਵਿੱਚ 4 NVIDIA V100 GPU ਹਨ ਜਦਕਿ Standard_NC12s_v3 ਵਿੱਚ 2 NVIDIA V100 GPU ਹਨ। ਇਸ ਜਾਣਕਾਰੀ ਲਈ ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਦੇਖੋ। ਹਰ ਨੋਡ ਵਿੱਚ GPU ਕਾਰਡਾਂ ਦੀ ਗਿਣਤੀ ਪਰਾਮੈਟਰ gpus_per_node ਵਿੱਚ ਸੈੱਟ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਮੂਲ ਨੂੰ ਸਹੀ ਸੈੱਟ ਕਰਨ ਨਾਲ ਨੋਡ ਵਿੱਚ ਸਾਰੇ GPU ਦੀ ਵਰਤੋਂ ਯਕੀਨੀ ਬਣੇਗੀ। ਸਿਫਾਰਸ਼ੀਤ GPU ਕੰਪਿਊਟ SKUs ਇੱਥੇ ਅਤੇ ਇੱਥੇ ਮਿਲ ਸਕਦੇ ਹਨ।

### Python ਲਾਇਬ੍ਰੇਰੀਜ਼

 ਡਿਪੈਂਡੰਸੀਜ਼ ਹੇਠਾਂ ਦਿੱਤਾ ਸੈੱਲ ਚਲਾਕੇ ਇੰਸਟਾਲ ਕਰੋ। ਇਹ ਨਵੀਂ ਵਾਤਾਵਰਣ ਵਿੱਚ ਚਲਾਉਂਦੇ ਸਮੇਂ ਇਕ ਵਿਕਲਪਿਕ ਕਦਮ ਨਹੀਂ ਹੈ।

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure ਮਸ਼ੀਨ ਲਰਨਿੰਗ (Azure ML) ਸੇਵਾ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਇਸਦਾ ਖਾਕਾ ਇਹ ਹੈ:

    - ਇਹ azure.ai.ml, azure.identity ਅਤੇ azure.ai.ml.entities ਪੈਕੇਜਾਂ ਤੋਂ ਜਰੂਰੀ ਮੋਡਿਊਲ ਆਯਾਤ ਕਰਦਾ ਹੈ। ਇਸਦੇ ਨਾਲ ਹੀ time ਮੋਡਿਊਲ ਵੀ ਆਯਾਤ ਹੁੰਦਾ ਹੈ।

    - ਇਹ DefaultAzureCredential() ਨਾਲ ਪ੍ਰਮਾਣਿਕਤਾ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ, ਜੋ ਕਿ Azure ਕਲਾਉਡ ਵਿੱਚ ਤੇਜ਼ ਵਿਕਾਸ ਲਈ ਸਰਲ ਪ੍ਰਮਾਣਿਕਤਾ ਦਾ ਤਰੀਕਾ ਹੁੰਦਾ ਹੈ। ਜੇ ਇਹ ਅਸਫਲ ਰਹਿੰਦਾ ਹੈ, ਤਾਂ ਇਹ InteractiveBrowserCredential() ਨਾਲ ਜੁੜਦਾ ਹੈ, ਜੋ ਇੰਟਰਐਕਟਿਵ ਲਾਗਿਨ ਪ੍ਰਾਂਪਟ ਦਿੰਦਾ ਹੈ।

    - ਫਿਰ ਇਹ from_config ਵਿਧੀ ਨਾਲ MLClient ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ, ਜੋ ਡਿਫਾਲਟ ਕਾਨਫਿਗ ਫਾਈਲ (config.json) ਤੋਂ ਕੰਫਿਗਰੇਸ਼ਨ ਪੜ੍ਹਦਾ ਹੈ। ਜੇ ਇਹ ਅਸਫਲ ਰਹਿੰਦਾ ਹੈ, ਤਾਂ ਇਹ ਸਬਸਕ੍ਰਿਪਸ਼ਨ_ਆਈਡੀ, ਰਿਸੋਰਸ_ਗਰੁੱਪ_ਨਾਂ ਅਤੇ ਵਰਕਸਪੇਸ_ਨਾਂ ਇੱਥੋਂ ਦਿੱਤੇ ਗਏ ਹਨ, ਉਹਨਾਂ ਨੂੰ ਹੱਥੋਂ ਦੇ ਕੇ MLClient ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ।

    - ਇਹ ਇੱਕ ਹੋਰ MLClient ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ, ਜੋ Azure ML ਰਜਿਸਟਰੀ "azureml" ਲਈ ਹੈ। ਇਹ ਰਜਿਸਟਰੀ ਉਸ ਥਾਂ ਹੈ ਜਿੱਥੇ ਮਾਡਲ, ਫਾਇਨ-ਟਿਊਨਿੰਗ ਪਾਈਪਲਾਈਨ ਅਤੇ ਇੰਵਾਇਰਨਮੈਂਟ ਸਟੋਰ ਕੀਤੇ ਵੰਨਦੇ ਹਨ।

    - ਇਹ experiment_name ਨੂੰ "chat_completion_Phi-3-mini-4k-instruct" ਸੈੱਟ ਕਰਦਾ ਹੈ।

    - ਇਹ ਇੱਕ ਯੂਨੀਕ ਟਾਈਮਸਟੈਂਪ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਮੌਜੂਦਾ ਸਮੇਂ (ਐਪੋਕ ਤੋਂ ਸਕਿੰਟਾਂ ਵਿੱਚ, ਫਲੋਟਿੰਗ ਬਿੰਦੂ ਸੰਗਿਆ ਦੇ ਰੂਪ ਵਿੱਚ) ਨੂੰ ਪੂਰੇ ਅੰਕ ਵਿੱਚ ਅਤੇ ਫਿਰ ਸਟਰਿੰਗ ਵਿੱਚ ਬਦਲ ਕੇ ਬਣਦਾ ਹੈ। ਇਹ ਟਾਈਮਸਟੈਂਪ ਯੂਨੀਕ ਨਾਮ ਅਤੇ ਵਰਜਨ ਬਣਾਉਣ ਲਈ ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ।

    ```python
    # Azure ML ਅਤੇ Azure Identity ਤੋਂ ਜਰੂਰੀ ਮੌਡੀਊਲਾਂ ਇੰਪੋਰਟ ਕਰੋ
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # ਸਮਾਂ ਮੌਡੀਊਲ ਇੰਪੋਰਟ ਕਰੋ
    
    # DefaultAzureCredential ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਮਾਣਿਕਤਾ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # ਜੇ DefaultAzureCredential ਫੇਲ੍ਹ ਹੁੰਦੀ ਹੈ, ਤਾਂ InteractiveBrowserCredential ਦੀ ਵਰਤੋਂ ਕਰੋ
        credential = InteractiveBrowserCredential()
    
    # ਡਿਫਾਲਟ ਕਨਫਿਗ ਫਾਈਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ MLClient ਇੰਸਟੈਂਸ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # ਜੇ ਇਹ ਫੇਲ੍ਹ ਹੁੰਦਾ ਹੈ, ਤਾਂ ਜਾਣਕਾਰੀ ਮੁਹੱਈਆ ਕਰਵਾ ਕੇ ਹੱਥੋਂ MLClient ਇੰਸਟੈਂਸ ਬਣਾਓ
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # "azureml" ਨਾਂ ਦੇ Azure ML ਰਜਿਸਟਰੀ ਲਈ ਹੋਰ MLClient ਇੰਸਟੈਂਸ ਬਣਾਓ
    # ਇਹ ਰਜਿਸਟਰੀ ਉਹ ਜਗ੍ਹਾ ਹੈ ਜਿੱਥੇ ਮਾਡਲ, ਫਾਈਨ-ਟਿੂਨਿੰਗ ਪਾਈਪਲਾਈਨ ਅਤੇ ਵਾਤਾਵਰਨ ਸਾਂਭੇ ਜਾਂਦੇ ਹਨ
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # ਪ੍ਰਯੋਗਸ਼ਾਲਾ ਦਾ ਨਾਮ ਸੈੱਟ ਕਰੋ
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # ਇੱਕ ਵਿਲੱਖਣ ਸਮਾਂਮੁਦ੍ਰਾ ਬਣਾਓ ਜੋ ਵੱਖ-ਵੱਖ ਨਾਮਾਂ ਅਤੇ ਸੰਸਕਰਣਾਂ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ
    timestamp = str(int(time.time()))
    ```

## 2. ਫਾਇਨ ਟਿਊਨ ਲਈ ਇੱਕ ਨਿਯਮਤ ਮਾਡਲ ਚੁਣੋ

1. Phi-3-mini-4k-instruct 3.8B ਪੈਰਾਮੀਟਰ ਵਾਲਾ, ਕਮਜੋਰ, ਸਭ ਤੋਂ ਅਧੁਨਿਕ ਖੁੱਲਾ ਮਾਡਲ ਹੈ ਜੋ Phi-2 ਦੇ ਵਰਤੇ ਡੇਟਾਸੈੱਟ ਉੱਤੇ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਮਾਡਲ Phi-3 ਮਾਡਲ ਪਰਿਵਾਰ ਲਈ ਹੈ, ਅਤੇ ਮਿਨੀ ਵਰਜਨ ਵਿੱਚ ਦੋ ਵੈਰੀਅੰਟ 4K ਅਤੇ 128K ਹਨ ਜੋ ਕਾਂਟੈਕਸਟ ਲੰਬਾਈ (ਟੋਕਨਸ ਵਿੱਚ) ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਇਹ ਸਮਰਥਨ ਕਰ ਸਕਦਾ ਹੈ। ਸਾਡੇ ਖਾਸ ਉਦੇਸ਼ ਲਈ ਸਾਨੂੰ ਮਾਡਲ ਨੂੰ ਫਾਇਨ ਟਿਊਨ ਕਰਨਾ ਪਵੇਗਾ। ਤੁਸੀਂ ਇਹ ਮਾਡਲ AzureML Studio ਵਿੱਚ ਮਾਡਲ ਕੈਟਾਲੌਗ ਵਿਚ ਖੋਜ ਸਕਦੇ ਹੋ, ਚੈਟ-ਕੰਪਲੀਸ਼ਨ ਟਾਸਕ ਨਾਲ ਫਿਲਟਰ ਕਰਕੇ। ਇਸ ਉਦਾਹਰਣ ਵਿੱਚ ਅਸੀਂ Phi-3-mini-4k-instruct ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ। ਜੇ ਤੁਸੀਂ ਇਹ ਨੋਟਬੁੱਕ ਕਿਸੇ ਵੱਖਰੇ ਮਾਡਲ ਲਈ ਖੋਲਾ ਹੈ, ਤਾਂ ਮਾਡਲ ਨਾਮ ਅਤੇ ਵਰਜਨ ਅਨੁਸਾਰ ਬਦਲੋ।

> [!NOTE]
> ਮਾਡਲ ਦੀ id ਪ੍ਰੋਪਟੀ ਮਾਡਲ ਨੂੰ ਫਾਇਨ ਟਿਊਨ ਜੌਬ ਨੂੰ ਦਿੱਤੀ ਜਾਵੇਗੀ। ਇਹ AzureML Studio ਮਾਡਲ ਕੈਟਾਲੌਗ ਵਿੱਚ ਮਾਡਲ ਦੇ ਵੇਰਵੇ ਸਫੇ ਤੇ Asset ID ਫੀਲਡ ਵਜੋਂ ਵੀ ਦਿਖਾਈ ਦੇਂਦੀ ਹੈ।

2. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure ਮਸ਼ੀਨ ਲਰਨਿੰਗ (Azure ML) ਸੇਵਾ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰ ਰਿਹਾ ਹੈ। ਇਹਦਾ ਖਾਕਾ ਇਹ ਹੈ:

    - ਇਹ model_name ਨੂੰ "Phi-3-mini-4k-instruct" ਸੈੱਟ ਕਰਦਾ ਹੈ।

    - ਇਹ registry_ml_client ਵਸਤੂ ਦੇ models ਗੁਣ ਵੱਲੋਂ get ਵਿਧੀ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ, ਜੋ ਨਾਮ ਅਤੇ ਲੇਬਲ ਨਾਲ ਨਵੀਂਤਮ ਵਰਜਨ ਵਾਲਾ ਮਾਡਲ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ।

    - ਇਹ ਕਨਸੋਲ 'ਤੇ ਸੁਨੇਹਾ ਛਾਪਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦੇ ਨਾਮ, ਵਰਜਨ ਅਤੇ id ਦੀ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ ਜੋ ਫਾਇਨ-ਟਿਊਨਿੰਗ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ। strings.format ਮੈਥਡ ਨਾਲ ਇਹ ਵੇਰਵਾ ਜੋੜਿਆ ਜਾਂਦਾ ਹੈ। ਸੋਧੇ ਗਏ foundation_model ਵਸਤੂ ਦੇ ਗੁਣਾਂ ਵਜੋਂ ਨਾਮ, ਵਰਜਨ ਅਤੇ id ਪ੍ਰਾਪਤ ਹੁੰਦੇ ਹਨ।

    ```python
    # ਮਾਡਲ ਦਾ ਨਾਮ ਸੈੱਟ ਕਰੋ
    model_name = "Phi-3-mini-4k-instruct"
    
    # ਐਜ਼ੂਰ ਐਮਐਲ ਰਜਿਸਟਰੀ ਤੋਂ ਮਾਡਲ ਦਾ ਨਵਾਂਤਮ ਵਰਜਨ ਪ੍ਰਾਪਤ ਕਰੋ
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # ਮਾਡਲ ਦਾ ਨਾਮ, ਵਰਜਨ, ਅਤੇ ਆਈਡੀ ਛਾਪੋ
    # ਇਹ ਜਾਣਕਾਰੀ ਟਰੇਕਿੰਗ ਅਤੇ ਡਿਬੱਗਿੰਗ ਲਈ ਲਾਭਦਾਇਕ ਹੈ
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. ਇੱਕ ਕੰਪਿਊਟ ਬਣਾਓ ਜੋ ਜੌਬ ਨਾਲ ਵਰਤੋਂ ਲਈ ਹੋਵੇ

ਫਾਇਨ ਟਿਊਨ ਜੌਬ ਕੇਵਲ GPU ਕੰਪਿਊਟ ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ। ਕੰਪਿਊਟ ਦਾ ਆਕਾਰ ਮਾਡਲ ਦੇ ਵੱਡੇ ਪੈਮਾਨੇ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ ਅਤੇ ਜ਼ਿਆਦਾਤਰ ਮਾਮਲਿਆਂ ਵਿੱਚ ਜੌਬ ਲਈ ਸਹੀ ਕੰਪਿਊਟ ਚੁਣਨਾ ਔਖਾ ਹੁੰਦਾ ਹੈ। ਇਸ ਸੈੱਲ ਵਿੱਚ ਵਰਤੋਂਕਾਰ ਨੂੰ ਸਹੀ ਕੰਪਿਊਟ ਚੁਣਨ ਲਈ ਮਦਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

> [!NOTE]
> ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਪਿਊਟ ਸਭ ਤੋਂ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਸੰਰਚਨਾ ਨਾਲ ਕੰਮ ਕਰਦੇ ਹਨ। ਸੰਰਚਨਾ ਵਿੱਚ ਕੋਈ ਵੀ ਬਦਲਾਅ CUDA Out Of Memory ਗਲਤੀ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦਾ ਹੈ। ਅਜਿਹੇ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਕੰਪਿਊਟ ਨੂੰ ਵੱਡੇ ਆਕਾਰ ਵਾਲੇ ਕੰਪਿਊਟ 'ਤੇ ਅਪਗ੍ਰੇਡ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।

> [!NOTE]
> ਕੰਪਿਊਟ ਕੁਲਸਾਈਜ਼ ਚੁਣਦੇ ਸਮੇਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਕੰਪਿਊਟ ਤੁਹਾਡੇ ਰਿਸੋਰਸ ਗਰੁੱਪ ਵਿੱਚ ਉਪਲੱਬਧ ਹੈ। ਜੇ ਕੋਈ ਵਿਸ਼ੇਸ਼ ਕੰਪਿਊਟ ਉਪਲੱਬਧ ਨਹੀਂ, ਤਾਂ ਤੁਰੰਤ ਇਸ ਕੰਪਿਊਟ ਸਰੋਤਾਂ ਤੱਕ ਪਹੁੰਚ ਲਈ ਬੇਨਤੀ ਕਰੋ।

### ਫਾਇਨ ਟਿਊਨ ਸਹਾਇਤਾ ਲਈ ਮਾਡਲ ਜਾਂਚਣਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure ML ਮਾਡਲ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਦਾ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ ਇਹ ਹੈ:

    - ਇਹ ast ਮੋਡੀਊਲ ਆਯਾਤ ਕਰਦਾ ਹੈ ਜੋ Python ਦਾ ਅਬਸਟ੍ਰੈਕਟ ਸਿੰਟੈਕਸ ਟ੍ਰੀ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ ਦੇਖਦਾ ਹੈ ਕਿ foundation_model (ਜੋ Azure ML ਦੇ ਮਾਡਲ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ) ਵਿੱਚ finetune_compute_allow_list ਨਾਂਮਕ ਟੈਗ ਮੌਜੂਦ ਹੈ ਜਾਂ ਨਹੀਂ। Azure ML ਵਿੱਚ ਟੈਗ ਕੁੰਜੀ-ਮੁੱਲ ਜੋੜੇ ਹੁੰਦੇ ਹਨ ਜੋ ਮਾਡਲਾਂ ਬਾਰੇ ਛਾਂਟ ਅਤੇ ਵੱਖਰਾ ਕਰਨ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

    - ਜੇ finetune_compute_allow_list ਟੈਗ ਮੌਜੂਦ ਹੈ, ਤਾਂ ਇਹ ast.literal_eval ਨਾਲ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਟੈਗ ਮੁੱਲ (ਸਟ੍ਰਿੰਗ) ਨੂੰ Python ਸੂਚੀ ਵਿੱਚ ਬਦਲਦਾ ਹੈ। ਇਸ ਸੂਚੀ ਨੂੰ computes_allow_list ਵਿੱਚ ਰੱਖਦਾ ਹੈ। ਫਿਰ ਇਹ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਕਿ ਕੰਪਿਊਟ ਦੀ ਸੂਚੀ ਤੋਂ ਬਣਾਉਣਾ ਹੈ।

    - ਜੇ finetune_compute_allow_list ਟੈਗ ਮੌਜੂਦ ਨਹੀਂ, ਤਾਂ computes_allow_list ਨੂੰ None ਸੈੱਟ ਕਰਦਾ ਹੈ ਅਤੇ ਸੁਨੇਹਾ ਦਿੰਦਾ ਹੈ ਕਿ finetune_compute_allow_list ਟੈਗ ਮਾਡਲ ਦੇ ਟੈਗਸ ਦਾ ਹਿੱਸਾ ਨਹੀਂ ਹੈ।

    - ਸਮਾਪਤੀ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਮਾਡਲ ਮੈਟਾਡੇਟਾ ਵਿੱਚ ਖਾਸ ਟੈਗ ਚੈੱਕ ਕਰ ਰਿਹਾ ਹੈ, ਟੈਗ ਦੀ ਕਦਰ ਨੂੰ ਸੂਚੀ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਜੇ ਮੌਜੂਦ ਹੋਵੇ, ਅਤੇ ਉਪਭੋਗਤਾ ਨੂੰ ਸੂਚਨਾ ਦਿੰਦਾ ਹੈ।

    ```python
    # ast ਮੌਡੀਊਲ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ, ਜੋ ਪਾਇਥਨ ਅਧਾਰਭੂਤ ਵਿਆਕਰਨ ਦੇ ਵ੍ਰਿਕਸ਼ਾਂ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨ ਦਿੰਦਾ ਹੈ
    import ast
    
    # ਚੈੱਕ ਕਰੋ ਕਿ ਮਾਡਲ ਦੇ ਟੈਗਾਂ ਵਿੱਚ 'finetune_compute_allow_list' ਟੈਗ ਮੌਜੂਦ ਹੈ ਜਾਂ ਨਹੀਂ
    if "finetune_compute_allow_list" in foundation_model.tags:
        # ਜੇਕਰ ਟੈਗ ਮੌਜੂਦ ਹੈ, ਤਾਂ ast.literal_eval ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੈਗ ਦੇ ਮੁੱਲ (ਇੱਕ ਸਤਰ) ਨੂੰ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਪਾਇਥਨ ਲਿਸਟ ਵਿੱਚ ਪਾਰਸ ਕਰੋ
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # ਸਤਰ ਨੂੰ ਪਾਇਥਨ ਲਿਸਟ ਵਿੱਚ ਬਦਲੋ
        # ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰੋ ਜਿਸ ਵਿੱਚ ਦੱਸਿਆ ਗਿਆ ਹੈ ਕਿ ਲਿਸਟ ਤੋਂ ਇੱਕ ਕਮਪਿਊਟ ਬਣਾਇਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # ਜੇ ਟੈਗ ਮੌਜੂਦ ਨਹੀਂ ਹੈ ਤਾਂ computes_allow_list ਨੂੰ None ਸੈੱਟ ਕਰੋ
        computes_allow_list = None
        # ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰੋ ਕਿ 'finetune_compute_allow_list' ਟੈਗ ਮਾਡਲ ਦੇ ਟੈਗਾਂ ਦਾ ਹਿੱਸਾ ਨਹੀਂ ਹੈ
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਜਾਂਚਣਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure ML ਸੇਵਾ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਦਾ ਹੈ ਅਤੇ ਇੱਕ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਤੇ ਕਈ ਚੈੱਕ ਕਰਦਾ ਹੈ। ਇਹਦਾ ਖਾਕਾ ਇਹ ਹੈ:

    - ਇਹ compute_cluster ਨਾਂ ਦੇ ਅੰਦਰ ਰੱਖੇ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਨੂੰ ਵਰਕਸਪੇਸ ਤੋਂ ਪ੍ਰਾਪਤ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ। ਜੇ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਦੀ ਪ੍ਰੋਵਿਜ਼ਨਿੰਗ ਸਥਿਤੀ "failed" ਹੈ, ਤਾਂ ValueError ਥ੍ਰੋ ਕਰਦਾ ਹੈ।

    - ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ computes_allow_list None ਨਹੀਂ ਹੈ। ਜੇ ਨਹੀਂ, ਤਾਂ ਸੂਚੀ ਦੇ ਸਾਰੇ ਕੰਪਿਊਟ ਆਕਾਰ ਨੀਵਾਂ ਕੇਸ ਕਰਕੇ ਮੌਜੂਦਾ ਕੰਪਿਊਟ ਆਕਾਰ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ। ਜੇ ਇਹ ਨਹੀਂ ਹੈ, ਤਾਂ ValueError ਫੇਂਕਦਾ ਹੈ।

    - ਜੇ computes_allow_list None ਹੈ, ਤਾਂ ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ ਕੰਪਿਊਟ ਆਕਾਰ ਅਣਸਮਰਥਤ GPU VM ਆਕਾਰਾਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਹੈ ਜਾਂ ਨਹੀਂ। ਜੇ ਹਾਂ, ਤਾ ValueError ਫੇਂਕਦਾ ਹੈ।

    - ਇਹ ਵਰਕਸਪੇਸ ਵਿੱਚ ਸਭ ਉਪਲੱਬਧ ਕੰਪਿਊਟ ਆਕਾਰਾਂ ਦੀ ਸੂਚੀ ਲੈਂਦਾ ਹੈ। ਫਿਰ ਇਸ ਸੂਚੀ ਵਿੱਚੋਂ ਪ੍ਰਤੀ ਇੱਕ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ ਕਿ ਉਸ ਦਾ ਨਾਮ ਮੌਜੂਦਾ ਕੰਪਿਊਟ ਦੇ ਆਕਾਰ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਕਿ ਨਹੀਂ। ਜੇ ਮੇਲ ਖਾਂਦਾ ਹੈ ਤਾਂ ਉਸ ਕੰਪਿਊਟ ਆਕਾਰ ਲਈ GPU ਦੀ ਗਿਣਤੀ ਲੈ ਕੇ gpu_count_found ਨੂੰ ਸੱਚ ਕਰਦਾ ਹੈ।

    - ਜੇ gpu_count_found ਸੱਚ ਹੈ, ਤਾਂ ਕੰਪਿਊਟ ਵਿੱਚ GPU ਦੀ ਗਿਣਤੀ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ। ਨਹੀਂ ਤਾਂ ValueError ਲਾਉਂਦਾ ਹੈ।

    - ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ Azure ML ਵਰਕਸਪੇਸ ਵਿੱਚ ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਦੀ ਸਥਿਤੀ, ਆਕਾਰ, ਇਜਾਜ਼ਤ ਯੋਗਤਾ ਅਤੇ GPU ਗਿਣਤੀ ਦੀ ਜਾਂਚ ਕਰ ਰਿਹਾ ਹੈ।

    ```python
    # ਐਕਸੈਪਸ਼ਨ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰੋ
    print(e)
    # ਜੇ ਲੇਖਾਸਾਧਨ ਸਾਈਜ਼ ਵਰਕਸਪੇਸ ਵਿੱਚ ਉਪਲਬਧ ਨਹੀਂ ਹੈ ਤਾਂ ValueError ਉਠਾਓ
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML ਵਰਕਸਪੇਸ ਤੋਂ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਪ੍ਰਾਪਤ ਕਰੋ
    compute = workspace_ml_client.compute.get(compute_cluster)
    # ਜਾਂਚੋ ਕਿ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਦੀ ਪ੍ਰੋਵਿਜ਼ਨਿੰਗ ਸਥਿਤੀ "ਫੇਲ" ਹੈ ਕਿ ਨਹੀਂ
    if compute.provisioning_state.lower() == "failed":
        # ਜੇ ਪ੍ਰੋਵਿਜ਼ਨਿੰਗ ਸਥਿਤੀ "ਫੇਲ" ਹੈ ਤਾਂ ValueError ਉਠਾਓ
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # ਜਾਂਚੋ ਕਿ computes_allow_list ਨਲ ਨਹੀਂ ਹੈ
    if computes_allow_list is not None:
        # computes_allow_list ਵਿਚ ਸਾਰੇ ਲੇਖਾਸਾਧਨ ਸਾਈਜ਼ ਨੂੰ ਲੋਅਰਕੇਸ ਵਿੱਚ ਬਦਲੋ
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # ਜਾਂਚੋ ਕਿ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਦਾ ਸਾਈਜ਼ computes_allow_list_lower_case ਵਿੱਚ ਹੈ ਕਿ ਨਹੀਂ
        if compute.size.lower() not in computes_allow_list_lower_case:
            # ਜੇ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਦਾ ਸਾਈਜ਼ computes_allow_list_lower_case ਵਿੱਚ ਨਹੀਂ ਹੈ ਤਾਂ ValueError ਉਠਾਓ
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # ਅਸਮਰਥਿਤ GPU VM ਸਾਈਜ਼ਾਂ ਦੀ ਸੂਚੀ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # ਜਾਂਚੋ ਕਿ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਦਾ ਸਾਈਜ਼ unsupported_gpu_vm_list ਵਿੱਚ ਹੈ ਕਿ ਨਹੀਂ
        if compute.size.lower() in unsupported_gpu_vm_list:
            # ਜੇ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਦਾ ਸਾਈਜ਼ unsupported_gpu_vm_list ਵਿੱਚ ਹੈ ਤਾਂ ValueError ਉਠਾਓ
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # ਇੱਕ ਫਲੈਗ ਸ਼ੁਰੂ ਕਰੋ ਕਿ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਵਿੱਚ GPUs ਦੀ ਗਿਣਤੀ ਮਿਲ ਗਈ ਹੈ ਜਾਂ ਨਹੀਂ
    gpu_count_found = False
    # ਵਰਕਸਪੇਸ ਵਿੱਚ ਉਪਲਬਧ ਸਾਰੇ ਲੇਖਾਸਾਧਨ ਸਾਈਜ਼ਾਂ ਦੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # ਉਪਲਬਧ ਲੇਖਾਸਾਧਨ ਸਾਈਜ਼ਾਂ ਦੀ ਸੂਚੀ 'ਤੇ ਇਤਰਾਏਟ ਕਰੋ
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # ਜਾਂਚੋ ਕਿ ਲੇਖਾਸਾਧਨ ਸਾਈਜ਼ ਦਾ ਨਾਮ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਦੇ ਸਾਈਜ਼ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਕਿ ਨਹੀਂ
        if compute_sku.name.lower() == compute.size.lower():
            # ਜੇ ਕਰਦਾ ਹੈ, ਉਸ ਲੇਖਾਸਾਧਨ ਸਾਈਜ਼ ਲਈ GPUs ਦੀ ਗਿਣਤੀ ਪ੍ਰਾਪਤ ਕਰੋ ਅਤੇ gpu_count_found ਨੂੰ ਸੱਚਾਓ
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # ਜੇ gpu_count_found ਸੱਚ ਹੈ, ਤਾਂ ਲੇਖਾਸਾਧਨ ਉਦਾਹਰਨ ਵਿੱਚ GPUs ਦੀ ਗਿਣਤੀ ਪ੍ਰਿੰਟ ਕਰੋ
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # ਜੇ gpu_count_found ਝੂਠ ਹੈ, ਤਾਂ ValueError ਉਠਾਓ
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. ਮਾਡਲ ਦੀ ਫਾਇਨ-ਟਿਊਨਿੰਗ ਲਈ ਡੇਟਾਸੈੱਟ ਚੁਣੋ

1. ਅਸੀਂ ultrachat_200k ਡੇਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ। ਡੇਟਾਸੈੱਟ ਵਿੱਚ ਚਾਰ ਵੰਡ ਹਨ ਜੋ Supervised fine-tuning (sft) ਲਈ ਉਚਿਤ ਹਨ।
Generation ranking (gen). ਹਰ ਵੰਡ ਵਿੱਚ ਉਦਾਹਰਣਾਂ ਦੀ ਗਿਣਤੀ ਹੇਠਾਂ ਦਿੱਤੀ ਹੈ:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. ਆਗਲੇ ਕੁਝ ਸੈੱਲ ਫਾਇਨ ਟਿਊਨ ਲਈ ਬੁਨਿਆਦੀ ਡੇਟਾ ਤਿਆਰੀ ਦਿਖਾਉਂਦੇ ਹਨ:

### ਕੁਝ ਡੇਟਾ ਲਾਈਨਾਂ ਦਰਸਾਉਣਾ

ਸਾਡਾ ਮਕਸਦ ਹੈ ਕਿ ਇਹ ਨਮੂਨਾ ਤੇਜ਼ ਚੱਲੇ, ਇਸ ਲਈ train_sft ਅਤੇ test_sft ਫਾਈਲਾਂ ਨੂੰ ਸੰਭਾਲੋ ਜੋ ਪਹਿਲਾਂ ਤੋਂ ਛਣੇ ਹੋਏ ਕਤਾਰਾਂ ਦੇ 5% ਸਮੇਤ ਹਨ। ਇਸਦਾ ਅਰਥ ਹੈ ਕਿ ਫਾਇਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਘੱਟ ਸ਼ੁੱਧਤਾ ਵਾਲਾ ਹੋਵੇਗਾ, ਇਸ ਲਈ ਇਸਨੂੰ ਅਸਲ ਜਗਤ ਵਿੱਚ ਵਰਤਣਾ ਨਹੀਂ ਚਾਹੀਦਾ।
download-dataset.py ਸਕ੍ਰਿਪਟ ultrachat_200k ਡੇਟਾਸੈੱਟ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰਨ ਅਤੇ ਡੇਟਾਸੈੱਟ ਨੂੰ ਫਾਇਨਟਿਊਨ ਪਾਈਪਲਾਈਨ ਕੰਪੋਨੈਂਟ ਲਈ ਉਪਯੋਗੀ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਨਾਲ ਹੀ ਕਿਉਂਕਿ ਡੇਟਾਸੈੱਟ ਵੱਡਾ ਹੈ, ਇਸ ਲਈ ਸਾਡੇ ਕੋਲ ਇਹਦਾ ਪਰਤਿਮਾ ਹੀ ਹੈ।

1. ਹੇਠਾਂ ਦਿੱਤਾ ਸਕ੍ਰਿਪਟ ਕੇਵਲ 5% ਡੇਟਾ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ। ਇਸਨੂੰ dataset_split_pc ਪੈਰਾਮੀਟਰ ਬਦਲ ਕੇ ਵਧਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

> [!NOTE]
> ਕੁਝ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਵਿੱਚ ਵੱਖ-ਵੱਖ ਭਾਸ਼ਾ ਕੋਡ ਹੁੰਦੇ ਹਨ, ਇਸ ਲਈ ਡੇਟਾਸੈੱਟ ਵਿੱਚ ਕਾਲਮ ਦੇ ਨਾਮ ਉਹੀ ਦਰਸਾਉਣੇ ਚਾਹੀਦੇ ਹਨ।

1. ਇਹ ਇੱਕ ਉਦਾਹਰਣ ਹੈ ਕਿ ਡੇਟਾ ਕਿਵੇਂ ਦਿਖਣਾ ਚਾਹੀਦਾ ਹੈ
ਚੈਟ-ਕੰਪਲੀਸ਼ਨ ਡੇਟਾਸੈੱਟ ਨੂੰ parquet ਫਾਰਮੈਟ ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਿਸ ਵਿੱਚ ਹਰ ਐਂਟਰੀ ਹੇਠਾਂ ਦਿੱਤੇ ਸਕੀਮਾ ਅਨੁਸਾਰ ਹੈ:

    - ਇਹ ਇੱਕ JSON (ਜਾਵਾਸਕ੍ਰਿਪਟ ਆਬਜੈਕਟ ਨੋਟੇਸ਼ਨ) ਦਸਤਾਵੇਜ਼ ਹੈ, ਜੋ ਕਿ ਡੇਟਾ ਦਾ ਪ੍ਰਸਿੱਧ ਬਦਲਾਅ ਫਾਰਮੈਟ ਹੈ। ਇਹ ਚਲਾਉਣਯੋਗ ਕੋਡ ਨਹੀਂ ਹੈ, ਪਰ ਡੇਟਾ ਸਟੋਰ ਅਤੇ ਪ੍ਰੇਰਣਾ ਦਾ ਤਰੀਕਾ ਹੈ। ਇਹਦੀ ਬਣਤਰ:

    - "prompt": ਇਹ ਕੁੰਜੀ ਇੱਕ ਸਟਰਿੰਗ ਮੁੱਲ ਰੱਖਦੀ ਹੈ ਜੋ AI ਸਹਾਇਤਾ ਲਈ ਟਾਸਕ ਜਾਂ ਸਵਾਲ ਨੂੰ ਦਰਸਾਉਂਦੀ ਹੈ।

    - "messages": ਇਹ ਕੁੰਜੀ ਇੱਕ	objects ਦੀ ਅਰੇ ਰੱਖਦੀ ਹੈ। ਹਰ objcct ਗੱਲਬਾਤ ਵਿੱਚ ਇੱਕ ਸੁਨੇਹਾ ਦਰਸਾਉਂਦਾ ਹੈ ਜੋ ਉਪਭੋਗੀ ਅਤੇ AI ਸਹਾਇਤਾ ਵਿਚਕਾਰ ਹੁੰਦੀ ਹੈ। ਹਰ ਸੁਨੇਹਾ objcct ਵਿੱਚ ਦੋ ਕੁੰਜੀਆਂ ਹੁੰਦੀਆਂ ਹਨ:

    - "content": ਇਹ ਸੁਨੇਹਾ ਦੀ ਸਮੱਗਰੀ ਨੂੰ ਦਰਸਾਉਂਦਾ ਸਟਰਿੰਗ ਮੁੱਲ ਹੈ।
    - "role": ਇਹ ਸੁਨੇਹਾ ਭੇਜਣ ਵਾਲੇ ਦੀ ਭੂਮਿਕਾ ਨੂੰ ਦਰਸਾਉਂਦਾ ਸਟਰਿੰਗ ਮੁੱਲ ਹੈ। ਇਹ "user" ਜਾਂ "assistant" ਹੋ ਸਕਦੀ ਹੈ।
    - "prompt_id": ਇਹ ਇੱਕ ਵਿਲੱਖਣ ਪਛਾਣਕਰਤਾ ਹੈ ਜੋ ਪ੍ਰਾਮਪਟ ਲਈ ਹੈ।

1. ਇਸ ਵਿਸ਼ੇਸ਼ JSON ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਇੱਕ ਗੱਲਬਾਤ ਦਰਸਾਈ ਗਈ ਹੈ ਜਿੱਥੇ ਇੱਕ ਉਪਭੋਗੀ AI ਸਹਾਇਤਾ ਨੂੰ ਇੱਕ ਡਿਸਟੋਪੀਆਨ ਕਹਾਣੀ ਲਈ ਪ੍ਰਮੁੱਖ ਪਾਤਰ ਬਣਾਉਣ ਲਈ ਕਹਿੰਦਾ ਹੈ। ਸਹਾਇਤਾ ਜਵਾਬ ਦਿੰਦਾ ਹੈ, ਫਿਰ ਉਪਭੋਗੀ ਵਧੇਰੇ ਵੇਰਵੇ ਮੰਗਦਾ ਹੈ। ਸਹਾਇਤਾ ਵਧੇਰੇ ਵੇਰਵੇ ਦੇਣ ਲਈ ਸਹਿਮਤ ਹੁੰਦੀ ਹੈ। ਪੂਰੀ ਗੱਲਬਾਤ ਕਿਸੇ ਖਾਸ prompt id ਨਾਲ ਜੁੜੀ ਹੈ।

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### ਡਾਟਾ ਡਾਊਨਲੋਡ ਕਰਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ download-dataset.py ਸਹਾਇਕ ਸਕ੍ਰਿਪਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡੇਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰਨ ਲਈ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ:

    - ਇਹ os ਮੋਡੀਊਲ ਆਯਾਤ ਕਰਦਾ ਹੈ, ਜੋ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨਾਲ ਸੰਬੰਧਿਤ ਕਾਰਜਾਂ ਲਈ ਹੈ।

    - ਇਹ os.system ਫੰਕਸ਼ਨ ਨਾਲ download-dataset.py ਸਕ੍ਰਿਪਟ ਚਲਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਕਮਾਨਡ ਲਾਈਨ ਦਲੀਲਾਂ ਹਨ: ਡਾਊਨਲੋਡ ਕਰਨ ਵਾਲਾ ਡੇਟਾਸੈੱਟ (HuggingFaceH4/ultrachat_200k), ਉਸ ਡਾਇਰੈਕਟਰੀ ਦਾ ਨਾਮ ਜਿੱਥੇ ਡਾਊਨਲੋਡ ਕਰਨਾ ਹੈ (ultrachat_200k_dataset), ਅਤੇ ਡੇਟਾਸੈੱਟ ਦਾ ਕਿਸ ਹਿੱਸੇ ਦਾ ਅੰਸ਼ (5%)। os.system ਕਮਾਂਡ ਦਾ ਐਕਜ਼ਿਟ ਸਥਿਤੀ ਦਿੰਦਾ ਹੈ ਜੋ exit_status ਵੈਰੀਏਬਲ ਵਿੱਚ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ।

    - ਯੇਖੇ ਜਾਂਦਾ ਹੈ ਕਿ exit_status 0 ਤੋਂ ਵੱਖਰਾ ਤਾਂ ਨਹੀਂ। linux-ਜੈਸੀਆਂ ਸਿਸਟਮਾਂ ਵਿੱਚ 0 ਕਾਮਯਾਬੀ ਦਾ ਸੰਕੇਤ ਹੈ, ਹੋਰ ਕੋਈ ਵੀ ਗਲਤੀ ਹੁੰਦੀ ਹੈ। ਜੇ exit_status 0 ਨਹੀਂ ਤਾਂ Exception ਛੱਡਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਡਾਊਨਲੋਡ ਵਿੱਚ ਸਮੱਸਿਆ ਦਰਸਾਈ ਜਾਂਦੀ ਹੈ।

    - ਖੁਲਾਸਾ, ਇਹ ਸਕ੍ਰਿਪਟ ਸਹਾਇਕ ਸਕ੍ਰਿਪਟ ਦੇ ਨਾਲ ਡੇਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ ਜੇ ਕੰਮ ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ ਐਸਪਸ਼ਨ ਲਾਂਦਾ ਹੈ।

    ```python
    # os ਮੌਡਿਊਲ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ, ਜੋ ਕਿ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨਾਲ ਸੰਬੰਧਤ ਕਾਰਜਕਾਰੀ ਵਿਧੀ ਦੇਣ ਦਾ ਤਰੀਕਾ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ
    import os
    
    # os.system ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ download-dataset.py ਸਕ੍ਰਿਪਟ ਨੂੰ ਖਾਸ ਕਮਾਂਡ-ਲਾਈਨ ਆਰਗਯੂਮੈਂਟਾਂ ਨਾਲ ਸ਼ੈੱਲ ਵਿੱਚ ਚਲਾਓ
    # ਆਰਗਯੂਮੈਂਟ ਦੱਸਦੇ ਹਨ ਕਿ ਕਿਹੜਾ ਡੈਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰਨਾ ਹੈ (HuggingFaceH4/ultrachat_200k), ਕਿਹੜੇ ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰਨਾ ਹੈ (ultrachat_200k_dataset), ਅਤੇ ਡੈਟਾਸੈੱਟ ਦਾ ਕਿੰਨਾ ਹਿੱਸਾ ਵੰਡਨਾ ਹੈ (5)
    # os.system ਫੰਕਸ਼ਨ ਉਸ ਕਮਾਂਡ ਦਾ ਐਗਜ਼ਿਟ ਸਟੇਟਸ ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੋ ਉਸਨੇ ਚਲਾਈ ਸੀ; ਇਹ ਸਟੇਟਸ exit_status ਵੈਰੀਏਬਲ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # ਚੈੱਕ ਕਰੋ ਕਿ exit_status 0 ਨਹੀਂ ਹੈ
    # ਯੂਨਿਕਸ-ਸਮਾਨ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ ਵਿੱਚ, 0 ਐਗਜ਼ਿਟ ਸਟੇਟਸ ਆਮ ਤੌਰ ਤੇ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਕਮਾਂਡ ਸਫਲ ਰਹੀ ਸੀ, ਜਦਕਿ ਹੋਰ ਕੋਈ ਵੀ ਨੰਬਰ ਗਲਤੀ ਦਰਸਾਉਂਦਾ ਹੈ
    # ਜੇ exit_status 0 ਨਹੀਂ ਹੈ, ਤਾਂ ਇੱਕ Exception ਉਠਾਓ ਜਿਸ ਵਿੱਚ ਇੱਕ ਸੁਨੇਹਾ ਹੋਵੇ ਕਿ ਡੈਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰਨ 'ਚ ਗਲਤੀ ਹੋਈ ਹੈ
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### ਡਾਟਾ ਨੂੰ DataFrame ਵਿੱਚ ਲੋਡ ਕਰਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ JSON Lines ਫਾਈਲ ਨੂੰ pandas DataFrame ਵਿੱਚ ਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ ਪਹਿਲੀਆਂ 5 ਲਾਈਨਾਂ ਦਿਖਾਉਂਦਾ ਹੈ। ਇਹਦਾ ਵੇਰਵਾ:

    - ਇਹ pandas ਲਾਇਬ੍ਰੇਰੀ ਆਯਾਤ ਕਰਦਾ ਹੈ ਜੋ ਡੇਟਾ ਵਿਵਸਥਾ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਹੈ।

    - pandas ਦੇ ਡਿਸਪਲੇਅ ਵਿਕਲਪਾਂ ਦੀ ਸਥਿਤੀ ਵਿੱਚ ਕਾਲਮ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਚੌੜਾਈ 0 ਸੈੱਟ ਕੀਤੀ ਹੈ। ਇਸਦਾ ਅਰਥ ਹੈ ਕਿ DataFrame ਪ੍ਰਿੰਟ ਕਰਦੇ ਵੇਲੇ ਕਾਲਮ ਦਾ ਪੂਰਾ ਟੈਕਸਟ ਕੱਟਿਆ ਨਹੀਂ ਜਾਵੇਗਾ।
- ਇਹ pd.read_json ਫੰਗਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ train_sft.jsonl ਫਾਇਲ ਨੂੰ ultrachat_200k_dataset ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਇੱਕ DataFrame ਵਿੱਚ ਲੋਡ ਕੀਤਾ ਜਾ ਸਕੇ। lines=True ਆਰਗਯੂਮੈਂਟ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਫਾਇਲ JSON Lines ਫਾਰਮੈਟ ਵਿੱਚ ਹੈ, ਜਿੱਥੇ ਹਰ ਲਾਈਨ ਇੱਕ ਵੱਖਰਾ JSON ਆਬਜੈਕਟ ਹੁੰਦੀ ਹੈ।

- ਇਹ head ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ DataFrame ਦੀਆਂ ਪਹਿਲੀਆਂ 5 ਪੰਗਤੀਆਂ ਦਿਖਾਈਆਂ ਜਾਣ। ਜੇ DataFrame ਵਿੱਚ 5 ਤੋਂ ਘੱਟ ਪੰਗਤੀਆਂ ਹਨ, ਤਾਂ ਇਹ ਸਾਰੀਆਂ ਦਿਖਾਈਆਂ ਜਾਣਗੀਆਂ।

- ਸੰਖੇਪ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ JSON Lines ਫਾਇਲ ਨੂੰ DataFrame ਵਿੱਚ ਲੋਡ ਕਰ ਰਿਹਾ ਹੈ ਅਤੇ ਪਹਿਲੀਆਂ 5 ਪੰਗਤੀਆਂ ਨੂੰ ਪੂਰੇ ਕਾਲਮ ਟੈਕਸਟ ਨਾਲ ਦਿਖਾ ਰਿਹਾ ਹੈ।
    
    ```python
    # pandas ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ, ਜੋ ਕਿ ਇੱਕ ਤਾਕਤਵਰ ਡਾਟਾ ਪ੍ਰਬੰਧਨ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਲਾਇਬ੍ਰੇਰੀ ਹੈ
    import pandas as pd
    
    # pandas ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਵਿਕਲਪਾਂ ਲਈ ਅਧਿਕਤਮ ਕਾਲਮ ਚੌੜਾਈ 0 ਤੇ ਸੈੱਟ ਕਰੋ
    # ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਜਦੋਂ DataFrame ਪ੍ਰਿੰਟ ਕੀਤਾ ਜਾਵੇਗਾ ਤਾਂ ਹਰੇਕ ਕਾਲਮ ਦਾ ਪੂਰਾ ਟੈਕਸਟ ਕਟਾਅ ਤੋਂ ਬਿਨਾਂ ਵਿਖਾਇਆ ਜਾਵੇਗਾ
    pd.set_option("display.max_colwidth", 0)
    
    # pd.read_json ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ultrachat_200k_dataset ਡਾਇਰੈਕਟਰੀ ਤੋਂ train_sft.jsonl ਫਾਇਲ ਨੂੰ DataFrame ਵਿੱਚ ਲੋਡ ਕਰੋ
    # lines=True ਦਲੀਲ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਫਾਇਲ JSON Lines ਫਾਰਮੈਟ ਵਿੱਚ ਹੈ, ਜਿੱਥੇ ਹਰ ਇਕ ਲਾਈਨ ਇੱਕ ਵੱਖਰਾ JSON ਆਬਜੈਕਟ ਹੁੰਦਾ ਹੈ
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # DataFrame ਦੀਆਂ ਪਹਿਲੀਆਂ 5 ਕਤਾਰਾਂ ਨੂੰ ਦਿਖਾਉਣ ਲਈ head ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰੋ
    # ਜੇ DataFrame ਵਿਚ 5 ਤੋਂ ਘੱਟ ਕਤਾਰਾਂ ਹਨ, ਤਾਂ ਇਹ ਸਭ ਨੂੰ ਦਿਖਾਏਗਾ
    df.head()
    ```

## 5. ਮਾਡਲ ਅਤੇ ਡੇਟਾ ਨੂੰ ਇਨਪੁੱਟ ਵਜੋਂ ਵਰਤਦੇ ਹੋਏ ਫਾਈਨ ਟਿਊਨਿੰਗ ਜਾਬ ਸਬਮਿਟ ਕਰੋ

ਉਹ ਜਾਬ ਬਣਾਓ ਜੋ chat-completion ਪਾਈਪਲਾਈਨ ਕੰਪੋਨੇਟ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਫਾਈਨ ਟਿਊਨਿੰਗ ਲਈ ਸਾਰੇ ਸਪੋਰਟਿਡ ਪੈਰਾਮੀਟਰਾਂ ਬਾਰੇ ਹੋਰ ਜਾਨਕਾਰੀ ਲਵੋ।

### ਫਾਈਨਟਿਊਨ ਪੈਰਾਮੀਟਰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ

1. ਫਾਈਨਟਿਊਨ ਪੈਰਾਮੀਟਰ ਦੋ ਸ਼੍ਰੇਣੀਆਂ ਵਿੱਚ ਵੰਡੇ ਜਾ ਸਕਦੇ ਹਨ - ਟ੍ਰੇਨਿੰਗ ਪੈਰਾਮੀਟਰ, ਅਪਟੀਮਾਈਜੇਸ਼ਨ ਪੈਰਾਮੀਟਰ

1. ਟ੍ਰੇਨਿੰਗ ਪੈਰਾਮੀਟਰ ਟ੍ਰੇਨਿੰਗ ਦੇ ਪੱਖਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਨ ਜਿਵੇਂ ਕਿ -

    - ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ optimizer, scheduler
    - ਫਾਈਨਟਿਊਨ ਨੂੰ optimize ਕਰਨ ਲਈ ਮੈਟਰਿਕ
    - ਟ੍ਰੇਨਿੰਗ ਕਦਮਾਂ ਦੀ ਗਿਣਤੀ ਅਤੇ ਬੈਚ ਆਕਾਰ ਆਦਿ
    - ਅਪਟੀਮਾਈਜੇਸ਼ਨ ਪੈਰਾਮੀਟਰ GPU ਮੈਮੋਰੀ ਨੂੰ optimize ਕਰਨ ਅਤੇ ਕਮਪਿਊਟ ਰਿਸੋর্সਾਂ ਦੀ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਵਰਤੋਂ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ।

1. ਹੇਠਾਂ ਕੁਝ ਉਹ ਪੈਰਾਮੀਟਰ ਦਿੱਤੇ ਗਏ ਹਨ ਜੋ ਇਸ ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹਨ। ਅਪਟੀਮਾਈਜੇਸ਼ਨ ਪੈਰਾਮੀਟਰ ਹਰ ਮਾਡਲ ਲਈ ਵੱਖਰੇ ਹੁੰਦੇ ਹਨ ਅਤੇ ਮਾਡਲ ਨਾਲ ਪੈਕੇਜ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਤਾਂ ਜੋ ਇਹ ਬਦਲਾਵ ਸਮਭਾਲੇ ਜਾ ਸਕਣ।

    - deepspeed ਅਤੇ LoRA ਨੂੰ ਚਾਲੂ ਕਰੋ
    - ਮਿਕਸਡ ਪ੍ਰਿਸੀਸ਼ਨ ਟ੍ਰੇਨਿੰਗ ਚਾਲੂ ਕਰੋ
    - ਮਲਟੀ-ਨੋਡ ਟ੍ਰੇਨਿੰਗ ਚਾਲੂ ਕਰੋ

> [!NOTE]
> ਸੁਪਰਵਾਈਜ਼ਡ ਫਾਈਨਟਿਊਨਿੰਗ ਨੇ alignment ਖੋਣ ਜਾਂ catastrophic forgetting ਦਾ ਨਤੀਜਾ ਦੇ ਸਕਦਾ ਹੈ। ਅਸੀਂ ਇਸ ਸਮੱਸਿਆ ਦੀ ਜਾਂਚ ਕਰਨ ਅਤੇ ਫਾਈਨਟਿਊਨ ਕਰਨ ਤੋਂ ਬਾਅਦ alignment ਸਟੇਜ ਚਲਾਉਣ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

### ਫਾਈਨ ਟਿਊਨਿੰਗ ਪੈਰਾਮੀਟਰ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਪੈਰਾਮੀਟਰ ਸੈਟ ਕਰ ਰਿਹਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

    - ਇਹ ਡਿਫਾਲਟ ਟ੍ਰੇਨਿੰਗ ਪੈਰਾਮੀਟਰ ਸੈਟ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਟ੍ਰੇਨਿੰਗ epochs ਦੀ ਗਿਣਤੀ, ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਇਵੈਲੂਏਸ਼ਨ ਲਈ ਬੈਚ ਸਾਈਜ਼, ਲਰਨਿੰਗ ਰੇਟ ਅਤੇ ਲਰਨਿੰਗ ਰੇਟ scheduler ਦੀ ਕਿਸਮ।

    - ਇਹ ਡਿਫਾਲਟ ਅਪਟੀਮਾਈਜੇਸ਼ਨ ਪੈਰਾਮੀਟਰ ਸੈਟ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਕਿ Layer-wise Relevance Propagation (LoRa) ਅਤੇ DeepSpeed ਲਾਗੂ ਕਰਨ ਦੀ ਸਥਿਤੀ, ਅਤੇ DeepSpeed ਦਾ ਸਟੇਜ।

    - ਇਹ ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਅਪਟੀਮਾਈਜੇਸ਼ਨ ਪੈਰਾਮੀਟਰ ਨੂੰ ਇੱਕ ਇਕੱਲੇ ਡਿਕਸ਼ਨਰੀ finetune_parameters ਵਿੱਚ ਜੋੜਦਾ ਹੈ।

    - ਇਹ ਚੈੱਕ ਕਰਦਾ ਹੈ ਕਿ foundation_model ਕੋਲ ਕੋਈ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਡਿਫਾਲਟ ਪੈਰਾਮੀਟਰ ਹਨ ਜਾਂ ਨਹੀਂ। ਜੇ ਹਨ, ਤਾਂ ਇਹ ਚੇਤਾਵਨੀ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਅਤੇ finetune_parameters ਡਿਕਸ਼ਨਰੀ ਨੂੰ ਇਹ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਡਿਫਾਲਟ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ। ast.literal_eval ਫੰਗਸ਼ਨ ਸਟ੍ਰਿੰਗ ਤੋਂ Python ਡਿਕਸ਼ਨਰੀ ਵਿੱਚ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਡਿਫਾਲਟਾਂ ਨੂੰ ਕਨਵਰਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ ਉਹ ਆਖਰੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪੈਰਾਮੀਟਰ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਜੋ ਰਨ ਲਈ ਵਰਤੇ ਜਾਣਗੇ।

    - ਸੰਖੇਪ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਪੈਰਾਮੀਟਰ ਸੈਟ ਅਤੇ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰ ਰਿਹਾ ਹੈ, ਜਦਕਿ ਡਿਫਾਲਟ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਨਾਲ ਉੱਤੇ ਲਿਖਣ ਦੀ ਸਮਰੱਥਾ ਨਾਲ।

    ```python
    # ਟ੍ਰੈਨਿੰਗ ਸਮੇਂ ਦੀ ਗਿਣਤੀ, ਟ੍ਰੈਨਿੰਗ ਅਤੇ ਮੁਲਾਂਕਣ ਲਈ ਬੈਚ ਸਾਈਜ਼, ਲਰਨਿੰਗ ਰੇਟ ਅਤੇ ਲਰਨਿੰਗ ਰੇਟ ਸਕੈਜੂਲਰ ਕਿਸਮ ਵਰਗੇ ਮੂਲ ਟ੍ਰੈਨਿੰਗ ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰੋ
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # ਅਪਟਾਈਮੇਜ਼ੇਸ਼ਨ ਦੇ ਮੂਲ ਪੈਰਾਮੀਟਰ ਸੈੱਟ ਕਰੋ ਜਿਵੇਂ ਕਿ Layer-wise Relevance Propagation (LoRa) ਅਤੇ DeepSpeed ਲਾਗੂ ਕਰਨਾ ਹੈ ਜਾਂ ਨਹੀਂ, ਅਤੇ DeepSpeed ਦਾ ਪੱਧਰ
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # ਟ੍ਰੈਨਿੰਗ ਅਤੇ ਅਪਟਾਈਮੇਜ਼ੇਸ਼ਨ ਪੈਰਾਮੀਟਰ ਨੂੰ finetune_parameters ਨਾਮਕ ਇੱਕੋ ਡਿਕਸ਼ਨਰੀ ਵਿੱਚ ਮਿਲਾਓ
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # ਦੇਖੋ ਕਿ foundation_model ਕੋਲ ਕੋਈ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਮੂਲ ਪੈਰਾਮੀਟਰ ਹਨ ਜਾਂ ਨਹੀਂ
    # ਜੇ ਹਨ, ਤਾਂ ਚੇਤਾਵਨੀ ਸੁਨੇਹਾ ਛਾਪੋ ਅਤੇ finetune_parameters ਡਿਕਸ਼ਨਰੀ ਨੂੰ ਇਹ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਮੂਲ ਪੈਰਾਮੀਟਰ ਨਾਲ ਅਪਡੇਟ ਕਰੋ
    # ast.literal_eval ਫੰਕਸ਼ਨ ਮਾਡਲ-ਵਿਸ਼ੇਸ਼ ਮੂਲ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸਟਰਿੰਗ ਤੋਂ ਪਾਇਥਨ ਡਿਕਸ਼ਨਰੀ ਵਿੱਚ ਬਦਲਣ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # ਸਟਰਿੰਗ ਨੂੰ ਪਾਇਥਨ ਡਿਕਸ਼ਨਰੀ ਵਿੱਚ ਬਦਲੋ
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦੇ ਅੰਤਮ ਪੈਰਾਮੀਟਰਾਂ ਦਾ ਸੈੱਟ ਛਾਪੋ ਜੋ ਚਲਾਉਣ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### ਟ੍ਰੇਨਿੰਗ ਪਾਈਪਲਾਈਨ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਇੱਕ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰ ਰਿਹਾ ਹੈ ਜੋ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਟ੍ਰੇਨਿੰਗ ਪਾਈਪਲਾਈਨ ਲਈ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਂਦਾ ਹੈ, ਅਤੇ ਫਿਰ ਇਸ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਕੇ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਂਦਾ ਅਤੇ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

1. get_pipeline_display_name ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ ਫੰਕਸ਼ਨ ਵੱਖ-ਵੱਖ ਟ੍ਰੇਨਿੰਗ ਪਾਈਪਲਾਈਨ ਨਾਲ ਸੰਬੰਧਿਤ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਆਧਾਰ ‘ਤੇ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਂਦਾ ਹੈ।

1. ਫੰਕਸ਼ਨ ਦੇ ਅੰਦਰ, ਇਹ ਕੁੱਲ ਬੈਚ ਸਾਈਜ਼ ਗਣਾ ਕਰਦਾ ਹੈ ਜੋ ਪ੍ਰਤੀ ਡਿਵਾਈਸ ਬੈਚ ਸਾਈਜ਼, gradient accumulation ਕਦਮਾਂ ਦੀ ਗਿਣਤੀ, ਹਰ ਨੋਡ ਦੇ GPU ਦੀ ਗਿਣਤੀ, ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਵਰਤੇ ਗਏ ਨੋਡਾਂ ਦੀ ਗਿਣਤੀ ਨਾਲ ਗੁਣਾ ਕਰਕੇ ਪ੍ਰਾਪਤ ਹੁੰਦੀ ਹੈ।

1. ਇਹ ਹੋਰ ਪੈਰਾਮੀਟਰ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਲਰਨਿੰਗ ਰੇਟ scheduler ਦੀ ਕਿਸਮ, DeepSpeed ਲਾਗੂ ਹੋਣਾ, DeepSpeed ਸਟੇਜ, Layer-wise Relevance Propagation (LoRa) ਲਾਗੂ ਹੋਣਾ, ਰੱਖਣ ਲਈ ਮਾਡਲ ਚੈੱਕਪੋਇੰਟ ਦੀ ਗਿਣਤੀ ਦੀ ਸੀਮਾ, ਅਤੇ ਵੱਧ ਤੋਂ ਵੱਧ ਸੀਕਵੇਂਸ ਲੰਬਾਈ।

1. ਇਹ ਸਾਰੇ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਇੱਕ ਸਟ੍ਰਿੰਗ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਹਾਈਫਨੋਂ ਨਾਲ ਵੱਖਰਾ ਹੁੰਦੀ ਹੈ। ਜੇ DeepSpeed ਜਾਂ LoRa ਲਾਗੂ ਹੈ, ਤਾਂ ਸਟ੍ਰਿੰਗ “ds” ਨਾਲ DeepSpeed ਸਟੇਜ ਜਾਂ “lora” ਸ਼ਾਮਿਲ ਕਰਦੀ ਹੈ। ਨਹੀਂ ਤਾਂ ਇਹ “nods” ਜਾਂ “nolora” ਸ਼ਾਮਿਲ ਕਰਦੀ ਹੈ।

1. ਫੰਕਸ਼ਨ ਇਸ ਸਟ੍ਰਿੰਗ ਨੂੰ ਵਾਪਸ ਕਰਦਾ ਹੈ, ਜੋ ਟ੍ਰੇਨਿੰਗ ਪਾਈਪਲਾਈਨ ਲਈ ਡਿਸਪਲੇ ਨਾਮ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ।

1. ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਇਸਨੂੰ ਕਾਲ ਕਰਕੇ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾ ਕੇ ਪ੍ਰਿੰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

1. ਤੇਜ਼ੀ ਨਾਲ, ਇਹ ਸਕ੍ਰਿਪਟ ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਆਧਾਰ ‘ਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਟ੍ਰੇਨਿੰਗ ਪਾਈਪਲਾਈਨ ਲਈ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਂਦਾ ਅਤੇ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

    ```python
    # ਟ੍ਰੇਨਿੰਗ ਪਾਈਪਲਾਈਨ ਲਈ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਣ ਲਈ ਇੱਕ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
    def get_pipeline_display_name():
        # ਪ੍ਰਤੀ ਡਿਵਾਈਸ ਬੈਚ ਸਾਈਜ਼, ਗ੍ਰੇਡੀਐਂਟ ਇਕੱਤਰ ਕਰਨ ਦੇ ਕਦਮਾਂ ਦੀ ਗਿਣਤੀ, ਪ੍ਰਤੀ ਨੋਡ GPU ਦੀ ਗਿਣਤੀ ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਵਰਤੇ ਗਏ ਨੋਡਾਂ ਦੀ ਸੰਖਿਆ ਨੂੰ ਗੁਣਾ ਕਰਕੇ ਕੁੱਲ ਬੈਚ ਸਾਈਜ਼ ਦਾ ਹਿਸਾਬ ਲਗਾਓ
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # ਲਰਨਿੰਗ ਰੇਟ ਸ਼ੈਡੀਊਲਰ ਕਿਸਮ ਪ੍ਰਾਪਤ ਕਰੋ
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # ਜਾਣੋ ਕਿ ਕੀ DeepSpeed ਲਾਗੂ ਕੀਤਾ ਗਿਆ ਹੈ
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # DeepSpeed ਸਟੇਜ ਪ੍ਰਾਪਤ ਕਰੋ
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # ਜੇ DeepSpeed ਲਾਗੂ ਕੀਤਾ ਗਿਆ ਹੈ, ਡਿਸਪਲੇ ਨਾਮ ਵਿੱਚ "ds" ਅਤੇ DeepSpeed ਸਟੇਜ ਸ਼ਾਮਲ ਕਰੋ; ਨਹੀਂ ਤਾਂ "nods" ਸ਼ਾਮਲ ਕਰੋ
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # ਜਾਣੋ ਕਿ ਕੀ Layer-wise Relevance Propagation (LoRa) ਲਾਗੂ ਕੀਤਾ ਗਿਆ ਹੈ
        lora = finetune_parameters.get("apply_lora", "false")
        # ਜੇ LoRa ਲਾਗੂ ਹੈ, ਡਿਸਪਲੇ ਨਾਮ ਵਿੱਚ "lora" ਸ਼ਾਮਲ ਕਰੋ; ਨਹੀਂ ਤਾਂ "nolora" ਸ਼ਾਮਲ ਕਰੋ
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # ਮਾਡਲ ਚੈਕਪੌਇੰਟ ਦੀ ਸੰਖਿਆ 'ਤੇ ਸੀਮਾ ਪ੍ਰਾਪਤ ਕਰੋ ਜੋ ਰੱਖੀ ਜਾਵੇ
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # ਵੱਧ ਤੋਂ ਵੱਧ ਸੀਕਵੈਂਸ ਲੰਬਾਈ ਪ੍ਰਾਪਤ ਕਰੋ
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # ਇਹ ਸਾਰੇ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਹਾਈਫਨ ਨਾਲ ਜੋੜ ਕੇ ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਓ
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
    
    # ਡਿਸਪਲੇ ਨਾਮ ਬਣਾਉਣ ਲਈ ਫੰਕਸ਼ਨ ਨੂੰ ਕਹੋ
    pipeline_display_name = get_pipeline_display_name()
    # ਡਿਸਪਲੇ ਨਾਮ ਪ੍ਰਿੰਟ ਕਰੋ
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### ਪਾਈਪਲਾਈਨ ਨੂੰ ਸੰਰਚਿਤ ਕਰਨਾ

ਇਹ Python ਸਕ੍ਰਿਪਟ Azure Machine Learning SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਪਾਈਪਲਾਈਨ ਪਰਿਭਾਸ਼ਿਤ ਅਤੇ ਸੰਰਚਿਤ ਕਰ ਰਿਹਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

1. ਇਹ Azure AI ML SDK ਵਿੱਚੋਂ ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ।

1. ਇਹ ਰਜਿਸਟਰੀ ਵਿੱਚੋਂ "chat_completion_pipeline" ਨਾਮਕ ਇੱਕ ਪਾਈਪਲਾਈਨ ਕੰਪੋਨੇਟ ਲੈਦਾ ਹੈ।

1. ਇਹ `@pipeline` ਡੈਕੋਰੇਟਰ ਅਤੇ `create_pipeline` ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਪਾਈਪਲਾਈਨ ਜਾਬ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ। ਪਾਈਪਲਾਈਨ ਦਾ ਨਾਮ `pipeline_display_name` ਹੁੰਦਾ ਹੈ।

1. `create_pipeline` ਫੰਕਸ਼ਨ ਦੇ ਅੰਦਰ, ਇਹ ਪ੍ਰਾਪਤ ਕੀਤਾ ਗਿਆ ਪਾਈਪਲਾਈਨ ਕੰਪੋਨੇਟ ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਮਾਡਲ ਦਾ ਰਸਤਾ, ਵੱਖ-ਵੱਖ ਸਟੇਜਾਂ ਲਈ ਕਮਪਿਊਟ ਕਲੱਸਟਰ, ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਟੈਸਟਿੰਗ ਲਈ ਡੇਟਾਸੈਟ ਸਪਲਿਟ, ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ GPU ਦੀ ਗਿਣਤੀ ਅਤੇ ਹੋਰ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪੈਰਾਮੀਟਰ।

1. ਇਹ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਜਾਬ ਦੇ ਆਉਟਪੁੱਟ ਨੂੰ ਪਾਈਪਲਾਈਨ ਜਾਬ ਦੇ ਆਊਟਪੁੱਟ ਨਾਲ ਜੋੜਦਾ ਹੈ ਤਾਂ ਜੋ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਆਸਾਨੀ ਨਾਲ ਰਜਿਸਟਰ ਕੀਤਾ ਜਾ ਸਕੇ, ਜੋ ਕਿ ਮਾਡਲ ਨੂੰ ਅਨਲਾਈਨ ਜਾਂ ਬੈਚ ਏਂਡਪੋਇੰਟ ਤੇ ਡਿਪਲੌਇ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਹੈ।

1. ਇਹ `create_pipeline` ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਕੇ ਪਾਈਪਲਾਈਨ ਦੀ ਇੱਕ ਨਕਲ ਬਣਾਉਂਦਾ ਹੈ।

1. ਇਹ ਪਾਈਪਲਾਈਨ ਦੀ `force_rerun` ਸੈਟਿੰਗ `True` ਕਰਦਾ ਹੈ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਪਹਿਲਾਂ ਦੇ ਜਾਬਾਂ ਤੋਂ ਕੈਸ਼ ਕੀਤੇ ਨਤੀਜੇ ਵਰਤੇ ਨਹੀਂ ਜਾਣਗੇ।

1. ਇਹ ਪਾਈਪਲਾਈਨ ਦੀ `continue_on_step_failure` ਸੈਟਿੰਗ `False` ਕਰਦਾ ਹੈ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਜੇ ਕਿਸੇ ਵੀ ਕਦਮ ਵਿੱਚ ਅਸਫਲਤਾ ਆਈ ਤਾਂ ਪਾਈਪਲਾਈਨ ਰੁਕ ਜਾਵੇਗੀ।

1. ਸੰਖੇਪ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ Azure Machine Learning SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਚੈਟ ਕੰਪਲੀਸ਼ਨ ਟਾਸਕ ਲਈ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਪਾਈਪਲਾਈਨ ਪਰਿਭਾਸ਼ਿਤ ਅਤੇ ਸੰਰਚਿਤ ਕਰ ਰਿਹਾ ਹੈ।

    ```python
    # Azure AI ML SDK ਤੋਂ ਜਰੂਰੀ ਮੋਡੀਊਲਾਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # ਰਜਿਸਟਰੀ ਤੋਂ "chat_completion_pipeline" ਨਾਮਕ ਪਾਈਪਲਾਈਨ ਕੰਪੋਨੈਂਟ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰੋ
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline ਡੈਕੋਰੇਟਰ ਅਤੇ create_pipeline ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪਾਈਪਲਾਈਨ ਜੌਬ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
    # ਪਾਈਪਲਾਈਨ ਦਾ ਨਾਮ pipeline_display_name 'ਤੇ ਸੈਟ ਕੀਤਾ ਗਿਆ ਹੈ
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # ਭਿੰਨ-ਭਿੰਨ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਪ੍ਰਾਪਤ ਕੀਤਾ ਗਿਆ ਪਾਈਪਲਾਈਨ ਕੰਪੋਨੈਂਟ ਇਨਿਸ਼ੀਅਲਾਈਜ਼ ਕਰੋ
        # ਇਹ ਵਿੱਚ ਮਾਡਲ ਪਾਥ, ਵੱਖ-ਵੱਖ ਸਟੇਜਾਂ ਲਈ ਕਮਪਿਊਟ ਕਲੱਸਟਰ, ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਟੈਸਟਿੰਗ ਲਈ ਡੇਟਾ ਸੈੱਟ ਵਿਭਾਜਨ, ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਜੀਪਯੂ ਦੀ ਸੰਖਿਆ ਅਤੇ ਹੋਰ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪੈਰਾਮੀਟਰ ਸ਼ਾਮਲ ਹਨ
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # ਡੇਟਾ ਸੈੱਟ ਦੇ ਵਿਭਾਜਨ ਨੂੰ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਜੋੜੋ
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # ਟ੍ਰੇਨਿੰਗ ਸੰਸਥਾਪਨ
            number_of_gpu_to_use_finetuning=gpus_per_node,  # ਕਮਪਿਊਟ ਵਿੱਚ ਉਪਲਬਧ ਜੀਪਯੂ ਦੀ ਸੰਖਿਆ 'ਤੇ ਸੈਟ ਕਰੋ
            **finetune_parameters
        )
        return {
            # ਫਾਈਨ ਟਿਊਨਿੰਗ ਜੌਬ ਦੇ ਨਤੀਜੇ ਨੂੰ ਪਾਈਪਲਾਈਨ ਜੌਬ ਦੇ ਨਤੀਜੇ ਨਾਲ ਨਕਸ਼ਾ ਕਰੋ
            # ਇਹ ਇਸ ਲਈ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਤਾਂ ਜੋ ਅਸੀਂ ਸੁਗਮ ਤਰੀਕੇ ਨਾਲ ਫਾਈਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਰਜਿਸਟਰ ਕਰ ਸਕੀਏ
            # ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ ਤਾਂ ਜੋ ਮਾਡਲ ਨੂੰ ਆਨਲਾਈਨ ਜਾਂ ਬੈਚ ਐਂਡਪੋਇੰਟ 'ਤੇ ਡਿਪਲੋਇ ਕੀਤਾ ਜਾ ਸਕੇ
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਕੇ ਪਾਈਪਲਾਈਨ ਦੀ ਇਕ ਇੰਸਟੈਂਸ ਬਣਾਓ
    pipeline_object = create_pipeline()
    
    # ਪਿਛਲੇ ਜੌਬ ਤੋਂ ਕੈਸ਼ ਕੀਤੇ ਨਤੀਜਿਆਂ ਦੀ ਵਰਤੋਂ ਨਾ ਕਰੋ
    pipeline_object.settings.force_rerun = True
    
    # ਕਦਮ ਦੀ ਅਸਫਲਤਾ 'ਤੇ ਜਾਰੀ ਰੱਖਣ ਦੀ ਸੈਟਿੰਗ False ਕਰੋ
    # ਇਸਦਾ ਅਰਥ ਹੈ ਕਿ ਜੇ ਕਿਸੇ ਵੀ ਕਦਮ ਵਿੱਚ ਅਸਫਲਤਾ ਹੁੰਦੀ ਹੈ ਤਾਂ ਪਾਈਪਲਾਈਨ ਰੁਕ ਜਾਵੇਗੀ
    pipeline_object.settings.continue_on_step_failure = False
    ```

### ਜਾਬ ਸਬਮਿਟ ਕਰੋ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਪਾਈਪਲਾਈਨ ਜਾਬ ਨੂੰ Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ ਸਬਮਿਟ ਕਰਦਾ ਹੈ ਅਤੇ ਫਿਰ ਜਾਬ ਦੇ ਮੁਕੰਮਲ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰਦਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

    - ਇਹ workspace_ml_client ਵਿੱਚ jobs ਆਬਜੈਕਟ ਦੇ create_or_update ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਪਾਈਪਲਾਈਨ ਜਾਬ ਸਬਮਿਟ ਹੋ ਜਾਵੇ। ਚਲਾਈ ਜਾਣ ਵਾਲੀ ਪਾਈਪਲਾਈਨ pipeline_object ਨਾਲ ਦਿੱਤੀ ਗਈ ਹੈ, ਅਤੇ ਜਿੱਥੇ ਜਾਬ ਚਲਾਇਆ ਜਾ ਰਿਹਾ ਹੈ ਉਹ experiment_name ਹੈ।

    - ਫਿਰ ਇਹ workspace_ml_client ਵਿੱਚ jobs ਆਬਜੈਕਟ ਦੇ stream ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਪਾਈਪਲਾਈਨ ਜਾਬ ਦੇ ਮੁਕੰਮਲ ਹੋਣ ਦੀ ਉਡੀਕ ਕੀਤੀ ਜਾ ਸਕੇ। ਉਡੀਕ ਕਰਨ ਵਾਲਾ ਜਾਬ pipeline_job ਆਬਜੈਕਟ ਦੇ name এটਰੀਬਿਊਟ ਨਾਲ ਨਿਰਧਾਰਿਤ ਹੁੰਦਾ ਹੈ।

    - ਸੰਖੇਪ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਪਾਈਪਲਾਈਨ ਜਾਬ ਨੂੰ Azure Machine Learning ਵਰਕਸਪੇਸ ਵਿੱਚ ਸਬਮਿਟ ਕਰਦਾ ਹੈ ਅਤੇ ਫਿਰ ਜਾਬ ਦੇ ਮੁਕੰਮਲ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰਦਾ ਹੈ।

    ```python
    # ਐਜ਼ਯੂਰ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਵਰਕਸਪੇਸ ਨੂੰ ਪਾਈਪਲਾਈਨ ਜ਼ਾਬ ਸਬਮਿਟ ਕਰੋ
    # ਚਲਾਈ ਜਾਣ ਵਾਲੀ ਪਾਈਪਲਾਈਨ pipeline_object ਨਾਲ ਨਿਰਧਾਰਿਤ ਕੀਤੀ ਗਈ ਹੈ
    # ਜਿਸ ਪ੍ਰਯੋਗ ਹੇਠਾਂ ਜ਼ਾਬ ਚਲਾਈ ਜਾ ਰਹੀ ਹੈ ਉਹ experiment_name ਨਾਲ ਨਿਰਧਾਰਿਤ ਹੈ
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # ਪਾਈਪਲਾਈਨ ਜ਼ਾਬ ਦੇ ਪੂਰਾ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰੋ
    # ਉਡੀਕ ਕਰਨ ਲਈ ਜ਼ਾਬ pipeline_job ਵਸਤੂ ਦੇ ਨਾਮ ਵਿਸ਼ੇਸ਼ਤਾ ਨਾਲ ਨਿਰਧਾਰਿਤ ਹੈ
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. ਫਾਈਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਵਰਕਸਪੇਸ ਨਾਲ ਰਜਿਸਟਰ ਕਰੋ

ਅਸੀਂ ਫਾਈਨ ਟਿਊਨਿੰਗ ਜਾਬ ਦੇ ਆਉਟਪੁੱਟ ਤੋਂ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਾਂਗੇ। ਇਹ ਫਾਈਨ ਟਿਊਨਿੰਗ ਜਾਬ ਅਤੇ ਫਾਈਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਵਿਚਕਾਰ ਲਾਈਨੇਜ ਦਾ ਟ੍ਰੈਕ ਰੱਖੇਗਾ। ਫਾਈਨ ਟਿਊਨਿੰਗ ਜਾਬ ਸਥਾਪਨਾ ਮਾਡਲ, ਡੇਟਾ ਅਤੇ ਟ੍ਰੇਨਿੰਗ ਕੋਡ ਨਾਲ ਲਾਈਨੇਜ ਵੀ ਟ੍ਰੈਕ ਕਰਦਾ ਹੈ।

### ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਰਜਿਸਟ੍ਰੇਸ਼ਨ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰ ਰਿਹਾ ਹੈ ਜੋ Azure Machine Learning ਪਾਈਪਲਾਈਨ ਵਿੱਚ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਸੀ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

    - ਇਹ Azure AI ML SDK ਵਿੱਚੋਂ ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ।

    - ਇਹ ਚੈੱਕ ਕਰਦਾ ਹੈ ਕਿ trained_model ਆਉਟਪੁੱਟ ਪਾਈਪਲਾਈਨ ਜਾਬ ਤੋਂ ਉਪਲਬਧ ਹੈ ਕਿ ਨਹੀਂ, workspace_ml_client ਵਿੱਚ jobs ਆਬਜੈਕਟ ਦੇ get ਮੈਥਡ ਨਾਲ ਅਤੇ ਇਸਦੇ outputs ਐਟਰੀਬਿਊਟ ਨੂੰ ਐਕਸੈਸ ਕਰਕੇ।

    - ਇਹ ਪਾਈਪਲਾਈਨ ਜਾਬ ਦੇ ਨਾਮ ਅਤੇ ਆਉਟਪੁੱਟ ("trained_model") ਦੇ ਨਾਮ ਨਾਲ ਇੱਕ ਮਾਡਲ ਲਈ ਪਾਥ ਬਣਾਉਂਦਾ ਹੈ।

    - ਇਹ ਇੱਕ ਨਾਮ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਮੂਲ ਮਾਡਲ ਨਾਮ ਵਿੱਚ "-ultrachat-200k" ਜੁੜਦਾ ਹੈ ਅਤੇ ਸਾਰੇ ਸਲੇਸ਼ਾਂ ਨੂੰ ਹਾਇਫਨ ਨਾਲ ਬਦਲਦਾ ਹੈ।

    - ਇਹ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨ ਲਈ Model ਆਬਜੈਕਟ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦਾ ਰਸਤਾ, ਮਾਡਲ ਦੀ ਕਿਸਮ (MLflow ਮਾਡਲ), ਮਾਡਲ ਦਾ ਨਾਮ ਅਤੇ ਵਰਜ਼ਨ ਅਤੇ ਮਾਡਲ ਦਾ ਵੇਰਵਾ ਸ਼ਾਮਿਲ ਹਨ।

    - ਇਹ workspace_ml_client ਵਿੱਚ models ਆਬਜੈਕਟ ਦੇ create_or_update ਮੈਥਡ ਨੂੰ Model ਆਬਜੈਕਟ ਦੇ ਨਾਲ ਕਾਲ ਕਰਕੇ ਮਾਡਲ ਰਜਿਸਟਰ ਕਰਦਾ ਹੈ।

    - ਇਹ ਰਜਿਸਟਰ ਕੀਤਾ ਮਾਡਲ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

1. ਸੰਖੇਪ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰ ਰਿਹਾ ਹੈ ਜੋ Azure Machine Learning ਪਾਈਪਲਾਈਨ ਵਿੱਚ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਸੀ।
    
    ```python
    # Azure AI ML SDK ਤੋਂ ਜ਼ਰੂਰੀ ਮੌਡਿਊਲ ਇੰਪੋਰਟ ਕਰੋ
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # ਚੈੱਕ ਕਰੋ ਕਿ ਪਾਈਪਲਾਈਨ ਜੌਬ ਤੋਂ `trained_model` ਆਉਟਪੁੱਟ ਉਪਲਬਧ ਹੈ ਕਿ ਨਹੀਂ
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # ਪਾਈਪਲਾਈਨ ਜੌਬ ਦੇ ਨਾਮ ਅਤੇ ਆਉਟਪੁੱਟ ("trained_model") ਦੇ ਨਾਮ ਨਾਲ ਸਤਰ ਨੂੰ ਫਾਰਮੈਟ ਕਰ ਕੇ ਟ੍ਰੇਨ ਕੀਤਾ ਮਾਡਲ ਦਾ ਪਾਥ ਬਣਾਓ
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # ਮੂਲ ਮਾਡਲ ਨਾਮ ਦੇ ਅੱਗੇ "-ultrachat-200k" ਲਗਾ ਕੇ ਅਤੇ ਕਿਸੇ ਵੀ ਸਲੈਸ਼ ਨੂੰ ਹਾਈਫਨ ਨਾਲ ਬਦਲ ਕੇ ਫਾਈਨ-ਟਿਊਨਡ ਮਾਡਲ ਦਾ ਨਾਮ ਪਰਿਭਾਸ਼ਤ ਕਰੋ
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਇਕ ਮਾਡਲ ਆਬਜੈਕਟ ਬਣਾਕੇ ਮਾਡਲ ਨੂੰ ਰਜਿਸਟਰ ਕਰਨ ਲਈ ਤਿਆਰ ਕਰੋ
    # ਇਨ੍ਹਾਂ ਵਿੱਚ ਮਾਡਲ ਦਾ ਪਾਥ, ਮਾਡਲ ਦੀ ਕਿਸਮ (MLflow ਮਾਡਲ), ਨਾਮ ਅਤੇ ਵਰਜਨ, ਅਤੇ ਮਾਡਲ ਦਾ ਵੇਰਵਾ ਸ਼ਾਮਿਲ ਹਨ
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # ਵਰਜਨ ਸੰਘਰਸ਼ ਤੋਂ ਬਚਣ ਲਈ ਸਮਾਂਮੁਹੂ ਯੂਜ਼ ਕਰੋ
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # ਮਾਡਲ ਆਬਜੈਕਟ ਨੂੰ ਦਰਜ ਕਰ ਦੇਂਦੇ ਹੋਏ workspace_ml_client ਵਿੱਚ models ਆਬਜੈਕਟ ਦੀ create_or_update ਵਿਧੀ ਨੂੰ ਕਾਲ ਕਰੋ
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # ਰਜਿਸਟਰ ਕੀਤਾ ਮਾਡਲ ਪ੍ਰਿੰਟ ਕਰੋ
    print("registered model: \n", registered_model)
    ```

## 7. ਫਾਈਨ ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਅਨਲਾਈਨ ਏਂਡਪੋਇੰਟ ਤੇ ਡਿਪਲੌਇ ਕਰੋ

ਅਨਲਾਈਨ ਏਂਡਪੋਇੰਟ ਇੱਕ ਟਿਕਾਊ REST API ਦਿੰਦੇ ਹਨ ਜੋ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ ਇੰਟੀਗਰੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ ਜੋ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ।

### ਏਂਡਪੋਇੰਟ ਪ੍ਰਬੰਧਨ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਮੈਨੇਜਡ ਅਨਲਾਈਨ ਏਂਡਪੋਇੰਟ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

    - ਇਹ Azure AI ML SDK ਵਿੱਚੋਂ ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ।

    - ਇਹ ਅਨਲਾਈਨ ਏਂਡਪੋਇੰਟ ਲਈ ਇੱਕ ਵਿਲੱਖਣ ਨਾਮ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਸਤਰਿੰਗ "ultrachat-completion-" ਦੇ ਨਾਲ ਇੱਕ ਟਾਈਮਸਟੈਂਪ ਜੋੜ ਕੇ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ ManagedOnlineEndpoint ਆਬਜੈਕਟ ਬਣਾਉਣ ਲਈ ਤਿਆਰ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਏਂਡਪੋਇੰਟ ਦਾ ਨਾਮ, ਏਂਡਪੋਇੰਟ ਦਾ ਵੇਰਵਾ, ਅਤੇ 인증 ਮੋਡ ("key") ਸ਼ਾਮਿਲ ਹਨ।

    - ਇਹ workspace_ml_client ਵਿੱਚ begin_create_or_update ਮੈਥਡ ਨੂੰ ManagedOnlineEndpoint ਆਬਜੈਕਟ ਦੇ ਨਾਲ ਕਾਲ ਕਰਦਾ ਹੈ ਅਤੇ ਫਿਰ wait ਮੈਥਡ ਨਾਲ ਬਣਾਉਣ ਦੀ ਕਾਰਵਾਈ ਦੇ ਮੁਕੰਮਲ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰਦਾ ਹੈ।

1. ਸੰਖੇਪ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਮੈਨੇਜਡ ਅਨਲਾਈਨ ਏਂਡਪੋਇੰਟ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਇੱਕ ਰਜਿਸਟਰ ਕੀਤਾ ਮਾਡਲ ਲਈ ਹੈ।

    ```python
    # Azure AI ML SDK ਤੋਂ ਲੋੜੀਂਦੇ ਮੌਡੀਊਲਾਂ ਨੂੰ ਆਯਾਤ ਕਰੋ
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # "ultrachat-completion-" ਸਟਰਿੰਗ ਨਾਲ ਇੱਕ ਟਾਈਮਸਟੈਂਪ ਜੋੜ ਕੇ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਲਈ ਇੱਕ ਵਿਲੱਖਣ ਨਾਮ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਇੱਕ ManagedOnlineEndpoint ਓਬਜੈਕਟ ਬਣਾਕੇ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਬਣਾਉਣ ਲਈ ਤਿਆਰ ਹੋਵੋ
    # ਇਨ੍ਹਾਂ ਵਿੱਚ ਐਂਡਪੋਇੰਟ ਦਾ ਨਾਮ, ਐਂਡਪੋਇੰਟ ਦਾ ਵਰਣਨ, ਅਤੇ ਪ੍ਰਮਾਣਿਕਤਾ ਮੋਡ ("key") ਸ਼ਾਮਲ ਹਨ
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ManagedOnlineEndpoint ਓਬਜੈਕਟ ਨੂੰ ਆਰਗੁਮੈਂਟ ਵਜੋਂ ਦੇ ਕੇ workspace_ml_client ਦੀ begin_create_or_update ਵਿਧੀ ਨੂੰ ਕਾਲ ਕਰਕੇ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਬਣਾਓ
    # ਫਿਰ wait ਵਿਧੀ ਨੂੰ ਕਾਲ ਕਰਕੇ ਬਣਾਉਣ ਦੀ ਕਾਰਵਾਈ ਮੁਕੰਮਲ ਹੋਣ ਦਾ ਇੰਤਜ਼ਾਰ ਕਰੋ
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> ਤੁਹਾਡੇ ਲਈ ਇੱਥੇ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਸਪੋਰਟ ਕੀਤੇ SKU's ਦੀ ਸੂਚੀ ਹੈ - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਇੱਕ ਰਜਿਸਟਰ ਕੀਤਾ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਮੈਨੇਜਡ ਅਨਲਾਈਨ ਏਂਡਪੋਇੰਟ 'ਤੇ ਡਿਪਲੌਇ ਕਰ ਰਿਹਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

    - ਇਹ ast ਮੋਡੀਊਲ ਨੂੰ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ, ਜੋ Python ਅਬਸਟ੍ਰੈਕਟ ਸਿੰਟੈਕਸ ਗ੍ਰੈਮਰ ਦੇ ਖਜਾਨਚੇ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨ ਲਈ ਫੰਗਸ਼ਨਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

    - ਇਹ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਇੰਸਟੈਂਸ ਕਿਸਮ "Standard_NC6s_v3" ਸੈਟ ਕਰਦਾ ਹੈ।

    - ਇਹ ਚੈੱਕ ਕਰਦਾ ਹੈ ਕਿ ਖੁਲਾਸਾ ਮਾਡਲ ਵਿੱਚ inference_compute_allow_list ਟੈਗ ਮੌਜੂਦ ਹੈ ਕਿ ਨਹੀਂ। ਜੇ ਹੈ, ਤਾਂ ਇਸ ਟੈਗ ਦਾ ਮੁੱਲ ਸਟਰਿੰਗ ਤੋਂ Python ਨੂੰ ਲਿਸਟ ਵਿੱਚ ਬਦਲ ਦਿੰਦਾ ਹੈ ਅਤੇ ਉਸਨੂੰ inference_computes_allow_list ਵਿੱਚ ਸੌਂਪਦਾ ਹੈ, ਨਹੀਂ ਤਾਂ ਇਸ ਨੂੰ None ਸੈਟ ਕਰਦਾ ਹੈ।

    - ਇਹ ਜਾਂਚਦਾ ਹੈ ਕਿ ਨਿਰਧਾਰਿਤ ਇੰਸਟੈਂਸ ਕਿਸਮ ਅਨੁਮਤ ਸੂਚੀ ਵਿੱਚ ਹੈ ਕਿ ਨਹੀਂ। ਜੇ ਨਹੀਂ है, ਤਾਂ ਇਹ ਸਥਿਤੀ ਸਥੀਤੀ ਨੂੰ ਚੁੱਕਣ ਲਈ ਇੱਕ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

    - ਇਹ ManagedOnlineDeployment ਆਬਜੈਕਟ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਡਿਪਲੌਇਮੈਂਟ ਦਾ ਨਾਮ, ਏਂਡਪੋਇੰਟ ਦਾ ਨਾਮ, ਮਾਡਲ ਦਾ ID, ਇੰਸਟੈਂਸ ਕਿਸਮ ਅਤੇ ਗਿਣਤੀ, ਲਾਈਵਨੈਸ ਪ੍ਰੋਬ ਸੈਟਿੰਗਜ਼ ਅਤੇ ਬੇਨਤੀ ਸੈਟਿੰਗਜ਼ ਸ਼ਾਮਿਲ ਹਨ।

    - ਇਹ workspace_ml_client ਵਿੱਚ begin_create_or_update ਮੈਥਡ ਨੂੰ ਇਸ ਡਿਪਲੌਇਮੈਂਟ ਆਬਜੈਕਟ ਨਾਲ ਕਾਲ ਕਰਦਾ ਹੈ ਅਤੇ ਫਿਰ wait ਮੈਥਡ ਨਾਲ ਬਣਾਉਣ ਦੀ ਕਾਰਵਾਈ ਦੇ ਮੁਕੰਮਲ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰਦਾ ਹੈ।

    - ਇਹ ਐਂਡਪੋਇੰਟ ਦਾ ਟ੍ਰੈਫਿਕ "demo" ਡਿਪਲੌਇਮੈਂਟ ਵੱਲ 100% ਡਾਇਰੈਕਟ ਕਰਦਾ ਹੈ।

    - ਇਹ begin_create_or_update ਨਾਲ ਐਂਡਪੋਇੰਟ ਨੂੰ ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ ਅਤੇ result ਮੈਥਡ ਨਾਲ ਅੱਪਡੇਟ ਮੁਕੰਮਲ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰਦਾ ਹੈ।

1. ਸੰਖੇਪ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਰਜਿਸਟਰ ਕੀਤਾ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਨੂੰ ਇੱਕ ਮੈਨੇਜਡ ਅਨਲਾਈਨ ਏਂਡਪੋਇੰਟ ਵਿੱਚ ਡਿਪਲੌਇ ਕਰਦਾ ਹੈ ਜੋ Azure Machine Learning ਦਾ ਹਿੱਸਾ ਹੈ।

    ```python
    # ast ਮੋਡੀਊਲ ਨੂੰ ਆਯਾਤ ਕਰੋ, ਜੋ Python ਐਬਸਟ੍ਰੈਕਟ ਸਿੰਟੈਕਸ ਗ੍ਰੈਮਰ ਦੇ ਦਰੱਖਤਾਂ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
    import ast
    
    # ਡਿਪਲੋਇਮੈਂਟ ਲਈ ਇੰਸਟੈਂਸ ਟਾਈਪ ਸੈੱਟ ਕਰੋ
    instance_type = "Standard_NC6s_v3"
    
    # ਜਾਂਚ ਕਰੋ ਕਿ `inference_compute_allow_list` ਟੈਗ ਫਾਉਂਡੇਸ਼ਨ ਮਾਡਲ ਵਿੱਚ ਮੌਜੂਦ ਹੈ ਜਾਂ ਨਹੀਂ
    if "inference_compute_allow_list" in foundation_model.tags:
        # ਜੇ ਹੈ, ਤਾਂ ਟੈਗ ਦੀ ਵੈਲਯੂ ਨੂੰ ਸਤਰ ਤੋਂ Python ਸੂਚੀ ਵਿੱਚ ਤਬਦੀਲ ਕਰੋ ਅਤੇ `inference_computes_allow_list` ਨੂੰ ਸੌਂਪੋ
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # ਜੇ ਨਹੀਂ, ਤਾਂ `inference_computes_allow_list` ਨੂੰ `None` ਤੇ ਸੈੱਟ ਕਰੋ
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # ਜਾਂਚ ਕਰੋ ਕਿ ਦਿੱਤਾ ਗਿਆ ਇੰਸਟੈਂਸ ਟਾਈਪ ਅਲਾਵ ਲਿਸਟ ਵਿੱਚ ਹੈ ਜਾਂ ਨਹੀਂ
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ `ManagedOnlineDeployment` ਆਬਜੈਕਟ ਬਣਾਕੇ ਡਿਪਲੋਇਮੈਂਟ ਬਣਾਉਣ ਲਈ ਤਿਆਰ ਕਰੋ
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `ManagedOnlineDeployment` ਆਬਜੈਕਟ ਨੂੰ argument ਵਜੋਂ ਦੇ ਕੇ `workspace_ml_client` ਦੇ `begin_create_or_update` ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਕੇ ਡਿਪਲੋਇਮੈਂਟ ਬਣਾਓ
    # ਫਿਰ `wait` ਮੈਥਡ ਕਾਲ ਕਰਕੇ ਬਣਾਉਣ ਦੇ ਉਪਰੇਸ਼ਨ ਦੇ پورਾ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰੋ
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # ਐਂਡਪੋਇੰਟ ਦੇ ਟ੍ਰੈਫਿਕ ਨੂੰ ਐਸਾ ਸੈੱਟ ਕਰੋ ਕਿ 100% ਟ੍ਰੈਫਿਕ "ਡੈਮੋ" ਡਿਪਲੋਇਮੈਂਟ ਨੂੰ ਜਾਏ
    endpoint.traffic = {"demo": 100}
    
    # `endpoint` ਆਬਜੈਕਟ ਨੂੰ argument ਵਜੋਂ ਦੇ ਕੇ `workspace_ml_client` ਦੇ `begin_create_or_update` ਮੈਥਡ ਕਾਲ ਕਰਕੇ ਐਂਡਪੋਇੰਟ ਅਪਡੇਟ ਕਰੋ
    # ਫਿਰ `result` ਮੈਥਡ ਕਾਲ ਕਰਕੇ ਅਪਡੇਟ ਉਪਰੇਸ਼ਨ ਦੇ ਮੁਕੰਮਲ ਹੋਣ ਦੀ ਉਡੀਕ ਕਰੋ
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. ਸੈਂਪਲ ਡੇਟਾ ਨਾਲ ਏਂਡਪੋਇੰਟ ਦੀ ਪਰਖ

ਅਸੀਂ ਟੈਸਟ ਡੇਟਾਸੈਟ ਤੋਂ ਕੁਝ ਸੈਂਪਲ ਡੇਟਾ ਲੈ ਕੇ ਅਨਲਾਈਨ ਏਂਡਪੋਇੰਟ ਨੂੰ ਇੰਫਰੈਂਸ ਲਈ ਸਬਮਿਟ ਕਰਾਂਗੇ। ਫਿਰ ਅਸੀਂ ਸਕੋਰ ਕੀਤੇ ਲੇਬਲਾਂ ਨੂੰ ਗਰਾਊਂਡ ਟਰੂਥ ਲੇਬਲਾਂ ਦੇ ਨਾਲ ਦਰਸਾਵਾਂਗੇ।

### ਨਤੀਜੇ ਪੜ੍ਹਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ JSON Lines ਫਾਇਲ ਨੂੰ pandas DataFrame ਵਿੱਚ ਪੜ੍ਹਦਾ ਹੈ, ਇੱਕ ਰੈਂਡਮ ਸੈਂਪਲ ਲੈਂਦਾ ਹੈ, ਅਤੇ ਇੰਡੈਕਸ ਰੀਸੈਟ ਕਰਦਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

    - ਇਹ ਫਾਇਲ ./ultrachat_200k_dataset/test_gen.jsonl ਨੂੰ pandas DataFrame ਵਿੱਚ ਪੜ੍ਹਦਾ ਹੈ। read_json ਫੰਗਸ਼ਨ lines=True ਆਰਗਯੂਮੈਂਟ ਨਾਲ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ ਕਿਉਂਕਿ ਫਾਇਲ JSON Lines ਫਾਰਮੈਟ ਵਿੱਚ ਹੈ, ਜਿੱਥੇ ਹਰ ਲਾਈਨ ਇੱਕ ਵੱਖਰਾ JSON ਆਬਜੈਕਟ ਹੁੰਦੀ ਹੈ।

    - ਇਹ DataFrame ਵਿੱਚੋਂ 1 ਰਿਕਾਰਡ ਦਾ ਰੈਂਡਮ ਸੈਂਪਲ ਲੈਂਦਾ ਹੈ। sample ਫੰਗਸ਼ਨ n=1 ਆਰਗਯੂਮੈਂਟ ਨਾਲ ਵਰਤਿਆ ਗਿਆ ਹੈ।

    - ਇਹ DataFrame ਦਾ ਇੰਡੈਕਸ ਰੀਸੈਟ ਕਰਦਾ ਹੈ। reset_index ਫੰਗਸ਼ਨ drop=True ਨਾਲ ਵਰਤਿਆ ਗਿਆ ਹੈ ਤਾਂ ਜੋ ਅਸਲ ਇੰਡੈਕਸ ਡ੍ਰਾਪ ਅਤੇ ਨਵੇਂ ਡਿਫਾਲਟ ਇੰਟੀਜਰ ਇੰਡੈਕਸ ਨਾਲ ਬਦਲਿਆ ਜਾ ਸਕੇ।

    - ਇਹ head ਫੰਗਸ਼ਨ ਨਾਲ DataFrame ਦੀਆਂ ਪਹਿਲੀਆਂ 2 ਲਾਈਨਾਂ ਦਿਖਾਉਂਦਾ ਹੈ, ਪਰ ਕਿਉਂਕਿ ਸੈਂਪਲਿੰਗ ਤੋਂ ਬਾਅਦ DataFrame ਵਿੱਚ ਸਿਰਫ ਇੱਕ ਲਾਈਨ ਹੈ, ਇਸ ਲਈ ਇਹ ਸਿਰਫ ਇੱਕ ਲਾਈਨ ਦਿਖਾਏਗਾ।

1. ਸੰਖੇਪ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ JSON Lines ਫਾਇਲ ਨੂੰ pandas DataFrame ਵਿੱਚ ਪੜ੍ਹਦਾ ਹੈ, ਇੱਕ ਰੈਂਡਮ ਸੈਂਪਲ ਲੈਂਦਾ ਹੈ, ਇੰਡੈਕਸ ਰੀਸੈਟ ਕਰਦਾ ਹੈ, ਅਤੇ ਪਹਿਲੀ ਲਾਈਨ ਦਿਖਾਉਂਦਾ ਹੈ।
    
    ```python
    # pandas ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਆਯਾਤ ਕਰੋ
    import pandas as pd
    
    # JSON Lines ਫਾਈਲ './ultrachat_200k_dataset/test_gen.jsonl' ਨੂੰ pandas DataFrame ਵਿੱਚ ਪੜ੍ਹੋ
    # 'lines=True' ਆਰਗੂਮੈਂਟ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਫਾਈਲ JSON Lines ਫਾਰਮੈਟ ਵਿੱਚ ਹੈ, ਜਿੱਥੇ ਹਰ ਲਾਈਨ ਇੱਕ ਵੱਖਰੀ JSON ਵਸਤੂ ਹੁੰਦੀ ਹੈ
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # DataFrame ਵਿੱਚੋਂ 1 ਕਤਾਰ ਦਾ ਯਾਦೃਚਿਕ ਨਮੂਨਾ ਲਵੋ
    # 'n=1' ਆਰਗੂਮੈਂਟ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਚੁਣੀਆਂ ਜਾਣ ਵਾਲੀਆਂ ਯਾਦ੍ਰਚਿਕ ਕਤਾਰਾਂ ਦੀ ਗਿਣਤੀ 1 ਹੈ
    test_df = test_df.sample(n=1)
    
    # DataFrame ਦਾ ਇੰਡੈਕਸ ਰੀਸੈੱਟ ਕਰੋ
    # 'drop=True' ਆਰਗੂਮੈਂਟ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ ਮੂਲ ਇੰਡੈਕਸ ਨੂੰ ਹਟਾ ਕੇ ਨਵੇਂ ਡਿਫਾਲਟ ਪੂਰੇ ਅੰਕਾਂ ਵਾਲੇ ਇੰਡੈਕਸ ਨਾਲ ਬਦਲ ਦਿੱਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ
    # 'inplace=True' ਆਰਗੂਮੈਂਟ ਦਰਸਾਉਂਦਾ ਹੈ ਕਿ DataFrame ਨੂੰ ਥੱਠੇ ਹੀ ਬਦਲਣਾ (ਨਵੀਂ ਵਸਤੂ ਬਣਾਏ ਬਿਨਾਂ) ਚਾਹੀਦਾ ਹੈ
    test_df.reset_index(drop=True, inplace=True)
    
    # DataFrame ਦੀਆਂ ਪਹਿਲੀਆਂ 2 ਕਤਾਰਾਂ ਦਿਖਾਓ
    # ਹਾਲਾਂਕਿ ਕਿਉਂਕਿ ਸਮਪਲਿੰਗ ਤੋਂ ਬਾਅਦ DataFrame ਵਿੱਚ ਸਿਰਫ ਇੱਕ ਕਤਾਰ ਹੀ ਹੈ, ਇਸ ਲਈ ਇਹ ਸਿਰਫ ਉਹੀ ਇੱਕ ਕਤਾਰ ਦਿਖਾਏਗਾ
    test_df.head(2)
    ```

### JSON ਆਬਜੈਕਟ ਬਣਾਉਣਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ ਖਾਸ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਇੱਕ JSON ਆਬਜੈਕਟ ਬਣਾਊਂਦਾ ਹੈ ਅਤੇ ਇਸਨੂੰ ਫਾਇਲ ਵਿੱਚ ਸੇਵ ਕਰਦਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕਰਦਾ ਹੈ:

    - ਇਹ json ਮੋਡੀਊਲ ਨੂੰ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ, ਜੋ JSON ਡੇਟਾ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਫੰਗਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
    - ਇਹ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਲਈ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਕੁੰਜੀਆਂ ਅਤੇ ਮੁੱਲਾਂ ਨਾਲ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਪੈਰਾਮੀਟਰ ਬਣਾਉਂਦਾ ਹੈ। ਕੁੰਜੀਆਂ ਹਨ "temperature", "top_p", "do_sample", ਅਤੇ "max_new_tokens", ਅਤੇ ਸੰਬੰਧਤ ਮੁੱਲ 0.6, 0.9, True, ਅਤੇ 200 ਹਨ।

    - ਇਹ ਇੱਕ ਹੋਰ ਡਿਕਸ਼ਨਰੀ test_json ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਦੋ ਕੁੰਜੀਆਂ ਹਨ: "input_data" ਅਤੇ "params"। "input_data" ਦਾ ਮੁੱਲ ਇੱਕ ਹੋਰ ਡਿਕਸ਼ਨਰੀ ਹੈ ਜਿਸ ਵਿੱਚ "input_string" ਅਤੇ "parameters" ਕੁੰਜੀਆਂ ਹਨ। "input_string" ਦਾ ਮੁੱਲ ਇੱਕ ਸੂਚੀ ਹੈ ਜਿਸ ਵਿੱਚ test_df DataFrame ਦਾ ਪਹਿਲਾ ਮੈਸਜ ਹੈ। "parameters" ਦਾ ਮੁੱਲ ਪਹਿਲਾਂ ਬਣਾਈ ਗਈ ਪੈਰਾਮੀਟਰ ਡਿਕਸ਼ਨਰੀ ਹੈ। "params" ਦਾ ਮੁੱਲ ਇੱਕ ਖਾਲੀ ਡਿਕਸ਼ਨਰੀ ਹੈ।

    - ਇਹ sample_score.json ਨਾਮਕ ਫਾਈਲ ਖੋਲ੍ਹਦਾ ਹੈ
    
    ```python
    # json ਮਾਡਿਊਲ ਇمپੋਰਟ ਕਰੋ, ਜੋ JSON ਡੇਟਾ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨ ਦਿੰਦਾ ਹੈ
    import json
    
    # ਇੱਕ ਡਿਕਸ਼ਨਰੀ `parameters` ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਕੀ ਅਤੇ ਮੁੱਲ ਹਨ ਜੋ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਲਈ ਪੈਰਾਮੀਟਰ ਦਰਸਾਉਂਦੇ ਹਨ
    # ਕੁੰਜੀਆਂ "temperature", "top_p", "do_sample", ਅਤੇ "max_new_tokens" ਹਨ, ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਸਮਕਾਲੀ ਮੁੱਲ 0.6, 0.9, True, ਅਤੇ 200 ਹਨ
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # ਇੱਕ ਹੋਰ ਡਿਕਸ਼ਨਰੀ `test_json` ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਦੋ ਕੁੰਜੀਆਂ ਹਨ: "input_data" ਅਤੇ "params"
    # "input_data" ਦਾ ਮੁੱਲ ਇੱਕ ਹੋਰ ਡਿਕਸ਼ਨਰੀ ਹੈ ਜਿਸ ਵਿੱਚ ਕੁੰਜੀਆਂ "input_string" ਅਤੇ "parameters" ਹਨ
    # "input_string" ਦਾ ਮੁੱਲ ਇੱਕ ਲਿਸਟ ਹੈ ਜਿਸ ਵਿੱਚ `test_df` DataFrame ਤੋਂ ਪਹਿਲਾ ਸੁਨੇਹਾ ਸ਼ਾਮਲ ਹੈ
    # "parameters" ਦਾ ਮੁੱਲ ਪਹਿਲਾਂ ਬਣਾਈ ਗਈ `parameters` ਡਿਕਸ਼ਨਰੀ ਹੈ
    # "params" ਦਾ ਮੁੱਲ ਇੱਕ ਖਾਲੀ ਡਿਕਸ਼ਨਰੀ ਹੈ
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ `sample_score.json` ਨਾਮਕ ਫਾਇਲ ਨੂੰ ਲਿਖਣ ਮੋਡ ਵਿੱਚ ਖੋਲ੍ਹੋ
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `json.dump` ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ `test_json` ਡਿਕਸ਼ਨਰੀ ਨੂੰ JSON ਫਾਰਮੈਟ ਵਿੱਚ ਫਾਈਲ ਵਿੱਚ ਲਿਖੋ
        json.dump(test_json, f)
    ```

### ਐਂਡਪੋਇੰਟ ਨੂੰ ਕਾਲ ਕਰਨਾ

1. ਇਹ Python ਸਕ੍ਰਿਪਟ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਨੂੰ ਇੱਕ JSON ਫਾਈਲ ਸਕੋਰ ਕਰਨ ਲਈ ਕਾਲ ਕਰ ਰਿਹਾ ਹੈ। ਇਹ ਰਾਹੀਂ ਕੀ ਕੀ ਹੁੰਦਾ ਹੈ ਉਸ ਦਾ ਵਿਸਥਾਰ ਇੱਥੇ ਹੈ:

    - ਇਹ workspace_ml_client ਆਬਜੈਕਟ ਦੀ online_endpoints ਪ੍ਰਾਪਰਟੀ ਦੇ invoke ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ। ਇਹ ਮੈਥਡ ਇਕ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਨੂੰ ਬੇਨਤੀ ਭੇਜਣ ਅਤੇ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ endpoint_name ਅਤੇ deployment_name ਆਰਗੁਮੈਂਟਸ ਨਾਲ ਐਂਡਪੋਇੰਟ ਅਤੇ ਡਿਪਲੋਇਮੈਂਟ ਦੇ ਨਾਮ ਦੱਸਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਐਂਡਪੋਇੰਟ ਦਾ ਨਾਮ online_endpoint_name ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਹੈ ਅਤੇ ਡਿਪਲੋਇਮੈਂਟ ਦਾ ਨਾਮ "demo" ਹੈ।

    - ਇਹ request_file ਆਰਗੁਮੈਂਟ ਨਾਲ ਸਕੋਰ ਕੀਤੀ ਜਾਣ ਵਾਲੀ JSON ਫਾਈਲ ਦਾ ਪਾਥ ਦੱਸਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ ਫਾਈਲ ./ultrachat_200k_dataset/sample_score.json ਹੈ।

    - ਇਹ ਐਂਡਪੋਇੰਟ ਤੋਂ ਮਿਲੇ ਜਵਾਬ ਨੂੰ response ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਕਰਦਾ ਹੈ।

    - ਇਹ ਕੱਚਾ ਜਵਾਬ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

1. ਸਾਰ ਵਿੱਚ, ਇਹ ਸਕ੍ਰਿਪਟ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਨੂੰ ਇਕ JSON ਫਾਈਲ ਸਕੋਰ ਕਰਨ ਲਈ ਕਾਲ ਕਰ ਰਿਹਾ ਹੈ ਅਤੇ ਜਵਾਬ ਪ੍ਰਿੰਟ ਕਰ ਰਿਹਾ ਹੈ।

    ```python
    # Azure ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਵਿੱਚ ਆਨਲਾਈਨ ਐਂਡਪੁਆਇੰਟ ਨੂੰ ਕਾਲ ਕਰਕੇ `sample_score.json` ਫਾਇਲ ਦਾ ਸਕੋਰ ਕਰੋ
    # `workspace_ml_client` ਆਬਜੈਕਟ ਦੀ `online_endpoints` ਪ੍ਰਾਪਰਟੀ ਦੀ `invoke` ਮੇਥਡ ਨੂੰ ਆਨਲਾਈਨ ਐਂਡਪੁਆਇੰਟ ਨੂੰ ਰਿਕਵੈਸਟ ਭੇਜਣ ਅਤੇ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ
    # `endpoint_name` ਆਰਗੁਮੈਂਟ ਐਂਡਪੁਆਇੰਟ ਦਾ ਨਾਮ ਦੱਸਦਾ ਹੈ, ਜੋ ਕਿ `online_endpoint_name` ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਹੈ
    # `deployment_name` ਆਰਗੁਮੈਂਟ ਡਿਪਲੋਇਮੈਂਟ ਦਾ ਨਾਮ ਦੱਸਦਾ ਹੈ, ਜੋ "demo" ਹੈ
    # `request_file` ਆਰਗੁਮੈਂਟ JSON ਫਾਇਲ ਦਾ ਰਾਹ ਦਰਸਾਉਂਦਾ ਹੈ ਜਿਸਦਾ ਸਕੋਰ ਲੈਣਾ ਹੈ, ਜੋ ਕਿ `./ultrachat_200k_dataset/sample_score.json` ਹੈ
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # ਐਂਡਪੁਆਇੰਟ ਤੋਂ ਕੱਚਾ ਜਵਾਬ ਪ੍ਰਿੰਟ ਕਰੋ
    print("raw response: \n", response, "\n")
    ```

## 9. ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਮਿਟਾਓ

1. ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਨੂੰ ਮਿਟਾਉਣਾ ਨਾ ਭੁੱਲੋ, ਨਹੀਂ ਤਾਂ ਤੁਸੀਂ ਐਂਡਪੋਇੰਟ ਦੁਆਰਾ ਵਰਤੇ ਗਏ ਕੰਪਿਊਟ ਲਈ ਬਿੱਲਿੰਗ ਮੀਟਰ ਚਾਲੂ ਰਹਿਣ ਦਿਓਗੇ। ਇਹ Python ਕੋਡ ਲਾਈਨ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਨੂੰ ਮਿਟਾ ਰਹੀ ਹੈ। ਇਹ ਰਾਹੀਂ ਕੀ ਕੀ ਹੁੰਦਾ ਹੈ ਉਸ ਦੀ ਵਿਆਖਿਆ ਇੱਥੇ ਹੈ:

    - ਇਹ workspace_ml_client ਆਬਜੈਕਟ ਦੀ online_endpoints ਪ੍ਰਾਪਰਟੀ ਦੇ begin_delete ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ। ਇਹ ਮੈਥਡ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਦੇ ਮਿਟਾਉਣ ਦੀ ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।

    - ਇਹ name ਆਰਗੁਮੈਂਟ ਨਾਲ ਮਿਟਾਉਣ ਲਈ ਐਂਡਪੋਇੰਟ ਦਾ ਨਾਮ ਦੱਸਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਐਂਡਪੋਇੰਟ ਦਾ ਨਾਮ online_endpoint_name ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਹੈ।

    - ਇਹ wait ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਮਿਟਾਉਣ ਵਾਲਾ ਪ੍ਰਕਿਰਿਆ ਸਮਾਪਤ ਹੋਣ ਤੱਕ ਇੰਤਜ਼ਾਰ ਕੀਤਾ ਜਾ ਸਕੇ। ਇਹ ਇੱਕ ਬਲਾਕਿੰਗ ਆਪਰੇਸ਼ਨ ਹੈ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਇਹ ਸਕ੍ਰਿਪਟ ਨੂੰ ਅੱਗੇ ਵਧਣ ਤੋਂ ਰੋਕਦਾ ਹੈ ਜਦ ਤੱਕ ਮਿਟਾਉਣ ਦਾ ਕੰਮ ਖਤਮ ਨਹੀਂ ਹੁੰਦਾ।

    - ਸਾਰ ਵਿੱਚ, ਇਹ ਕੋਡ ਲਾਈਨ Azure Machine Learning ਵਿੱਚ ਇੱਕ ਆਨਲਾਈਨ ਐਂਡਪੋਇੰਟ ਦੇ ਮਿਟਾਉਣ ਦੀ ਸ਼ੁਰੂਆਤ ਕਰ ਰਹੀ ਹੈ ਅਤੇ ਕੰਮ ਖਤਮ ਹੋਣ ਤੱਕ ਇੰਤਜ਼ਾਰ ਕਰ ਰਹੀ ਹੈ।

    ```python
    # Azure Machine Learning ਵਿੱਚ ਑ਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਨੂੰ ਮਿਟਾਓ
    # `workspace_ml_client` ਔਬਜੈਕਟ ਦੀ `online_endpoints` ਪ੍ਰੋਪਰਟੀ ਦਾ `begin_delete` ਮੈਥਡ ਑ਨਲਾਈਨ ਐਂਡਪੌਇੰਟ ਦੀ ਮਿਟਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ
    # `name` ਆਰਗੂਮੈਂਟ ਉਸ ਐਂਡਪੌਇੰਟ ਦਾ ਨਾਮ ਦੱਸਦਾ ਹੈ ਜੋ ਮਿਟਾਇਆ ਜਾਣਾ ਹੈ, ਜੋ ਕਿ `online_endpoint_name` ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਗਿਆ ਹੈ
    # ਮਿਟਾਉਣ ਦੀ ਕਾਰਵਾਈ ਖਤਮ ਹੋਣ ਦਾ ਇੰਤਜ਼ਾਰ ਕਰਨ ਲਈ `wait` ਮੈਥਡ ਨੂੰ ਕੌਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਇਹ ਇਕ ਬਲਾਕਿੰਗ ਓਪਰੇਸ਼ਨ ਹੈ, ਜਿਸਦਾ ਅਰਥ ਹੈ ਕਿ ਇਹ ਸਕ੍ਰਿਪਟ ਨੂੰ ਅੱਗੇ ਵਧਣ ਤੋਂ ਰੋਕੇਗਾ ਜਦ ਤੱਕ ਮਿਟਾਉਣ ਮੁਕੰਮਲ ਨਾ ਹੋ ਜਾਵੇ
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਤੀਫਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੋ ਕਿ ਆਟੋਮੈਟਡ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਤੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਜਿਸ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਉਸਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਾਨਵ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਅਸਮਝਦਾਰੀਆਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹੋਵਾਂਗੇ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->