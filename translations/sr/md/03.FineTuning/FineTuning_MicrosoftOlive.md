<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:51:34+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "sr"
}
-->
# **Фино подешавање Phi-3 уз Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) је једноставан алат за оптимизацију модела који је свестран према хардверу и обједињује водеће индустријске технике у области компресије, оптимизације и компилације модела.

Дизајниран је да поједностави процес оптимизације модела машинског учења, обезбеђујући њихову најефикаснију употребу на одређеним хардверским архитектурама.

Без обзира да ли радите на апликацијама у облаку или на уређајима на ивици мреже, Olive вам омогућава да лако и ефикасно оптимизујете своје моделе.

## Кључне карактеристике:
- Olive окупља и аутоматизује технике оптимизације за жељене хардверске платформе.
- Једна техника оптимизације не одговара свим сценаријима, па Olive омогућава проширивост тако што стручњацима из индустрије дозвољава да убаце своје иновације у оптимизацији.

## Смањите инжењерски напор:
- Програмери често морају да науче и користе више алата специфичних за различите хардверске произвођаче како би припремили и оптимизовали обучене моделе за имплементацију.
- Olive поједностављује овај процес аутоматизујући технике оптимизације за жељени хардвер.

## Спремно за употребу E2E решење за оптимизацију:

Комбинујући и подешавајући интегрисане технике, Olive нуди јединствено решење за оптимизацију од почетка до краја.
У обзир узима ограничења као што су прецизност и латенција током оптимизације модела.

## Коришћење Microsoft Olive за фино подешавање

Microsoft Olive је веома једноставан алат отвореног кода за оптимизацију модела који покрива и фино подешавање и референце у области генеративне вештачке интелигенције. Захтева само једноставну конфигурацију, у комбинацији са коришћењем отворених малих језичких модела и релевантних окружења за извршавање (AzureML / локални GPU, CPU, DirectML), омогућавајући вам да завршите фино подешавање или референцу модела кроз аутоматску оптимизацију и пронађете најбољи модел за имплементацију у облаку или на уређајима на ивици мреже. Омогућава предузећима да граде своје индустријске вертикалне моделе локално и у облаку.

![intro](../../../../translated_images/intro.46086a3f16ec48e2.sr.png)

## Фино подешавање Phi-3 уз Microsoft Olive

![FinetuningwithOlive](../../../../translated_images/olivefinetune.76d09e9b68253681.sr.png)

## Phi-3 Olive пример кода и пример
У овом примеру ћете користити Olive да:

- Фино подесите LoRA адаптер за класификацију фраза у категорије Туга, Радост, Страх, Изненађење.
- Спојите тежине адаптера у основни модел.
- Оптимизујете и квантујете модел у int4.

[Пример кода](../../code/03.Finetuning/olive-ort-example/README.md)

### Подешавање Microsoft Olive

Инсталација Microsoft Olive је врло једноставна, и може се инсталирати за CPU, GPU, DirectML и Azure ML

```bash
pip install olive-ai
```

Ако желите да покренете ONNX модел на CPU-у, можете користити

```bash
pip install olive-ai[cpu]
```

Ако желите да покренете ONNX модел на GPU-у, можете користити

```python
pip install olive-ai[gpu]
```

Ако желите да користите Azure ML, користите

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Напомена**  
Захтеви за ОС: Ubuntu 20.04 / 22.04

### **Microsoft Olive Config.json**

Након инсталације, можете конфигурисати различита подешавања специфична за модел преко Config фајла, укључујући податке, рачунарске ресурсе, тренинг, имплементацију и генерисање модела.

**1. Податци**

На Microsoft Olive платформи, тренинг на локалним и облачним подацима је подржан и може се конфигурисати у подешавањима.

*Подешавања локалних података*

Једноставно можете подесити скуп података који треба да се користи за фино подешавање, обично у json формату, и прилагодити га уз помоћ шаблона података. Ово треба прилагодити у складу са захтевима модела (на пример, прилагодити формату који захтева Microsoft Phi-3-mini. Ако користите друге моделе, молимо погледајте потребне формате за фино подешавање тих модела)

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

**Подешавања извора облачних података**

Повезивањем складишта података Azure AI Studio/Azure Machine Learning Service за приступ подацима у облаку, можете изабрати да увезете различите изворе података у Azure AI Studio/Azure Machine Learning Service преко Microsoft Fabric и Azure Data као подршку за фино подешавање.

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

**2. Конфигурација рачунарских ресурса**

Ако желите да радите локално, можете директно користити локалне ресурсе података. Ако желите да користите ресурсе Azure AI Studio / Azure Machine Learning Service, потребно је да конфигуришете релевантне Azure параметре, име рачунарске снаге и слично.

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

***Напомена***

Пошто се покреће кроз контејнер на Azure AI Studio/Azure Machine Learning Service, потребно је конфигурисати захтевано окружење. Ово се подешава у conda.yaml окружењу.

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

**3. Избор вашег SLM**

Можете користити модел директно са Hugging face, или га повезати са Model Catalog-ом Azure AI Studio / Azure Machine Learning да бисте изабрали модел за коришћење. У примеру кода испод користићемо Microsoft Phi-3-mini као пример.

Ако имате модел локално, можете користити овај начин

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

Ако желите да користите модел из Azure AI Studio / Azure Machine Learning Service, можете користити овај начин

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

**Напомена:**  
Потребна је интеграција са Azure AI Studio / Azure Machine Learning Service, па приликом подешавања модела обратите пажњу на верзију и релевантна имена.

Сви модели на Azure-у морају бити подешени као PyTorch.MLflow

Потребно је да имате Hugging face налог и да повежете кључ са Key вредношћу Azure AI Studio / Azure Machine Learning

**4. Алгоритам**

Microsoft Olive веома добро обухвата Lora и QLora алгоритме за фино подешавање. Потребно је само да конфигуришете неке релевантне параметре. Овде узимамо QLora као пример.

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

Ако желите конверзију квантизације, главна грана Microsoft Olive већ подржава onnxruntime-genai метод. Можете га подесити према својим потребама:

1. спојити тежине адаптера у основни модел  
2. конвертовати модел у onnx модел са потребном прецизношћу помоћу ModelBuilder-а

на пример, конверзија у квантизовани INT4

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

**Напомена**  
- Ако користите QLoRA, тренутно није подржана квантизација преко ONNXRuntime-genai.  
- Важно је напоменути да горе наведене кораке можете подесити према својим потребама. Није неопходно да конфигуришете све кораке у потпуности. У зависности од потреба, можете директно користити кораке алгоритма без фино подешавања. На крају је потребно конфигурисати релевантне енџине.

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

**5. Завршено фино подешавање**

На командној линији, покрените у директоријуму са olive-config.json

```bash
olive run --config olive-config.json  
```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати коришћењем овог превода.