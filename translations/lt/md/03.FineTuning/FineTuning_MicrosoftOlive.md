# **Phi-3 derinimas su Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) yra paprastas naudoti, techninei įrangai pritaikytas modelių optimizavimo įrankis, kuris sujungia pramonės lyderiaujančias technikas modelių suspaudimo, optimizavimo ir kompiliavimo srityse.

Jis sukurtas tam, kad supaprastintų mašininio mokymosi modelių optimizavimo procesą, užtikrinant efektyvų specifinių techninės įrangos architektūrų panaudojimą.

Nesvarbu, ar dirbate su debesų pagrindu veikiančiomis programomis, ar kraštiniais įrenginiais, Olive leidžia lengvai ir efektyviai optimizuoti jūsų modelius.

## Pagrindinės savybės:
- Olive apjungia ir automatizuoja optimizavimo technikas, pritaikytas norimai techninei įrangai.
- Nėra vienos universalios optimizavimo technikos, todėl Olive suteikia galimybę pramonės ekspertams integruoti savo inovacijas.

## Sumažinkite inžinerinį darbą:
- Kūrėjai dažnai turi išmokti ir naudoti įvairius techninės įrangos tiekėjų įrankius, kad paruoštų ir optimizuotų apmokytus modelius diegimui.
- Olive supaprastina šią patirtį, automatizuodamas optimizavimo technikas norimai techninei įrangai.

## Paruoštas naudoti E2E optimizavimo sprendimas:

Sujungdamas ir derindamas integruotas technikas, Olive siūlo vieningą sprendimą nuo pradžios iki pabaigos optimizavimui.
Optimizuojant modelius, atsižvelgiama į tokius apribojimus kaip tikslumas ir vėlinimas.

## Microsoft Olive naudojimas derinimui

Microsoft Olive yra labai paprastas naudoti atvirojo kodo modelių optimizavimo įrankis, kuris gali būti naudojamas tiek derinimui, tiek generatyvinės dirbtinio intelekto srities modelių referencijai. Jis reikalauja tik paprastos konfigūracijos, kartu su atvirojo kodo mažais kalbos modeliais ir susijusiomis vykdymo aplinkomis (AzureML / vietinis GPU, CPU, DirectML). Naudodami automatinį optimizavimą, galite užbaigti modelio derinimą ar referenciją ir rasti geriausią modelį, kurį galima diegti debesyje arba kraštiniuose įrenginiuose. Tai leidžia įmonėms kurti savo pramonės vertikalius modelius vietoje ir debesyje.

![intro](../../../../imgs/03/ft/intro.png)

## Phi-3 derinimas su Microsoft Olive 

![FinetuningwithOlive](../../../../imgs/03/ft/olivefinetune.png)

## Phi-3 Olive pavyzdinis kodas ir pavyzdys
Šiame pavyzdyje naudosite Olive:

- Derinti LoRA adapterį frazių klasifikavimui į liūdesį, džiaugsmą, baimę, nuostabą.
- Sujungti adapterio svorius su baziniu modeliu.
- Optimizuoti ir kvantizuoti modelį į int4.

[Pavyzdinis kodas](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive nustatymas

Microsoft Olive įdiegimas yra labai paprastas ir gali būti pritaikytas CPU, GPU, DirectML ir Azure ML

```bash
pip install olive-ai
```

Jei norite paleisti ONNX modelį su CPU, galite naudoti

```bash
pip install olive-ai[cpu]
```

Jei norite paleisti ONNX modelį su GPU, galite naudoti

```python
pip install olive-ai[gpu]
```

Jei norite naudoti Azure ML, naudokite

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Pastaba**
OS reikalavimai: Ubuntu 20.04 / 22.04 

### **Microsoft Olive Config.json**

Po įdiegimo galite konfigūruoti skirtingus modelio nustatymus per Config failą, įskaitant duomenis, skaičiavimus, mokymą, diegimą ir modelio generavimą.

**1. Duomenys**

Microsoft Olive palaiko mokymą su vietiniais ir debesų duomenimis, kuriuos galima konfigūruoti nustatymuose.

*Vietinių duomenų nustatymai*

Galite paprastai nustatyti duomenų rinkinį, kurį reikia mokyti derinimui, paprastai json formatu, ir pritaikyti jį duomenų šablonui. Tai reikia koreguoti pagal modelio reikalavimus (pvz., pritaikyti Microsoft Phi-3-mini reikalaujamam formatui. Jei turite kitų modelių, prašome vadovautis kitų modelių reikalaujamais derinimo formatais).

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

**Debesų duomenų šaltinio nustatymai**

Sujungus Azure AI Studio/Azure Machine Learning Service duomenų saugyklą su debesų duomenimis, galite pasirinkti įvesti skirtingus duomenų šaltinius į Azure AI Studio/Azure Machine Learning Service per Microsoft Fabric ir Azure Data kaip duomenų palaikymą derinimui.

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

**2. Skaičiavimo konfigūracija**

Jei reikia vietinių resursų, galite tiesiogiai naudoti vietinius duomenų resursus. Jei reikia naudoti Azure AI Studio / Azure Machine Learning Service resursus, turite konfigūruoti susijusius Azure parametrus, skaičiavimo galios pavadinimą ir kt.

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

***Pastaba***

Kadangi tai vykdoma per konteinerį Azure AI Studio/Azure Machine Learning Service, reikia konfigūruoti reikiamą aplinką. Tai konfigūruojama conda.yaml aplinkoje.

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

**3. Pasirinkite savo SLM**

Galite naudoti modelį tiesiai iš Hugging Face arba tiesiogiai sujungti jį su Azure AI Studio / Azure Machine Learning Model Catalog, kad pasirinktumėte naudojamą modelį. Žemiau pateiktame kodo pavyzdyje naudosime Microsoft Phi-3-mini kaip pavyzdį.

Jei turite modelį vietoje, galite naudoti šį metodą

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

Jei norite naudoti modelį iš Azure AI Studio / Azure Machine Learning Service, galite naudoti šį metodą

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

**Pastaba:**
Reikia integruoti su Azure AI Studio / Azure Machine Learning Service, todėl nustatant modelį prašome vadovautis versijos numeriu ir susijusiais pavadinimais.

Visi modeliai Azure turi būti nustatyti kaip PyTorch.MLflow

Turite turėti Hugging Face paskyrą ir susieti raktą su Azure AI Studio / Azure Machine Learning Key reikšme.

**4. Algoritmas**

Microsoft Olive puikiai apjungia Lora ir QLora derinimo algoritmus. Jums tereikia konfigūruoti keletą susijusių parametrų. Čia pateikiu QLora kaip pavyzdį.

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

Jei norite kvantizacijos konversijos, Microsoft Olive pagrindinė šaka jau palaiko onnxruntime-genai metodą. Galite nustatyti pagal savo poreikius:

1. Sujungti adapterio svorius su baziniu modeliu
2. Konvertuoti modelį į onnx modelį su reikiamu tikslumu naudojant ModelBuilder

pvz., konvertuoti į kvantizuotą INT4

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

**Pastaba** 
- Jei naudojate QLoRA, ONNXRuntime-genai kvantizacijos konversija šiuo metu nėra palaikoma.

- Reikia pažymėti, kad galite nustatyti aukščiau pateiktus žingsnius pagal savo poreikius. Nėra būtina visiškai konfigūruoti visų šių žingsnių. Priklausomai nuo poreikių, galite tiesiogiai naudoti algoritmo žingsnius be derinimo. Galiausiai reikia konfigūruoti susijusius variklius.

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

**5. Derinimo užbaigimas**

Komandinėje eilutėje vykdykite olive-config.json kataloge

```bash
olive run --config olive-config.json  
```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.