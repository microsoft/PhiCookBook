<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-07-16T20:01:53+00:00",
  "source_file": "md/01.Introduction/03/AIPC_Inference.md",
  "language_code": "th"
}
-->
# **การทำ Inference Phi-3 บน AI PC**

ด้วยความก้าวหน้าของปัญญาประดิษฐ์เชิงสร้างสรรค์ (generative AI) และการพัฒนาความสามารถของฮาร์ดแวร์อุปกรณ์ขอบเครือข่าย (edge device) ทำให้มีโมเดล generative AI จำนวนมากขึ้นที่สามารถนำไปใช้งานบนอุปกรณ์ Bring Your Own Device (BYOD) ของผู้ใช้ได้ AI PC ก็เป็นหนึ่งในโมเดลเหล่านี้ เริ่มตั้งแต่ปี 2024 Intel, AMD และ Qualcomm ได้ร่วมมือกับผู้ผลิต PC เพื่อนำเสนอ AI PC ที่ช่วยให้การใช้งานโมเดล generative AI แบบท้องถิ่นเป็นไปได้ผ่านการปรับแต่งฮาร์ดแวร์ ในบทความนี้เราจะเน้นที่ Intel AI PC และสำรวจวิธีการใช้งาน Phi-3 บน Intel AI PC

### NPU คืออะไร

NPU (Neural Processing Unit) คือหน่วยประมวลผลเฉพาะทางที่ฝังอยู่ใน SoC ขนาดใหญ่ ออกแบบมาเพื่อเร่งการทำงานของเครือข่ายประสาทเทียมและงาน AI โดยเฉพาะ ต่างจาก CPU และ GPU ทั่วไป NPU ถูกปรับแต่งให้เหมาะกับการประมวลผลแบบขนานที่เน้นข้อมูลจำนวนมาก ทำให้มีประสิทธิภาพสูงในการประมวลผลข้อมูลมัลติมีเดียขนาดใหญ่ เช่น วิดีโอและภาพ รวมถึงการประมวลผลข้อมูลสำหรับเครือข่ายประสาทเทียม NPU เหมาะอย่างยิ่งกับงานที่เกี่ยวข้องกับ AI เช่น การรู้จำเสียง การเบลอพื้นหลังในวิดีโอคอล และกระบวนการแก้ไขภาพหรือวิดีโอ เช่น การตรวจจับวัตถุ

## NPU กับ GPU

แม้งาน AI และ machine learning หลายอย่างจะรันบน GPU แต่มีความแตกต่างสำคัญระหว่าง GPU กับ NPU
GPU มีชื่อเสียงในด้านความสามารถประมวลผลแบบขนาน แต่ไม่ใช่ GPU ทุกตัวที่จะมีประสิทธิภาพเท่ากันนอกเหนือจากการประมวลผลกราฟิก ในขณะที่ NPU ถูกสร้างขึ้นมาเพื่อการคำนวณที่ซับซ้อนในงานเครือข่ายประสาทเทียมโดยเฉพาะ ทำให้มีประสิทธิภาพสูงสำหรับงาน AI

สรุปคือ NPU คือผู้เชี่ยวชาญทางคณิตศาสตร์ที่ช่วยเร่งการคำนวณ AI และมีบทบาทสำคัญในยุคใหม่ของ AI PC!

***ตัวอย่างนี้อ้างอิงจาก Intel Core Ultra Processor รุ่นล่าสุดของ Intel***

## **1. ใช้ NPU เพื่อรันโมเดล Phi-3**

อุปกรณ์ Intel® NPU คืออุปกรณ์เร่งการทำงาน AI inference ที่ฝังรวมกับ CPU ของ Intel client เริ่มตั้งแต่ Intel® Core™ Ultra รุ่นใหม่ (เดิมชื่อ Meteor Lake) ช่วยให้การทำงานของเครือข่ายประสาทเทียมเป็นไปอย่างประหยัดพลังงาน

![Latency](../../../../../translated_images/th/aipcphitokenlatency.2be14f04f30a3bf7.png)

![Latency770](../../../../../translated_images/th/aipcphitokenlatency770.e923609a57c5d394.png)

**Intel NPU Acceleration Library**

Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) คือไลบรารี Python ที่ออกแบบมาเพื่อเพิ่มประสิทธิภาพแอปพลิเคชันของคุณโดยใช้พลังของ Intel Neural Processing Unit (NPU) ในการประมวลผลความเร็วสูงบนฮาร์ดแวร์ที่รองรับ

ตัวอย่าง Phi-3-mini บน AI PC ที่ใช้ Intel® Core™ Ultra processors

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

ติดตั้งไลบรารี Python ด้วย pip

```bash

   pip install intel-npu-acceleration-library

```

***หมายเหตุ*** โปรเจกต์ยังอยู่ในระหว่างพัฒนา แต่โมเดลอ้างอิงมีความสมบูรณ์มากแล้ว

### **การรัน Phi-3 ด้วย Intel NPU Acceleration Library**

เมื่อใช้การเร่งด้วย Intel NPU ไลบรารีนี้จะไม่ส่งผลกระทบต่อกระบวนการเข้ารหัสแบบดั้งเดิม คุณเพียงแค่ใช้ไลบรารีนี้เพื่อทำการ quantize โมเดล Phi-3 ดั้งเดิม เช่น FP16, INT8, INT4 เป็นต้น

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

หลังจากการ quantize สำเร็จ ให้ดำเนินการเรียกใช้ NPU เพื่อรันโมเดล Phi-3

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

เมื่อรันโค้ด เราสามารถดูสถานะการทำงานของ NPU ผ่าน Task Manager

![NPU](../../../../../translated_images/th/aipc_NPU.7a3cb6db47b377e1.png)

***ตัวอย่าง*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. ใช้ DirectML + ONNX Runtime เพื่อรันโมเดล Phi-3**

### **DirectML คืออะไร**

[DirectML](https://github.com/microsoft/DirectML) คือไลบรารี DirectX 12 ที่เร่งความเร็วด้วยฮาร์ดแวร์สำหรับงาน machine learning โดย DirectML ให้การเร่งด้วย GPU สำหรับงาน machine learning ทั่วไปบนฮาร์ดแวร์และไดรเวอร์ที่รองรับหลากหลาย รวมถึง GPU ที่รองรับ DirectX 12 จากผู้ผลิตอย่าง AMD, Intel, NVIDIA และ Qualcomm

เมื่อใช้งานแบบ standalone DirectML API คือไลบรารี DirectX 12 ระดับต่ำ เหมาะสำหรับแอปพลิเคชันที่ต้องการประสิทธิภาพสูงและหน่วงเวลาต่ำ เช่น เฟรมเวิร์ก เกม และแอปพลิเคชันเรียลไทม์ การทำงานร่วมกันอย่างไร้รอยต่อของ DirectML กับ Direct3D 12 รวมถึงค่า overhead ต่ำและความสอดคล้องในการทำงานข้ามฮาร์ดแวร์ ทำให้ DirectML เหมาะสำหรับเร่ง machine learning เมื่อทั้งประสิทธิภาพสูงและความน่าเชื่อถือของผลลัพธ์ข้ามฮาร์ดแวร์เป็นสิ่งสำคัญ

***หมายเหตุ*** : DirectML รุ่นล่าสุดรองรับ NPU แล้ว (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### ความสามารถและประสิทธิภาพของ DirectML และ CUDA

**DirectML** คือไลบรารี machine learning ที่พัฒนาโดย Microsoft ออกแบบมาเพื่อเร่งงาน machine learning บนอุปกรณ์ Windows รวมถึงเดสก์ท็อป โน้ตบุ๊ก และอุปกรณ์ edge
- พื้นฐาน DX12: DirectML สร้างบน DirectX 12 (DX12) ซึ่งรองรับฮาร์ดแวร์ GPU หลากหลาย รวมถึง NVIDIA และ AMD
- รองรับกว้าง: เนื่องจากใช้ DX12 DirectML จึงทำงานกับ GPU ที่รองรับ DX12 ได้ทุกตัว แม้แต่ GPU แบบฝัง
- ประมวลผลภาพ: DirectML ประมวลผลภาพและข้อมูลอื่น ๆ ด้วยเครือข่ายประสาทเทียม เหมาะกับงานเช่น การรู้จำภาพ การตรวจจับวัตถุ และอื่น ๆ
- ติดตั้งง่าย: การตั้งค่า DirectML ทำได้ง่าย ไม่ต้องใช้ SDK หรือไลบรารีเฉพาะจากผู้ผลิต GPU
- ประสิทธิภาพ: ในบางกรณี DirectML ทำงานได้ดีและอาจเร็วกว่าคู่แข่งอย่าง CUDA โดยเฉพาะงานบางประเภท
- ข้อจำกัด: อย่างไรก็ตาม บางครั้ง DirectML อาจช้ากว่า โดยเฉพาะกับงานที่ใช้ float16 และ batch ขนาดใหญ่

**CUDA** คือแพลตฟอร์มและโมเดลการเขียนโปรแกรมแบบขนานของ NVIDIA ช่วยให้นักพัฒนาสามารถใช้พลังของ GPU NVIDIA สำหรับงานทั่วไป รวมถึง machine learning และการจำลองทางวิทยาศาสตร์
- เฉพาะ NVIDIA: CUDA ผูกติดกับ GPU ของ NVIDIA และออกแบบมาเพื่อใช้งานกับ GPU เหล่านี้โดยเฉพาะ
- ปรับแต่งสูง: ให้ประสิทธิภาพยอดเยี่ยมสำหรับงานที่เร่งด้วย GPU โดยเฉพาะบน GPU ของ NVIDIA
- ใช้กันแพร่หลาย: เฟรมเวิร์กและไลบรารี machine learning หลายตัว (เช่น TensorFlow และ PyTorch) รองรับ CUDA
- ปรับแต่งได้: นักพัฒนาสามารถปรับแต่งการตั้งค่า CUDA สำหรับงานเฉพาะ เพื่อให้ได้ประสิทธิภาพสูงสุด
- ข้อจำกัด: อย่างไรก็ตาม CUDA ขึ้นอยู่กับฮาร์ดแวร์ NVIDIA ซึ่งอาจจำกัดความเข้ากันได้กับ GPU อื่น ๆ

### การเลือกใช้ระหว่าง DirectML กับ CUDA

การเลือกใช้ DirectML หรือ CUDA ขึ้นอยู่กับกรณีการใช้งาน ฮาร์ดแวร์ที่มี และความชอบส่วนตัว
ถ้าคุณต้องการความเข้ากันได้กว้างและตั้งค่าง่าย DirectML อาจเป็นตัวเลือกที่ดี แต่ถ้าคุณมี GPU NVIDIA และต้องการประสิทธิภาพสูง CUDA ก็ยังคงเป็นตัวเลือกที่แข็งแกร่ง สรุปคือทั้ง DirectML และ CUDA มีจุดแข็งและข้อจำกัดของตัวเอง ควรพิจารณาความต้องการและฮาร์ดแวร์ที่มีเมื่อเลือกใช้งาน

### **Generative AI กับ ONNX Runtime**

ในยุค AI ความสามารถในการย้ายโมเดล AI เป็นสิ่งสำคัญ ONNX Runtime ช่วยให้สามารถนำโมเดลที่ผ่านการฝึกมาแล้วไปใช้งานบนอุปกรณ์ต่าง ๆ ได้อย่างง่ายดาย นักพัฒนาไม่ต้องกังวลกับเฟรมเวิร์ก inference และใช้ API เดียวกันในการทำ inference โมเดล ในยุค generative AI ONNX Runtime ยังมีการปรับแต่งโค้ด (https://onnxruntime.ai/docs/genai/) ผ่าน ONNX Runtime ที่ปรับแต่งแล้ว โมเดล generative AI ที่ผ่านการ quantize สามารถทำ inference บนอุปกรณ์ต่าง ๆ ได้ ใน Generative AI กับ ONNX Runtime คุณสามารถเรียกใช้ AI model API ผ่าน Python, C#, C / C++ แน่นอนว่าการ deploy บน iPhone สามารถใช้ประโยชน์จาก API Generative AI with ONNX Runtime ใน C++

[ตัวอย่างโค้ด](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***คอมไพล์ไลบรารี generative AI กับ ONNX Runtime***

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

**ติดตั้งไลบรารี**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

นี่คือผลลัพธ์การรัน

![DML](../../../../../translated_images/th/aipc_DML.52a44180393ab491.png)

***ตัวอย่าง*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. ใช้ Intel OpenVino เพื่อรันโมเดล Phi-3**

### **OpenVINO คืออะไร**

[OpenVINO](https://github.com/openvinotoolkit/openvino) คือชุดเครื่องมือโอเพนซอร์สสำหรับการปรับแต่งและ deploy โมเดล deep learning ช่วยเพิ่มประสิทธิภาพ deep learning สำหรับโมเดลด้านภาพ เสียง และภาษา จากเฟรมเวิร์กยอดนิยมอย่าง TensorFlow, PyTorch และอื่น ๆ เริ่มต้นใช้งาน OpenVINO OpenVINO ยังสามารถใช้ร่วมกับ CPU และ GPU เพื่อรันโมเดล Phi-3 ได้

***หมายเหตุ***: ปัจจุบัน OpenVINO ยังไม่รองรับ NPU

### **ติดตั้งไลบรารี OpenVINO**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **การรัน Phi-3 ด้วย OpenVINO**

เช่นเดียวกับ NPU, OpenVINO เรียกใช้งานโมเดล generative AI โดยการรันโมเดลที่ผ่านการ quantize เราต้องทำการ quantize โมเดล Phi-3 ก่อน และทำการ quantize ผ่านคำสั่ง optimum-cli

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

รูปแบบที่แปลงแล้วจะเป็นแบบนี้

![openvino_convert](../../../../../translated_images/th/aipc_OpenVINO_convert.9e6360b65331ffca.png)

โหลดเส้นทางโมเดล (model_dir), การตั้งค่าที่เกี่ยวข้อง (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) และอุปกรณ์เร่งความเร็วฮาร์ดแวร์ (GPU.0) ผ่าน OVModelForCausalLM

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

เมื่อรันโค้ด เราสามารถดูสถานะการทำงานของ GPU ผ่าน Task Manager

![openvino_gpu](../../../../../translated_images/th/aipc_OpenVINO_GPU.20180edfffd91e55.png)

***ตัวอย่าง*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***หมายเหตุ*** : ทั้งสามวิธีข้างต้นมีข้อดีของตัวเอง แต่แนะนำให้ใช้การเร่งด้วย NPU สำหรับการ inference บน AI PC

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้