<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-12-21T18:25:19+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "te"
}
-->
# **Phi-3ని Microsoft Oliveతో ఫైన్‑ట్యూనింగ్**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) ఒక సులభంగా ఉపయోగించుకునేందుకు అనువైన హార్డ్‌వేర్‑అవేర్ మోడల్ ఆప్టిమైజేషన్ టూల్, ఇది మోడల్ కంప్రెషన్, ఆప్టిమైజేషన్, మరియు కంపైలేషన్ ప్రాంతాలలో పరిశ్రమనాయక తంత్రజ్ఞానాలను ఒకే చోట చేరుస్తుంది.

ఇది ప్రత్యేక హార్డ్‌వేర్ ఆర్కిటెక్చర్లను సమర్థవంతంగా ఉపయోగించుకునేలా మిషిన్ లెర్నింగ్ మోడళ్లను ఆప్టిమైజ్ చేయునట్లుగా ప్రక్రియను సులభతరం చేయడానికి రూపొందించబడింది.

మీరు క్లౌడ్ ఆధారిత యాప్స్ మీద పనిచేస్తున్నా లేదా ఎడ్జ్ పరికరాలపై ఉన్నా, Olive మీ మోడళ్లను Effortlessly మరియు Effectively గా ఆప్టిమైజ్ చేయడానికి సామర్థ్యం కల్పిస్తుంది.

## ముఖ్య లక్షణాలు:
- Olive లక్ష్య హార్డ్‌వేర్ కోసం కావలసిన ఆప్టిమైజేషన్ తంత్రజ్ఞానాలను సముదాయంగా సమీకరించి ఆటోమేట్ చేస్తుంది.
- ఒక్కో ఆప్టిమైజేషన్ పద్ధతి అన్ని సందర్భాలకు సరిపోదు, అందుకై Olive అనువర్తింపుల పరిజ్ఞానాన్ని పరికర experts ద్వారా కొత్త ఆప్టిమైజేషన్ ఇన్నోవేషన్లను ప్లగ్ చేయడానికి విస్తారతను అందిస్తుంది.

## ఇంజనీరింగ్ శ్రమను తగ్గించడం:
- డెవలపర్లు తరచుగా ట్రైన్డ్ మోడళ్లను డిప్లాయ్ చేయడానికి వివిధ హార్డ్‌వేర్ వెండర్‑నిర్దిష్ట టూల్‌చెయిన్‌లు నేర్చుకుని ఉపయోగించాల్సి ఉంటుంది.
- Olive కావలసిన హార్డ్‌వేర్ కోసం ఆప్టిమైజేషన్ పద్ధతులను ఆటోమేటింగ్ చేయడం ద్వారా ఈ అనుభవాన్ని సులభతరం చేస్తుంది.

## ఉపయోగించడానికి సిద్ధంగా ఉన్న E2E ఆప్టిమైజేషన్ పరిష్కారం:

ఎంటిగ్రేటెడ్ తంత్రజ్ఞానాలను కంపోస్ చేసి ట్యూన్ చేయడం ద్వారా, Olive ఎండ్‑టు‑ఎండ్ ఆప్టిమైజేషన్ కోసం ఒక ఐక్య పరిష్కారాన్ని అందిస్తుంది.
యాక్యూరసీ మరియు లేటెన్సీ వంటి పరిమితుల్ని పరిగణనలోకి తీసుకుని మోడళ్లను ఆప్టిమైజ్ చేస్తుంది.

## Microsoft Olive ఉపయోగించి ఫైన్‑ట్యూనింగ్

Microsoft Olive ఒక చాలా సुलభంగా ఉపయోగించగల ఓపెన్‑సోর্স మోడల్ ఆప్టిమైజేషన్ టూల్, ఇది జనరేటివ్ ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ రంగంలో ఫైన్‑ట్యూనింగ్ మరియు రిఫరెన్స్ రెండింటినీ కవర్ చేయగలదు. ఇది కేవలం సాదాసీదా కాన్ఫిగరేషన్ మాత్రమే అవసరం, ఓపెన్‑సోర్స్ చిన్న భాషా మోడళ్లను మరియు సంబంధిత రన్‌టైమ్ ఎన్విరాన్‌మెంట్స్ (AzureML / local GPU, CPU, DirectML) ను కలిపి ఉపయోగించి, ఆటోమేటిక్ ఆప్టిమైజేషన్ ద్వారా మోడల్ ఫైన్‑ట్యూనింగ్ లేదా రిఫరెన్సింగ్ పూర్తి చేయవచ్చు, మరియు క్లౌడ్ లేదా ఎడ్జ్ పరికరాలకు డిప్లాయ్ చేయడానికి ఉత్తమ మోడల్‌ని కనుగొంటుంది. సంస్థలకు తమ పరిశ్రమ ప్రత్యేక మోడళ్లను ఆన్‑ప్రెమీస్ మరియు క్లౌడ్‌లో నిర్మించడానికి అనుమతిస్తుంది.

![పరిచయం](../../../../translated_images/intro.46086a3f16ec48e273c5ec11ec23b0dd23593dbab951e95d565145b40e8571a5.te.png)

## Microsoft Oliveతో Phi-3 ఫైన్‌ట్యూనింగ్

![Oliveతో ఫైన్‌ట్యూనింగ్](../../../../translated_images/olivefinetune.76d09e9b68253681cff9564145ddbf6d335cbcd7a79f4886b4120380deaa384f.te.png)

## Phi-3 Olive నమూనా కోడ్ మరియు ఉదాహరణ
ఈ ఉదాహరణలో మీరు Olive ను ఉపయోగించి:

- LoRA అడాప్టర్‌ను ఫైన్‑ట్యూన్ చేసి వాక్యాలను దుఃఖం, సంతోషం, భయం, ఆశ్చర్యం గా వర్గీకరించండి.
- అడాప్టర్ వెయిట్స్‌ను బేస్ మోడల్‌లో విలీనం చేయండి.
- మోడల్‌ను ఆప్టిమైజ్ చేసి int4 గా క్వాంటైజ్ చేయండి.

[నమూనా కోడ్](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive సెటప్

Microsoft Olive ఇన్‌స్టాలేషన్ చాలా సులభం, మరియు ఇది CPU, GPU, DirectML, మరియు Azure ML కోసం కూడా ఇన్‌స్టాల్ చేయవచ్చు

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
pip install git+https://github.com/microsoft/Olive#గుడ్డు=olive-ai[azureml]
```

**గమనిక**
OS requirement : Ubuntu 20.04 / 22.04 

### **Microsoft Olive యొక్క Config.json**

ఇన్‌స్టాలేషన్ తర్వాత, మీరు Config ఫైల్ ద్వారా డేటా, కంప్యూటింగ్, ట్రైనింగ్, డిప్లాయ్‌మెంట్, మరియు మోడల్ జనరేషన్ వంటి వివిధ మోడల్‑స్పెసిఫిక్ సెట్టింగులను కాన్ఫిగర్ చేయవచ్చు.

**1. డేటా**

Microsoft Olive పై, స్థానిక డేటా మరియు క్లౌడ్ డేటా మీద ట్రైనింగ్ సపోర్ట్ చేయబడుతుంది, మరియు సెట్టింగుల్లో దీన్ని కాన్ఫిగర్ చేయవచ్చు.

*స్థానిక డేటా సెట్టింగ్స్*

ఫైన్‑ట్యూనింగ్ కోసం ట్రైన్ చేయాల్సిన డేటా సెట్‌ను సాదాసీదాగా సెటప్ చేయవచ్చు, సాధారణంగా json ఫార్మాట్‌లో ఉండి, డేటా టెంప్లేట్‌కు అనుగుణంగా ఉండాలి. ఇది మోడల్ అవసరాల ఆధారంగా సర్దుబాటు చేయబడాలి (ఉదాహరణకు, Microsoft Phi-3-mini కోరుకునే ఫార్మాట్‌కు అనుగుణంగా అమర్చండి. మీ వద్ద ఇతర మోడళ్లు ఉంటే, దయచేసి ఇతర మోడళ్ల అవసరమైన ఫైన్‑ట్యూనింగ్ ఫార్మాట్లను పరిశీలించి ప్రాసెస్ చేయండి)

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

**క్లౌడ్ డేటా సోర్స్ సెట్టింగ్స్**

Azure AI Studio/Azure Machine Learning Service యొక్క datastore ను లింక్ చేయడం ద్వారా క్లౌడ్‌లోని డేటాను లింక్ చేయగలరు, మీరు Microsoft Fabric మరియు Azure Data ద్వారా Azure AI Studio/Azure Machine Learning Service కు వివిధ డేటా సోర్సులను పరిచయం చేయడానికి ఎంచుకోవచ్చు, ఇది ఫైన్‑ట్యూనింగ్ డేటాకు మద్దతుగా ఉంటుంది.

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

**2. కంప్యూటింగ్ కాన్ఫిగరేషన్**

మీరు స్థానికంగా ఉండాల్సిన అవసరం ఉంటే, మీరు నేరుగా స్థానిక డేటా వనరులను ఉపయోగించవచ్చు. మీరు Azure AI Studio / Azure Machine Learning Service వనరులను ఉపయోగించాలనుకుంటే సంబంధిత Azure పారామీటర్లు, కంప్యూటింగ్ పవర్ పేరు మొదలైన వాటిని కాన్ఫిగర్ చేయాల్సి ఉంటుంది.

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

***గమనిక***

Azure AI Studio/Azure Machine Learning Service పై కంటైనర్ ద్వారా నడిచే కారణంగా, అవసరమైన ఎన్విరాన్‌మెంట్‌ను కాన్ఫిగర్ చేయాల్సి ఉంటుంది. ఇది conda.yaml ఎన్విరాన్‌మెంట్‌లో కాన్ఫిగర్ చేయబడుతుంది.

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

**3. మీ SLMని ఎంచుకోండి**

మీరు మోడల్‌ను నేరుగా Hugging Face నుండి ఉపయోగించవచ్చు, లేదా మీరు Azure AI Studio / Azure Machine Learning యొక్క Model Catalogతో నేరుగా కాంబైన్ చేసి ఉపయోగించవలసిన మోడల్‌ను ఎంచుకోవచ్చు. కింది కోడ్ ఉదాహరణలో మేము Microsoft Phi-3-mini ను ఉదాహరణగా ఉపయోగిస్తాము.

మీ వద్ద మోడల్ స్థానికంగా ఉంటే, మీరు ఈ పద్ధతి ఉపయోగించవచ్చు

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

If you want to use a model from Azure AI Studio / Azure Machine Learning Service, you can use this method


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

**గమనిక:**
Azure AI Studio / Azure Machine Learning Service తో ఇంటిగ్రేట్ చేయాల్సిన అవసరం ఉంది, కాబట్టి మోడల్ సెటప్ చేస్తున్నప్పుడు వెర్షన్ నంబర్ మరియు సంబంధిత నేమింగ్‌ను దయచేసి పరిశీలించండి.

Azure పై ఉన్న అన్ని మోడళ్లను PyTorch.MLflow గా సెట్ చేయాల్సి ఉంటుంది

మీకు Hugging Face ఖాతా ఉండి, కీని Azure AI Studio / Azure Machine Learning లోని Key value కి బైండింగ్ చేయాలి

**4. అల్గోరిథం**

Microsoft Olive Lora మరియు QLora ఫైన్‑ట్యూనింగ్ అల్గోరిథంలను బాగా ఇన్క్యాప్సులేట్ చేసి ఉంటుంది. మీరే కాన్ఫిగర్ చేయాల్సింది కొన్ని సంబంధిత పారామీటర్లు మాత్రమే. ఇక్కడ నేను QLora ను ఉదాహరణగా తీసుకుంటాను.

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

If you want quantization conversion, Microsoft Olive main branch already supports the onnxruntime-genai method. You can set it according to your needs：

1. అడాప్టర్ వెయిట్స్‌ను బేస్ మోడల్‌లో విలీనం చేయండి
2. ModelBuilder ద్వారా అవసరమైన ప్రెసిషన్‌తో మోడల్‌ను onnx మోడల్‌గా కన్వర్ట్ చేయండి

ఉదాహరణకు క్వాంటైజ్ చేయబడిన INT4 గా మార్చడం వంటి

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

**గమనిక** 
- మీరు QLoRA ఉపయోగిస్తే, ONNXRuntime-genai యొక్క క్వాంటైజేషన్ మార్పిడి ప్రస్తుతానికి మద్దతు ఇవ్వబడలేదు.

- ఇక్కడ వెళ్తే మీరు పై స్టెప్పులు మీ అవసరాల ప్రకారం సెట్ చేయవచ్చు. పై పేర్కొన్న అన్ని స్టెప్పులను పూర్తిగా అమర్చవలసిన అవసరం లేదు. మీ అవసరాలపై ఆధారపడి, మీరు ఫైన్‑ట్యూనింగ్ లేకుండా నేరుగా ఆల్గోరిథం స్టెప్పులను ఉపయోగించవచ్చు. చివరగా మీరు సంబంధిత ఇంజిన్లను కాన్ఫిగర్ చేయాల్సి ఉంటుంది

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

**5. ఫైన్‑ట్యూనింగ్ పూర్తయింది**

కమాండ్ లైన్‌లో, olive-config.json ఉన్న డైరెక్టరీలో క్రింది ఆదేశాన్ని అమలు చేయండి

```bash
olive run --config olive-config.json  
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యత మినహాయింపు:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వం కోసం శ్రద్ధ వహించ అయినప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా అపక్ర‌మాలు ఉండవచ్చని దయచేసి గమనించండి. మౌలిక భాషలోని అసలు పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. మూల్యమైన సమాచారం కోసం వృత్తిపరమైన మానవ అనువాదాన్ని సూచించబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుడు భావాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->