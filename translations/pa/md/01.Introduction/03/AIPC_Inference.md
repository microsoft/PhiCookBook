# **AI PC ਵਿੱਚ Inference Phi-3**

ਜਨਰੇਟਿਵ AI ਦੇ ਵਿਕਾਸ ਅਤੇ ਐਜ ਡਿਵਾਈਸ ਹਾਰਡਵੇਅਰ ਸਮਰੱਥਾਵਾਂ ਵਿੱਚ ਸੁਧਾਰ ਨਾਲ, ਵੱਧ ਤੋਂ ਵੱਧ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਹੁਣ ਯੂਜ਼ਰਾਂ ਦੇ Bring Your Own Device (BYOD) ਡਿਵਾਈਸਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ। AI PC ਇਨ੍ਹਾਂ ਮਾਡਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹਨ। 2024 ਤੋਂ ਸ਼ੁਰੂ ਹੋ ਕੇ, Intel, AMD, ਅਤੇ Qualcomm ਨੇ PC ਨਿਰਮਾਤਿਆਂ ਨਾਲ ਮਿਲ ਕੇ AI PC ਲਾਂਚ ਕੀਤੇ ਹਨ ਜੋ ਹਾਰਡਵੇਅਰ ਤਬਦੀਲੀਆਂ ਰਾਹੀਂ ਸਥਾਨਕ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਦੀ ਤਾਇਨਾਤੀ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦੇ ਹਨ। ਇਸ ਚਰਚਾ ਵਿੱਚ, ਅਸੀਂ Intel AI PC ਤੇ Phi-3 ਨੂੰ ਕਿਵੇਂ ਤਾਇਨਾਤ ਕਰਨਾ ਹੈ, ਇਸ 'ਤੇ ਧਿਆਨ ਦੇਵਾਂਗੇ।

### NPU ਕੀ ਹੈ

NPU (Neural Processing Unit) ਇੱਕ ਸਮਰਪਿਤ ਪ੍ਰੋਸੈਸਰ ਜਾਂ ਵੱਡੇ SoC ਵਿੱਚ ਇੱਕ ਪ੍ਰੋਸੈਸਿੰਗ ਯੂਨਿਟ ਹੁੰਦਾ ਹੈ ਜੋ ਖਾਸ ਤੌਰ 'ਤੇ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਓਪਰੇਸ਼ਨਾਂ ਅਤੇ AI ਕੰਮਾਂ ਨੂੰ ਤੇਜ਼ ਕਰਨ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਆਮ CPU ਅਤੇ GPU ਤੋਂ ਵੱਖ, NPUs ਡਾਟਾ-ਚਲਿਤ ਪੈਰਾਲਲ ਕੰਪਿਊਟਿੰਗ ਲਈ ਅਨੁਕੂਲਿਤ ਹੁੰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਇਹ ਵੀਡੀਓ ਅਤੇ ਚਿੱਤਰਾਂ ਵਰਗੇ ਵੱਡੇ ਮਲਟੀਮੀਡੀਆ ਡਾਟਾ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਸੈਸ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਲਈ ਡਾਟਾ ਸੰਭਾਲਦੇ ਹਨ। ਇਹ ਖਾਸ ਕਰਕੇ AI ਸੰਬੰਧੀ ਕੰਮਾਂ ਜਿਵੇਂ ਕਿ ਬੋਲ ਚੀਨ੍ਹਾ, ਵੀਡੀਓ ਕਾਲਾਂ ਵਿੱਚ ਬੈਕਗ੍ਰਾਊਂਡ ਧੁੰਦਲਾ ਕਰਨਾ, ਅਤੇ ਫੋਟੋ ਜਾਂ ਵੀਡੀਓ ਸੰਪਾਦਨ ਜਿਵੇਂ ਆਬਜੈਕਟ ਡਿਟੈਕਸ਼ਨ ਵਿੱਚ ਮਹਿਰ ਹਨ।

## NPU ਅਤੇ GPU ਵਿੱਚ ਫਰਕ

ਜਦੋਂ ਕਿ ਬਹੁਤ ਸਾਰੇ AI ਅਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਕੰਮ GPU ਤੇ ਚਲਦੇ ਹਨ, GPU ਅਤੇ NPU ਵਿੱਚ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਫਰਕ ਹੈ।  
GPU ਆਪਣੀ ਪੈਰਾਲਲ ਕੰਪਿਊਟਿੰਗ ਸਮਰੱਥਾ ਲਈ ਜਾਣੇ ਜਾਂਦੇ ਹਨ, ਪਰ ਸਾਰੇ GPU ਗ੍ਰਾਫਿਕਸ ਤੋਂ ਇਲਾਵਾ ਸਮਾਨ ਤੌਰ ਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਨਹੀਂ ਹੁੰਦੇ। ਦੂਜੇ ਪਾਸੇ, NPU ਖਾਸ ਤੌਰ 'ਤੇ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਓਪਰੇਸ਼ਨਾਂ ਲਈ ਬਣਾਏ ਗਏ ਹਨ, ਜੋ AI ਕੰਮਾਂ ਲਈ ਬਹੁਤ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਹਨ।  

ਸੰਖੇਪ ਵਿੱਚ, NPUs ਉਹ ਗਣਿਤ ਦੇ ਮਾਹਿਰ ਹਨ ਜੋ AI ਗਣਨਾਵਾਂ ਨੂੰ ਤੇਜ਼ ਕਰਦੇ ਹਨ ਅਤੇ AI PC ਦੇ ਉਭਰਦੇ ਯੁੱਗ ਵਿੱਚ ਇੱਕ ਮੁੱਖ ਭੂਮਿਕਾ ਨਿਭਾਉਂਦੇ ਹਨ!

***ਇਹ ਉਦਾਹਰਨ Intel ਦੇ ਨਵੇਂ Intel Core Ultra Processor 'ਤੇ ਆਧਾਰਿਤ ਹੈ***

## **1. Phi-3 ਮਾਡਲ ਚਲਾਉਣ ਲਈ NPU ਦੀ ਵਰਤੋਂ ਕਰੋ**

Intel® NPU ਡਿਵਾਈਸ ਇੱਕ AI inference ਐਕਸਲੇਰੇਟਰ ਹੈ ਜੋ Intel ਕਲਾਇੰਟ CPU ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕੀਤਾ ਗਿਆ ਹੈ, ਜੋ Intel® Core™ Ultra ਜਨਰੇਸ਼ਨ ਦੇ CPU (ਜਿਸਨੂੰ ਪਹਿਲਾਂ Meteor Lake ਕਿਹਾ ਜਾਂਦਾ ਸੀ) ਤੋਂ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ। ਇਹ ਕ੍ਰਿਤ੍ਰਿਮ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਕੰਮਾਂ ਨੂੰ ਊਰਜਾ-ਕੁਸ਼ਲਤਾ ਨਾਲ ਚਲਾਉਣ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ।

![Latency](../../../../../translated_images/pa/aipcphitokenlatency.2be14f04f30a3bf7.webp)

![Latency770](../../../../../translated_images/pa/aipcphitokenlatency770.e923609a57c5d394.webp)

**Intel NPU Acceleration Library**

Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) ਇੱਕ Python ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ ਤੁਹਾਡੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੀ ਕੁਸ਼ਲਤਾ ਨੂੰ ਵਧਾਉਂਦੀ ਹੈ, Intel Neural Processing Unit (NPU) ਦੀ ਤਾਕਤ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਉੱਚ-ਗਤੀ ਗਣਨਾਵਾਂ ਕਰਨ ਲਈ।

Intel® Core™ Ultra ਪ੍ਰੋਸੈਸਰਾਂ ਨਾਲ ਚਲਦੇ AI PC 'ਤੇ Phi-3-mini ਦਾ ਉਦਾਹਰਨ।

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Python ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ pip ਨਾਲ ਇੰਸਟਾਲ ਕਰੋ

```bash

   pip install intel-npu-acceleration-library

```

***ਨੋਟ*** ਪ੍ਰੋਜੈਕਟ ਅਜੇ ਵਿਕਾਸ ਵਿੱਚ ਹੈ, ਪਰ ਰੈਫਰੈਂਸ ਮਾਡਲ ਪਹਿਲਾਂ ਹੀ ਕਾਫੀ ਪੂਰਾ ਹੈ।

### **Intel NPU Acceleration Library ਨਾਲ Phi-3 ਚਲਾਉਣਾ**

Intel NPU ਐਕਸਲੇਰੇਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ, ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਰਵਾਇਤੀ ਐਨਕੋਡਿੰਗ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਨਹੀਂ ਕਰਦੀ। ਤੁਹਾਨੂੰ ਸਿਰਫ਼ ਇਸ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੂਲ Phi-3 ਮਾਡਲ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ ਹੁੰਦਾ ਹੈ, ਜਿਵੇਂ FP16, INT8, INT4, ਆਦਿ।

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

ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਸਫਲ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਅੱਗੇ ਚੱਲ ਕੇ NPU ਨੂੰ ਕਾਲ ਕਰਕੇ Phi-3 ਮਾਡਲ ਚਲਾਓ।

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

ਕੋਡ ਚਲਾਉਂਦੇ ਸਮੇਂ, ਅਸੀਂ Task Manager ਰਾਹੀਂ NPU ਦੀ ਚਾਲੂ ਹਾਲਤ ਵੇਖ ਸਕਦੇ ਹਾਂ।

![NPU](../../../../../translated_images/pa/aipc_NPU.7a3cb6db47b377e1.webp)

***ਨਮੂਨੇ*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Phi-3 ਮਾਡਲ ਚਲਾਉਣ ਲਈ DirectML + ONNX Runtime ਦੀ ਵਰਤੋਂ ਕਰੋ**

### **DirectML ਕੀ ਹੈ**

[DirectML](https://github.com/microsoft/DirectML) ਇੱਕ ਉੱਚ-ਕਾਰਗਰ, ਹਾਰਡਵੇਅਰ-ਐਕਸਲੇਰੇਟਡ DirectX 12 ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਈ ਬਣਾਈ ਗਈ ਹੈ। DirectML ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਅਤੇ ਡਰਾਈਵਰਾਂ 'ਤੇ ਆਮ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਕੰਮਾਂ ਲਈ GPU ਐਕਸਲੇਰੇਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ AMD, Intel, NVIDIA, ਅਤੇ Qualcomm ਦੇ ਸਾਰੇ DirectX 12 ਸਮਰਥਿਤ GPU ਸ਼ਾਮਲ ਹਨ।

ਜਦੋਂ ਇਹ ਸਵਤੰਤਰ ਤੌਰ 'ਤੇ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ DirectML API ਇੱਕ ਨੀਵੀਂ ਸਤਰ ਦੀ DirectX 12 ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ ਉੱਚ-ਕਾਰਗਰਤਾ ਅਤੇ ਘੱਟ-ਵਿਲੰਬਤਾ ਵਾਲੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਉਚਿਤ ਹੈ, ਜਿਵੇਂ ਕਿ ਫਰੇਮਵਰਕ, ਖੇਡਾਂ ਅਤੇ ਹੋਰ ਰੀਅਲ-ਟਾਈਮ ਐਪਲੀਕੇਸ਼ਨ। DirectML ਦੀ Direct3D 12 ਨਾਲ ਬਿਨਾਂ ਰੁਕਾਵਟ ਕੰਮ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਅਤੇ ਘੱਟ ਓਵਰਹੈੱਡ ਇਸਨੂੰ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਨੂੰ ਤੇਜ਼ ਕਰਨ ਲਈ ਬਹੁਤ ਵਧੀਆ ਬਣਾਉਂਦੀ ਹੈ, ਜਦੋਂ ਕਿ ਉੱਚ ਕਾਰਗਰਤਾ ਅਤੇ ਹਾਰਡਵੇਅਰ 'ਤੇ ਨਤੀਜਿਆਂ ਦੀ ਭਰੋਸੇਯੋਗਤਾ ਜ਼ਰੂਰੀ ਹੋਵੇ।

***ਨੋਟ*** : ਨਵੀਂ DirectML ਪਹਿਲਾਂ ਹੀ NPU ਨੂੰ ਸਪੋਰਟ ਕਰਦੀ ਹੈ (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML ਅਤੇ CUDA ਦੀ ਸਮਰੱਥਾ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਦੇ ਮਾਮਲੇ ਵਿੱਚ ਤੁਲਨਾ:

**DirectML** ਮਾਈਕ੍ਰੋਸਾਫਟ ਵੱਲੋਂ ਵਿਕਸਿਤ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਾਇਬ੍ਰੇਰੀ ਹੈ। ਇਹ Windows ਡਿਵਾਈਸਾਂ, ਜਿਵੇਂ ਡੈਸਕਟਾਪ, ਲੈਪਟਾਪ ਅਤੇ ਐਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਕੰਮਾਂ ਨੂੰ ਤੇਜ਼ ਕਰਨ ਲਈ ਬਣਾਈ ਗਈ ਹੈ।  
- DX12-ਅਧਾਰਿਤ: DirectML DirectX 12 (DX12) 'ਤੇ ਬਣੀ ਹੈ, ਜੋ NVIDIA ਅਤੇ AMD ਸਮੇਤ ਵੱਖ-ਵੱਖ GPU ਲਈ ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ ਦਿੰਦੀ ਹੈ।  
- ਵਿਆਪਕ ਸਹਾਇਤਾ: ਕਿਉਂਕਿ ਇਹ DX12 ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ, DirectML ਕਿਸੇ ਵੀ DX12 ਸਮਰਥਿਤ GPU ਨਾਲ ਕੰਮ ਕਰ ਸਕਦੀ ਹੈ, ਇੰਟਿਗ੍ਰੇਟਿਡ GPU ਸਮੇਤ।  
- ਚਿੱਤਰ ਪ੍ਰੋਸੈਸਿੰਗ: DirectML ਚਿੱਤਰਾਂ ਅਤੇ ਹੋਰ ਡਾਟਾ ਨੂੰ ਨਿਊਰਲ ਨੈੱਟਵਰਕਾਂ ਰਾਹੀਂ ਪ੍ਰੋਸੈਸ ਕਰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਚਿੱਤਰ ਪਛਾਣ, ਆਬਜੈਕਟ ਡਿਟੈਕਸ਼ਨ ਵਰਗੇ ਕੰਮਾਂ ਲਈ ਉਚਿਤ ਹੈ।  
- ਸੈਟਅੱਪ ਵਿੱਚ ਆਸਾਨੀ: DirectML ਸੈਟਅੱਪ ਕਰਨਾ ਸੌਖਾ ਹੈ ਅਤੇ ਇਸ ਲਈ GPU ਨਿਰਮਾਤਿਆਂ ਤੋਂ ਖਾਸ SDK ਜਾਂ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਲੋੜ ਨਹੀਂ।  
- ਪ੍ਰਦਰਸ਼ਨ: ਕੁਝ ਹਾਲਤਾਂ ਵਿੱਚ, DirectML ਚੰਗਾ ਪ੍ਰਦਰਸ਼ਨ ਕਰਦਾ ਹੈ ਅਤੇ ਕੁਝ ਕੰਮਾਂ ਲਈ CUDA ਨਾਲੋਂ ਤੇਜ਼ ਵੀ ਹੋ ਸਕਦਾ ਹੈ।  
- ਸੀਮਾਵਾਂ: ਪਰ ਕੁਝ ਹਾਲਤਾਂ ਵਿੱਚ, ਖਾਸ ਕਰਕੇ float16 ਵੱਡੇ ਬੈਚ ਸਾਈਜ਼ ਲਈ, DirectML ਧੀਮਾ ਹੋ ਸਕਦਾ ਹੈ।  

**CUDA** NVIDIA ਦਾ ਪੈਰਾਲਲ ਕੰਪਿਊਟਿੰਗ ਪਲੇਟਫਾਰਮ ਅਤੇ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਮਾਡਲ ਹੈ। ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ NVIDIA GPU ਦੀ ਤਾਕਤ ਨੂੰ ਆਮ ਕੰਪਿਊਟਿੰਗ ਲਈ ਵਰਤਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਅਤੇ ਵਿਗਿਆਨਕ ਸਿਮੂਲੇਸ਼ਨ ਸ਼ਾਮਲ ਹਨ।  
- NVIDIA-ਖਾਸ: CUDA NVIDIA GPU ਨਾਲ ਗਹਿਰਾਈ ਨਾਲ ਜੁੜਿਆ ਹੈ ਅਤੇ ਖਾਸ ਤੌਰ 'ਤੇ ਉਨ੍ਹਾਂ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ।  
- ਬਹੁਤ ਅਨੁਕੂਲਿਤ: ਇਹ GPU-ਐਕਸਲੇਰੇਟਡ ਕੰਮਾਂ ਲਈ ਬਹੁਤ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਦਿੰਦਾ ਹੈ, ਖਾਸ ਕਰਕੇ NVIDIA GPU ਵਰਤਣ ਸਮੇਂ।  
- ਵਿਆਪਕ ਵਰਤੋਂ: ਬਹੁਤ ਸਾਰੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਫਰੇਮਵਰਕ ਅਤੇ ਲਾਇਬ੍ਰੇਰੀਆਂ (ਜਿਵੇਂ TensorFlow ਅਤੇ PyTorch) CUDA ਸਹਾਇਤਾ ਰੱਖਦੀਆਂ ਹਨ।  
- ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ: ਵਿਕਾਸਕਾਰ CUDA ਸੈਟਿੰਗਾਂ ਨੂੰ ਖਾਸ ਕੰਮਾਂ ਲਈ ਬਹੁਤ ਬਰੀਕੀ ਨਾਲ ਢਾਲ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਮਿਲਦਾ ਹੈ।  
- ਸੀਮਾਵਾਂ: ਪਰ CUDA ਦੀ ਨਿਰਭਰਤਾ NVIDIA ਹਾਰਡਵੇਅਰ 'ਤੇ ਹੋਣ ਕਾਰਨ, ਇਹ ਵੱਖ-ਵੱਖ GPU ਲਈ ਵਿਆਪਕ ਅਨੁਕੂਲਤਾ ਵਿੱਚ ਰੁਕਾਵਟ ਬਣ ਸਕਦੀ ਹੈ।  

### DirectML ਅਤੇ CUDA ਵਿੱਚ ਚੋਣ

DirectML ਅਤੇ CUDA ਵਿੱਚ ਚੋਣ ਤੁਹਾਡੇ ਖਾਸ ਵਰਤੋਂ ਦੇ ਕੇਸ, ਹਾਰਡਵੇਅਰ ਉਪਲਬਧਤਾ ਅਤੇ ਪਸੰਦਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ।  
ਜੇ ਤੁਸੀਂ ਵਿਆਪਕ ਅਨੁਕੂਲਤਾ ਅਤੇ ਸੌਖਾ ਸੈਟਅੱਪ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ DirectML ਚੰਗਾ ਵਿਕਲਪ ਹੋ ਸਕਦਾ ਹੈ। ਪਰ ਜੇ ਤੁਹਾਡੇ ਕੋਲ NVIDIA GPU ਹਨ ਅਤੇ ਤੁਹਾਨੂੰ ਬਹੁਤ ਅਨੁਕੂਲਿਤ ਪ੍ਰਦਰਸ਼ਨ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ CUDA ਇੱਕ ਮਜ਼ਬੂਤ ਵਿਕਲਪ ਹੈ। ਸੰਖੇਪ ਵਿੱਚ, ਦੋਹਾਂ ਦੇ ਆਪਣੇ ਫਾਇਦੇ ਅਤੇ ਨੁਕਸਾਨ ਹਨ, ਇਸ ਲਈ ਆਪਣੀਆਂ ਜ਼ਰੂਰਤਾਂ ਅਤੇ ਉਪਲਬਧ ਹਾਰਡਵੇਅਰ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖ ਕੇ ਫੈਸਲਾ ਕਰੋ।  

### **ONNX Runtime ਨਾਲ ਜਨਰੇਟਿਵ AI**

AI ਦੇ ਯੁੱਗ ਵਿੱਚ, AI ਮਾਡਲਾਂ ਦੀ ਪੋਰਟੇਬਿਲਿਟੀ ਬਹੁਤ ਮਹੱਤਵਪੂਰਨ ਹੈ। ONNX Runtime ਸਿਖਲਾਈ ਗਏ ਮਾਡਲਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਡਿਵਾਈਸਾਂ 'ਤੇ ਆਸਾਨੀ ਨਾਲ ਤਾਇਨਾਤ ਕਰ ਸਕਦਾ ਹੈ। ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਇੰਫਰੈਂਸ ਫਰੇਮਵਰਕ ਦੀ ਚਿੰਤਾ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ ਅਤੇ ਇੱਕ ਇਕਸਾਰ API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਡਲ ਇੰਫਰੈਂਸ ਕਰ ਸਕਦੇ ਹਨ। ਜਨਰੇਟਿਵ AI ਦੇ ਯੁੱਗ ਵਿੱਚ, ONNX Runtime ਨੇ ਕੋਡ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਵੀ ਕੀਤੀ ਹੈ (https://onnxruntime.ai/docs/genai/). ਇਸ ਅਪਟੀਮਾਈਜ਼ਡ ONNX Runtime ਰਾਹੀਂ, ਕਵਾਂਟਾਈਜ਼ਡ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਵੱਖ-ਵੱਖ ਟਰਮੀਨਲਾਂ 'ਤੇ ਇੰਫਰੈਂਸ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ONNX Runtime ਨਾਲ ਜਨਰੇਟਿਵ AI ਵਿੱਚ, ਤੁਸੀਂ Python, C#, C / C++ ਰਾਹੀਂ AI ਮਾਡਲ API ਨੂੰ ਇੰਫਰੈਂਸ ਕਰ ਸਕਦੇ ਹੋ। ਬਿਲਕੁਲ, iPhone 'ਤੇ ਤਾਇਨਾਤੀ ਲਈ C++ ਦੀ ONNX Runtime API ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

[ਨਮੂਨਾ ਕੋਡ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***ONNX Runtime ਲਾਇਬ੍ਰੇਰੀ ਨਾਲ ਜਨਰੇਟਿਵ AI ਕੰਪਾਈਲ ਕਰੋ***

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

**ਲਾਇਬ੍ਰੇਰੀ ਇੰਸਟਾਲ ਕਰੋ**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

ਇਹ ਚਲਾਉਣ ਦਾ ਨਤੀਜਾ ਹੈ

![DML](../../../../../translated_images/pa/aipc_DML.52a44180393ab491.webp)

***ਨਮੂਨੇ*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Phi-3 ਮਾਡਲ ਚਲਾਉਣ ਲਈ Intel OpenVino ਦੀ ਵਰਤੋਂ ਕਰੋ**

### **OpenVINO ਕੀ ਹੈ**

[OpenVINO](https://github.com/openvinotoolkit/openvino) ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਟੂਲਕਿਟ ਹੈ ਜੋ ਡੀਪ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਨੂੰ ਅਪਟੀਮਾਈਜ਼ ਅਤੇ ਤਾਇਨਾਤ ਕਰਨ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਇਹ TensorFlow, PyTorch ਅਤੇ ਹੋਰ ਪ੍ਰਸਿੱਧ ਫਰੇਮਵਰਕਾਂ ਤੋਂ ਵਿਜ਼ਨ, ਆਡੀਓ ਅਤੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਲਈ ਡੀਪ ਲਰਨਿੰਗ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਤੇਜ਼ ਕਰਦਾ ਹੈ। OpenVINO ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ। OpenVINO CPU ਅਤੇ GPU ਦੇ ਨਾਲ ਮਿਲ ਕੇ Phi-3 ਮਾਡਲ ਚਲਾਉਣ ਲਈ ਵੀ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

***ਨੋਟ***: ਇਸ ਸਮੇਂ OpenVINO NPU ਨੂੰ ਸਪੋਰਟ ਨਹੀਂ ਕਰਦਾ।

### **OpenVINO ਲਾਇਬ੍ਰੇਰੀ ਇੰਸਟਾਲ ਕਰੋ**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **OpenVINO ਨਾਲ Phi-3 ਚਲਾਉਣਾ**

NPU ਵਾਂਗ, OpenVINO ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ਡ ਮਾਡਲ ਚਲਾਕੇ ਕਾਲ ਕਰਦਾ ਹੈ। ਸਾਨੂੰ ਪਹਿਲਾਂ Phi-3 ਮਾਡਲ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ ਪੈਂਦਾ ਹੈ ਅਤੇ optimum-cli ਰਾਹੀਂ ਕਮਾਂਡ ਲਾਈਨ 'ਤੇ ਮਾਡਲ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਪੂਰਾ ਕਰਨਾ ਹੁੰਦਾ ਹੈ।

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

ਬਦਲੇ ਹੋਏ ਫਾਰਮੈਟ, ਇਸ ਤਰ੍ਹਾਂ

![openvino_convert](../../../../../translated_images/pa/aipc_OpenVINO_convert.9e6360b65331ffca.webp)

ਮਾਡਲ ਪਾਥ (model_dir), ਸੰਬੰਧਿਤ ਸੰਰਚਨਾਵਾਂ (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}), ਅਤੇ ਹਾਰਡਵੇਅਰ-ਐਕਸਲੇਰੇਟਡ ਡਿਵਾਈਸ (GPU.0) ਨੂੰ OVModelForCausalLM ਰਾਹੀਂ ਲੋਡ ਕਰੋ

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

ਕੋਡ ਚਲਾਉਂਦੇ ਸਮੇਂ, ਅਸੀਂ Task Manager ਰਾਹੀਂ GPU ਦੀ ਚਾਲੂ ਹਾਲਤ ਵੇਖ ਸਕਦੇ ਹਾਂ।

![openvino_gpu](../../../../../translated_images/pa/aipc_OpenVINO_GPU.20180edfffd91e55.webp)

***ਨਮੂਨੇ*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***ਨੋਟ*** : ਉਪਰੋਕਤ ਤਿੰਨ ਤਰੀਕੇ ਆਪਣੇ-ਆਪ ਵਿੱਚ ਫਾਇਦੇਮੰਦ ਹਨ, ਪਰ AI PC ਇੰਫਰੈਂਸ ਲਈ NPU ਐਕਸਲੇਰੇਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।