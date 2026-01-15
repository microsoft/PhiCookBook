<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-12-21T18:27:19+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "ml"
}
-->
# **Microsoft Olive ഉപയോഗിച്ച് Phi-3 ഫൈൻട്യൂണിംഗ്**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) ഒരു ഉപയോഗിക്കാൻ എളുപ്പമുള്ള hardware-aware മോഡൽ ഒപ്റ്റിമൈസേഷൻ ടൂൾ ആണ്, മോഡൽ കമ്പ്രഷൻ, ഒപ്റ്റിമൈസേഷൻ, കോംപൈലേഷൻ എന്നിവയിൽ വ്യവസായനേതൃത്വമുള്ള സാങ്കേതിക വിദ്യകൾ കൂട്ടിച്ചേർക്കുന്നു.

ഇത് മെഷീൻ ലേണിംഗ് മോഡലുകൾ ഒപ്റ്റിമൈസുചെയ്യുന്നതിനുള്ള പ്രക്രിയ ലളിതമാക്കി, പ്രത്യേക ഹാർഡ്‌വെയർ ആർക്കിടെക്ചറുകൾക്കുള്ള കാര്യക്ഷമ ഉപയോഗം ഉറപ്പാക്കാൻ രൂപകൽപ്പന ചെയ്തതാണ്.

നിങ്ങൾ ക്ലൌഡ് ആധാരിത എപ്ലിക്കേഷനുകളിലോ എഡ്ജ് ഡിവൈസുകളിലോ പ്രവർത്തിച്ചാലും, Olive നിങ്ങളുടെ മോഡലുകൾ പ്രയാസമില്ലാതെ ഫലപ്രദമായി ഒപ്റ്റിമൈസ് ചെയ്യാൻ സഹായിക്കുന്നു.

## പ്രധാന സവിശേഷതകൾ:
- Olive ആവശ്യമായ ഹാർഡ്‌വെയർ ടാർഗറ്റുകൾക്കുള്ള ഒപ്റ്റിമൈസേഷൻ സാങ്കേതിക വിദ്യകൾ ഏകീകരിക്കുകയും സ്വയംക്രമീകരിക്കുകയും ചെയ്യുന്നു.
- ഒരൊറ്റ ഒപ്റ്റിമൈസേഷൻ സാങ്കേതികം എല്ലാ സാഹചര്യങ്ങൾക്കും അനുയോജ്യമാകില്ല, അതിനാൽ Olive വ്യവസായ വിദഗ്ധർ അവരുടെ ഒപ്റ്റിമൈസേഷൻ новേഷനുകൾ പ്ലഗ് ഇൻ ചെയ്യാൻ അനുവദിച്ച് വിപുലീകരണശേഷി നൽകുന്നു.

## എഞ്ചിനീയറിങ് പരിശ്രമം കുറയ്ക്കുക:
- ഡെവലപ്പർമാർക്ക് ചിലപ്പോൾ വിവിധ ഹാർഡ്‌വെയർ വൻദാതാവിന്റെ ടൂൾചെയിനുകൾ പഠിച്ച് ഉപയോഗിക്കേണ്ടത് ആവശ്യമാകും പരിശീലിപ്പിച്ച മോഡലുകൾ ഡിപ്ലോയ് ചെയ്യാൻ തയ്യാറാക്കുന്നതിനും ഒപ്റ്റിമൈസ് ചെയ്യുന്നതിനും.
- Olive ആവശ്യമായ ഹാർഡ്‌വെയറിന് അനുസൃതമായി ഒപ്റ്റിമൈസേഷൻ സാങ്കേതികവിദ്യകൾ സ്വയംക്രമീകരിച്ച് ഈ അനുഭവം ലളിതമാക്കുന്നു.

## ഉപയോഗിക്കാൻ സജ്ജമായ E2E ഒപ്റ്റിമൈസേഷൻ പരിഹാരം:

സംയോജിപ്പിച്ച സാങ്കേതികതകൾ സംയോജിച്ച് ട്യൂൺ ചെയ്യുന്നതിലൂടെ Olive end-to-end ഒപ്റ്റിമൈസേഷനു ഏകീകൃത പരിഹാരം നൽകുന്നു.
അതിന്റെ സമയം നിശ്ചിതമായ കാര്യക്ഷമത, latency പോലുള്ള നിയന്ത്രണങ്ങൾ പരിഗണിച്ച് മോഡലുകൾ ഒപ്റ്റിമൈസ് ചെയ്യുന്നു.

## Microsoft Olive ഉപയോഗിച്ച് ഫൈൻട്യൂണിംഗ്

Microsoft Olive വളരെ ഉപയോഗത്തിൽ എളുപ്പമുള്ള open source മോഡൽ ഒപ്റ്റിമൈസേഷൻ ടൂൾ ആണ്, ഇത് ജനറേറ്റീവ് ആർട്ടിഫിഷ്യൽ ഇന്റലിജൻസിയുടെ മേഖലയിലെ ഫൈൻട്യൂണിംഗും റഫറൻസും ഉൾക്കൊള്ളും. ഇതിനു ക്രമീകരണം മാത്രമേ ആവശ്യമായുള്ളൂ, ഓപ്പൺ സോഴ്‌സ് ചെറിയ ഭാഷാ മോഡലുകളും ബന്ധപ്പെട്ട റൺടൈം പരിസ്ഥിതികളും (AzureML / local GPU, CPU, DirectML) ഉപയോഗിച്ച് ചേർത്താൽ, നിങ്ങൾ സ്വയംരീതിയിലുള്ള ഒപ്റ്റിമൈസേഷനിലൂടെ മോഡൽ ഫൈൻട്യൂൺ അല്ലെങ്കിൽ റഫറൻസ് പൂർത്തിയാക്കി ക്ലൗഡിലോ എഡ്ജ് ഡിവൈസിലോ ഡിപ്ലോയ് ചെയ്യാൻ ഏറ്റവും അനുയോജ്യമായ മോഡൽ കണ്ടെത്താം. സംരംഭങ്ങൾ അവരുടെ സ്വന്തം ഇൻഡസ്ട്രി വേർച്വൽ മോഡലുകൾ ഓൺ-പ്രേമിസിസിലും ക്ലൗഡിലും നിർമ്മിക്കാൻ സാധിക്കും.

![ആമുഖം](../../../../translated_images/ml/intro.46086a3f16ec48e2.png)

## Microsoft Olive ഉപയോഗിച്ച് Phi-3 ഫൈൻട്യൂണിംഗ് 

![ഒലിവിനൊപ്പം ഫൈൻട്യൂണിംഗ്](../../../../translated_images/ml/olivefinetune.76d09e9b68253681.png)

## Phi-3 Olive സാമ്പിൾ കോഡ് and ഉദാഹരണം
ഈ ഉദാഹരണത്തിൽ നിങ്ങൾ Olive ഉപയോഗിച്ച് താഴെ ചെയ്യുക:

- LoRA അഡാപ്റ്റർ ഫൈൻട്യൂൺ ചെയ്ത് വാചകങ്ങൾ Sad, Joy, Fear, Surprise എന്നിങ്ങനെ വർഗ്ഗീകരിക്കുക.
- അഡാപ്റ്റർ വെയിറ്റുകൾ ബേസ് മോഡലിൽ മർജ് ചെയ്യുക.
- മോഡൽ int4 ആയി ഒപ്റ്റിമൈസ് ചെയ്ത് ക്വാന്റൈസ് ചെയ്യുക.

[സാമ്പിൾ കോഡ്](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive സജ്ജീകരിക്കൽ

Microsoft Olive ഇൻസ്റ്റലേഷൻ വളരെ ലളിതമാണ്, കൂടാതെ ഇത് CPU, GPU, DirectML, Azure ML എന്നിവയ്ക്ക് ഇൻസ്റ്റാൾ ചെയ്യാൻ കഴിയും

```bash
pip install olive-ai
```

If you wish to run an ONNX model with a CPU, you can use

```bash
pip install olive-ai[cpu]
```

If you want to run an ONNX model with a GPU, you can use

```python
pip install olive-ai[gpu]
```

If you want to use Azure ML, use

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**ശ്രദ്ധിക്കുക**
ഓഎസ് ആവശ്യകത : Ubuntu 20.04 / 22.04 

### **Microsoft Olive-ന്റെ Config.json**

ഇൻസ്റ്റലേഷനുശേഷം, Config ഫയലിലൂടെ ഡാറ്റ, കംപ്യൂട്ടിംഗ്, ട്രെയിനിംഗ്, ഡിപ്ലോയ്മെന്റ്, മോഡൽ ജനറേഷൻ എന്നിവ ഉൾപ്പെടെ മോഡൽ-നിയമിത വ്യത്യസ്ത ക്രമീകരണങ്ങൾ നിങ്ങൾ നിർവഹിക്കാവുന്നതാണ്.

**1. Data**

Microsoft Olive-ൽ ലോക്കൽ ഡാറ്റയും ക്ലൗഡ് ഡാറ്റയും ട്രെയിനിങ് പിന്തുണക്കപ്പെടുന്നു, ഇത് സജ്ജീകരണങ്ങളിൽ ക്രമീകരിക്കാവുന്നതാണ്.

*ലോകൽ ഡാറ്റ ക്രമീകരണങ്ങൾ*

ഫൈൻട്യൂണിംഗിനായി പരിശീലിപ്പിക്കേണ്ട ഡാറ്റാസെറ്റ് സാധാരണയായി json ഫോർമാറ്റിൽ സജ്ജീകരിച്ച് ഡാറ്റ ടെമ്പ്ലേറ്റ് അനുസരിച്ച് അഡပ်്റ്റ് ചെയ്യാം. ഇത് മോഡലിന്റെ ആവശ്യകത അനുസരിച്ച് ക്രമീകരിക്കേണ്ടതാണ് (ഉദാഹരണത്തിന് Microsoft Phi-3-mini ആവശ്യമായ ഫോർമാറ്റിലേക്ക് അഡപ്റ്റ് ചെയ്യുക. മറ്റ് മോഡലുകൾ ഉണ്ടായാൽ, അവയുടെ ഫൈൻട്യൂണിംഗ് ഫോർമാറ്റുകൾ കാണുക)

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

**ക്ലൗഡ് ഡാറ്റ സോഴ്‌സ് ക്രമീകരണങ്ങൾ**

Azure AI Studio/Azure Machine Learning Service-ന്റെ datastore-നെ ലിങ്കുചെയ്ത് ക്ലൗഡിലുള്ള ഡാറ്റക്ക് ലിങ്കുചെയ്യമൂലം, Microsoft Fabric және Azure Data എന്നിവ വഴിയിലൂടെ വ്യത്യസ്ത ഡാറ്റ സോഴ്‌സുകൾ Azure AI Studio/Azure Machine Learning Service-ൽ ഇറക്കുമതി ചെയ്യാൻ തിരഞ്ഞെടുക്കാവുന്നതാണ് ഫൈൻട്യൂണിംഗിന് പിന്തുണ നൽകുന്നതിന്.

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

**2. കംപ്യൂട്ടിംഗ് ക്രമീകരണം**

ലോക്കലായി പ്രവർത്തിക്കേണ്ട പക്ഷം, നിങ്ങൾ നേരിട്ട് ലോക്കൽ ഡാറ്റാ റിസോഴ്സുകൾ ഉപയോഗിക്കാം. Azure AI Studio / Azure Machine Learning Service റിസോഴ്സുകൾ ഉപയോഗിക്കേണ്ടതുണ്ടെങ്കിൽ, ബന്ധപ്പെട്ട Azure പാരാമീറ്ററുകൾ, കംപ്യൂട്ടിംഗ് നാമം തുടങ്ങിയവ ക്രമീകരിക്കേണ്ടതാണ്.

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

***ശ്രദ്ധിക്കുക***

Azure AI Studio/Azure Machine Learning Service-ൽ 컨TAINER മുഖേന റൺ ചെയ്യുന്നതുകൊണ്ട്, ആവശ്യമുള്ള പരിസ്ഥിതി ക്രമീകരണം നിർബന്ധമാണ്. ഇത് conda.yaml പരിസ്ഥിതിയിൽ ക്രമീകരിച്ചിരിക്കണം.



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

**3. നിങ്ങളുടെ SLM തിരഞ്ഞെടുക്കുക**

Hugging face-ൽ നിന്നോ നേരിട്ട് Azure AI Studio / Azure Machine Learning-ന്റെ Model Catalog-ഇൽ നിന്നോ മോഡൽ ഉപയോഗിക്കാവുന്നതാണ്. താഴെയുള്ള കോഡ് ഉദാഹരണത്തിൽ ഞങ്ങൾ Microsoft Phi-3-mini മോഡലിനെ ഉദാഹരണമായി ഉപയോഗിക്കുന്നു.

നിങ്ങൾക്ക് മോഡൽ ലോക്കലായി ഉണ്ടെങ്കിൽ, ഈ രീതിയാണ് ഉപയോഗിക്കേണ്ടത്

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

Azure AI Studio / Azure Machine Learning Service-ൽ നിന്നുള്ള മോഡൽ ഉപയോഗിക്കുവാൻ ആഗ്രഹിച്ചാൽ, ഈ രീതിയാണ് ഉപയോഗിക്കുക


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

**ശ്രദ്ധ:**
ഞങ്ങൾ Azure AI Studio / Azure Machine Learning Service-ഉം ഇന്റഗ്രേറ്റ് ചെയ്യേണ്ടതുണ്ട്, അതിനാൽ മോഡൽ ക്രമീകരിക്കുമ്പോൾ പതിപ്പ് നമ്പറും ബന്ധപ്പെട്ട നാമകരണം പരിഗണിക്കുക.

Azure-上的 എല്ലാ മോഡലുകളും PyTorch.MLflow ആയി സെറ്റ് ചെയ്യേണ്ടതാണ്

നിങ്ങൾക്കു ഒരു Hugging face അക്കൗണ്ട് ഉണ്ടായിരിക്കുകയും കീ Azure AI Studio / Azure Machine Learning-ന്റെ Key value-ൽ ബൈൻഡ് ചെയ്തിരിക്കുകയുമാകണം

**4. ആൽഗോരിതം**

Microsoft Olive Lora மற்றும் QLora ഫൈൻട്യൂണിംഗ് ആൽഗോറിതങ്ങളെയും നന്നായി എംബഡുചെയ്യുന്നു. നിങ്ങൾ ക്രമീകരിക്കേണ്ടത് ചില ബന്ധപ്പെട്ട പാരാമീറ്ററുകൾ മാത്രമേയുള്ളൂ. ഇവിടെ QLora ഒരു ഉദാഹരണമായി എടുത്തിട്ടുണ്ട്.

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

ക്വാന്റൈസേഷനായി മാറ്റം ചെയ്യാനാണെങ്കിൽ, Microsoft Olive മെയിൻ ബ്രാഞ്ച് ഇതിനായി onnxruntime-genai രീതിയെ ഇതിനകം പിന്തുണക്കുന്നുണ്ട്. നിങ്ങൾക്ക് ആവശ്യാനുസരണം ഇത് ക്രമീകരിക്കാം：

1. അഡാപ്റ്റർ വെയിറ്റുകൾ ബേസ് മോഡലിലേക്ക് മർജ്ജ് ചെയ്യുക
2. ModelBuilder ഉപയോഗിച്ച് ആവശ്യമായ_PRECISION_ ഉപയോഗിച്ച് മോഡൽ ONNX മോഡലാക്കി മാറ്റുക

ഉദാഹരണത്തിന് ക്വാന്റൈസ്ഡ് INT4-ലേക്ക് മാറ്റൽ പോലുള്ളത്


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

**ശ്രദ്ധ** 
- നിങ്ങൾ QLoRA ഉപയോഗിച്ചാൽ, ONNXRuntime-genai-യുടെ ക്വാന്റൈസേഷൻ പരിവർത്തനം പ്രാഥമികമായി പിന്തുണയ്ക്കാത്തതാണ്.

- ഇവിടെ പറയേണ്ടത് നിങ്ങൾ മുകളിൽ പറഞ്ഞിരിക്കുന്ന സ്റ്റെപ്പുകൾ നിങ്ങളുടെ ആവശ്യാനുസരണം ക്രമീകരിക്കാവുന്നതാണ്. മുകളിൽ പറയപ്പെട്ട എല്ലാ സ്റ്റെപ്പുകളും പൂർണ്ണമായി ക്രമീകരിക്കേണ്ടതില്ല. നിങ്ങളുടെ ആവശ്യകത അനുസരിച്ച് ഫൈൻട്യൂണിംങ് ഇല്ലാതെ നേരിട്ട് ആൽഗോരിതത്തിന്റെ ചില ഘടകങ്ങൾ ഉപയോഗിക്കാം. അന്ത്യം Relevant engines-കൾ ക്രമീകരിക്കേണ്ടതുണ്ടാകും

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

**5. ഫൈൻട്യൂണിംഗ് പൂർത്തിയാക്കൽ**

കമാൻഡ് ലൈൻയിൽ, olive-config.json ഉള്ള ഡയറക്ടറിയിൽ പ്രവർത്തിപ്പിക്കുക

```bash
olive run --config olive-config.json  
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിക്കുന്നുവെങ്കിലും, സ്വയം പ്രവർത്തിപ്പിക്കപ്പെടുന്ന വിവർത്തനങ്ങളിൽ പിശകുകളും തെറ്റുകളും ഉണ്ടായിരിക്കാൻ സാധ്യതയുണ്ടെന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൗലിക രേഖ അതിന്റെ സ്ഥാനം ഭാഷയിൽ തന്നെയാണ് അധികാരപരമായ സ്രോതസ്സായി പരിഗണിക്കേണ്ടത്. നിർണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദ്ദേശിക്കുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണയ്ക്കോ തെറ്റായ വ്യാഖ്യാനത്തിനോ ഞങ്ങൾക്ക് ഉത്തരവാദിത്തമില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->