<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:49:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "tl"
}
-->
# **Fine-tuning ng Phi-3 gamit ang Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) ay isang madaling gamitin na hardware-aware na tool para sa pag-optimize ng modelo na pinagsasama ang mga nangungunang teknik sa industriya para sa model compression, optimization, at compilation.

Ito ay idinisenyo upang gawing mas madali ang proseso ng pag-optimize ng mga machine learning model, na tinitiyak na nagagamit nila nang pinakamainam ang partikular na hardware architectures.

Kahit na nagtatrabaho ka sa cloud-based na mga aplikasyon o mga edge device, pinapadali ng Olive ang pag-optimize ng iyong mga modelo nang walang kahirap-hirap at epektibo.

## Pangunahing Mga Tampok:
- Pinagsasama at ina-automate ng Olive ang mga teknik sa pag-optimize para sa mga target na hardware.
- Walang iisang teknik sa pag-optimize na angkop sa lahat ng sitwasyon, kaya pinapayagan ng Olive ang extensibility sa pamamagitan ng pagbibigay-daan sa mga eksperto sa industriya na magdagdag ng kanilang mga inobasyon sa pag-optimize.

## Bawasan ang Pagsisikap sa Engineering:
- Kadalasan, kailangang matutunan at gamitin ng mga developer ang iba't ibang toolchain na specific sa hardware vendor para ihanda at i-optimize ang mga na-train na modelo para sa deployment.
- Pinapasimple ng Olive ang karanasang ito sa pamamagitan ng pag-automate ng mga teknik sa pag-optimize para sa nais na hardware.

## Handang Gamitin na E2E Optimization Solution:

Sa pamamagitan ng pagsasama at pag-tune ng mga integrated na teknik, nag-aalok ang Olive ng isang pinag-isang solusyon para sa end-to-end na pag-optimize.
Isinasaalang-alang nito ang mga limitasyon tulad ng accuracy at latency habang ini-optimize ang mga modelo.

## Paggamit ng Microsoft Olive para sa fine-tuning

Ang Microsoft Olive ay isang napakadaling gamitin na open source na tool para sa pag-optimize ng modelo na kayang saklawin ang parehong fine-tuning at reference sa larangan ng generative artificial intelligence. Kailangan lamang nito ng simpleng configuration, kasabay ng paggamit ng open source na maliliit na language model at kaugnay na runtime environment (AzureML / lokal na GPU, CPU, DirectML), maaari mong tapusin ang fine-tuning o reference ng modelo sa pamamagitan ng awtomatikong pag-optimize, at mahanap ang pinakamahusay na modelo para i-deploy sa cloud o sa mga edge device. Pinapayagan nito ang mga negosyo na bumuo ng kanilang sariling industry vertical na mga modelo sa on-premises at sa cloud.

![intro](../../../../translated_images/tl/intro.46086a3f16ec48e2.png)

## Phi-3 Fine Tuning gamit ang Microsoft Olive

![FinetuningwithOlive](../../../../translated_images/tl/olivefinetune.76d09e9b68253681.png)

## Phi-3 Olive Sample Code at Halimbawa
Sa halimbawang ito gagamitin mo ang Olive para sa:

- Fine-tune ng isang LoRA adapter upang i-classify ang mga parirala sa Sad, Joy, Fear, Surprise.
- Pagsamahin ang mga adapter weights sa base model.
- I-optimize at i-Quantize ang modelo sa int4.

[Sample Code](../../code/03.Finetuning/olive-ort-example/README.md)

### I-setup ang Microsoft Olive

Napakasimple ng pag-install ng Microsoft Olive, at maaari rin itong i-install para sa CPU, GPU, DirectML, at Azure ML

```bash
pip install olive-ai
```

Kung nais mong patakbuhin ang isang ONNX model gamit ang CPU, maaari mong gamitin

```bash
pip install olive-ai[cpu]
```

Kung gusto mong patakbuhin ang isang ONNX model gamit ang GPU, maaari mong gamitin

```python
pip install olive-ai[gpu]
```

Kung gusto mong gamitin ang Azure ML, gamitin

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Paalala**
Kinakailangan ng OS: Ubuntu 20.04 / 22.04

### **Config.json ng Microsoft Olive**

Pagkatapos ng pag-install, maaari mong i-configure ang iba't ibang model-specific na settings sa pamamagitan ng Config file, kabilang ang data, computing, training, deployment, at model generation.

**1. Data**

Sa Microsoft Olive, sinusuportahan ang training gamit ang lokal na data at cloud data, at maaaring i-configure ito sa settings.

*Mga setting para sa lokal na data*

Maaari mong madaling i-setup ang dataset na kailangang i-train para sa fine-tuning, karaniwang nasa json format, at i-adapt ito gamit ang data template. Kailangang i-adjust ito base sa pangangailangan ng modelo (halimbawa, i-adapt ito sa format na kailangan ng Microsoft Phi-3-mini. Kung may iba kang modelo, pakitingnan ang kinakailangang fine-tuning format ng ibang mga modelo para sa pagproseso)

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

**Mga setting para sa cloud data source**

Sa pamamagitan ng pag-link ng datastore ng Azure AI Studio/Azure Machine Learning Service para i-link ang data sa cloud, maaari kang pumili na mag-import ng iba't ibang data source papunta sa Azure AI Studio/Azure Machine Learning Service gamit ang Microsoft Fabric at Azure Data bilang suporta para sa fine-tuning ng data.

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

Kung kailangan mong maging lokal, maaari mong direktang gamitin ang lokal na data resources. Kung kailangan mong gamitin ang resources ng Azure AI Studio / Azure Machine Learning Service, kailangan mong i-configure ang mga kaugnay na Azure parameters, pangalan ng computing power, atbp.

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

***Paalala***

Dahil ito ay pinapatakbo sa pamamagitan ng container sa Azure AI Studio/Azure Machine Learning Service, kailangang i-configure ang kinakailangang environment. Ito ay naka-configure sa conda.yaml environment.

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

**3. Piliin ang iyong SLM**

Maaari mong gamitin ang modelo nang direkta mula sa Hugging face, o maaari mo itong pagsamahin nang direkta sa Model Catalog ng Azure AI Studio / Azure Machine Learning para piliin ang modelong gagamitin. Sa code example sa ibaba gagamitin natin ang Microsoft Phi-3-mini bilang halimbawa.

Kung mayroon kang modelo nang lokal, maaari mong gamitin ang paraang ito

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

Kung gusto mong gumamit ng modelo mula sa Azure AI Studio / Azure Machine Learning Service, maaari mong gamitin ang paraang ito

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

**Paalala:**
Kailangan nating i-integrate ito sa Azure AI Studio / Azure Machine Learning Service, kaya kapag nagse-setup ng modelo, pakitingnan ang version number at kaugnay na pangalan.

Lahat ng modelo sa Azure ay kailangang naka-set sa PyTorch.MLflow

Kailangan mong magkaroon ng Hugging face account at i-bind ang key sa Key value ng Azure AI Studio / Azure Machine Learning

**4. Algorithm**

Napakaganda ng pagkaka-encapsulate ng Microsoft Olive sa Lora at QLora fine-tuning algorithms. Ang kailangan mo lang i-configure ay ilang kaugnay na parameters. Dito gagamitin ko ang QLora bilang halimbawa.

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

Kung gusto mo ng quantization conversion, sinusuportahan na ng main branch ng Microsoft Olive ang onnxruntime-genai method. Maaari mo itong i-set ayon sa iyong pangangailangan:

1. pagsamahin ang adapter weights sa base model
2. I-convert ang modelo sa onnx model na may kinakailangang precision gamit ang ModelBuilder

halimbawa, pag-convert sa quantized INT4

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

**Paalala**  
- Kung gagamit ka ng QLoRA, hindi pa suportado ang quantization conversion ng ONNXRuntime-genai sa ngayon.

- Dapat ding banggitin dito na maaari mong i-set ang mga hakbang sa itaas ayon sa iyong pangangailangan. Hindi kinakailangang i-configure nang buo ang mga hakbang na ito. Depende sa iyong pangangailangan, maaari mong direktang gamitin ang mga hakbang ng algorithm nang walang fine-tuning. Sa huli, kailangan mong i-configure ang mga kaugnay na engine.

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

**5. Tapos na ang fine-tuning**

Sa command line, patakbuhin sa directory ng olive-config.json

```bash
olive run --config olive-config.json  
```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.