<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-12-21T18:23:18+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "pcm"
}
-->
# **Fine-tuning Phi-3 wit Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) na easy-to-use hardware-aware model optimization tool wey dey gather top industry techniques for model compression, optimization, and compilation.

E dey designed to make the process of optimizing machine learning models straightforward, make dem use hardware architectures chop small power and perform well.

Whether you dey work on cloud-based applications or edge devices, Olive go enable you optimize your models without yawa and well.

## Wetin E Fit Do:
- Olive dey aggregate and automate optimization techniques for di hardware wey you want.
- No one optimization technique dey fit all scenarios, so Olive dey allow extensibility by making industry experts fit plug in their optimization innovations.

## Make Engineers Work Easy:
- Developers dey often need learn and use multiple hardware vendor-specific toolchains to prepare and optimize trained models for deployment.
- Olive dey simplify this experience by automating optimization techniques for the hardware wey you want.

## E2E Optimization Solution Wey Ready to Use:

By putting together and tuning integrated techniques, Olive dey offer one unified solution for end-to-end optimization.
E dey consider constraints like accuracy and latency when e dey optimize models.

## Using Microsoft Olive to fine-tune

Microsoft Olive na very easy-to-use open-source model optimization tool wey fit handle both fine-tuning and reference work for generative artificial intelligence. E only need small configuration; combine am with open-source small language models and related runtime environments (AzureML / local GPU, CPU, DirectML), you fit complete the fine-tuning or reference of the model through automatic optimization, and find the best model wey you go deploy to the cloud or on edge devices. E dey allow enterprises build their own industry vertical models on-premises and for the cloud.

![introduction](../../../../translated_images/intro.46086a3f16ec48e2.pcm.png)

## Phi-3 Fine Tuning with Microsoft Olive 

![Fine-tuning wit Olive](../../../../translated_images/olivefinetune.76d09e9b68253681.pcm.png)

## Phi-3 Olive Sample Code and Example
For this example you go use Olive to:

- Fine-tune one LoRA adapter to classify phrases into Sad, Joy, Fear, Surprise.
- Merge the adapter weights into the base model.
- Optimize and quantize the model to int4.

[Sample Code](../../code/03.Finetuning/olive-ort-example/README.md)

### Setup Microsoft Olive

Microsoft Olive installation dey very simple, and you fit also install am for CPU, GPU, DirectML, and Azure ML

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

**Notice**
OS wey e need : Ubuntu 20.04 / 22.04 

### **Microsoft Olive Config.json**

After installation, you fit configure different model-specific settings through the Config file, including data, computing, training, deployment, and model generation.

**1. Data**

For Microsoft Olive, training on local data and cloud data dey supported, and you fit configure am in the settings.

*Local data settings*

You fit simply set up the dataset wey you wan use for fine-tuning, usually for json format, and adapt am with the data template. This one need to dey adjusted based on the requirements of the model (for example, adapt am to the format wey Microsoft Phi-3-mini need. If you get other models, abeg refer to the required fine-tuning formats of those models for processing)

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

**Cloud data source settings**

By linking the datastore of Azure AI Studio/Azure Machine Learning Service to the data wey dey cloud, you fit bring different data sources into Azure AI Studio/Azure Machine Learning Service through Microsoft Fabric and Azure Data as support for fine-tuning the data.

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

**2. Computing configuration**

If you dey run locally, you fit directly use local compute resources. If you want use resources from Azure AI Studio / Azure Machine Learning Service, you go need configure the relevant Azure parameters, compute name, and so on.

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

Because e dey run through container on Azure AI Studio/Azure Machine Learning Service, the required environment need to dey configured. This one dey configured inside the conda.yaml environment.



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

**3. Choose your SLM**

You fit use the model directly from Hugging Face, or you fit combine am with the Model Catalog of Azure AI Studio / Azure Machine Learning to select the model to use. For the code example below we go use Microsoft Phi-3-mini as example.

If you get the model locally, you fit use this method

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

If you want to use a model from Azure AI Studio / Azure Machine Learning Service, you fit use this method


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
We need make am integrate with Azure AI Studio / Azure Machine Learning Service, so when you dey set up the model, abeg refer to the version number and related naming.

All models on Azure need to be set to PyTorch.MLflow

You need to get a Hugging Face account and bind the key to the Key value of Azure AI Studio / Azure Machine Learning

**4. Algorithm**

Microsoft Olive don encapsulate LoRA and QLoRA fine-tuning algorithms well well. All wey you need configure na some relevant parameters. Here I go use QLoRA as example.

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

If you want quantization conversion, Microsoft Olive main branch don already support the onnxruntime-genai method. You fit set am according to your needs：

1. merge adapter weights into base model
2. Convert the model to onnx model with required precision by ModelBuilder

for example convert to quantized INT4


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
- If you use QLoRA, the quantization conversion of ONNXRuntime-genai no dey supported for now.

- Make I point out say you fit arrange the above steps according to your own needs. E no necessary to configure all the steps complete. Depending on wetin you need, you fit directly use the algorithm steps without fine-tuning. Finally you go need configure the relevant engines

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

**5. Finished fine-tuning**

For command line, run am inside the directory wey get olive-config.json

```bash
olive run --config olive-config.json  
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Abeg note:
Dis document don translate wit AI translation service (Co-op Translator: https://github.com/Azure/co-op-translator). Even though we dey try make am correct, make you sabi say automated translations fit get errors or mistakes. Di original document for im native language suppose be di correct/authoritative source. If na important information, better make person use professional human translator. We no dey responsible for any misunderstanding or wrong interpretation wey fit waka come from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->