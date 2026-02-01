# **Inference Phi-3 AI PC**

Su generatyviosios AI pažanga ir kraštinių įrenginių techninės įrangos galimybių gerėjimu, vis daugiau generatyviosios AI modelių gali būti integruojami į vartotojų „Bring Your Own Device“ (BYOD) įrenginius. AI kompiuteriai yra vieni iš šių modelių. Nuo 2024 metų Intel, AMD ir Qualcomm bendradarbiauja su kompiuterių gamintojais, kad pristatytų AI kompiuterius, kurie palengvina lokalizuotų generatyviosios AI modelių diegimą per techninės įrangos modifikacijas. Šiame aptarime mes sutelksime dėmesį į Intel AI kompiuterius ir nagrinėsime, kaip diegti Phi-3 Intel AI kompiuteryje.

### Kas yra NPU

NPU (Neural Processing Unit) yra specializuotas procesorius arba apdorojimo blokas didesniame SoC, sukurtas specialiai neuroninių tinklų operacijų ir AI užduočių spartinimui. Skirtingai nuo bendros paskirties CPU ir GPU, NPU yra optimizuoti duomenų valdomam lygiagrečiam skaičiavimui, todėl jie yra labai efektyvūs apdorojant didžiulius multimedijos duomenis, tokius kaip vaizdo įrašai ir nuotraukos, bei apdorojant duomenis neuroniniams tinklams. Jie ypač tinkami AI užduotims, tokioms kaip kalbos atpažinimas, fono suliejimas vaizdo skambučiuose ir nuotraukų ar vaizdo įrašų redagavimo procesai, pavyzdžiui, objektų atpažinimas.

## NPU vs GPU

Nors daugelis AI ir mašininio mokymosi užduočių vykdomos GPU, yra esminis skirtumas tarp GPU ir NPU.
GPU yra žinomi dėl savo lygiagrečių skaičiavimo galimybių, tačiau ne visi GPU yra vienodai efektyvūs už grafikos apdorojimo ribų. Tuo tarpu NPU yra specialiai sukurti sudėtingiems skaičiavimams, susijusiems su neuroninių tinklų operacijomis, todėl jie yra labai veiksmingi AI užduotims.

Apibendrinant, NPU yra matematikos genijai, kurie pagreitina AI skaičiavimus ir atlieka svarbų vaidmenį naujoje AI kompiuterių eroje!

***Šis pavyzdys yra pagrįstas naujausiu Intel Core Ultra procesoriumi***

## **1. Naudokite NPU Phi-3 modeliui vykdyti**

Intel® NPU įrenginys yra AI inferencijos spartintuvas, integruotas su Intel klientų CPU, pradedant nuo Intel® Core™ Ultra procesorių kartos (anksčiau žinomos kaip Meteor Lake). Jis leidžia energiją taupančiai vykdyti dirbtinių neuroninių tinklų užduotis.

![Latencija](../../../../../imgs/01/03/AIPC/aipcphitokenlatency.png)

![Latencija770](../../../../../imgs/01/03/AIPC/aipcphitokenlatency770.png)

**Intel NPU spartinimo biblioteka**

Intel NPU spartinimo biblioteka [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) yra Python biblioteka, sukurta padidinti jūsų programų efektyvumą, pasinaudojant Intel Neural Processing Unit (NPU) galia, kad būtų atliekami didelės spartos skaičiavimai suderinamoje techninėje įrangoje.

Phi-3-mini pavyzdys AI kompiuteryje, kurį maitina Intel® Core™ Ultra procesoriai.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Įdiekite Python biblioteką naudodami pip

```bash

   pip install intel-npu-acceleration-library

```

***Pastaba*** Projektas vis dar kuriamas, tačiau referencinis modelis jau yra labai išsamus.

### **Phi-3 vykdymas naudojant Intel NPU spartinimo biblioteką**

Naudojant Intel NPU spartinimą, ši biblioteka neturi įtakos tradiciniam kodavimo procesui. Jums tereikia naudoti šią biblioteką, kad kvantizuotumėte originalų Phi-3 modelį, pvz., FP16, INT8, INT4, pvz.

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

Po sėkmingos kvantifikacijos tęskite vykdymą, kad iškviestumėte NPU Phi-3 modeliui vykdyti.

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

Vykdant kodą, galime peržiūrėti NPU veikimo būseną per Task Manager.

![NPU](../../../../../imgs/01/03/AIPC/aipc_NPU.png)

***Pavyzdžiai*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Naudokite DirectML + ONNX Runtime Phi-3 modeliui vykdyti**

### **Kas yra DirectML**

[DirectML](https://github.com/microsoft/DirectML) yra aukštos kokybės, techninės įrangos spartinta DirectX 12 biblioteka mašininio mokymosi užduotims. DirectML teikia GPU spartinimą bendroms mašininio mokymosi užduotims įvairioje suderinamoje techninėje įrangoje ir tvarkyklėse, įskaitant visus DirectX 12 palaikančius GPU iš tokių tiekėjų kaip AMD, Intel, NVIDIA ir Qualcomm.

Naudojant atskirai, DirectML API yra žemo lygio DirectX 12 biblioteka ir tinkama aukštos kokybės, mažos latencijos programoms, tokioms kaip sistemos, žaidimai ir kitos realaus laiko programos. DirectML sklandus suderinamumas su Direct3D 12, taip pat jo mažas pridėtinis išlaidos ir suderinamumas su technine įranga, daro DirectML idealų mašininio mokymosi spartinimui, kai norima tiek aukštos kokybės, tiek patikimumo ir rezultatų nuspėjamumo įvairioje techninėje įrangoje.

***Pastaba*** : Naujausias DirectML jau palaiko NPU(https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML ir CUDA galimybių ir našumo palyginimas:

**DirectML** yra mašininio mokymosi biblioteka, sukurta Microsoft. Ji skirta spartinti mašininio mokymosi užduotis Windows įrenginiuose, įskaitant stalinius kompiuterius, nešiojamuosius kompiuterius ir kraštinius įrenginius.
- DX12 pagrindu: DirectML yra sukurta ant DirectX 12 (DX12), kuris teikia platų techninės įrangos palaikymą GPU, įskaitant tiek NVIDIA, tiek AMD.
- Platesnis palaikymas: Kadangi ji naudoja DX12, DirectML gali veikti su bet kuriuo GPU, kuris palaiko DX12, net integruotais GPU.
- Vaizdų apdorojimas: DirectML apdoroja vaizdus ir kitus duomenis naudodama neuroninius tinklus, todėl ji tinkama užduotims, tokioms kaip vaizdų atpažinimas, objektų aptikimas ir kt.
- Paprastas nustatymas: DirectML nustatymas yra paprastas ir nereikalauja specifinių SDK ar bibliotekų iš GPU gamintojų.
- Našumas: Kai kuriais atvejais DirectML veikia gerai ir gali būti greitesnė nei CUDA, ypač tam tikroms užduotims.
- Apribojimai: Tačiau yra atvejų, kai DirectML gali būti lėtesnė, ypač didelėms FP16 partijoms.

**CUDA** yra NVIDIA lygiagretaus skaičiavimo platforma ir programavimo modelis. Ji leidžia kūrėjams pasinaudoti NVIDIA GPU galia bendros paskirties skaičiavimams, įskaitant mašininį mokymąsi ir mokslines simuliacijas.
- NVIDIA specifinė: CUDA yra glaudžiai integruota su NVIDIA GPU ir specialiai jiems sukurta.
- Labai optimizuota: Ji teikia puikų našumą GPU spartintoms užduotims, ypač naudojant NVIDIA GPU.
- Plačiai naudojama: Daugelis mašininio mokymosi sistemų ir bibliotekų (pvz., TensorFlow ir PyTorch) turi CUDA palaikymą.
- Pritaikymas: Kūrėjai gali smulkiai pritaikyti CUDA nustatymus specifinėms užduotims, o tai gali lemti optimalų našumą.
- Apribojimai: Tačiau CUDA priklausomybė nuo NVIDIA techninės įrangos gali būti ribojanti, jei norite platesnio suderinamumo su skirtingais GPU.

### Pasirinkimas tarp DirectML ir CUDA

Pasirinkimas tarp DirectML ir CUDA priklauso nuo jūsų specifinio naudojimo atvejo, turimos techninės įrangos ir pageidavimų.
Jei ieškote platesnio suderinamumo ir paprasto nustatymo, DirectML gali būti geras pasirinkimas. Tačiau jei turite NVIDIA GPU ir jums reikia labai optimizuoto našumo, CUDA išlieka stiprus kandidatas. Apibendrinant, tiek DirectML, tiek CUDA turi savo stipriąsias ir silpnąsias puses, todėl apsvarstykite savo reikalavimus ir turimą techninę įrangą priimdami sprendimą.

### **Generatyvioji AI su ONNX Runtime**

AI eroje AI modelių perkeliamumas yra labai svarbus. ONNX Runtime leidžia lengvai diegti apmokytus modelius skirtinguose įrenginiuose. Kūrėjams nereikia rūpintis inferencijos sistema ir jie gali naudoti vieningą API modelio inferencijai atlikti. Generatyviosios AI eroje ONNX Runtime taip pat atliko kodo optimizavimą (https://onnxruntime.ai/docs/genai/). Naudojant optimizuotą ONNX Runtime, kvantizuotas generatyviosios AI modelis gali būti inferencijuojamas skirtinguose terminaluose. Generatyvioji AI su ONNX Runtime leidžia inferencijuoti AI modelio API per Python, C#, C / C++. Žinoma, diegimas iPhone gali pasinaudoti C++ Generatyviosios AI su ONNX Runtime API.

[Pavyzdinis kodas](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Kompiliuokite generatyviosios AI su ONNX Runtime biblioteką***

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

**Įdiekite biblioteką**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Tai yra vykdymo rezultatas

![DML](../../../../../imgs/01/03/AIPC/aipc_DML.png)

***Pavyzdžiai*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Naudokite Intel OpenVino Phi-3 modeliui vykdyti**

### **Kas yra OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) yra atvirojo kodo įrankių rinkinys, skirtas optimizuoti ir diegti giluminio mokymosi modelius. Jis teikia padidintą giluminio mokymosi našumą vizijos, garso ir kalbos modeliams iš populiarių sistemų, tokių kaip TensorFlow, PyTorch ir kt. Pradėkite naudotis OpenVINO. OpenVINO taip pat gali būti naudojamas kartu su CPU ir GPU Phi-3 modeliui vykdyti.

***Pastaba***: Šiuo metu OpenVINO nepalaiko NPU.

### **Įdiekite OpenVINO biblioteką**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Phi-3 vykdymas naudojant OpenVINO**

Kaip ir NPU, OpenVINO užbaigia generatyviosios AI modelių kvietimą vykdydamas kvantizuotus modelius. Pirmiausia turime kvantizuoti Phi-3 modelį ir užbaigti modelio kvantizaciją komandinėje eilutėje per optimum-cli.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

Konvertuotas formatas, atrodo taip:

![openvino_convert](../../../../../imgs/01/03/AIPC/aipc_OpenVINO_convert.png)

Įkelkite modelio kelią (model_dir), susijusius nustatymus (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) ir techninės įrangos spartinimo įrenginius (GPU.0) per OVModelForCausalLM.

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Vykdant kodą, galime peržiūrėti GPU veikimo būseną per Task Manager.

![openvino_gpu](../../../../../imgs/01/03/AIPC/aipc_OpenVINO_GPU.png)

***Pavyzdžiai*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Pastaba*** : Aukščiau aprašyti trys metodai turi savo privalumų, tačiau rekomenduojama naudoti NPU spartinimą AI kompiuterių inferencijai.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.