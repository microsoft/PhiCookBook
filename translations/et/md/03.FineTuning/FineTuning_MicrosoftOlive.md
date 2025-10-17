<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-10-11T11:44:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "et"
}
-->
# **Phi-3 peenhäälestamine Microsoft Olive'iga**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) on lihtsasti kasutatav riistvarateadlik mudeli optimeerimise tööriist, mis koondab tööstuse juhtivad tehnikad mudeli tihendamise, optimeerimise ja kompileerimise valdkonnas.

See on loodud masinõppe mudelite optimeerimise protsessi lihtsustamiseks, tagades, et need kasutaksid konkreetseid riistvaraarhitektuure võimalikult tõhusalt.

Olgu tegemist pilvepõhiste rakenduste või servaseadmetega, Olive võimaldab mudeleid hõlpsalt ja tõhusalt optimeerida.

## Põhifunktsioonid:
- Olive koondab ja automatiseerib optimeerimistehnikad soovitud riistvarasihtmärkide jaoks.
- Ükski optimeerimistehnika ei sobi kõigile olukordadele, seega võimaldab Olive laiendatavust, et tööstuse eksperdid saaksid lisada oma optimeerimisuuendusi.

## Vähenda inseneritööd:
- Arendajad peavad sageli õppima ja kasutama mitmeid riistvaratootjate spetsiifilisi tööriistakette, et ette valmistada ja optimeerida treenitud mudeleid kasutuselevõtuks.
- Olive lihtsustab seda kogemust, automatiseerides optimeerimistehnikad soovitud riistvara jaoks.

## Valmis kasutamiseks E2E optimeerimislahendus:

Integreeritud tehnikate koostamise ja häälestamise abil pakub Olive ühtset lahendust otsast lõpuni optimeerimiseks.
See arvestab mudelite optimeerimisel piiranguid, nagu täpsus ja latentsus.

## Microsoft Olive'i kasutamine peenhäälestamiseks

Microsoft Olive on väga lihtsasti kasutatav avatud lähtekoodiga mudeli optimeerimise tööriist, mis katab nii peenhäälestamise kui ka viite loomise generatiivse tehisintellekti valdkonnas. See nõuab vaid lihtsat konfiguratsiooni, kombineerituna avatud lähtekoodiga väikeste keelemudelite ja seotud käituskeskkondadega (AzureML / kohalik GPU, CPU, DirectML), võimaldab mudelit automaatse optimeerimise kaudu peenhäälestada või viiteid luua ning leida parim mudel pilve või servaseadmetesse juurutamiseks. See võimaldab ettevõtetel luua oma tööstusharu vertikaalseid mudeleid kohapeal ja pilves.

![intro](../../../../imgs/03/ft/intro.png)

## Phi-3 peenhäälestamine Microsoft Olive'iga 

![FinetuningwithOlive](../../../../imgs/03/ft/olivefinetune.png)

## Phi-3 Olive'i näidiskood ja näide
Selles näites kasutate Olive'i, et:

- Peenhäälestada LoRA adapter fraaside klassifitseerimiseks kategooriatesse kurbus, rõõm, hirm, üllatus.
- Ühendada adapteri kaalud baasmudeliga.
- Optimeerida ja kvantiseerida mudel int4 täpsuseks.

[Näidiskood](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive'i seadistamine

Microsoft Olive'i paigaldamine on väga lihtne ning seda saab paigaldada CPU, GPU, DirectML ja Azure ML jaoks.

```bash
pip install olive-ai
```

Kui soovite käitada ONNX-mudelit CPU-ga, saate kasutada

```bash
pip install olive-ai[cpu]
```

Kui soovite käitada ONNX-mudelit GPU-ga, saate kasutada

```python
pip install olive-ai[gpu]
```

Kui soovite kasutada Azure ML-i, kasutage

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Märkus**
OS-i nõuded: Ubuntu 20.04 / 22.04 

### **Microsoft Olive'i Config.json**

Pärast paigaldamist saate Config-faili kaudu konfigureerida erinevaid mudelispetsiifilisi seadeid, sealhulgas andmeid, arvutust, treenimist, juurutamist ja mudeli genereerimist.

**1. Andmed**

Microsoft Olive'is saab treenida nii kohalike kui ka pilveandmete põhjal ning seda saab seadistustes konfigureerida.

*Kohalike andmete seadistamine*

Saate lihtsalt seadistada andmekogu, mida on vaja peenhäälestamiseks treenida, tavaliselt json-formaadis, ja kohandada seda andmetemplaadiga. Seda tuleb kohandada mudeli nõuete järgi (näiteks kohandada Microsoft Phi-3-mini nõutud formaadiga. Kui teil on teisi mudeleid, viidake teiste mudelite nõutud peenhäälestamise formaatidele).

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

**Pilveandmete allika seadistamine**

Azure AI Studio/Azure Machine Learning Service'i andmesalvestust linkides saate pilveandmeid siduda ja valida erinevaid andmeallikaid, mida Azure AI Studio/Azure Machine Learning Service kaudu peenhäälestamiseks kasutada.

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

**2. Arvutuskonfiguratsioon**

Kui soovite kasutada kohalikke ressursse, saate kasutada otse kohalikke andmeallikaid. Kui vajate Azure AI Studio / Azure Machine Learning Service'i ressursse, peate konfigureerima vastavad Azure'i parameetrid, arvutusvõimsuse nime jne.

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

***Märkus***

Kuna see käitatakse konteineri kaudu Azure AI Studio/Azure Machine Learning Service'is, tuleb vajalik keskkond konfigureerida. See konfigureeritakse conda.yaml keskkonnas.

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

**3. Valige oma SLM**

Mudelid saab otse Hugging Face'ist kasutada või kombineerida Azure AI Studio / Azure Machine Learning'i mudelikataloogiga, et valida kasutatav mudel. Allolevas koodinäites kasutame Microsoft Phi-3-mini mudelit.

Kui teil on mudel kohapeal, saate kasutada seda meetodit

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

Kui soovite kasutada mudelit Azure AI Studio / Azure Machine Learning Service'ist, saate kasutada seda meetodit

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

**Märkus:**
Peame integreeruma Azure AI Studio / Azure Machine Learning Service'iga, seega mudeli seadistamisel viidake versiooninumbrile ja seotud nimetustele.

Kõik Azure'i mudelid peavad olema seadistatud PyTorch.MLflow'ks.

Teil peab olema Hugging Face'i konto ja võtme sidumine Azure AI Studio / Azure Machine Learning'i võtmeväärtusega.

**4. Algoritm**

Microsoft Olive on väga hästi kapseldanud Lora ja QLora peenhäälestamise algoritmid. Teil tuleb konfigureerida vaid mõned asjakohased parameetrid. Siin võtan QLora näitena.

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

Kui soovite kvantiseerimise konversiooni, toetab Microsoft Olive'i põhiharu juba onnxruntime-genai meetodit. Saate selle vastavalt oma vajadustele seadistada:

1. ühendada adapteri kaalud baasmudeliga
2. Konverteerida mudel onnx-mudeliks vajaliku täpsusega ModelBuilderi abil

näiteks konverteerida kvantiseeritud INT4-ks

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

**Märkus** 
- Kui kasutate QLoRA-d, ei toetata ONNXRuntime-genai kvantiseerimise konversiooni praegu.

- Siinkohal tuleb märkida, et saate ülaltoodud samme vastavalt oma vajadustele seadistada. Ei ole vajalik kõiki ülaltoodud samme täielikult konfigureerida. Vastavalt vajadustele saate kasutada algoritmi samme ilma peenhäälestamiseta. Lõpuks peate konfigureerima asjakohased mootorid.

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

**5. Peenhäälestamise lõpetamine**

Käsureal täitke olive-config.json kataloogis

```bash
olive run --config olive-config.json  
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.