<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-12-21T15:27:08+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "pcm"
}
-->
# Lab. Make AI models work well for on-device inference

## Introduction 

> [!IMPORTANT]
> Dis lab need an **Nvidia A10 or A100 GPU** with de drivers and CUDA toolkit (version 12+) wey don install.

> [!NOTE]
> Dis na a **35-minute** lab wey go give you hands-on introduction to the main ideas for optimizing models make dem run for on-device inference using OLIVE.

## Learning Objectives

By di end of dis lab, you go fit use OLIVE to:

- Quantize AI model using de AWQ quantization method.
- Fine-tune AI model for one specific task.
- Generate LoRA adapters (fine-tuned model) for efficient on-device inference on de ONNX Runtime.

### What is Olive

Olive (*O*NNX *live*) na model optimization toolkit wey get CLI wey allow you to ship models for de ONNX runtime +++https://onnxruntime.ai+++ with good quality and performance.

![Olive Flow](../../../../../translated_images/olive-flow.c4f76d9142c579b2.pcm.png)

De input to Olive na most times a PyTorch or Hugging Face model and de output na one optimized ONNX model wey dem go run for a device (deployment target) wey dey run de ONNX runtime. Olive go optimize de model for de deployment target AI accelerator (NPU, GPU, CPU) wey hardware vendor like Qualcomm, AMD, Nvidia or Intel provide.

Olive dey run a *workflow*, wey na ordered sequence of individual model optimization tasks wey dem dey call *passes* - example passes include: model compression, graph capture, quantization, graph optimization. Each pass get parameters wey fit tune to get best metrics like accuracy and latency wey de respective evaluator go check. Olive dey use search strategy wey use search algorithm to auto-tune each pass one by one or set of passes together.

#### Benefits of Olive

- **Reduce wahala and time** of trial-and-error manual experimentation with different techniques for graph optimization, compression and quantization. Define your quality and performance constraints and make Olive automatically find de best model for you.
- **40+ built-in model optimization components** wey cover de latest techniques for quantization, compression, graph optimization and finetuning.
- **Easy-to-use CLI** for common model optimization tasks. For example, olive quantize, olive auto-opt, olive finetune.
- Model packaging and deployment dey built-in.
- Support to generate models for **Multi LoRA serving**.
- You fit construct workflows using YAML/JSON to orchestrate model optimization and deployment tasks.
- **Hugging Face** and **Azure AI** Integration.
- Built-in **caching** mechanism to **save costs**.

## Lab Instructions
> [!NOTE]
> Make sure say you don provision your Azure AI Hub and Project and setup your A100 compute like we show for Lab 1.

### Step 0: Connect to your Azure AI Compute

You go connect to de Azure AI compute using de remote feature for **VS Code.** 

1. Open your **VS Code** desktop application:
1. Open de **command palette** using  **Shift+Ctrl+P**
1. For de command palette search for **AzureML - remote: Connect to compute instance in New Window**.
1. Follow de on-screen instructions to connect to de Compute. Dis go involve selecting your Azure Subscription, Resource Group, Project and de Compute name wey you setup for Lab 1.
1. Once you don connect to your Azure ML Compute node e go show for **bottom left of Visual Code** `><Azure ML: Compute Name`

### Step 1: Clone this repo

For VS Code, you fit open new terminal with **Ctrl+J** and clone dis repo:

For de terminal you suppose see de prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clone the solution 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Step 2: Open Folder in VS Code

To open VS Code for de correct folder execute de following command for de terminal, e go open new window:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

If you prefer, you fit open de folder by selecting **File** > **Open Folder**. 

### Step 3: Dependencies

Open one terminal window for VS Code inside your Azure AI Compute Instance (tip: **Ctrl+J**) and run de following commands to install de dependencies:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> E go take about ~5mins to install all de dependencies.

For dis lab you go download and upload models to de Azure AI Model catalog. So that you fit access de model catalog, you go need to login to Azure using:

```bash
az login
```

> [!NOTE]
> When you dey login dem go ask you to select your subscription. Make sure say you set de subscription to de one wey dem give for dis lab.

### Step 4: Execute Olive commands 

Open one terminal window for VS Code inside your Azure AI Compute Instance (tip: **Ctrl+J**) and make sure say de `olive-ai` conda environment don activate:

```bash
conda activate olive-ai
```

Next, run de following Olive commands for de command line.

1. **Inspect the data:** For dis example, you dey go fine-tune Phi-3.5-Mini model so e go specialize for answering travel related questions. Code below go show de first few records of de dataset, wey dey JSON lines format:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Quantize the model:** Before you train de model, first quantize am with dis command wey use technique wey dem call Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ dey quantize weights of a model by considering de activations wey dem produce during inference. This one mean say de quantization process dey take into account de actual data distribution for de activations, and so e dey preserve model accuracy better than normal weight quantization methods.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    E go take **~8mins** to finish de AWQ quantization, and e go **reduce de model size from ~7.5GB to ~2.5GB**.
   
   For dis lab, we dey show how to input models from Hugging Face (for example: `microsoft/Phi-3.5-mini-instruct`). But Olive also allow you to input models from de Azure AI catalog by updating de `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, de `olive finetune` command go finetune de quantized model. Quantizing de model *before* fine-tuning instead of afterwards dey give better accuracy because de fine-tuning process go recover some of de loss wey quantization cause.
    
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
    
    E go take **~6mins** to finish de Fine-tuning (with 100 steps).

1. **Optimize:** After model don train, you go now optimize de model using Olive `auto-opt` command, wey go capture de ONNX graph and automatically do some optimizations to make de model faster for CPU by compressing de model and doing fusions. E good to note say you fit also optimize for other devices like NPU or GPU by just changing de `--device` and `--provider` arguments - but for dis lab we go use CPU.

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
    
    E go take **~5mins** to finish de optimization.

### Step 5: Model inference quick test

To test inference with de model, create one Python file for your folder wey dem go call **app.py** and copy-and-paste de following code:

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

Run de code with:

```bash
python app.py
```

### Step 6: Upload model to Azure AI

Uploading de model to Azure AI model repository make de model sharable with oda members of your dev team and e also handle version control of de model. To upload de model run de following command:

> [!NOTE]
> Update de `{}` placeholders with de name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"and Azure AI Project name, run de following command 

```
az ml workspace show
```

Or go to +++ai.azure.com+++ and select **management center** **project** **overview**

Update de `{}` placeholders with de name of your resource group and Azure AI Project Name.

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
Make you sabi:
Dis document don translate wit AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, make you sabi say automatic translations fit get mistakes or no too accurate. The original document for im native language suppose be the authoritative source. If na critical information, e good make you use professional human translator. We no go responsible for any misunderstanding or misinterpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->