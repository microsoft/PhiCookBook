<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:55:43+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "tr"
}
-->
# **Intel OpenVINO kullanarak Phi-3.5'in Kantitleştirilmesi**

Intel, çok sayıda kullanıcısı olan en köklü CPU üreticisidir. Makine öğrenimi ve derin öğrenmenin yükselişiyle birlikte Intel, AI hızlandırma yarışına katılmıştır. Model çıkarımı için Intel sadece GPU ve CPU değil, aynı zamanda NPU da kullanmaktadır.

Phi-3.x Ailesini uç tarafta dağıtmayı hedefliyoruz ve AI PC ile Copilot PC'nin en önemli parçası olmasını umuyoruz. Uç tarafta modelin yüklenmesi farklı donanım üreticilerinin iş birliğine bağlıdır. Bu bölümde ağırlıklı olarak Intel OpenVINO'nun kantitatif model uygulama senaryosuna odaklanacağız.

## **OpenVINO Nedir**

OpenVINO, buluttan uca derin öğrenme modellerini optimize etmek ve dağıtmak için açık kaynaklı bir araç setidir. PyTorch, TensorFlow, ONNX gibi popüler çerçevelerden gelen modellerle, üretken AI, video, ses ve dil gibi çeşitli kullanım durumlarında derin öğrenme çıkarımını hızlandırır. Modelleri dönüştürün ve optimize edin, ardından Intel® donanımları ve ortamlarının karışımında, yerel veya cihazda, tarayıcıda veya bulutta dağıtım yapın.

Artık OpenVINO ile Intel donanımında GenAI modelini hızlıca kantitleştirebilir ve model referansını hızlandırabilirsiniz.

OpenVINO şu anda Phi-3.5-Vision ve Phi-3.5 Instruct modellerinin kantitleştirme dönüşümünü desteklemektedir.

### **Ortam Kurulumu**

Lütfen aşağıdaki ortam bağımlılıklarının yüklü olduğundan emin olun, bu requirement.txt dosyasıdır

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO kullanarak Phi-3.5-Instruct’in Kantitleştirilmesi**

Terminalde, lütfen bu betiği çalıştırın

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO kullanarak Phi-3.5-Vision’un Kantitleştirilmesi**

Lütfen bu betiği Python veya Jupyter lab ortamında çalıştırın

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Intel OpenVINO ile Phi-3.5 için Örnekler**

| Laboratuvarlar    | Tanıtım | Git |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instruct Tanıtımı  | AI PC'nizde Phi-3.5 Instruct nasıl kullanılır öğrenin    |  [Git](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (görüntü) Tanıtımı | AI PC'nizde Phi-3.5 Vision ile görüntü analizini öğrenin      |  [Git](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (video) Tanıtımı   | AI PC'nizde Phi-3.5 Vision ile video analizini öğrenin    |  [Git](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |


## **Kaynaklar**

1. Intel OpenVINO hakkında daha fazla bilgi edinin [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Deposu [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.