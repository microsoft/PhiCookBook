# **Inference Phi-3 AI PC-s**

Generatiivse tehisintellekti areng ja servaseadmete riistvara võimekuse paranemine on võimaldanud üha rohkematel generatiivse tehisintellekti mudelitel integreeruda kasutajate isiklikesse seadmetesse (BYOD). AI PC-d kuuluvad nende mudelite hulka. Alates 2024. aastast on Intel, AMD ja Qualcomm teinud koostööd arvutitootjatega, et tuua turule AI PC-d, mis võimaldavad lokaliseeritud generatiivse tehisintellekti mudelite kasutuselevõttu riistvara muudatuste kaudu. Selles arutelus keskendume Intel AI PC-dele ja uurime, kuidas rakendada Phi-3 Intel AI PC-s.

### Mis on NPU

NPU (Neural Processing Unit) on spetsiaalne protsessor või töötlemisüksus suuremal SoC-l, mis on loodud spetsiaalselt närvivõrkude operatsioonide ja tehisintellekti ülesannete kiirendamiseks. Erinevalt üldotstarbelistest CPU-dest ja GPU-dest on NPU-d optimeeritud andmepõhise paralleelse arvutuse jaoks, muutes need väga tõhusaks massiivsete multimeediaandmete, nagu videod ja pildid, töötlemisel ning närvivõrkude andmete töötlemisel. Need on eriti osavad tehisintellekti ülesannete täitmisel, nagu kõnetuvastus, taustahägustamine videokõnedes ja foto- või videotöötlusprotsessid, näiteks objektide tuvastamine.

## NPU vs GPU

Kuigi paljud tehisintellekti ja masinõppe töökoormused töötavad GPU-del, on GPU-de ja NPU-de vahel oluline erinevus.  
GPU-d on tuntud oma paralleelse arvutusvõimekuse poolest, kuid mitte kõik GPU-d pole võrdselt tõhusad graafikast kaugemale ulatuvate ülesannete täitmisel. NPU-d, seevastu, on spetsiaalselt loodud keerukate arvutuste jaoks, mis on seotud närvivõrkude operatsioonidega, muutes need tehisintellekti ülesannete täitmisel väga tõhusaks.

Kokkuvõttes on NPU-d matemaatilised geeniused, mis kiirendavad tehisintellekti arvutusi ja mängivad olulist rolli AI PC-de uues ajastus!

***See näide põhineb Inteli uusimal Intel Core Ultra protsessoril***

## **1. Kasuta NPU-d Phi-3 mudeli käivitamiseks**

Intel® NPU seade on tehisintellekti järelduskiirendi, mis on integreeritud Inteli kliendi CPU-desse, alates Intel® Core™ Ultra protsessorite generatsioonist (varem tuntud kui Meteor Lake). See võimaldab energiatõhusat tehisnärvivõrkude ülesannete täitmist.

![Latentsus](../../../../../imgs/01/03/AIPC/aipcphitokenlatency.png)

![Latentsus770](../../../../../imgs/01/03/AIPC/aipcphitokenlatency770.png)

**Intel NPU kiirendusteek**

Intel NPU kiirendusteek [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) on Python-teek, mis on loodud teie rakenduste tõhususe suurendamiseks, kasutades Intel Neural Processing Unit (NPU) võimsust kiirete arvutuste tegemiseks ühilduval riistvaral.

Näide Phi-3-mini mudelist AI PC-s, mida toetavad Intel® Core™ Ultra protsessorid.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Paigalda Python-teek pip-iga

```bash

   pip install intel-npu-acceleration-library

```

***Märkus*** Projekt on endiselt arendamisel, kuid viitemudel on juba väga täielik.

### **Phi-3 käivitamine Intel NPU kiirendusteegiga**

Intel NPU kiirendust kasutades ei mõjuta see teek traditsioonilist kodeerimisprotsessi. Teil on vaja ainult seda teeki, et kvantiseerida algne Phi-3 mudel, näiteks FP16, INT8, INT4, näiteks

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

Pärast kvantiseerimise edukat lõpetamist jätkake täitmist, et kutsuda NPU-d Phi-3 mudeli käivitamiseks.

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

Koodi täitmisel saame vaadata NPU tööolekut Task Manageri kaudu.

![NPU](../../../../../imgs/01/03/AIPC/aipc_NPU.png)

***Näited*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Kasuta DirectML + ONNX Runtime'i Phi-3 mudeli käivitamiseks**

### **Mis on DirectML**

[DirectML](https://github.com/microsoft/DirectML) on suure jõudlusega, riistvarakiirendusega DirectX 12 teek masinõppe jaoks. DirectML pakub GPU kiirendust tavaliste masinõppe ülesannete jaoks laias valikus toetatud riistvara ja draiverite jaoks, sealhulgas kõik DirectX 12-ga ühilduvad GPU-d tootjatelt nagu AMD, Intel, NVIDIA ja Qualcomm.

Kui seda kasutatakse iseseisvalt, on DirectML API madala taseme DirectX 12 teek ja sobib suure jõudlusega, madala latentsusega rakenduste jaoks, nagu raamistikud, mängud ja muud reaalajas rakendused. DirectML-i sujuv koostalitlusvõime Direct3D 12-ga, samuti selle madal üldkulu ja vastavus riistvarale muudavad DirectML-i ideaalseks masinõppe kiirendamiseks, kui soovitakse nii kõrget jõudlust kui ka tulemuste usaldusväärsust ja prognoositavust riistvaral.

***Märkus*** : Viimane DirectML toetab juba NPU-d (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML ja CUDA võimekuse ja jõudluse osas:

**DirectML** on Microsofti poolt välja töötatud masinõppe teek. See on loodud masinõppe töökoormuste kiirendamiseks Windowsi seadmetel, sealhulgas lauaarvutitel, sülearvutitel ja servaseadmetel.
- DX12-põhine: DirectML on ehitatud DirectX 12 (DX12) peale, mis pakub laia riistvaratuge GPU-dele, sealhulgas nii NVIDIA kui AMD.
- Laiem tugi: Kuna see kasutab DX12, saab DirectML töötada mis tahes GPU-ga, mis toetab DX12, isegi integreeritud GPU-dega.
- Pilditöötlus: DirectML töötleb pilte ja muid andmeid närvivõrkude abil, muutes selle sobivaks ülesannete jaoks, nagu pildituvastus, objektide tuvastamine ja palju muud.
- Lihtne seadistamine: DirectML-i seadistamine on lihtne ja see ei nõua GPU tootjate spetsiifilisi SDK-sid või teeke.
- Jõudlus: Mõnel juhul toimib DirectML hästi ja võib olla teatud töökoormuste puhul kiirem kui CUDA.
- Piirangud: Siiski on juhtumeid, kus DirectML võib olla aeglasem, eriti float16 suurte partiide puhul.

**CUDA** on NVIDIA paralleelarvutuse platvorm ja programmeerimismudel. See võimaldab arendajatel kasutada NVIDIA GPU-de võimsust üldotstarbeliseks arvutamiseks, sealhulgas masinõppeks ja teaduslikeks simulatsioonideks.
- NVIDIA-spetsiifiline: CUDA on tihedalt integreeritud NVIDIA GPU-dega ja on spetsiaalselt nende jaoks loodud.
- Väga optimeeritud: See pakub suurepärast jõudlust GPU-kiirendatud ülesannete jaoks, eriti NVIDIA GPU-de kasutamisel.
- Laialdaselt kasutatav: Paljud masinõppe raamistikud ja teegid (nagu TensorFlow ja PyTorch) toetavad CUDA-d.
- Kohandatavus: Arendajad saavad CUDA seadeid konkreetsete ülesannete jaoks peenhäälestada, mis võib viia optimaalse jõudluseni.
- Piirangud: Siiski võib CUDA sõltuvus NVIDIA riistvarast olla piirav, kui soovite laiemat ühilduvust erinevate GPU-dega.

### DirectML-i ja CUDA vahel valimine

Valik DirectML-i ja CUDA vahel sõltub teie konkreetsetest kasutusjuhtudest, riistvara kättesaadavusest ja eelistustest.  
Kui otsite laiemat ühilduvust ja lihtsat seadistamist, võib DirectML olla hea valik. Kui teil on NVIDIA GPU-d ja vajate väga optimeeritud jõudlust, jääb CUDA tugevaks kandidaadiks. Kokkuvõttes on mõlemal, DirectML-il ja CUDA-l, oma tugevused ja nõrkused, seega kaaluge oma nõudeid ja olemasolevat riistvara otsuse tegemisel.

### **Generatiivne tehisintellekt ONNX Runtime'iga**

Tehisintellekti ajastul on tehisintellekti mudelite teisaldatavus väga oluline. ONNX Runtime võimaldab hõlpsasti koolitatud mudeleid erinevatesse seadmetesse juurutada. Arendajad ei pea muretsema järeldusraamistiku pärast ja saavad kasutada ühtset API-d mudeli järelduse lõpuleviimiseks. Generatiivse tehisintellekti ajastul on ONNX Runtime teinud ka koodi optimeerimist (https://onnxruntime.ai/docs/genai/). Optimeeritud ONNX Runtime'i abil saab kvantiseeritud generatiivse tehisintellekti mudelit järeldada erinevatel terminalidel. Generatiivses tehisintellektis ONNX Runtime'iga saate tehisintellekti mudeli API-d järeldada Pythonis, C#-is, C/C++-is. Loomulikult saab iPhone'i juurutamisel kasutada C++ Generatiivse tehisintellekti ONNX Runtime API-d.

[Näidiskood](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Generatiivse tehisintellekti kompileerimine ONNX Runtime teegiga***

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

**Paigalda teek**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

See on käitustulemus

![DML](../../../../../imgs/01/03/AIPC/aipc_DML.png)

***Näited*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Kasuta Intel OpenVino't Phi-3 mudeli käivitamiseks**

### **Mis on OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) on avatud lähtekoodiga tööriistakomplekt süvaõppemudelite optimeerimiseks ja juurutamiseks. See pakub süvaõppe jõudluse tõstmist visiooni-, heli- ja keelemudelitele populaarsetest raamistikest nagu TensorFlow, PyTorch ja teised. Alustage OpenVINO-ga. OpenVINO-d saab kasutada ka CPU ja GPU kombinatsioonis Phi-3 mudeli käivitamiseks.

***Märkus***: Praegu OpenVINO ei toeta NPU-d.

### **Paigalda OpenVINO teek**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Phi-3 käivitamine OpenVINO-ga**

Nagu NPU, täidab OpenVINO generatiivse tehisintellekti mudelite kutse kvantitatiivsete mudelite käivitamise kaudu. Me peame esmalt kvantiseerima Phi-3 mudeli ja lõpetama mudeli kvantiseerimise käsureal optimum-cli abil.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

Konverteeritud formaat, näiteks selline

![openvino_convert](../../../../../imgs/01/03/AIPC/aipc_OpenVINO_convert.png)

Laadige mudeli teed (model_dir), seotud konfiguratsioonid (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) ja riistvarakiirendusega seadmed (GPU.0) läbi OVModelForCausalLM.

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Koodi täitmisel saame vaadata GPU tööolekut Task Manageri kaudu.

![openvino_gpu](../../../../../imgs/01/03/AIPC/aipc_OpenVINO_GPU.png)

***Näited*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Märkus*** : Ülaltoodud kolmel meetodil on igaühel oma eelised, kuid AI PC järelduse jaoks on soovitatav kasutada NPU kiirendust.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.