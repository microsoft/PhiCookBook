<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:42:20+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "mr"
}
-->
# **Microsoft Olive सह Phi-3 चे फाइन-ट्यूनिंग**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) हा एक सोपा वापरता येणारा हार्डवेअर-आधारित मॉडेल ऑप्टिमायझेशन टूल आहे जो मॉडेल कंप्रेशन, ऑप्टिमायझेशन आणि कंपायलेशनमधील उद्योगातील आघाडीच्या तंत्रांचा समावेश करतो.

हा मशीन लर्निंग मॉडेल्स ऑप्टिमाइझ करण्याच्या प्रक्रियेला सुलभ करण्यासाठी डिझाइन केला गेला आहे, ज्यामुळे ते विशिष्ट हार्डवेअर आर्किटेक्चरचा अधिक कार्यक्षम वापर करू शकतात.

तुम्ही क्लाउड-आधारित अॅप्लिकेशन्सवर काम करत असाल किंवा एज डिव्हाइसेसवर, Olive तुम्हाला तुमचे मॉडेल सहज आणि प्रभावीपणे ऑप्टिमाइझ करण्याची परवानगी देते.

## मुख्य वैशिष्ट्ये:
- Olive इच्छित हार्डवेअर टार्गेटसाठी ऑप्टिमायझेशन तंत्रे एकत्र करते आणि स्वयंचलित करते.
- कोणतीही एकल ऑप्टिमायझेशन तंत्र सर्व परिस्थितींना लागू होत नाही, त्यामुळे Olive उद्योग तज्ञांना त्यांच्या ऑप्टिमायझेशन नवकल्पना जोडण्याची मुभा देते.

## अभियांत्रिकी प्रयत्न कमी करा:
- विकसकांना अनेक हार्डवेअर विक्रेता-विशिष्ट टूलचेन शिकावे लागतात आणि प्रशिक्षित मॉडेल्स तैनात करण्यासाठी ऑप्टिमाइझ करावे लागते.
- Olive या अनुभवाला सुलभ करते आणि इच्छित हार्डवेअर साठी ऑप्टिमायझेशन तंत्र स्वयंचलित करते.

## वापरायला तयार E2E ऑप्टिमायझेशन सोल्यूशन:

एकत्रित तंत्रांची रचना आणि ट्यूनिंग करून, Olive एंड-टू-एंड ऑप्टिमायझेशनसाठी एकसंध सोल्यूशन प्रदान करते.
ते अचूकता आणि विलंब यांसारख्या बंधनांचा विचार करून मॉडेल्स ऑप्टिमाइझ करते.

## Microsoft Olive वापरून फाइन-ट्यूनिंग

Microsoft Olive हा एक अतिशय सोपा वापरता येणारा ओपन सोर्स मॉडेल ऑप्टिमायझेशन टूल आहे जो जनरेटिव्ह आर्टिफिशियल इंटेलिजन्स क्षेत्रात फाइन-ट्यूनिंग आणि संदर्भ दोन्ही कव्हर करू शकतो. यासाठी फक्त सोपी कॉन्फिगरेशन आवश्यक आहे, ज्यात ओपन सोर्स लहान भाषा मॉडेल्स आणि संबंधित रनटाइम एन्व्हायर्नमेंट्स (AzureML / स्थानिक GPU, CPU, DirectML) चा वापर करून तुम्ही मॉडेलचे फाइन-ट्यूनिंग किंवा संदर्भ स्वयंचलित ऑप्टिमायझेशनद्वारे पूर्ण करू शकता, आणि क्लाउडवर किंवा एज डिव्हाइसेसवर तैनात करण्यासाठी सर्वोत्तम मॉडेल शोधू शकता. हे उद्योगांना त्यांच्या स्वतःच्या क्षेत्रीय मॉडेल्स ऑन-प्रिमायसेस आणि क्लाउडमध्ये तयार करण्याची परवानगी देते.

![intro](../../../../translated_images/mr/intro.46086a3f16ec48e2.webp)

## Microsoft Olive सह Phi-3 फाइन ट्यूनिंग

![FinetuningwithOlive](../../../../translated_images/mr/olivefinetune.76d09e9b68253681.webp)

## Phi-3 Olive नमुना कोड आणि उदाहरण
या उदाहरणात तुम्ही Olive वापरून:

- LoRA अ‍ॅडॉप्टर फाइन-ट्यून करून वाक्यांशांना Sad, Joy, Fear, Surprise मध्ये वर्गीकृत कराल.
- अ‍ॅडॉप्टरचे वजन बेस मॉडेलमध्ये मर्ज कराल.
- मॉडेलला int4 मध्ये ऑप्टिमाइझ आणि क्वांटाइज कराल.

[Sample Code](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive सेटअप करा

Microsoft Olive ची स्थापना खूप सोपी आहे, आणि CPU, GPU, DirectML, आणि Azure ML साठी देखील स्थापित केली जाऊ शकते.

```bash
pip install olive-ai
```

जर तुम्हाला CPU वर ONNX मॉडेल चालवायचे असेल, तर तुम्ही वापरू शकता

```bash
pip install olive-ai[cpu]
```

जर तुम्हाला GPU वर ONNX मॉडेल चालवायचे असेल, तर तुम्ही वापरू शकता

```python
pip install olive-ai[gpu]
```

जर तुम्हाला Azure ML वापरायचे असेल, तर वापरा

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**सूचना**
ऑपरेटिंग सिस्टमची आवश्यकता: Ubuntu 20.04 / 22.04

### **Microsoft Olive चे Config.json**

स्थापनेनंतर, तुम्ही Config फाइलद्वारे वेगवेगळ्या मॉडेल-विशिष्ट सेटिंग्ज कॉन्फिगर करू शकता, ज्यात डेटा, संगणन, प्रशिक्षण, तैनाती, आणि मॉडेल जनरेशन यांचा समावेश आहे.

**1. डेटा**

Microsoft Olive वर स्थानिक डेटा आणि क्लाउड डेटा दोन्हीवर प्रशिक्षण दिले जाऊ शकते, आणि ते सेटिंग्जमध्ये कॉन्फिगर करता येते.

*स्थानिक डेटा सेटिंग्ज*

तुम्ही फाइन-ट्यूनिंगसाठी आवश्यक असलेला डेटा सेट सोप्या पद्धतीने सेट करू शकता, सहसा json फॉरमॅटमध्ये, आणि डेटा टेम्प्लेटशी जुळवून घेऊ शकता. हे मॉडेलच्या गरजेनुसार समायोजित करावे लागेल (उदाहरणार्थ, Microsoft Phi-3-mini साठी आवश्यक फॉरमॅटशी जुळवून घ्या. जर तुमच्याकडे इतर मॉडेल्स असतील, तर कृपया इतर मॉडेल्ससाठी आवश्यक फाइन-ट्यूनिंग फॉरमॅटसाठी संदर्भ घ्या)

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

**क्लाउड डेटा स्रोत सेटिंग्ज**

Azure AI Studio/Azure Machine Learning Service चा डेटास्टोर लिंक करून क्लाउडमधील डेटा लिंक करता येतो, तुम्ही Microsoft Fabric आणि Azure Data द्वारे Azure AI Studio/Azure Machine Learning Service मध्ये विविध डेटा स्रोत आणू शकता, जे फाइन-ट्यूनिंगसाठी डेटा सपोर्ट म्हणून वापरले जातात.

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

**2. संगणन कॉन्फिगरेशन**

जर तुम्हाला स्थानिक असायचे असेल, तर तुम्ही थेट स्थानिक डेटा संसाधने वापरू शकता. जर तुम्हाला Azure AI Studio / Azure Machine Learning Service चे संसाधने वापरायचे असतील, तर संबंधित Azure पॅरामीटर्स, संगणन शक्तीचे नाव इत्यादी कॉन्फिगर करावे लागेल.

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

***सूचना***

कारण हे Azure AI Studio/Azure Machine Learning Service वर कंटेनरद्वारे चालते, आवश्यक वातावरण कॉन्फिगर करणे गरजेचे आहे. हे conda.yaml एन्व्हायर्नमेंटमध्ये कॉन्फिगर केले जाते.

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

**3. तुमचा SLM निवडा**

तुम्ही मॉडेल थेट Hugging Face वरून वापरू शकता, किंवा Azure AI Studio / Azure Machine Learning च्या Model Catalog सोबत थेट जोडून वापरायचा मॉडेल निवडू शकता. खालील कोड उदाहरणात आपण Microsoft Phi-3-mini वापरणार आहोत.

जर तुमच्याकडे मॉडेल स्थानिक असेल, तर तुम्ही हा मार्ग वापरू शकता

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

जर तुम्हाला Azure AI Studio / Azure Machine Learning Service मधील मॉडेल वापरायचे असेल, तर हा मार्ग वापरा

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

**सूचना:**
आपल्याला Azure AI Studio / Azure Machine Learning Service सोबत एकत्रित करावे लागेल, त्यामुळे मॉडेल सेट करताना आवृत्ती क्रमांक आणि संबंधित नावांची नोंद घ्या.

Azure वरील सर्व मॉडेल्स PyTorch.MLflow मध्ये सेट केलेले असावेत.

तुमच्याकडे Hugging Face खाते असावे आणि Azure AI Studio / Azure Machine Learning च्या Key value शी की बाइंड केलेली असावी.

**4. अल्गोरिदम**

Microsoft Olive मध्ये Lora आणि QLora फाइन-ट्यूनिंग अल्गोरिदम चांगल्या प्रकारे समाविष्ट आहेत. तुम्हाला फक्त काही संबंधित पॅरामीटर्स कॉन्फिगर करायचे आहेत. येथे मी QLora चे उदाहरण घेतले आहे.

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

जर तुम्हाला क्वांटायझेशन रूपांतरण करायचे असेल, तर Microsoft Olive मुख्य शाखा आधीच onnxruntime-genai पद्धतला समर्थन देते. तुम्ही तुमच्या गरजेनुसार सेट करू शकता:

1. अ‍ॅडॉप्टरचे वजन बेस मॉडेलमध्ये मर्ज करा  
2. ModelBuilder द्वारे आवश्यक अचूकतेसह मॉडेल onnx मॉडेलमध्ये रूपांतरित करा

उदाहरणार्थ, क्वांटाइज्ड INT4 मध्ये रूपांतरित करणे

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

**सूचना**  
- जर तुम्ही QLoRA वापरत असाल, तर ONNXRuntime-genai चे क्वांटायझेशन रूपांतरण सध्या समर्थित नाही.  
- येथे नमूद करणे आवश्यक आहे की तुम्ही वरील पायऱ्या तुमच्या गरजेनुसार सेट करू शकता. वरील सर्व पायऱ्या पूर्णपणे कॉन्फिगर करणे आवश्यक नाही. तुमच्या गरजेनुसार, तुम्ही फाइन-ट्यूनिंगशिवाय थेट अल्गोरिदमच्या पायऱ्या वापरू शकता. शेवटी तुम्हाला संबंधित इंजिन कॉन्फिगर करावे लागतील.

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

**5. फाइन-ट्यूनिंग पूर्ण**

कमांड लाइनवर, olive-config.json च्या डायरेक्टरीमध्ये खालीलप्रमाणे चालवा

```bash
olive run --config olive-config.json  
```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.