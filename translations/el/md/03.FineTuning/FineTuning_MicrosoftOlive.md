<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5764be88ad2eb4f341e742eb8f14fab1",
  "translation_date": "2025-07-17T06:45:04+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MicrosoftOlive.md",
  "language_code": "el"
}
-->
# **Fine-tuning του Phi-3 με το Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) είναι ένα εύχρηστο εργαλείο βελτιστοποίησης μοντέλων με επίγνωση του υλικού, που συνδυάζει κορυφαίες τεχνικές της βιομηχανίας σε συμπίεση, βελτιστοποίηση και μεταγλώττιση μοντέλων.

Έχει σχεδιαστεί για να απλοποιεί τη διαδικασία βελτιστοποίησης μοντέλων μηχανικής μάθησης, εξασφαλίζοντας την πιο αποδοτική χρήση συγκεκριμένων αρχιτεκτονικών υλικού.

Είτε εργάζεστε σε εφαρμογές στο cloud είτε σε συσκευές άκρου, το Olive σας επιτρέπει να βελτιστοποιείτε τα μοντέλα σας εύκολα και αποτελεσματικά.

## Κύρια Χαρακτηριστικά:
- Το Olive συγκεντρώνει και αυτοματοποιεί τεχνικές βελτιστοποίησης για τους επιθυμητούς στόχους υλικού.
- Καμία μεμονωμένη τεχνική βελτιστοποίησης δεν ταιριάζει σε όλα τα σενάρια, γι’ αυτό το Olive επιτρέπει την επεκτασιμότητα δίνοντας τη δυνατότητα σε ειδικούς του κλάδου να ενσωματώνουν τις δικές τους καινοτομίες βελτιστοποίησης.

## Μείωση Μηχανικού Κόπου:
- Οι προγραμματιστές συχνά χρειάζεται να μάθουν και να χρησιμοποιήσουν πολλαπλές αλυσίδες εργαλείων ειδικές για κάθε προμηθευτή υλικού, προκειμένου να προετοιμάσουν και να βελτιστοποιήσουν εκπαιδευμένα μοντέλα για ανάπτυξη.
- Το Olive απλοποιεί αυτή την εμπειρία αυτοματοποιώντας τις τεχνικές βελτιστοποίησης για το επιθυμητό υλικό.

## Έτοιμη για Χρήση Λύση Βελτιστοποίησης E2E:

Συνθέτοντας και ρυθμίζοντας ενσωματωμένες τεχνικές, το Olive προσφέρει μια ενιαία λύση για βελτιστοποίηση από άκρο σε άκρο.
Λαμβάνει υπόψη περιορισμούς όπως ακρίβεια και καθυστέρηση κατά τη βελτιστοποίηση των μοντέλων.

## Χρήση του Microsoft Olive για fine-tuning

Το Microsoft Olive είναι ένα πολύ εύχρηστο εργαλείο ανοιχτού κώδικα για βελτιστοποίηση μοντέλων που καλύπτει τόσο το fine-tuning όσο και την αναφορά στον τομέα της γενετικής τεχνητής νοημοσύνης. Απαιτεί μόνο απλή διαμόρφωση, σε συνδυασμό με τη χρήση ανοιχτών μικρών γλωσσικών μοντέλων και σχετικών περιβαλλόντων εκτέλεσης (AzureML / τοπικό GPU, CPU, DirectML), μπορείτε να ολοκληρώσετε το fine-tuning ή την αναφορά του μοντέλου μέσω αυτόματης βελτιστοποίησης και να βρείτε το καλύτερο μοντέλο για ανάπτυξη στο cloud ή σε συσκευές άκρου. Επιτρέπει στις επιχειρήσεις να δημιουργήσουν τα δικά τους μοντέλα για κάθετα βιομηχανικά πεδία τόσο on-premises όσο και στο cloud.

![intro](../../../../translated_images/intro.46086a3f16ec48e2.el.png)

## Fine Tuning του Phi-3 με το Microsoft Olive

![FinetuningwithOlive](../../../../translated_images/olivefinetune.76d09e9b68253681.el.png)

## Παράδειγμα Κώδικα και Χρήσης του Phi-3 Olive
Σε αυτό το παράδειγμα θα χρησιμοποιήσετε το Olive για:

- Fine-tune ενός LoRA adapter για ταξινόμηση φράσεων σε Sad, Joy, Fear, Surprise.
- Συγχώνευση των βαρών του adapter στο βασικό μοντέλο.
- Βελτιστοποίηση και ποσοτικοποίηση του μοντέλου σε int4.

[Παράδειγμα Κώδικα](../../code/03.Finetuning/olive-ort-example/README.md)

### Εγκατάσταση του Microsoft Olive

Η εγκατάσταση του Microsoft Olive είναι πολύ απλή και μπορεί να εγκατασταθεί για CPU, GPU, DirectML και Azure ML

```bash
pip install olive-ai
```

Αν θέλετε να τρέξετε ένα μοντέλο ONNX με CPU, μπορείτε να χρησιμοποιήσετε

```bash
pip install olive-ai[cpu]
```

Αν θέλετε να τρέξετε ένα μοντέλο ONNX με GPU, μπορείτε να χρησιμοποιήσετε

```python
pip install olive-ai[gpu]
```

Αν θέλετε να χρησιμοποιήσετε Azure ML, χρησιμοποιήστε

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Σημείωση**  
Απαιτήσεις λειτουργικού: Ubuntu 20.04 / 22.04

### **Config.json του Microsoft Olive**

Μετά την εγκατάσταση, μπορείτε να διαμορφώσετε διάφορες ρυθμίσεις ειδικές για το μοντέλο μέσω του αρχείου Config, συμπεριλαμβανομένων δεδομένων, υπολογιστικής ισχύος, εκπαίδευσης, ανάπτυξης και δημιουργίας μοντέλου.

**1. Δεδομένα**

Στο Microsoft Olive, υποστηρίζεται η εκπαίδευση με τοπικά και δεδομένα cloud, και μπορεί να ρυθμιστεί στις ρυθμίσεις.

*Ρυθμίσεις τοπικών δεδομένων*

Μπορείτε απλά να ορίσετε το σύνολο δεδομένων που χρειάζεται για fine-tuning, συνήθως σε μορφή json, και να το προσαρμόσετε με το πρότυπο δεδομένων. Αυτό πρέπει να προσαρμοστεί ανάλογα με τις απαιτήσεις του μοντέλου (π.χ. προσαρμογή στη μορφή που απαιτεί το Microsoft Phi-3-mini. Αν έχετε άλλα μοντέλα, παρακαλούμε ανατρέξτε στις απαιτούμενες μορφές fine-tuning άλλων μοντέλων για επεξεργασία)

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

**Ρυθμίσεις πηγής δεδομένων cloud**

Συνδέοντας το datastore του Azure AI Studio/Azure Machine Learning Service για πρόσβαση σε δεδομένα στο cloud, μπορείτε να επιλέξετε να εισάγετε διαφορετικές πηγές δεδομένων στο Azure AI Studio/Azure Machine Learning Service μέσω Microsoft Fabric και Azure Data ως υποστήριξη για fine-tuning.

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

**2. Ρυθμίσεις υπολογιστικής ισχύος**

Αν χρειάζεστε τοπικά, μπορείτε να χρησιμοποιήσετε απευθείας τοπικούς πόρους δεδομένων. Αν χρειάζεστε πόρους του Azure AI Studio / Azure Machine Learning Service, πρέπει να ρυθμίσετε τις σχετικές παραμέτρους Azure, το όνομα υπολογιστικής ισχύος κ.ά.

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

***Σημείωση***

Επειδή τρέχει μέσω container στο Azure AI Studio/Azure Machine Learning Service, πρέπει να ρυθμιστεί το απαιτούμενο περιβάλλον. Αυτό γίνεται στο αρχείο conda.yaml.

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

**3. Επιλογή του SLM σας**

Μπορείτε να χρησιμοποιήσετε το μοντέλο απευθείας από το Hugging face, ή να το συνδυάσετε με το Model Catalog του Azure AI Studio / Azure Machine Learning για να επιλέξετε το μοντέλο που θα χρησιμοποιήσετε. Στο παράδειγμα κώδικα παρακάτω θα χρησιμοποιήσουμε το Microsoft Phi-3-mini ως παράδειγμα.

Αν έχετε το μοντέλο τοπικά, μπορείτε να χρησιμοποιήσετε αυτή τη μέθοδο

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

Αν θέλετε να χρησιμοποιήσετε μοντέλο από το Azure AI Studio / Azure Machine Learning Service, μπορείτε να χρησιμοποιήσετε αυτή τη μέθοδο

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

**Σημείωση:**  
Πρέπει να γίνει ενσωμάτωση με το Azure AI Studio / Azure Machine Learning Service, οπότε κατά τη ρύθμιση του μοντέλου παρακαλούμε ανατρέξτε στον αριθμό έκδοσης και τα σχετικά ονόματα.

Όλα τα μοντέλα στο Azure πρέπει να είναι ρυθμισμένα σε PyTorch.MLflow

Πρέπει να έχετε λογαριασμό Hugging face και να συνδέσετε το κλειδί με την τιμή Key του Azure AI Studio / Azure Machine Learning

**4. Αλγόριθμος**

Το Microsoft Olive ενσωματώνει πολύ καλά τους αλγορίθμους fine-tuning Lora και QLora. Το μόνο που χρειάζεται να ρυθμίσετε είναι κάποιες σχετικές παραμέτρους. Εδώ παίρνω ως παράδειγμα το QLora.

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

Αν θέλετε μετατροπή ποσοτικοποίησης, ο κύριος κλάδος του Microsoft Olive υποστηρίζει ήδη τη μέθοδο onnxruntime-genai. Μπορείτε να το ρυθμίσετε ανάλογα με τις ανάγκες σας:

1. συγχώνευση των βαρών του adapter στο βασικό μοντέλο  
2. Μετατροπή του μοντέλου σε onnx με την απαιτούμενη ακρίβεια μέσω ModelBuilder

όπως μετατροπή σε ποσοτικοποιημένο INT4

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

**Σημείωση**  
- Αν χρησιμοποιείτε QLoRA, η μετατροπή ποσοτικοποίησης με ONNXRuntime-genai δεν υποστηρίζεται προς το παρόν.

- Αξίζει να σημειωθεί ότι μπορείτε να ρυθμίσετε τα παραπάνω βήματα ανάλογα με τις ανάγκες σας. Δεν είναι απαραίτητο να διαμορφώσετε πλήρως όλα τα παραπάνω βήματα. Ανάλογα με τις ανάγκες σας, μπορείτε να χρησιμοποιήσετε απευθείας τα βήματα του αλγορίθμου χωρίς fine-tuning. Τέλος, πρέπει να ρυθμίσετε τους σχετικούς μηχανισμούς.

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

**5. Ολοκλήρωση fine-tuning**

Στη γραμμή εντολών, εκτελέστε στον φάκελο που βρίσκεται το olive-config.json

```bash
olive run --config olive-config.json  
```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.