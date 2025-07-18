<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:46:28+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "no"
}
-->
# **Finjustering av Phi-3 med Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) er et brukervennlig verktøy for maskinvarebevisst modelloptimalisering som samler bransjeledende teknikker innen modellkomprimering, optimalisering og kompilering.

Det er utviklet for å forenkle prosessen med å optimalisere maskinlæringsmodeller, slik at de utnytter spesifikke maskinvarearkitekturer på en mest mulig effektiv måte.

Enten du jobber med skybaserte applikasjoner eller enheter på kanten, gjør Olive det enkelt og effektivt å optimalisere modellene dine.

## Viktige funksjoner:
- Olive samler og automatiserer optimaliseringsteknikker for ønskede maskinvaremål.
- Ingen enkelt optimaliseringsteknikk passer for alle situasjoner, derfor tillater Olive utvidelser slik at bransjeeksperter kan integrere sine egne optimaliseringsinnovasjoner.

## Reduser ingeniørarbeidet:
- Utviklere må ofte lære og bruke flere maskinvareleverandørspesifikke verktøykjeder for å forberede og optimalisere trente modeller for distribusjon.
- Olive forenkler denne prosessen ved å automatisere optimaliseringsteknikkene for ønsket maskinvare.

## Klar-til-bruk ende-til-ende optimaliseringsløsning:

Ved å sette sammen og finjustere integrerte teknikker tilbyr Olive en samlet løsning for ende-til-ende optimalisering.
Den tar hensyn til begrensninger som nøyaktighet og latenstid under optimaliseringen av modeller.

## Bruke Microsoft Olive til finjustering

Microsoft Olive er et svært brukervennlig åpen kildekode-verktøy for modelloptimalisering som dekker både finjustering og referanse innen generativ kunstig intelligens. Det krever kun enkel konfigurasjon, kombinert med bruk av åpne små språkmodeller og tilhørende kjøremiljøer (AzureML / lokal GPU, CPU, DirectML), slik at du kan fullføre finjustering eller referanse av modellen gjennom automatisk optimalisering, og finne den beste modellen for distribusjon i skyen eller på enheter på kanten. Dette gjør det mulig for bedrifter å bygge sine egne bransjespesifikke modeller både lokalt og i skyen.

![intro](../../../../translated_images/intro.46086a3f16ec48e273c5ec11ec23b0dd23593dbab951e95d565145b40e8571a5.no.png)

## Phi-3 finjustering med Microsoft Olive

![FinetuningwithOlive](../../../../translated_images/olivefinetune.76d09e9b68253681cff9564145ddbf6d335cbcd7a79f4886b4120380deaa384f.no.png)

## Phi-3 Olive eksempel på kode og bruk
I dette eksempelet vil du bruke Olive til å:

- Finjustere en LoRA-adapter for å klassifisere setninger i Sad, Joy, Fear, Surprise.
- Slå sammen adaptervektene med basismodellen.
- Optimalisere og kvantisere modellen til int4.

[Eksempelkode](../../code/03.Finetuning/olive-ort-example/README.md)

### Sette opp Microsoft Olive

Installasjonen av Microsoft Olive er veldig enkel, og kan også installeres for CPU, GPU, DirectML og Azure ML.

```bash
pip install olive-ai
```

Hvis du ønsker å kjøre en ONNX-modell med CPU, kan du bruke

```bash
pip install olive-ai[cpu]
```

Hvis du vil kjøre en ONNX-modell med GPU, kan du bruke

```python
pip install olive-ai[gpu]
```

Hvis du vil bruke Azure ML, bruk

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Merk**
OS-krav: Ubuntu 20.04 / 22.04

### **Microsoft Olive sin Config.json**

Etter installasjon kan du konfigurere ulike modellspesifikke innstillinger via Config-filen, inkludert data, beregning, trening, distribusjon og modellgenerering.

**1. Data**

På Microsoft Olive støttes trening på både lokale data og skydata, og dette kan konfigureres i innstillingene.

*Innstillinger for lokale data*

Du kan enkelt sette opp datasettet som skal trenes for finjustering, vanligvis i json-format, og tilpasse det med datamalen. Dette må justeres basert på modellens krav (for eksempel tilpasses formatet som kreves av Microsoft Phi-3-mini. Hvis du har andre modeller, vennligst se på de nødvendige finjusteringsformatene for disse modellene).

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

**Innstillinger for skybaserte datakilder**

Ved å koble til datalageret i Azure AI Studio/Azure Machine Learning Service for å hente data i skyen, kan du velge å importere ulike datakilder til Azure AI Studio/Azure Machine Learning Service via Microsoft Fabric og Azure Data som støtte for finjustering.

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

**2. Beregningskonfigurasjon**

Hvis du trenger lokal kjøring, kan du bruke lokale dataressurser direkte. Hvis du skal bruke ressurser fra Azure AI Studio / Azure Machine Learning Service, må du konfigurere relevante Azure-parametere, navn på beregningsressurser osv.

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

***Merk***

Siden det kjøres gjennom en container på Azure AI Studio/Azure Machine Learning Service, må det nødvendige miljøet konfigureres. Dette gjøres i conda.yaml-miljøet.

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

**3. Velg din SLM**

Du kan bruke modellen direkte fra Hugging Face, eller du kan kombinere den med Model Catalog i Azure AI Studio / Azure Machine Learning for å velge modellen du vil bruke. I kodeeksempelet under bruker vi Microsoft Phi-3-mini som eksempel.

Hvis du har modellen lokalt, kan du bruke denne metoden

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

Hvis du vil bruke en modell fra Azure AI Studio / Azure Machine Learning Service, kan du bruke denne metoden

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

**Merk:**
Vi må integrere med Azure AI Studio / Azure Machine Learning Service, så ved oppsett av modellen, vennligst følg versjonsnummer og tilhørende navngivning.

Alle modeller på Azure må settes til PyTorch.MLflow.

Du må ha en Hugging Face-konto og knytte nøkkelen til nøkkelverdien i Azure AI Studio / Azure Machine Learning.

**4. Algoritme**

Microsoft Olive pakker inn Lora og QLora finjusteringsalgoritmer på en god måte. Alt du trenger å konfigurere er noen relevante parametere. Her bruker jeg QLora som eksempel.

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

Hvis du ønsker kvantiseringskonvertering, støtter hovedgrenen til Microsoft Olive allerede onnxruntime-genai-metoden. Du kan sette det etter behov:

1. Slå sammen adaptervekter med basismodellen
2. Konverter modellen til onnx-modell med ønsket presisjon via ModelBuilder

for eksempel konvertering til kvantisert INT4

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

**Merk**
- Hvis du bruker QLoRA, støttes ikke kvantiseringskonvertering med ONNXRuntime-genai foreløpig.

- Det bør påpekes at du kan sette opp de ovennevnte trinnene etter eget behov. Det er ikke nødvendig å konfigurere alle trinnene fullstendig. Avhengig av dine behov kan du bruke algoritmetrinnene direkte uten finjustering. Til slutt må du konfigurere relevante motorer.

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

**5. Fullført finjustering**

På kommandolinjen, kjør i katalogen med olive-config.json

```bash
olive run --config olive-config.json  
```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.