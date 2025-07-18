<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:40:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "ja"
}
-->
# **Microsoft OliveによるPhi-3のファインチューニング**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo)は、モデル圧縮、最適化、コンパイルにおける業界最先端の技術を統合した、使いやすいハードウェア対応のモデル最適化ツールです。

特定のハードウェアアーキテクチャを最大限に活用できるよう、機械学習モデルの最適化プロセスを効率化することを目的としています。

クラウドベースのアプリケーションでもエッジデバイスでも、Oliveを使えばモデルの最適化を簡単かつ効果的に行えます。

## 主な特徴：
- Oliveは、対象ハードウェア向けの最適化技術を集約し自動化します。
- すべてのシナリオに適した単一の最適化技術は存在しないため、業界の専門家が独自の最適化技術を組み込める拡張性を備えています。

## エンジニアリング工数の削減：
- 開発者は通常、複数のハードウェアベンダー固有のツールチェーンを学び、訓練済みモデルの展開準備と最適化を行う必要があります。
- Oliveは、対象ハードウェア向けの最適化技術を自動化することで、この作業を簡素化します。

## すぐに使えるエンドツーエンドの最適化ソリューション：

統合された技術を組み合わせて調整することで、Oliveはエンドツーエンドの最適化を一元的に提供します。
精度やレイテンシなどの制約を考慮しながらモデルを最適化します。

## Microsoft Oliveを使ったファインチューニング

Microsoft Oliveは非常に使いやすいオープンソースのモデル最適化ツールで、生成系AI分野におけるファインチューニングとリファレンスの両方をカバーできます。簡単な設定だけで、オープンソースの小型言語モデルや関連するランタイム環境（AzureML / ローカルGPU、CPU、DirectML）と組み合わせて、自動最適化によりモデルのファインチューニングやリファレンスを完了し、クラウドやエッジデバイスに展開する最適なモデルを見つけられます。企業がオンプレミスやクラウド上で独自の業界特化モデルを構築することを可能にします。

![intro](../../../../translated_images/intro.46086a3f16ec48e273c5ec11ec23b0dd23593dbab951e95d565145b40e8571a5.ja.png)

## Microsoft OliveによるPhi-3のファインチューニング

![FinetuningwithOlive](../../../../translated_images/olivefinetune.76d09e9b68253681cff9564145ddbf6d335cbcd7a79f4886b4120380deaa384f.ja.png)

## Phi-3 Olive サンプルコードと例
この例では、Oliveを使って以下を行います：

- LoRAアダプターをファインチューニングし、フレーズをSad、Joy、Fear、Surpriseに分類
- アダプターの重みをベースモデルにマージ
- モデルをint4に最適化・量子化

[サンプルコード](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Oliveのセットアップ

Microsoft Oliveのインストールは非常に簡単で、CPU、GPU、DirectML、Azure ML向けにもインストール可能です。

```bash
pip install olive-ai
```

CPUでONNXモデルを実行したい場合は以下を使用できます。

```bash
pip install olive-ai[cpu]
```

GPUでONNXモデルを実行したい場合は以下を使用できます。

```python
pip install olive-ai[gpu]
```

Azure MLを使いたい場合は以下を使用してください。

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**注意**
対応OS：Ubuntu 20.04 / 22.04

### **Microsoft OliveのConfig.json**

インストール後、Configファイルを通じてデータ、計算、トレーニング、展開、モデル生成など、モデル固有の設定を行えます。

**1. データ**

Microsoft Oliveでは、ローカルデータとクラウドデータの両方でのトレーニングをサポートしており、設定で指定可能です。

*ローカルデータ設定*

ファインチューニングに必要なデータセットをjson形式で簡単に設定し、データテンプレートに合わせて調整します。モデルの要件に応じて調整が必要です（例：Microsoft Phi-3-miniが要求する形式に適合させる。その他のモデルの場合は、それぞれのファインチューニング形式を参照してください）

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

**クラウドデータソース設定**

Azure AI Studio/Azure Machine Learning Serviceのデータストアを連携し、Microsoft FabricやAzure Dataを通じて異なるデータソースをAzure AI Studio/Azure Machine Learning Serviceに取り込み、ファインチューニング用のデータとして利用できます。

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

**2. 計算設定**

ローカルで実行する場合はローカルのデータリソースを直接使用できます。Azure AI Studio / Azure Machine Learning Serviceのリソースを使う場合は、関連するAzureパラメータや計算リソース名などを設定する必要があります。

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

***注意***

Azure AI Studio/Azure Machine Learning Service上のコンテナで実行されるため、必要な環境はconda.yamlで設定します。

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

**3. SLMの選択**

Hugging Faceから直接モデルを使うことも、Azure AI Studio / Azure Machine Learningのモデルカタログと連携してモデルを選択することも可能です。以下のコード例ではMicrosoft Phi-3-miniを例にします。

ローカルにモデルがある場合は以下の方法を使えます。

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

Azure AI Studio / Azure Machine Learning Serviceのモデルを使いたい場合は以下の方法を使います。

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

**注意：**
Azure AI Studio / Azure Machine Learning Serviceと連携するため、モデル設定時にはバージョン番号や関連する名称を参照してください。

Azure上のすべてのモデルはPyTorch.MLflowに設定する必要があります。

Hugging Faceアカウントを持ち、Azure AI Studio / Azure Machine Learningのキーにバインドしてください。

**4. アルゴリズム**

Microsoft OliveはLoraとQLoraのファインチューニングアルゴリズムをうまくラップしています。設定すべきは関連パラメータのみです。ここではQLoraを例にします。

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

量子化変換を行いたい場合、Microsoft Oliveのメインブランチはonnxruntime-genai方式をサポートしています。必要に応じて以下のように設定できます：

1. アダプターの重みをベースモデルにマージ
2. ModelBuilderで必要な精度のonnxモデルに変換

例えば量子化されたINT4への変換など

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

**注意**  
- QLoRAを使う場合、現時点でONNXRuntime-genaiの量子化変換はサポートされていません。  
- 上記のステップは必要に応じて設定可能で、すべてを完全に設定する必要はありません。ニーズに応じてファインチューニングなしでアルゴリズムのステップだけを使うこともできます。最後に関連するエンジンを設定してください。

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

**5. ファインチューニング完了**

コマンドラインでolive-config.jsonのあるディレクトリで以下を実行します。

```bash
olive run --config olive-config.json  
```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。