<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:41:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "ko"
}
-->
# **Microsoft Olive로 Phi-3 미세 조정하기**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo)는 모델 압축, 최적화, 컴파일 분야의 업계 선도 기술을 한데 모은 사용하기 쉬운 하드웨어 인식 모델 최적화 도구입니다.

특정 하드웨어 아키텍처를 최대한 효율적으로 활용할 수 있도록 머신러닝 모델 최적화 과정을 간소화하도록 설계되었습니다.

클라우드 기반 애플리케이션이든 엣지 디바이스든, Olive를 사용하면 모델을 손쉽고 효과적으로 최적화할 수 있습니다.

## 주요 기능:
- Olive는 원하는 하드웨어 타겟에 맞춘 최적화 기법을 집약하고 자동화합니다.
- 모든 상황에 맞는 단일 최적화 기법은 없기 때문에, Olive는 업계 전문가들이 자신만의 최적화 혁신을 플러그인할 수 있도록 확장성을 제공합니다.

## 엔지니어링 노력 절감:
- 개발자들은 종종 훈련된 모델을 배포하기 위해 여러 하드웨어 벤더별 툴체인을 배우고 활용해야 합니다.
- Olive는 원하는 하드웨어에 맞춘 최적화 기법을 자동화하여 이 과정을 단순화합니다.

## 바로 사용 가능한 E2E 최적화 솔루션:

통합된 기법을 조합하고 조율하여 Olive는 엔드 투 엔드 최적화를 위한 통합 솔루션을 제공합니다.
정확도와 지연 시간 같은 제약 조건을 고려하면서 모델을 최적화합니다.

## Microsoft Olive를 사용한 미세 조정

Microsoft Olive는 생성형 인공지능 분야에서 미세 조정과 참조 모두를 지원하는 매우 사용하기 쉬운 오픈 소스 모델 최적화 도구입니다. 간단한 설정만으로, 오픈 소스 소형 언어 모델과 관련 런타임 환경(AzureML / 로컬 GPU, CPU, DirectML)을 결합해 자동 최적화를 통해 모델의 미세 조정 또는 참조를 완료할 수 있으며, 클라우드 또는 엣지 디바이스에 배포할 최적의 모델을 찾을 수 있습니다. 이를 통해 기업은 온프레미스와 클라우드에서 자체 산업별 모델을 구축할 수 있습니다.

![intro](../../../../translated_images/intro.46086a3f16ec48e2.ko.png)

## Microsoft Olive로 Phi-3 미세 조정하기

![FinetuningwithOlive](../../../../translated_images/olivefinetune.76d09e9b68253681.ko.png)

## Phi-3 Olive 샘플 코드 및 예제
이 예제에서는 Olive를 사용하여:

- LoRA 어댑터를 미세 조정해 문구를 슬픔, 기쁨, 두려움, 놀라움으로 분류합니다.
- 어댑터 가중치를 기본 모델에 병합합니다.
- 모델을 최적화하고 int4로 양자화합니다.

[샘플 코드](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive 설치

Microsoft Olive 설치는 매우 간단하며 CPU, GPU, DirectML, Azure ML용으로도 설치할 수 있습니다.

```bash
pip install olive-ai
```

CPU에서 ONNX 모델을 실행하려면 다음을 사용할 수 있습니다.

```bash
pip install olive-ai[cpu]
```

GPU에서 ONNX 모델을 실행하려면 다음을 사용할 수 있습니다.

```python
pip install olive-ai[gpu]
```

Azure ML을 사용하려면 다음을 사용하세요.

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**알림**  
운영체제 요구사항: Ubuntu 20.04 / 22.04

### **Microsoft Olive의 Config.json**

설치 후 Config 파일을 통해 데이터, 컴퓨팅, 학습, 배포, 모델 생성 등 다양한 모델별 설정을 구성할 수 있습니다.

**1. 데이터**

Microsoft Olive는 로컬 데이터와 클라우드 데이터 모두에서 학습을 지원하며, 설정에서 구성할 수 있습니다.

*로컬 데이터 설정*

미세 조정을 위해 학습할 데이터셋을 간단히 설정할 수 있으며, 보통 json 형식으로 데이터 템플릿에 맞게 조정합니다. 이는 모델 요구사항에 따라 조정해야 합니다(예: Microsoft Phi-3-mini가 요구하는 형식에 맞게 조정). 다른 모델을 사용하는 경우 해당 모델의 미세 조정 형식을 참고하세요.

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

**클라우드 데이터 소스 설정**

Azure AI Studio/Azure Machine Learning Service의 데이터 저장소를 연결해 클라우드 내 데이터를 연동할 수 있으며, Microsoft Fabric과 Azure Data를 통해 다양한 데이터 소스를 Azure AI Studio/Azure Machine Learning Service에 도입해 미세 조정 데이터로 활용할 수 있습니다.

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

**2. 컴퓨팅 구성**

로컬에서 실행하려면 로컬 데이터 리소스를 직접 사용할 수 있습니다. Azure AI Studio / Azure Machine Learning Service 리소스를 사용하려면 관련 Azure 파라미터, 컴퓨팅 이름 등을 설정해야 합니다.

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

***알림***

Azure AI Studio/Azure Machine Learning Service에서 컨테이너로 실행되므로 필요한 환경을 conda.yaml 환경에서 구성해야 합니다.

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

**3. SLM 선택**

Hugging Face에서 직접 모델을 사용하거나 Azure AI Studio / Azure Machine Learning의 모델 카탈로그와 연동해 사용할 모델을 선택할 수 있습니다. 아래 코드 예제에서는 Microsoft Phi-3-mini를 예로 듭니다.

로컬에 모델이 있다면 다음 방법을 사용할 수 있습니다.

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

Azure AI Studio / Azure Machine Learning Service에서 모델을 사용하려면 다음 방법을 사용하세요.

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

**알림:**  
Azure AI Studio / Azure Machine Learning Service와 연동해야 하므로 모델 설정 시 버전 번호와 관련 명칭을 참고하세요.

Azure의 모든 모델은 PyTorch.MLflow로 설정해야 합니다.

Hugging Face 계정이 필요하며, 키를 Azure AI Studio / Azure Machine Learning의 Key 값에 바인딩해야 합니다.

**4. 알고리즘**

Microsoft Olive는 Lora와 QLora 미세 조정 알고리즘을 잘 캡슐화했습니다. 관련 파라미터만 설정하면 됩니다. 여기서는 QLora를 예로 듭니다.

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

양자화 변환을 원한다면 Microsoft Olive 메인 브랜치에서 onnxruntime-genai 방식을 지원합니다. 필요에 따라 설정할 수 있습니다:

1. 어댑터 가중치를 기본 모델에 병합  
2. ModelBuilder를 사용해 원하는 정밀도로 모델을 onnx 모델로 변환

예를 들어 INT4 양자화 변환

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

**알림**  
- QLoRA를 사용하는 경우 ONNXRuntime-genai의 양자화 변환은 현재 지원되지 않습니다.  
- 위 단계는 필요에 따라 설정할 수 있으며, 반드시 모두 구성할 필요는 없습니다. 필요에 따라 미세 조정 없이 알고리즘 단계만 사용할 수도 있습니다. 마지막으로 관련 엔진을 설정하면 됩니다.

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

**5. 미세 조정 완료**

명령줄에서 olive-config.json 파일이 있는 디렉터리에서 실행하세요.

```bash
olive run --config olive-config.json  
```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.