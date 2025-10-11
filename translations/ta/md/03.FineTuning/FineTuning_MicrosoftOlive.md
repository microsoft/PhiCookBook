<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-10-11T11:43:55+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "ta"
}
-->
# **Phi-3 ஐ Microsoft Olive மூலம் Fine-tuning செய்யுதல்**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) என்பது hardware-aware மாடல் மேம்பாட்டு கருவியாகும், இது மாடல் சுருக்கம், மேம்பாடு மற்றும் தொகுப்பு ஆகியவற்றில் முன்னணி தொழில்நுட்பங்களை ஒருங்கிணைத்து வழங்குகிறது.

இது இயந்திரக் கற்றல் மாடல்களை மேம்படுத்தும் செயல்முறையை எளிமையாக்குவதற்காக வடிவமைக்கப்பட்டுள்ளது, குறிப்பிட்ட hardware கட்டமைப்புகளை மிகச் சிறப்பாகப் பயன்படுத்துவதற்கான உத்திகளை உறுதிப்படுத்துகிறது.

நீங்கள் cloud-based பயன்பாடுகளில் அல்லது edge சாதனங்களில் வேலை செய்கிறீர்களா என்பதைப் பொருட்படுத்தாமல், Olive உங்கள் மாடல்களை எளிதாகவும் திறமையாகவும் மேம்படுத்த உதவுகிறது.

## முக்கிய அம்சங்கள்:
- Olive, தேவையான hardware இலக்குகளைப் பொருத்தி மேம்பாட்டு உத்திகளை ஒருங்கிணைத்து தானியக்கமாக்குகிறது.
- ஒவ்வொரு சூழலுக்கும் ஒரே மேம்பாட்டு உத்தி பொருந்தாது, எனவே Olive தொழில்நுட்ப வல்லுநர்கள் தங்கள் மேம்பாட்டு புதுமைகளை இணைக்க அனுமதிக்கிறது.

## பொறியியல் முயற்சியை குறைத்தல்:
- டெவலப்பர்கள், பயிற்சி செய்யப்பட்ட மாடல்களை deploy செய்யத் தயாரிக்கவும் மேம்படுத்தவும் பல hardware vendor-specific toolchains கற்றுக்கொண்டு பயன்படுத்த வேண்டும்.
- Olive இந்த அனுபவத்தை எளிமையாக்கி, தேவையான hardware க்கான மேம்பாட்டு உத்திகளை தானியக்கமாக்குகிறது.

## தயாராக பயன்படுத்தக்கூடிய E2E மேம்பாட்டு தீர்வு:

ஒருங்கிணைந்த உத்திகளை அமைத்து fine-tune செய்வதன் மூலம், Olive end-to-end மேம்பாட்டிற்கான ஒருங்கிணைந்த தீர்வை வழங்குகிறது.
இது மாடல்களை மேம்படுத்தும் போது துல்லியத்தையும் latency யையும் போன்ற கட்டுப்பாடுகளை கருத்தில் கொள்கிறது.

## Microsoft Olive ஐ பயன்படுத்தி fine-tuning

Microsoft Olive என்பது பயன்படுத்த எளிதான திறந்த மூல மாடல் மேம்பாட்டு கருவியாகும், இது உருவாக்கும் செயற்கை நுண்ணறிவு துறையில் fine-tuning மற்றும் reference ஆகியவற்றை உள்ளடக்குகிறது. இது எளிய configuration மட்டுமே தேவைப்படுகிறது, திறந்த மூல சிறிய மொழி மாடல்கள் மற்றும் தொடர்புடைய runtime சூழல்களை (AzureML / local GPU, CPU, DirectML) இணைத்து, மாடலின் fine-tuning அல்லது reference ஐ தானியக்கமாக மேம்படுத்த முடியும், மற்றும் cloud அல்லது edge சாதனங்களில் deploy செய்ய சிறந்த மாடலை கண்டறிய முடியும். நிறுவனங்கள் தங்கள் சொந்த தொழில்துறை vertical மாடல்களை on-premises மற்றும் cloud இல் உருவாக்க அனுமதிக்கிறது.

![intro](../../../../imgs/03/ft/intro.png)

## Microsoft Olive மூலம் Phi-3 Fine Tuning 

![FinetuningwithOlive](../../../../imgs/03/ft/olivefinetune.png)

## Phi-3 Olive மாதிரி குறியீடு மற்றும் உதாரணம்
இந்த உதாரணத்தில் நீங்கள் Olive ஐ பயன்படுத்தி:

- Sad, Joy, Fear, Surprise ஆகியவற்றில் phrases ஐ வகைப்படுத்த LoRA adapter ஐ fine-tune செய்யுங்கள்.
- adapter weights ஐ base model இல் இணைக்கவும்.
- மாடலை int4 ஆக optimize மற்றும் quantize செய்யுங்கள்.

[Sample Code](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive ஐ அமைத்தல்

Microsoft Olive ஐ நிறுவுவது மிகவும் எளிது, மேலும் CPU, GPU, DirectML மற்றும் Azure ML க்காகவும் நிறுவலாம்.

```bash
pip install olive-ai
```

நீங்கள் ONNX மாடலை CPU மூலம் இயக்க விரும்பினால், நீங்கள் பயன்படுத்தலாம்

```bash
pip install olive-ai[cpu]
```

நீங்கள் ONNX மாடலை GPU மூலம் இயக்க விரும்பினால், நீங்கள் பயன்படுத்தலாம்

```python
pip install olive-ai[gpu]
```

Azure ML ஐ பயன்படுத்த விரும்பினால், நீங்கள் பயன்படுத்தலாம்

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**குறிப்பு**
OS தேவை: Ubuntu 20.04 / 22.04 

### **Microsoft Olive இன் Config.json**

நிறுவலுக்குப் பிறகு, Config கோப்பின் மூலம் மாடல்-சிறப்பு அமைப்புகளை data, computing, training, deployment மற்றும் model generation உட்பட configure செய்யலாம்.

**1. தரவுகள்**

Microsoft Olive இல், உள்ளூர் தரவுகள் மற்றும் cloud தரவுகளில் பயிற்சி செய்ய முடியும், மேலும் அமைப்புகளில் configure செய்யலாம்.

*உள்ளூர் தரவுகள் அமைப்புகள்*

Fine-tuning க்காக பயிற்சி செய்ய வேண்டிய தரவுத்தொகுப்பை எளிதாக அமைக்கலாம், இது பொதுவாக json வடிவத்தில் இருக்கும், மற்றும் data template உடன் பொருந்தும். இது மாடலின் தேவைகளின் அடிப்படையில் சரிசெய்யப்பட வேண்டும் (உதாரணமாக, Microsoft Phi-3-mini க்கு தேவையான வடிவமைப்புடன் பொருந்த வேண்டும். உங்களிடம் பிற மாடல்கள் இருந்தால், பிற மாடல்களின் fine-tuning வடிவமைப்புகளின் தேவைகளைப் பார்க்கவும்)

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

**Cloud தரவுத் மூல அமைப்புகள்**

Azure AI Studio/Azure Machine Learning Service இன் datastore ஐ இணைத்து cloud இல் உள்ள தரவுகளை இணைப்பதன் மூலம், Microsoft Fabric மற்றும் Azure Data மூலம் Azure AI Studio/Azure Machine Learning Service க்கு வெவ்வேறு தரவுத் மூலங்களை fine-tuning க்கு ஆதரவாக அறிமுகப்படுத்த முடியும்.

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

**2. கணினி அமைப்பு**

உங்களுக்கு உள்ளூர் தேவைப்பட்டால், நீங்கள் நேரடியாக உள்ளூர் தரவுப் வளங்களைப் பயன்படுத்தலாம். Azure AI Studio / Azure Machine Learning Service இன் வளங்களைப் பயன்படுத்த வேண்டும். தொடர்புடைய Azure அளவுருக்கள், கணினி சக்தி பெயர் போன்றவற்றை configure செய்ய வேண்டும்.

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

***குறிப்பு***

Azure AI Studio/Azure Machine Learning Service இல் container மூலம் இயக்கப்படும் காரணமாக, தேவையான சூழலை configure செய்ய வேண்டும். இது conda.yaml சூழலில் configure செய்யப்படுகிறது.

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

**3. உங்கள் SLM ஐ தேர்ந்தெடுக்கவும்**

நீங்கள் Hugging face இல் இருந்து மாடலை நேரடியாகப் பயன்படுத்தலாம், அல்லது Azure AI Studio / Azure Machine Learning இன் Model Catalog உடன் இணைத்து பயன்படுத்த வேண்டிய மாடலைத் தேர்ந்தெடுக்கலாம். கீழே உள்ள குறியீடு உதாரணத்தில் Microsoft Phi-3-mini ஐ எடுத்துக்காட்டாகப் பயன்படுத்துவோம்.

உங்களிடம் மாடல் உள்ளூரில் இருந்தால், இந்த முறையைப் பயன்படுத்தலாம்

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

Azure AI Studio / Azure Machine Learning Service இல் இருந்து மாடலைப் பயன்படுத்த விரும்பினால், இந்த முறையைப் பயன்படுத்தலாம்

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

**குறிப்பு:**
Azure AI Studio / Azure Machine Learning Service உடன் ஒருங்கிணைக்க வேண்டும், எனவே மாடலை அமைக்கும் போது பதிப்பு எண் மற்றும் தொடர்புடைய பெயரிடலைப் பார்க்கவும்.

Azure இல் உள்ள அனைத்து மாடல்களும் PyTorch.MLflow ஆக அமைக்கப்பட வேண்டும்.

Hugging face கணக்கை வைத்திருக்க வேண்டும் மற்றும் Azure AI Studio / Azure Machine Learning இன் Key value க்கு key ஐ இணைக்க வேண்டும்.

**4. Algorithm**

Microsoft Olive, Lora மற்றும் QLora fine-tuning algorithm களை மிகவும் சிறப்பாக encapsulate செய்கிறது. உங்களுக்கு தேவையானவை சில தொடர்புடைய அளவுருக்களை configure செய்வது மட்டுமே. இங்கு நான் QLora ஐ எடுத்துக்காட்டாக எடுத்துக்கொள்கிறேன்.

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

Quantization conversion செய்ய விரும்பினால், Microsoft Olive முக்கிய கிளை ஏற்கனவே onnxruntime-genai முறையை ஆதரிக்கிறது. உங்கள் தேவைகளுக்கு ஏற்ப அமைக்கலாம்:

1. adapter weights ஐ base model இல் இணைக்கவும்
2. ModelBuilder மூலம் தேவையான துல்லியத்துடன் மாடலை onnx மாடலாக மாற்றவும்

உதாரணமாக quantized INT4 ஆக மாற்றுதல்

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

**குறிப்பு** 
- நீங்கள் QLoRA ஐ பயன்படுத்தினால், ONNXRuntime-genai இன் quantization conversion தற்போது ஆதரிக்கப்படவில்லை.

- இங்கு குறிப்பிடப்பட வேண்டியது, உங்கள் தேவைகளுக்கு ஏற்ப மேலே உள்ள படிகளை அமைக்கலாம். மேலே உள்ள படிகளை முழுமையாக configure செய்ய வேண்டிய அவசியமில்லை. உங்கள் தேவைகளுக்கு ஏற்ப, algorithm இன் படிகளை fine-tuning இல்லாமல் நேரடியாகப் பயன்படுத்தலாம். இறுதியாக நீங்கள் தொடர்புடைய engines ஐ configure செய்ய வேண்டும்.

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

**5. Fine-tuning முடிந்தது**

கட்டளைகள் வரியில், olive-config.json இன் directory இல் செயல்படுத்தவும்

```bash
olive run --config olive-config.json  
```

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.