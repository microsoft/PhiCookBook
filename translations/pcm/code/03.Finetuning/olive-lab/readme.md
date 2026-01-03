<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-12-21T16:39:23+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "pcm"
}
-->
# Lab. Make AI models dey run well for on-device inference

## Intro 

> [!IMPORTANT]
> Dis lab need an **Nvidia A10 or A100 GPU** wey get correct drivers and CUDA toolkit (version 12+) installed.

> [!NOTE]
> Dis na a **35-minute** lab wey go give you hands-on introduction to di main concepts of optimizing models for on-device inference using OLIVE.

## Wetin you go learn

By di time you finish dis lab, you go fit use OLIVE to:

- Quantize an AI Model using the AWQ quantization method.
- Fine-tune an AI model for a specific task.
- Generate LoRA adapters (fine-tuned model) for efficient on-device inference on the ONNX Runtime.

### Wetin be Olive

Olive (*O*NNX *live*) na model optimization toolkit wey get accompanying CLI wey enable you to ship models for the ONNX runtime +++https://onnxruntime.ai+++ with better quality and performance.

![Olive Flow](../../../../../translated_images/olive-flow.a47985655a756dcb.pcm.png)

Di input to Olive normally be a PyTorch or Hugging Face model and di output na an optimized ONNX model wey dem go run on a device (deployment target) wey dey run the ONNX runtime. Olive go optimize di model for di deployment target's AI accelerator (NPU, GPU, CPU) wey hardware vendor like Qualcomm, AMD, Nvidia or Intel provide.

Olive dey execute a *workflow*, wey be ordered sequence of individual model optimization tasks wey dem dey call *passes* - example passes include: model compression, graph capture, quantization, graph optimization. Each pass get parameters wey fit tune to reach di best metrics, like accuracy and latency, wey di respective evaluator go measure. Olive dey use one search strategy wey use search algorithm to auto-tune each pass one-by-one or set of passes together.

#### Benefits of Olive

- **Reduce frustration and time** of trial-and-error manual experimentation with different techniques for graph optimization, compression and quantization. Define your quality and performance constraints and make Olive automatically find di best model for you.
- **40+ built-in model optimization components** wey cover cutting edge techniques in quantization, compression, graph optimization and finetuning.
- **Easy-to-use CLI** for common model optimization tasks. For example, olive quantize, olive auto-opt, olive finetune.
- Model packaging and deployment built-in.
- Supports generating models for **Multi LoRA serving**.
- Construct workflows using YAML/JSON to orchestrate model optimization and deployment tasks.
- **Hugging Face** and **Azure AI** Integration.
- Built-in **caching** mechanism to **save costs**.

## Lab Instructions
> [!NOTE]
> Make sure say you don provision your Azure AI Hub and Project and don setup your A100 compute as per Lab 1.

### Step 0: Connect to your Azure AI Compute

You go connect to the Azure AI compute using the remote feature in **VS Code.** 

1. Open your **VS Code** desktop application:
1. Open the **command palette** using  **Shift+Ctrl+P**
1. In the command palette search for **AzureML - remote: Connect to compute instance in New Window**.
1. Follow di on-screen instructions to connect to the Compute. E go involve selecting your Azure Subscription, Resource Group, Project and Compute name wey you set up in Lab 1.
1. Once you connected to your Azure ML Compute node this go display for di **bottom left of Visual Code** `><Azure ML: Compute Name`

### Step 1: Clone this repo

In VS Code, you fit open a new terminal with **Ctrl+J** and clone this repo:

In the terminal you should see the prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clone the solution 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Step 2: Open Folder in VS Code

To open VS Code in the relevant folder execute the following command in the terminal, which will open a new window:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternatively, you fit open the folder by selecting **File** > **Open Folder**. 

### Step 3: Dependencies

Open a terminal window in VS Code in your Azure AI Compute Instance (tip: **Ctrl+J**) and execute the following commands to install the dependencies:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> E go take ~5mins to install all the dependencies.

For this lab you go download and upload models to the Azure AI Model catalog. To access di model catalog, you need to login to Azure using:

```bash
az login
```

> [!NOTE]
> When you login dem go ask you to select your subscription. Make sure say you set the subscription to di one wey dem provide for this lab.

### Step 4: Execute Olive commands 

Open a terminal window in VS Code in your Azure AI Compute Instance (tip: **Ctrl+J**) and ensure the `olive-ai` conda environment is activated:

```bash
conda activate olive-ai
```

Next, run di following Olive commands for the command line.

1. **Inspect the data:** For this example, you go fine-tune Phi-3.5-Mini model so e go specialise for answering travel related questions. Di code below dey display di first few records of di dataset, wey dey in JSON lines format:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Quantize the model:** Before you train the model, you first go quantize am with di following command wey use technique called Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ quantizes di weights of a model by considering di activations wey dem produce during inference. This one mean say di quantization process dey consider di actual data distribution for di activations, wey lead to better preservation of model accuracy compared to traditional weight quantization methods.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    E go take **~8mins** to complete the AWQ quantization, wey go **reduce the model size from ~7.5GB to ~2.5GB**.
   
   For this lab, we dey show you how to input models from Hugging Face (for example: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allow you input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, di `olive finetune` command go finetune di quantized model. Quantizing di model *before* fine-tuning instead of afterwards dey give better accuracy as di fine-tuning process fit recover some of di loss wey quantization cause.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    E go take **~6mins** to complete the Fine-tuning (with 100 steps).

1. **Optimize:** After di model don train, you now optimize am using Olive's `auto-opt` command, wey go capture di ONNX graph and automatically perform plenty optimizations to improve di model performance for CPU by compressing di model and doing fusions. E good make you know say you fit also optimize for other devices like NPU or GPU by just updating di `--device` and `--provider` arguments - but for di purposes of dis lab we go use CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    E go take **~5mins** to complete the optimization.

### Step 5: Model inference quick test

To test model inference, create a Python file in your folder called **app.py** and copy-and-paste di following code:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Run di code using:

```bash
python app.py
```

### Step 6: Upload model to Azure AI

To upload di model to an Azure AI model repository go make di model sharable with other members of your development team and e go also handle version control of di model. To upload di model run di following command:

> [!NOTE]
> Update di `{}` placeholders with di name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"and Azure AI Project name, run di following command 

```
az ml workspace show
```

Or by going to +++ai.azure.com+++ and selecting **management center** **project** **overview**

Update di `{}` placeholders with di name of your resource group and Azure AI Project Name.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
You fit then see your uploaded model and deploy your model at https://ml.azure.com/model/list

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document dem translate wit AI translation service (Co-op Translator: https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automatic translations fit get mistakes or wrong parts. Di original document for im own language na di correct/authoritative source. If na important matter, e better make professional human translator check or do am. We no go liable for any misunderstanding or wrong interpretation wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->