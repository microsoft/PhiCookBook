<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:50:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "cs"
}
-->
# **Doladění Phi-3 pomocí Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) je snadno použitelný nástroj pro optimalizaci modelů s ohledem na hardware, který kombinuje špičkové techniky v oblasti komprese, optimalizace a kompilace modelů.

Je navržen tak, aby zjednodušil proces optimalizace strojově učených modelů a zajistil jejich co nejefektivnější využití na specifických hardwarových architekturách.

Ať už pracujete na cloudových aplikacích nebo na edge zařízeních, Olive vám umožní optimalizovat modely snadno a efektivně.

## Klíčové vlastnosti:
- Olive shromažďuje a automatizuje optimalizační techniky pro požadované hardwarové cíle.
- Žádná jednotlivá optimalizační technika nevyhovuje všem scénářům, proto Olive umožňuje rozšiřitelnost tím, že odborníkům z oboru dovoluje přidávat vlastní optimalizační inovace.

## Snížení inženýrské námahy:
- Vývojáři často musí zvládnout a používat více nástrojů specifických pro různé výrobce hardwaru, aby připravili a optimalizovali natrénované modely pro nasazení.
- Olive tento proces zjednodušuje automatizací optimalizačních technik pro požadovaný hardware.

## Připravené end-to-end řešení optimalizace:

Složením a laděním integrovaných technik nabízí Olive jednotné řešení pro end-to-end optimalizaci.
Při optimalizaci modelů bere v úvahu omezení jako přesnost a latenci.

## Použití Microsoft Olive pro doladění

Microsoft Olive je velmi snadno použitelný open source nástroj pro optimalizaci modelů, který pokrývá jak doladění, tak referenční použití v oblasti generativní umělé inteligence. Vyžaduje pouze jednoduchou konfiguraci, v kombinaci s použitím open source malých jazykových modelů a souvisejících runtime prostředí (AzureML / lokální GPU, CPU, DirectML) můžete dokončit doladění nebo referenci modelu pomocí automatické optimalizace a najít nejlepší model pro nasazení do cloudu nebo na edge zařízení. Umožňuje firmám vytvářet vlastní vertikální modely pro průmyslová odvětví jak lokálně, tak v cloudu.

![intro](../../../../translated_images/cs/intro.46086a3f16ec48e2.png)

## Doladění Phi-3 pomocí Microsoft Olive

![FinetuningwithOlive](../../../../translated_images/cs/olivefinetune.76d09e9b68253681.png)

## Ukázkový kód a příklad Phi-3 Olive
V tomto příkladu použijete Olive k:

- Doladění LoRA adaptéru pro klasifikaci frází do kategorií Smutek, Radost, Strach, Překvapení.
- Sloučení vah adaptéru do základního modelu.
- Optimalizaci a kvantizaci modelu do int4.

[Ukázkový kód](../../code/03.Finetuning/olive-ort-example/README.md)

### Nastavení Microsoft Olive

Instalace Microsoft Olive je velmi jednoduchá a lze ji nainstalovat pro CPU, GPU, DirectML i Azure ML.

```bash
pip install olive-ai
```

Pokud chcete spustit ONNX model na CPU, můžete použít

```bash
pip install olive-ai[cpu]
```

Pokud chcete spustit ONNX model na GPU, můžete použít

```python
pip install olive-ai[gpu]
```

Pokud chcete použít Azure ML, použijte

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Poznámka**
Požadavky na OS: Ubuntu 20.04 / 22.04

### **Config.json Microsoft Olive**

Po instalaci můžete konfigurovat různá nastavení specifická pro model přes konfigurační soubor, včetně dat, výpočetních zdrojů, tréninku, nasazení a generování modelu.

**1. Data**

Microsoft Olive podporuje trénink na lokálních i cloudových datech, což lze nastavit v konfiguraci.

*Nastavení lokálních dat*

Jednoduše nastavíte datovou sadu, kterou chcete použít pro doladění, obvykle ve formátu json, a přizpůsobíte ji datové šabloně. Toto je potřeba upravit podle požadavků modelu (například přizpůsobit formátu požadovanému Microsoft Phi-3-mini. Pokud máte jiné modely, prosím podívejte se na požadované formáty doladění pro dané modely).

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

**Nastavení cloudových datových zdrojů**

Propojením datového úložiště Azure AI Studio/Azure Machine Learning Service můžete přistupovat k datům v cloudu a zvolit různé datové zdroje přes Microsoft Fabric a Azure Data jako podporu pro doladění.

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

**2. Výpočetní konfigurace**

Pokud chcete pracovat lokálně, můžete přímo využít lokální datové zdroje. Pokud chcete využít zdroje Azure AI Studio / Azure Machine Learning Service, je potřeba nastavit příslušné parametry Azure, název výpočetního výkonu apod.

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

***Poznámka***

Protože běží v kontejneru na Azure AI Studio/Azure Machine Learning Service, je potřeba nakonfigurovat požadované prostředí. To se nastavuje v souboru conda.yaml.

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

**3. Výběr SLM**

Model můžete použít přímo z Hugging Face, nebo jej můžete vybrat z katalogu modelů Azure AI Studio / Azure Machine Learning. V níže uvedeném příkladu použijeme Microsoft Phi-3-mini.

Pokud máte model lokálně, můžete použít tento způsob

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

Pokud chcete použít model z Azure AI Studio / Azure Machine Learning Service, použijte tento způsob

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

**Poznámka:**
Je potřeba integrace s Azure AI Studio / Azure Machine Learning Service, proto při nastavování modelu dbejte na správné verze a pojmenování.

Všechny modely na Azure musí být nastaveny jako PyTorch.MLflow.

Musíte mít účet na Hugging Face a propojit klíč s hodnotou Key v Azure AI Studio / Azure Machine Learning.

**4. Algoritmus**

Microsoft Olive velmi dobře zabalil algoritmy doladění Lora a QLora. Stačí nastavit několik relevantních parametrů. Zde uvádím příklad s QLora.

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

Pokud chcete provést kvantizační převod, hlavní větev Microsoft Olive již podporuje metodu onnxruntime-genai. Můžete ji nastavit podle potřeby:

1. sloučit váhy adaptéru do základního modelu
2. převést model na onnx model s požadovanou přesností pomocí ModelBuilderu

například převod na kvantizovaný INT4

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

**Poznámka**
- Pokud používáte QLoRA, kvantizační převod pomocí ONNXRuntime-genai zatím není podporován.

- Je třeba zdůraznit, že výše uvedené kroky lze nastavit podle vlastních potřeb. Není nutné je všechny kompletně konfigurovat. Podle potřeby můžete použít pouze kroky algoritmu bez doladění. Nakonec je potřeba nastavit příslušné enginy.

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

**5. Dokončení doladění**

Na příkazové řádce spusťte v adresáři s olive-config.json

```bash
olive run --config olive-config.json  
```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.