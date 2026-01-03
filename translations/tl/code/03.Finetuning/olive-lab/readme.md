<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-16T15:56:26+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "tl"
}
-->
# Lab. I-optimize ang mga AI model para sa on-device inference

## Panimula

> [!IMPORTANT]
> Kailangan ng lab na ito ng **Nvidia A10 o A100 GPU** kasama ang mga kaukulang driver at CUDA toolkit (bersyon 12+) na naka-install.

> [!NOTE]
> Ito ay isang **35-minutong** lab na magbibigay sa iyo ng praktikal na pagpapakilala sa mga pangunahing konsepto ng pag-optimize ng mga modelo para sa on-device inference gamit ang OLIVE.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng lab na ito, magagawa mong gamitin ang OLIVE upang:

- I-quantize ang isang AI Model gamit ang AWQ quantization method.
- I-fine-tune ang isang AI model para sa isang partikular na gawain.
- Gumawa ng LoRA adapters (fine-tuned model) para sa epektibong on-device inference gamit ang ONNX Runtime.

### Ano ang Olive

Ang Olive (*O*NNX *live*) ay isang toolkit para sa pag-optimize ng modelo na may kasamang CLI na nagpapahintulot sa iyo na ipadala ang mga modelo para sa ONNX runtime +++https://onnxruntime.ai+++ na may kalidad at mahusay na performance.

![Olive Flow](../../../../../translated_images/olive-flow.a47985655a756dcb.tl.png)

Karaniwan, ang input sa Olive ay isang PyTorch o Hugging Face model at ang output ay isang optimized ONNX model na pinapatakbo sa isang device (deployment target) na nagpapatakbo ng ONNX runtime. I-o-optimize ng Olive ang modelo para sa AI accelerator (NPU, GPU, CPU) ng deployment target na ibinibigay ng hardware vendor tulad ng Qualcomm, AMD, Nvidia o Intel.

Pinapatakbo ng Olive ang isang *workflow*, na isang sunud-sunod na pagkakasunod ng mga indibidwal na gawain sa pag-optimize ng modelo na tinatawag na *passes* - halimbawa ng mga passes ay: model compression, graph capture, quantization, graph optimization. Bawat pass ay may mga parameter na maaaring i-tune upang makamit ang pinakamahusay na metrics, tulad ng accuracy at latency, na sinusuri ng kaukulang evaluator. Gumagamit ang Olive ng search strategy na may search algorithm upang awtomatikong i-tune ang bawat pass isa-isa o bilang grupo.

#### Mga Benepisyo ng Olive

- **Bawasan ang pagka-frustrate at oras** sa manu-manong pagsubok-sulit gamit ang iba't ibang teknik para sa graph optimization, compression, at quantization. Itakda ang iyong kalidad at performance na mga limitasyon at hayaang awtomatikong hanapin ng Olive ang pinakamahusay na modelo para sa iyo.
- **Mahigit 40 built-in na bahagi ng pag-optimize ng modelo** na sumasaklaw sa mga pinakabagong teknik sa quantization, compression, graph optimization, at finetuning.
- **Madaling gamitin na CLI** para sa mga karaniwang gawain sa pag-optimize ng modelo. Halimbawa, olive quantize, olive auto-opt, olive finetune.
- Kasama ang pag-package at deployment ng modelo.
- Sinusuportahan ang paggawa ng mga modelo para sa **Multi LoRA serving**.
- Gumawa ng workflows gamit ang YAML/JSON upang i-orchestrate ang mga gawain sa pag-optimize at deployment ng modelo.
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
1. Sundin ang mga tagubilin sa screen para kumonekta sa Compute. Kabilang dito ang pagpili ng iyong Azure Subscription, Resource Group, Project, at Compute name na na-setup mo sa Lab 1.
1. Kapag nakakonekta ka na sa iyong Azure ML Compute node, makikita ito sa **ibabang kaliwang bahagi ng Visual Code** `><Azure ML: Compute Name`

### Hakbang 1: I-clone ang repo na ito

Sa VS Code, maaari kang magbukas ng bagong terminal gamit ang **Ctrl+J** at i-clone ang repo na ito:

Sa terminal makikita mo ang prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
I-clone ang solusyon

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Hakbang 2: Buksan ang Folder sa VS Code

Para buksan ang VS Code sa tamang folder, patakbuhin ang sumusunod na command sa terminal, na magbubukas ng bagong window:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Bilang alternatibo, maaari mong buksan ang folder sa pamamagitan ng pagpili ng **File** > **Open Folder**.

### Hakbang 3: Mga Dependencies

Buksan ang terminal window sa VS Code sa iyong Azure AI Compute Instance (tip: **Ctrl+J**) at patakbuhin ang mga sumusunod na command para i-install ang mga dependencies:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Aabutin ng humigit-kumulang ~5 minuto para ma-install lahat ng dependencies.

Sa lab na ito, magda-download at mag-u-upload ka ng mga modelo sa Azure AI Model catalog. Para ma-access ang model catalog, kailangan mong mag-login sa Azure gamit ang:

```bash
az login
```

> [!NOTE]
> Sa oras ng pag-login, hihilingin kang pumili ng subscription. Siguraduhing piliin ang subscription na ibinigay para sa lab na ito.

### Hakbang 4: Patakbuhin ang mga Olive command

Buksan ang terminal window sa VS Code sa iyong Azure AI Compute Instance (tip: **Ctrl+J**) at siguraduhing naka-activate ang `olive-ai` conda environment:

```bash
conda activate olive-ai
```

Sunod, patakbuhin ang mga sumusunod na Olive command sa command line.

1. **Suriin ang data:** Sa halimbawang ito, mag-fine-tune ka ng Phi-3.5-Mini model upang maging espesyalisado sa pagsagot ng mga tanong tungkol sa paglalakbay. Ipinapakita ng code sa ibaba ang unang ilang tala ng dataset, na nasa JSON lines format:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **I-quantize ang modelo:** Bago i-train ang modelo, i-quantize mo muna gamit ang sumusunod na command na gumagamit ng teknik na tinatawag na Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. Ang AWQ ay nag-quantize ng mga timbang ng modelo sa pamamagitan ng pagsasaalang-alang sa mga activations na nangyayari habang nag-i-infer. Ibig sabihin, isinasaalang-alang ng proseso ng quantization ang aktwal na distribusyon ng data sa activations, kaya mas napapanatili ang accuracy ng modelo kumpara sa tradisyunal na mga paraan ng weight quantization.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Aabutin ng **~8 minuto** para matapos ang AWQ quantization, na magbabawas ng laki ng modelo mula sa **~7.5GB hanggang ~2.5GB**.
   
   Sa lab na ito, ipinapakita namin kung paano mag-input ng mga modelo mula sa Hugging Face (halimbawa: `microsoft/Phi-3.5-mini-instruct`). Gayunpaman, pinapayagan ka rin ng Olive na mag-input ng mga modelo mula sa Azure AI catalog sa pamamagitan ng pag-update ng `model_name_or_path` argument sa isang Azure AI asset ID (halimbawa: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **I-train ang modelo:** Sunod, ang `olive finetune` command ay mag-fine-tune sa na-quantize na modelo. Ang pag-quantize ng modelo *bago* ang fine-tuning kaysa pagkatapos ay nagbibigay ng mas magandang accuracy dahil naibabalik ng fine-tuning ang ilan sa nawalang kalidad mula sa quantization.
    
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
    
    Aabutin ng **~6 minuto** para matapos ang fine-tuning (sa 100 steps).

1. **I-optimize:** Kapag na-train na ang modelo, i-o-optimize mo ito gamit ang `auto-opt` command ng Olive, na kukunin ang ONNX graph at awtomatikong gagawa ng ilang optimizations upang mapabuti ang performance ng modelo para sa CPU sa pamamagitan ng pag-compress ng modelo at pagsasagawa ng fusions. Dapat tandaan na maaari mo ring i-optimize para sa ibang device tulad ng NPU o GPU sa pamamagitan ng pag-update ng `--device` at `--provider` arguments - ngunit para sa layunin ng lab na ito gagamit tayo ng CPU.

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

### Hakbang 5: Mabilisang pagsubok ng model inference

Para subukan ang pag-infer ng modelo, gumawa ng Python file sa iyong folder na pinangalanang **app.py** at kopyahin at i-paste ang sumusunod na code:

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

Patakbuhin ang code gamit ang:

```bash
python app.py
```

### Hakbang 6: I-upload ang modelo sa Azure AI

Ang pag-upload ng modelo sa Azure AI model repository ay nagpapahintulot na maibahagi ang modelo sa iba pang miyembro ng iyong development team at pinamamahalaan din ang version control ng modelo. Para i-upload ang modelo, patakbuhin ang sumusunod na command:

> [!NOTE]
> Palitan ang mga placeholder na `{}` ng pangalan ng iyong resource group at Azure AI Project Name.

Para makita ang iyong resource group `"resourceGroup"` at Azure AI Project name, patakbuhin ang sumusunod na command

```
az ml workspace show
```

O pumunta sa +++ai.azure.com+++ at piliin ang **management center** **project** **overview**

Palitan ang mga placeholder na `{}` ng pangalan ng iyong resource group at Azure AI Project Name.

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
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.