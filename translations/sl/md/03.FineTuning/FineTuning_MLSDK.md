<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-09T21:41:04+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "sl"
}
-->
## How use chat-completion components from the Azure ML system registry to fine tune a model

In this example, we will fine-tune the Phi-3-mini-4k-instruct model to complete a conversation between two people using the ultrachat_200k dataset.

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.sl.png)

This example demonstrates how to fine-tune a model using the Azure ML SDK and Python, then deploy the fine-tuned model to an online endpoint for real-time inference.

### Training data

We will use the ultrachat_200k dataset, a heavily filtered version of the UltraChat dataset that was used to train Zephyr-7B-β, a state-of-the-art 7b chat model.

### Model

We will use the Phi-3-mini-4k-instruct model to show how users can fine-tune a model for chat-completion tasks. If you opened this notebook from a specific model card, remember to replace the model name accordingly.

### Tasks

- Choose a model to fine-tune.
- Select and explore training data.
- Configure the fine-tuning job.
- Run the fine-tuning job.
- Review training and evaluation metrics.
- Register the fine-tuned model.
- Deploy the fine-tuned model for real-time inference.
- Clean up resources.

## 1. Setup pre-requisites

- Install dependencies.
- Connect to AzureML Workspace. Learn more at set up SDK authentication. Replace <WORKSPACE_NAME>, <RESOURCE_GROUP>, and <SUBSCRIPTION_ID> below.
- Connect to AzureML system registry.
- Set an optional experiment name.
- Check or create compute.

> [!NOTE]  
> Requirements: a single GPU node can have multiple GPU cards. For example, one node of Standard_NC24rs_v3 has 4 NVIDIA V100 GPUs, while Standard_NC12s_v3 has 2 NVIDIA V100 GPUs. See the docs for details. The number of GPU cards per node is set in the parameter gpus_per_node below. Setting this correctly ensures full GPU utilization. Recommended GPU compute SKUs can be found here and here.

### Python Libraries

Install dependencies by running the cell below. This step is mandatory if you are running in a new environment.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interacting with Azure ML

1. This Python script interacts with the Azure Machine Learning (Azure ML) service. Here's what it does:

    - Imports necessary modules from azure.ai.ml, azure.identity, and azure.ai.ml.entities, as well as the time module.

    - Attempts to authenticate using DefaultAzureCredential(), which simplifies authentication for Azure cloud applications. If that fails, it falls back to InteractiveBrowserCredential() for an interactive login.

    - Tries to create an MLClient instance from the default config file (config.json). If that fails, it manually creates an MLClient with subscription_id, resource_group_name, and workspace_name.

    - Creates another MLClient instance for the Azure ML registry named "azureml", where models, fine-tuning pipelines, and environments are stored.

    - Sets the experiment_name to "chat_completion_Phi-3-mini-4k-instruct".

    - Generates a unique timestamp by converting the current time (in seconds since epoch) to an integer string, useful for unique naming and versioning.

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

## 2. Pick a foundation model to fine tune

1. Phi-3-mini-4k-instruct is a 3.8B parameter lightweight, state-of-the-art open model built on datasets used for Phi-2. The model belongs to the Phi-3 family, and the Mini version comes in two variants: 4K and 128K, which indicate the supported context length (in tokens). We need to fine-tune the model for our specific use case. You can browse these models in the Model Catalog in AzureML Studio, filtering by chat-completion task. In this example, we use Phi-3-mini-4k-instruct. If you opened this notebook for a different model, replace the model name and version accordingly.

    > [!NOTE]  
    > The model id property will be passed as input to the fine-tuning job. This is also available as the Asset ID field in the model details page in AzureML Studio Model Catalog.

2. This Python script interacts with Azure ML service. Here's what it does:

    - Sets model_name to "Phi-3-mini-4k-instruct".

    - Uses the get method of the models property of registry_ml_client to retrieve the latest version of the model from the Azure ML registry. The get method is called with the model name and a label indicating to get the latest version.

    - Prints a message showing the name, version, and id of the model to be used for fine-tuning.

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

## 3. Create a compute to be used with the job

The fine-tune job works ONLY with GPU compute. The compute size depends on the model size, and selecting the right compute can be tricky. This cell guides you to select the appropriate compute.

> [!NOTE]  
> The computes listed below use the most optimized configurations. Changing these might cause CUDA Out Of Memory errors. If that happens, try upgrading to a larger compute size.

> [!NOTE]  
> When selecting compute_cluster_size below, ensure the compute is available in your resource group. If a compute is not available, you can request access to those resources.

### Checking Model for Fine Tuning Support

1. This Python script interacts with an Azure ML model. Here's what it does:

    - Imports the ast module to safely parse strings into Python data structures.

    - Checks if the foundation_model has a tag named finetune_compute_allow_list. Tags in Azure ML are key-value pairs used to filter and sort models.

    - If the tag exists, it parses the tag's string value into a Python list and assigns it to computes_allow_list, then prints a message to create a compute from this list.

    - If the tag does not exist, it sets computes_allow_list to None and informs the user.

    - In summary, it checks for a specific tag in the model's metadata, converts it to a list if present, and provides feedback.

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

### Checking Compute Instance

1. This Python script performs several checks on a compute instance in Azure ML:

    - Attempts to retrieve the compute instance named compute_cluster from the workspace. Raises an error if its provisioning state is "failed".

    - If computes_allow_list is not None, converts all allowed compute sizes to lowercase and checks if the current compute size is in the list; raises an error if not.

    - If computes_allow_list is None, checks if the compute size is in a list of unsupported GPU VM sizes; raises an error if it is.

    - Retrieves all available compute sizes in the workspace, then finds the number of GPUs for the current compute size.

    - If GPU count is found, prints the number of GPUs; otherwise, raises an error.

    - In summary, this script verifies the compute instance's state, checks if its size is allowed, and confirms GPU availability.

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

## 4. Pick the dataset for fine-tuning the model

1. We use the ultrachat_200k dataset, which has four splits suitable for supervised fine-tuning (sft) and generation ranking (gen). The number of examples per split is shown below:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. The next few cells show basic data preparation for fine-tuning:

### Visualize some data rows

We want this sample to run quickly, so save train_sft and test_sft files containing 5% of the already trimmed rows. This means the fine-tuned model will have lower accuracy and should not be used in real-world scenarios.  
The download-dataset.py script downloads the ultrachat_200k dataset and transforms it into a format consumable by the fine-tune pipeline component. Since the dataset is large, we only use a part here.

1. Running the script below downloads only 5% of the data. You can increase this by changing the dataset_split_pc parameter to the desired percentage.

    > [!NOTE]  
    > Some language models use different language codes, so the dataset's column names should match accordingly.

1. Here is an example of how the data looks:  
The chat-completion dataset is stored in parquet format with each entry following this schema:

    - This is a JSON document, a popular data interchange format used to store and transfer data. Here's its structure:

    - "prompt": a string representing a task or question posed to the AI assistant.

    - "messages": an array of objects, each representing a message in a conversation between a user and an AI assistant. Each message has two keys:

        - "content": string content of the message.

        - "role": string indicating the sender's role, either "user" or "assistant".

    - "prompt_id": a unique string identifier for the prompt.

1. In this example, the JSON document represents a conversation where a user asks the AI assistant to create a protagonist for a dystopian story. The assistant responds, and the user requests more details, which the assistant agrees to provide. The entire conversation is linked to a specific prompt id.

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

1. This Python script downloads a dataset using a helper script named download-dataset.py. Here's what it does:

    - Imports the os module for operating system functionalities.

    - Runs the download-dataset.py script with command-line arguments specifying the dataset (HuggingFaceH4/ultrachat_200k), the download directory (ultrachat_200k_dataset), and the percentage split (5%). The exit status of the command is stored in exit_status.

    - Checks if exit_status is not 0, indicating an error, and raises an Exception if so.

    - In summary, it runs a command to download the dataset and raises an error if the download fails.

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

### Loading Data into a DataFrame

1. This Python script loads a JSON Lines file into a pandas DataFrame and shows the first 5 rows. Here's what it does:

    - Imports the pandas library for data manipulation.

    - Sets pandas display option to show full column contents without truncation.

    - Loads train_sft.jsonl from the ultrachat_200k_dataset directory using pd.read_json with lines=True to handle JSON Lines format.

    - Displays the first 5 rows of the DataFrame.

    - In summary, it loads the JSON Lines data into a DataFrame and displays the first few rows with full content.

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

## 5. Submit the fine tuning job using the model and data as inputs

Create the job using the chat-completion pipeline component. Learn more about all supported fine-tuning parameters.

### Define finetune parameters

1. Fine-tune parameters fall into two categories: training parameters and optimization parameters.

1. Training parameters cover aspects like:

    - The optimizer and scheduler to use.

    - The metric to optimize during fine-tuning.

    - Number of training steps, batch size, etc.

1. Optimization parameters help optimize GPU memory usage and effectively use compute resources.

1. Below are some optimization parameters. These differ per model and come packaged with the model to handle variations.

    - Enable DeepSpeed and LoRA.

    - Enable mixed precision training.

    - Enable multi-node training.

> [!NOTE]  
> Supervised fine-tuning may cause loss of alignment or catastrophic forgetting. It’s recommended to check for this and run an alignment stage after fine-tuning.

### Fine Tuning Parameters

1. This Python script sets up parameters for fine-tuning a machine learning model. Here's what it does:

    - Defines default training parameters like number of epochs, batch sizes for training and evaluation, learning rate, and scheduler type.

    - Defines default optimization parameters like whether to enable LoRa, DeepSpeed, and the DeepSpeed stage.

    - Combines training and optimization parameters into a dictionary called finetune_parameters.

    - Checks if the foundation_model provides any model-specific default parameters. If so, it prints a warning and updates finetune_parameters with these model-specific defaults, parsing them safely.

    - Prints the final fine-tuning parameters that will be used.

    - In summary, this script prepares and displays fine-tuning parameters, allowing model-specific overrides.

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

1. This Python script defines a function to generate a display name for a training pipeline and calls it to print the name. Here's what it does:

    1. Defines get_pipeline_display_name function that builds a display name based on training pipeline parameters.

    2. Calculates total batch size by multiplying per-device batch size, gradient accumulation steps, GPUs per node, and number of nodes.

    3. Retrieves other parameters such as learning rate scheduler type, DeepSpeed status and stage, LoRa status, checkpoint limits, and max sequence length.

    4. Constructs a string combining these parameters with hyphens. If DeepSpeed or LoRa is enabled, it includes "ds" plus stage or "lora"; otherwise, "nods" or "nolora".

    5. Returns the constructed string as the pipeline display name.

    6. Calls the function and prints the display name.

    7. In summary, this script generates a descriptive name for the training pipeline based on configuration.
training pipeline temeljen na različitim parametrima, a zatim ispisuje ovaj prikazani naziv. ```python
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

### Konfiguriranje pipelinea

Ovaj Python skript definira i konfigurira pipeline za strojno učenje koristeći Azure Machine Learning SDK. Evo što radi:

1. Uvozi potrebne module iz Azure AI ML SDK-a.
2. Dohvaća komponentu pipelinea pod nazivom "chat_completion_pipeline" iz registra.
3. Definira pipeline job koristeći `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`, što znači da će pipeline stati ako bilo koji korak ne uspije.
4. Ukratko, ovaj skript definira i konfigurira pipeline za strojno učenje za zadatak dovršavanja chata koristeći Azure Machine Learning SDK.

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

### Podnošenje posla

1. Ovaj Python skript podnosi posao pipelinea za strojno učenje u Azure Machine Learning workspace i zatim čeka da posao završi. Evo što radi:

- Poziva metodu create_or_update objekta jobs u workspace_ml_client za podnošenje pipeline posla. Pipeline koji će se pokrenuti specificiran je preko pipeline_object, a eksperiment pod kojim se posao izvodi preko experiment_name.
- Zatim poziva metodu stream objekta jobs u workspace_ml_client da čeka završetak pipeline posla. Posao za čekanje specificiran je atributom name objekta pipeline_job.
- Ukratko, ovaj skript podnosi posao pipelinea za strojno učenje u Azure Machine Learning workspace i čeka njegov završetak.

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

## 6. Registracija fino podešenog modela u workspace

Registrirat ćemo model iz izlaza posla fino podešavanja. Time pratimo povezanost između fino podešenog modela i posla fino podešavanja. Taj posao dodatno prati povezanost s osnovnim modelom, podacima i kodom za treniranje.

### Registracija ML modela

1. Ovaj Python skript registrira model strojnog učenja koji je treniran u Azure Machine Learning pipelineu. Evo što radi:

- Uvozi potrebne module iz Azure AI ML SDK-a.
- Provjerava postoji li izlaz trained_model iz pipeline posla pozivajući metodu get objekta jobs u workspace_ml_client i pristupajući njegovom atributu outputs.
- Konstrukciju puta do treniranog modela radi formatiranjem stringa s imenom pipeline posla i imenom izlaza ("trained_model").
- Definira ime za fino podešeni model dodavanjem "-ultrachat-200k" izvornom imenu modela i zamjenom svih kosa crta s crticama.
- Priprema registraciju modela stvaranjem Model objekta s različitim parametrima, uključujući put do modela, tip modela (MLflow model), ime i verziju modela te opis modela.
- Registrira model pozivajući metodu create_or_update objekta models u workspace_ml_client s Model objektom kao argumentom.
- Ispisuje registrirani model.

1. Ukratko, ovaj skript registrira model strojnog učenja treniran u Azure Machine Learning pipelineu.

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

## 7. Deploy fino podešenog modela na online endpoint

Online endpointi pružaju trajni REST API koji se može koristiti za integraciju s aplikacijama kojima je potreban model.

### Upravljanje endpointom

1. Ovaj Python skript stvara upravljani online endpoint u Azure Machine Learning za registrirani model. Evo što radi:

- Uvozi potrebne module iz Azure AI ML SDK-a.
- Definira jedinstveno ime za online endpoint dodavanjem vremenskog žiga na string "ultrachat-completion-".
- Priprema stvaranje online endpointa stvaranjem ManagedOnlineEndpoint objekta s različitim parametrima, uključujući ime endpointa, opis endpointa i način autentikacije ("key").
- Stvara online endpoint pozivajući metodu begin_create_or_update workspace_ml_client-a s ManagedOnlineEndpoint objektom kao argumentom, zatim čeka da se operacija dovrši pozivom metode wait.

1. Ukratko, ovaj skript stvara upravljani online endpoint u Azure Machine Learning za registrirani model.

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
> Ovdje možete pronaći popis SKU-ova podržanih za deployment - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Deploy ML modela

1. Ovaj Python skript implementira registrirani model strojnog učenja na upravljani online endpoint u Azure Machine Learning. Evo što radi:

- Uvozi modul ast, koji pruža funkcije za obradu stabala apstraktne sintakse Pythona.
- Postavlja tip instance za deployment na "Standard_NC6s_v3".
- Provjerava postoji li tag inference_compute_allow_list u osnovnom modelu. Ako postoji, pretvara vrijednost taga iz stringa u Python listu i dodjeljuje je varijabli inference_computes_allow_list. Ako ne postoji, postavlja inference_computes_allow_list na None.
- Provjerava je li specificirani tip instance u dopuštenom popisu. Ako nije, ispisuje poruku korisniku da odabere tip instance s dopuštenog popisa.
- Priprema stvaranje deploymenta stvaranjem ManagedOnlineDeployment objekta s različitim parametrima, uključujući ime deploymenta, ime endpointa, ID modela, tip i broj instanci, postavke liveness probe i postavke zahtjeva.
- Stvara deployment pozivajući metodu begin_create_or_update workspace_ml_client-a s ManagedOnlineDeployment objektom kao argumentom, zatim čeka završetak pozivom wait.
- Postavlja promet endpointa tako da 100% prometa ide na deployment "demo".
- Ažurira endpoint pozivajući metodu begin_create_or_update workspace_ml_client-a s endpoint objektom kao argumentom, zatim čeka završetak pozivom result.

1. Ukratko, ovaj skript implementira registrirani model strojnog učenja na upravljani online endpoint u Azure Machine Learning.

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

## 8. Testiranje endpointa s uzorkom podataka

Dohvatit ćemo uzorak podataka iz testnog skupa i poslati ga online endpointu na inferenciju. Zatim ćemo prikazati predviđene oznake zajedno s stvarnim oznakama.

### Čitanje rezultata

1. Ovaj Python skript učitava JSON Lines datoteku u pandas DataFrame, uzima slučajni uzorak i resetira indeks. Evo što radi:

- Učitava datoteku ./ultrachat_200k_dataset/test_gen.jsonl u pandas DataFrame. Funkcija read_json koristi se s argumentom lines=True jer je datoteka u JSON Lines formatu, gdje je svaki redak zaseban JSON objekt.
- Uzima slučajni uzorak od 1 retka iz DataFramea. Funkcija sample koristi se s argumentom n=1 za broj slučajnih redaka.
- Resetira indeks DataFramea. Funkcija reset_index koristi se s argumentom drop=True kako bi se izbrisao originalni indeks i zamijenio novim, standardnim cijelobrojnim indeksom.
- Prikazuje prvih 2 retka DataFramea koristeći funkciju head s argumentom 2. Budući da DataFrame sadrži samo jedan redak nakon uzorkovanja, prikazat će samo taj jedan redak.

1. Ukratko, ovaj skript učitava JSON Lines datoteku u pandas DataFrame, uzima slučajni uzorak od 1 retka, resetira indeks i prikazuje prvi redak.

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

### Kreiranje JSON objekta

1. Ovaj Python skript kreira JSON objekt s određenim parametrima i sprema ga u datoteku. Evo što radi:

- Uvozi modul json, koji pruža funkcije za rad s JSON podacima.
- Kreira rječnik parameters s ključevima i vrijednostima koji predstavljaju parametre za model strojnog učenja. Ključevi su "temperature", "top_p", "do_sample" i "max_new_tokens", a njihove vrijednosti su redom 0.6, 0.9, True i 200.
- Kreira drugi rječnik test_json s dva ključa: "input_data" i "params". Vrijednost "input_data" je drugi rječnik s ključevima "input_string" i "parameters". Vrijednost "input_string" je lista koja sadrži prvu poruku iz test_df DataFramea. Vrijednost "parameters" je rječnik parameters kreiran ranije. Vrijednost "params" je prazan rječnik.
- Otvara datoteku pod nazivom sample_score.json

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

### Pozivanje endpointa

1. Ovaj Python skript poziva online endpoint u Azure Machine Learning za procjenu JSON datoteke. Evo što radi:

- Poziva metodu invoke svojstva online_endpoints objekta workspace_ml_client. Ova metoda šalje zahtjev online endpointu i prima odgovor.
- Specificira ime endpointa i deploymenta s argumentima endpoint_name i deployment_name. U ovom slučaju, ime endpointa pohranjeno je u varijabli online_endpoint_name, a ime deploymenta je "demo".
- Specificira putanju do JSON datoteke za procjenu s argumentom request_file. U ovom slučaju, datoteka je ./ultrachat_200k_dataset/sample_score.json.
- Sprema odgovor endpointa u varijablu response.
- Ispisuje sirovi odgovor.

1. Ukratko, ovaj skript poziva online endpoint u Azure Machine Learning za procjenu JSON datoteke i ispisuje odgovor.

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

## 9. Brisanje online endpointa

1. Nemojte zaboraviti obrisati online endpoint, inače ćete nastaviti plaćati za računalne resurse koje endpoint koristi. Ovaj redak Python koda briše online endpoint u Azure Machine Learning. Evo što radi:

- Poziva metodu begin_delete svojstva online_endpoints objekta workspace_ml_client. Ova metoda započinje brisanje online endpointa.
- Specificira ime endpointa za brisanje s argumentom name. U ovom slučaju, ime endpointa pohranjeno je u varijabli online_endpoint_name.
- Poziva metodu wait da čeka dovršetak operacije brisanja. To je blokirajuća operacija, što znači da će spriječiti nastavak skripte dok brisanje ne završi.
- Ukratko, ovaj redak koda započinje brisanje online endpointa u Azure Machine Learning i čeka da operacija završi.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku naj velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.