# **AI PC-ல் Phi-3 மாடலைInference செய்யுதல்**

உருவாக்கும் AI-யின் முன்னேற்றம் மற்றும் எட்ஜ் சாதனங்களின் ஹார்ட்வேரின் திறன்கள் மேம்படுவதால், பல உருவாக்கும் AI மாடல்கள் தற்போது பயனர்களின் Bring Your Own Device (BYOD) சாதனங்களில் ஒருங்கிணைக்க முடிகிறது. AI PC-கள் இந்த மாடல்களில் ஒன்றாகும். 2024 முதல், Intel, AMD மற்றும் Qualcomm PC உற்பத்தியாளர்களுடன் இணைந்து AI PC-களை அறிமுகப்படுத்தி உள்ளனர், இது உள்ளூர் உருவாக்கும் AI மாடல்களை ஹார்ட்வேர மாற்றங்கள் மூலம் செயல்படுத்த உதவுகிறது. இந்த விவாதத்தில், Intel AI PC-க்களை மையமாகக் கொண்டு, Intel AI PC-ல் Phi-3 மாடலை எப்படி செயல்படுத்துவது என்பதை ஆராய்வோம்.

### NPU என்றால் என்ன?

NPU (Neural Processing Unit) என்பது பெரிய SoC-ல் உள்ள ஒரு தனிப்பட்ட செயலி அல்லது செயலாக்க அலகு ஆகும், இது நரம்பு வலைப்பின்னல் செயல்பாடுகள் மற்றும் AI பணிகளை வேகமாக செயல்படுத்துவதற்காக வடிவமைக்கப்பட்டுள்ளது. பொதுப் பயன்பாட்டு CPUs மற்றும் GPUs-க்கு மாறாக, NPUs தரவுகளின் அடிப்படையில் இணை செயலாக்கத்திற்கு மேம்படுத்தப்பட்டவை, இது வீடியோக்கள் மற்றும் படங்கள் போன்ற பெரும் மிடியாக் தரவுகளை செயலாக்குவதில் மிகவும் திறமையானதாக உள்ளது. மேலும், நரம்பு வலைப்பின்னல்களுக்கான தரவுகளை செயலாக்குவதில் NPUs சிறப்பாக செயல்படுகின்றன. AI தொடர்பான பணிகளை, உதாரணமாக பேச்சு அடையாளம் காணுதல், வீடியோ அழைப்புகளில் பின்னணி மங்குதல், மற்றும் பொருள் கண்டறிதல் போன்ற புகைப்படம் அல்லது வீடியோ எடிட்டிங் செயல்பாடுகளை NPUs சிறப்பாக கையாளுகின்றன.

## NPU vs GPU

பல AI மற்றும் இயந்திரக் கற்றல் பணிகள் GPUs-ல் இயங்கினாலும், GPUs மற்றும் NPUs இடையே ஒரு முக்கிய வேறுபாடு உள்ளது.  
GPUs இணை செயலாக்க திறன்களுக்காக அறியப்பட்டவை, ஆனால் அனைத்து GPUs-களும் கிராபிக்ஸ் செயலாக்கத்திற்கு அப்பால் சமமாக செயல்படுவதில்லை. NPUs, மாறாக, நரம்பு வலைப்பின்னல் செயல்பாடுகளில் உள்ள சிக்கலான கணக்கீடுகளுக்காக உருவாக்கப்பட்டவை, இது AI பணிகளுக்கு மிகவும் பயனுள்ளதாக உள்ளது.

சுருக்கமாக, NPUs AI கணக்கீடுகளை வேகமாக செயல்படுத்தும் கணித வல்லுநர்கள், மேலும் அவை AI PC-க்களின் புதிய காலத்தில் முக்கிய பங்கு வகிக்கின்றன!

***இந்த எடுத்துக்காட்டு Intel-இன் சமீபத்திய Intel Core Ultra Processor அடிப்படையில் உள்ளது***

## **1. Intel NPU-யை பயன்படுத்தி Phi-3 மாடலை இயக்குதல்**

Intel® NPU சாதனம் Intel® Core™ Ultra தலைமுறை CPUs (முன்னர் Meteor Lake என அறியப்பட்டது) முதல் Intel வாடிக்கையாளர் CPUs உடன் ஒருங்கிணைக்கப்பட்ட AI inference வேகப்படுத்தியாகும். இது செயற்கை நரம்பு வலைப்பின்னல் பணிகளை ஆற்றல் திறனுடன் செயல்படுத்த உதவுகிறது.

![Latency](../../../../../imgs/01/03/AIPC/aipcphitokenlatency.png)

![Latency770](../../../../../imgs/01/03/AIPC/aipcphitokenlatency770.png)

**Intel NPU Acceleration Library**

Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) என்பது Python நூலகமாகும், இது Intel Neural Processing Unit (NPU)-இன் சக்தியை பயன்படுத்தி, பொருத்தமான ஹார்ட்வேரில் வேகமான கணக்கீடுகளைச் செய்ய உங்கள் பயன்பாடுகளின் திறனை மேம்படுத்த வடிவமைக்கப்பட்டுள்ளது.

Intel® Core™ Ultra செயலிகளால் இயக்கப்படும் AI PC-ல் Phi-3-mini மாடலின் எடுத்துக்காட்டு.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Python நூலகத்தை pip மூலம் நிறுவவும்

```bash

   pip install intel-npu-acceleration-library

```

***குறிப்பு*** இந்த திட்டம் இன்னும் மேம்பாட்டில் உள்ளது, ஆனால் குறிப்புக் மாடல் ஏற்கனவே மிகவும் முழுமையானது.

### **Intel NPU Acceleration Library-யை பயன்படுத்தி Phi-3-ஐ இயக்குதல்**

Intel NPU வேகப்படுத்தலைப் பயன்படுத்தும்போது, இந்த நூலகம் பாரம்பரிய குறியாக்க செயல்முறையை பாதிக்காது. நீங்கள் இந்த நூலகத்தை பயன்படுத்தி FP16, INT8, INT4 போன்ற Phi-3 மாடலின் அசல் வடிவத்தை அளவிட வேண்டும்.

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

அளவீடு வெற்றிகரமாக முடிந்த பிறகு, NPU-ஐ அழைத்து Phi-3 மாடலை இயக்க செயல்படுத்தவும்.

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

குறியீட்டை செயல்படுத்தும்போது, Task Manager மூலம் NPU-வின் செயல்பாட்டு நிலையை பார்க்கலாம்.

![NPU](../../../../../imgs/01/03/AIPC/aipc_NPU.png)

***எடுத்துக்காட்டுகள்*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. DirectML + ONNX Runtime-ஐ பயன்படுத்தி Phi-3 மாடலை இயக்குதல்**

### **DirectML என்றால் என்ன**

[DirectML](https://github.com/microsoft/DirectML) என்பது இயந்திரக் கற்றல் பணிகளுக்கான DirectX 12 அடிப்படையிலான, உயர் செயல்திறன் கொண்ட, ஹார்ட்வேரால் வேகப்படுத்தப்பட்ட நூலகமாகும். DirectML, AMD, Intel, NVIDIA மற்றும் Qualcomm போன்ற விற்பனையாளர்களின் அனைத்து DirectX 12-க்கு பொருந்தக்கூடிய GPUs உட்பட, பரந்த அளவிலான ஹார்ட்வேரம் மற்றும் டிரைவர்கள் மூலம் இயந்திரக் கற்றல் பணிகளுக்கு GPU வேகப்படுத்தலை வழங்குகிறது.

தனியாக பயன்படுத்தும்போது, DirectML API ஒரு குறைந்த நிலை DirectX 12 நூலகமாகும், மேலும் இது frameworks, விளையாட்டுகள் மற்றும் பிற நேரடி பயன்பாடுகள் போன்ற உயர் செயல்திறன், குறைந்த தாமத பயன்பாடுகளுக்கு பொருத்தமானது. DirectML மற்றும் Direct3D 12 இடையேயான எளிதான இணக்கத்தன்மை, அதன் குறைந்த மேலதிகச் செலவு மற்றும் ஹார்ட்வேரம் முழுவதும் ஒத்திசைவு ஆகியவை DirectML-ஐ இயந்திரக் கற்றலை வேகப்படுத்துவதற்கு சிறந்ததாக ஆக்குகின்றன, குறிப்பாக உயர் செயல்திறன் தேவைப்படும் போது மற்றும் ஹார்ட்வேரம் முழுவதும் முடிவுகளின் நம்பகத்தன்மை மற்றும் கணிக்கத்தக்க தன்மையை உறுதிப்படுத்துவது முக்கியமானது.

***குறிப்பு*** : சமீபத்திய DirectML ஏற்கனவே NPU-ஐ ஆதரிக்கிறது (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML மற்றும் CUDA-வின் திறன்கள் மற்றும் செயல்திறன்:

**DirectML** என்பது Microsoft-ஆல் உருவாக்கப்பட்ட இயந்திரக் கற்றல் நூலகமாகும். இது Windows சாதனங்களில் இயந்திரக் கற்றல் பணிகளை வேகப்படுத்த வடிவமைக்கப்பட்டுள்ளது, இதில் டெஸ்க்டாப்கள், லேப்டாப்கள் மற்றும் எட்ஜ் சாதனங்கள் அடங்கும்.
- DX12 அடிப்படையிலானது: DirectML DirectX 12 (DX12) மீது கட்டமைக்கப்பட்டுள்ளது, இது NVIDIA மற்றும் AMD ஆகியவற்றின் GPUs உட்பட பரந்த அளவிலான ஹார்ட்வேர ஆதரவை வழங்குகிறது.
- பரந்த ஆதரவு: DX12-ஐ பயன்படுத்துவதால், DirectML DX12-ஐ ஆதரிக்கும் எந்த GPU-வுடனும் வேலை செய்ய முடியும், ஒருங்கிணைக்கப்பட்ட GPUs உட்பட.
- பட செயலாக்கம்: DirectML நரம்பு வலைப்பின்னல்களைப் பயன்படுத்தி படங்கள் மற்றும் பிற தரவுகளை செயலாக்குகிறது, இது பட அடையாளம் காணுதல், பொருள் கண்டறிதல் மற்றும் பலவற்றுக்கு பொருத்தமானது.
- அமைப்பின் எளிமை: DirectML-ஐ அமைப்பது எளிது, மேலும் GPU உற்பத்தியாளர்களின் குறிப்பிட்ட SDKs அல்லது நூலகங்களை தேவைப்படாது.
- செயல்திறன்: சில சந்தர்ப்பங்களில், DirectML சிறப்பாக செயல்படுகிறது மற்றும் குறிப்பிட்ட பணிகளுக்கு CUDA-வைவிட வேகமாக இருக்கலாம்.
- வரம்புகள்: இருப்பினும், DirectML சில நேரங்களில் மெதுவாக இருக்கலாம், குறிப்பாக float16 பெரிய தொகுதிகளுக்கு.

**CUDA** என்பது NVIDIA-வின் இணை செயலாக்க தளம் மற்றும் நிரலாக்க முறைமையாகும். இது NVIDIA GPUs-இன் சக்தியை பொதுப் பயன்பாட்டு கணக்கீடுகளுக்கு, இயந்திரக் கற்றல் மற்றும் அறிவியல் சிமுலேஷன்கள் உட்பட, பயன்படுத்துவதற்கு டெவலப்பர்களுக்கு அனுமதிக்கிறது.
- NVIDIA-க்கு தனிப்பட்டது: CUDA NVIDIA GPUs-வுடன் நெருக்கமாக ஒருங்கிணைக்கப்பட்டுள்ளது மற்றும் குறிப்பாக அவற்றிற்காக வடிவமைக்கப்பட்டுள்ளது.
- மிகவும் மேம்படுத்தப்பட்டது: இது GPU-வேகப்படுத்தப்பட்ட பணிகளுக்கு சிறந்த செயல்திறனை வழங்குகிறது, குறிப்பாக NVIDIA GPUs-ஐப் பயன்படுத்தும்போது.
- பரவலாக பயன்படுத்தப்படுகிறது: TensorFlow மற்றும் PyTorch போன்ற பல இயந்திரக் கற்றல் frameworks மற்றும் நூலகங்கள் CUDA ஆதரவை கொண்டுள்ளன.
- தனிப்பயனாக்கம்: டெவலப்பர்கள் குறிப்பிட்ட பணிகளுக்கு CUDA அமைப்புகளை நன்றாகச் சரிசெய்ய முடியும், இது சிறந்த செயல்திறனை ஏற்படுத்தலாம்.
- வரம்புகள்: இருப்பினும், CUDA-வின் NVIDIA ஹார்ட்வேரம் சார்ந்த தன்மை, வெவ்வேறு GPUs முழுவதும் பரந்த இணக்கத்தன்மையை விரும்பினால், வரம்பாக இருக்கலாம்.

### DirectML மற்றும் CUDA-இடையேயான தேர்வு

DirectML மற்றும் CUDA-இடையேயான தேர்வு உங்கள் குறிப்பிட்ட பயன்பாடு, ஹார்ட்வேரம் கிடைப்பது மற்றும் விருப்பங்களைப் பொறுத்தது.  
நீங்கள் பரந்த இணக்கத்தன்மை மற்றும் அமைப்பின் எளிமையைத் தேடுகிறீர்கள் என்றால், DirectML ஒரு நல்ல தேர்வாக இருக்கலாம். இருப்பினும், நீங்கள் NVIDIA GPUs-ஐ வைத்திருந்தால் மற்றும் மிகவும் மேம்படுத்தப்பட்ட செயல்திறன் தேவைப்பட்டால், CUDA ஒரு வலுவான தேர்வாக உள்ளது.  
சுருக்கமாக, DirectML மற்றும் CUDA இரண்டுக்கும் தங்கள் பலவீனங்கள் மற்றும் பலவீனங்கள் உள்ளன, எனவே உங்கள் தேவைகள் மற்றும் கிடைக்கும் ஹார்ட்வேரத்தைப் பொருத்து முடிவெடுக்கவும்.

### **ONNX Runtime உடன் Generative AI**

AI காலத்தில், AI மாடல்களின் தாங்குதிறன் மிகவும் முக்கியமானது. ONNX Runtime பயிற்சி பெற்ற மாடல்களை வெவ்வேறு சாதனங்களில் எளிதாக செயல்படுத்த முடியும். டெவலப்பர்கள் inference framework-ஐ கவனிக்க தேவையில்லை, மேலும் ஒரே API-ஐப் பயன்படுத்தி மாடல் inference-ஐ முடிக்க முடியும். Generative AI காலத்தில், ONNX Runtime கூட குறியீட்டு மேம்படுத்தலை (https://onnxruntime.ai/docs/genai/) செய்துள்ளது. மேம்படுத்தப்பட்ட ONNX Runtime மூலம், அளவிடப்பட்ட Generative AI மாடலை வெவ்வேறு டெர்மினல்களில் inference செய்ய முடியும். Generative AI உடன் ONNX Runtime-ல், Python, C#, C / C++ மூலம் AI மாடல் API-ஐ inference செய்யலாம்.  
மிகவும் முக்கியமாக, iPhone-ல் C++-இன் Generative AI உடன் ONNX Runtime API-ஐ பயன்படுத்தி deployment செய்யலாம்.

[எடுத்துக்காட்டு குறியீடு](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Generative AI-ஐ ONNX Runtime நூலகத்துடன் compile செய்யவும்***

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

**நூலகத்தை நிறுவவும்**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

இது இயக்கும் முடிவாகும்

![DML](../../../../../imgs/01/03/AIPC/aipc_DML.png)

***எடுத்துக்காட்டுகள்*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Intel OpenVino-ஐ பயன்படுத்தி Phi-3 மாடலை இயக்குதல்**

### **OpenVINO என்றால் என்ன**

[OpenVINO](https://github.com/openvinotoolkit/openvino) என்பது ஆழமான கற்றல் மாடல்களை மேம்படுத்தவும், செயல்படுத்தவும் உதவும் திறந்த மூலக் கருவியாகும். இது TensorFlow, PyTorch போன்ற பிரபலமான frameworks-லிருந்து பார்வை, ஒலி மற்றும் மொழி மாடல்களுக்கு மேம்படுத்தப்பட்ட ஆழமான கற்றல் செயல்திறனை வழங்குகிறது. OpenVINO-ஐ CPU மற்றும் GPU-வுடன் இணைந்து Phi-3 மாடலை இயக்கவும் பயன்படுத்தலாம்.

***குறிப்பு***: தற்போதைய OpenVINO NPU-ஐ ஆதரிக்கவில்லை.

### **OpenVINO நூலகத்தை நிறுவவும்**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **OpenVINO-யை பயன்படுத்தி Phi-3-ஐ இயக்குதல்**

NPU போல, OpenVINO அளவிடப்பட்ட மாடல்களை இயக்குவதன் மூலம் Generative AI மாடல்களின் அழைப்பை முடிக்கிறது. முதலில் Phi-3 மாடலை அளவிட வேண்டும், மேலும் optimum-cli மூலம் கட்டளைக் கோடில் மாடல் அளவீட்டை முடிக்க வேண்டும்.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

மாற்றிய வடிவம், இதுபோல் இருக்கும்

![openvino_convert](../../../../../imgs/01/03/AIPC/aipc_OpenVINO_convert.png)

OVModelForCausalLM மூலம் மாடல் பாதைகள் (model_dir), தொடர்புடைய கட்டமைப்புகள் (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}), மற்றும் ஹார்ட்வேர வேகப்படுத்தப்பட்ட சாதனங்கள் (GPU.0) ஆகியவற்றை ஏற்றவும்.

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

குறியீட்டை செயல்படுத்தும்போது, Task Manager மூலம் GPU-வின் செயல்பாட்டு நிலையை பார்க்கலாம்.

![openvino_gpu](../../../../../imgs/01/03/AIPC/aipc_OpenVINO_GPU.png)

***எடுத்துக்காட்டுகள்*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***குறிப்பு*** : மேலே கூறப்பட்ட மூன்று முறைகளுக்கும் தங்களது தனித்தன்மை உள்ளது, ஆனால் AI PC inference-க்கு NPU வேகப்படுத்தலை பயன்படுத்த பரிந்துரைக்கப்படுகிறது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.