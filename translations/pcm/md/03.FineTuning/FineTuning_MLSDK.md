## How to use chat-completion components wey dey for the Azure ML system registry to fine tune a model

For this example, we go do fine tuning of the Phi-3-mini-4k-instruct model make e fit complete conversation between 2 people using the ultrachat_200k dataset.

![ML Fine-Tune](../../../../translated_images/MLFineTune.928d4c6b3767dd35.pcm.png)

This example go show you how to do fine tuning using the Azure ML SDK and Python and after dat deploy the fine tuned model to an online endpoint for real-time inference.

### Training data

We go use the ultrachat_200k dataset. Dis one na heavily filtered version of the UltraChat dataset and na wetin dem use train Zephyr-7B-β, wey be state-of-the-art 7b chat model.

### Model

We go use the Phi-3-mini-4k-instruct model to show how person fit finetune model for chat-completion task. If you open this notebook from one specific model card, make you remember to change the specific model name.

### Tasks

- Choose model wey you wan fine tune.
- Choose and explore training data.
- Configure the fine tuning job.
- Run the fine tuning job.
- Check training and evaluation metrics.
- Register the fine tuned model.
- Deploy the fine tuned model for real-time inference.
- Clean up resources.

## 1. Setup pre-requisites

- Install dependencies
- Connect to AzureML Workspace. Learn more at set up SDK authentication. Replace <WORKSPACE_NAME>, <RESOURCE_GROUP> and <SUBSCRIPTION_ID> below.
- Connect to azureml system registry
- Set optional experiment name
- Check or create compute.

> [!NOTE]
> Requirement be say single GPU node fit get multiple GPU cards. For example, for one node of Standard_NC24rs_v3 get 4 NVIDIA V100 GPUs while for Standard_NC12s_v3 get 2 NVIDIA V100 GPUs. Check the docs for this info. The number of GPU cards per node na wetin you go set for the param gpus_per_node below. If you set am correct, e go make sure say all GPUs for the node dey utilized. The recommended GPU compute SKUs fit dey found here and here.

### Python Libraries

Install dependencies by running the cell below. This step no be optional if you dey run for new environment.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interacting with Azure ML

1. This Python script dey used to interact with Azure Machine Learning (Azure ML) service. Below na wetin e dey do:

    - E dey import necessary modules from the azure.ai.ml, azure.identity, and azure.ai.ml.entities packages. E still import the time module.

    - E dey try authenticate using DefaultAzureCredential(), wey dey provide simplified authentication experience make e quick to start developing applications wey go run for the Azure cloud. If this one fail, e go fallback to InteractiveBrowserCredential(), wey dey give interactive login prompt.

    - Then e go try create MLClient instance using the from_config method, wey dey read config from the default config file (config.json). If e no fit, e go create MLClient instance by manually providing the subscription_id, resource_group_name, and workspace_name.

    - E go create another MLClient instance, this time for the Azure ML registry named "azureml". Dis registry na where models, fine-tuning pipelines, and environments dey stored.

    - E set the experiment_name to "chat_completion_Phi-3-mini-4k-instruct".

    - E generate unique timestamp by converting the current time (in seconds since the epoch, as floating point number) to integer then to string. This timestamp fit dey used for create unique names and versions.

    ```python
    # Bring in di necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Bring in di time module
    
    # Try authenticate with DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential no work, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try create an MLClient instance using di default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If e fail, create an MLClient instance manually by giving di details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create anoda MLClient instance for di Azure ML registry wey dem call "azureml"
    # Dis registry na where models, fine-tuning pipelines, and environments dey stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set di experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate one unique timestamp wey you fit use for names and versions wey gats be unique
    timestamp = str(int(time.time()))
    ```

## 2. Pick a foundation model to fine tune

1. Phi-3-mini-4k-instruct na 3.8B parameters, lightweight, state-of-the-art open model wey dem build on top of datasets wey dem use for Phi-2. The model belong to the Phi-3 model family, and the Mini version get two variants 4K and 128K wey be the context length (in tokens) e fit support. We need to finetune the model for our specific purpose before we fit use am. You fit browse these models for the Model Catalog inside AzureML Studio, filter by the chat-completion task. For this example, we dey use the Phi-3-mini-4k-instruct model. If you open this notebook for different model, make you change the model name and version accordingly.

    > [!NOTE]
    > the model id property of the model. This one go pass as input to the fine tuning job. You go still see am as the Asset ID field for the model details page inside AzureML Studio Model Catalog.

2. This Python script dey interact with Azure Machine Learning (Azure ML) service. Below na wetin e dey do:

    - E set the model_name to "Phi-3-mini-4k-instruct".

    - E use the get method of the models property of the registry_ml_client object to retrieve the latest version of the model with the specified name from the Azure ML registry. The get method dey call with two arguments: the name of the model and a label wey dey specify say make e fetch the latest version.

    - E print message to the console wey show the name, version, and id of the model wey go use for fine-tuning. The format method of the string dey insert the name, version, and id of the model into the message. The name, version, and id of the model dey accessed as properties of the foundation_model object.

    ```python
    # Put di model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Bring di latest version of di model from di Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print di model name, version, and id
    # Dis information dey useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Create a compute to be used with the job

The finetune job dey work ONLY with GPU compute. The size of the compute depend on how big the model be and for most cases e fit hard to know the correct compute for the job. For this cell, we go guide the user to select the right compute for the job.

> [!NOTE]
> The computes wey dem list below dey work with the most optimized configuration. Any changes to the configuration fit cause Cuda Out Of Memory error. For such cases, try upgrade the compute to bigger compute size.

> [!NOTE]
> When you dey choose the compute_cluster_size below, make sure say the compute dey available for your resource group. If particular compute no dey available you fit raise request to get access to the compute resources.

### Checking Model for Fine Tuning Support

1. This Python script dey interact with an Azure Machine Learning (Azure ML) model. Below na wetin e dey do:

    - E import the ast module, wey get functions to process trees of the Python abstract syntax grammar.

    - E check if the foundation_model object (wey represent model for Azure ML) get a tag named finetune_compute_allow_list. Tags for Azure ML na key-value pairs wey you fit create and use to filter and sort models.

    - If the finetune_compute_allow_list tag dey, e go use ast.literal_eval function to safely parse the tag's value (wey be string) into Python list. This list go assign to computes_allow_list variable. Then e go print message wey tell say compute suppose create from the list.

    - If the finetune_compute_allow_list tag no dey, e go set computes_allow_list to None and print message wey tell say finetune_compute_allow_list tag no dey part of the model's tags.

    - In short, this script dey check one specific tag for the model's metadata, convert the tag value to list if e dey, and then give feedback to the user.

    ```python
    # Import di ast module wey get functions to process tree dem of the Python abstract syntax grammar
    import ast
    
    # Check if di 'finetune_compute_allow_list' tag dey among di model tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If di tag dey, use ast.literal_eval make e safely parse di tag value (wey na string) convert am to Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert di string to Python list
        # Print message wey dey talk say dem suppose create compute from di list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If di tag no dey, set computes_allow_list to None
        computes_allow_list = None
        # Print message wey talk say 'finetune_compute_allow_list' tag no dey part of di model tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Checking Compute Instance

1. This Python script dey interact with Azure Machine Learning (Azure ML) service and e dey perform several checks on a compute instance. Below na wetin e dey do:

    - E try retrieve the compute instance wey get the name wey dey compute_cluster from the Azure ML workspace. If the compute instance provisioning state na "failed", e go raise ValueError.

    - E check if computes_allow_list no be None. If e no be None, e go convert all compute sizes for the list to lowercase and check if the size of the current compute instance dey the list. If e no dey, e go raise ValueError.

    - If computes_allow_list be None, e go check if the size of the compute instance dey inside list of unsupported GPU VM sizes. If e dey, e go raise ValueError.

    - E retrieve list of all available compute sizes for the workspace. Then e go iterate over dis list, and for each compute size, e check if its name match the size of the current compute instance. If e match, e go retrieve the number of GPUs for that compute size and set gpu_count_found to True.

    - If gpu_count_found be True, e go print the number of GPUs for the compute instance. If gpu_count_found be False, e go raise ValueError.

    - In short, this script dey perform multiple checks on a compute instance for an Azure ML workspace, including checking provisioning state, checking size against an allow list or deny list, and checking how many GPUs e get.
    
    ```python
    # Print di exception message
    print(e)
    # Raise ValueError if di compute size no dey for di workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve di compute instance from di Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if di provisioning state of di compute instance na "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise ValueError if di provisioning state na "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list no be None
    if computes_allow_list is not None:
        # Convert all compute sizes wey dey computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if di size of di compute instance dey for computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise ValueError if di size of di compute instance no dey for computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define list of GPU VM sizes wey no dey supported
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if di size of di compute instance dey for unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise ValueError if di size of di compute instance dey for unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize flag to know if dem don find how many GPUs dey for di compute instance
    gpu_count_found = False
    # Retrieve list of all available compute sizes wey dey for di workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Loop through di list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if di name of di compute size match di size of di compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If e do, get di number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found na True, print di number of GPUs for di compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found na False, raise ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Pick the dataset for fine-tuning the model

1. We dey use the ultrachat_200k dataset. The dataset get four splits, wey fit for Supervised fine-tuning (sft) and Generation ranking (gen). The number of examples per split dey shown as follows:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. The next few cells go show basic data preparation for fine tuning:

### Visualize some data rows

We want this sample to run quick, so save train_sft, test_sft files wey contain 5% of the already trimmed rows. This one mean the fine tuned model go get lower accuracy, so e no suppose put for real-world use.
The download-dataset.py dey used to download the ultrachat_200k dataset and transform the dataset into finetune pipeline component consumable format. Also because the dataset big, we only get part of the dataset here.

1. Running the script below go only download 5% of the data. You fit increase am by changing dataset_split_pc parameter to the percentage wey you want.

    > [!NOTE]
    > Some language models get different language codes and because of that the column names inside the dataset suppose reflect the same.

1. Here na example of how the data suppose look
The chat-completion dataset dey stored in parquet format with each entry using the following schema:

    - This one na JSON (JavaScript Object Notation) document, wey na popular data interchange format. E no be executable code, na just way to store and transport data. Below na breakdown of the structure:

    - "prompt": This key hold string value wey represent task or question wey dem give AI assistant.

    - "messages": This key hold array of objects. Each object represent one message inside conversation between user and AI assistant. Each message object get two keys:

    - "content": This key hold string value wey represent the content of the message.
    - "role": This key hold string value wey represent the role of the entity wey send the message. E fit be either "user" or "assistant".
    - "prompt_id": This key hold string value wey represent unique identifier for the prompt.

1. For this specific JSON document, the conversation dey show where user ask AI assistant to create protagonist for dystopian story. The assistant respond, then the user ask for more details. The assistant agree to provide more details. The whole conversation join with one specific prompt id.

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

### Download Data

1. This Python script dey used to download dataset using helper script wey dem call download-dataset.py. Below na wetin e dey do:

    - E import os module, wey provide portable way to run operating system dependent functionality.

    - E use os.system function to run download-dataset.py script for shell with specific command-line arguments. The arguments specify dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download to (ultrachat_200k_dataset), and the percentage of dataset to split (5). The os.system function go return exit status of the command; this status dey store for exit_status variable.

    - E check if exit_status no be 0. For Unix-like systems, exit status 0 usually mean command succeed, any other number mean error. If exit_status no be 0, e go raise Exception with message wey talk say error happen when downloading the dataset.

    - In short, this script dey run command to download dataset using helper script, and e go raise exception if the command fail.
    
    ```python
    # Import di os module wey dey provide way to use functions wey depend on di operating system
    import os
    
    # Use di os.system function to run di download-dataset.py script for di shell wit specific command-line arguments
    # Di arguments dey specify which dataset to download (HuggingFaceH4/ultrachat_200k), di directory to download to (ultrachat_200k_dataset), and di percentage of di dataset to split (5)
    # Di os.system function dey return di exit status of di command e run; dis status dem store for di exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status no be 0
    # For Unix-like operating systems, exit status 0 usually mean say di command succeed, any oda number mean error
    # If exit_status no be 0, raise an Exception wit message wey say error happen wen dem dey download di dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Loading Data into a DataFrame

1. This Python script dey load JSON Lines file into pandas DataFrame and display first 5 rows. Below na wetin e dey do:

    - E import pandas library, wey be powerful data manipulation and analysis library.

    - E set maximum column width for pandas' display options to 0. This one mean full text of each column go display without truncation when the DataFrame print.
    - E dey use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame. The lines=True argument mean say the file dey JSON Lines format, where each line na separate JSON object.

    - E dey use the head method to show the first 5 rows of the DataFrame. If the DataFrame get less than 5 rows, e go show all of dem.

    - Short-short, dis script dey load a JSON Lines file into a DataFrame and dey show the first 5 rows with full column text.
    
    ```python
    # Import di pandas library, wey na strong library for data manipulation and analysis
    import pandas as pd
    
    # Make di maximum column width for pandas display options be 0
    # Dis mean say di full text of each column go show without truncation when di DataFrame dey printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use pd.read_json function to load di train_sft.jsonl file from di ultrachat_200k_dataset directory into one DataFrame
    # The lines=True argument show say di file dey JSON Lines format, wey mean each line na separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use di head method to show di first 5 rows of di DataFrame
    # If di DataFrame get less than 5 rows, e go show all of dem
    df.head()
    ```

## 5. Submit di fine-tuning job wey dey use di model and data as inputs

Create the job wey dey use the chat-completion pipeline component. Find out more about all di parameters wey dem support for fine tuning.

### Define finetune parameters

1. Finetune parameters fit into 2 categories - training parameters, optimization parameters

1. Training parameters dey define the training aspects such as -

    - Which optimizer and scheduler we go use
    - Which metric we dey optimize for the finetune
    - How many training steps, batch size, etc.
    - Optimization parameters help balance GPU memory and make sure compute resources dey used well. 

1. Below na some of the parameters wey belong to this category. The optimization parameters dey different for each model and dem package dem with the model to handle those variations.

    - Enable deepspeed and LoRA
    - Enable mixed precision training
    - Enable multi-node training

> [!NOTE]
> Supervised finetuning fit cause loss of alignment or catastrophic forgetting. We recommend make you check for dis issue and run an alignment stage after you finetune.

### Fine Tuning Parameters

1. Dis Python script dey set up parameters for fine-tuning a machine learning model. Below na wetin e dey do:

    - E dey set up default training parameters like number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type.

    - E dey set up default optimization parameters like whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage.

    - E dey combine the training and optimization parameters into one dictionary called finetune_parameters.

    - E dey check if foundation_model get any model-specific default parameters. If e get, e go print warning message and update the finetune_parameters dictionary with those model-specific defaults. The ast.literal_eval function dey used to convert the model-specific defaults wey be string to Python dictionary.

    - E go print the final set of fine-tuning parameters wey dem go use for the run.

    - Short-short, dis script dey set up and show parameters for fine-tuning a machine learning model, and you fit override the default parameters with model-specific ones.

    ```python
    # Arrange di default training parameters like di number of training epochs, batch sizes for training and evaluation, learning rate, and di type of learning rate scheduler
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Arrange di default optimization parameters like whether dem go use Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and which DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine di training and optimization parameters into one dictionary wey dem call finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if di foundation_model get any model-specific default parameters
    # If e get, print one warning message and update di finetune_parameters dictionary with dem model-specific defaults
    # Di ast.literal_eval function dey used to convert di model-specific defaults from string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # Make string turn to Python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print di final set of fine-tuning parameters wey dem go use for di run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Training Pipeline

1. Dis Python script dey define function to generate display name for a machine learning training pipeline, then e dey call that function to generate and print the display name. Below na wetin e dey do:

1. The get_pipeline_display_name function dey defined. Dis function dey generate a display name based on different parameters wey relate to the training pipeline.

1. Inside the function, e dey calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes wey dem use for fine-tuning.

1. E dey fetch other parameters like the learning rate scheduler type, whether DeepSpeed dey applied, the DeepSpeed stage, whether Layer-wise Relevance Propagation (LoRa) dey applied, the limit on the number of model checkpoints to keep, and the maximum sequence length.

1. E dey build a string wey include all these parameters, separated by hyphens. If DeepSpeed or LoRa dey applied, the string go include "ds" followed by the DeepSpeed stage, or "lora", respectively. If not, e go include "nods" or "nolora", respectively.

1. The function go return this string, wey go serve as the display name for the training pipeline.

1. After dem define the function, dem go call am to generate the display name, wey dem go print.

1. Short-short, dis script dey generate a display name for a machine learning training pipeline based on various parameters, and then print this display name.

    ```python
    # Make one function wey go generate display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate di total batch size by multiply per-device batch size, gradient accumulation steps, GPUs per node, and number of nodes wey dem use for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Get di learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Check if DeepSpeed dey applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Get di DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed dey applied, put "ds" plus di DeepSpeed stage for di display name; if no, put "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Check if Layer-wise Relevance Propagation (LoRa) dey applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa dey applied, put "lora" for di display name; if no, put "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Get di limit for how many model checkpoints dem go keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Get di maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct di display name by joining all these parameters, separated by hyphens
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
    
    # Call di function to generate di display name
    pipeline_display_name = get_pipeline_display_name()
    # Print di display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Configuring Pipeline

Dis Python script dey define and configure a machine learning pipeline using the Azure Machine Learning SDK. Below na wetin e dey do:

1. E dey import di necessary modules from the Azure AI ML SDK.

1. E dey fetch pipeline component named "chat_completion_pipeline" from the registry.

1. E dey define a pipeline job using the `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, e dey initialize the fetched pipeline component with different parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. E map output of the fine-tuning job to the output of the pipeline job. This one dey do so that the fine-tuned model fit easily be registered, which dey required to deploy the model to an online or batch endpoint.

1. E create an instance of the pipeline by calling the `create_pipeline` function.

1. E set the `force_rerun` setting of the pipeline to `True`, mean say cached results from previous jobs no go dey used.

1. E set the `continue_on_step_failure` setting of the pipeline to `False`, mean say the pipeline go stop if any step fail.

1. Short-short, dis script dey define and configure a machine learning pipeline for a chat completion task using the Azure Machine Learning SDK.

    ```python
    # Import di necessary modules from di Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch di pipeline component wey dem name "chat_completion_pipeline" from di registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define di pipeline job using the @pipeline decorator and di function create_pipeline
    # Di name of di pipeline set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize di fetched pipeline component wit various parameters
        # Dem include di model path, compute clusters for different stages, dataset splits for training and testing, di number of GPUs to use for fine-tuning, and oda fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map di dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to di number of GPUs wey dey available for di compute
            **finetune_parameters
        )
        return {
            # Map di output of di fine-tuning job to di output of di pipeline job
            # Dis na to make we fit easily register di fine-tuned model
            # Register di model required to deploy am to online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create instance of di pipeline by calling di create_pipeline function
    pipeline_object = create_pipeline()
    
    # No use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # Dis mean say di pipeline go stop if any step fail
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Submit the Job

1. Dis Python script dey submit a machine learning pipeline job to an Azure Machine Learning workspace and then dey wait make the job complete. Below na wetin e dey do:

    - E go call create_or_update method of the jobs object in the workspace_ml_client to submit the pipeline job. The pipeline to be run dey specified by pipeline_object, and the experiment under which the job dey run dey specified by experiment_name.

    - Then e go call the stream method of the jobs object in the workspace_ml_client to wait for the pipeline job to complete. The job to wait for dey specified by the name attribute of the pipeline_job object.

    - Short-short, dis script dey submit a machine learning pipeline job to an Azure Machine Learning workspace, and then dey wait for the job to complete.

    ```python
    # Submit di pipeline job go di Azure Machine Learning workspace
    # Di pipeline wey go run na pipeline_object dey specify
    # Di experiment wey di job dey run under na experiment_name dey specify
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait make di pipeline job finish
    # Di job wey you dey wait for na di name attribute of di pipeline_job object dey specify
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Register di fine-tuned model with di workspace

We go register the model wey come from the output of the fine tuning job. Dis go track lineage between the fine-tuned model and the fine tuning job. The fine tuning job go still track lineage back to the foundation model, data and training code.

### Registering the ML Model

1. Dis Python script dey register a machine learning model wey dem train in an Azure Machine Learning pipeline. Below na wetin e dey do:

    - E dey import necessary modules from the Azure AI ML SDK.

    - E dey check if the trained_model output dey available from the pipeline job by calling the get method of the jobs object in the workspace_ml_client and accessing its outputs attribute.

    - E dey construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model").

    - E dey define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens.

    - E dey prepare to register the model by creating a Model object with various parameters, including the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model.

    - E dey register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument.

    - E print the registered model.

1. Short-short, dis script dey register a machine learning model wey dem train in an Azure Machine Learning pipeline.
    
    ```python
    # Import di necessary modules from di Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if `trained_model` output dey available from di pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to di trained model by formatting a string with di name of di pipeline job and di name of di output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for di fine-tuned model by appending "-ultrachat-200k" to di original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register di model by creating a Model object with various parameters
    # Dem include di path to di model, di type of di model (MLflow model), di name and version of di model, and one description of di model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version so e no go cause version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register di model by calling di create_or_update method of di models object in di workspace_ml_client with di Model object as di argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print di registered model
    print("registered model: \n", registered_model)
    ```

## 7. Deploy the fine-tuned model to an online endpoint

Online endpoints dey give a durable REST API wey fit be used to integrate with applications wey need to use the model.

### Manage Endpoint

1. Dis Python script dey create a managed online endpoint in Azure Machine Learning for a registered model. Below na wetin e dey do:

    - E import necessary modules from the Azure AI ML SDK.

    - E define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-".

    - E prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters, including the name of the endpoint, a description of the endpoint, and the authentication mode ("key").

    - E create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument. Then e wait for the creation operation to complete by calling the wait method.

1. Short-short, dis script dey create a managed online endpoint in Azure Machine Learning for a registered model.

    ```python
    # Import di necessary modules from di Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Make one unique name for di online endpoint by addin a timestamp to di string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Get ready to create di online endpoint by creating one ManagedOnlineEndpoint object wit various parameters
    # Dem include di name of di endpoint, one description for di endpoint, and di authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create di online endpoint by calling di begin_create_or_update method of di workspace_ml_client wit di ManagedOnlineEndpoint object as di argument
    # Then wait make di creation operation finish by calling di wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> You fit find here di list of SKU's wey dem support for deployment - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Deploying ML Model

1. Dis Python script dey deploy a registered machine learning model to a managed online endpoint in Azure Machine Learning. Below na wetin e dey do:

    - E import the ast module, wey provide functions to process trees of the Python abstract syntax grammar.

    - E set the instance type for the deployment to "Standard_NC6s_v3".

    - E check if the inference_compute_allow_list tag dey present in the foundation model. If e dey, e go convert the tag value from a string to a Python list and assign am to inference_computes_allow_list. If e no dey, e go set inference_computes_allow_list to None.

    - E check if the specified instance type dey for the allow list. If e no dey, e go print message wey ask the user make dem select an instance type from the allow list.

    - E prepare to create the deployment by creating a ManagedOnlineDeployment object with various parameters, including the name of the deployment, the name of the endpoint, the ID of the model, the instance type and count, the liveness probe settings, and the request settings.

    - E create the deployment by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineDeployment object as the argument. Then e wait for the creation operation to complete by calling the wait method.

    - E set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment.

    - E update the endpoint by calling the begin_create_or_update method of the workspace_ml_client with the endpoint object as the argument. Then e wait for the update operation to complete by calling the result method.

1. Short-short, dis script dey deploy a registered machine learning model to a managed online endpoint in Azure Machine Learning.

    ```python
    # Import di ast module, wey dey provide functions to process tree dem of the Python abstract syntax grammar
    import ast
    
    # Set di instance type for di deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if di `inference_compute_allow_list` tag dey for di foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If e dey, convert di tag value from string to Python list and assign am to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If e no dey, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if di specified instance type dey inside di allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create di deployment by making a `ManagedOnlineDeployment` object with different parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create di deployment by calling di `begin_create_or_update` method of di `workspace_ml_client` with di `ManagedOnlineDeployment` object as argument
    # Then wait make di creation operation finish by calling di `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set di traffic of di endpoint to direct 100% of di traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update di endpoint by calling di `begin_create_or_update` method of di `workspace_ml_client` with di `endpoint` object as argument
    # Then wait make di update operation finish by calling di `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Test di endpoint with sample data

We go fetch some sample data from the test dataset and submit am to online endpoint for inference. Then we go show the scored labels side-by-side with the ground truth labels

### Reading the results

1. Dis Python script dey read a JSON Lines file into a pandas DataFrame, take a random sample, and reset the index. Below na wetin e dey do:

    - E read the file ./ultrachat_200k_dataset/test_gen.jsonl into a pandas DataFrame. The read_json function dey used with the lines=True argument because the file dey JSON Lines format, where each line na a separate JSON object.

    - E take a random sample of 1 row from the DataFrame. The sample function dey used with the n=1 argument to specify the number of random rows to select.

    - E reset the index of the DataFrame. The reset_index function dey used with the drop=True argument to drop the original index and replace am with a new index of default integer values.

    - E display the first 2 rows of the DataFrame using the head function with the argument 2. But since the DataFrame only contain one row after the sampling, this go only display that one row.

1. Short-short, dis script dey read a JSON Lines file into a pandas DataFrame, take a random sample of 1 row, reset the index, and display the first row.
    
    ```python
    # Bring in pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' put am for pandas DataFrame
    # The 'lines=True' argument mean say the file na JSON Lines format, where every line na separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take one random row from the DataFrame
    # The 'n=1' argument dey show how many random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index for the DataFrame
    # The 'drop=True' argument mean make the original index comot and be replaced with new default integer values
    # The 'inplace=True' argument mean say the DataFrame go change for the same object (no create new one)
    test_df.reset_index(drop=True, inplace=True)
    
    # Show the first 2 rows of the DataFrame
    # But because the DataFrame get only one row after the sampling, e go just show that one row
    test_df.head(2)
    ```

### Create JSON Object

1. Dis Python script dey create a JSON object with specific parameters and save am to a file. Below na wetin e dey do:

    - E import the json module, wey provide functions to work with JSON data.
    - E dey create a dictionary parameters with keys and values wey represent parameters for a machine learning model. The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively.

    - E dey create another dictionary test_json with two keys: "input_data" and "params". The value of "input_data" is another dictionary with keys "input_string" and "parameters". The value of "input_string" is a list containing the first message from the test_df DataFrame. The value of "parameters" is the parameters dictionary created earlier. The value of "params" is an empty dictionary.

    - E dey open a file named sample_score.json
    
    ```python
    # Import di json module, wey dey provide functions to work with JSON data
    import json
    
    # Create one dictionary `parameters` with keys and values wey represent parameters for a machine learning model
    # The keys na "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values na 0.6, 0.9, True, and 200 in that order
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` wey get two keys: "input_data" and "params"
    # The value of "input_data" na another dictionary wey get keys "input_string" and "parameters"
    # The value of "input_string" na list wey contain the first message from the `test_df` DataFrame
    # The value of "parameters" na the `parameters` dictionary wey we create earlier
    # The value of "params" na empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open one file named `sample_score.json` for the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary inside the file as JSON using the `json.dump` function
        json.dump(test_json, f)
    ```

### How dem dey call Endpoint

1. This Python script dey call one online endpoint for Azure Machine Learning to score a JSON file. Here's a breakdown of what it does:

    - E dey call the invoke method of the online_endpoints property of the workspace_ml_client object. This method dey used to send a request to an online endpoint and get a response.

    - E dey specify the name of the endpoint and the deployment with the endpoint_name and deployment_name arguments. In this case, the endpoint name is stored in the online_endpoint_name variable and the deployment name is "demo".

    - E dey specify the path to the JSON file wey dem go score with the request_file argument. In this case, the file is ./ultrachat_200k_dataset/sample_score.json.

    - E dey store the response from the endpoint in the response variable.

    - E dey print the raw response.

1. For summary, dis script dey call one online endpoint in Azure Machine Learning to score a JSON file and e go print the response.

    ```python
    # Call the online endpoint for Azure Machine Learning make e score the `sample_score.json` file
    # We dey use the `invoke` method wey dey the `online_endpoints` property of the `workspace_ml_client` object to send request to an online endpoint and collect the response
    # The `endpoint_name` argument dey show the name of the endpoint, wey dem store for the `online_endpoint_name` variable
    # The `deployment_name` argument dey show the name of the deployment, wey na "demo"
    # The `request_file` argument dey show the path to the JSON file wey dem go score, wey na `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Show the raw response wey come from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. Delete di online endpoint

1. No forget to delete the online endpoint, otherwise you go leave the billing meter running for the compute used by the endpoint. This line of Python code dey delete an online endpoint in Azure Machine Learning. Here's a breakdown of what it does:

    - E dey call the begin_delete method of the online_endpoints property of the workspace_ml_client object. This method dey used to start the deletion of an online endpoint.

    - E dey specify the name of the endpoint wey dem go delete with the name argument. In this case, the endpoint name is stored in the online_endpoint_name variable.

    - E dey call the wait method to wait for the deletion operation to complete. This na blocking operation, meaning say e go prevent the script from continuing until the deletion don finish.

    - For summary, dis line of code dey start the deletion of an online endpoint in Azure Machine Learning and e dey wait make the operation complete.

    ```python
    # Delete di online endpoint for Azure Machine Learning
    # Di `begin_delete` method wey dey di `online_endpoints` property of di `workspace_ml_client` object na wetin dem dey use to start di deletion of an online endpoint
    # Di `name` argument dey show which endpoint dem wan delete, e dey stored for di `online_endpoint_name` variable
    # Di `wait` method dem call to wait make di deletion operation complete. Na blocking operation dis, meaning say e go prevent di script from continuing until di deletion don finish
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate by AI translation service wey dem dey call Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg make una sabi say automated translations fit get mistakes or no too accurate. Di original dokument for im native language na di authoritative source. If na important or critical information, e better make professional human translator do am. We no dey responsible for any misunderstanding or wrong interpretation wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->