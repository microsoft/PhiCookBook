# **Inference Phi-3 på AI PC**

Med fremskridtet inden for generativ AI og forbedringer i hardwarekapaciteter på edge-enheder, kan et stigende antal generative AI-modeller nu integreres i brugernes Bring Your Own Device (BYOD)-enheder. AI PC’er er blandt disse modeller. Fra 2024 har Intel, AMD og Qualcomm samarbejdet med PC-producenter om at introducere AI PC’er, der muliggør implementering af lokaliserede generative AI-modeller gennem hardwareændringer. I denne gennemgang vil vi fokusere på Intel AI PC’er og undersøge, hvordan man implementerer Phi-3 på en Intel AI PC.

### Hvad er en NPU

En NPU (Neural Processing Unit) er en dedikeret processor eller behandlingsenhed på en større SoC, designet specifikt til at accelerere neurale netværksoperationer og AI-opgaver. I modsætning til generelle CPU’er og GPU’er er NPUs optimeret til datadrevet parallel computing, hvilket gør dem meget effektive til at behandle store mængder multimediedata som videoer og billeder samt data til neurale netværk. De er særligt dygtige til AI-relaterede opgaver som talegenkendelse, baggrundsudsløring i videoopkald og foto- eller videoredigeringsprocesser som objektgenkendelse.

## NPU vs GPU

Selvom mange AI- og maskinlæringsopgaver kører på GPU’er, er der en vigtig forskel mellem GPU’er og NPU’er.  
GPU’er er kendt for deres parallelle beregningskapaciteter, men ikke alle GPU’er er lige effektive ud over grafisk behandling. NPUs er derimod specialbygget til komplekse beregninger involveret i neurale netværksoperationer, hvilket gør dem meget effektive til AI-opgaver.

Sammenfattende er NPUs de matematiske eksperter, der giver AI-beregninger et boost, og de spiller en central rolle i den nye æra med AI PC’er!

***Dette eksempel er baseret på Intels nyeste Intel Core Ultra Processor***

## **1. Brug NPU til at køre Phi-3 modellen**

Intel® NPU-enheden er en AI-inferensaccelerator integreret med Intel klient-CPU’er, startende fra Intel® Core™ Ultra generationen af CPU’er (tidligere kendt som Meteor Lake). Den muliggør energieffektiv udførelse af kunstige neurale netværksopgaver.

![Latency](../../../../../translated_images/da/aipcphitokenlatency.2be14f04f30a3bf7.webp)

![Latency770](../../../../../translated_images/da/aipcphitokenlatency770.e923609a57c5d394.webp)

**Intel NPU Acceleration Library**

Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) er et Python-bibliotek designet til at øge effektiviteten af dine applikationer ved at udnytte kraften i Intel Neural Processing Unit (NPU) til at udføre højhastighedsberegninger på kompatibel hardware.

Eksempel på Phi-3-mini på AI PC drevet af Intel® Core™ Ultra processorer.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Installer Python-biblioteket med pip

```bash

   pip install intel-npu-acceleration-library

```

***Bemærk*** Projektet er stadig under udvikling, men reference-modellen er allerede meget komplet.

### **Kørsel af Phi-3 med Intel NPU Acceleration Library**

Ved brug af Intel NPU-acceleration påvirker dette bibliotek ikke den traditionelle kodningsproces. Du skal kun bruge dette bibliotek til at kvantisere den oprindelige Phi-3 model, såsom FP16, INT8, INT4, for eksempel

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

Når kvantiseringen er gennemført, fortsætter du med at kalde NPU’en for at køre Phi-3 modellen.

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

Når koden kører, kan vi se NPU’ens status via Jobliste (Task Manager)

![NPU](../../../../../translated_images/da/aipc_NPU.7a3cb6db47b377e1.webp)

***Eksempler*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Brug DirectML + ONNX Runtime til at køre Phi-3 modellen**

### **Hvad er DirectML**

[DirectML](https://github.com/microsoft/DirectML) er et højtydende, hardwareaccelereret DirectX 12-bibliotek til maskinlæring. DirectML giver GPU-acceleration til almindelige maskinlæringsopgaver på et bredt udvalg af understøttet hardware og drivere, inklusive alle DirectX 12-kompatible GPU’er fra leverandører som AMD, Intel, NVIDIA og Qualcomm.

Når det bruges alene, er DirectML API’et et lavniveau DirectX 12-bibliotek og egnet til højtydende, lav-latens applikationer som frameworks, spil og andre realtidsapplikationer. Den sømløse interoperabilitet mellem DirectML og Direct3D 12 samt dets lave overhead og overensstemmelse på tværs af hardware gør DirectML ideelt til at accelerere maskinlæring, når både høj ydeevne ønskes, og pålidelighed og forudsigelighed af resultater på tværs af hardware er kritisk.

***Bemærk*** : Den nyeste DirectML understøtter allerede NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML og CUDA med hensyn til deres kapaciteter og ydeevne:

**DirectML** er et maskinlæringsbibliotek udviklet af Microsoft. Det er designet til at accelerere maskinlæringsopgaver på Windows-enheder, herunder desktops, laptops og edge-enheder.  
- DX12-baseret: DirectML er bygget oven på DirectX 12 (DX12), som giver bred hardwareunderstøttelse på tværs af GPU’er, inklusive både NVIDIA og AMD.  
- Bredere understøttelse: Da det udnytter DX12, kan DirectML arbejde med enhver GPU, der understøtter DX12, også integrerede GPU’er.  
- Billedbehandling: DirectML behandler billeder og andre data ved hjælp af neurale netværk, hvilket gør det velegnet til opgaver som billedgenkendelse, objektgenkendelse og mere.  
- Nem opsætning: Opsætning af DirectML er ligetil, og det kræver ikke specifikke SDK’er eller biblioteker fra GPU-producenter.  
- Ydeevne: I nogle tilfælde yder DirectML godt og kan være hurtigere end CUDA, især for visse arbejdsbelastninger.  
- Begrænsninger: Dog kan DirectML i visse tilfælde være langsommere, især ved float16 store batch-størrelser.

**CUDA** er NVIDIAs parallelle beregningsplatform og programmeringsmodel. Den giver udviklere mulighed for at udnytte kraften i NVIDIA GPU’er til generel computing, herunder maskinlæring og videnskabelige simuleringer.  
- NVIDIA-specifik: CUDA er tæt integreret med NVIDIA GPU’er og er designet specifikt til dem.  
- Meget optimeret: Det giver fremragende ydeevne for GPU-accelererede opgaver, især ved brug af NVIDIA GPU’er.  
- Bredt anvendt: Mange maskinlæringsframeworks og biblioteker (som TensorFlow og PyTorch) har CUDA-understøttelse.  
- Tilpasning: Udviklere kan finjustere CUDA-indstillinger for specifikke opgaver, hvilket kan føre til optimal ydeevne.  
- Begrænsninger: Dog kan CUDA’s afhængighed af NVIDIA-hardware være begrænsende, hvis man ønsker bredere kompatibilitet på tværs af forskellige GPU’er.

### Valg mellem DirectML og CUDA

Valget mellem DirectML og CUDA afhænger af dit specifikke brugsscenarie, hardwaretilgængelighed og præferencer.  
Hvis du ønsker bredere kompatibilitet og nem opsætning, kan DirectML være et godt valg. Hvis du derimod har NVIDIA GPU’er og har brug for højt optimeret ydeevne, er CUDA stadig en stærk kandidat. Samlet set har både DirectML og CUDA deres styrker og svagheder, så overvej dine krav og tilgængelig hardware, når du træffer beslutning.

### **Generativ AI med ONNX Runtime**

I AI-æraen er portabilitet af AI-modeller meget vigtig. ONNX Runtime kan nemt implementere trænede modeller på forskellige enheder. Udviklere behøver ikke bekymre sig om inferensframework og kan bruge et ensartet API til at udføre modelinferens. I den generative AI-æra har ONNX Runtime også udført kodeoptimering (https://onnxruntime.ai/docs/genai/). Gennem den optimerede ONNX Runtime kan den kvantiserede generative AI-model infereres på forskellige terminaler. I Generative AI med ONNX Runtime kan du inferere AI-model API via Python, C#, C/C++. Selvfølgelig kan implementering på iPhone drage fordel af C++’s Generative AI med ONNX Runtime API.

[Eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Kompilér generativ AI med ONNX Runtime bibliotek***

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

**Installer bibliotek**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Dette er kørselsresultatet

![DML](../../../../../translated_images/da/aipc_DML.52a44180393ab491.webp)

***Eksempler*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Brug Intel OpenVino til at køre Phi-3 modellen**

### **Hvad er OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) er et open source toolkit til optimering og implementering af dybe læringsmodeller. Det giver forbedret dyb læringsydelse for vision-, lyd- og sprogmodeller fra populære frameworks som TensorFlow, PyTorch og flere. Kom i gang med OpenVINO. OpenVINO kan også bruges i kombination med CPU og GPU til at køre Phi-3 modellen.

***Bemærk***: OpenVINO understøtter ikke NPU på nuværende tidspunkt.

### **Installer OpenVINO bibliotek**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Kørsel af Phi-3 med OpenVINO**

Ligesom NPU fuldfører OpenVINO kaldet af generative AI-modeller ved at køre kvantitative modeller. Vi skal først kvantisere Phi-3 modellen og fuldføre modelkvantiseringen via kommandolinjen gennem optimum-cli

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

det konverterede format, som dette

![openvino_convert](../../../../../translated_images/da/aipc_OpenVINO_convert.9e6360b65331ffca.webp)

Indlæs modelstier (model_dir), relaterede konfigurationer (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) og hardwareaccelererede enheder (GPU.0) gennem OVModelForCausalLM

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Når koden kører, kan vi se GPU’ens status via Jobliste (Task Manager)

![openvino_gpu](../../../../../translated_images/da/aipc_OpenVINO_GPU.20180edfffd91e55.webp)

***Eksempler*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Bemærk*** : De tre ovenstående metoder har hver deres fordele, men det anbefales at bruge NPU-acceleration til AI PC-inferens.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.