<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-09T21:08:04+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "pl"
}
-->
## Jak korzystać z komponentów chat-completion z rejestru systemowego Azure ML do dostrajania modelu

W tym przykładzie przeprowadzimy dostrajanie modelu Phi-3-mini-4k-instruct, aby ukończyć rozmowę między 2 osobami, korzystając z zestawu danych ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.pl.png)

Przykład pokaże, jak wykonać dostrajanie za pomocą Azure ML SDK i Pythona, a następnie wdrożyć dostrojony model na endpoint online do wnioskowania w czasie rzeczywistym.

### Dane treningowe

Użyjemy zestawu danych ultrachat_200k. Jest to mocno przefiltrowana wersja zestawu UltraChat, używana do trenowania Zephyr-7B-β, nowoczesnego modelu chat o wielkości 7b.

### Model

Użyjemy modelu Phi-3-mini-4k-instruct, aby pokazać, jak użytkownik może dostroić model do zadania chat-completion. Jeśli otworzyłeś ten notebook z konkretnej karty modelu, pamiętaj, aby zastąpić nazwę modelu odpowiednią.

### Zadania

- Wybierz model do dostrajania.
- Wybierz i zbadaj dane treningowe.
- Skonfiguruj zadanie dostrajania.
- Uruchom zadanie dostrajania.
- Przejrzyj metryki treningu i ewaluacji.
- Zarejestruj dostrojony model.
- Wdróż dostrojony model do wnioskowania w czasie rzeczywistym.
- Posprzątaj zasoby.

## 1. Przygotowanie środowiska

- Zainstaluj zależności
- Połącz się z AzureML Workspace. Więcej informacji znajdziesz w sekcji konfiguracji uwierzytelniania SDK. Zamień poniżej <WORKSPACE_NAME>, <RESOURCE_GROUP> i <SUBSCRIPTION_ID>.
- Połącz się z rejestrem systemowym azureml
- Ustaw opcjonalną nazwę eksperymentu
- Sprawdź lub utwórz zasób obliczeniowy.

> [!NOTE]
> Wymagania: pojedynczy węzeł GPU może mieć wiele kart GPU. Na przykład, w jednym węźle Standard_NC24rs_v3 jest 4 karty NVIDIA V100, a w Standard_NC12s_v3 są 2 karty NVIDIA V100. Informacje te znajdziesz w dokumentacji. Liczba kart GPU na węzeł jest ustawiana w parametrze gpus_per_node poniżej. Poprawne ustawienie tej wartości zapewni wykorzystanie wszystkich GPU w węźle. Zalecane SKU obliczeniowe GPU znajdziesz tutaj i tutaj.

### Biblioteki Pythona

Zainstaluj zależności, uruchamiając poniższą komórkę. To nie jest opcjonalny krok, jeśli działasz w nowym środowisku.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interakcja z Azure ML

1. Ten skrypt Pythona służy do interakcji z usługą Azure Machine Learning (Azure ML). Oto, co robi:

    - Importuje niezbędne moduły z pakietów azure.ai.ml, azure.identity oraz azure.ai.ml.entities. Importuje także moduł time.

    - Próbuje uwierzytelnić się za pomocą DefaultAzureCredential(), co upraszcza proces uwierzytelniania, umożliwiając szybkie rozpoczęcie pracy z aplikacjami działającymi w chmurze Azure. Jeśli to się nie powiedzie, przechodzi do InteractiveBrowserCredential(), które wyświetla interaktywny prompt logowania.

    - Następnie próbuje utworzyć instancję MLClient używając metody from_config, która odczytuje konfigurację z domyślnego pliku konfiguracyjnego (config.json). Jeśli to się nie uda, tworzy MLClient podając ręcznie subscription_id, resource_group_name i workspace_name.

    - Tworzy kolejną instancję MLClient, tym razem dla rejestru Azure ML o nazwie "azureml". To właśnie tam przechowywane są modele, pipeline'y do dostrajania i środowiska.

    - Ustawia nazwę eksperymentu na "chat_completion_Phi-3-mini-4k-instruct".

    - Generuje unikalny znacznik czasowy, konwertując aktualny czas (w sekundach od epoki, jako liczba zmiennoprzecinkowa) na liczbę całkowitą, a następnie na string. Ten znacznik może być użyty do tworzenia unikalnych nazw i wersji.

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

## 2. Wybierz model bazowy do dostrajania

1. Phi-3-mini-4k-instruct to lekki, nowoczesny model o 3,8 mld parametrów, oparty na zbiorach danych użytych dla Phi-2. Model należy do rodziny Phi-3, a wersja Mini występuje w dwóch wariantach: 4K i 128K, które oznaczają długość kontekstu (w tokenach), jaką model może obsłużyć. Aby go użyć, musimy go dostroić do naszego konkretnego celu. Możesz przeglądać te modele w Model Catalog w AzureML Studio, filtrując po zadaniu chat-completion. W tym przykładzie używamy modelu Phi-3-mini-4k-instruct. Jeśli otworzyłeś ten notebook dla innego modelu, zamień nazwę i wersję modelu odpowiednio.

    > [!NOTE]
    > właściwość model id modelu. Będzie ona przekazana jako wejście do zadania dostrajania. Jest też dostępna jako pole Asset ID na stronie szczegółów modelu w AzureML Studio Model Catalog.

2. Ten skrypt Pythona komunikuje się z usługą Azure Machine Learning (Azure ML). Oto, co robi:

    - Ustawia model_name na "Phi-3-mini-4k-instruct".

    - Korzysta z metody get właściwości models obiektu registry_ml_client, aby pobrać najnowszą wersję modelu o podanej nazwie z rejestru Azure ML. Metoda get jest wywoływana z dwoma argumentami: nazwą modelu oraz etykietą wskazującą, że ma zostać pobrana najnowsza wersja.

    - Wypisuje na konsolę komunikat z nazwą, wersją i id modelu, który będzie używany do dostrajania. Metoda format stringa jest użyta do wstawienia tych wartości. Nazwa, wersja i id modelu są dostępne jako właściwości obiektu foundation_model.

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

## 3. Utwórz zasób obliczeniowy do użycia w zadaniu

Zadanie finetune działa TYLKO z zasobem obliczeniowym GPU. Rozmiar zasobu zależy od wielkości modelu i często trudno jest wybrać odpowiedni zasób. W tej komórce pomagamy użytkownikowi wybrać właściwy zasób do zadania.

> [!NOTE]
> Poniżej wymienione zasoby działają z najbardziej zoptymalizowaną konfiguracją. Jakiekolwiek zmiany konfiguracji mogą spowodować błąd Cuda Out Of Memory. W takich przypadkach spróbuj zwiększyć rozmiar zasobu.

> [!NOTE]
> Podczas wyboru compute_cluster_size upewnij się, że zasób jest dostępny w Twojej grupie zasobów. Jeśli dany zasób nie jest dostępny, możesz złożyć prośbę o dostęp do zasobów obliczeniowych.

### Sprawdzanie wsparcia modelu dla dostrajania

1. Ten skrypt Pythona komunikuje się z modelem Azure Machine Learning (Azure ML). Oto, co robi:

    - Importuje moduł ast, który dostarcza funkcje do przetwarzania drzew składni abstrakcyjnej Pythona.

    - Sprawdza, czy obiekt foundation_model (reprezentujący model w Azure ML) ma tag o nazwie finetune_compute_allow_list. Tagi w Azure ML to pary klucz-wartość, które można tworzyć i używać do filtrowania i sortowania modeli.

    - Jeśli tag finetune_compute_allow_list jest obecny, używa funkcji ast.literal_eval, aby bezpiecznie przekształcić wartość tego tagu (string) na listę Pythona. Ta lista jest przypisywana do zmiennej computes_allow_list. Następnie wypisuje komunikat, że należy utworzyć zasób obliczeniowy z tej listy.

    - Jeśli tag finetune_compute_allow_list nie jest obecny, ustawia computes_allow_list na None i wypisuje komunikat, że tag nie jest częścią tagów modelu.

    - Podsumowując, skrypt sprawdza, czy w metadanych modelu znajduje się konkretny tag, konwertuje jego wartość na listę, jeśli istnieje, i informuje użytkownika.

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

### Sprawdzanie instancji obliczeniowej

1. Ten skrypt Pythona komunikuje się z usługą Azure Machine Learning (Azure ML) i wykonuje kilka kontroli na instancji obliczeniowej. Oto, co robi:

    - Próbuje pobrać instancję obliczeniową o nazwie przechowywanej w zmiennej compute_cluster z Azure ML workspace. Jeśli stan provisioningowy instancji to "failed", zgłasza błąd ValueError.

    - Sprawdza, czy computes_allow_list nie jest None. Jeśli nie jest, konwertuje wszystkie rozmiary w liście na małe litery i sprawdza, czy rozmiar bieżącej instancji jest na liście. Jeśli nie, zgłasza błąd ValueError.

    - Jeśli computes_allow_list jest None, sprawdza, czy rozmiar instancji jest na liście nieobsługiwanych rozmiarów GPU VM. Jeśli tak, zgłasza błąd ValueError.

    - Pobiera listę wszystkich dostępnych rozmiarów zasobów w workspace. Następnie iteruje po niej i dla każdego rozmiaru sprawdza, czy jego nazwa pasuje do rozmiaru bieżącej instancji. Jeśli tak, pobiera liczbę GPU dla tego rozmiaru i ustawia gpu_count_found na True.

    - Jeśli gpu_count_found jest True, wypisuje liczbę GPU w instancji. W przeciwnym wypadku zgłasza błąd ValueError.

    - Podsumowując, skrypt wykonuje kilka kontroli na instancji obliczeniowej w Azure ML, w tym stan provisioningowy, zgodność rozmiaru z listą dozwolonych lub niedozwolonych oraz liczbę GPU.

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

## 4. Wybierz zestaw danych do dostrajania modelu

1. Używamy zestawu ultrachat_200k. Zestaw ma cztery podziały, odpowiednie do nadzorowanego dostrajania (sft). Ranking generacji (gen). Liczba przykładów na podział jest pokazana poniżej:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Kolejne komórki pokazują podstawowe przygotowanie danych do dostrajania:

### Wizualizacja kilku wierszy danych

Chcemy, aby ten przykład działał szybko, więc zapisujemy pliki train_sft i test_sft zawierające 5% już przyciętych wierszy. Oznacza to, że dostrojony model będzie mniej dokładny, więc nie powinien być używany w zastosowaniach produkcyjnych.  
Plik download-dataset.py służy do pobrania zestawu ultrachat_200k i przekształcenia go do formatu przetwarzanego przez pipeline do dostrajania. Ponieważ zestaw jest duży, tutaj mamy tylko jego część.

1. Uruchomienie poniższego skryptu pobiera tylko 5% danych. Można to zwiększyć, zmieniając parametr dataset_split_pc na pożądaną wartość procentową.

    > [!NOTE]
    > Niektóre modele językowe mają różne kody języków, więc nazwy kolumn w zestawie danych powinny to odzwierciedlać.

1. Przykład, jak powinny wyglądać dane:  
Zestaw chat-completion jest zapisany w formacie parquet, gdzie każdy wpis ma następującą strukturę:

    - To jest dokument JSON (JavaScript Object Notation), popularny format wymiany danych. Nie jest to kod wykonywalny, a sposób przechowywania i przesyłania danych. Oto jego struktura:

    - "prompt": klucz zawierający ciąg znaków reprezentujący zadanie lub pytanie skierowane do asystenta AI.

    - "messages": klucz zawierający tablicę obiektów. Każdy obiekt to wiadomość w rozmowie między użytkownikiem a asystentem AI. Każda wiadomość ma dwa klucze:

        - "content": zawiera treść wiadomości jako ciąg znaków.
        - "role": określa rolę nadawcy wiadomości, może być "user" lub "assistant".
    - "prompt_id": zawiera unikalny identyfikator zapytania.

1. W tym konkretnym dokumencie JSON przedstawiona jest rozmowa, w której użytkownik prosi asystenta AI o stworzenie protagonisty do dystopijnej historii. Asystent odpowiada, a użytkownik prosi o więcej szczegółów. Asystent zgadza się je podać. Cała rozmowa jest powiązana z konkretnym prompt_id.

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

### Pobieranie danych

1. Ten skrypt Pythona służy do pobrania zestawu danych za pomocą pomocniczego skryptu download-dataset.py. Oto, co robi:

    - Importuje moduł os, który zapewnia przenośny sposób korzystania z funkcji systemu operacyjnego.

    - Używa funkcji os.system do uruchomienia skryptu download-dataset.py w powłoce z określonymi argumentami wiersza poleceń. Argumenty określają zestaw do pobrania (HuggingFaceH4/ultrachat_200k), katalog docelowy (ultrachat_200k_dataset) oraz procent podziału zestawu (5). Funkcja os.system zwraca status wyjścia polecenia, który jest zapisywany w zmiennej exit_status.

    - Sprawdza, czy exit_status jest różny od 0. W systemach Unix status 0 oznacza sukces, inne wartości wskazują błąd. Jeśli exit_status jest różny od 0, zgłasza wyjątek z komunikatem o błędzie pobierania.

    - Podsumowując, skrypt uruchamia polecenie pobrania zestawu danych i zgłasza wyjątek, jeśli pobieranie się nie powiedzie.

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

### Ładowanie danych do DataFrame

1. Ten skrypt Pythona ładuje plik JSON Lines do obiektu pandas DataFrame i wyświetla pierwsze 5 wierszy. Oto, co robi:

    - Importuje bibliotekę pandas, potężne narzędzie do manipulacji i analizy danych.

    - Ustawia maksymalną szerokość kolumny w opcjach wyświetlania pandas na 0, co oznacza, że cały tekst kolumn będzie wyświetlany bez ucinania.

    - Używa funkcji pd.read_json do załadowania pliku train_sft.jsonl z katalogu ultrachat_200k_dataset do DataFrame. Argument lines=True oznacza, że plik jest w formacie JSON Lines, gdzie każda linia to osobny obiekt JSON.

    - Używa metody head, aby wyświetlić pierwsze 5 wierszy DataFrame. Jeśli jest ich mniej niż 5, wyświetli wszystkie.

    - Podsumowując, skrypt ładuje plik JSON Lines do DataFrame i pokazuje pierwsze 5 wierszy z pełnym tekstem kolumn.

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

## 5. Prześlij zadanie dostrajania, używając modelu i danych jako wejścia

Utwórz zadanie, które korzysta z komponentu pipeline chat-completion. Dowiedz się więcej o wszystkich parametrach obsługiwanych przy dostrajaniu.

### Definicja parametrów dostrajania

1. Parametry dostrajania można podzielić na 2 kategorie – parametry treningowe oraz parametry optymalizacji.

1. Parametry treningowe definiują aspekty treningu takie jak:

    - Optymalizator, scheduler do użycia
    - Metryka, którą chcemy zoptymalizować podczas dostrajania
    - Liczba kroków treningowych, rozmiar batcha itd.
    - Parametry optymalizacji pomagają efektywnie zarządzać pamięcią GPU i zasobami obliczeniowymi.

1. Poniżej kilka parametrów należących do tej kategorii. Parametry optymalizacji różnią się dla każdego modelu i są dołączone do modelu, aby radzić sobie z tymi różnicami.

    - Włącz deepspeed i LoRA
    - Włącz trening z mieszanymi precyzjami
    - Włącz trening wielowęzłowy

> [!NOTE]
> Nadzorowane dostrajanie może powodować utratę zgodności lub katastrofalne zapominanie. Zalecamy sprawdzenie tego problemu i przeprowadzenie etapu wyrównania po dostrojeniu.

### Parametry dostrajania  
1. Ten skrypt Pythona ustawia parametry dla dostrajania modelu ML. Oto, co robi:

    - Ustawia domyślne parametry treningowe, takie jak liczba epok, rozmiary batchy dla treningu i ewaluacji, współczynnik uczenia oraz typ scheduler’a.

    - Ustawia domyślne parametry optymalizacji, takie jak włączenie LoRa, DeepSpeed oraz etap DeepSpeed.

    - Łączy parametry treningowe i optymalizacji w jeden słownik finetune_parameters.

    - Sprawdza, czy foundation_model ma jakieś specyficzne
pipeline treningowy oparty na różnych parametrach, a następnie wyświetlanie tej nazwy wyświetlanej. ```python
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

### Konfigurowanie Pipeline
Ten skrypt Pythona definiuje i konfiguruje pipeline uczenia maszynowego przy użyciu Azure Machine Learning SDK. Oto co robi:
1. Importuje niezbędne moduły z Azure AI ML SDK.
2. Pobiera komponent pipeline o nazwie "chat_completion_pipeline" z rejestru.
3. Definiuje zadanie pipeline za pomocą `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`, co oznacza, że pipeline zatrzyma się, jeśli którykolwiek krok zakończy się niepowodzeniem.
4. Podsumowując, ten skrypt definiuje i konfiguruje pipeline uczenia maszynowego dla zadania uzupełniania czatu przy użyciu Azure Machine Learning SDK.

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

### Zgłaszanie zadania
1. Ten skrypt Pythona wysyła zadanie pipeline uczenia maszynowego do workspace Azure Machine Learning, a następnie czeka na jego zakończenie. Oto co robi:
- Wywołuje metodę create_or_update obiektu jobs w workspace_ml_client, aby wysłać zadanie pipeline. Pipeline, które ma zostać uruchomione, jest określone przez pipeline_object, a eksperyment, pod którym zadanie jest uruchamiane, przez experiment_name.
- Następnie wywołuje metodę stream obiektu jobs w workspace_ml_client, aby czekać na zakończenie zadania pipeline. Zadanie, na które czeka, jest określone przez atrybut name obiektu pipeline_job.
- Podsumowując, ten skrypt wysyła zadanie pipeline uczenia maszynowego do workspace Azure Machine Learning i czeka na jego zakończenie.

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

## 6. Rejestracja modelu fine-tuned w workspace
Zarejestrujemy model pochodzący z wyniku zadania fine-tuningu. To pozwoli śledzić pochodzenie między modelem fine-tuned a zadaniem fine-tuningu. Zadanie fine-tuningu z kolei śledzi pochodzenie do modelu bazowego, danych i kodu treningowego.

### Rejestracja modelu ML
1. Ten skrypt Pythona rejestruje model uczenia maszynowego, który został wytrenowany w pipeline Azure Machine Learning. Oto co robi:
- Importuje niezbędne moduły z Azure AI ML SDK.
- Sprawdza, czy output trained_model jest dostępny z zadania pipeline, wywołując metodę get obiektu jobs w workspace_ml_client i uzyskując dostęp do atrybutu outputs.
- Tworzy ścieżkę do wytrenowanego modelu, formatując ciąg znaków z nazwą zadania pipeline oraz nazwą outputu ("trained_model").
- Definiuje nazwę dla modelu fine-tuned, dodając "-ultrachat-200k" do oryginalnej nazwy modelu i zastępując ukośniki myślnikami.
- Przygotowuje rejestrację modelu, tworząc obiekt Model z różnymi parametrami, w tym ścieżką do modelu, typem modelu (model MLflow), nazwą i wersją modelu oraz opisem modelu.
- Rejestruje model, wywołując metodę create_or_update obiektu models w workspace_ml_client z obiektem Model jako argumentem.
- Wyświetla zarejestrowany model.
1. Podsumowując, ten skrypt rejestruje model uczenia maszynowego, który został wytrenowany w pipeline Azure Machine Learning.

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

## 7. Wdrażanie modelu fine-tuned do endpointu online
Endpointy online zapewniają trwałe API REST, które można wykorzystać do integracji z aplikacjami potrzebującymi korzystać z modelu.

### Zarządzanie Endpointem
1. Ten skrypt Pythona tworzy zarządzany endpoint online w Azure Machine Learning dla zarejestrowanego modelu. Oto co robi:
- Importuje niezbędne moduły z Azure AI ML SDK.
- Definiuje unikalną nazwę endpointu online, dodając znacznik czasu do ciągu "ultrachat-completion-".
- Przygotowuje się do utworzenia endpointu online, tworząc obiekt ManagedOnlineEndpoint z różnymi parametrami, w tym nazwą endpointu, opisem oraz trybem uwierzytelniania ("key").
- Tworzy endpoint online, wywołując metodę begin_create_or_update obiektu workspace_ml_client z obiektem ManagedOnlineEndpoint jako argumentem. Następnie czeka na zakończenie operacji, wywołując metodę wait.
1. Podsumowując, ten skrypt tworzy zarządzany endpoint online w Azure Machine Learning dla zarejestrowanego modelu.

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
> Tutaj znajdziesz listę obsługiwanych SKU dla wdrożeń - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Wdrażanie modelu ML

1. Ten skrypt Pythona wdraża zarejestrowany model uczenia maszynowego do zarządzanego endpointu online w Azure Machine Learning. Oto co robi:

    - Importuje moduł ast, który dostarcza funkcje do przetwarzania drzew składni abstrakcyjnej Pythona.

    - Ustawia typ instancji dla wdrożenia na "Standard_NC6s_v3".

    - Sprawdza, czy tag inference_compute_allow_list jest obecny w modelu bazowym. Jeśli tak, konwertuje wartość tagu z ciągu na listę Pythona i przypisuje ją do inference_computes_allow_list. Jeśli nie, ustawia inference_computes_allow_list na None.

    - Sprawdza, czy określony typ instancji znajduje się na liście dozwolonych. Jeśli nie, wyświetla komunikat proszący użytkownika o wybór typu instancji z listy dozwolonych.

    - Przygotowuje się do utworzenia wdrożenia, tworząc obiekt ManagedOnlineDeployment z różnymi parametrami, w tym nazwą wdrożenia, nazwą endpointu, ID modelu, typem i liczbą instancji, ustawieniami sondy liveness oraz ustawieniami zapytań.

    - Tworzy wdrożenie, wywołując metodę begin_create_or_update obiektu workspace_ml_client z obiektem ManagedOnlineDeployment jako argumentem. Następnie czeka na zakończenie operacji, wywołując metodę wait.

    - Ustawia ruch endpointu tak, aby 100% ruchu było kierowane do wdrożenia "demo".

    - Aktualizuje endpoint, wywołując metodę begin_create_or_update obiektu workspace_ml_client z obiektem endpoint jako argumentem. Następnie czeka na zakończenie aktualizacji, wywołując metodę result.

1. Podsumowując, ten skrypt wdraża zarejestrowany model uczenia maszynowego do zarządzanego endpointu online w Azure Machine Learning.

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

## 8. Testowanie endpointu na przykładowych danych

Pobierzemy przykładowe dane z zestawu testowego i wyślemy je do endpointu online do inferencji. Następnie pokażemy etykiety przewidziane wraz z etykietami prawdziwymi.

### Odczyt wyników

1. Ten skrypt Pythona odczytuje plik JSON Lines do DataFrame biblioteki pandas, losowo wybiera próbkę i resetuje indeks. Oto co robi:

    - Odczytuje plik ./ultrachat_200k_dataset/test_gen.jsonl do DataFrame pandas. Funkcja read_json jest używana z argumentem lines=True, ponieważ plik jest w formacie JSON Lines, gdzie każda linia to osobny obiekt JSON.

    - Losowo wybiera 1 wiersz z DataFrame. Funkcja sample jest używana z argumentem n=1, aby określić liczbę losowo wybranych wierszy.

    - Resetuje indeks DataFrame. Funkcja reset_index jest używana z argumentem drop=True, aby usunąć oryginalny indeks i zastąpić go nowym indeksem z domyślnymi wartościami całkowitymi.

    - Wyświetla pierwsze 2 wiersze DataFrame za pomocą funkcji head z argumentem 2. Jednak ponieważ DataFrame zawiera tylko jeden wiersz po próbkowaniu, zostanie wyświetlony tylko ten jeden wiersz.

1. Podsumowując, ten skrypt odczytuje plik JSON Lines do DataFrame pandas, losowo wybiera 1 wiersz, resetuje indeks i wyświetla pierwszy wiersz.

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

### Tworzenie obiektu JSON

1. Ten skrypt Pythona tworzy obiekt JSON z określonymi parametrami i zapisuje go do pliku. Oto co robi:

    - Importuje moduł json, który dostarcza funkcje do pracy z danymi JSON.

    - Tworzy słownik parameters z kluczami i wartościami reprezentującymi parametry dla modelu uczenia maszynowego. Klucze to "temperature", "top_p", "do_sample" oraz "max_new_tokens", a odpowiadające im wartości to odpowiednio 0.6, 0.9, True oraz 200.

    - Tworzy kolejny słownik test_json z dwoma kluczami: "input_data" oraz "params". Wartość "input_data" to kolejny słownik z kluczami "input_string" oraz "parameters". Wartość "input_string" to lista zawierająca pierwszą wiadomość z DataFrame test_df. Wartość "parameters" to wcześniej utworzony słownik parameters. Wartość "params" to pusty słownik.

    - Otwiera plik o nazwie sample_score.json

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

### Wywoływanie endpointu

1. Ten skrypt Pythona wywołuje endpoint online w Azure Machine Learning, aby ocenić plik JSON. Oto co robi:

    - Wywołuje metodę invoke właściwości online_endpoints obiektu workspace_ml_client. Metoda ta służy do wysłania żądania do endpointu online i otrzymania odpowiedzi.

    - Określa nazwę endpointu i wdrożenia za pomocą argumentów endpoint_name oraz deployment_name. W tym przypadku nazwa endpointu jest przechowywana w zmiennej online_endpoint_name, a nazwa wdrożenia to "demo".

    - Określa ścieżkę do pliku JSON, który ma zostać oceniony, za pomocą argumentu request_file. W tym przypadku plik to ./ultrachat_200k_dataset/sample_score.json.

    - Przechowuje odpowiedź z endpointu w zmiennej response.

    - Wyświetla surową odpowiedź.

1. Podsumowując, ten skrypt wywołuje endpoint online w Azure Machine Learning, aby ocenić plik JSON i wyświetla odpowiedź.

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

## 9. Usuwanie endpointu online

1. Nie zapomnij usunąć endpointu online, w przeciwnym razie będziesz naliczany za wykorzystanie zasobów obliczeniowych przez endpoint. Ta linia kodu Pythona usuwa endpoint online w Azure Machine Learning. Oto co robi:

    - Wywołuje metodę begin_delete właściwości online_endpoints obiektu workspace_ml_client. Metoda ta służy do rozpoczęcia usuwania endpointu online.

    - Określa nazwę endpointu do usunięcia za pomocą argumentu name. W tym przypadku nazwa endpointu jest przechowywana w zmiennej online_endpoint_name.

    - Wywołuje metodę wait, aby poczekać na zakończenie operacji usuwania. Jest to operacja blokująca, co oznacza, że skrypt nie będzie kontynuowany, dopóki usuwanie się nie zakończy.

    - Podsumowując, ta linia kodu rozpoczyna usuwanie endpointu online w Azure Machine Learning i czeka na zakończenie operacji.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być traktowany jako źródło autorytatywne. W przypadku informacji o krytycznym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.