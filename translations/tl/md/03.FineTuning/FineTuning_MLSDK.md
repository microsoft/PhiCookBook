<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:38:02+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "tl"
}
-->
## Paano gamitin ang chat-completion components mula sa Azure ML system registry para i-fine tune ang isang modelo

Sa halimbawang ito, gagawin natin ang fine tuning ng Phi-3-mini-4k-instruct na modelo upang tapusin ang isang pag-uusap sa pagitan ng 2 tao gamit ang ultrachat_200k dataset.

![MLFineTune](../../../../translated_images/tl/MLFineTune.928d4c6b3767dd35.png)

Ipinapakita ng halimbawa kung paano magsagawa ng fine tuning gamit ang Azure ML SDK at Python, at pagkatapos ay ide-deploy ang fine tuned na modelo sa isang online endpoint para sa real time inference.

### Training data

Gagamitin natin ang ultrachat_200k dataset. Ito ay isang malakas na na-filter na bersyon ng UltraChat dataset at ginamit upang sanayin ang Zephyr-7B-β, isang makabagong 7b chat model.

### Modelo

Gagamitin natin ang Phi-3-mini-4k-instruct na modelo upang ipakita kung paano maaaring i-finetune ng user ang isang modelo para sa chat-completion na gawain. Kung binuksan mo ang notebook na ito mula sa isang partikular na model card, tandaan na palitan ang pangalan ng modelo.

### Mga Gawain

- Pumili ng modelo para i-fine tune.
- Pumili at suriin ang training data.
- I-configure ang fine tuning job.
- Patakbuhin ang fine tuning job.
- Suriin ang mga training at evaluation metrics.
- Irehistro ang fine tuned na modelo.
- I-deploy ang fine tuned na modelo para sa real time inference.
- Linisin ang mga resources.

## 1. Ihanda ang mga kinakailangan

- I-install ang mga dependencies
- Kumonekta sa AzureML Workspace. Alamin pa sa set up SDK authentication. Palitan ang <WORKSPACE_NAME>, <RESOURCE_GROUP> at <SUBSCRIPTION_ID> sa ibaba.
- Kumonekta sa azureml system registry
- Magtakda ng opsyonal na pangalan ng eksperimento
- Suriin o gumawa ng compute.

> [!NOTE]
> Kinakailangan ang isang GPU node na maaaring magkaroon ng maraming GPU cards. Halimbawa, sa isang node ng Standard_NC24rs_v3 ay may 4 NVIDIA V100 GPUs habang sa Standard_NC12s_v3 ay may 2 NVIDIA V100 GPUs. Tingnan ang docs para sa impormasyong ito. Ang bilang ng GPU cards kada node ay itinakda sa param na gpus_per_node sa ibaba. Ang tamang pag-set ng value na ito ay titiyak ng paggamit ng lahat ng GPUs sa node. Ang mga inirerekomendang GPU compute SKUs ay makikita dito at dito.

### Mga Python Libraries

I-install ang mga dependencies sa pamamagitan ng pagpapatakbo ng cell sa ibaba. Hindi ito opsyonal kung tumatakbo sa bagong environment.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Pakikipag-ugnayan sa Azure ML

1. Ang Python script na ito ay ginagamit para makipag-ugnayan sa Azure Machine Learning (Azure ML) service. Narito ang paliwanag ng ginagawa nito:

    - Ina-import nito ang mga kinakailangang modules mula sa azure.ai.ml, azure.identity, at azure.ai.ml.entities packages. Ina-import din ang time module.

    - Sinusubukan nitong mag-authenticate gamit ang DefaultAzureCredential(), na nagbibigay ng pinasimpleng authentication para mabilis makapagsimula sa pag-develop ng mga aplikasyon na tumatakbo sa Azure cloud. Kapag nabigo ito, bumabalik ito sa InteractiveBrowserCredential(), na nagbibigay ng interactive login prompt.

    - Sinusubukan nitong gumawa ng MLClient instance gamit ang from_config method, na nagbabasa ng configuration mula sa default config file (config.json). Kapag nabigo ito, gumagawa ito ng MLClient instance sa pamamagitan ng manu-manong pagbibigay ng subscription_id, resource_group_name, at workspace_name.

    - Gumagawa ito ng isa pang MLClient instance, para sa Azure ML registry na pinangalanang "azureml". Dito naka-imbak ang mga modelo, fine-tuning pipelines, at mga environment.

    - Itinakda ang experiment_name sa "chat_completion_Phi-3-mini-4k-instruct".

    - Gumagawa ito ng natatanging timestamp sa pamamagitan ng pag-convert ng kasalukuyang oras (sa segundo mula nang epoch, bilang floating point number) sa integer at pagkatapos ay string. Magagamit ang timestamp na ito para gumawa ng natatanging mga pangalan at bersyon.

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

## 2. Pumili ng foundation model para i-fine tune

1. Ang Phi-3-mini-4k-instruct ay isang 3.8B parameters, magaan, makabagong open model na binuo gamit ang mga dataset na ginamit para sa Phi-2. Ang modelo ay kabilang sa Phi-3 model family, at ang Mini version ay may dalawang variant na 4K at 128K na siyang haba ng context (sa tokens) na kaya nitong suportahan. Kailangan nating i-finetune ang modelo para sa ating partikular na layunin bago ito magamit. Maaari mong tingnan ang mga modelong ito sa Model Catalog sa AzureML Studio, gamit ang filter para sa chat-completion task. Sa halimbawang ito, ginagamit natin ang Phi-3-mini-4k-instruct na modelo. Kung binuksan mo ang notebook na ito para sa ibang modelo, palitan ang pangalan at bersyon ng modelo nang naaayon.

    > [!NOTE]
    > ang model id property ng modelo. Ito ang ipapasa bilang input sa fine tuning job. Makikita rin ito bilang Asset ID field sa model details page sa AzureML Studio Model Catalog.

2. Ang Python script na ito ay nakikipag-ugnayan sa Azure Machine Learning (Azure ML) service. Narito ang paliwanag ng ginagawa nito:

    - Itinakda ang model_name sa "Phi-3-mini-4k-instruct".

    - Ginagamit ang get method ng models property ng registry_ml_client object para kunin ang pinakabagong bersyon ng modelo na may tinukoy na pangalan mula sa Azure ML registry. Tinatawag ang get method gamit ang dalawang argumento: ang pangalan ng modelo at isang label na nagsasaad na ang pinakabagong bersyon ng modelo ang kukunin.

    - Nagpi-print ito ng mensahe sa console na nagsasaad ng pangalan, bersyon, at id ng modelong gagamitin para sa fine-tuning. Ginagamit ang format method ng string para ipasok ang pangalan, bersyon, at id ng modelo sa mensahe. Ang pangalan, bersyon, at id ng modelo ay ina-access bilang mga property ng foundation_model object.

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

## 3. Gumawa ng compute na gagamitin sa job

Ang finetune job ay gumagana LAMANG sa GPU compute. Ang laki ng compute ay depende sa laki ng modelo at kadalasan ay mahirap tukuyin ang tamang compute para sa job. Sa cell na ito, gagabayan ang user sa pagpili ng tamang compute para sa job.

> [!NOTE]
> Ang mga compute na nakalista sa ibaba ay gumagana sa pinaka-optimal na configuration. Anumang pagbabago sa configuration ay maaaring magdulot ng Cuda Out Of Memory error. Sa ganitong mga kaso, subukang i-upgrade ang compute sa mas malaking compute size.

> [!NOTE]
> Sa pagpili ng compute_cluster_size sa ibaba, siguraduhing available ang compute sa iyong resource group. Kung hindi available ang isang partikular na compute, maaari kang mag-request para makakuha ng access sa compute resources.

### Pagsusuri kung sinusuportahan ng Modelo ang Fine Tuning

1. Ang Python script na ito ay nakikipag-ugnayan sa isang Azure Machine Learning (Azure ML) model. Narito ang paliwanag ng ginagawa nito:

    - Ina-import ang ast module, na nagbibigay ng mga function para iproseso ang mga puno ng Python abstract syntax grammar.

    - Sinusuri kung ang foundation_model object (na kumakatawan sa isang modelo sa Azure ML) ay may tag na finetune_compute_allow_list. Ang mga tag sa Azure ML ay mga key-value pairs na maaari mong likhain at gamitin para i-filter at ayusin ang mga modelo.

    - Kung naroroon ang finetune_compute_allow_list tag, ginagamit ang ast.literal_eval function para ligtas na i-parse ang value ng tag (isang string) sa isang Python list. Ang listahang ito ay itinalaga sa computes_allow_list variable. Nagpi-print ito ng mensahe na nagsasaad na dapat gumawa ng compute mula sa listahan.

    - Kung wala ang finetune_compute_allow_list tag, itinatakda ang computes_allow_list sa None at nagpi-print ng mensahe na nagsasaad na hindi bahagi ng mga tag ng modelo ang finetune_compute_allow_list.

    - Sa kabuuan, sinusuri ng script na ito ang isang partikular na tag sa metadata ng modelo, kino-convert ang value ng tag sa listahan kung ito ay naroroon, at nagbibigay ng feedback sa user.

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

### Pagsusuri ng Compute Instance

1. Ang Python script na ito ay nakikipag-ugnayan sa Azure Machine Learning (Azure ML) service at nagsasagawa ng ilang pagsusuri sa isang compute instance. Narito ang paliwanag ng ginagawa nito:

    - Sinusubukang kunin ang compute instance na may pangalang naka-imbak sa compute_cluster mula sa Azure ML workspace. Kung ang provisioning state ng compute instance ay "failed", nagta-throw ito ng ValueError.

    - Sinusuri kung ang computes_allow_list ay hindi None. Kung hindi, kino-convert nito ang lahat ng compute sizes sa listahan sa lowercase at tinitingnan kung ang laki ng kasalukuyang compute instance ay nasa listahan. Kung hindi, nagta-throw ito ng ValueError.

    - Kung ang computes_allow_list ay None, sinusuri nito kung ang laki ng compute instance ay nasa listahan ng mga hindi suportadong GPU VM sizes. Kung oo, nagta-throw ito ng ValueError.

    - Kinukuha nito ang listahan ng lahat ng available na compute sizes sa workspace. Ini-iterate nito ang listahan, at para sa bawat compute size, tinitingnan kung ang pangalan nito ay tumutugma sa laki ng kasalukuyang compute instance. Kung oo, kinukuha nito ang bilang ng GPUs para sa compute size na iyon at itinatakda ang gpu_count_found sa True.

    - Kung ang gpu_count_found ay True, nagpi-print ito ng bilang ng GPUs sa compute instance. Kung False, nagta-throw ito ng ValueError.

    - Sa kabuuan, nagsasagawa ang script na ito ng ilang pagsusuri sa isang compute instance sa Azure ML workspace, kabilang ang pagsusuri sa provisioning state, laki laban sa allow list o deny list, at bilang ng GPUs nito.

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

## 4. Pumili ng dataset para sa fine-tuning ng modelo

1. Gagamitin natin ang ultrachat_200k dataset. Ang dataset ay may apat na bahagi, angkop para sa Supervised fine-tuning (sft).
Generation ranking (gen). Ang bilang ng mga halimbawa kada bahagi ay ipinapakita sa ibaba:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Ang mga susunod na ilang cell ay nagpapakita ng basic na paghahanda ng data para sa fine tuning:

### Ipakita ang ilang mga hilera ng data

Gusto nating mabilis tumakbo ang sample na ito, kaya i-save ang train_sft, test_sft files na naglalaman ng 5% ng mga na-trim na hilera. Ibig sabihin, ang fine tuned na modelo ay magkakaroon ng mas mababang accuracy, kaya hindi ito dapat gamitin sa totoong mundo.
Ang download-dataset.py ay ginagamit para i-download ang ultrachat_200k dataset at i-transform ang dataset sa format na maaaring gamitin ng finetune pipeline component. Dahil malaki ang dataset, dito ay bahagi lamang ng dataset ang mayroon tayo.

1. Ang pagpapatakbo ng script sa ibaba ay nagda-download lamang ng 5% ng data. Maaari itong dagdagan sa pamamagitan ng pagbabago ng dataset_split_pc parameter sa nais na porsyento.

    > [!NOTE]
    > Ang ilang language models ay may iba't ibang language codes kaya ang mga pangalan ng column sa dataset ay dapat sumalamin dito.

1. Narito ang halimbawa kung paano dapat magmukha ang data
Ang chat-completion dataset ay nakaimbak sa parquet format kung saan ang bawat entry ay gumagamit ng sumusunod na schema:

    - Ito ay isang JSON (JavaScript Object Notation) na dokumento, isang popular na format ng pagpapalitan ng data. Hindi ito executable code, kundi paraan ng pag-iimbak at pagdadala ng data. Narito ang paliwanag ng istruktura nito:

    - "prompt": Ang key na ito ay naglalaman ng string na kumakatawan sa isang gawain o tanong na ibinibigay sa AI assistant.

    - "messages": Ang key na ito ay naglalaman ng array ng mga object. Bawat object ay kumakatawan sa isang mensahe sa pag-uusap sa pagitan ng user at AI assistant. Bawat message object ay may dalawang key:

    - "content": Ang key na ito ay naglalaman ng string na kumakatawan sa nilalaman ng mensahe.
    - "role": Ang key na ito ay naglalaman ng string na kumakatawan sa papel ng entity na nagpadala ng mensahe. Maaari itong "user" o "assistant".
    - "prompt_id": Ang key na ito ay naglalaman ng string na kumakatawan sa natatanging identifier para sa prompt.

1. Sa partikular na JSON document na ito, isang pag-uusap ang inilalarawan kung saan ang user ay humihiling sa AI assistant na gumawa ng pangunahing tauhan para sa isang dystopian na kwento. Sumagot ang assistant, at pagkatapos ay humiling ang user ng karagdagang detalye. Pumayag ang assistant na magbigay ng karagdagang detalye. Ang buong pag-uusap ay naka-ugnay sa isang partikular na prompt id.

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

### I-download ang Data

1. Ang Python script na ito ay ginagamit para i-download ang isang dataset gamit ang helper script na download-dataset.py. Narito ang paliwanag ng ginagawa nito:

    - Ina-import ang os module, na nagbibigay ng portable na paraan para gamitin ang mga functionality na nakadepende sa operating system.

    - Ginagamit ang os.system function para patakbuhin ang download-dataset.py script sa shell na may partikular na mga command-line arguments. Tinukoy ng mga argumento ang dataset na ida-download (HuggingFaceH4/ultrachat_200k), ang directory kung saan ida-download (ultrachat_200k_dataset), at ang porsyento ng dataset na hahatiin (5). Ibinabalik ng os.system function ang exit status ng command na pinatakbo; ang status na ito ay itinalaga sa exit_status variable.

    - Sinusuri kung ang exit_status ay hindi 0. Sa mga Unix-like operating system, ang exit status na 0 ay karaniwang nangangahulugang matagumpay ang command, habang ang ibang numero ay nagpapahiwatig ng error. Kung hindi 0 ang exit_status, nagta-throw ito ng Exception na may mensahe na may error sa pag-download ng dataset.

    - Sa kabuuan, pinapatakbo ng script na ito ang isang command para i-download ang dataset gamit ang helper script, at nagta-throw ng exception kung nabigo ang command.

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

### Pag-load ng Data sa isang DataFrame

1. Ang Python script na ito ay naglo-load ng JSON Lines file sa isang pandas DataFrame at ipinapakita ang unang 5 hilera. Narito ang paliwanag ng ginagawa nito:

    - Ina-import ang pandas library, isang makapangyarihang library para sa manipulasyon at pagsusuri ng data.

    - Itinakda ang maximum column width para sa pandas' display options sa 0. Ibig sabihin, ipapakita ang buong teksto ng bawat column nang hindi pinapaikli kapag na-print ang DataFrame. 

    - Ginagamit ang pd.read_json function para i-load ang train_sft.jsonl file mula sa ultrachat_200k_dataset directory papunta sa isang DataFrame. Ang lines=True argument ay nagsasaad na ang file ay nasa JSON Lines format, kung saan bawat linya ay isang hiwalay na JSON object.
- Ginagamit nito ang head method para ipakita ang unang 5 hilera ng DataFrame. Kung ang DataFrame ay may mas kaunting 5 hilera, ipapakita nito lahat ng iyon.

- Sa kabuuan, ang script na ito ay naglo-load ng JSON Lines file sa isang DataFrame at ipinapakita ang unang 5 hilera na may buong teksto ng mga kolum.

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

## 5. Isumite ang fine tuning job gamit ang modelo at data bilang inputs

Gumawa ng job na gumagamit ng chat-completion pipeline component. Alamin pa ang tungkol sa lahat ng mga parameter na sinusuportahan para sa fine tuning.

### Tukuyin ang mga finetune parameters

1. Ang mga finetune parameters ay maaaring hatiin sa 2 kategorya - training parameters, optimization parameters

1. Ang training parameters ay naglalarawan ng mga aspeto ng pagsasanay tulad ng -

    - Ang optimizer, scheduler na gagamitin
    - Ang metric na i-o-optimize sa finetune
    - Bilang ng mga training steps at batch size, at iba pa
    - Ang optimization parameters ay tumutulong sa pag-optimize ng GPU memory at epektibong paggamit ng compute resources.

1. Narito ang ilan sa mga parameter na kabilang sa kategoryang ito. Ang optimization parameters ay nagkakaiba-iba depende sa modelo at kasama sa package ng modelo upang hawakan ang mga pagkakaibang ito.

    - Paganahin ang deepspeed at LoRA
    - Paganahin ang mixed precision training
    - Paganahin ang multi-node training


> [!NOTE]
> Ang supervised finetuning ay maaaring magresulta sa pagkawala ng alignment o catastrophic forgetting. Inirerekomenda naming suriin ang isyung ito at magsagawa ng alignment stage pagkatapos ng finetune.

### Fine Tuning Parameters

1. Ang Python script na ito ay nagse-set up ng mga parameter para sa fine-tuning ng isang machine learning model. Narito ang paliwanag ng ginagawa nito:

    - Ise-set nito ang mga default training parameters tulad ng bilang ng training epochs, batch sizes para sa training at evaluation, learning rate, at uri ng learning rate scheduler.

    - Ise-set nito ang mga default optimization parameters tulad ng kung gagamitin ang Layer-wise Relevance Propagation (LoRa) at DeepSpeed, at ang DeepSpeed stage.

    - Pinagsasama nito ang training at optimization parameters sa isang dictionary na tinatawag na finetune_parameters.

    - Sinusuri nito kung ang foundation_model ay may mga model-specific default parameters. Kung mayroon, magpi-print ito ng warning message at ia-update ang finetune_parameters dictionary gamit ang mga model-specific defaults. Ginagamit ang ast.literal_eval para i-convert ang mga model-specific defaults mula sa string papuntang Python dictionary.

    - Ipinapakita nito ang panghuling set ng fine-tuning parameters na gagamitin para sa run.

    - Sa kabuuan, ang script na ito ay nagse-set up at nagpapakita ng mga parameter para sa fine-tuning ng isang machine learning model, na may kakayahang palitan ang default parameters gamit ang mga model-specific na parameter.

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

### Training Pipeline

1. Ang Python script na ito ay nagdedeklara ng isang function para gumawa ng display name para sa isang machine learning training pipeline, at pagkatapos ay tinatawag ang function na ito para gumawa at i-print ang display name. Narito ang paliwanag ng ginagawa nito:

1. Ipinapahayag ang get_pipeline_display_name function. Ang function na ito ay gumagawa ng display name base sa iba't ibang parameter na may kinalaman sa training pipeline.

1. Sa loob ng function, kinukwenta nito ang total batch size sa pamamagitan ng pag-multiply ng per-device batch size, bilang ng gradient accumulation steps, bilang ng GPUs kada node, at bilang ng nodes na ginagamit para sa fine-tuning.

1. Kinukuha nito ang iba pang mga parameter tulad ng learning rate scheduler type, kung ginagamit ang DeepSpeed, ang DeepSpeed stage, kung ginagamit ang Layer-wise Relevance Propagation (LoRa), ang limitasyon sa bilang ng model checkpoints na itatago, at ang maximum sequence length.

1. Gumagawa ito ng string na naglalaman ng lahat ng mga parameter na ito, na pinaghiwalay ng hyphens. Kung ginagamit ang DeepSpeed o LoRa, isinasama sa string ang "ds" kasunod ang DeepSpeed stage, o "lora", ayon sa pagkakasunod. Kung hindi, isinasama ang "nods" o "nolora", ayon sa pagkakasunod.

1. Ibinabalik ng function ang string na ito, na nagsisilbing display name para sa training pipeline.

1. Pagkatapos ideklara ang function, tinatawag ito para gumawa ng display name, na pagkatapos ay ini-print.

1. Sa kabuuan, ang script na ito ay gumagawa ng display name para sa isang machine learning training pipeline base sa iba't ibang parameter, at pagkatapos ay ini-print ang display name.

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

### Pag-configure ng Pipeline

Ang Python script na ito ay nagdedeklara at nagko-configure ng isang machine learning pipeline gamit ang Azure Machine Learning SDK. Narito ang paliwanag ng ginagawa nito:

1. Nag-iimport ng mga kinakailangang module mula sa Azure AI ML SDK.

1. Kinukuha ang isang pipeline component na pinangalanang "chat_completion_pipeline" mula sa registry.

1. Nagdedeklara ng pipeline job gamit ang `@pipeline` decorator at ang function na `create_pipeline`. Ang pangalan ng pipeline ay itinakda bilang `pipeline_display_name`.

1. Sa loob ng `create_pipeline` function, ini-initialize ang nakuha na pipeline component gamit ang iba't ibang parameter, kabilang ang model path, compute clusters para sa iba't ibang yugto, dataset splits para sa training at testing, bilang ng GPUs na gagamitin para sa fine-tuning, at iba pang fine-tuning parameters.

1. Ina-map nito ang output ng fine-tuning job sa output ng pipeline job. Ginagawa ito upang madaling mairehistro ang fine-tuned model, na kinakailangan para i-deploy ang modelo sa online o batch endpoint.

1. Gumagawa ng instance ng pipeline sa pamamagitan ng pagtawag sa `create_pipeline` function.

1. Itinakda ang `force_rerun` setting ng pipeline sa `True`, ibig sabihin ay hindi gagamitin ang cached results mula sa mga naunang job.

1. Itinakda ang `continue_on_step_failure` setting ng pipeline sa `False`, ibig sabihin ay hihinto ang pipeline kung may anumang hakbang na mabigo.

1. Sa kabuuan, ang script na ito ay nagdedeklara at nagko-configure ng isang machine learning pipeline para sa chat completion task gamit ang Azure Machine Learning SDK.

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

### Isumite ang Job

1. Ang Python script na ito ay nagsusumite ng machine learning pipeline job sa isang Azure Machine Learning workspace at pagkatapos ay naghihintay na matapos ang job. Narito ang paliwanag ng ginagawa nito:

    - Tinatawag nito ang create_or_update method ng jobs object sa workspace_ml_client para isumite ang pipeline job. Ang pipeline na tatakbuhin ay tinutukoy ng pipeline_object, at ang experiment kung saan tatakbo ang job ay tinutukoy ng experiment_name.

    - Pagkatapos, tinatawag nito ang stream method ng jobs object sa workspace_ml_client para maghintay na matapos ang pipeline job. Ang job na hinihintay ay tinutukoy ng name attribute ng pipeline_job object.

    - Sa kabuuan, ang script na ito ay nagsusumite ng machine learning pipeline job sa isang Azure Machine Learning workspace, at pagkatapos ay naghihintay na matapos ang job.

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

## 6. Irehistro ang fine tuned model sa workspace

Ire-rehistro natin ang modelo mula sa output ng fine tuning job. Ito ay magtatala ng lineage sa pagitan ng fine tuned model at ng fine tuning job. Ang fine tuning job naman ay sumusubaybay ng lineage sa foundation model, data, at training code.

### Pagrehistro ng ML Model

1. Ang Python script na ito ay nagrerehistro ng isang machine learning model na na-train sa isang Azure Machine Learning pipeline. Narito ang paliwanag ng ginagawa nito:

    - Nag-iimport ng mga kinakailangang module mula sa Azure AI ML SDK.

    - Sinusuri kung available ang trained_model output mula sa pipeline job sa pamamagitan ng pagtawag sa get method ng jobs object sa workspace_ml_client at pag-access sa outputs attribute nito.

    - Gumagawa ng path papunta sa trained model sa pamamagitan ng pag-format ng string gamit ang pangalan ng pipeline job at pangalan ng output ("trained_model").

    - Nagde-define ng pangalan para sa fine-tuned model sa pamamagitan ng pagdagdag ng "-ultrachat-200k" sa orihinal na pangalan ng modelo at pagpapalit ng anumang slash ng hyphens.

    - Naghahanda para irehistro ang modelo sa pamamagitan ng paggawa ng Model object na may iba't ibang parameter, kabilang ang path ng modelo, uri ng modelo (MLflow model), pangalan at bersyon ng modelo, at isang deskripsyon ng modelo.

    - Ire-rehistro ang modelo sa pamamagitan ng pagtawag sa create_or_update method ng models object sa workspace_ml_client gamit ang Model object bilang argumento.

    - Ipinapakita ang narehistrong modelo.

1. Sa kabuuan, ang script na ito ay nagrerehistro ng isang machine learning model na na-train sa isang Azure Machine Learning pipeline.

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

## 7. I-deploy ang fine tuned model sa isang online endpoint

Ang mga online endpoint ay nagbibigay ng matibay na REST API na maaaring gamitin para sa integrasyon sa mga aplikasyon na kailangang gumamit ng modelo.

### Pamahalaan ang Endpoint

1. Ang Python script na ito ay lumilikha ng isang managed online endpoint sa Azure Machine Learning para sa isang narehistrong modelo. Narito ang paliwanag ng ginagawa nito:

    - Nag-iimport ng mga kinakailangang module mula sa Azure AI ML SDK.

    - Nagde-define ng natatanging pangalan para sa online endpoint sa pamamagitan ng pagdagdag ng timestamp sa string na "ultrachat-completion-".

    - Naghahanda para gumawa ng online endpoint sa pamamagitan ng paggawa ng ManagedOnlineEndpoint object na may iba't ibang parameter, kabilang ang pangalan ng endpoint, deskripsyon ng endpoint, at authentication mode ("key").

    - Lumilikha ng online endpoint sa pamamagitan ng pagtawag sa begin_create_or_update method ng workspace_ml_client gamit ang ManagedOnlineEndpoint object bilang argumento. Pagkatapos ay naghihintay sa pagkumpleto ng operasyon gamit ang wait method.

1. Sa kabuuan, ang script na ito ay lumilikha ng isang managed online endpoint sa Azure Machine Learning para sa isang narehistrong modelo.

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
> Makikita dito ang listahan ng mga SKU na sinusuportahan para sa deployment - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Pag-deploy ng ML Model

1. Ang Python script na ito ay nagde-deploy ng isang narehistrong machine learning model sa isang managed online endpoint sa Azure Machine Learning. Narito ang paliwanag ng ginagawa nito:

    - Nag-iimport ng ast module, na nagbibigay ng mga function para iproseso ang mga puno ng Python abstract syntax grammar.

    - Itinakda ang instance type para sa deployment bilang "Standard_NC6s_v3".

    - Sinusuri kung ang inference_compute_allow_list tag ay naroroon sa foundation model. Kung oo, kino-convert ang tag value mula sa string papuntang Python list at itinatakda sa inference_computes_allow_list. Kung wala, itinatakda ito sa None.

    - Sinusuri kung ang tinukoy na instance type ay nasa allow list. Kung hindi, nagpi-print ito ng mensahe na hinihikayat ang user na pumili ng instance type mula sa allow list.

    - Naghahanda para gumawa ng deployment sa pamamagitan ng paggawa ng ManagedOnlineDeployment object na may iba't ibang parameter, kabilang ang pangalan ng deployment, pangalan ng endpoint, ID ng modelo, instance type at bilang, liveness probe settings, at request settings.

    - Lumilikha ng deployment sa pamamagitan ng pagtawag sa begin_create_or_update method ng workspace_ml_client gamit ang ManagedOnlineDeployment object bilang argumento. Pagkatapos ay naghihintay sa pagkumpleto ng operasyon gamit ang wait method.

    - Itinakda ang traffic ng endpoint upang idirekta ang 100% ng traffic sa "demo" deployment.

    - Ina-update ang endpoint sa pamamagitan ng pagtawag sa begin_create_or_update method ng workspace_ml_client gamit ang endpoint object bilang argumento. Pagkatapos ay naghihintay sa pagkumpleto ng update gamit ang result method.

1. Sa kabuuan, ang script na ito ay nagde-deploy ng isang narehistrong machine learning model sa isang managed online endpoint sa Azure Machine Learning.

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

## 8. Subukan ang endpoint gamit ang sample data

Kukunin natin ang ilang sample data mula sa test dataset at isusumite ito sa online endpoint para sa inference. Ipapakita natin ang mga scored labels kasabay ng ground truth labels.

### Pagbasa ng mga resulta

1. Ang Python script na ito ay nagbabasa ng JSON Lines file papunta sa isang pandas DataFrame, kumukuha ng random sample, at nire-reset ang index. Narito ang paliwanag ng ginagawa nito:

    - Binabasa nito ang file na ./ultrachat_200k_dataset/test_gen.jsonl papunta sa isang pandas DataFrame. Ginagamit ang read_json function na may argument na lines=True dahil ang file ay nasa JSON Lines format, kung saan bawat linya ay isang hiwalay na JSON object.

    - Kumukuha ito ng random sample na 1 hilera mula sa DataFrame. Ginagamit ang sample function na may argument na n=1 para tukuyin ang bilang ng random na hilera na pipiliin.

    - Nirereset nito ang index ng DataFrame. Ginagamit ang reset_index function na may argument na drop=True para alisin ang orihinal na index at palitan ito ng bagong index na default na mga integer.

    - Ipinapakita nito ang unang 2 hilera ng DataFrame gamit ang head function na may argument na 2. Ngunit dahil ang DataFrame ay may isang hilera lamang pagkatapos ng sampling, ipapakita lamang nito ang isang hilera.

1. Sa kabuuan, ang script na ito ay nagbabasa ng JSON Lines file papunta sa isang pandas DataFrame, kumukuha ng random sample na 1 hilera, nire-reset ang index, at ipinapakita ang unang hilera.

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

### Gumawa ng JSON Object

1. Ang Python script na ito ay gumagawa ng isang JSON object na may partikular na mga parameter at sine-save ito sa isang file. Narito ang paliwanag ng ginagawa nito:

    - Nag-iimport ng json module, na nagbibigay ng mga function para magtrabaho sa JSON data.

    - Gumagawa ng dictionary na parameters na may mga key at value na kumakatawan sa mga parameter para sa isang machine learning model. Ang mga key ay "temperature", "top_p", "do_sample", at "max_new_tokens", at ang mga katumbas na value ay 0.6, 0.9, True, at 200 ayon sa pagkakasunod.

    - Gumagawa ng isa pang dictionary na test_json na may dalawang key: "input_data" at "params". Ang value ng "input_data" ay isa pang dictionary na may mga key na "input_string" at "parameters". Ang value ng "input_string" ay isang listahan na naglalaman ng unang mensahe mula sa test_df DataFrame. Ang value ng "parameters" ay ang parameters dictionary na ginawa kanina. Ang value ng "params" ay isang walang lamang dictionary.
- Binubuksan nito ang isang file na pinangalanang sample_score.json

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

### Pagtawag sa Endpoint

1. Ang Python script na ito ay tumatawag sa isang online endpoint sa Azure Machine Learning upang i-score ang isang JSON file. Narito ang paliwanag ng mga ginagawa nito:

    - Tinatawag nito ang invoke method ng online_endpoints property ng workspace_ml_client object. Ginagamit ang method na ito para magpadala ng request sa isang online endpoint at makatanggap ng tugon.

    - Itinatakda nito ang pangalan ng endpoint at deployment gamit ang endpoint_name at deployment_name na mga argumento. Sa kasong ito, ang pangalan ng endpoint ay naka-imbak sa online_endpoint_name variable at ang pangalan ng deployment ay "demo".

    - Itinatakda nito ang path papunta sa JSON file na i-score gamit ang request_file na argumento. Sa kasong ito, ang file ay ./ultrachat_200k_dataset/sample_score.json.

    - Iniimbak nito ang tugon mula sa endpoint sa response variable.

    - Ipinapakita nito ang raw na tugon.

1. Sa kabuuan, ang script na ito ay tumatawag sa isang online endpoint sa Azure Machine Learning upang i-score ang isang JSON file at ipinapakita ang tugon.

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

## 9. Tanggalin ang online endpoint

1. Huwag kalimutang tanggalin ang online endpoint, kung hindi ay patuloy na tatakbo ang billing meter para sa compute na ginamit ng endpoint. Ang linyang ito ng Python code ay nagtatanggal ng isang online endpoint sa Azure Machine Learning. Narito ang paliwanag ng mga ginagawa nito:

    - Tinatawag nito ang begin_delete method ng online_endpoints property ng workspace_ml_client object. Ginagamit ang method na ito para simulan ang pagtanggal ng isang online endpoint.

    - Itinatakda nito ang pangalan ng endpoint na tatanggalin gamit ang name na argumento. Sa kasong ito, ang pangalan ng endpoint ay naka-imbak sa online_endpoint_name variable.

    - Tinatawag nito ang wait method upang maghintay na matapos ang operasyon ng pagtanggal. Ito ay isang blocking operation, ibig sabihin, pipigilan nito ang script na magpatuloy hanggang sa matapos ang pagtanggal.

    - Sa kabuuan, ang linyang ito ng code ay nagsisimula ng pagtanggal ng isang online endpoint sa Azure Machine Learning at naghihintay na matapos ang operasyon.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.