# **Phi šeimos kvantizavimas naudojant llama.cpp**

## **Kas yra llama.cpp**

llama.cpp yra atvirojo kodo programinės įrangos biblioteka, daugiausia parašyta C++ kalba, skirta atlikti įvairių didelių kalbos modelių (LLM), tokių kaip Llama, inferenciją. Pagrindinis jos tikslas – užtikrinti pažangų našumą LLM inferencijai įvairioje aparatinėje įrangoje su minimaliu nustatymu. Be to, šiai bibliotekai yra prieinami Python priedai, kurie siūlo aukšto lygio API tekstų užbaigimui ir OpenAI suderinamą interneto serverį.

Pagrindinis llama.cpp tikslas – leisti LLM inferenciją su minimaliu nustatymu ir pažangiu našumu įvairioje aparatinėje įrangoje – tiek lokaliai, tiek debesyje.

- Paprasta C/C++ implementacija be jokių priklausomybių
- Apple Silicon yra prioritetinė platforma – optimizuota naudojant ARM NEON, Accelerate ir Metal sistemas
- AVX, AVX2 ir AVX512 palaikymas x86 architektūroms
- 1,5-bitų, 2-bitų, 3-bitų, 4-bitų, 5-bitų, 6-bitų ir 8-bitų sveikųjų skaičių kvantizacija greitesnei inferencijai ir mažesniam atminties naudojimui
- Specialūs CUDA branduoliai LLM paleidimui NVIDIA GPU (AMD GPU palaikymas per HIP)
- Vulkan ir SYCL galinių sistemų palaikymas
- CPU+GPU hibridinė inferencija, leidžianti dalinai pagreitinti modelius, kurie viršija bendrą VRAM talpą

## **Phi-3.5 kvantizavimas naudojant llama.cpp**

Phi-3.5-Instruct modelį galima kvantizuoti naudojant llama.cpp, tačiau Phi-3.5-Vision ir Phi-3.5-MoE dar nėra palaikomi. llama.cpp konvertuojamas formatas yra gguf, kuris taip pat yra plačiausiai naudojamas kvantizacijos formatas.

Hugging Face platformoje yra daugybė kvantizuotų GGUF formato modelių. AI Foundry, Ollama ir LlamaEdge naudoja llama.cpp, todėl GGUF modeliai taip pat dažnai naudojami.

### **Kas yra GGUF**

GGUF yra dvejetainis formatas, optimizuotas greitam modelių įkėlimui ir išsaugojimui, todėl jis yra labai efektyvus inferencijos tikslais. GGUF yra sukurtas naudoti su GGML ir kitais vykdytojais. GGUF sukūrė @ggerganov, kuris taip pat yra llama.cpp, populiarios C/C++ LLM inferencijos sistemos, kūrėjas. Modeliai, iš pradžių sukurti tokiose sistemose kaip PyTorch, gali būti konvertuoti į GGUF formatą, kad būtų naudojami su šiais varikliais.

### **ONNX vs GGUF**

ONNX yra tradicinis mašininio mokymosi/gilaus mokymosi formatas, kuris yra gerai palaikomas įvairiuose AI sistemose ir turi gerus naudojimo scenarijus kraštiniuose įrenginiuose. GGUF, savo ruožtu, yra pagrįstas llama.cpp ir gali būti laikomas GenAI eros produktu. Abu formatai turi panašius naudojimo būdus. Jei siekiate geresnio našumo įterptinėje aparatinėje įrangoje ir taikomųjų programų sluoksniuose, ONNX gali būti jūsų pasirinkimas. Jei naudojate llama.cpp išvestines sistemas ir technologijas, GGUF gali būti geresnis pasirinkimas.

### **Phi-3.5-Instruct kvantizavimas naudojant llama.cpp**

**1. Aplinkos konfigūracija**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```

**2. Kvantizacija**

Naudojant llama.cpp konvertuoti Phi-3.5-Instruct į FP16 GGUF

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantizuoti Phi-3.5 į INT4

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. Testavimas**

Įdiegti llama-cpp-python

```bash

pip install llama-cpp-python -U

```

***Pastaba*** 

Jei naudojate Apple Silicon, įdiekite llama-cpp-python taip:

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testavimas

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **Resursai**

1. Sužinokite daugiau apie llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Sužinokite daugiau apie onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Sužinokite daugiau apie GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius naudojant šį vertimą.