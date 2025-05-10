<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-05-09T20:49:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "pa"
}
-->
# **Microsoft Olive ਨਾਲ Phi-3 ਨੂੰ Fine-tune ਕਰਨਾ**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) ਇੱਕ ਆਸਾਨ-ਇਸਤਮਾਲ ਹਾਰਡਵੇਅਰ-ਅਵੇਅਰ ਮਾਡਲ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਟੂਲ ਹੈ ਜੋ ਮਾਡਲ ਕੰਪ੍ਰੈਸ਼ਨ, ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਕੰਪਾਇਲੇਸ਼ਨ ਵਿੱਚ ਉਦਯੋਗ-ਪ੍ਰਮੁੱਖ ਤਕਨੀਕਾਂ ਨੂੰ ਇਕੱਠਾ ਕਰਦਾ ਹੈ।

ਇਹ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਨੂੰ ਓਪਟੀਮਾਈਜ਼ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਂਦਾ ਹੈ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਇਹ ਖਾਸ ਹਾਰਡਵੇਅਰ ਆਰਕੀਟੈਕਚਰਾਂ ਦਾ ਸਭ ਤੋਂ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕੇ ਨਾਲ ਇਸਤੇਮਾਲ ਕਰਦੇ ਹਨ।

ਚਾਹੇ ਤੁਸੀਂ ਕਲਾਉਡ-ਅਧਾਰਿਤ ਐਪਲੀਕੇਸ਼ਨਾਂ 'ਤੇ ਕੰਮ ਕਰ ਰਹੇ ਹੋ ਜਾਂ ਏਜ ਡਿਵਾਈਸز 'ਤੇ, Olive ਤੁਹਾਡੇ ਮਾਡਲਾਂ ਨੂੰ ਬਿਨਾਂ ਕਿਸੇ ਮੁਸ਼ਕਲ ਦੇ ਓਪਟੀਮਾਈਜ਼ ਕਰਨ ਦੀ ਸਹੂਲਤ ਦਿੰਦਾ ਹੈ।

## ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:
- Olive ਚਾਹੀਦੇ ਹਾਰਡਵੇਅਰ ਟਾਰਗੇਟਾਂ ਲਈ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ ਨੂੰ ਇਕੱਠਾ ਕਰਦਾ ਅਤੇ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।
- ਕੋਈ ਇੱਕ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਤਕਨੀਕ ਸਾਰੇ ਸਥਿਤੀਆਂ ਲਈ ਫਿੱਟ ਨਹੀਂ ਹੁੰਦੀ, ਇਸ ਲਈ Olive ਉਦਯੋਗ ਦੇ ਮਾਹਿਰਾਂ ਨੂੰ ਆਪਣੇ ਨਵੇਂ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਇ노ਵੇਸ਼ਨ ਜੋੜਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

## ਇੰਜੀਨੀਅਰਿੰਗ ਕੋਸ਼ਿਸ਼ ਘਟਾਓ:
- ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਅਕਸਰ ਤਿਆਰ ਮਾਡਲਾਂ ਨੂੰ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਤਿਆਰ ਕਰਨ ਅਤੇ ਓਪਟੀਮਾਈਜ਼ ਕਰਨ ਲਈ ਕਈ ਹਾਰਡਵੇਅਰ ਵੇਂਡਰ-ਖਾਸ ਟੂਲਚੇਨਾਂ ਨੂੰ ਸਿੱਖਣਾ ਅਤੇ ਵਰਤਣਾ ਪੈਂਦਾ ਹੈ।
- Olive ਇਹ ਅਨੁਭਵ ਸਧਾਰਨ ਬਣਾਉਂਦਾ ਹੈ ਕਿਉਂਕਿ ਇਹ ਚਾਹੀਦੇ ਹਾਰਡਵੇਅਰ ਲਈ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਤਕਨੀਕਾਂ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।

## ਤਿਆਰ-ਇਸਤਮਾਲ E2E ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਹੱਲ:

ਇਕੱਠੇ ਕੀਤੀਆਂ ਅਤੇ ਟਿਊਨ ਕੀਤੀਆਂ ਇੰਟੀਗ੍ਰੇਟਡ ਤਕਨੀਕਾਂ ਰਾਹੀਂ, Olive ਐਂਡ-ਟੂ-ਐਂਡ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਲਈ ਇਕ ਸੰਗਠਿਤ ਹੱਲ ਪੇਸ਼ ਕਰਦਾ ਹੈ।
ਇਹ ਮਾਡਲਾਂ ਨੂੰ ਓਪਟੀਮਾਈਜ਼ ਕਰਦਿਆਂ ਸ਼ੁੱਧਤਾ ਅਤੇ ਲੈਟੈਂਸੀ ਵਰਗੀਆਂ ਪਾਬੰਦੀਆਂ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦਾ ਹੈ।

## Microsoft Olive ਨਾਲ Fine-tuning ਕਰਨਾ

Microsoft Olive ਇੱਕ ਬਹੁਤ ਹੀ ਆਸਾਨ-ਇਸਤਮਾਲ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਮਾਡਲ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਟੂਲ ਹੈ ਜੋ ਜਨਰੇਟਿਵ ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ ਖੇਤਰ ਵਿੱਚ Fine-tuning ਅਤੇ ਰੈਫਰੈਂਸ ਦੋਹਾਂ ਨੂੰ ਕਵਰ ਕਰ ਸਕਦਾ ਹੈ। ਇਸ ਨੂੰ ਸਿਰਫ ਸਧਾਰਣ ਕਨਫਿਗਰੇਸ਼ਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਦੇ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਅਤੇ ਸੰਬੰਧਿਤ ਰਨਟਾਈਮ ਵਾਤਾਵਰਨ (AzureML / ਲੋਕਲ GPU, CPU, DirectML) ਦੇ ਨਾਲ ਜੋੜ ਕੇ, ਤੁਸੀਂ ਆਟੋਮੈਟਿਕ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਰਾਹੀਂ ਮਾਡਲ ਦਾ Fine-tuning ਜਾਂ ਰੈਫਰੈਂਸ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਸਭ ਤੋਂ ਵਧੀਆ ਮਾਡਲ ਕਲਾਉਡ ਜਾਂ ਏਜ ਡਿਵਾਈਸز 'ਤੇ ਡਿਪਲੌਇ ਕਰਨ ਲਈ ਲੱਭ ਸਕਦੇ ਹੋ। ਇਹ ਉਦਯੋਗਾਂ ਨੂੰ ਆਪਣੇ ਖੁਦ ਦੇ ਉਦਯੋਗ ਖਾਸ ਮਾਡਲ ਬਣਾ ਕੇ ਓਨ-ਪ੍ਰੈਮਿਸਿਜ ਅਤੇ ਕਲਾਉਡ 'ਤੇ ਤਿਆਰ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

![intro](../../../../translated_images/intro.dcc44a1aafcf58bf979b9a69384ffea98b5b599ac034dde94937a94a29260332.pa.png)

## Microsoft Olive ਨਾਲ Phi-3 Fine Tuning

![FinetuningwithOlive](../../../../translated_images/olivefinetune.7a9c66b3310981030c47cf637befed8fa1ea1acd0f5acec5ac090a8f3f904a45.pa.png)

## Phi-3 Olive ਨਮੂਨਾ ਕੋਡ ਅਤੇ ਉਦਾਹਰਨ
ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਤੁਸੀਂ Olive ਦੀ ਵਰਤੋਂ ਕਰਕੇ:

- ਇੱਕ LoRA ਐਡਾਪਟਰ ਨੂੰ Fine-tune ਕਰੋ ਤਾਂ ਜੋ ਫ੍ਰੇਜ਼ਾਂ ਨੂੰ Sad, Joy, Fear, Surprise ਵਿੱਚ ਵਰਗੀਕ੍ਰਿਤ ਕੀਤਾ ਜਾ ਸਕੇ।
- ਐਡਾਪਟਰ ਵਜ਼ਨਜ਼ ਨੂੰ ਬੇਸ ਮਾਡਲ ਵਿੱਚ ਮਰਜ ਕਰੋ।
- ਮਾਡਲ ਨੂੰ Optimize ਅਤੇ Quantize ਕਰਕੇ int4 ਵਿੱਚ ਬਦਲੋ।

[Sample Code](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive ਸੈਟਅੱਪ ਕਰੋ

Microsoft Olive ਦੀ ਇੰਸਟਾਲੇਸ਼ਨ ਬਹੁਤ ਸਧਾਰਣ ਹੈ, ਅਤੇ ਇਹ CPU, GPU, DirectML ਅਤੇ Azure ML ਲਈ ਵੀ ਇੰਸਟਾਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

```bash
pip install olive-ai
```

ਜੇ ਤੁਸੀਂ CPU ਨਾਲ ONNX ਮਾਡਲ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਤੁਸੀਂ ਇਸਦਾ ਇਸਤੇਮਾਲ ਕਰ ਸਕਦੇ ਹੋ

```bash
pip install olive-ai[cpu]
```

ਜੇ ਤੁਸੀਂ GPU ਨਾਲ ONNX ਮਾਡਲ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਤੁਸੀਂ ਇਸਦਾ ਇਸਤੇਮਾਲ ਕਰ ਸਕਦੇ ਹੋ

```python
pip install olive-ai[gpu]
```

ਜੇ ਤੁਸੀਂ Azure ML ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਇਸਦਾ ਇਸਤੇਮਾਲ ਕਰੋ

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Notice**
OS ਦੀ ਲੋੜ: Ubuntu 20.04 / 22.04

### **Microsoft Olive ਦਾ Config.json**

ਇੰਸਟਾਲੇਸ਼ਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ Config ਫਾਈਲ ਰਾਹੀਂ ਵੱਖ-ਵੱਖ ਮਾਡਲ-ਖਾਸ ਸੈਟਿੰਗਜ਼ ਕਨਫਿਗਰ ਕਰ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ ਡਾਟਾ, ਕਮਪਿਊਟਿੰਗ, ਟ੍ਰੇਨਿੰਗ, ਡਿਪਲੌਇਮੈਂਟ ਅਤੇ ਮਾਡਲ ਜਨਰੇਸ਼ਨ।

**1. ਡਾਟਾ**

Microsoft Olive 'ਤੇ, ਟ੍ਰੇਨਿੰਗ ਲਈ ਲੋਕਲ ਡਾਟਾ ਅਤੇ ਕਲਾਉਡ ਡਾਟਾ ਦੋਹਾਂ ਦਾ ਸਹਿਯੋਗ ਹੈ, ਅਤੇ ਇਹ ਸੈਟਿੰਗਜ਼ ਵਿੱਚ ਕਨਫਿਗਰ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

*ਲੋਕਲ ਡਾਟਾ ਸੈਟਿੰਗਜ਼*

ਤੁਸੀਂ ਸਿਰਫ਼ ਉਸ ਡਾਟਾਸੈਟ ਨੂੰ ਸੈਟ ਕਰ ਸਕਦੇ ਹੋ ਜਿਸ 'ਤੇ Fine-tuning ਲਈ ਟ੍ਰੇਨਿੰਗ ਕਰਨੀ ਹੈ, ਆਮ ਤੌਰ 'ਤੇ ਇਹ json ਫਾਰਮੈਟ ਵਿੱਚ ਹੁੰਦਾ ਹੈ, ਅਤੇ ਡਾਟਾ ਟੈਂਪਲੇਟ ਨਾਲ ਅਨੁਕੂਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ ਮਾਡਲ ਦੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ ਸੈਟ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ (ਜਿਵੇਂ ਕਿ Microsoft Phi-3-mini ਲਈ ਜਰੂਰੀ ਫਾਰਮੈਟ ਵਿੱਚ ਅਨੁਕੂਲ ਕਰਨਾ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਹੋਰ ਮਾਡਲ ਹਨ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਹੋਰ ਮਾਡਲਾਂ ਦੀਆਂ ਜਰੂਰੀ Fine-tuning ਫਾਰਮੈਟਾਂ ਦੀ ਜਾਂਚ ਕਰੋ)

```json

    "data_configs": [
        {
            "name": "dataset_default_train",
            "type": "HuggingfaceContainer",
            "load_dataset_config": {
                "params": {
                    "data_name": "json", 
                    "data_files":"dataset/dataset-classification.json",
                    "split": "train"
                }
            },
            "pre_process_data_config": {
                "params": {
                    "dataset_type": "corpus",
                    "text_cols": [
                            "phrase",
                            "tone"
                    ],
                    "text_template": "### Text: {phrase}\n### The tone is:\n{tone}",
                    "corpus_strategy": "join",
                    "source_max_len": 2048,
                    "pad_to_max_len": false,
                    "use_attention_mask": false
                }
            }
        }
    ],
```

**ਕਲਾਉਡ ਡਾਟਾ ਸੋਰਸ ਸੈਟਿੰਗਜ਼**

Azure AI Studio/Azure Machine Learning Service ਦੇ ਡਾਟਾਸਟੋਰ ਨੂੰ ਲਿੰਕ ਕਰਕੇ ਕਲਾਉਡ ਵਿੱਚ ਮੌਜੂਦ ਡਾਟਾ ਨਾਲ ਜੁੜਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਤੁਸੀਂ Microsoft Fabric ਅਤੇ Azure Data ਰਾਹੀਂ ਵੱਖ-ਵੱਖ ਡਾਟਾ ਸਰੋਤਾਂ ਨੂੰ Azure AI Studio/Azure Machine Learning Service ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਕੇ Fine-tuning ਲਈ ਸਹਾਇਤਾ ਦੇ ਸਕਦੇ ਹੋ।

```json

    "data_configs": [
        {
            "name": "dataset_default_train",
            "type": "HuggingfaceContainer",
            "load_dataset_config": {
                "params": {
                    "data_name": "json", 
                    "data_files": {
                        "type": "azureml_datastore",
                        "config": {
                            "azureml_client": {
                                "subscription_id": "Your Azure Subscrition ID",
                                "resource_group": "Your Azure Resource Group",
                                "workspace_name": "Your Azure ML Workspaces name"
                            },
                            "datastore_name": "workspaceblobstore",
                            "relative_path": "Your train_data.json Azure ML Location"
                        }
                    },
                    "split": "train"
                }
            },
            "pre_process_data_config": {
                "params": {
                    "dataset_type": "corpus",
                    "text_cols": [
                            "Question",
                            "Best Answer"
                    ],
                    "text_template": "<|user|>\n{Question}<|end|>\n<|assistant|>\n{Best Answer}\n<|end|>",
                    "corpus_strategy": "join",
                    "source_max_len": 2048,
                    "pad_to_max_len": false,
                    "use_attention_mask": false
                }
            }
        }
    ],
    
```

**2. ਕਮਪਿਊਟਿੰਗ ਕਨਫਿਗਰੇਸ਼ਨ**

ਜੇ ਤੁਸੀਂ ਲੋਕਲ ਵਰਕਲੋਡ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਸਿੱਧਾ ਲੋਕਲ ਡਾਟਾ ਸਰੋਤਾਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਜੇ Azure AI Studio / Azure Machine Learning Service ਦੇ ਸਰੋਤ ਵਰਤਣੇ ਹਨ, ਤਾਂ ਤੁਹਾਨੂੰ Azure ਦੇ ਸੰਬੰਧਿਤ ਪੈਰਾਮੀਟਰ, ਕਮਪਿਊਟਿੰਗ ਪਾਵਰ ਦਾ ਨਾਮ ਆਦਿ ਕਨਫਿਗਰ ਕਰਨੇ ਪੈਣਗੇ।

```json

    "systems": {
        "aml": {
            "type": "AzureML",
            "config": {
                "accelerators": ["gpu"],
                "hf_token": true,
                "aml_compute": "Your Azure AI Studio / Azure Machine Learning Service Compute Name",
                "aml_docker_config": {
                    "base_image": "Your Azure AI Studio / Azure Machine Learning Service docker",
                    "conda_file_path": "conda.yaml"
                }
            }
        },
        "azure_arc": {
            "type": "AzureML",
            "config": {
                "accelerators": ["gpu"],
                "aml_compute": "Your Azure AI Studio / Azure Machine Learning Service Compute Name",
                "aml_docker_config": {
                    "base_image": "Your Azure AI Studio / Azure Machine Learning Service docker",
                    "conda_file_path": "conda.yaml"
                }
            }
        }
    },
```

***Notice***

ਕਿਉਂਕਿ ਇਹ Azure AI Studio/Azure Machine Learning Service 'ਤੇ ਕੰਟੇਨਰ ਰਾਹੀਂ ਚਲਾਇਆ ਜਾਂਦਾ ਹੈ, ਇਸ ਲਈ ਲੋੜੀਂਦਾ ਵਾਤਾਵਰਨ conda.yaml ਵਿੱਚ ਕਨਫਿਗਰ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

```yaml

name: project_environment
channels:
  - defaults
dependencies:
  - python=3.8.13
  - pip=22.3.1
  - pip:
      - einops
      - accelerate
      - azure-keyvault-secrets
      - azure-identity
      - bitsandbytes
      - datasets
      - huggingface_hub
      - peft
      - scipy
      - sentencepiece
      - torch>=2.2.0
      - transformers
      - git+https://github.com/microsoft/Olive@jiapli/mlflow_loading_fix#egg=olive-ai[gpu]
      - --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/ 
      - ort-nightly-gpu==1.18.0.dev20240307004
      - --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-genai/pypi/simple/
      - onnxruntime-genai-cuda

    

```

**3. ਆਪਣਾ SLM ਚੁਣੋ**

ਤੁਸੀਂ Hugging Face ਤੋਂ ਸਿੱਧਾ ਮਾਡਲ ਵਰਤ ਸਕਦੇ ਹੋ, ਜਾਂ Azure AI Studio / Azure Machine Learning ਦੇ Model Catalog ਨਾਲ ਜੋੜ ਕੇ ਮਾਡਲ ਚੁਣ ਸਕਦੇ ਹੋ। ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ ਅਸੀਂ Microsoft Phi-3-mini ਨੂੰ ਉਦਾਹਰਨ ਵਜੋਂ ਵਰਤਾਂਗੇ।

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਮਾਡਲ ਲੋਕਲ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਤਰੀਕਾ ਵਰਤ ਸਕਦੇ ਹੋ

```json

    "input_model":{
        "type": "PyTorchModel",
        "config": {
            "hf_config": {
                "model_name": "model-cache/microsoft/phi-3-mini",
                "task": "text-generation",
                "model_loading_args": {
                    "trust_remote_code": true
                }
            }
        }
    },
```

ਜੇ ਤੁਸੀਂ Azure AI Studio / Azure Machine Learning Service ਤੋਂ ਮਾਡਲ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਤਰੀਕਾ ਵਰਤ ਸਕਦੇ ਹੋ

```json

    "input_model":{
        "type": "PyTorchModel",
        "config": {
            "model_path": {
                "type": "azureml_registry_model",
                "config": {
                    "name": "microsoft/Phi-3-mini-4k-instruct",
                    "registry_name": "azureml-msr",
                    "version": "11"
                }
            },
             "model_file_format": "PyTorch.MLflow",
             "hf_config": {
                "model_name": "microsoft/Phi-3-mini-4k-instruct",
                "task": "text-generation",
                "from_pretrained_args": {
                    "trust_remote_code": true
                }
            }
        }
    },
```

**Notice:**
ਸਾਨੂੰ Azure AI Studio / Azure Machine Learning Service ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨਾ ਪੈਂਦਾ ਹੈ, ਇਸ ਲਈ ਮਾਡਲ ਸੈਟਅੱਪ ਕਰਦਿਆਂ ਵਰਜਨ ਨੰਬਰ ਅਤੇ ਸੰਬੰਧਿਤ ਨਾਂਵਾਂ ਦਾ ਧਿਆਨ ਰੱਖੋ।

Azure ਦੇ ਸਾਰੇ ਮਾਡਲਾਂ ਨੂੰ PyTorch.MLflow 'ਤੇ ਸੈੱਟ ਕਰਨਾ ਜਰੂਰੀ ਹੈ।

ਤੁਹਾਡੇ ਕੋਲ Hugging Face ਖਾਤਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਇਸਦੀ ਕੁੰਜੀ Azure AI Studio / Azure Machine Learning ਦੇ Key value ਨਾਲ ਬਾਈਂਡ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।

**4. Algorithm**

Microsoft Olive ਨੇ Lora ਅਤੇ QLora Fine-tuning ਅਲਗੋਰਿਦਮਾਂ ਨੂੰ ਬਹੁਤ ਵਧੀਆ ਤਰੀਕੇ ਨਾਲ ਕੈਪਸੂਲ ਕੀਤਾ ਹੈ। ਤੁਹਾਨੂੰ ਸਿਰਫ ਕੁਝ ਸੰਬੰਧਿਤ ਪੈਰਾਮੀਟਰ ਕਨਫਿਗਰ ਕਰਨੇ ਹੁੰਦੇ ਹਨ। ਇੱਥੇ ਮੈਂ QLora ਦਾ ਉਦਾਹਰਨ ਲੈ ਰਿਹਾ ਹਾਂ।

```json
        "lora": {
            "type": "LoRA",
            "config": {
                "target_modules": [
                    "o_proj",
                    "qkv_proj"
                ],
                "double_quant": true,
                "lora_r": 64,
                "lora_alpha": 64,
                "lora_dropout": 0.1,
                "train_data_config": "dataset_default_train",
                "eval_dataset_size": 0.3,
                "training_args": {
                    "seed": 0,
                    "data_seed": 42,
                    "per_device_train_batch_size": 1,
                    "per_device_eval_batch_size": 1,
                    "gradient_accumulation_steps": 4,
                    "gradient_checkpointing": false,
                    "learning_rate": 0.0001,
                    "num_train_epochs": 3,
                    "max_steps": 10,
                    "logging_steps": 10,
                    "evaluation_strategy": "steps",
                    "eval_steps": 187,
                    "group_by_length": true,
                    "adam_beta2": 0.999,
                    "max_grad_norm": 0.3
                }
            }
        },
```

ਜੇ ਤੁਸੀਂ quantization conversion ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ Microsoft Olive ਦਾ ਮੁੱਖ ਬ੍ਰਾਂਚ ਪਹਿਲਾਂ ਹੀ onnxruntime-genai ਮੈਥਡ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ। ਤੁਸੀਂ ਆਪਣੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ ਇਸਨੂੰ ਸੈਟ ਕਰ ਸਕਦੇ ਹੋ:

1. ਐਡਾਪਟਰ ਵਜ਼ਨਜ਼ ਨੂੰ ਬੇਸ ਮਾਡਲ ਵਿੱਚ ਮਰਜ ਕਰੋ  
2. ModelBuilder ਰਾਹੀਂ ਮਾਡਲ ਨੂੰ ਲੋੜੀਂਦੇ ਪ੍ਰਿਸੀਜ਼ਨ ਨਾਲ onnx ਮਾਡਲ ਵਿੱਚ ਬਦਲੋ

ਜਿਵੇਂ ਕਿ quantized INT4 ਵਿੱਚ ਬਦਲਣਾ

```json

        "merge_adapter_weights": {
            "type": "MergeAdapterWeights"
        },
        "builder": {
            "type": "ModelBuilder",
            "config": {
                "precision": "int4"
            }
        }
```

**Notice**  
- ਜੇ ਤੁਸੀਂ QLoRA ਵਰਤਦੇ ਹੋ, ਤਾਂ ONNXRuntime-genai ਦੀ quantization conversion ਇਸ ਸਮੇਂ ਸਹਿਯੋਗਿਤ ਨਹੀਂ ਹੈ।  
- ਇੱਥੇ ਇਹ ਗੱਲ ਦੱਸਣ ਯੋਗ ਹੈ ਕਿ ਤੁਸੀਂ ਉਪਰ ਦਿੱਤੇ ਕਦਮਾਂ ਨੂੰ ਆਪਣੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ ਸੈਟ ਕਰ ਸਕਦੇ ਹੋ। ਸਾਰਿਆਂ ਕਦਮਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਕਨਫਿਗਰ ਕਰਨਾ ਜਰੂਰੀ ਨਹੀਂ। ਤੁਹਾਡੇ ਲੋੜ ਅਨੁਸਾਰ ਤੁਸੀਂ ਸਿੱਧਾ algorithm ਦੇ ਕਦਮ ਵਰਤ ਸਕਦੇ ਹੋ ਬਿਨਾਂ Fine-tuning ਦੇ। ਆਖ਼ਿਰ ਵਿੱਚ ਤੁਹਾਨੂੰ ਸੰਬੰਧਿਤ ਇੰਜਣਾਂ ਨੂੰ ਕਨਫਿਗਰ ਕਰਨਾ ਪਵੇਗਾ।

```json

    "engine": {
        "log_severity_level": 0,
        "host": "aml",
        "target": "aml",
        "search_strategy": false,
        "execution_providers": ["CUDAExecutionProvider"],
        "cache_dir": "../model-cache/models/phi3-finetuned/cache",
        "output_dir" : "../model-cache/models/phi3-finetuned"
    }
```

**5. Fine-tuning ਮੁਕੰਮਲ**

ਕਮਾਂਡ ਲਾਈਨ 'ਤੇ, olive-config.json ਵਾਲੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇਹ ਕਮਾਂਡ ਚਲਾਓ

```bash
olive run --config olive-config.json  
```

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਵਜੋਂ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।