<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-07-16T20:07:05+00:00",
  "source_file": "md/01.Introduction/03/AIPC_Inference.md",
  "language_code": "sk"
}
-->
# **Inference Phi-3 na AI PC**

S rozvojom generatívnej AI a zlepšovaním hardvérových schopností edge zariadení je čoraz viac generatívnych AI modelov možné integrovať do používateľských zariadení typu Bring Your Own Device (BYOD). AI PC patria medzi tieto modely. Od roku 2024 spolupracujú Intel, AMD a Qualcomm s výrobcami PC na zavedení AI PC, ktoré umožňujú nasadenie lokalizovaných generatívnych AI modelov prostredníctvom hardvérových úprav. V tejto diskusii sa zameriame na Intel AI PC a preskúmame, ako nasadiť Phi-3 na Intel AI PC.

### Čo je NPU

NPU (Neural Processing Unit) je špecializovaný procesor alebo výpočtová jednotka na väčšom SoC, navrhnutá špeciálne na zrýchlenie operácií neurónových sietí a AI úloh. Na rozdiel od všeobecných CPU a GPU sú NPU optimalizované na dátovo paralelné výpočty, čo ich robí veľmi efektívnymi pri spracovaní veľkého množstva multimediálnych dát, ako sú videá a obrázky, a pri spracovaní dát pre neurónové siete. Sú obzvlášť zdatné pri riešení AI úloh, ako je rozpoznávanie reči, rozmazávanie pozadia vo video hovoroch alebo úprava fotografií a videí, napríklad detekcia objektov.

## NPU vs GPU

Hoci mnoho AI a strojového učenia beží na GPU, existuje zásadný rozdiel medzi GPU a NPU.  
GPU sú známe svojimi schopnosťami paralelného výpočtu, no nie všetky GPU sú rovnako efektívne mimo spracovania grafiky. NPU sú naopak špeciálne navrhnuté pre zložité výpočty spojené s neurónovými sieťami, čo ich robí veľmi účinnými pre AI úlohy.

Zhrnuté, NPU sú matematickí experti, ktorí zrýchľujú AI výpočty a zohrávajú kľúčovú úlohu v nastupujúcej ére AI PC!

***Tento príklad je založený na najnovšom procesore Intel Core Ultra***

## **1. Použitie NPU na spustenie modelu Phi-3**

Intel® NPU zariadenie je AI inferenčný akcelerátor integrovaný s Intel klientskymi CPU, počnúc generáciou Intel® Core™ Ultra (predtým známa ako Meteor Lake). Umožňuje energeticky efektívne vykonávanie úloh umelých neurónových sietí.

![Latency](../../../../../translated_images/sk/aipcphitokenlatency.2be14f04f30a3bf7.png)

![Latency770](../../../../../translated_images/sk/aipcphitokenlatency770.e923609a57c5d394.png)

**Intel NPU Acceleration Library**

Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) je Python knižnica navrhnutá na zvýšenie efektivity vašich aplikácií využitím výkonu Intel Neural Processing Unit (NPU) na rýchle výpočty na kompatibilnom hardvéri.

Príklad Phi-3-mini na AI PC poháňanom procesormi Intel® Core™ Ultra.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Inštalácia Python knižnice cez pip

```bash

   pip install intel-npu-acceleration-library

```

***Poznámka*** Projekt je stále vo vývoji, no referenčný model je už veľmi kompletný.

### **Spustenie Phi-3 s Intel NPU Acceleration Library**

Použitím Intel NPU akcelerácie táto knižnica neovplyvňuje tradičný proces kódovania. Stačí použiť túto knižnicu na kvantizáciu pôvodného modelu Phi-3, napríklad FP16, INT8, INT4, ako napríklad

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

Po úspešnej kvantizácii pokračujte v spustení volania NPU na spustenie modelu Phi-3.

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

Pri vykonávaní kódu môžeme sledovať stav NPU cez Správcu úloh

![NPU](../../../../../translated_images/sk/aipc_NPU.7a3cb6db47b377e1.png)

***Ukážky*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Použitie DirectML + ONNX Runtime na spustenie modelu Phi-3**

### **Čo je DirectML**

[DirectML](https://github.com/microsoft/DirectML) je vysoko výkonná, hardvérovo akcelerovaná knižnica DirectX 12 pre strojové učenie. DirectML poskytuje GPU akceleráciu pre bežné úlohy strojového učenia na širokej škále podporovaného hardvéru a ovládačov, vrátane všetkých GPU kompatibilných s DirectX 12 od výrobcov ako AMD, Intel, NVIDIA a Qualcomm.

Keď sa používa samostatne, DirectML API je nízkoúrovňová knižnica DirectX 12 vhodná pre vysoko výkonné, nízkolatenčné aplikácie ako frameworky, hry a iné aplikácie v reálnom čase. Bezproblémová interoperabilita DirectML s Direct3D 12, nízke režijné náklady a konzistentnosť naprieč hardvérom robia z DirectML ideálny nástroj na zrýchlenie strojového učenia, keď je potrebný vysoký výkon a spoľahlivosť výsledkov na rôznom hardvéri.

***Poznámka*** : Najnovší DirectML už podporuje NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### Porovnanie DirectML a CUDA z hľadiska schopností a výkonu:

**DirectML** je knižnica strojového učenia vyvinutá spoločnosťou Microsoft. Je navrhnutá na zrýchlenie strojového učenia na Windows zariadeniach, vrátane desktopov, notebookov a edge zariadení.  
- Založené na DX12: DirectML je postavené na DirectX 12, ktorý poskytuje širokú hardvérovú podporu pre GPU vrátane NVIDIA a AMD.  
- Širšia podpora: Vďaka DX12 môže DirectML pracovať s akýmkoľvek GPU, ktorý DX12 podporuje, vrátane integrovaných GPU.  
- Spracovanie obrázkov: DirectML spracováva obrázky a iné dáta pomocou neurónových sietí, vhodné pre úlohy ako rozpoznávanie obrázkov, detekcia objektov a podobne.  
- Jednoduchá inštalácia: Nastavenie DirectML je jednoduché a nevyžaduje špecifické SDK alebo knižnice od výrobcov GPU.  
- Výkon: V niektorých prípadoch má DirectML dobrý výkon a môže byť rýchlejší ako CUDA, najmä pri určitých úlohách.  
- Obmedzenia: Niekedy môže byť DirectML pomalší, najmä pri veľkých dávkach float16.

**CUDA** je paralelná výpočtová platforma a programovací model od NVIDIA. Umožňuje vývojárom využiť výkon NVIDIA GPU pre všeobecné výpočty, vrátane strojového učenia a vedeckých simulácií.  
- Špecifické pre NVIDIA: CUDA je úzko integrované s NVIDIA GPU a je pre ne špeciálne navrhnuté.  
- Vysoko optimalizované: Poskytuje vynikajúci výkon pre GPU-akcelerované úlohy, najmä na NVIDIA GPU.  
- Široko používané: Mnoho frameworkov a knižníc strojového učenia (napr. TensorFlow, PyTorch) podporuje CUDA.  
- Prispôsobiteľné: Vývojári môžu doladiť nastavenia CUDA pre konkrétne úlohy, čo vedie k optimálnemu výkonu.  
- Obmedzenia: Závislosť na NVIDIA hardvéri môže byť limitujúca, ak chcete širšiu kompatibilitu s rôznymi GPU.

### Výber medzi DirectML a CUDA

Výber medzi DirectML a CUDA závisí od vášho konkrétneho použitia, dostupnosti hardvéru a preferencií.  
Ak hľadáte širšiu kompatibilitu a jednoduchú inštaláciu, DirectML môže byť dobrá voľba. Ak však máte NVIDIA GPU a potrebujete vysoko optimalizovaný výkon, CUDA zostáva silným kandidátom. Obidve majú svoje výhody a nevýhody, preto zvážte svoje požiadavky a dostupný hardvér pri rozhodovaní.

### **Generatívna AI s ONNX Runtime**

V ére AI je prenosnosť AI modelov veľmi dôležitá. ONNX Runtime umožňuje jednoduché nasadenie trénovaných modelov na rôzne zariadenia. Vývojári nemusia riešiť inferenčný framework a môžu použiť jednotné API na dokončenie inferencie modelu. V ére generatívnej AI ONNX Runtime tiež optimalizuje kód (https://onnxruntime.ai/docs/genai/). Vďaka optimalizovanému ONNX Runtime je možné kvantizovaný generatívny AI model inferovať na rôznych zariadeniach. V Generative AI s ONNX Runtime môžete inferovať AI model cez API v Pythone, C#, C/C++. Nasadenie na iPhone môže využiť C++ Generative AI s ONNX Runtime API.

[Ukážkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Kompilácia generatívnej AI s ONNX Runtime knižnicou***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**Inštalácia knižnice**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Toto je výsledok behu

![DML](../../../../../translated_images/sk/aipc_DML.52a44180393ab491.png)

***Ukážky*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Použitie Intel OpenVINO na spustenie modelu Phi-3**

### **Čo je OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) je open-source nástroj na optimalizáciu a nasadenie hlbokých neurónových modelov. Poskytuje zrýchlenie hlbokého učenia pre modely z oblasti videnia, zvuku a jazyka z populárnych frameworkov ako TensorFlow, PyTorch a ďalších. Začnite s OpenVINO. OpenVINO je možné použiť aj v kombinácii s CPU a GPU na spustenie modelu Phi-3.

***Poznámka***: Momentálne OpenVINO nepodporuje NPU.

### **Inštalácia OpenVINO knižnice**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Spustenie Phi-3 s OpenVINO**

Rovnako ako NPU, OpenVINO vykonáva volanie generatívnych AI modelov spustením kvantizovaných modelov. Najprv je potrebné kvantizovať model Phi-3 a dokončiť kvantizáciu modelu cez príkazový riadok pomocou optimum-cli.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

konvertovaný formát vyzerá takto

![openvino_convert](../../../../../translated_images/sk/aipc_OpenVINO_convert.9e6360b65331ffca.png)

Načítajte cesty k modelu (model_dir), súvisiace konfigurácie (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) a hardvérovo akcelerované zariadenia (GPU.0) cez OVModelForCausalLM

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Pri vykonávaní kódu môžeme sledovať stav GPU cez Správcu úloh

![openvino_gpu](../../../../../translated_images/sk/aipc_OpenVINO_GPU.20180edfffd91e55.png)

***Ukážky*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Poznámka*** : Všetky tri vyššie uvedené metódy majú svoje výhody, no pre inferenciu na AI PC sa odporúča použiť NPU akceleráciu.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.