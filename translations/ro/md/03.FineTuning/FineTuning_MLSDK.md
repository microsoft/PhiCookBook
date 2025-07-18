<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:44:46+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "ro"
}
-->
## Cum să folosești componentele chat-completion din registrul de sistem Azure ML pentru a ajusta un model

În acest exemplu vom realiza ajustarea modelului Phi-3-mini-4k-instruct pentru a completa o conversație între 2 persoane folosind setul de date ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.ro.png)

Exemplul îți va arăta cum să faci ajustarea folosind Azure ML SDK și Python, apoi cum să implementezi modelul ajustat la un endpoint online pentru inferență în timp real.

### Date de antrenament

Vom folosi setul de date ultrachat_200k. Acesta este o versiune puternic filtrată a setului UltraChat și a fost folosit pentru antrenarea modelului Zephyr-7B-β, un model de chat de ultimă generație cu 7 miliarde de parametri.

### Model

Vom folosi modelul Phi-3-mini-4k-instruct pentru a arăta cum utilizatorul poate ajusta un model pentru sarcina de chat-completion. Dacă ai deschis acest notebook dintr-un card de model specific, nu uita să înlocuiești numele modelului respectiv.

### Sarcini

- Alege un model pentru ajustare.
- Alege și explorează datele de antrenament.
- Configurează jobul de ajustare.
- Rulează jobul de ajustare.
- Revizuiește metricile de antrenament și evaluare.
- Înregistrează modelul ajustat.
- Implementează modelul ajustat pentru inferență în timp real.
- Curăță resursele.

## 1. Configurarea pre-rechizitelor

- Instalează dependențele
- Conectează-te la AzureML Workspace. Află mai multe la set up SDK authentication. Înlocuiește <WORKSPACE_NAME>, <RESOURCE_GROUP> și <SUBSCRIPTION_ID> de mai jos.
- Conectează-te la registrul de sistem azureml
- Setează un nume opțional pentru experiment
- Verifică sau creează un compute.

> [!NOTE]
> Cerințele: un nod GPU poate avea mai multe plăci GPU. De exemplu, un nod Standard_NC24rs_v3 are 4 plăci NVIDIA V100, iar Standard_NC12s_v3 are 2 plăci NVIDIA V100. Consultă documentația pentru aceste informații. Numărul de plăci GPU per nod este setat în parametrul gpus_per_node de mai jos. Setarea corectă a acestei valori va asigura utilizarea tuturor plăcilor GPU din nod. SKU-urile recomandate pentru compute GPU pot fi găsite aici și aici.

### Biblioteci Python

Instalează dependențele rulând celula de mai jos. Acest pas nu este opțional dacă rulezi într-un mediu nou.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interacțiunea cu Azure ML

1. Acest script Python este folosit pentru a interacționa cu serviciul Azure Machine Learning (Azure ML). Iată o descriere a ceea ce face:

    - Importă modulele necesare din pachetele azure.ai.ml, azure.identity și azure.ai.ml.entities. De asemenea, importă modulul time.

    - Încearcă să se autentifice folosind DefaultAzureCredential(), care oferă o experiență simplificată de autentificare pentru a începe rapid dezvoltarea aplicațiilor care rulează în cloud-ul Azure. Dacă acest lucru eșuează, folosește InteractiveBrowserCredential(), care oferă un prompt interactiv de autentificare.

    - Apoi încearcă să creeze o instanță MLClient folosind metoda from_config, care citește configurația din fișierul implicit config.json. Dacă acest lucru eșuează, creează o instanță MLClient furnizând manual subscription_id, resource_group_name și workspace_name.

    - Creează o altă instanță MLClient, de data aceasta pentru registrul Azure ML numit "azureml". Acest registru este locul unde sunt stocate modelele, pipeline-urile de fine-tuning și mediile.

    - Setează experiment_name la "chat_completion_Phi-3-mini-4k-instruct".

    - Generează un timestamp unic convertind timpul curent (în secunde de la epocă, ca număr în virgulă mobilă) într-un întreg și apoi într-un șir de caractere. Acest timestamp poate fi folosit pentru a crea nume și versiuni unice.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. Alege un model de bază pentru ajustare

1. Phi-3-mini-4k-instruct este un model ușor, de ultimă generație, cu 3.8 miliarde de parametri, construit pe baza seturilor de date folosite pentru Phi-2. Modelul face parte din familia Phi-3, iar versiunea Mini vine în două variante, 4K și 128K, care reprezintă lungimea contextului (în tokeni) pe care o poate susține. Trebuie să ajustăm modelul pentru scopul nostru specific înainte de utilizare. Poți explora aceste modele în Catalogul de Modele din AzureML Studio, filtrând după sarcina chat-completion. În acest exemplu, folosim modelul Phi-3-mini-4k-instruct. Dacă ai deschis acest notebook pentru un alt model, înlocuiește numele și versiunea modelului corespunzător.

    > [!NOTE]
    > proprietatea model id a modelului. Aceasta va fi transmisă ca input jobului de ajustare. Este disponibilă și ca Asset ID în pagina de detalii a modelului din Catalogul de Modele AzureML Studio.

2. Acest script Python interacționează cu serviciul Azure Machine Learning (Azure ML). Iată o descriere a ceea ce face:

    - Setează model_name la "Phi-3-mini-4k-instruct".

    - Folosește metoda get a proprietății models a obiectului registry_ml_client pentru a prelua cea mai recentă versiune a modelului cu numele specificat din registrul Azure ML. Metoda get este apelată cu două argumente: numele modelului și o etichetă care specifică că trebuie preluată cea mai recentă versiune.

    - Afișează un mesaj în consolă care indică numele, versiunea și id-ul modelului ce va fi folosit pentru ajustare. Metoda format a șirului este folosită pentru a introduce numele, versiunea și id-ul modelului în mesaj. Aceste proprietăți sunt accesate din obiectul foundation_model.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Creează un compute care va fi folosit pentru job

Jobul de fine-tuning funcționează DOAR cu compute GPU. Dimensiunea compute-ului depinde de mărimea modelului și, în majoritatea cazurilor, poate fi dificil să identifici compute-ul potrivit pentru job. În această celulă, ghidăm utilizatorul să aleagă compute-ul corect pentru job.

> [!NOTE]
> Compute-urile listate mai jos funcționează cu cea mai optimizată configurație. Orice modificare a configurației poate duce la eroarea Cuda Out Of Memory. În astfel de cazuri, încearcă să faci upgrade la un compute mai mare.

> [!NOTE]
> Când selectezi compute_cluster_size mai jos, asigură-te că compute-ul este disponibil în grupul tău de resurse. Dacă un anumit compute nu este disponibil, poți face o cerere pentru acces la resursele compute.

### Verificarea suportului modelului pentru fine tuning

1. Acest script Python interacționează cu un model Azure Machine Learning (Azure ML). Iată o descriere a ceea ce face:

    - Importă modulul ast, care oferă funcții pentru procesarea arborilor de sintaxă abstractă Python.

    - Verifică dacă obiectul foundation_model (care reprezintă un model în Azure ML) are un tag numit finetune_compute_allow_list. Tag-urile în Azure ML sunt perechi cheie-valoare pe care le poți crea și folosi pentru a filtra și sorta modelele.

    - Dacă tag-ul finetune_compute_allow_list este prezent, folosește funcția ast.literal_eval pentru a parsa în siguranță valoarea tag-ului (un șir de caractere) într-o listă Python. Această listă este apoi atribuită variabilei computes_allow_list. Afișează un mesaj care indică faptul că un compute ar trebui creat din această listă.

    - Dacă tag-ul finetune_compute_allow_list nu este prezent, setează computes_allow_list la None și afișează un mesaj care indică faptul că tag-ul nu face parte din tag-urile modelului.

    - Pe scurt, acest script verifică un tag specific în metadatele modelului, convertește valoarea tag-ului într-o listă dacă există și oferă feedback utilizatorului.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Verificarea Compute Instance

1. Acest script Python interacționează cu serviciul Azure Machine Learning (Azure ML) și efectuează mai multe verificări asupra unei instanțe compute. Iată o descriere a ceea ce face:

    - Încearcă să recupereze instanța compute cu numele stocat în compute_cluster din workspace-ul Azure ML. Dacă starea de provisioning a instanței este "failed", ridică o eroare ValueError.

    - Verifică dacă computes_allow_list nu este None. Dacă nu este, convertește toate dimensiunile compute din listă în litere mici și verifică dacă dimensiunea instanței compute curente este în listă. Dacă nu este, ridică o eroare ValueError.

    - Dacă computes_allow_list este None, verifică dacă dimensiunea instanței compute este într-o listă de dimensiuni GPU VM neacceptate. Dacă este, ridică o eroare ValueError.

    - Recuperează o listă cu toate dimensiunile compute disponibile în workspace. Parcurge această listă și pentru fiecare dimensiune verifică dacă numele corespunde cu dimensiunea instanței compute curente. Dacă da, recuperează numărul de GPU-uri pentru acea dimensiune și setează gpu_count_found la True.

    - Dacă gpu_count_found este True, afișează numărul de GPU-uri din instanța compute. Dacă este False, ridică o eroare ValueError.

    - Pe scurt, acest script face mai multe verificări asupra unei instanțe compute dintr-un workspace Azure ML, inclusiv starea de provisioning, dimensiunea față de o listă permisă sau interzisă și numărul de GPU-uri.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Alege setul de date pentru ajustarea modelului

1. Folosim setul de date ultrachat_200k. Setul are patru diviziuni, potrivite pentru fine-tuning supravegheat (sft).
Generare ranking (gen). Numărul de exemple per diviziune este afișat astfel:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Următoarele celule arată pregătirea de bază a datelor pentru fine tuning:

### Vizualizează câteva rânduri de date

Dorim ca acest eșantion să ruleze rapid, așa că salvăm fișierele train_sft, test_sft conținând 5% din rândurile deja filtrate. Aceasta înseamnă că modelul ajustat va avea o acuratețe mai mică, deci nu ar trebui folosit în producție.
Scriptul download-dataset.py este folosit pentru a descărca setul ultrachat_200k și a transforma datele într-un format consumabil de componenta pipeline-ului de fine tuning. Deoarece setul este mare, aici avem doar o parte din el.

1. Rularea scriptului de mai jos descarcă doar 5% din date. Aceasta poate fi mărită schimbând parametrul dataset_split_pc la procentul dorit.

    > [!NOTE]
    > Unele modele de limbaj au coduri de limbă diferite, deci numele coloanelor din setul de date ar trebui să reflecte acest lucru.

1. Iată un exemplu despre cum ar trebui să arate datele
Setul de date chat-completion este stocat în format parquet, fiecare intrare folosind următorul schelet:

    - Acesta este un document JSON (JavaScript Object Notation), un format popular de schimb de date. Nu este cod executabil, ci o modalitate de a stoca și transporta date. Iată o descriere a structurii:

    - "prompt": Această cheie conține un șir de caractere care reprezintă o sarcină sau o întrebare adresată unui asistent AI.

    - "messages": Această cheie conține un array de obiecte. Fiecare obiect reprezintă un mesaj într-o conversație între un utilizator și un asistent AI. Fiecare mesaj are două chei:

    - "content": Această cheie conține un șir de caractere care reprezintă conținutul mesajului.
    - "role": Această cheie conține un șir de caractere care reprezintă rolul entității care a trimis mesajul. Poate fi "user" sau "assistant".
    - "prompt_id": Această cheie conține un șir de caractere care reprezintă un identificator unic pentru prompt.

1. În acest document JSON specific, este reprezentată o conversație în care un utilizator îi cere unui asistent AI să creeze un protagonist pentru o poveste distopică. Asistentul răspunde, iar utilizatorul cere mai multe detalii. Asistentul acceptă să ofere mai multe detalii. Întreaga conversație este asociată cu un id specific de prompt.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Descărcarea datelor

1. Acest script Python este folosit pentru a descărca un set de date folosind un script auxiliar numit download-dataset.py. Iată o descriere a ceea ce face:

    - Importă modulul os, care oferă o modalitate portabilă de a folosi funcționalități dependente de sistemul de operare.

    - Folosește funcția os.system pentru a rula scriptul download-dataset.py în shell cu argumente specifice din linia de comandă. Argumentele specifică setul de date de descărcat (HuggingFaceH4/ultrachat_200k), directorul în care să fie descărcat (ultrachat_200k_dataset) și procentul de divizare a setului (5). Funcția os.system returnează codul de ieșire al comenzii executate; acest cod este stocat în variabila exit_status.

    - Verifică dacă exit_status nu este 0. În sistemele Unix-like, un cod de ieșire 0 indică succes, iar orice alt număr indică o eroare. Dacă exit_status nu este 0, ridică o excepție cu un mesaj care indică o eroare la descărcarea setului de date.

    - Pe scurt, acest script rulează o comandă pentru a descărca un set de date folosind un script auxiliar și ridică o excepție dacă comanda eșuează.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Încărcarea datelor într-un DataFrame

1. Acest script Python încarcă un fișier JSON Lines într-un DataFrame pandas și afișează primele 5 rânduri. Iată o descriere a ceea ce face:

    - Importă biblioteca pandas, o bibliotecă puternică pentru manipularea și analiza datelor.

    - Setează lățimea maximă a coloanelor pentru opțiunile de afișare pandas la 0. Aceasta înseamnă că textul complet al fiecărei coloane va fi afișat fără trunchiere când DataFrame-ul este tipărit.

    - Folosește funcția pd.read_json pentru a încărca fișierul train_sft.jsonl din directorul ultrachat_200k_dataset într-un DataFrame. Argumentul lines=True indică faptul că fișierul este în format JSON Lines, unde fiecare linie este un obiect JSON separat.
- Folosește metoda head pentru a afișa primele 5 rânduri din DataFrame. Dacă DataFrame-ul are mai puțin de 5 rânduri, va afișa toate rândurile.

- Pe scurt, acest script încarcă un fișier JSON Lines într-un DataFrame și afișează primele 5 rânduri cu textul complet al coloanelor.

```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. Trimite jobul de fine tuning folosind modelul și datele ca inputuri

Creează jobul care folosește componenta pipeline pentru chat-completion. Află mai multe despre toți parametrii suportați pentru fine tuning.

### Definirea parametrilor pentru finetune

1. Parametrii pentru finetune pot fi grupați în 2 categorii - parametri de antrenament și parametri de optimizare

1. Parametrii de antrenament definesc aspectele legate de antrenament, cum ar fi -

    - Optimizer-ul și scheduler-ul folosit
    - Metoda de optimizare a fine tuning-ului
    - Numărul de pași de antrenament, dimensiunea batch-ului și altele
    - Parametrii de optimizare ajută la optimizarea memoriei GPU și la utilizarea eficientă a resurselor de calcul.

1. Mai jos sunt câțiva dintre parametrii care aparțin acestei categorii. Parametrii de optimizare diferă pentru fiecare model și sunt incluși împreună cu modelul pentru a gestiona aceste variații.

    - Activarea deepspeed și LoRA
    - Activarea antrenamentului cu precizie mixtă
    - Activarea antrenamentului multi-nod


> [!NOTE]
> Fine tuning-ul supravegheat poate duce la pierderea alinierii sau la uitare catastrofală. Recomandăm verificarea acestei probleme și rularea unei etape de aliniere după fine tuning.

### Parametrii pentru Fine Tuning

1. Acest script Python setează parametrii pentru fine tuning-ul unui model de machine learning. Iată o descriere a ceea ce face:

    - Setează parametrii impliciți pentru antrenament, cum ar fi numărul de epoci, dimensiunile batch-urilor pentru antrenament și evaluare, rata de învățare și tipul scheduler-ului pentru rata de învățare.

    - Setează parametrii impliciți pentru optimizare, cum ar fi dacă se aplică Layer-wise Relevance Propagation (LoRa) și DeepSpeed, și stadiul DeepSpeed.

    - Combină parametrii de antrenament și optimizare într-un singur dicționar numit finetune_parameters.

    - Verifică dacă foundation_model are parametri impliciți specifici modelului. Dacă da, afișează un mesaj de avertizare și actualizează dicționarul finetune_parameters cu acești parametri specifici modelului. Funcția ast.literal_eval este folosită pentru a converti parametrii specifici modelului dintr-un șir de caractere într-un dicționar Python.

    - Afișează setul final de parametri pentru fine tuning care vor fi folosiți în execuție.

    - Pe scurt, acest script configurează și afișează parametrii pentru fine tuning-ul unui model de machine learning, cu posibilitatea de a suprascrie parametrii impliciți cu cei specifici modelului.

```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline de Antrenament

1. Acest script Python definește o funcție pentru a genera un nume de afișare pentru un pipeline de antrenament machine learning, apoi apelează această funcție pentru a genera și afișa numele. Iată o descriere a ceea ce face:

1. Funcția get_pipeline_display_name este definită. Această funcție generează un nume de afișare bazat pe diverși parametri legați de pipeline-ul de antrenament.

1. În interiorul funcției, calculează dimensiunea totală a batch-ului prin înmulțirea dimensiunii batch-ului per dispozitiv, numărul de pași de acumulare a gradientului, numărul de GPU-uri per nod și numărul de noduri folosite pentru fine tuning.

1. Recuperează alți parametri precum tipul scheduler-ului pentru rata de învățare, dacă se aplică DeepSpeed, stadiul DeepSpeed, dacă se aplică Layer-wise Relevance Propagation (LoRa), limita pentru numărul de checkpoint-uri ale modelului de păstrat și lungimea maximă a secvenței.

1. Construiește un șir care include toți acești parametri, separați prin cratime. Dacă DeepSpeed sau LoRa sunt aplicate, șirul include "ds" urmat de stadiul DeepSpeed, sau "lora", respectiv. Dacă nu, include "nods" sau "nolora", respectiv.

1. Funcția returnează acest șir, care servește drept nume de afișare pentru pipeline-ul de antrenament.

1. După definirea funcției, aceasta este apelată pentru a genera numele de afișare, care este apoi afișat.

1. Pe scurt, acest script generează un nume de afișare pentru un pipeline de antrenament machine learning bazat pe diverși parametri și apoi afișează acest nume.

```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Configurarea Pipeline-ului

Acest script Python definește și configurează un pipeline de machine learning folosind Azure Machine Learning SDK. Iată o descriere a ceea ce face:

1. Importă modulele necesare din Azure AI ML SDK.

1. Preia o componentă pipeline numită "chat_completion_pipeline" din registru.

1. Definește un job pipeline folosind decoratorul `@pipeline` și funcția `create_pipeline`. Numele pipeline-ului este setat la `pipeline_display_name`.

1. În funcția `create_pipeline`, inițializează componenta pipeline preluată cu diverși parametri, inclusiv calea modelului, clusterele de calcul pentru diferite etape, diviziunile dataset-ului pentru antrenament și testare, numărul de GPU-uri folosite pentru fine tuning și alți parametri pentru fine tuning.

1. Mapează output-ul jobului de fine tuning la output-ul jobului pipeline. Acest lucru se face pentru ca modelul fine-tuned să poată fi ușor înregistrat, ceea ce este necesar pentru a implementa modelul la un endpoint online sau batch.

1. Creează o instanță a pipeline-ului apelând funcția `create_pipeline`.

1. Setează opțiunea `force_rerun` a pipeline-ului la `True`, ceea ce înseamnă că rezultatele cache-uite din joburile anterioare nu vor fi folosite.

1. Setează opțiunea `continue_on_step_failure` a pipeline-ului la `False`, ceea ce înseamnă că pipeline-ul se va opri dacă vreun pas eșuează.

1. Pe scurt, acest script definește și configurează un pipeline de machine learning pentru o sarcină de chat completion folosind Azure Machine Learning SDK.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Trimiterea Jobului

1. Acest script Python trimite un job pipeline de machine learning către un workspace Azure Machine Learning și apoi așteaptă finalizarea jobului. Iată o descriere a ceea ce face:

    - Apelează metoda create_or_update a obiectului jobs din workspace_ml_client pentru a trimite jobul pipeline. Pipeline-ul care va fi rulat este specificat prin pipeline_object, iar experimentul sub care se rulează jobul este specificat prin experiment_name.

    - Apoi apelează metoda stream a obiectului jobs din workspace_ml_client pentru a aștepta finalizarea jobului pipeline. Jobul pentru care se așteaptă este specificat prin atributul name al obiectului pipeline_job.

    - Pe scurt, acest script trimite un job pipeline de machine learning către un workspace Azure Machine Learning și apoi așteaptă finalizarea jobului.

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Înregistrează modelul fine tuned în workspace

Vom înregistra modelul din output-ul jobului de fine tuning. Acest lucru va urmări linia de proveniență între modelul fine tuned și jobul de fine tuning. Jobul de fine tuning, la rândul său, urmărește linia de proveniență către modelul de bază, date și codul de antrenament.

### Înregistrarea Modelului ML

1. Acest script Python înregistrează un model de machine learning antrenat într-un pipeline Azure Machine Learning. Iată o descriere a ceea ce face:

    - Importă modulele necesare din Azure AI ML SDK.

    - Verifică dacă output-ul trained_model este disponibil din jobul pipeline apelând metoda get a obiectului jobs din workspace_ml_client și accesând atributul outputs.

    - Construiește o cale către modelul antrenat formatând un șir cu numele jobului pipeline și numele output-ului ("trained_model").

    - Definește un nume pentru modelul fine tuned adăugând "-ultrachat-200k" la numele original al modelului și înlocuind orice slash-uri cu cratime.

    - Pregătește înregistrarea modelului creând un obiect Model cu diverși parametri, inclusiv calea către model, tipul modelului (model MLflow), numele și versiunea modelului și o descriere a modelului.

    - Înregistrează modelul apelând metoda create_or_update a obiectului models din workspace_ml_client cu obiectul Model ca argument.

    - Afișează modelul înregistrat.

1. Pe scurt, acest script înregistrează un model de machine learning antrenat într-un pipeline Azure Machine Learning.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. Deployează modelul fine tuned la un endpoint online

Endpoint-urile online oferă o API REST durabilă care poate fi folosită pentru integrarea cu aplicații ce au nevoie să utilizeze modelul.

### Gestionarea Endpoint-ului

1. Acest script Python creează un endpoint online gestionat în Azure Machine Learning pentru un model înregistrat. Iată o descriere a ceea ce face:

    - Importă modulele necesare din Azure AI ML SDK.

    - Definește un nume unic pentru endpoint-ul online adăugând un timestamp la șirul "ultrachat-completion-".

    - Pregătește crearea endpoint-ului online creând un obiect ManagedOnlineEndpoint cu diverși parametri, inclusiv numele endpoint-ului, o descriere a endpoint-ului și modul de autentificare ("key").

    - Creează endpoint-ul online apelând metoda begin_create_or_update a workspace_ml_client cu obiectul ManagedOnlineEndpoint ca argument. Apoi așteaptă finalizarea operațiunii apelând metoda wait.

1. Pe scurt, acest script creează un endpoint online gestionat în Azure Machine Learning pentru un model înregistrat.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Poți găsi aici lista SKU-urilor suportate pentru deployment - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Deployarea Modelului ML

1. Acest script Python deployează un model de machine learning înregistrat la un endpoint online gestionat în Azure Machine Learning. Iată o descriere a ceea ce face:

    - Importă modulul ast, care oferă funcții pentru procesarea arborilor de sintaxă abstractă Python.

    - Setează tipul instanței pentru deployment la "Standard_NC6s_v3".

    - Verifică dacă tag-ul inference_compute_allow_list este prezent în foundation model. Dacă este, convertește valoarea tag-ului dintr-un șir într-o listă Python și o atribuie lui inference_computes_allow_list. Dacă nu, setează inference_computes_allow_list la None.

    - Verifică dacă tipul instanței specificat este în lista permisă. Dacă nu este, afișează un mesaj care cere utilizatorului să selecteze un tip de instanță din lista permisă.

    - Pregătește crearea deployment-ului creând un obiect ManagedOnlineDeployment cu diverși parametri, inclusiv numele deployment-ului, numele endpoint-ului, ID-ul modelului, tipul și numărul de instanțe, setările pentru liveness probe și setările pentru request.

    - Creează deployment-ul apelând metoda begin_create_or_update a workspace_ml_client cu obiectul ManagedOnlineDeployment ca argument. Apoi așteaptă finalizarea operațiunii apelând metoda wait.

    - Setează traficul endpoint-ului pentru a direcționa 100% din trafic către deployment-ul "demo".

    - Actualizează endpoint-ul apelând metoda begin_create_or_update a workspace_ml_client cu obiectul endpoint ca argument. Apoi așteaptă finalizarea operațiunii apelând metoda result.

1. Pe scurt, acest script deployează un model de machine learning înregistrat la un endpoint online gestionat în Azure Machine Learning.

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Testează endpoint-ul cu date de exemplu

Vom prelua câteva date de exemplu din dataset-ul de test și le vom trimite către endpoint-ul online pentru inferență. Apoi vom afișa etichetele prezise alături de etichetele reale.

### Citirea rezultatelor

1. Acest script Python citește un fișier JSON Lines într-un DataFrame pandas, ia un eșantion aleator și resetează indexul. Iată o descriere a ceea ce face:

    - Citește fișierul ./ultrachat_200k_dataset/test_gen.jsonl într-un DataFrame pandas. Funcția read_json este folosită cu argumentul lines=True deoarece fișierul este în format JSON Lines, unde fiecare linie este un obiect JSON separat.

    - Ia un eșantion aleator de 1 rând din DataFrame. Funcția sample este folosită cu argumentul n=1 pentru a specifica numărul de rânduri aleatorii selectate.

    - Resetează indexul DataFrame-ului. Funcția reset_index este folosită cu argumentul drop=True pentru a elimina indexul original și a-l înlocui cu un index nou, cu valori întregi implicite.

    - Afișează primele 2 rânduri ale DataFrame-ului folosind funcția head cu argumentul 2. Totuși, deoarece DataFrame-ul conține doar un rând după eșantionare, va afișa doar acel rând.

1. Pe scurt, acest script citește un fișier JSON Lines într-un DataFrame pandas, ia un eșantion aleator de 1 rând, resetează indexul și afișează primul rând.

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### Crearea Obiectului JSON

1. Acest script Python creează un obiect JSON cu parametri specifici și îl salvează într-un fișier. Iată o descriere a ceea ce face:

    - Importă modulul json, care oferă funcții pentru lucrul cu date JSON.

    - Creează un dicționar parameters cu chei și valori care reprezintă parametrii pentru un model de machine learning. Cheile sunt "temperature", "top_p", "do_sample" și "max_new_tokens", iar valorile corespunzătoare sunt 0.6, 0.9, True și 200.

    - Creează un alt dicționar test_json cu două chei: "input_data" și "params". Valoarea pentru "input_data" este un alt dicționar cu cheile "input_string" și "parameters". Valoarea pentru "input_string" este o listă care conține primul mesaj din DataFrame-ul test_df. Valoarea pentru "parameters" este dicționarul parameters creat anterior. Valoarea pentru "params" este un dicționar gol.
- Se deschide un fișier numit sample_score.json

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### Invocarea Endpoint-ului

1. Acest script Python invocă un endpoint online în Azure Machine Learning pentru a evalua un fișier JSON. Iată o descriere a ceea ce face:

    - Apelează metoda invoke a proprietății online_endpoints a obiectului workspace_ml_client. Această metodă este folosită pentru a trimite o cerere către un endpoint online și a primi un răspuns.

    - Specifică numele endpoint-ului și al implementării prin argumentele endpoint_name și deployment_name. În acest caz, numele endpoint-ului este stocat în variabila online_endpoint_name, iar numele implementării este „demo”.

    - Specifică calea către fișierul JSON care trebuie evaluat prin argumentul request_file. În acest caz, fișierul este ./ultrachat_200k_dataset/sample_score.json.

    - Stochează răspunsul de la endpoint în variabila response.

    - Afișează răspunsul brut.

1. Pe scurt, acest script invocă un endpoint online în Azure Machine Learning pentru a evalua un fișier JSON și afișează răspunsul.

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. Ștergerea endpoint-ului online

1. Nu uita să ștergi endpoint-ul online, altfel vei lăsa contorul de facturare activ pentru resursele de calcul folosite de endpoint. Această linie de cod Python șterge un endpoint online în Azure Machine Learning. Iată o descriere a ceea ce face:

    - Apelează metoda begin_delete a proprietății online_endpoints a obiectului workspace_ml_client. Această metodă este folosită pentru a începe ștergerea unui endpoint online.

    - Specifică numele endpoint-ului care trebuie șters prin argumentul name. În acest caz, numele endpoint-ului este stocat în variabila online_endpoint_name.

    - Apelează metoda wait pentru a aștepta finalizarea operațiunii de ștergere. Aceasta este o operațiune blocantă, ceea ce înseamnă că va împiedica continuarea scriptului până când ștergerea este finalizată.

    - Pe scurt, această linie de cod pornește ștergerea unui endpoint online în Azure Machine Learning și așteaptă finalizarea operațiunii.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.