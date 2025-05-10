<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-05-09T20:50:56+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "pl"
}
-->
# **Dostrajanie Phi-3 za pomocą Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) to łatwe w użyciu narzędzie do optymalizacji modeli z uwzględnieniem sprzętu, które łączy w sobie najlepsze techniki z zakresu kompresji, optymalizacji i kompilacji modeli.

Zostało zaprojektowane, aby usprawnić proces optymalizacji modeli uczenia maszynowego, zapewniając ich maksymalnie efektywne wykorzystanie na określonych architekturach sprzętowych.

Niezależnie od tego, czy pracujesz nad aplikacjami w chmurze, czy na urządzeniach brzegowych, Olive umożliwia łatwą i skuteczną optymalizację modeli.

## Kluczowe funkcje:
- Olive agreguje i automatyzuje techniki optymalizacji dla wybranych celów sprzętowych.
- Nie istnieje jedna uniwersalna technika optymalizacji dla wszystkich scenariuszy, dlatego Olive pozwala na rozszerzalność, umożliwiając ekspertom z branży wprowadzanie własnych innowacji optymalizacyjnych.

## Zmniejsz wysiłek inżynieryjny:
- Programiści często muszą poznać i korzystać z różnych narzędzi specyficznych dla dostawców sprzętu, aby przygotować i zoptymalizować wytrenowane modele do wdrożenia.
- Olive upraszcza ten proces, automatyzując techniki optymalizacji dla wybranego sprzętu.

## Gotowe rozwiązanie do kompleksowej optymalizacji:

Poprzez komponowanie i dostrajanie zintegrowanych technik, Olive oferuje zunifikowane rozwiązanie do kompleksowej optymalizacji.
Uwzględnia ograniczenia takie jak dokładność i opóźnienie podczas optymalizacji modeli.

## Korzystanie z Microsoft Olive do dostrajania

Microsoft Olive to bardzo łatwe w użyciu otwarte narzędzie do optymalizacji modeli, które może obejmować zarówno dostrajanie, jak i referencję w obszarze generatywnej sztucznej inteligencji. Wymaga jedynie prostej konfiguracji, a w połączeniu z otwartymi modelami małych języków i odpowiednimi środowiskami uruchomieniowymi (AzureML / lokalne GPU, CPU, DirectML) pozwala na automatyczne dostrajanie lub referencję modelu oraz znalezienie najlepszego modelu do wdrożenia w chmurze lub na urządzeniach brzegowych. Umożliwia to firmom tworzenie własnych, branżowych modeli pionowych zarówno lokalnie, jak i w chmurze.

![intro](../../../../translated_images/intro.dcc44a1aafcf58bf979b9a69384ffea98b5b599ac034dde94937a94a29260332.pl.png)

## Dostrajanie Phi-3 za pomocą Microsoft Olive

![FinetuningwithOlive](../../../../translated_images/olivefinetune.7a9c66b3310981030c47cf637befed8fa1ea1acd0f5acec5ac090a8f3f904a45.pl.png)

## Przykładowy kod i przykład Phi-3 Olive
W tym przykładzie użyjesz Olive do:

- Dostrojenia adaptera LoRA do klasyfikacji fraz na Smutek, Radość, Strach, Zaskoczenie.
- Połączenia wag adaptera z modelem bazowym.
- Optymalizacji i kwantyzacji modelu do int4.

[Sample Code](../../code/03.Finetuning/olive-ort-example/README.md)

### Instalacja Microsoft Olive

Instalacja Microsoft Olive jest bardzo prosta i może być wykonana dla CPU, GPU, DirectML oraz Azure ML

```bash
pip install olive-ai
```

Jeśli chcesz uruchomić model ONNX na CPU, możesz użyć

```bash
pip install olive-ai[cpu]
```

Jeśli chcesz uruchomić model ONNX na GPU, możesz użyć

```python
pip install olive-ai[gpu]
```

Jeśli chcesz korzystać z Azure ML, użyj

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Uwaga**
Wymagania systemowe: Ubuntu 20.04 / 22.04

### **Plik Config.json Microsoft Olive**

Po instalacji możesz skonfigurować różne ustawienia specyficzne dla modelu za pomocą pliku Config, obejmujące dane, obliczenia, trening, wdrożenie i generowanie modeli.

**1. Dane**

W Microsoft Olive możliwe jest trenowanie na danych lokalnych oraz w chmurze, co można ustawić w konfiguracji.

*Ustawienia danych lokalnych*

Możesz łatwo ustawić zbiór danych do treningu dla dostrajania, zwykle w formacie json, i dostosować go do szablonu danych. Trzeba to dostosować w zależności od wymagań modelu (np. do formatu wymaganego przez Microsoft Phi-3-mini. Jeśli masz inne modele, zapoznaj się z wymaganymi formatami dostrajania dla tych modeli).

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

**Ustawienia źródła danych w chmurze**

Poprzez połączenie magazynu danych Azure AI Studio/Azure Machine Learning Service możesz importować dane z chmury. Możesz wybrać różne źródła danych w Azure AI Studio/Azure Machine Learning Service korzystając z Microsoft Fabric i Azure Data jako wsparcia dla danych do dostrajania.

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

**2. Konfiguracja obliczeń**

Jeśli chcesz korzystać z zasobów lokalnych, możesz użyć lokalnych danych. Aby korzystać z zasobów Azure AI Studio / Azure Machine Learning Service, musisz skonfigurować odpowiednie parametry Azure, nazwę mocy obliczeniowej itp.

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

***Uwaga***

Ponieważ uruchomienie odbywa się w kontenerze na Azure AI Studio/Azure Machine Learning Service, konieczne jest skonfigurowanie wymaganego środowiska. Odbywa się to w pliku conda.yaml.

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

**3. Wybierz swój SLM**

Możesz użyć modelu bezpośrednio z Hugging Face lub połączyć go z katalogiem modeli Azure AI Studio / Azure Machine Learning, aby wybrać model do użycia. W poniższym przykładzie kodu używamy Microsoft Phi-3-mini.

Jeśli masz model lokalnie, możesz użyć tej metody

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

Jeśli chcesz użyć modelu z Azure AI Studio / Azure Machine Learning Service, możesz użyć tej metody

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

**Uwaga:**
Musimy zintegrować się z Azure AI Studio / Azure Machine Learning Service, dlatego podczas konfiguracji modelu zwróć uwagę na numer wersji i powiązane nazwy.

Wszystkie modele na Azure muszą być ustawione jako PyTorch.MLflow

Musisz posiadać konto na Hugging Face i powiązać klucz z wartością klucza w Azure AI Studio / Azure Machine Learning

**4. Algorytm**

Microsoft Olive bardzo dobrze opakowuje algorytmy dostrajania Lora i QLora. Wystarczy skonfigurować kilka powiązanych parametrów. Tutaj jako przykład podaję QLora.

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

Jeśli chcesz wykonać konwersję kwantyzacji, główna gałąź Microsoft Olive już wspiera metodę onnxruntime-genai. Możesz ustawić ją według własnych potrzeb:

1. scal adapter weights z modelem bazowym
2. przekonwertuj model do onnx z wymaganą precyzją za pomocą ModelBuilder

np. konwersja do skwantyzowanego INT4

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

**Uwaga**  
- Jeśli używasz QLoRA, konwersja kwantyzacji ONNXRuntime-genai nie jest na razie wspierana.

- Warto zaznaczyć, że powyższe kroki można ustawić według własnych potrzeb. Nie ma konieczności kompletnego konfigurowania wszystkich tych kroków. W zależności od potrzeb możesz użyć bezpośrednio kroków algorytmu bez dostrajania. Na końcu musisz skonfigurować odpowiednie silniki.

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

**5. Zakończenie dostrajania**

Na linii poleceń wykonaj w katalogu z olive-config.json

```bash
olive run --config olive-config.json  
```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.