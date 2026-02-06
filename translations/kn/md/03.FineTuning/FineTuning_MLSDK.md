## Azure ML ಸಿಸ್ಟಂ ರಜಿಸ್ಟ್ರಿಯಿಂದ ಚಾಟ್-ಪೂರ್ಣತೆ ಘಟಕಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಮಾದರಿಯನ್ನು ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆ ಮಾಡಲು ಹೇಗೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ನಾವು Phi-3-mini-4k-instruct ಮಾದರಿಯನ್ನು ultrachat_200k ಡೇಟಾಸೆಟ್ ಬಳಸಿ 2 ಜನರ ನಡುವೆ ಸಂವಾದವನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆ ಮಾಡುತ್ತೇವೆ.

![MLFineTune](../../../../translated_images/kn/MLFineTune.928d4c6b3767dd35.webp)

ಈ ಉದಾಹರಣೆ ನಿಮಗೆ ಹೇಗೆ Azure ML SDK ಮತ್ತು Python ಬಳಸಿ ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆಯನ್ನು ನಡೆಸುವುದು ಮತ್ತು ನಂತರ ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸಿದ ಮಾದರಿಯನ್ನು ಆನ್‌ಲೈನ್ ಎಂಡಿಪಾಯಿಂಟ್‌ಗೆ ರಿಯಲ್ ಟೈಂ ನಿರೂಪಣೆಗೆ ನಿಯೋಜಿಸುವುದು ತೋರಿಸುತ್ತದೆ.

### ತರಬೇತಿ ಡೇಟಾ

ನಾವು ultrachat_200k ಡೇಟಾಸೆಟ್ ಅನ್ನು ಬಳಸುವುದು. ಇದು UltraChat ಡೇಟಾಸೆಟ್‌ನ ಬಹಳ ಫಿಲ್ಟರ್ ಮಾಡಲಾದ ಆವೃತ್ತಿ ಮತ್ತು Zephyr-7B-β ಗೆ ತರಬೇತಿಗೊಳಿಸಲು ಬಳಸಲ್ಪಟ್ಟ ಒಂದು ಅತ್ಯಾಧುನಿಕ 7b ಚಾಟ್ ಮಾದರಿ.

### ಮಾದರಿ

ನಾವು Phi-3-mini-4k-instruct ಮಾದರಿಯನ್ನು ಬಳಸಿ ಬಳಕೆದಾರನು ಚಾಟ್-ಪೂರ್ಣತೆ ಕೆಲಸಕ್ಕೆ ಮಾದರಿಯನ್ನು ಹೇಗೆ ಸೂಕ್ಷ್ಮವಾಗಿ ಮರುಚಲಿಸುವುದನ್ನು ತೋರಿಸುತ್ತೇವೆ. ನೀವು ಈ ನೋಟ್‌ಬುಕ್ ಅನ್ನು ನಿರ್ದಿಷ್ಟ ಮಾದರಿ ಕಾರ್ಡಿನಿಂದ ತೆರೆಯಿದರೆ, ನಿಮ್ಮ ಮಾದರಿ ಹೆಸರನ್ನು ಬದಲಿಸಿ.

### ಕಾರ್ಯಗಳು

- ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸಲು ಮಾದರಿಯನ್ನು ಆರಿಸಿ.
- ತರಬೇತಿ ಡೇಟಾವನ್ನು ಆರಿಸಿ ಮತ್ತು ಪರಿಶೀಲಿಸಿ.
- ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆ ಕೆಲಸವನ್ನು ಸಂರಚಿಸಿ.
- ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆ ಕೆಲಸವನ್ನು ಚಾಲನೆಯಲ್ಲಿಡಿ.
- ತರಬೇತಿ ಮತ್ತು ಮೌಲ್ಯಮಾಪನ ಮಿತಿಗಳನ್ನು ವಿಮರ್ಶಿಸಿ.
- ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸಿದ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸಿ.
- ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸಿದ ಮಾದರಿಯನ್ನು ರಿಯಲ್ ಟೈಂ ನಿರೂಪಣೆಗೆ ನಿಯೋಜಿಸಿ.
- ಸಂಪನ್ಮೂಲಗಳನ್ನು ಶುದ್ಧಗೊಳಿಸಿ.

## 1. ಅಗತ್ಯಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿ

- ಅವಶ್ಯಕತೆಯನ್ನು ಸ್ಥಾಪಿಸಿ
- AzureML ವರ್ಕ್‌ಸ್ಪೇಸ್‌ಗೆ ಸಂಪರ್ಕಿಸಿ. SDK ದೃಢೀಕರಣವನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಲು ಇನ್ನಷ್ಟು ತಿಳಿದುಕೊಳ್ಳಿ. ಕೆಳಗಿನ <WORKSPACE_NAME>, <RESOURCE_GROUP>, ಮತ್ತು <SUBSCRIPTION_ID> ನ್ನು ಬದಲಿಸಿ.
- azureml ಸಿಸ್ಟಂ ರಜಿಸ್ಟ್ರಿಗೆ ಸಂಪರ್ಕಿಸಿ
- ಐಚ್ಛಿಕ ಪ್ರಯೋಗದ ಹೆಸರನ್ನು ನಿಗದಿಪಡಿ
- ಕಂಪ್ಯೂಟನ್ನು ಪರಿಶೀಲಿಸಿ ಅಥವಾ ರಚಿಸಿ.

> [!NOTE]
> ಅಗತ್ಯವಿದ್ದರೆ ಒಂದು GPU ನೋಡ್‌ನಲ್ಲಿ ಹಲವಾರು GPU ಕಾರ್ಡುಗಳು ಇರಬಹುದು. ಉದಾಹರಣೆಗೆ, Standard_NC24rs_v3 ಒಂದು ನೋಡ್‌ನಲ್ಲಿ 4 NVIDIA V100 GPUಗಳು ಇವೆ ಹಾಗೂ Standard_NC12s_v3ನಲ್ಲಿ 2 NVIDIA V100 GPUಗಳು ಇವೆ. ಈ ಮಾಹಿತಿಗಾಗಿ ಡಾಕ್ಯುಮೆಂಟ್ ನೋಡಿ. ಪ್ರತಿಯೊಬ್ಬ ನೋಡ್‌ಗೆ ಗಳು ಇರುವ GPU ಕಾರ್ಡ್‌ಗಳ ಸಂಖ್ಯೆ param gpus_per_node ನ್ನಲ್ಲಿ ಹೊಂದಿಸಲಾಗುತ್ತದೆ. ಈ ಮೌಲ್ಯವನ್ನು ಸರಿಯಾಗಿ ಹೊಂದಿಸುವುದರಿಂದ ನೋಡ್‌ನ ಎಲ್ಲಾ GPUಗಳನ್ನು ಬಳಸಿ ಪಡೆಯಲಾಗುತ್ತದೆ. ಶಿಫಾರಸು ಮಾಡಿದ GPU ಕಂಪ್ಯೂಟ್ SKUಗಳನ್ನು ಇಲ್ಲಿ ಮತ್ತು ಇಲ್ಲಿ ಕಾಣಬಹುದು.

### Python ಗ್ರಂಥಾಲಯಗಳು

ಕೆಳಗಿನ ಸೆಲ್ ಅನ್ನು ಜಾರಿಗೊಳಿಸುವ ಮೂಲಕ ಅವಶ್ಯಕತೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ. ಇದು ಹೊಸ ಪರಿಸರದಲ್ಲಿ ಚಾಲನೆ ಮಾಡಿದಾಗ ಐಚ್ಛಿಕ ಹಂತವಲ್ಲ.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML ಜೊತೆಗೆ ಸಂವಹನ

1. ಈ Python ಸ್ಕ್ರಿಪ್ಟ್ Azure Machine Learning (Azure ML) ಸೇವೆಯೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಬಳಸಲಾಗುತ್ತದೆ. ಇದರ ಕಾರ್ಯವಿವರಣೆ:

    - ಇದು azure.ai.ml, azure.identity ಮತ್ತು azure.ai.ml.entities ಪ್ಯಾಕೇಜ್‌ಗಳಿಂದ ಅಗತ್ಯ ಮಡ್ಯೂಲ್‌ಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತದೆ. ಸಹಿತವಾಗಿ time ಮಡ್ಯೂಲ್ ಮಾಡಲಾಗಿದೆ.

    - DefaultAzureCredential() ಬಳಸಿ ಪ್ರಾಮಾಣೀಕರಣ ಮಾಡಲು ಪ್ರಯತ್ನಿಸುತ್ತದೆ, ಇದು ಸರಳೀಕೃತ ಲಾಗಿನ್ ಅನುಭವ ನೀಡುತ್ತದೆ ಮತ್ತು Azure ಕ್ಲೌಡ್‌ನಲ್ಲಿ ಅನ್ವಯಿಕೆಗಳನ್ನು ವೇಗವಾಗಿ ಅಭಿವೃದ್ಧಿಪಡಿಸಲು ಸಹಾಯಕ. ವಿಫಲವಾದರೆ, InteractiveBrowserCredential() ಮೂಲಕ ಇಂಟರಾಕ್ಟಿವ್ ಲಾಗಿನ್ ಪ್ರಾಂಪ್ಟ್ ನೀಡುತ್ತದೆ.

    - ನಂತರ from_config ವಿಧಾನದಿಂದ MLClient ಇನ್ಸ್ಟೆನ್ಸ್ ರಚಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತದೆ, ಇದು ಡೀಫಾಲ್ಟ್ ಸಂರಚನಾ ಫೈಲ್(config.json)ನಿಂದ ಕಾನ್ಫಿಗರೇಶನ್ ಓದುತ್ತದೆ. ವಿಫಲವಾದರೆ, subscription_id, resource_group_name, ಮತ್ತು workspace_name ನ್ನು ಕೈಮುಗಿದಂತೆ ನೀಡುತ್ತಾ MLClient ರಚಿಸುತ್ತದೆ.

    - "azureml" ಎಂಬ Azure ML ರಜಿಸ್ಟ್ರಿಗಾಗಿ ಇನ್ನೊ MLClient ಇನ್ಸ್ಟೆನ್ಸ್ ಸೃಷ್ಟಿಸುತ್ತದೆ. ಇದರಲ್ಲಿ ಮಾದರಿಗಳು, ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆ ಪೈಪ್ಲೈನ್ಗಳು ಮತ್ತು ಪರಿಸರಗಳು ಸಂಗ್ರಹಿತವಾಗಿವೆ.

    - ಪ್ರಯೋಗದ ಹೆಸರನ್ನು "chat_completion_Phi-3-mini-4k-instruct" ಎಂದು ನಿಗದಿಪಡಿಸುತ್ತದೆ.

    - ಪ್ರಸ್ತುತ ಕಾಲವನ್ನು (ಎಪಾಕ್‌ನಿಂದ ಸೆಕೆಂಡುಗಳಲ್ಲಿ, ದಶಮಾಂಶ ಸಹಿತ) ಪೂರ್ಣಾಂಕವಾಗಿ ಪರಿವರ್ತಿಸಿ ಮತ್ತು ನಂತರ ಸ್ಟ್ರಿಂಗ್ ಆಗಿ ಪರಿವರ್ತಿಸಿ ವಿಶಿಷ್ಟ ಟೈಮ್ಸ್ಟಾಂಪ್ ತಯಾರಿಸುತ್ತದೆ. ಇದನ್ನು ವಿಭಿನ್ನ ಹೆಸರು ಮತ್ತು ಆವೃತ್ತಿಗಳನ್ನು ರಚಿಸಲು ಬಳಸಬಹುದು.

    ```python
    # Azure ML ಮತ್ತು Azure Identity ನಿಂದ ಅಗತ್ಯವಾದ ಮಾಯ್ದೊಳುಗಳನ್ನು ಆಮದುಮಾಡಿ
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # ಸಮಯ ಮಾಯ್ದೊಳು ಆಮದುಮಾಡಿ
    
    # DefaultAzureCredential ಬಳಸಿ ಪ್ರಮಾಣೀಕೃತಿಯನ್ನು ಪ್ರಯತ್ನಿಸಿ
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # DefaultAzureCredential ವಿಫಲವಾದರೆ, InteractiveBrowserCredential ಬಳಸಿ
        credential = InteractiveBrowserCredential()
    
    # ಡೀಫಾಲ್ಟ್ ಕಾಂಫಿಗ್ ಫೈಲ್ ಬಳಸಿ MLClient ಉದಾಹರಣೆ ನಿರ್ಮಿಸಲು ಪ್ರಯತ್ನಿಸಿ
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # ಅದು ವಿಫಲವಾದರೆ, ವಿವರಗಳನ್ನು ಕೈಯಿಂದ ನೀಡುವ ಮೂಲಕ MLClient ಉದಾಹರಣೆ ನಿರ್ಮಿಸಿ
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # "azureml" ಎಂಬ Azure ML ನೋಂದಣಿ (registry)ಗಾಗಿ ಮತ್ತೊಂದು MLClient ಉದಾಹರಣೆ ರಚಿಸಿ
    # ಈ ನೋಂದಣಿಯಲ್ಲಿ ಮಾದರಿಗಳು, ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಪೈಪ್ಲೈನ್ಗಳು ಮತ್ತು ವಾತಾವರಣಗಳು (environments) ಸಂಗ್ರಹವಾಗಿವೆ
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # ಪ್ರಯೋಗ (experiment) ಹೆಸರನ್ನು ನಿಗದಿ ಮಾಡಿ
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # ವಿಶಿಷ್ಟವಾದ ಸಮಯಸ್ಟ್ಯಾಂಪ್ ಅನ್ನು ರಚಿಸಿ, ಇದು ಅನನ್ಯ ಹೆಸರುಗಳು ಮತ್ತು ಆವೃತ್ತಿಗಳಿಗಾಗಿ ಬಳಸಬಹುದು
    timestamp = str(int(time.time()))
    ```

## 2. ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆಗಾಗಿ ಮೂಲ ಮಾದರಿಯನ್ನು ಆರಿಸಿ

1. Phi-3-mini-4k-instruct 3.8B ಪ್ಯಾರಾಮೀಟರ್‌ಗಳಿರುವ, ತೂಕದಲ್ಲಿ ಸೂಕ್ಷ್ಮ, ಅತ್ಯಾಧುನಿಕ open ಮಾದರಿ ಆಗಿದ್ದು Phi-2 ಗೆ ಬಳಸಲಾದ ಡೇಟಾಸೆಟ್ ಮೇಲೆ ನಿರ್ಮಿತವಾಗಿದೆ. ಈ ಮಾದರಿ Phi-3 ಮಾದರಿ ಕುಟುಂಬಕ್ಕೆ ಸೇರಿದೆ, ಮತ್ತು ಮಿನಿ ಆವೃತ್ತಿಯು ಎರಡು ಬಗೆಯ 4K ಮತ್ತು 128K (ಮೊತ್ತುಗಳು) ಪರಿಧಿಯನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. ನಿಖರ ಉದ್ದೇಶಕ್ಕಾಗಿ ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸಲು ಈ ಮಾದರಿಯನ್ನು ಬಳಸಬೇಕು. ನೀವು ಈ ನೋಟ್‌ಬುಕ್ ಅನ್ನು ಬೇರೆ ಮಾದರಿ ಕಾರ್ಡ್‌ನಿಂದ ತೆರೆಯಿದ್ರೆ, ಮಾದರಿ ಹೆಸರು ಮತ್ತು ಆವೃತ್ತಿಯನ್ನು ಅನುಗುಣವಾಗಿ ಬದಲಿಸಿ.

> [!NOTE]
> ಮಾದರಿಯ id ಗುಣವನ್ನು ಗಮನಿಸಿ. ಇದು ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆ ಕೆಲಸಕ್ಕೆ ಇನ್‌ಪುಟ್ ಆಗಿ ಬಳಸಲಾಗುವುದು. AzureML ಸ್ಟುಡಿಯೋ Model Catalog ಮಾದರಿ ವಿವರಗಳ ಪುಟದಲ್ಲಿಯೂ Asset ID ಫೀಲ್ಡ್ ಆಗಿ ಲಭ್ಯವಿದೆ.

2. ಈ Python ಸ್ಕ್ರಿಪ್ಟ್ Azure Machine Learning (Azure ML) ಸೇವೆಯೊಂದಿಗೆ ಸಂವಹನ ಮಾಡುತ್ತಿದೆ. ಇದರ ವಿವರಣೆ:

    - model_name = "Phi-3-mini-4k-instruct" ಎಂದು ನಿಗದಿಪಡಿಸುತ್ತದೆ.

    - registry_ml_client ನ models ಗುಣದ get ವಿಧಾನ ಬಳಸಿ ನಿರ್ದಿಷ್ಟ ಹೆಸರಿನ ಮಾದರಿಯ ಇತ್ತೀಚಿನ ಆವೃತ್ತಿಯನ್ನು Azure ML ರಜಿಸ್ಟ್ರಿಯಿಂದ ಪಡೆಯುತ್ತದೆ. get ವಿಧಾನಕ್ಕೆ ಎರಡು ಅರ್ಗ್ಯೂಮೆಂಟ್‌ಗಳು ಕೊಡುವದು: ಮಾದರಿ ಹೆಸರು ಮತ್ತು 최신 ಆವೃತ್ತಿ ತೆಗೆದುಕೊಳ್ಳುವ ಲೇಬಲ್.

    - ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆಗಾಗಿ ಬಳಸದ ಮಾದರಿಯ ಹೆಸರು, ಆವೃತ್ತಿ ಮತ್ತು id ಕಾನ್ಸೋಲ್‌ಗೆ ಮುದ್ರಣ ಮಾಡುತ್ತದೆ. ಸ್ಟ್ರಿಂಗ್‌ನ format ವಿಧಾನದಿಂದ ಈ ಡೇಟಾ ಸಂದೇಶಕ್ಕೆ ಸೇರಿಸಲಾಗುತ್ತದೆ. 

    ```python
    # ಮಾದರಿ ಹೆಸರನ್ನು ಸೆಟ್ ಮಾಡಿ
    model_name = "Phi-3-mini-4k-instruct"
    
    # ಅಜೂರ್ ಎಂಎಲ್ ರೆಜಿಸ್ಟ್ರೀನಿಂದ ಮಾದರಿಯ ಇತ್ತೀಚಿನ ಸಂಸ್ಕರಣೆಯನ್ನು ಪಡೆಯಿರಿ
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # ಮಾದರಿ ಹೆಸರು, ಆವೃತ್ತಿ ಮತ್ತು ಐಡಿಯನ್ನು ಮುದ್ರಿಸಿ
    # ಈ ಮಾಹಿತಿಯು ಟ್ರ್ಯಾಕಿಂಗ್ ಮತ್ತು ಡಿಬಗ್ ಮಾಡಲು ಉಪಯುಕ್ತವಾಗಿದೆ
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. ಕೆಲಸಕ್ಕೆ ಬಳಸಲು compute ರಚಿಸಿ

ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆ ಕೆಲಸ GPU ಕಂಪ್ಯೂಟ್‌ನೊಂದಿಗೆ ಮಾತ್ರ ಕೆಲಸ ಮಾಡುತ್ತದೆ. compute ಗಾತ್ರವು ಮಾದರಿಯ ವ್ಯ modalityಗದಿಂದ ಕಾರ್ಯಾಗತ. ಈ ಸೆಲ್ ಬಳಕೆದಾರರನ್ನು ಸರಿಯಾದ compute ಆಯ್ಕೆ ಮಾಡಿಕೊಳ್ಳಲು ಮಾರ್ಗದರ್ಶನ ಮಾಡುತ್ತದೆ.

> [!NOTE]
> ಕೆಳಗಿನ computeಗಳು ಅತ್ಯಂತ ಸುಧಾರಿತ ಸಂರಚನೆಯೊಂದಿಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ. ಸಂರಚನೆಯಲ್ಲಿ ಯಾವಶೇಖಾಗಲಿ ಬದಲಾವಣೆಯಾದರೆ Cuda Out Of Memory ದೋಷ ಬರುವ ಸಾಧ್ಯತೆ ಇದೆ. ಇಂತಹ ಸಂದರ್ಭದಲ್ಲಿ compute ಗಾತ್ರವನ್ನು ದೊಡ್ಡದಾಗಿ ಮೇಲುಗೈ ಮಾಡಿ.

> [!NOTE]
> compute_cluster_size ಆಯ್ಕೆಮಾಡುವಾಗ compute ನಿಮ್ಮ resource group ನಲ್ಲಿ ಲಭ್ಯವಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿ. ಲಭ್ಯವಿಲ್ಲದ compute ಮೇಲೆ ನೀವು compute ಸಂಪನ್ಮೂಲಗಳಿಗೆ ಪ್ರವೇಶ ಕೇಳಬಹುದು.

### ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆಗೆ ಮಾದರಿ ಬೆಂಬಲ ಪರಿಶೀಲನೆ

1. ಈ Python ಸ್ಕ್ರಿಪ್ಟ್ Azure ML ಮಾದರಿಯೊಂದಿಗೆ ಸಂವಹನ ಮಾಡುತ್ತಿದೆ. ಇದರ ಕಾರ್ಯಪಟುತೆ:

    - ast ಮಡ್ಯೂಲ್ ಅನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತದೆ, ಇದು Python ಅನುಸ್ಕೃತ ನಿರ್ರೂಪಣೆಯ ಮರಗಳನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಲು ಬಳಕೆಮಾಡಲಾಗುತ್ತದೆ.

    - foundation_model ವಸ್ತುವಿನಲ್ಲಿ finetune_compute_allow_list ಎಂಬ ಟ್ಯಾಗ್ ಇರುವುದನ್ನ ಪರಿಶೀಲಿಸುತ್ತದೆ. Azure ML ಟ್ಯಾಗ್‌ಗಳು ಕೀ-ಮೌಲ್ಯ ಜೋಡಿಗಳು ಆಗಿದ್ದು, ನಿಮ್ಮ ಮಾದರಿಗಳನ್ನು ಫಿಲ್ಟರ್ ಮತ್ತು ವಿಂಗಡಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

    - finetune_compute_allow_list ಇದ್ದರೆ ast.literal_eval ಮೂಲಕ ಆ ಸ್ಟ್ರಿಂಗ್ ಮೌಲ್ಯವನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಪೈಥನ್ ಪಟ್ಟಿಗೆ ಪರಿವರ್ತಿಸುತ್ತದೆ ಮತ್ತು computes_allow_list ಗೆ ನಿಯೋಜಿಸುತ್ತದೆ. ನಂತರ compute ಪಟ್ಟಿ ಇಂದ compute ರಚಿಸುವುದಾಗಿ ಸಂದೇಶ ಮುದ್ರಣ ಮಾಡುತ್ತದೆ.

    - finetune_compute_allow_list ಇಲ್ಲದಿದ್ದರೆ computes_allow_list ನುಲ್ ಆಗಿ ನಿಗದಿಪಡಿಸಿ, ಮಾದರಿಯ ಟ್ಯಾಗ್‌ಗಳಲ್ಲಿ finetune_compute_allow_list ಇಲ್ಲದಿರುವುದಾಗಿ ತಿಳಿಸಿದ್ದಾರೆ.

    - ಸಾರಾಂಶವಾಗಿ, ಮಾದರಿಯ ಮೆಟಾಡೇಟಾದಲ್ಲಿ ನಿರ್ದಿಷ್ಟ ಟ್ಯಾಗ್‌ ಪರೀಕ್ಷಿಸಿ, ಟ್ಯಾಗ್ ಮೌಲ್ಯವನ್ನು ಪಟ್ಟಿಗೆ ಪರಿವರ್ತಿಸಿ, ಬಳಕೆದಾರರಿಗೆ ನಿರ್ದಿಷ್ಟ ಮಾಹಿತಿ ನೀಡುತ್ತದೆ.

    ```python
    # ಪೈಥಾನ್ ಅನಾವರಣ ಸಿಂಟ್ಯಾಕ್ಸ್ ವ್ಯಾಕರಣದ ಮರಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಕಾರ್ಯಗಳನ್ನು ಒದಗಿಸುವ ast ಮড್ಯೂಲ್ ಅನ್ನು ಆಮದುಮಾಡಿ
    import ast
    
    # ಮಾದರಿಯ ಟ್ಯಾಗ್‌ಗಳಲ್ಲಿ 'finetune_compute_allow_list' ಟ್ಯಾಗ್ ಇದ್ದೇ ಅಂದುಕೊಳ್ಳಿ
    if "finetune_compute_allow_list" in foundation_model.tags:
        # ಟ್ಯಾಗ್ ಇದ್ದರೆ, ast.literal_eval ಅನ್ನು ಬಳಸಿಕೊಂಡು ಟ್ಯಾಗ್‌ನ ಮೌಲ್ಯವನ್ನು (ಒಂದು ಸ್ಟ್ರಿಂಗ್) ಸುರಕ್ಷಿತ ರೀತಿಯಲ್ಲಿ ಪೈಥಾನ್ ಪಟ್ಟಿ ಆಗಿ ಪಾರ್ಸ್ ಮಾಡಿ
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # ಸ್ಟ್ರಿಂಗ್ ಅನ್ನು ಪೈಥಾನ್ ಪಟ್ಟಿ ಆಗಿ ಪರಿವರ್ತಿಸಿ
        # ಪಟ್ಟಿಯಿಂದ ಒಂದು ಕಂಪ್ಯೂಟ್ ಅನ್ನು ರಚಿಸಬೇಕೆಂದು ಸೂಚಿಸುವ ಸಂದೇಶ ಮುದ್ರಿಸಿ
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # ಟ್ಯಾಗ್ ಇಲ್ಲದಿದ್ದರೆ, computes_allow_list ಅನ್ನು None ಗೆ ಸೆಟ್ ಮಾಡಿ
        computes_allow_list = None
        # 'finetune_compute_allow_list' ಟ್ಯಾಗ್ ಮಾದರಿಯ ಟ್ಯಾಗ್‌ಗಳ ಭಾಗವಲ್ಲ ಎಂದು ಸೂಚಿಸುವ ಸಂದೇಶ ಮುದ್ರಿಸಿ
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Compute Instance ಪರಿಶೀಲನೆ

1. ಈ Python ಸ್ಕ್ರಿಪ್ಟ್ Azure ML ಸೇವೆಯೊಂದಿಗೆ ಸಂವಹನ ಮಾಡುತ್ತಿದ್ದು, compute instance ಮೇಲೆ ವಿವಿಧ ಪರಿಶೀಲನೆಗಳನ್ನು ಮಾಡುತ್ತದೆ. ವಿವರ:

    - compute_cluster ನಲ್ಲಿ ಉಳಿಸಿರುವ compute name ಉಪಯೋಗಿಸಿ compute instance ಪಡೆಯಲು ಪ್ರಯತ್ನಿಸುತ್ತದೆ. provisioning state "failed" ಇದ್ದರೆ, ValueError ಉದ್ಧರಿಸುತ್ತದೆ.

    - computes_allow_list None ಅಲ್ಲದಿದ್ದರೆ, ಪಟ್ಟಿಯ ಎಲ್ಲಾ compute ಗಾತ್ರಗಳನ್ನು lowercase ಗೆ ಬದಲಿಸಿ, ಪ್ರಸ್ತುತ compute ಗಾತ್ರ ಆ ಪಟ್ಟಿಯಲ್ಲಿ ಇದೆಯೇ ಎಂದು ಪರೀಕ್ಷಿಸಿ. ಇಲ್ಲದಿದ್ದರೆ ValueError ನೀಡುತ್ತದೆ.

    - computes_allow_list None ಆಗಿದ್ದರೆ, compute ಗಾತ್ರವು ತಿರಸ್ಕೃತ GPU VM ಗಾತ್ರ ಪಟ್ಟಿಯಲ್ಲಿ ಇದ್ದರೆ ValueError ನೀಡುತ್ತದೆ.

    - ವರ್ಕ್‌ಸ್ಪೇಸ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ compute ಗಾತ್ರಗಳ ಪಟ್ಟಿಯನ್ನು ಪಡೆಯುತ್ತದೆ. ಮೇಲೆ ಕೊಟ್ಟ ಪಟ್ಟಿಗೆ ತಕ್ಕ compute ಗಾತ್ರ ಸಿಕ್ಕಿದ್ದರೆ, ಆ compute ಗಾತ್ರದ GPUಗಳ ಸಂಖ್ಯೆಯನ್ನು ಪಡೆಯುತ್ತದೆ ಮತ್ತು gpu_count_found ನ್ನು ಸತ್ಯವಾಗಿ ನಿಗದಿಪಡಿಸುತ್ತದೆ.

    - gpu_count_found ಸತ್ಯವಾದರೆ, compute instance ನಲ್ಲಿ ಎಷ್ಟು GPU ಇದ್ದ ವಿವರಣೆ ನೀಡುತ್ತದೆ. ಇಲ್ಲದಿದ್ದರೆ ValueErrorನು ನೀಡುತ್ತದೆ.

    - ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ compute instance provisioning ಸ್ಥಿತಿ, compute ಗಾತ್ರ ಅನುಮೋದಿತ ಪಟ್ಟಿಯಲ್ಲಿ ಇದೆಯೇ ಪೋಳಿಗೊಂಡ್ಲೇ ಎಂಬುದನ್ನು, ಮತ್ತು compute ನಲ್ಲಿ ಎಷ್ಟು GPU ಇದ್ದಯೋ ಪರಿಶೀಲನೆ ಮಾಡುತ್ತದೆ.

    ```python
    # ವಿಸರ್ಜನೆಯ ಸಂದೇಶವನ್ನು ಮುದ್ರಿಸಿ
    print(e)
    # ವರ್ಕ್‌ಸ್ಪೇಸ್‌ನಲ್ಲಿ ಗಣನೆ ಗಾತ್ರ ಲಭ್ಯವಿಲ್ಲದಿದ್ದರೆ ValueError ಅನ್ನು ಎತ್ತಿ
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Azure ML ವರ್ಕ್‌ಸ್ಪೇಸ್‌ನಿಂದ ಗಣನೆ ಘಟಕವನ್ನು ಪಡೆಯಿರಿ
    compute = workspace_ml_client.compute.get(compute_cluster)
    # ಗಣನೆ ಘಟಕದ ಪ್ರೊವೀಶನಿಂಗ್ ಸ್ಥಿತಿ "ವಿಫಲ" ಆಗಿದೆಯೇ ಎಂದಾದರೆ ಪರಿಶೀಲಿಸಿ
    if compute.provisioning_state.lower() == "failed":
        # ಪ್ರೊವೀಶನಿಂಗ್ ಸ್ಥಿತಿ "ವಿಫಲ" ಆಗಿದ್ದರೆ ValueError ಅನ್ನು ಎತ್ತಿ
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # computes_allow_list None ಅಲ್ಲದಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
    if computes_allow_list is not None:
        # computes_allow_list中的ಎಲ್ಲಾ ಗಣನೆ ಗಾತ್ರಗಳನ್ನು ಚಿಕ್ಕಾಕ್ಷರಗಳಿಗೆ ಪರಿವರ್ತಿಸಿ
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # ಗಣನೆ ಘಟಕದ ಗಾತ್ರ computes_allow_list_lower_case ನಲ್ಲಿ ఉందೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
        if compute.size.lower() not in computes_allow_list_lower_case:
            # ಗಣನೆ ಘಟಕದ ಗಾತ್ರ computes_allow_list_lower_case ನಲ್ಲಿ ಇಲ್ಲದಿದ್ದರೆ ValueError ಅನ್ನು ಎತ್ತಿ
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # ಬೆಂಬಲಿಸದ GPU VM ಗಾತ್ರಗಳ ಪಟ್ಟಿ ಅನ್ನು ನಿರ್ದಿಷ್ಟ ಗೊಳಿಸಿ
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # ಗಣನೆ ಘಟಕದ ಗಾತ್ರ unsupported_gpu_vm_list ನಲ್ಲಿ ಇದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
        if compute.size.lower() in unsupported_gpu_vm_list:
            # ಗಣನೆ ಘಟಕದ ಗಾತ್ರ unsupported_gpu_vm_list ನಲ್ಲಿ ಇದ್ದರೆ ValueError ಅನ್ನು ಎತ್ತಿ
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # ಗಣನೆ ಘಟಕದಲ್ಲಿ GPUಗಳ ಸಂಖ್ಯೆ ಕಂಡುಹಿಡಿದಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುವ ಡೊಂಕೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
    gpu_count_found = False
    # ವರ್ಕ್‌ಸ್ಪೇಸ್‌ನಲ್ಲಿರುವ ಎಲ್ಲ ಲಭ್ಯವಿರುವ ಗಣನೆ ಗಾತ್ರಗಳ ಪಟ್ಟಿಯನ್ನು ಪಡೆಯಿರಿ
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # ಲಭ್ಯವಿರುವ ಗಣನೆ ಗಾತ್ರಗಳ ಪಟ್ಟಿಯನ್ನು ಓಲುವುದು
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # ಗಣನೆ ಗಾತ್ರದ ಹೆಸರು ಗಣನೆ ಘಟಕದ ಗಾತ್ರಕ್ಕೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
        if compute_sku.name.lower() == compute.size.lower():
            # ಹೊಂದಿದ್ದರೆ ಆ ಗಣನೆ ಗಾತ್ರದ GPUಗಳ ಸಂಖ್ಯೆಯನ್ನು ಪಡೆಯಿರಿ ಮತ್ತು gpu_count_found ಅನ್ನು True ಗಾಗಿ ಸೆಟ್ ಮಾಡಿ
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # gpu_count_found True ಆಗಿದ್ದರೆ ಗಣನೆ ಘಟಕದ GPUಗಳ ಸಂಖ್ಯೆಯನ್ನು ಮುದ್ರಿಸಿ
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # gpu_count_found False ಇದ್ದರೆ ValueError ಅನ್ನು ಎತ್ತಿ
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. ಮಾದರಿಗೆ ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆಗೆ ಡೇಟಾಸೆಟ್ ಆರಿಸಿ

1. ನಾವು ultrachat_200k ಡೇಟಾಸೆಟ್ ಬಳಸುತ್ತೇವೆ. ಡೇಟಾಸೆಟ್ನು ನಾಲ್ಕು ಹಂಚಿಕೆಗಳನ್ನು ಒಳಗೊಂಡಿದೆ, ಸಹಾಯಿತ ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆಗಾಗಿ (Supervised fine-tuning - sft) ಯೋಗ್ಯವಾಗಿವೆ.
ಉತ್ಪಾದನಾ ಮೌಲ್ಯಮಾನ (generation ranking - gen). ಪ್ರತಿ ಹಂಚಿಕೆಗೆ ಉದಾಹರಣೆಗಳ ಸಂಖ್ಯೆ ಕೆಳಗಿನಂತಿದೆ:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. ಮುಂದಿನ ಕೆಲವು ಸೆಲ್‌ಗಳು ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆಗಾಗಿ ಮೂಲಭೂತ ಡೇಟಾ ತಯಾರಿಕೆಯನ್ನು ತೋರಿಸುತ್ತವೆ:

### ಕೆಲವು ಡೇಟಾ ಸಾಲುಗಳನ್ನು ದೃಶ್ಯೀಕರಿಸಿ

ನಾವು ಈ ಮಾದರಿಯನ್ನು ಬೇಗನೆ ನಿರ್ವಹಿಸಲು ಆಶಿಸುತ್ತಿದ್ದೇವೆ, ಆದ್ದರಿಂದ train_sft, test_sft ಫೈಲ್‌ಗಳಲ್ಲಿ ಪೂರ್ವತಿದ್ದುಗೊಳಿಸಿದ ಸಾಲುಗಳ 5% ಉಳಿಸಿಕೊಂಡಿದ್ದೇವೆ. ಇದರಿಂದ ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸಿದ ಮಾದರಿ ಕಡಿಮೆ ನಿಖರತೆ ಹೊಂದಿದ್ದು, ಅದನ್ನು ಗಣನೀಯ ಸಮಯದಲ್ಲಿ ಬಳಸಬಾರದು.
download-dataset.py ಸ್ಕ್ರಿಪ್ಟ್ ultrachat_200k ಡೇಟಾಸೆಟ್ ಅನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡಿ ಅದನ್ನು ಸೂಕ್ಷ್ಮ ಮರುಚಲಿಸುವಿಕೆ ಪೈಪ್ಲೈನ್ ಘಟಕ ಬಳಕೆಗೂ ಸೂಕ್ತ ರೀತಿಯಲ್ಲಿ ಪರಿವರ್ತಿಸುತ್ತದೆ. ಡೇಟಾಸೆಟ್ನು ದೊಡ್ಡದಾಗಿ ಇದೆ ಆದ್ದರಿಂದ ಇಲ್ಲಿ ಅದರ ಒಂದು ಭಾಗ ಮಾತ್ರ ಹೊಂದಿಸಲಾಗಿದೆ.

1. ಕೆಳಗಿನ ಸ್ಕ್ರಿಪ್ಟ್ 5% ಡೇಟಾ ಡೌನ್ಲೋಡ್ ಮಾತ್ರ ಮಾಡಲು ಬಳಸಲಾಗುತ್ತದೆ. dataset_split_pc ಪರಾಮೀಟರ್ ಬದಲಿಸಿ ಈ ಪ್ರಮಾಣವನ್ನು ಹೆಚ್ಚಿಸಬಹುದು.

> [!NOTE]
> ಕೆಲವು ಭಾಷಾ ಮಾದರಿಗಳಿಗೆ ವಿಭಿನ್ನ ಭಾಷಾ ಕೋಡ್‌ಗಳಿವೆ ಆದ್ದರಿಂದ ಡೇಟಾಸೆಟ್‌ನ ಕಾಲಮ್ ಹೆಸರಿಗಳು ಅದಕ್ಕನುಗುಣವಾಗಿ ಇರುವುದಕ್ಕೆ ನೋಡಿಕೊಳ್ಳಿ.

1. ಡೇಟಾ ಹೀಗೆ ಕಾಣಬೇಕು ಎಂಬ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ
ಚಾಟ್-ಪೂರ್ಣತೆ ಡೇಟಾಸೆಟ್ parquet ಸ್ವರೂಪದಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾಗಿದೆ ಮತ್ತು ಪ್ರತಿಯೊಂದು ದಾಖಲೆಯು ಕೆಳಗಿನ ವಿನ್ಯಾಸವನ್ನು ಹೊಂದಿದೆ:

    - ಇದು JSON (JavaScript Object Notation) ಡಾಕ್ಯುಮೆಂಟ್, ಇದು ಜನಪ್ರಿಯ ಡೇಟಾ ವಿನಿಮಯ ಸ್ವರೂಪವಾಗಿದೆ. ಇದು ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಕೋಡ್ ಅಲ್ಲ, ಆದರೆ ಡೇಟಾ ಸಂಗ್ರಹ ಮತ್ತು ಸಾಗಿಸಲು ವಿಧಾನ.

    - "prompt": ಈ ಕುಂಜಿಯು AI ಸಹಾಯಕರಿಗೆ ನೀಡಿರುವ ಕಾರ್ಯ ಅಥವಾ ಪ್ರಶ್ನೆಯ ಸರಣಿಯನ್ನು ಹೊಂದಿದೆ.

    - "messages": ಈ ಕುಂಜಿಯು ವಸ್ತುಗಳ ಸರಣಿಯನ್ನು ಹೊಂದಿದ್ದು, ಪ್ರತಿ ವಸ್ತು ಬಳಕೆದಾರನ ಮತ್ತು AI ಸಹಾಯಕರ ನಡುವಿನ ಸಂವಾದದ ಸಂದೇಶವಾಗಿದೆ. ಪ್ರತಿ ಸಂದೇಶ ವಸ್ತು ಎರಡು ಕೀಲಿಗಳನ್ನು ಹೊಂದಿದೆ:

    - "content": ಈ ಕೀಲ್ ಸಂದೇಶದ ವಿಷಯವನ್ನು ಹೊಂದಿದೆ.
    - "role": ಈ ಕೀಲ್ ಸಂದೇಶವನ್ನು ರವಾನಿಸಿದ ಘಟಕದ ಪಾತ್ರವನ್ನು ಸೂಚಿಸುತ್ತದೆ. ಇದು "user" ಅಥವಾ "assistant" ಆಗಿರಬಹುದು.
    - "prompt_id": ಈ ಕೀಲ್ ಪ್ರಾಂಪ್ಟ್ ಗೆ ವಿಶಿಷ್ಟ ಗುರುತಿನ ಸಂಖ್ಯೆಯನ್ನು ಹೊಂದಿದೆ.

1. ಈ ವಿಶೇಷ JSON ಡಾಕ್ಯುಮೆಂಟ್‌ನಲ್ಲಿ, ಬಳಕೆದಾರನು dystopian ಕಥೆಯ ನಾಯಕ ಚಲನಚಿತ್ರ ನಿರ್ಮಿಸಲು AI ಸಹಾಯಕನನ್ನು ಕೇಳುತ್ತಾನೆ. ಸಹಾಯಕನು ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುತ್ತಾನೆ, ನಂತರ ಬಳಕೆದಾರ ಹೆಚ್ಚಿನ ವಿವರಗಳನ್ನು ಕೇಳುತ್ತಾನೆ. ಸಹಾಯಕನು ಅವುಗಳನ್ನು ನೀಡಲು ಒಪ್ಪಿಕೊಳ್ಳುತ್ತಾನೆ. ಸಂಪೂರ್ಣ ಸಂವಾದವು ನಿರ್ದಿಷ್ಟ ಪ್ರಾಂಪ್ಟ್ ಐಡಿ ಗೆ ಸಂಬಂಧಿಸಿದೆ.

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

### ಡೇಟಾ ಡೌನ್ಲೋಡ್ ಮಾಡಿ

1. ಈ Python ಸ್ಕ್ರಿಪ್ಟ್ download-dataset.py ಎಂಬ ಸಹಾಯ ಕೋಡ್ ಮೂಲಕ ಡೇಟಾಸೆಟ್ ಡೌನ್ಲೋಡ್ ಮಾಡಲು ಬಳಸಲಾಗುತ್ತಿದೆ. ಇದರ ವಿವರಣೆ:

    - ಇದು os ಮಡ್ಯೂಲ್ ಅನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತದೆ, ಇದು ಆಪರೇಟಿಂಗ್ ಸಿಸ್ಟಮ್ ಅವಲಂಬಿತ ಕಾರ್ಯಗಳನ್ನು ಉಪಯೋಗಿಸಲು.

    - os.system() ಮೂಲಕ download-dataset.py ಕಮಾಂಡ್ ಡೌನ್ಲೋಡ್ ಮಾಡಲು, ಸೂಚಿಸಿರುವ dataset HuggingFaceH4/ultrachat_200k, ಡೌನ್ಲೋಡ್ ಡೈರೆಕ್ಟರಿ ultrachat_200k_dataset ಮತ್ತು ವಿಭಾಗದ ಪ್ರಮಾಣ 5% ಒದಗಿಸುತ್ತದೆ. exit_status ತಿರುಗಿಸಿ, ಇದು ಕಮಾಂಡ್ ಮೂಲಕ ಪೂರ್ಣಗೊಂಡ ಸ್ಥಿತಿಯನ್ನು ಸೂಚಿಸುತ್ತದೆ.

    - exit_status 0 ಅಲ್ಲದಿದ್ದರೆ, ಅರ್ಥಾತ್ ಕಮಾಂಡ್ ವಿಫಲವಾದರೆ, Exception ಎಬ್ಬಿಸುತ್ತದೆ "ಡೇಟಾಸೆಟ್ ಡೌನ್ಲೋಡ್‌ನಲ್ಲಿ ದೋಷ ನಡೆದಿದೆ" ಎಂದಾಗ.

    - ಸಾರಾಂಶ: ಸಹಾಯ ಕೋಡ್ ಮೂಲಕ ಡೇಟಾಸೆಟ್ ಡೌನ್ಲೋಡ್ ಮಾಡುವ ಕಮಾಂಡ್ ಅನ್ನು ನಡೆಸಿ, ವಿಫಲವಾದರೆ ಅಪವಾದ ಎತ್ತುತ್ತದೆ.

    ```python
    # ಕಾರ್ಯಾಚರಣಾ ವ್ಯವಸ್ಥೆಯ ಅವಲಂಬಿತ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಬಳಸುವ ವಿಧಾನವನ್ನು ಒದಗಿಸುವ os ಮೋಡ್ಯೂಲ್ ಅನ್ನು ಆಮದುಮಾಡಿ
    import os
    
    # ನಿರ್ದಿಷ್ಟ ಕಮಾಂಡ್-ಲೈನ್_ARGUMENTS_ಗಳೊಂದಿಗೆ ಶೆಲ್‌ನಲ್ಲಿ download-dataset.py ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಓಡಿಸಲು os.system ಫಂಕ್ಷನ್ ಅನ್ನು ಬಳಸಿ
    # ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳು ಡೌನ್‌ಲೋಡ್ ಮಾಡಬೇಕಾದ ಡೇಟಾಸೆಟ್ (HuggingFaceH4/ultrachat_200k), ಅದನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ಡೈರೆಕ್ಟರಿ (ultrachat_200k_dataset), ಮತ್ತು ಡೇಟಾಸೆಟ್‌ನ ಶೇಕಡಾವಾರು ವಿಭಜನೆ (5) ಅನ್ನು ಸೂಚಿಸುತ್ತವೆ
    # os.system ಫಂಕ್ಷನ್ ಆದೇಶವನ್ನು ನಿರ್ವಹಿಸಿದ ನಂತರ ಆದಿಷ್ಟ ಸ್ಥಿತಿಯನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ; ಈ ಸ್ಥಿತಿಯನ್ನು exit_status ಸ್ಥಿರಾಂಕದಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾಗುತ್ತದೆ
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # exit_status 0 ಅಲ್ಲದೆ ಇರುವುದನ್ನು ಪರಿಶೀಲಿಸಿ
    # Unix ರೀತಿ ಕಾರ್ಯಾಚರಣಾ ವ್ಯವಸ್ಥೆಗಳಲ್ಲಿ, 0 ಮೌಲ್ಯವು ಒಂದು ಆದೇಶ ಯಶಸ್ವಿಯಾಗಿದೆ ಎಂದು ಸೂಚಿಸುತ್ತದೆ, ಮತ್ತು ಯಾವುದಾದರೂ ಇತರ ಸಂಖ್ಯೆ ದೋಷವೊಂದು ಕಂಡುಬಂದಿದೆ ಎಂದು ಸೂಚಿಸುತ್ತದೆ
    # exit_status 0 ಅಲ್ಲದಿದ್ದರೆ, ಡೇಟಾಸೆಟ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವಾಗ ದೋಷವಿದೆ ಎಂದು ಸೂಚಿಸುವ ಸಂದೇಶದೊಂದಿಗೆ Exception ಅನ್ನು ಎತ್ತಿ
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### ಡೇಟಾ ಅನ್ನು DataFrame ಗೆ ಲೋಡ್ ಮಾಡುವುದು

1. ಈ Python ಸ್ಕ್ರಿಪ್ಟ್ JSON Lines ಫೈಲ್ ಅನ್ನು pandas DataFrame ಗೆ ಲೋಡ್ ಮಾಡುತ್ತಿದೆ ಮತ್ತು ಮೊದಲ 5 ಸಾಲುಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ. ವಿವರಣೆ:

    - pandas ಗ್ರಂಥಾಲಯವನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತದೆ, ಇದು ಶಕ್ತಿಶಾಲಿ ಡೇಟಾ ಮಾನಿಪ್ಯುಲೇಶನ್ ಮತ್ತು ವಿಶ್ಲೇಷಣೆ ಗ್ರಂಥಾಲಯ.

    - pandas ಪ್ರದರ್ಶನ ಆಯ್ಕೆಯಲ್ಲಿ ಗರಿಷ್ಠ ಕಾಲಮ್ ಅಗಲವನ್ನು 0ಕ್ಕೆ ಸಿದ್ಧಪಡಿಸುತ್ತದೆ. ಅಂದರೆ DataFrame ಮುದ್ರಿಸುವಾಗ ಪ್ರತಿಯೊಂದು ಕಾಲಮ್‌ನ ಸಂಪೂರ್ಣ ಪಠ್ಯವನ್ನು ಕಡಿತಗೊಳಿಸದೆ ತೋರಿಸುತ್ತದೆ.
    - ಇದು pd.read_json ಫಂಕ್ಷನ್ ಬಳಸಿಕೊಂಡು ultrachat_200k_dataset ಡೈರೆಕ್ಟರಿಯ train_sft.jsonl ಫೈಲ್ ಅನ್ನು DataFrame ಆಗಿ ಲೋಡ್ ಮಾಡುತ್ತದೆ. lines=True ಆರ್ಗುಮೆಂಟ್ ಫೈಲ್ JSON Lines ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಇದೆ ಎಂದು ಸೂಚಿಸುತ್ತದೆ, ಅಲ್ಲಿ ಪ್ರತಿಯೊಂದು ಸಾಲು ಪ್ರತ್ಯೇಕ JSON ಆಬ್ಜೆಕ್ಟ್ ಆಗಿದೆ.

    - ಇದು head ಮೆತ್ತೋಡ್ ಬಳಸಿಕೊಂಡು DataFrame ನ ಮೊದಲ 5 ಸಾಲುಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ. DataFrame ನಲ್ಲಿ 5 ಕ್ಕಿಂತ ಕಡಿಮೆ ಸಾಲುಗಳಿದ್ದರೆ, ಎಲ್ಲವನ್ನೂ ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ.

    - ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ JSON Lines ಫೈಲ್ ಅನ್ನು DataFrame ಆಗಿ ಲೋಡ್ ಮಾಡಿ ಮುಂಚಿನ 5 ಸಾಲುಗಳನ್ನು ಸಂಪೂರ್ಣ ಕಾಲಮ್ ಪಠ್ಯದೊಂದಿಗೆ ಪ್ರದರ್ಶಿಸುತ್ತದೆ.
    
    ```python
    # ಪಾಂಡಾಸ್ ಲೈബ്രರಿಯನ್ನು ಆಮದುಮಾಡಿ, ಇದು ಶಕ್ತಿಯಾದ ದತ್ತಾಂಶ ಕ್ರಮಗತ ಮಾಡು ಮತ್ತು ವಿಶ್ಲೇಷಣೆ ಲೈಬ್ರರಿ
    import pandas as pd
    
    # pandas ಪ್ರದರ್ಶನ ಆಯ್ಕೆಗಳಿಗಾಗಿ ಗರಿಷ್ಟ ಕಾಲಮ್ ಅಗಲವನ್ನು 0 గా ಸೆಟ್ ಮಾಡಿ
    # ಇದರ ಅರ್ಥ, DataFrame ಮುದ್ರಣವಾದಾಗ ಪ್ರತಿಯೊಂದು ಕಾಲಮ್ ಸಂಪೂರ್ಣ ಪಠ್ಯವನ್ನು ಕಡಿತವಿಲ್ಲದೆ ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ
    pd.set_option("display.max_colwidth", 0)
    
    # ultrachat_200k_dataset ಡೈರೆಕ್ಟರಿಯಲ್ಲಿರುವ train_sft.jsonl ಫೈಲನ್ನು DataFrame ಗೆ ಲೋಡ್ ಮಾಡಲು pd.read_json ಫಂಕ್ಷನ್ ಅನ್ನು ಬಳಸಿ
    # lines=True ಆರ್ಗ್ಯೂಮೆಂಟ್ ಫೈಲ್ JSON Lines ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಇದೆ ಎಂದು ಸೂಚಿಸುತ್ತದೆ, ಅಲ್ಲಿ ಪ್ರತಿಯೊಂದು ಸಾಲು ಬೇರೆ JSON ವಸ್ತುವಾಗಿರುತ್ತದೆ
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # DataFrame ಮೊದಲ 5 ಸಾಲುಗಳನ್ನು ಪ್ರದರ್ಶಿಸಲು head ಮೆಥಡ್ ಅನ್ನು ಬಳಸಿ
    # DataFrame ನಲ್ಲಿ 5 ಕ್ಕಿಂತ ಕಡಿಮೆ ಸಾಲುಗಳಿದ್ದರೆ, ಎಲ್ಲಾ ಸಾಲುಗಳನ್ನು ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ
    df.head()
    ```

## 5. ಮಾದರಿ ಮತ್ತು ಡೇಟಾವನ್ನು ಇನ್‌ಪುಟ್ ಆಗಿ ಬಳಸಿಕೊಂಡು ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಕೆಲಸವನ್ನು ಸಲ್ಲಿಸಿ

ಚಾಟ್-ಡಿಪ್ಲೀಷನ್ ಪೈಪ್ಲೈನ್ ಕಂಪೋನೆಂಟ್ ಬಳಸುವ ಕೆಲಸವನ್ನು ರಚಿಸಿ. ಫೈನ್ ಟ್ಯೂನಿಂಗ್‌ಗೆ ಬೆಂಬಲಿತ ಎಲ್ಲಾ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳ ಬಗ್ಗೆ ತಿಳಿದುಕೊಳ್ಳಿ.

### ಫೈನ್ ಟ್ಯೂನ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ

1. ಫೈನ್ ಟ್ಯೂನ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು 2 ವರ್ಗಗಳಲ್ಲಿ ಗುಂಪು ಮಾಡಬಹುದು - ತರಬೇತಿ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು, ಆಪ್ಟಿಮೈಜೇಶನ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು

1. ತರಬೇತಿ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು ತರಬೇತಿ ಅಂಶಗಳನ್ನು ವಿವರಿಸುತ್ತವೆ, ಉದಾ:

    - ಆಪ್ಟಿಮೈಜರ್, ಶೆಡ್ಯೂಲರ್ ಬಳಸುವುದು
    - ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಪರಿಮಾಣವನ್ನು ಆಪ್ಟಿಮೈಜ್ ಮಾಡಲು ಮೆಟ್ರಿಕ್
    - ತರಬೇತಿ ಹೆಜ್ಜೆಗಳ ಸಂಖ್ಯೆ, ಬ್ಯಾಚ್ ಗಾತ್ರ ಮತ್ತು ಇತರೆ
    - ಆಪ್ಟಿಮೈಸೇಶನ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು GPU ಮೆಮೊರಿಗೆ ಆಪ್ಟಿಮೈಸ್ ಮಾಡಲು ಮತ್ತು ಕಂಪ್ಯೂಟ್ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪರಿಣಾಮವಾಗಿ ಬಳಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

1. ಕೆಳಗಿನವು ಈ ವರ್ಗಕ್ಕೆ ಸೇರಿದ ಕೆಲವು ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು. ಆಪ್ಟಿಮೈಸೇಶನ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು ಪ್ರತಿ ಮಾದರಿಗೆ ವಿಭಿನ್ನವಾಗಿದ್ದು, ಆ ವಿಭೇದಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಮಾದರಿ ಜೊತೆಗೆ ಪ್ಯಾಕೇಜ್ ಆಗಿರುತ್ತವೆ.

    - ಡೀಪ್ಸ್ಪೀಡ್ ಮತ್ತು ಲೋರಾ ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸು
    - ಮಿಶ್ರ ಪ್ರಮಾಣಿತ ತರಬೇತಿಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸು
    - ಬಹುನೋಡ್ ತರಬೇತಿಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸು

> [!NOTE]
> ಸುಪರ್ವೈಸ್ಡ್ ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಆಲೈನ್‌ಮೆಂಟ್ ಕೆಡವಬಹುದು ಅಥವಾ ಭೀಕರ ಮರೆತಿಹೋಗುವಿಕೆ ಆಗಬಹುದು. ಈ ಸಮಸ್ಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ನಂತರ ಅಲೈನ್ಮೆಂಟ್ ಹಂತವನ್ನು ನಿರ್ವಹಿಸಲು ನಾವು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ.

### ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ಯಂತ್ರ ಅಧ್ಯಯನ ಮಾದರಿಯನ್ನು ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಮಾಡುವುದಕ್ಕೆ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸುತ್ತಿದೆ. ಇದು ಏನು ಮಾಡುತ್ತದೆ ಎಂಬ ವ್ಯಾಖ್ಯಾನ ಇಲ್ಲಿದೆ:

    - ಇದು ತರಬೇತಿ ಎಪೋಕ್‌ಗಳ ಸಂಖ್ಯೆ, ತರಬೇತಿ ಮತ್ತು ಮೌಲ್ಯಮಾಪನ ಬ್ಯಾಚ್ ಗಾತ್ರಗಳು, ಕಲಿಕೆಯ ದರ ಮತ್ತು ಕಲಿಕೆ ದರ ಶೆಡ್ಯೂಲರ್ ಪ್ರಕಾರದಂತೆ ಡೀಫಾಲ್ಟ್ ತರಬೇತಿ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಸೆಟ್ ಮಾಡುತ್ತದೆ.

    - ಲೋರಾ ಮತ್ತು ಡೀಪ್‌ಸ್ಪೀಡ್ ಅನ್ವಯಿಸುವುದು ಮತ್ತು ಡೀಪ್‌ಸ್ಪೀಡ್ ಹಂತ ಇತ್ಯಾದಿಗಳನ್ನು ಒಳಗೊಂಡ ಡೀಫಾಲ್ಟ್ ಆಪ್ಟಿಮೈಸೇಶನ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಸೆಟ್ ಮಾಡುತ್ತದೆ.

    - ತರಬೇತಿ ಮತ್ತು ಆಪ್ಟಿಮೈಸೇಶನ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು finetune_parameters ಎಂಬ ಒಟ್ಟಾರೆ ಡಿಕ್ಷನರಿಗೆ ಸೇರಿಸುತ್ತದೆ.

    - foundation_modelಗೆ ಯಾವುದೇ ಮಾದರಿ-ವಿಶಿಷ್ಟ ಡೀಫಾಲ್ಟ್ ಪರಿಸರಗಳು ಇದ್ದರೆ, ಎಚ್ಚರಿಕೆ ಸಂದೇಶವನ್ನು ಮುದ್ರಿಸಿ ಮತ್ತು finetune_parameters ಡಿಕ್ಷನರಿಯನ್ನು ಅವುಗಳಿಂದ ಅಪ್ಡೇಟ್ ಮಾಡುತ್ತದೆ. ast.literal_eval ಫಂಕ್ಷನ್ ಆ ಮಾದರಿ-ವಿಶಿಷ್ಟ ನೀವುಗಳನ್ನು ಸ್ಟ್ರಿಂಗ್‌ನಿಂದ ಪೈಥಾನ್ ಡಿಕ್ಷನರಿಗೆ ಮಾರ್ಪಡಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.

    - ಚಾಲನೆಗೆ ಬಳಸುವ ಅಂತಿಮ ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

    - ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ ಯಂತ್ರ ಅಧ್ಯಯನ ಮಾದರಿಯನ್ನು ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಮಾಡಲು ಅಗತ್ಯವಾದ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸಿ ಪ್ರದರ್ಶಿಸುತ್ತದೆ, ಮತ್ತು ಡೀಫಾಲ್ಟ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಮಾದರಿ-ವಿಶಿಷ್ಟಗಳೊಂದಿಗೆ ಪರಿವರ್ತಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ.

    ```python
    # ತರಬೇತಿ ಯುಗಗಳು, ತರಬೇತಿ ಮತ್ತು ಮೌಲ್ಯಮಾಪನಕ್ಕಾಗಿ ಬ್ಯಾಚ್ ಗಾತ್ರಗಳು, ಕಲಿಕಾದರ, ಮತ್ತು ಕಲಿಕಾದರ ವೇಳಾಪಟ್ಟಿ ಪ್ರಕಾರದಂತಹ ಡಿಫಾಲ್ಟ್ ತರಬೇತಿ ಪ್ಯಾರಾಮೀಟರ್ ಗಳನ್ನು ಹೊಂದಿಸಿ
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # ಲೇಯರ್-ವೈಸ್ ರಿಲಿವೆನ್ಸ್ ಪ್ರಪಗೇಶನ್ (LoRa) ಮತ್ತು ಡೀಪ್ ಸ್ಪೀಡ್ ಅನ್ವಯಿಸಲು ಅಥವಾ ಬಳಸದಿರುವುದನ್ನು ಹಾಗೂ ಡೀಪ್ ಸ್ಪೀಡ್ ಹಂತವನ್ನು ಹೊಂದಿಸುವಂತಹ ಡಿಫಾಲ್ಟ್ ಆಪ್ಟಿಮೈಜೆಶನ್ ಪ್ಯಾರಾಮೀಟರ್ ಗಳನ್ನು ಹೊಂದಿಸಿ
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # ತರಬೇತಿ ಮತ್ತು ಆಪ್ಟಿಮೈಜೆಶನ್ ಪ್ಯಾರಾಮೀಟರ್ ಗಳನ್ನು finetune_parameters ಎಂಬ ಒಂದೇ ಡಿಕ್ಷನರಿಯಲ್ಲಿ ಸಂಯೋಜಿಸಿ
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # ಫೌಂಡೇಷನ್ಮೋಡೆಲ್ ಗೆ ಯಾವುದೇ ಮಾದರಿ-ನಿರ್ದಿಷ್ಟ ಡಿಫಾಲ್ಟ್ ಪ್ಯಾರಾಮೀಟರ್ ಗಳಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
    # ಇದ್ದರೆ, ಎಚ್ಚರಿಕೆ ಸಂದೇಶವನ್ನು ಮುದ್ರಿಸಿ ಮತ್ತು finetune_parameters ಡಿಕ್ಷನರಿಯನ್ನು ಈ ಮಾದರಿ-ನಿರ್ದಿಷ್ಟ ಡಿಫಾಲ್ಟ್ ಗಳಿಂದ ನವೀಕರಿಸಿ
    # ast.literal_eval ಕಾರ್ಯವನ್ನು ಮಾದರಿ-ನಿರ್ದಿಷ್ಟ ಡಿಫಾಲ್ಟ್ ಗಳನ್ನು ಸ್ಟ್ರಿಂಗ್‍ನಿಂದ ಪೈಥಾನ್ ಡಿಕ್ಷನರಿಗೆ ಪರಿವರ್ತಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # ಸ್ಟ್ರಿಂಗ್ ಅನ್ನು ಪೈಥಾನ್ ಡಿಗ್ಗಿಸಿಕೊಂಡಿಕೆಗೆ ಪರಿವರ್ತಿಸಿ
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # ರನ್ ಗೆ ಬಳಸಲಾಗುವ ಅಂತಿಮ ಫೈನ್ಟ್ಯೂನಿಂಗ್ ಪ್ಯಾರಾಮೀಟರ್ ಗಳ ಉ ಸೇರಿಸಿ
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### ತರಬೇತಿ ಪೈಪ್ಲೈನ್

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ಯಂತ್ರ ಅಧ್ಯಯನ ತರಬೇತಿ ಪೈಪ್ಲೈನ್ಗಾಗಿ ಪ್ರದರ್ಶನಾ ಹೆಸರನ್ನು ರಚಿಸುವ ಫಂಕ್ಷನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ, ನಂತರ ಆ ಫಂಕ್ಷನ್ ಅನ್ನು ಕರೆ ಮಾಡಿ ಮತ್ತು ಹೆಸರನ್ನು ಮುದ್ರಿಸುತ್ತದೆ. ಇದು ಏನು ಮಾಡುತ್ತದೆ ಎಂಬ ವ್ಯಾಖ್ಯಾನ ಇಲ್ಲಿದೆ:

1. get_pipeline_display_name ಫಂಕ್ಷನ್ ನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ. ಈ ಫಂಕ್ಷನ್ ತರಬೇತಿ ಪೈಪ್ಲೈನ್ ಸಂಬಂಧಿಸಿದ ಹಲವಾರು ಪ್ಯಾರಾಮೀಟರ್‌ಗಳ ಆಧಾರದ ಮೇಲೆ ಪ್ರದರ್ಶನಾ ಹೆಸರನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ.

1. ಫಂಕ್ಷನ್ ಒಳಗೆ, ಪ್ರತಿ-ಡಿವೈಸ್ ಬ್ಯಾಚ್ ಗಾತ್ರ, ಗ್ರ್ಯಾಜುಯಂಟ್ ಅಕ್ಕ್ಯುಮ್ಯುಲೇಶನ್ ಸ್ಟೆಪ್ಸ್ ಸಂಖ್ಯೆ, ಪ್ರತಿ ನೋಡ್ GPUಗಳ ಸಂಖ್ಯೆ, ಫೈನ್ ಟ್ಯೂನಿಂಗ್‌ಗೆ ಬಳಸಿದ ನೋಡ್‌ಗಳ ಸಂಖ್ಯೆ ಗುಣಿಸಲ್ಪಟ್ಟಿದ್ದು ಒಟ್ಟು ಬ್ಯಾಚ್ ಗಾತ್ರವನ್ನು ಲೆಕ್ಕಹಾಕುತ್ತದೆ.

1. ಕಲಿಕೆಯ ದರ ಶೆಡ್ಯೂಲರ್ ಪ್ರಕಾರ, ಡೀಪ್‌ಸ್ಪೀಡ್ ಅನ್ವಯಿತ 여부, ಡೀಪ್‌ಸ್ಪೀಡ್ ಹಂತ, ಲೋರಾ ಅನ್ವಯಿತ 여부, ಸಂಗ್ರಹಿಸಲು ಮಾದರಿ ಚೆಕ್‌ಪಾಯಿಂಟ್‌ಗಳ ಸಂಖ್ಯೆ ಮಿತಿಯು, ಮತ್ತು ಗರಿಷ್ಠ ಕ್ರಮದ ಉದ್ದವನ್ನು ಪಡೆದುಕೊಳ್ಳುತ್ತದೆ.

1. ಈ ಎಲ್ಲಾ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಹೈಫನ್‌ನಿಂದ ವಿಂಗಡಿಸಿದ ಸತ್ರINGSಾಗಿ ರಚಿಸುತ್ತದೆ. ಡೀಪ್‌ಸ್ಪೀಡ್ ಅಥವಾ ಲೋರಾ ಅನ್ವಯಿಸಿದರೆ, ಸ್ಟ್ರಿಂಗ್ ಟೈಪ್ "ds" ಜೊತೆಗೆ ಡೀಪ್‌ಸ್ಪೀಡ್ ಹಂತ ಅಥವಾ "lora" ಅನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ. ಇಲ್ಲದಿದ್ದರೆ "nods" ಅಥವಾ "nolora" ಸೇರಿಸಲಾಗುತ್ತದೆ.

1. ಫಂಕ್ಷನ್ ಈ ಸ್ಟ್ರಿಂಗ್ ಅನ್ನು ಪರದಾನ ಮಾಡುತ್ತದೆ, ಇದು ತರಬೇತಿ ಪೈಪ್ಲೈನ್ಗೆ ಪ್ರದರ್ಶನಾ ಹೆಸರಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ.

1. ಫಂಕ್ಷನ್ ವ್ಯಾಖ್ಯಾನಾದ ನಂತರ, ಅದನ್ನು ಕರೆ ಮಾಡಿ ಪ್ರದರ್ಶನಾ ಹೆಸರನ್ನು ರಚಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಮುದ್ರಿಸಲಾಗುತ್ತದೆ.

1. ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ ವಿವಿಧ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳ ಆಧಾರದ ಮೇಲೆ ಯಂತ್ರ ಅಧ್ಯಯನ ತರಬೇತಿ ಪೈಪ್ಲೈನ್‌ಗೆ ಪ್ರದರ್ಶನಾ ಹೆಸರನ್ನು ರಚಿಸಿ ಅದನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

    ```python
    # ತರಬೇತಿ ಪೈಪ್‌ಲೈನ್‌ನ ಪ್ರದರ್ಶನ ಹೆಸರನ್ನು ಸೃಷ್ಟಿಸಲು ಫಂಕ್ಷನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
    def get_pipeline_display_name():
        # ಪ್ರತಿ ಉಪಕರಣದ ಬ್ಯಾಚ್ ಗಾತ್ರ, ಗ್ರೇಡಿಯಂಟ್ ಸಂಗ್ರಹಣಾ ಹಂತಗಳ ಸಂಖ್ಯೆ, ಪ್ರತಿ ನೋಡ್‌ನ GPU ಗಳು ಮತ್ತು ಫೈನ್-ಟ್ಯೂನಿಂಗ್‌ಗಾಗಿ ಬಳಸಿ ನೋಡ್‌ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಗುಣಿಸಲಾಗುವುದರಿಂದ ಒಟ್ಟಾರೆ ಬ್ಯಾಚ್ ಗಾತ್ರವನ್ನು ಲೆಕ್ಕಿಸಿ
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # ಕಲಿಕೆಯ ದರ ಶೆಡ್ಯೂಲರ್ ಪ್ರಕಾರವನ್ನು ಪಡೆಯಿರಿ
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # ಡೀಪ್‌ಸ್ಪೀಡ್ ಅನ್ವಯಿತವಾಗಿದೆಯೇ ಎಂದು ಪಡೆಯಿರಿ
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # ಡೀಪ್‌ಸ್ಪೀಡ್ ಹಂತವನ್ನು ಪಡೆಯಿರಿ
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # ಡೀಪ್‌ಸ್ಪೀಡ್ ಅನ್ವಯಿತವಾದರೆ, ಪ್ರದರ್ಶನ ಹೆಸರಿನಲ್ಲಿ ಡೀಪ್‌ಸ್ಪೀಡ್ ಹಂತವನ್ನು ಹಿಂಬಾಲಿಸಿ "ds" ಅನ್ನು ಸೇರಿಸಿ; ಇಲ್ಲದಿದ್ದರೆ, "nods" ಅನ್ನು ಸೇರಿಸಿ
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # ಲೇಯರ್ ವೈಸ್ ರೆಲೆವೆನ್ಸ್ ಪ್ರಪಾಗೇಶನ್ (ಲೋರಾ) ಅನ್ವಯಿತವಾಗಿದೆಯೇ ಎಂದು ಪಡೆಯಿರಿ
        lora = finetune_parameters.get("apply_lora", "false")
        # ಲೋರಾ ಅನ್ವಯಿತವಾದರೆ, ಪ್ರದರ್ಶನ ಹೆಸರಿನಲ್ಲಿ "lora" ಅನ್ನು ಸೇರಿಸಿ; ಇಲ್ಲದಿದ್ದರೆ, "nolora" ಅನ್ನು ಸೇರಿಸಿ
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # ಉಳಿಸಿಕೊಳ್ಳಬೇಕಾದ ಮಾದರಿ ಚೆಕ್‌ಪಾಯಿಂಟ್‌ಗಳ ಸಂಖ್ಯೆಯ ಮೀರವುದನ್ನು ಪಡೆಯಿರಿ
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # ಗರಿಷ್ಠ ಅನುಕ್ರಮಣಲಂಬವನ್ನು ಪಡೆಯಿರಿ
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # ಎಲ್ಲ ಈ ನಿಯಮಗಳನ್ನು ಹೈಫನ್‌ಗಳಿಂದ ವಿಭಜಿಸಿ ಸಂಯೋಜಿಸಿ ಪ್ರದರ್ಶನ ಹೆಸರನ್ನು ರಚಿಸಿ
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
    
    # ಪ್ರದರ್ಶನ ಹೆಸರನ್ನು ಸೃಷ್ಟಿಸಲು ಫಂಕ್ಷನ್ ಅನ್ನು ಕರೆ ಮಾಡಿ
    pipeline_display_name = get_pipeline_display_name()
    # ಪ್ರದರ್ಶನ ಹೆಸರನ್ನು ಮುದ್ರಿಸಿ
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### ಪೈಪ್ಲೈನ್ ಕಾನ್ಫಿಗರ್ ಮಾಡುತ್ತಿರುವುದು

ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ಆಟ್ಲೋನ್ ಯಂತ್ರ ಅಧ್ಯಯನ SDK ಬಳಸಿ ಯಂತ್ರ ಅಧ್ಯಯನ ಪೈಪ್ಲೈನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ ಮತ್ತು ಕಾನ್ಫಿಗರ್ ಮಾಡುತ್ತದೆ. ಇದು ಏನು ಮಾಡುತ್ತದೆ ಎಂಬ ವಿಸ್ತಾರ ಇಲ್ಲಿದೆ:

1. ಇದು ಅವಶ್ಯಕ ಮ್ಯಾಡ್ಯೂಲ್‌ಗಳನ್ನು Azure AI ML SDK ನಿಂದ ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತದೆ.

1. ರೆಜಿಸ್ಟ್ರಿಯಿಂದ "chat_completion_pipeline" ಎಂಬ ಪೈಪ್ಲೈನ್ ಕಂಪೋನೆಂಟ್ ಅನ್ನು ಪಡೆದಿದೆ.

1. `@pipeline` ಡೆಕಾರೇಟರ್ ಮತ್ತು `create_pipeline` ಫಂಕ್ಷನ್ ಬಳಸಿ ಪೈಪ್ಲೈನ್ ಕೆಲಸವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ. ಪೈಪ್ಲೈನಿನ ಹೆಸರು `pipeline_display_name` ಎಂದು ನಿಗದಿ ಮಾಡಲಾಗಿದೆ.

1. `create_pipeline` ಫಂಕ್ಷನ್ ಒಳಗೆ, ಪಡೆದ ಪೈಪ್ಲೈನ್ ಕಂಪೋನೆಂಟ್ ಅನ್ನು ವಿವಿಧ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳ ಜೊತೆಗೆ ಶುರುಮಾಡಲಾಗಿದೆ, ಉದಾ: ಮಾದರಿ ಪಥ, ಬಿನ್ನಹ ಹಂತಗಳಿಗಾಗಿ ಕಂಪ್ಯೂಟ್ ಕ್ಲಸ್ಟರ್‌ಗಳು, ತರಬೇತಿ ಮತ್ತು ಪರೀಕ್ಷೆಗಾಗಿ ಡೇಟಾಸೆಟ್ ವಿಭಾಜನೆಗಳು, ಫೈನ್ ಟ್ಯೂನಿಂಗ್‌ಗೆ ಬೇಕಾದ GPUಗಳ ಸಂಖ್ಯೆ, ಮತ್ತು ಇತರೆ ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು.

1. ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಕೆಲಸದOUTPUT ಅನ್ನು ಪೈಪ್ಲೈನ್ ಕೆಲಸದ OUTPUT ಗೆ ನಕ್ಷೆಗೊಳಿಸಲಾಗಿದೆ. ಇದರಿಂದ ಫೈನ್ ಟ್ಯೂನ್ಡ್ ಮಾದರಿಯನ್ನು ಸುಲಭವಾಗಿ ನೊಂದಾಯಿಸಬಹುದು, ಇದು ಆನ್‌ಲೈನ್ ಅಥವಾ ಬ್ಯಾಚ್ ಎಂತರಿಗೆ ನಿಯೋಜಿಸಲು ಅಗತ್ಯ.

1. `create_pipeline` ಫಂಕ್ಷನ್ ಅನ್ನು ಕರೆ ಮಾಡಿ ಪೈಪ್ಲೈನ್ ನಮೂನೆಯನ್ನು ರಚಿಸಲಾಗಿದೆ.

1. ಪೈಪ್ಲೈನಿನ `force_rerun` ಸೆಟ್ಟಿಂಗ್ ಅನ್ನು `True` ಮಾಡಲಾಗಿದೆ, ಅಂದರೆ ಹಳೆಯ ಕೆಲಸಗಳಿಂದ ಕ್ಯಾಸೆಡ್ ಫಲಿತಾಂಶಗಳನ್ನು ಬಳಸುವುದಿಲ್ಲ.

1. ಪೈಪ್ಲೈನಿನ `continue_on_step_failure` ಸೆಟ್ಟಿಂಗ್ ಅನ್ನು `False` ಮಾಡಲಾಗಿದೆ, ಅಂದರೆ ಯಾವುದೇ ಹಂತದಲ್ಲಿ ವೈಫಲ್ಯ ಸಂಭವಿಸಿದರೆ ಪೈಪ್ಲೈನ್ ನಿಲ್ಲಿಸುತ್ತದೆ.

1. ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ Azure ಯಂತ್ರ ಅಧ್ಯಯನ SDK ಬಳಸಿ ಚಾಟ್ ಡಿಪ್ಲೀಷನ್ ಕಾರ್ಯಕ್ಕಾಗಿ ಯಂತ್ರ ಅಧ್ಯಯನ ಪೈಪ್ಲೈನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ ಮತ್ತು ಕಾನ್ಫಿಗರ್ ಮಾಡುತ್ತಿದೆ.

    ```python
    # ಅಜೂರ್ ಎಐ ಎಮ್‌ಎಲ್ ಎಸ್‌ಡಿಕೆನಿಂದ ಅಗತ್ಯ ಮಾಯಾಜಾಲಗಳನ್ನು ಆಮದುಮಾಡಿ
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # ರೆಜಿಸ್ಟ್ರಿಯಿಂದ "chat_completion_pipeline" ಹೆಸರಿನ ಪೈಪ್ಲೈನ್ ಘಟಕವನ್ನು ಪಡೆದುಕೊಳ್ಳಿ
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # @pipeline ಅಲಂಕಾರಕ ಮತ್ತು create_pipeline ಕಾರ್ಯವನ್ನು ಉಪಯೋಗಿಸಿ ಪೈಪ್ಲೈನ್ ಕೆಲಸವನ್ನು ನಿರ್ಧರಿಸಿ
    # ಪೈಪ್ಲೈನಿನ ಹೆಸರು pipeline_display_nameಗೆ ಸೆಟ್ ಮಾಡಲಾಗಿದೆ
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # ಬೇರೆ ಬೇರೆ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ ಪಡೆದುಕೊಳ್ಳಲಾದ ಪೈಪ್ಲೈನ್ ಘಟಕವನ್ನು ಪ್ರಾರಂಭಿಸಿ
        # ಇದರಲ್ಲಿ ಮಾದರಿ ಪಥ, ವಿಭಿನ್ನ ಹಂತಗಳಿಗಾಗಿ ಗಣನೆ ಗುಚ್ಛಗಳು, ತರಬೇತಿ ಮತ್ತು ಪರೀಕ್ಷೆಯ ಡೇಟಾಸೆಟ್ বিভಜನೆಗಳು, ಸೂಕ್ಷ್ಮೀಕರಣಕ್ಕಾಗಿ ಬಳಸುವ GPUಗಳ ಸಂಖ್ಯೆ, ಮತ್ತು ಇತರ ಸೂಕ್ಷ್ಮೀಕರಣ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳು ಸೇರಿವೆ
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # ಡೇಟಾಸೆಟ್ ವಿಭಾಗಗಳನ್ನು ಪ್ಯಾರಾಮೀಟರ್‌ಗಳಿಗೆ ನಕ್ಷೆ ಮಾಡಿ
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # ತರಬೇತಿ ಸಂಯೋಜನೆಗಳು
            number_of_gpu_to_use_finetuning=gpus_per_node,  # ಲಭ್ಯವಿರುವ ಗಣನೆಯಲ್ಲಿ GPUಗಳ ಸಂಖ್ಯೆಗೆ ಅನುಗುಣವಾಗಿ ಸೆಟ್ ಮಾಡಿ
            **finetune_parameters
        )
        return {
            # ಸೂಕ್ಷ್ಮೀಕರಣ ಕೆಲಸದ output ಅನ್ನು ಪೈಪ್ಲೈನ್ ಕೆಲಸದ output ಗೆ ನಕ್ಷೆ ಮಾಡಿ
            # ಇದರಿಂದ ನಾವು ಸುಲಭವಾಗಿ ಸೂಕ್ಷ್ಮೀಕೃತ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸಬಹುದು
            # ಮಾದರಿಯನ್ನು ಆನ್‌ಲೈನ್ ಅಥವಾ ಬ್ಯಾಚ್ ಅಂತಿಮ ಬಿಂದುಗಳಿಗೆ ನಿಯೋಜಿಸಲು ನೋಂದಾಯಿಸುವುದು ಅಗತ್ಯ
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # create_pipeline ಕ್ರಿಯೆಯನ್ನು ಕರೆಮಾಡಿ ಪೈಪ್ಲೈನ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಿ
    pipeline_object = create_pipeline()
    
    # ಹಿಂದಿನ ಕೆಲಸಗಳಿಂದ ಸಂಗ್ರಹಿಸಲಾದ ಫಲಿತಾಂಶಗಳನ್ನು ಉಪಯೋಗಿಸಬೇಡಿ
    pipeline_object.settings.force_rerun = True
    
    # ಹಂತ ವೈಫಲ್ಯವಾಗಾಗ ಮುಂದುವರಿಯುವಿಕೆಯನ್ನ Falseಗೆ ಸೆಟ್ ಮಾಡಿ
    # ಇದರ ಅರ್ಥ, ಯಾವುದೇ ಹಂತ ವಿಫಲವಾದರೆ ಪೈಪ್ಲೈನ್ ನಿಲ್ಲುತ್ತದೆ ಎಂದಾಗುತ್ತದೆ
    pipeline_object.settings.continue_on_step_failure = False
    ```

### ಕೆಲಸವನ್ನು ಸಲ್ಲಿಸಿ

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ಯಂತ್ರ ಅಧ್ಯಯನ ಪೈಪ್ಲೈನ್ ಕೆಲಸವನ್ನು ಅದೃಷ್ಟ ಯಂತ್ರ ಅಧ್ಯಯನ ವರ್ಕ್‌ಸ್ಪೇಸ್‌ಗೆ ಸಲ್ಲಿಸಿ ನಂತರ ಕೆಲಸ ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ ಕಾಯುತ್ತದೆ. ಇದು ಏನು ಮಾಡುತ್ತದೆ ಎಂಬ ವಿಸ್ತಾರ ಇಲ್ಲಿದೆ:

    - workflows_ml_client ನಲ್ಲಿ jobs ಆಬ್‌ಜೆಕ್ಟಿನ create_or_update ಮೆತ್ತೋಡ್ ಅನ್ನು ಕರೆ ಮಾಡಿ ಪೈಪ್ಲೈನ್ ಕೆಲಸವನ್ನು ಸಲ್ಲಿಸುತ್ತದೆ. ಚಾಲನೆಯಲ್ಲಿ pipeline_object ಮೂಲಕ ಸೂಚಿಸಲಾಗಿದೆ, ಮತ್ತು experiment_name ಮೂಲಕ ಕಂಪ್‌ರೆದ ಅಧೀನ ಕಾರ್ಯ ನಿಗದಿತವಾಗಿದೆ.

    - ನಂತರ workflows_ml_client jobs ಆಬ್‌ಜೆಕ್ಟಿನ stream ಮೆತ್ತೋಡ್ ಮೂಲಕ ಪೈಪ್ಲೈನ್ ಕೆಲಸ ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ ಕಾಯುತ್ತದೆ. ಕಾಯಬೇಕಾದ ಕೆಲಸ pipeline_job ಆಬ್‌ಜೆಕ್ಟಿನ name ಅಟ್ರಿಬ್ಯೂಟ್ ಮೂಲಕ ಸೂಚಿಸಲಾಗಿದೆ.

    - ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ ಯಂತ್ರ ಅಧ್ಯಯನ ಪೈಪ್ಲೈನ್ ಕೆಲಸವನ್ನು ಯಂತ್ರ ಅಧ್ಯಯನ ವರ್ಕ್‌ಸ್ಪೇಸ್‌ಗೆ ಸಲ್ಲಿಸಿ ನಂತರ ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ ಕಾಯುತ್ತದೆ.

    ```python
    # Azure ಮಷಿನ್ ಲರ್ನಿಂಗ್ ವರ್ಕ್‌ಸ್ಪೇಸ್‌ಗೆ ಪೈಪ್ಲೈನ್ ಕೆಲಸವನ್ನು ಸಲ್ಲಿಸಿ
    # ನಿರ್ವಹಿಸುವ ಪೈಪ್ಲೈನ್ pipeline_object দ্বারা ಸೂಚಿಸಲಾಗಿದೆ
    # ಕೆಲಸ ನಡೆಸಲಾದ ಪ್ರಯೋಗವನ್ನು experiment_name ಸೂಚಿಸುತ್ತದೆ
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # ಪೈಪ್ಲೈನ್ ಕೆಲಸ ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ ಕಾಯಿರಿ
    # ಕಾಯಬೇಕಾಗಿರುವ ಕೆಲಸ pipeline_job ವಸ್ತುವಿನ name ಗುಣಲಕ್ಷಣದಿಂದ ಸೂಚಿಸಲಾಗಿದೆ
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. ಫೈನ್ ಟ್ಯೂನ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ವರ್ಕ್‌ಸ್ಪೇಸ್‌ನಲ್ಲಿ ನೋಂದಾಯಿಸಿ

ನಾವು ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಕೆಲಸದ OUTPUT ಯಿಂದ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸುವೆವು. ಇದರಿಂದ ಫೈನ್ ಟ್ಯೂನ್ ಮಾಡಿದ ಮಾದರಿ ಮತ್ತು ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಕೆಲಸದ ನಡುವೆ ಲಿನಿಯೇಜ್ ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದು. ಫೈನ್ ಟ್ಯೂನಿಂಗ್ ಕೆಲಸ ಪೈಕಿ ಫೌಂಡೇಶನ್ ಮಾದರಿ, ಡೇಟಾ ಮತ್ತು ತರಬೇತಿ ಕೋಡಿಗೆ ಲಿನಿಯೇಜ್ ಟ್ರ್ಯಾಕ್ ಮಾಡುತ್ತದೆ.

### ML ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸಲಾಗುತ್ತದೆ

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ಅಜೂರ್ ಯಂತ್ರ ಅಧ್ಯಯನ ಪೈಪ್ಲೈನ್‌ನಲ್ಲಿ ತರಬೇತಿಗೊಂಡ ಯಂತ್ರ ಅಧ್ಯಯನ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸುತ್ತದೆ. ಇದು ಏನು ಮಾಡುತ್ತಿದೆ ಎಂಬ ವ್ಯಾಖ್ಯಾನ ಇಲ್ಲಿದೆ:

    - ಅನುಕೂಲಕರ ಮಾದ್ಯೂಲ್‌ಗಳನ್ನು Azure AI ML SDK ನಿಂದ ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತದೆ.

    - ವರ್ಕ್‌ಸ್ಪೇಸ್_ml_client jobs ಆಬ್‌ಜೆಕ್ಟಿನ get ಮೆತ್ತೋಡ್ ಬಳಸಿ pipeline ಕೆಲಸದಿಂದ trained_model OUTPUT ದೊರೆತಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ.

    - pipeline ಕೆಲಸದ ಹೆಸರು ಮತ್ತು OUTPUT("trained_model") ಹೆಸರನ್ನು ಉಪಯೋಗಿಸಿ ತರಬೇತಿಗೊಂಡ ಮಾದರಿಯ ಪಥವನ್ನು ರಚಿಸುತ್ತದೆ.

    - ಮೂಲ ಮಾದರಿಯ ಹೆಸರಿಯ ನಂತರ "-ultrachat-200k" ಅನ್ನು ಸೇರಿಸಿ ಮತ್ತು ಯಾವುದೇ ಸ್ಲ್ಯಾಶ್‌ಗಳನ್ನು ಹೈಫನ್‌ಗಳಿಂದ ಬದಲಿಸಿ ಫೈನ್ ಟ್ಯೂನ್ಡ್ ಮಾದರಿಯ ಹೆಸರನ್ನು ನಿರ್ಧರಿಸುತ್ತದೆ.

    - Model ಆಬ್‌ಜೆಕ್ಟ್ ರಚಿಸಿ, ಇದರಲ್ಲಿ ಮಾದರಿಯ ಪಥ, ಮಾದರಿ ಪ್ರಕಾರ (MLflow ಮಾದರಿ), ಹೆಸರು ಮತ್ತು ಆವೃತ್ತಿ, ಮತ್ತು ವಿವರಣೆ ಸೇರಿಸಲಾಗಿದೆ. ಇದರಿಂದ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸಲು ಸಿದ್ಧವಾಗುತ್ತದೆ.

    - models ಆಬ್‌ಜೆಕ್ಟಿನ create_or_update ಮೆತ್ತೋಡ್ ಅನ್ನು ಕರೆ ಮಾಡಿ Model ಆಬ್‌ಜೆಕ್ಟ್ ನೊಂದಿಗೆ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸುತ್ತದೆ.

    - ನೋಂದಾಯಿಸಲಾದ ಮಾದರಿಯನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

1. ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ ಅಜೂರ್ ಯಂತ್ರ ಅಧ್ಯಯನ ಪೈಪ್ಲೈನ್‌ನಲ್ಲಿ ತರಬೇತಿಗೊಂಡ ಯಂತ್ರ ಅಧ್ಯಯನ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸುತ್ತಿದೆ.
    
    ```python
    # ಅಗತ್ಯ ಮ್ಯೂಡ್ಯೂಲ್ಗಳನ್ನು Azure AI ML SDKನಿಂದ ಆಮದುಮಾಡಿ
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # ಪೈಪ್‌ಲೈನ್ ಕೆಲಸದಿಂದ `trained_model` ಔಟ್‌ಪುಟ್ ಲಭ್ಯವಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # ಪೈಪ್‌ಲೈನ್ ಕೆಲಸದ ಹೆಸರು ಮತ್ತು ಔಟ್‌ಪುಟ್("trained_model") ಹೆಸರನ್ನು ಫಾರ್ಮ್ಯಾಟ್ ಮಾಡಿ ತರಬೇತುಗೊಂಡ ಮಾದರಿಗೂ ಮಾರ್ಗವನ್ನು ರಚಿಸಿ
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # ಮೂಲ ಮಾದರಿಯ ಹೆಸರಿಗೆ "-ultrachat-200k" ಅನ್ನು ಸೇರಿಸಿ ಮತ್ತು ಯಾವುದೇ ಸ್ಲ್ಯಾಶ್‌ಗಳನ್ನು ಹೈಫನ್‌ಗಳೊಂದಿಗೆ ಬದಲಾಯಿಸಿ, ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡಲಾದ ಮಾದರಿಗಾಗಿ ಹೆಸರು ನಿರ್ಧರಿಸಿ
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # ವಿವಿಧ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ Model ಆಬ್ಜೆಕ್ಟ್ ಸೃಷ್ಟಿಸುವ ಮೂಲಕ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸಲು ತಯಾರಾಗಿರಿ
    # ಇದರಲ್ಲಿ ಮಾದರಿಯ ಮಾರ್ಗ, ಮಾದರಿಯ ಪ್ರಕಾರ (MLflow ಮಾದರಿ), ಮಾದರಿಯ ಹೆಸರು ಮತ್ತು ಆವೃತ್ತಿ, ಮತ್ತು ಮಾದರಿಯ ವಿವರಣೆ ಒಳಗೊಂಡಿವೆ
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # ಆವೃತ್ತಿ ಸಂಘರ್ಷ ತಪ್ಪಿಸಿಕೊಳ್ಳಲು ಟೈಮ್‌ಸ್ಟ್ಯಾಂಪ್ ಅನ್ನು ಆವೃತ್ತಿಯಾಗಿ ಬಳಸಿ
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # workspace_ml_client ನಲ್ಲಿ models ಆಬ್ಜೆಕ್ಟಿನ create_or_update ವಿಧಾನವನ್ನು ಕರೆಸುವ ಮೂಲಕ Model ಆಬ್ಜೆಕ್ಟ್ ಅನ್ನು_ARGUMENT_ ಆಗಿ ನೀಡುತ್ತಾ ಮಾದರಿಯನ್ನು ನೋಂದಾಯಿಸಿ
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # ನೋಂದಾಯಿಸಿದ ಮಾದರಿಯನ್ನು ಮುದ್ರಿಸಿ
    print("registered model: \n", registered_model)
    ```

## 7. ಫೈನ್ ಟ್ಯೂನ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್‌ಗೆ ನಿಯೋಜಿಸಿ

ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್‌ಗಳು ಯುಗಪೂರಿತ REST APIಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ, ಇದು ಆಪ್ಲಿಕೇಶನ್‌ಗಳು ಮಾದರಿಯನ್ನು ಬಳಸಲು ಏಕೀಕೃತಗೊಳಿಸುವುದಕ್ಕೆ ಸಾಧ್ಯ ಮಾಡುತ್ತದೆ.

### ಎಂತ್‌ಪಾಯಿಂಟ್ ನಿರ್ವಹಣೆ

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ಅಜೂರ್ ಯಂತ್ರ ಅಧ್ಯಯನದಲ್ಲಿ ನೋಂದಾಯಿಸಿದ ಮಾದರಿಗಾಗಿ ನಿರ್ವಹಿತ ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ರಚಿಸುತ್ತಿದೆ. ಇದರ ವಿವರ ಇಲ್ಲಿದೆ:

    - ಅಗತ್ಯ ಮಾದ್ಯೂಲ್‌ಗಳನ್ನು Azure AI ML SDK ನಿಂದ ಆಮದು ಮಾಡುತ್ತದೆ.

    - "ultrachat-completion-" ಸ್ಟ್ರಿಂಗ್‌ಗೆ ಟೈಮ್ಸ್ಟ್ಯಾಂಪ್ ಸೇರಿಸಿ ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್‌ಗೆ ವಿಶಿಷ್ಟ ಹೆಸರು ನೀಡುತ್ತದೆ.

    - ManagedOnlineEndpoint ಆಬ್‌ಜೆಕ್ಟ್ ಅನ್ನು ಹೆಸರಿನ, ವಿವರಣೆಯ, ಇಲ್ಲಿನ ಚಾವಣಿ ಮೋಡ್ ("key") ಸೇರಿದಂತೆ ಹಲವಾರು ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ ರಚಿಸಲು ಸಿದ್ಧತೆ ಮಾಡುತ್ತದೆ.

    - workflow_ml_client ನಲ್ಲಿ begin_create_or_update ಮೆತ್ತೋಡ್ ಮೂಲಕ ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ರಚಿಸುತ್ತಿದೆ. ನಂತರ ಕಾರ್ಯ ಮುಗಿಯುವವರೆಗೆ wait ಮೆತ್ತೋಡ್ ಮೂಲಕ ಕಾಯುತ್ತದೆ.

1. ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ ನೊಂದಾಯಿಸಿದ ಮಾದರಿಗಾಗಿ ಅಜೂರ್ ಯಂತ್ರ ಅಧ್ಯಯನದಲ್ಲಿ ನಿರ್ವಹಿತ ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ರಚಿಸುತ್ತಿದೆ.

    ```python
    # Azure AI ML SDK ನಿಂದ ಅಗತ್ಯಮód್ಯೂಲ್‌ಗಳನ್ನು ಆಮದುಮಾಡಿ
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # "ultrachat-completion-" ಸ್ಟ್ರಿಂಗ್‌ಗೆ ಟೈಂಸ್ಟಾಂಪ್ ಚೇರಿಸಿ ಆನ್‌ಲೈನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗೆ ವಿಶಿಷ್ಟ ಹೆಸರು ನಿರ್ಧರಿಸಿ
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # ವಿವಿಧ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ ManagedOnlineEndpoint ವಸ್ತುವನ್ನು ರಚಿಸಿ ಆನ್‌ಲೈನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಸಿದ್ಧಪಡಿಸಿ
    # ಇದರಲ್ಲಿ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ನ ಹೆಸರು, ಎಂಡ್‌ಪಾಯಿಂಟ್‌ನ ವಿವರಣೆ, ಮತ್ತು ಪ್ರಾಮಾಣೀಕರಣ ವಿಧಾನ ("key") ಸೇರಿರುತ್ತವೆ
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # ManagedOnlineEndpoint ವಸ್ತುವನ್ನು ಆರ್ಗ್ಯುಮೆಂಟ್ ಆಗಿ workspace_ml_client ನ begin_create_or_update ವಿಧಾನವನ್ನು ಕರೆ ಮಾಡಿ ಆನ್‌ಲೈನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ರಚಿಸಿ
    # ನಂತರ wait ವಿಧಾನವನ್ನು ಕರೆ ಮಾಡಿ ರಚನಾ ಪ್ರಕ್ರಿಯೆ ಪೂರ್ಣಗೊಳ್ಳುವುದಕ್ಕೆ ಕಾಯಿರಿ
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> ನೀವು ಇಲ್ಲಿ ನಿಯೋಜನೆಗಾಗಿ ಬೆಂಬಲಿತ SKU ಗಳ ಪಟ್ಟಿ ಕಾಣಬಹುದು - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸುವುದು

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ನೋಂದಾಯಿಸಿರುವ ಯಂತ್ರ ಅಧ್ಯಯನ ಮಾದರಿಯನ್ನು ಅಜೂರ್ ಯಂತ್ರ ಅಧ್ಯಯನದಲ್ಲಿ ನಿರ್ವಹಿತ ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್‌ಗೆ ನಿಯೋಜಿಸುತ್ತಿದೆ. ಇದರ ವಿವರ ಇಲ್ಲಿದೆ:

    - ast ಮ್ಯಾಡ್ಯೂಲ್ ಅನ್ನು ಆಮದು ಮಾಡುತ್ತದೆ, ಇದು ಪೈಥಾನ್ ಸಿಂಟ್ಯಾಕ್ಸ್ ಗ್ರ್ಯಾಂಮರ್ ಮರಿಗಳನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಲು ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.

    - ನಿಯೋಜನೆಗಾಗಿ ಇನ್‌ಸ್ಟನ್ಸ್ ಟೈಪ್ ಅನ್ನು "Standard_NC6s_v3" ಎಂದು ನಿಗದಿಗೊಳಿಸುತ್ತದೆ.

    - foundation model ನಲ್ಲಿ inference_compute_allow_list ಟ್ಯಾಗ್ ಇದ್ದರೆ, ಅದರ ಮೌಲ್ಯವನ್ನು ಸ್ಟ್ರಿಂಗ್‌ನಿಂದ ಪೈಥಾನ್ ಪಟ್ಟಿಗೆ ಪರಿವರ್ತಿಸಿ inference_computes_allow_list ಗೆ ನೀಡುತ್ತದೆ. ಇಲ್ಲದಿದ್ದರೆ None ನಿಗದಿ ಮಾಡುತ್ತದೆ.

    - ನಿರ್ದಿಷ್ಟ ಇನ್‌ಸ್ಟನ್ಸ್ ಟೈಪ್ ಆ ಅನ್ವಯ ಪಟ್ಟಿಯಲ್ಲಿ ಇದೆಯೆಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ. ಇಲ್ಲದಿದ್ದರೆ ಬಳಕೆದಾರರನ್ನು ಅನುಮೋದಿತ ಪಟ್ಟಿಯಿಂದ ಇನ್‌ಸ್ಟನ್ಸ್ ಟೈಪ್ ಆಯ್ಕೆ ಮಾಡಲು ಸೂಚಿಸುತ್ತದೆ.

    - ManagedOnlineDeployment ಆಬ್‌ಜೆಕ್ಟ್ ಅನ್ನು ನಿಯೋಜನೆಗೆ ಸಿದ್ಧಪಡಿಸುತ್ತದೆ. ಇದರಲ್ಲಿ ನಿಯೋಜನೆ ಹೆಸರು, ಎಂತ್‌ಪಾಯಿಂಟ್ ಹೆಸರು, ಮಾದರಿ ಐಡಿ, ಇನ್‌ಸ್ಟನ್ಸ್ ಮಾದರಿ ಮತ್ತು ಗಣಿ, ಲೈವ್‌ನೆಸ್ ಪ್ರೋಬ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳು, ವಿನಂತಿ ಸೆಟ್ಟಿಂಗ್‌ಗಳು ಸೇರಿವೆ.

    - workflow_ml_client ನಲ್ಲಿ begin_create_or_update ಮೂಲಕ ನಿಯೋಜನೆಯನ್ನು ರಚಿಸಿ wait ಮೂಲಕ ಕಾರ್ಯ ಮುಗಿಯುವವರೆಗೆ ಕಾಯುತ್ತದೆ.

    - ಎಂತ್‌ಪಾಯಿಂಟ್ ಗೆ ಟ್ರಾಫಿಕ್ ಅನ್ನು 100% "demo" ನಿಯೋಜನೆಗೆ ನೇರವಾಗಿ ನೀಡುತ್ತದೆ.

    - begin_create_or_update ಮೂಲಕ ಎಂತ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ನವೀಕರಿಸಿ result ಮೂಲಕ ನವೀಕರಣ ಕಾರ್ಯ ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ ಕಾಯುತ್ತದೆ.

1. ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ ನೊಂದಾಯಿಸಿದ ಯಂತ್ರ ಅಧ್ಯಯನ ಮಾದರಿಯನ್ನು ಅಜೂರ್ ಯಂತ್ರ ಅಧ್ಯಯನದಲ್ಲಿ ನಿರ್ವಹಿತ ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್‌ಗೆ ನಿಯೋಜಿಸುತ್ತಿದೆ.

    ```python
    # ಪೈಥಾನ್ ಅವ್ಯಕ್ತ ವ್ಯವಸ್ಥಿತ ವ್ಯಾಕರಣದ ಮರಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಮಾಡಲು ಕಾರ್ಯಗಳನ್ನು ಒದಗಿಸುವ ast ಮಾಯಾಜಾಲವನ್ನು ಆಮದುಮಾಡಿ
    import ast
    
    # ನಿಯೋಜನೆಗಾಗಿ ಉದಾಹರಣೆ ಪ್ರಕಾರವನ್ನು ಹೊಂದಿಸಿ
    instance_type = "Standard_NC6s_v3"
    
    # ಅಸ್ತಿತ್ವದಲ್ಲಿದೆಯೇ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸಿ `inference_compute_allow_list` ಟ್ಯಾಗ್ ನ ಅಸ್ತಿತ್ವವನ್ನು ಸ್ಥಾಪನಾ ಮಾದರಿಯಲ್ಲಿ
    if "inference_compute_allow_list" in foundation_model.tags:
        # ಅದೆ ಇದ್ದರೆ, ಟ್ಯಾಗ್ ಮೌಲ್ಯವನ್ನು ಪಠ್ಯದಿಂದ ಪೈಥಾನ್ ಪಟ್ಟಿಗೆ ಬದಲಾಯಿಸಿ ಮತ್ತು `inference_computes_allow_list` ಗೆ ಹಂಚಿ
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # ಇಲ್ಲದಿದ್ದರೆ, `inference_computes_allow_list` ಅನ್ನು `None` ಗೆ ಹೊಂದಿಸಿ
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # ಸೂಚಿಸಿದ ಉದಾಹರಣೆ ಪ್ರಕಾರವು ಅನುಮತಿಸಲಾದ ಪಟ್ಟಿಯಲ್ಲಿ ಇದ್ದರೆ ಪರಿಶೀಲಿಸಿ
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # ವಿವಿಧ ಪರಿಮಾಣಗಳನ್ನು ಹೊಂದಿರುವ `ManagedOnlineDeployment` ವಸ್ತುವನ್ನು ಸೃಷ್ಟಿಸುವ ಮೂಲಕ ನಿಯೋಜನೆಯನ್ನು ಸಿದ್ಧಪಡಿಸಿ
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # `workspace_ml_client` ನ `begin_create_or_update` ವಿಧಾನವನ್ನು ಕರೆ ಮಾಡಿ `ManagedOnlineDeployment` ವಸ್ತುವನ್ನು ಆರ್ಗುಮೆಂಟ್ ಆಗಿ ನೀಡಿ ನಿಯೋಜನೆ ಸೃಷ್ಟಿಸಿ
    # ನಂತರ ಸೃಷ್ಟಿ ಕಾರ್ಯ ಪೂರ್ಣಗೊಳ್ಳಲು `wait` ವಿಧಾನವನ್ನು ಕರೆ ಮಾಡಿ ಕಾಯಿರಿ
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # ಅಂತಿಮ ಬಿಂದುವಿನ ಸಂಚಾರವನ್ನು "ಡೆಮೊ" ನಿಯೋಜನೆಗೆ 100% ಸಂಚಾರವನ್ನು ನೇರಿಸಲು ಹೊಂದಿಸಿ
    endpoint.traffic = {"demo": 100}
    
    # `workspace_ml_client` ನ `begin_create_or_update` ವಿಧಾನವನ್ನು ಕರೆ ಮಾಡಿ `endpoint` ವಸ್ತುವನ್ನು ಆರ್ಗುಮೆಂಟ್ ಆಗಿ ನೀಡಿ ಅಂತಿಮ ಬಿಂದುವನ್ನು ನವೀಕರಿಸಿ
    # ನಂತರ ನವೀಕರಣ ಕಾರ್ಯ ಪೂರ್ಣಗೊಳ್ಳಲು `result` ವಿಧಾನವನ್ನು ಕರೆ ಮಾಡಿ ಕಾಯಿರಿ
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. ಉದಾಹರಣಾ ಡೇಟಾವಿಂದ ಎಂತ್‌ಪಾಯಿಂಟ್ ಪರೀಕ್ಷೆ ಮಾಡಿ

ನಾವು ಪರೀಕ್ಷೆ ಡೇಟಾಸೆಟ್‌ನಿಂದ ಕೆಲವು ಸಂಕಲ್ಪ ಡೇಟಾವನ್ನು ಪಡೆದು ಆನ್‌ಲೈನ್ ಎಂತ್‌ಪಾಯಿಂಟ್‌ಗೆ ಇನ್‌ಫರೆನ್ಸ್‌ಗೆ ಸಲ್ಲಿಸಲಿದ್ದೇವೆ. ನಂತರ ಅಂಕೆಗಳು ಮತ್ತು ನಿಜವಾದ ಲೇಬಲ್‌ಗಳನ್ನು ಪಕ್ಕದವಾಗಿ ತೋರಿಸುವೆವು.

### ಫಲಿತಾಂಶಗಳನ್ನು ಓದುವುದು

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ JSON Lines ಫೈಲ್ ಅನ್ನು pandas DataFrame ಆಗಿ ಓದಿ, ರ್ಯಾಂಡಂ ಮಾದರಿಯನ್ನು ತೆಗೆದು, ಸೂಚ್ಯಂಕವನ್ನು ಮರುಹೊಂದಿಸುತ್ತದೆ. ವಿವರ ಇಲ್ಲಿದೆ:

    - ./ultrachat_200k_dataset/test_gen.jsonl ಫೈಲ್ ಅನ್ನು pandas DataFrame ಆಗಿ ಓದುಕೊಳ್ಳುತ್ತದೆ. read_json ಫಂಕ್ಷನ್ ಅನ್ನು lines=True ಆರ್ಗುಮೆಂಟ್ ಬಳಸಿ ಉಪಯೋಗಿಸಲಾಗುತ್ತದೆ ಏಕೆಂದರೆ ಫೈಲ್ JSON Lines ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿದೆ, ಅಲ್ಲಿ ಪ್ರತಿ ಸಾಲು ಪ್ರತ್ಯೇಕ JSON ಆಬ್ಜೆಕ್ಟ್ ಆಗಿದೆ.

    - DataFrame ನಿಂದ 1 ರ್ಯಾಂಡಂ ಸಾಲನ್ನು ಆಯ್ಕೆಮಾಡುತ್ತದೆ. sample ಫಂಕ್ಷನ್ n=1 ಆರ್ಗುಮೆಂಟ್ ಬಳಸಿ ಇದನ್ನು ನಿಗದಿಗೊಳಿಸಿದೆ.

    - DataFrame ನ ಸೂಚ್ಯಂಕವನ್ನು ಮರುಹೊಂದಿಸುತ್ತದೆ. reset_index ಡ್ರಾಪ್=True ಎಂದು ಮೂಲ ಸೂಚ್ಯಂಕವನ್ನು ಡ್ರಾಪ್ ಮಾಡಿ ಹೊಸ ಸಂಖ್ಯಾತ್ಮಕ ಸೂಚ್ಯಂಕವನ್ನು ಕಲ್ಪಿಸುತ್ತದೆ.

    - head ಫಂಕ್ಷನ್ 2 ಆರ್ಗುಮೆಂಟ್ ಜೊತೆ DataFrame ನ ಮೊದಲ 2 ಸಾಲುಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ. ಆದರೆ ರ್ಯಾಂಡಂ ಮಾದರಿಯ ನಂತರ DataFrame ನಲ್ಲಿ ಕೇವಲ ಒಂದು ಸಾಲು ಇರುವುದರಿಂದ, ಅದಷ್ಟೇ ಸಾಲನ್ನು ಮಾತ್ರ ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ.

1. ಸಾರಾಂಶವಾಗಿ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ JSON Lines ಫೈಲ್ ಅನ್ನು pandas DataFrame ಆಗಿ ಓದಿ, 1 ರ್ಯಾಂಡಂ ಸಾಲನ್ನು ಆಯ್ದು, ಸೂಚ್ಯಂಕವನ್ನು ಮರುಹೊಂದಿಸಿ ಮೊದಲ ಸಾಲನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ.
    
    ```python
    # pandas ಗ್ರಂಥಾಲಯವನ್ನು ಆಮದುಮಾಡಿ
    import pandas as pd
    
    # JSON Lines ಫೈಲ್ './ultrachat_200k_dataset/test_gen.jsonl' ಅನ್ನು pandas DataFrame‌ಗೆ ಓದಿ
    # 'lines=True' ನಿಯಾಮಕವು ಫೈಲ್ JSON Lines ಸ್ವರೂಪದಲ್ಲಿದೆ ಎಂದು ಸೂಚಿಸುತ್ತದೆ, ಇಲ್ಲಿ ಪ್ರತಿಯೊಂದು ಸಾಲೂ ವಿಭಿನ್ನ JSON ಆಬ್ಜೆಕ್ಟ್ ಆಗಿದೆ
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # DataFrame ನಿಂದ 1 ಸಾಲಿನ ಯಾದೃಚ್ಛಿಕ ಮಾದರಿಯನ್ನು ತೆಗೆದುಕೊಳ್ಳಿ
    # 'n=1' ನಿಯಾಮಕವು ಆಯ್ಕೆಮಾಡಲಾದ ಯಾದೃಚ್ಛಿಕ ಸಾಲುಗಳ ಸಂಖ್ಯೆಯನ್ನು ನಿರ್ಧರಿಸುತ್ತದೆ
    test_df = test_df.sample(n=1)
    
    # DataFrame ನ ಸೂಚ್ಯಂಕವನ್ನು ಮರುನಿಗದಿಪಡಿಸಿ
    # 'drop=True' ನಿಯಾಮಕವು ಮೂಲ ಸೂಚ್ಯಂಕವನ್ನು ತೊಡೆದು ಹಾಕಿ ಹೊಸ ಡೀಫಾಲ್ಟ್ ಪೂರ್ಣಾಂಕಗಳ ಸೂಚ್ಯಂಕವನ್ನು ಬದಲಾಯಿಸಬೇಕೆಂದು ಸೂಚಿಸುತ್ತದೆ
    # 'inplace=True' ನಿಯಾಮಕವು DataFrame ಅನ್ನು ಸ್ಥಳದಲ್ಲಿಯೇ ಪರಿವರ್ತಿಸಲು (ಹೊಸ ವಸ್ತುವಿಲ್ಲದೆ) ಸೂಚಿಸುತ್ತದೆ
    test_df.reset_index(drop=True, inplace=True)
    
    # DataFrame ನ ಮೊದಲ 2 ಸಾಲುಗಳನ್ನು ತೋರಿಸಿ
    # ಆದಾಗ್ಯೂ, ಮಾದರಿಮಾಡಿದ ನಂತರ DataFrame ನಲ್ಲಿ ಒಂದೇ ಸಾಲು ಇದರಿಂದ ಇದರಿಂದ ಕೇವಲ ಆ ಒಂದು ಸಾಲು ಪ್ರದರ್ಶಿಸಲಾಗುವುದು
    test_df.head(2)
    ```

### JSON ಆಬ್ಜೆಕ್ಟ್ ರಚನೆ

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ನಿಗದಿತ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ JSON ಆಬ್ಜೆಕ್ಟ್ ರಚಿಸಿ ಅದನ್ನು ಫೈಲ್‌ಗೆ ಉಳಿಸುತ್ತದೆ. ಇದು ಏನು ಮಾಡುತ್ತದೆ ಎಂಬ ವಿವರ ಇಲ್ಲಿದೆ:

    - json ಮೋಡ್ಯೂಲ್ ಅನ್ನು ಆಮದು ಮಾಡುತ್ತದೆ, ಇದು JSON ಡೇಟಾ ಕಾರ್ಯಾಚರಣೆಗೆ ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.
    - ಇದು ಮೆಷಿನ್ ಲರ್ನಿಂಗ್ ಮಾದರಿಗಾಗಿ ಮಾನದಂಡಗಳನ್ನು ಪ್ರತಿನಿಧಿಸುವ ಕೀಲಿಗಳು ಮತ್ತು ಮೌಲ್ಯಗಳೊಂದಿಗೆ parameters ಎಂಬ ಡಿಕ್ಷನರಿಯನ್ನು ರಚಿಸುತ್ತದೆ. ಕೀಲಿಗಳು "temperature", "top_p", "do_sample", ಮತ್ತು "max_new_tokens" ಆಗಿದ್ದು, ಅದರ ಸಮಾನ ಮೌಲ್ಯಗಳು ಕ್ರಮವಾಗಿ 0.6, 0.9, True, ಮತ್ತು 200 ಆಗಿವೆ.

    - ಇದು ಇನ್ನೊಂದು ಡಿಕ್ಷನರಿ test_json ಅನ್ನು ರಚಿಸುತ್ತದೆ, ಅದು "input_data" ಮತ್ತು "params" ಎಂಬ ಎರಡು ಕೀಲಿಗಳನ್ನು ಹೊಂದಿದೆ. "input_data" ಮೌಲ್ಯವು ಇನ್ನೊಂದು ಡಿಕ್ಷನರಿಯಾಗಿದೆ, ಅದು "input_string" ಮತ್ತು "parameters" ಎಂಬ ಕೀಲಿಗಳನ್ನು ಹೊಂದಿದೆ. "input_string" ಮೌಲ್ಯವು test_df ಡೇಟಾಫ್ರೇಮ್‌ನ ಮೊದಲ ಸಂದೇಶವನ್ನು ಒಳಗೊಂಡಿರುವ ಪಟ್ಟಿಯಾಗಿದೆ. "parameters" ಮೌಲ್ಯವು ಹಿಂದಿನಿಂದ ರಚಿಸಿದ parameters ಡಿಕ್ಷನರಿಯಾಗಿದೆ. "params" ಮೌಲ್ಯವು ಖಾಲಿ ಡಿಕ್ಷನರಿಯಾಗಿದೆ.

    - ಇದು sample_score.json ಎಂಬ ಫೈಲನ್ನು ತೆರೆಯುತ್ತದೆ.
    
    ```python
    # JSON ಡೇಟಾ ಜೊತೆ ಕೆಲಸ ಮಾಡಲು ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಒದಗಿಸುವ json ಮಡ್ಯುಲ್ ಅನ್ನು ಆಮದುಮಾಡಿ
    import json
    
    # ಯಂತ್ರಾಭ್ಯಾಸ ಮಾದರಿಗಾಗಿ ಪರಿಮಾಣಗಳನ್ನು ಪ್ರತಿನಿಧಿಸುವ ಕೀಲಿಗಳು ಮತ್ತು ಮೌಲ್ಯಗಳನ್ನು ಹೊಂದಿರುವ `parameters` ಎಂಬ ಡಿಕ್ಷನರಿ ರಚಿಸಿ
    # ಕೀಲಿಗಳು "temperature", "top_p", "do_sample", ಮತ್ತು "max_new_tokens" ಆಗಿದ್ದು, ಅವುಗಳ ಅನುಗುಣ ಬುದ್ಧಿಮತ್ತೆಗಳು ಕ್ರಮವಾಗಿ 0.6, 0.9, ಸತ್ಯ(True), ಮತ್ತು 200 ಆಗಿವೆ
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # "input_data" ಮತ್ತು "params" ಎಂಬ ಎರಡು ಕೀಲಿಗಳನ್ನು ಹೊಂದಿರುವ ಇನ್ನೊಂದು ಡಿಕ್ಷನರಿ `test_json` ರಚಿಸಿ
    # "input_data" ಮೌಲ್ಯವು "input_string" ಮತ್ತು "parameters" ಎಂಬ ಕೀಲಿಗಳನ್ನು ಹೊಂದಿರುವ ಮತ್ತೊಂದು ಡಿಕ್ಷನರಿ
    # "input_string" ಮೌಲ್ಯವು `test_df` ಡೇಟಾ‌ಫ್ರೇಮ್‌ನ ಮೊದಲ ಸಂದೇಶವನ್ನು ಒಳಗೊಂಡಿರುವ ಪಟ್ಟಿ
    # "parameters" ಮೌಲ್ಯವು ಮಿಕ್ಕಿ ರಚಿಸಿರುವ `parameters` ಡಿಕ್ಷನರಿ
    # "params" ಮೌಲ್ಯವು ಖಾಲಿ ಡಿಕ್ಷನರಿ
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # `./ultrachat_200k_dataset` ಡೈರೆಕ್ಟರಿಯಲ್ಲಿನ `sample_score.json` ಎಂಬ ಫೈಲ್ ಅನ್ನು ಬರೆಯುವ ಸ್ಥಿತಿಯಲ್ಲಿ ತೆರೆಯಿರಿ
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # `json.dump` ಫಂಕ್ಷನ್ ಬಳಸಿ `test_json` ಡಿಕ್ಷನರಿಯನ್ನು JSON ಸ್ವರೂಪದಲ್ಲಿ ಫೈಲ್‌ಗೆ ಬರೆಸಿ
        json.dump(test_json, f)
    ```

### ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಆಮಂತ್ರಿಸುವುದು

1. ಈ ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ Azure ಮೆಷಿನ್ ಲರ್ನಿಂಗ್‌ನ ಆನ್‌ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಸಕೋರಿಂಗ್ ಮಾಡಲಾಗುವ JSON ಫೈಲ್ ಅನ್ನು ಆಮಂತ್ರಿಸುತ್ತದೆ. ಇದರ ಕೆಲಸದ ವಿವರಣೆ ಹೀಗಿದೆ:

    - ಇದು workspace_ml_client ವಸ್ತುವಿನ online_endpoints ಪ್ರಾಪರ್ಟಿಯ invoke ವಿಧಾನವನ್ನು ಕರೆಸುತ್ತದೆ. ಈ ವಿಧಾನವು ಆನ್‌ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗೆ ವಿನಂತಿ ಕಳುಹಿಸಲು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಲು ಬಳಸಲ್ಪಡುತ್ತದೆ.

    - ಇಲ್ಲಿ ಕೊಟ್ಟಿರುವವರು ಎಂಡ್ಪಾಯಿಂಟ್‌ನ ಹೆಸರು ಮತ್ತು ಸ್ಥಾಪನೆಯನ್ನು endpoint_name ಮತ್ತು deployment_name ವಾದಗಳ ಮೂಲಕ ಸೂಚಿಸುತ್ತಾರೆ. ಈ ಸಂದರ್ಭದಲ್ಲಿ, ಎಂಡ್ಪಾಯಿಂಟ್ ಹೆಸರನ್ನು online_endpoint_name ಚರದಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾಗಿದೆ ಮತ್ತು ಸ್ಥಾಪನೆಯ ಹೆಸರು "demo".

    - JSON ಫೈಲ್ ಅನ್ನು ಸ್ಕೋರ್ ಮಾಡಲು request_file ವಾದ ಬಳಕೆ ಮಾಡಲಾಗಿದೆ. ಇಲ್ಲಿ ಫೈಲ್ ಸ್ಥಳ ./ultrachat_200k_dataset/sample_score.json.

    - ಎಂಡ್ಪಾಯಿಂಟ್‌ನಿಂದ ಲಭಿಸುವ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು response ಪರಿವರ್ತಕದಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾಗುತ್ತದೆ.

    - ಕಚ್ಚಾ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

1. ಸಂಕ್ಷಿಪ್ತವಾಗಿ ಹೇಳಬಹುದಾದರೆ, ಈ ಸ್ಕ್ರಿಪ್ಟ್ Azure ಮೆಷಿನ್ ಲರ್ನಿಂಗ್‌ನ ಆನ್‌ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಸಾಹಿತ್ಯ ಸ್ಕೋರ್ ಮಾಡಲು ಆಮಂತ್ರಿಸುತ್ತದೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

    ```python
    # `sample_score.json` ಫೈಲ್ ಅನ್ನು ಅಂಕ ಗಣನೆ ಮಾಡಲು Azure ಮೆಷೀನ್ ಲರ್ನಿಂಗ್‌ನ ಆನ್ಲೈನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಕರೆಮಾಡಿ
    # `workspace_ml_client` ವಸ್ತುವಿನ `online_endpoints` ಗುಣಲಕ್ಷಣದ `invoke` ವಿಧಾನವನ್ನು ಆನ್ಲೈನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗೆ ವಿನಂತಿಯನ್ನು ಕಳುಹಿಸಲು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಲು ಉಪಯೋಗಿಸಲಾಗುತ್ತದೆ
    # `endpoint_name` ಆರ್ಗ್ಯುಮೆಂಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ನ ಹೆಸರನ್ನು ಸೂಚಿಸುತ್ತದೆ, ಅದು `online_endpoint_name` ಚರದಲ್ಲಿ ಸಂಗ್ರಹಿಸಲ್ಪಟ್ಟಿದೆ
    # `deployment_name` ಆರ್ಗ್ಯುಮೆಂಟ್ ನಿಯೋಜನೆಯ ಹೆಸರನ್ನು ಸೂಚಿಸುತ್ತದೆ, ಅದು "demo" ಆಗಿದೆ
    # `request_file` ಆರ್ಗ್ಯುಮೆಂಟ್ ಅಂಕ ಸಂಕಲನಕ್ಕಾಗಿ ಬಳಸಬೇಕಾದ JSON ಫೈಲ್ ಮಾರ್ಗವನ್ನು ಸೂಚಿಸುತ್ತದೆ, ಅದು `./ultrachat_200k_dataset/sample_score.json` ಆಗಿದ್ದು
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # ಎಂಡ್‌ಪಾಯಿಂಟ್‌ನ ಕಚ್ಚಾ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮುದ್ರಿಸಿ
    print("raw response: \n", response, "\n")
    ```

## 9. ಆನ್‌ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಅಳಿಸಿ

1. ಎಂಡ್ಪಾಯಿಂಟ್‌ನ ಬಳಕೆಯ ಹಿಸಾಬಿಗಾಗಿ ಬಿಲ್ಲಿಂಗ್ ಮೀಟರ್ ಕಾರ್ಯನಿರ್ವಹಣೆಯಲ್ಲಿರಬಾರದು ಎಂದು ಮರೆಯಬೇಡಿ. ಈ ಪೈಥಾನ್ ಸಾಲು Azure ಮೆಷಿನ್ ಲರ್ನಿಂಗ್‌ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಅಳಿಸುತ್ತಿದೆ. ವಿವರಣೆ ಹೀಗಿದೆ:

    - ಇದು workspace_ml_client ವಸ್ತುವಿನ online_endpoints ಪ್ರಾಪರ್ಟಿಯ begin_delete ವಿಧಾನವನ್ನು ಕರೆಸುತ್ತದೆ. ಈ ವಿಧಾನ ಆನ್‌ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅಳಿಸುವಿಕೆಯನ್ನು ಪ್ರಾರಂಭಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.

    - ಅಳಿಸಲು ಯೋಚಿಸಿದ ಎಂಡ್ಪಾಯಿಂಟ್ ನಾಮವನ್ನು name ವಾದದ ಮೂಲಕ ಸೂಚಿಸಲಾಗುತ್ತದೆ. ಇಲ್ಲಿ ಎಂಡ್ಪಾಯಿಂಟ್ ಹೆಸರು online_endpoint_name ಚರದಲ್ಲಿ ಇದೆ.

    - ಅಳಿಸುವಿಕೆಯ ಕಾರ್ಯನಿರ್ವಹಣೆಯ ಪೂರ್ಣತೆಗಾಗಿ ಕಾತರವಾಗಿ wait ವಿಧಾನವನ್ನು ಕರೆಸುತ್ತದೆ. ಇದು ಪೈಥಾನ್ ಸ್ಕ್ರಿಪ್ಟ್ ಮುಂದುವರಿಯುವ ಮೊದಲು ಮುಕ್ತಾಯದವರೆಗೆ ಕಾಯುವ ತಡೆಹಿಡಿಯುವ ಕಾರ್ಯ.

    - ಸಂಕ್ಷಿಪ್ತವಾಗಿ, ಈ ಕೋಡ್ ಸಾಲು Azure ಮೆಷಿನ್ ಲರ್ನಿಂಗ್‌ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅಳಿಸುವಿಕೆಯನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ ಮತ್ತು ಕಾರ್ಯನಿರ್ವಹಣೆಯ ಮುಗಿಯುವ ತನಕ ಕಾಯುತ್ತದೆ.

    ```python
    # ಅಜೂರ್ ಮೆಶಿನ್ ಲರ್ನಿಂಗ್‌ನಲ್ಲಿನ ಆನ್ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಅಳಿಸಿ
    # ಆನ್ಲೈನ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅಳಿಸುವಂತೆ ಪ್ರಾರಂಭಿಸಲು `workspace_ml_client` ವಸ್ತುವಿನ `online_endpoints` ಗುಣಲಕ್ಷಣದ `begin_delete` ವಿಧಾನವನ್ನು ಬಳಸಲಾಗುತ್ತದೆ
    # ಅಳಿಸಲು ಎಂಡ್ಪಾಯಿಂಟ್‌ನ ಹೆಸರನ್ನು ಸೂಚಿಸುವ `name` ದಾರ್ವಿಕವು `online_endpoint_name` ಚರದಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾಗಿದೆ
    # ಅಳಿಸುವ ಕಾರ್ಯ ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ ಕಾಯಲು `wait` ವಿಧಾನವನ್ನು ಕರೆಸಲಾಗುತ್ತದೆ. ಇದು ತಡೆಯುವ ಕಾರ್ಯವಾಗಿದ್ದು, ಅಳಿಸುವಿಕೆ ಮುಗಿಯುವವರೆಗೆ ಸ್ಕ್ರಿಪ್ಟ್ ಮುಂದುವರಿಯುವುದನ್ನು ತಡೆಹಿಡಿಯುತ್ತದೆ
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತ್ಯಾಗಪತ್ರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಸತ್ಯಸಂಧತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದೆಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ದಸ್ತಾವೇಜಿನ ಸ್ವದೇಶಿ ಭಾಷೆಯೇ ನಿಖರಮಟ್ಟದ ಪ್ರಾಮಾಣಿಕ ಸಂಪನ್ಮೂಲ ಎಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವಪೂರ್ಣ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದ ಬಳಕೆದಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಗಳಿ ಅಥವಾ ತಪ್ಪುಮತಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರರಾಗಿರುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->