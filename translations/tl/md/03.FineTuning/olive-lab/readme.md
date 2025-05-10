<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T22:39:42+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "tl"
}
-->
# Lab. I-optimize ang AI models para sa on-device inference

## Panimula

> [!IMPORTANT]
> Kailangan ng lab na ito ng **Nvidia A10 o A100 GPU** na may kasamang drivers at CUDA toolkit (bersyon 12+) na naka-install.

> [!NOTE]
> Ito ay isang **35-minutong** lab na magbibigay sa iyo ng hands-on na pagpapakilala sa mga pangunahing konsepto ng pag-optimize ng mga modelo para sa on-device inference gamit ang OLIVE.

## Mga Layunin ng Pagkatuto

Pagkatapos ng lab na ito, magagawa mong gamitin ang OLIVE para:

- I-quantize ang isang AI Model gamit ang AWQ quantization method.
- I-fine-tune ang isang AI model para sa isang partikular na gawain.
- Gumawa ng LoRA adapters (fine-tuned model) para sa mas epektibong on-device inference gamit ang ONNX Runtime.

### Ano ang Olive

Ang Olive (*O*NNX *live*) ay isang toolkit para sa pag-optimize ng modelo na may kasamang CLI na nagbibigay-daan sa iyo na i-deploy ang mga modelo para sa ONNX runtime +++https://onnxruntime.ai+++ na may kalidad at performance.

![Olive Flow](../../../../../translated_images/olive-flow.9e6a284c256068568eb569a242b22dd2e7ec6e73f292d98272398739537ef513.tl.png)

Ang input sa Olive ay karaniwang isang PyTorch o Hugging Face model at ang output ay isang optimized na ONNX model na pinapatakbo sa isang device (deployment target) na gumagamit ng ONNX runtime. Ini-optimize ng Olive ang modelo para sa AI accelerator (NPU, GPU, CPU) ng deployment target na galing sa hardware vendor tulad ng Qualcomm, AMD, Nvidia o Intel.

Ang Olive ay nagpapatakbo ng isang *workflow*, na isang sunod-sunod na hanay ng mga indibidwal na gawain sa pag-optimize ng modelo na tinatawag na *passes* - halimbawa ng mga passes ay: model compression, graph capture, quantization, graph optimization. Bawat pass ay may mga parameter na maaaring i-tune upang makamit ang pinakamahusay na metrics, tulad ng accuracy at latency, na sinusuri ng kani-kanilang evaluator. Gumagamit ang Olive ng search strategy na may search algorithm para awtomatikong i-tune ang bawat pass isa-isa o bilang grupo.

#### Mga Benepisyo ng Olive

- **Bawasan ang abala at oras** ng paulit-ulit na manual na pagsubok sa iba't ibang teknik para sa graph optimization, compression, at quantization. Itakda ang iyong quality at performance constraints at hayaang awtomatikong hanapin ng Olive ang pinakamahusay na modelo para sa iyo.
- **Mahigit 40 built-in na components** para sa model optimization na sumasaklaw sa mga makabagong teknik sa quantization, compression, graph optimization, at finetuning.
- **Madaling gamitin na CLI** para sa mga karaniwang gawain sa pag-optimize ng modelo. Halimbawa, olive quantize, olive auto-opt, olive finetune.
- May built-in na packaging at deployment ng modelo.
- Sinusuportahan ang paggawa ng mga modelo para sa **Multi LoRA serving**.
- Gumagamit ng YAML/JSON para buuin ang workflows na nag-oorganisa ng mga gawain sa pag-optimize at deployment ng modelo.
- Integrasyon sa **Hugging Face** at **Azure AI**.
- May built-in na **caching** na mekanismo para **makatipid sa gastos**.

## Mga Tagubilin sa Lab
> [!NOTE]
> Siguraduhing na-provision mo na ang iyong Azure AI Hub at Project at na-setup ang iyong A100 compute ayon sa Lab 1.

### Hakbang 0: Kumonekta sa iyong Azure AI Compute

Kokonekta ka sa Azure AI compute gamit ang remote feature sa **VS Code.**

1. Buksan ang iyong **VS Code** desktop application:
1. Buksan ang **command palette** gamit ang **Shift+Ctrl+P**
1. Sa command palette, hanapin ang **AzureML - remote: Connect to compute instance in New Window**.
1. Sundin ang mga tagubilin sa screen para kumonekta sa Compute. Kabilang dito ang pagpili ng iyong Azure Subscription, Resource Group, Project at Compute name na na-setup mo sa Lab 1.
1. Kapag nakakonekta ka na sa Azure ML Compute node, makikita ito sa **ibabang kaliwang bahagi ng Visual Code** `><Azure ML: Compute Name`

### Hakbang 1: I-clone ang repo na ito

Sa VS Code, maaari kang magbukas ng bagong terminal gamit ang **Ctrl+J** at i-clone ang repo na ito:

Makikita mo ang prompt sa terminal

```
azureuser@computername:~/cloudfiles/code$ 
```
I-clone ang solusyon

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Hakbang 2: Buksan ang Folder sa VS Code

Para buksan ang VS Code sa kaukulang folder, i-execute ang sumusunod na command sa terminal, na magbubukas ng bagong window:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Bilang alternatibo, maaari mong buksan ang folder sa pamamagitan ng pagpili ng **File** > **Open Folder**.

### Hakbang 3: Mga Dependencies

Buksan ang terminal sa VS Code sa iyong Azure AI Compute Instance (tip: **Ctrl+J**) at i-execute ang mga sumusunod na command para i-install ang mga dependencies:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Aabutin ng humigit-kumulang 5 minuto ang pag-install ng lahat ng dependencies.

Sa lab na ito, magda-download at mag-u-upload ka ng mga modelo sa Azure AI Model catalog. Para ma-access ang model catalog, kailangan mong mag-login sa Azure gamit ang:

```bash
az login
```

> [!NOTE]
> Sa oras ng pag-login, hihilingin kang pumili ng subscription. Siguraduhing piliin ang subscription na ibinigay para sa lab na ito.

### Hakbang 4: I-execute ang mga Olive commands

Buksan ang terminal sa VS Code sa iyong Azure AI Compute Instance (tip: **Ctrl+J**) at siguraduhing naka-activate ang `olive-ai` conda environment:

```bash
conda activate olive-ai
```

Pagkatapos, i-execute ang mga sumusunod na Olive commands sa command line.

1. **Suriin ang data:** Sa halimbawang ito, ifi-fine-tune mo ang Phi-3.5-Mini model para maging espesyalista sa pagsagot ng mga tanong tungkol sa paglalakbay. Ipinapakita ng code sa ibaba ang unang ilang tala ng dataset, na nasa JSON lines format:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **I-quantize ang modelo:** Bago i-train ang modelo, i-quantize mo muna ito gamit ang sumusunod na command na gumagamit ng teknik na tinatawag na Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. I-quantize ng AWQ ang mga weights ng modelo sa pamamagitan ng pagsasaalang-alang sa mga activations na nabubuo habang nag-i-infer. Ibig sabihin, kinokonsidera ng quantization process ang aktwal na distribusyon ng data sa activations, kaya mas napapangalagaan ang accuracy ng modelo kumpara sa tradisyunal na weight quantization methods.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Aabutin ng **~8 minuto** para matapos ang AWQ quantization, na magbabawas ng laki ng modelo mula **~7.5GB hanggang ~2.5GB**.
   
   Sa lab na ito, ipinapakita namin kung paano mag-input ng mga modelo mula sa Hugging Face (halimbawa: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` command ay nag-fine-tune ng quantized model. Mas maganda ang accuracy kapag na-quantize ang modelo *bago* ang fine-tuning dahil naibabalik ng fine-tuning ang ilan sa mga nawalang katumpakan mula sa quantization.
    
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
    
    Aabutin ng **~6 minuto** para matapos ang Fine-tuning (na may 100 steps).

1. **I-optimize:** Kapag na-train na ang modelo, i-o-optimize mo ito gamit ang Olive `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` arguments - ngunit para sa lab na ito, gagamit tayo ng CPU.

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
    
    Aabutin ng **~5 minuto** para matapos ang optimization.

### Hakbang 5: Mabilisang pagsubok sa model inference

Para subukan ang inference ng modelo, gumawa ng Python file sa iyong folder na tinatawag na **app.py** at kopyahin-paste ang sumusunod na code:

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

I-execute ang code gamit ang:

```bash
python app.py
```

### Hakbang 6: I-upload ang modelo sa Azure AI

Ang pag-upload ng modelo sa Azure AI model repository ay nagpapahintulot na maibahagi ang modelo sa ibang miyembro ng iyong development team at nagha-handle din ng version control ng modelo. Para i-upload ang modelo, patakbuhin ang sumusunod na command:

> [!NOTE]
> I-update ang `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` at Azure AI Project name, patakbuhin ang sumusunod na command 

```
az ml workspace show
```

O kaya ay pumunta sa +++ai.azure.com+++ at piliin ang **management center** **project** **overview**

Palitan ang mga `{}` placeholders ng pangalan ng iyong resource group at Azure AI Project Name.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Makikita mo na ang iyong na-upload na modelo at maaari mo na itong i-deploy sa https://ml.azure.com/model/list

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kaming maging tumpak, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng salin na ito.