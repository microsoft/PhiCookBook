<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:50:55+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "ro"
}
-->
# **Fine-tuning Phi-3 cu Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) este un instrument ușor de folosit pentru optimizarea modelelor, conștient de hardware, care reunește tehnici de top din industrie în compresia, optimizarea și compilarea modelelor.

Este conceput pentru a simplifica procesul de optimizare a modelelor de machine learning, asigurând utilizarea cât mai eficientă a arhitecturilor hardware specifice.

Indiferent dacă lucrezi cu aplicații în cloud sau pe dispozitive edge, Olive îți permite să optimizezi modelele cu ușurință și eficiență.

## Caracteristici principale:
- Olive agregă și automatizează tehnici de optimizare pentru hardware-ul țintă dorit.
- Nicio tehnică de optimizare nu se potrivește tuturor scenariilor, așa că Olive permite extinderea prin integrarea inovațiilor experților din industrie.

## Reducerea efortului de inginerie:
- Dezvoltatorii trebuie adesea să învețe și să folosească mai multe toolchain-uri specifice furnizorilor de hardware pentru a pregăti și optimiza modelele antrenate pentru implementare.
- Olive simplifică această experiență prin automatizarea tehnicilor de optimizare pentru hardware-ul dorit.

## Soluție E2E de optimizare gata de utilizare:

Prin combinarea și reglarea tehnicilor integrate, Olive oferă o soluție unificată pentru optimizarea end-to-end.
Ia în considerare constrângeri precum acuratețea și latența în timpul optimizării modelelor.

## Utilizarea Microsoft Olive pentru fine-tuning

Microsoft Olive este un instrument open source foarte ușor de folosit pentru optimizarea modelelor, care acoperă atât fine-tuning-ul, cât și referința în domeniul inteligenței artificiale generative. Necesită doar o configurare simplă, combinată cu utilizarea modelelor mici open source și a mediilor de rulare aferente (AzureML / GPU local, CPU, DirectML), permițând finalizarea fine-tuning-ului sau referinței modelului prin optimizare automată și găsirea celui mai bun model pentru implementare în cloud sau pe dispozitive edge. Permite companiilor să-și construiască propriile modele verticale de industrie on-premises și în cloud.

![intro](../../../../translated_images/intro.46086a3f16ec48e2.ro.png)

## Fine-tuning Phi-3 cu Microsoft Olive

![FinetuningwithOlive](../../../../translated_images/olivefinetune.76d09e9b68253681.ro.png)

## Exemplu de cod și utilizare Phi-3 Olive
În acest exemplu vei folosi Olive pentru a:

- Face fine-tuning unui adaptor LoRA pentru clasificarea frazelor în Sad, Joy, Fear, Surprise.
- Îmbina greutățile adaptorului în modelul de bază.
- Optimiza și cuantiza modelul în int4.

[Sample Code](../../code/03.Finetuning/olive-ort-example/README.md)

### Configurarea Microsoft Olive

Instalarea Microsoft Olive este foarte simplă și poate fi făcută pentru CPU, GPU, DirectML și Azure ML

```bash
pip install olive-ai
```

Dacă dorești să rulezi un model ONNX pe CPU, poți folosi

```bash
pip install olive-ai[cpu]
```

Dacă vrei să rulezi un model ONNX pe GPU, poți folosi

```python
pip install olive-ai[gpu]
```

Dacă vrei să folosești Azure ML, folosește

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Notă**
Cerință OS: Ubuntu 20.04 / 22.04

### **Config.json Microsoft Olive**

După instalare, poți configura setări specifice modelului prin fișierul Config, inclusiv date, calcul, antrenament, implementare și generare model.

**1. Date**

Pe Microsoft Olive, antrenamentul pe date locale și în cloud este suportat și poate fi configurat în setări.

*Setări pentru date locale*

Poți configura simplu setul de date pentru fine-tuning, de obicei în format json, și îl adaptezi cu șablonul de date. Aceasta trebuie ajustată în funcție de cerințele modelului (de exemplu, adaptarea la formatul cerut de Microsoft Phi-3-mini. Dacă ai alte modele, te rugăm să consulți formatele necesare pentru fine-tuning ale altor modele).

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

**Setări pentru surse de date în cloud**

Prin conectarea datastore-ului Azure AI Studio/Azure Machine Learning Service pentru a accesa datele din cloud, poți alege să imporți diferite surse de date în Azure AI Studio/Azure Machine Learning Service prin Microsoft Fabric și Azure Data ca suport pentru fine-tuning.

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

**2. Configurarea calculului**

Dacă dorești să folosești resurse locale, poți utiliza direct datele locale. Dacă vrei să folosești resursele Azure AI Studio / Azure Machine Learning Service, trebuie să configurezi parametrii Azure relevanți, numele resurselor de calcul etc.

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

***Notă***

Pentru că rulează printr-un container pe Azure AI Studio/Azure Machine Learning Service, mediul necesar trebuie configurat. Aceasta se face în fișierul conda.yaml.

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

**3. Alege-ți SLM-ul**

Poți folosi modelul direct de pe Hugging Face sau îl poți combina direct cu Catalogul de modele din Azure AI Studio / Azure Machine Learning pentru a selecta modelul dorit. În exemplul de cod de mai jos vom folosi Microsoft Phi-3-mini ca exemplu.

Dacă ai modelul local, poți folosi această metodă

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

Dacă vrei să folosești un model din Azure AI Studio / Azure Machine Learning Service, poți folosi această metodă

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

**Notă:**
Trebuie să integrăm cu Azure AI Studio / Azure Machine Learning Service, așa că la configurarea modelului, te rugăm să consulți numărul versiunii și denumirile aferente.

Toate modelele din Azure trebuie setate pe PyTorch.MLflow

Trebuie să ai un cont Hugging Face și să legi cheia de valoarea Key din Azure AI Studio / Azure Machine Learning

**4. Algoritm**

Microsoft Olive încorporează foarte bine algoritmii de fine-tuning Lora și QLora. Tot ce trebuie să configurezi sunt câțiva parametri relevanți. Aici iau QLora ca exemplu.

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

Dacă dorești conversie prin cuantizare, ramura principală Microsoft Olive suportă deja metoda onnxruntime-genai. Poți seta în funcție de nevoi:

1. îmbină greutățile adaptorului în modelul de bază
2. convertește modelul în model onnx cu precizia necesară folosind ModelBuilder

de exemplu conversia în INT4 cuantizat

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

**Notă**  
- Dacă folosești QLoRA, conversia prin cuantizare ONNXRuntime-genai nu este momentan suportată.

- Trebuie menționat că poți configura pașii de mai sus după propriile nevoi. Nu este obligatoriu să configurezi complet toți acești pași. În funcție de necesități, poți folosi direct pașii algoritmului fără fine-tuning. În final, trebuie să configurezi motoarele relevante.

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

**5. Finalizarea fine-tuning-ului**

Pe linia de comandă, execută în directorul cu olive-config.json

```bash
olive run --config olive-config.json  
```

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.