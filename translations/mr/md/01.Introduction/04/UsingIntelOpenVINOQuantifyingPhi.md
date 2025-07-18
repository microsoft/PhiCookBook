<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:00:30+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "mr"
}
-->
# **Intel OpenVINO वापरून Phi-3.5 चे क्वांटायझेशन**

Intel हा सर्वात पारंपरिक CPU निर्माता असून त्याचे अनेक वापरकर्ते आहेत. मशीन लर्निंग आणि डीप लर्निंगच्या वाढीसह, Intel ने AI अॅक्सेलरेशनच्या स्पर्धेतही प्रवेश केला आहे. मॉडेल इन्फरन्ससाठी Intel फक्त GPU आणि CPU वापरत नाही, तर NPU देखील वापरतो.

आम्हाला Phi-3.x कुटुंबाला एंड साइडवर तैनात करण्याची आशा आहे, ज्यामुळे ते AI PC आणि Copilot PC चा सर्वात महत्त्वाचा भाग बनेल. एंड साइडवर मॉडेल लोडिंग वेगवेगळ्या हार्डवेअर उत्पादकांच्या सहकार्यावर अवलंबून असते. हा अध्याय मुख्यतः Intel OpenVINO च्या क्वांटिटेटिव्ह मॉडेलच्या वापरावर लक्ष केंद्रित करतो.

## **OpenVINO म्हणजे काय**

OpenVINO हा क्लाउडपासून एजपर्यंत डीप लर्निंग मॉडेल्सचे ऑप्टिमायझेशन आणि तैनाती करण्यासाठी एक ओपन-सोर्स टूलकिट आहे. हे जनरेटिव्ह AI, व्हिडिओ, ऑडिओ आणि भाषा यांसारख्या विविध वापराच्या प्रकरणांमध्ये डीप लर्निंग इन्फरन्सला वेग देते, ज्यात PyTorch, TensorFlow, ONNX आणि इतर लोकप्रिय फ्रेमवर्क्समधील मॉडेल्सचा समावेश आहे. मॉडेल्सचे रूपांतर करा आणि ऑप्टिमाइझ करा, आणि Intel® हार्डवेअर आणि विविध वातावरणांमध्ये, ऑन-प्रिमायसेस, डिव्हाइसवर, ब्राउझरमध्ये किंवा क्लाउडमध्ये तैनात करा.

आता OpenVINO वापरून, तुम्ही Intel हार्डवेअरवर GenAI मॉडेल जलद क्वांटायझ करू शकता आणि मॉडेल संदर्भ वेगाने चालवू शकता.

आता OpenVINO Phi-3.5-Vision आणि Phi-3.5 Instruct च्या क्वांटायझेशन रूपांतरणाला समर्थन देते.

### **पर्यावरण सेटअप**

कृपया खालील पर्यावरण अवलंबित्वे स्थापित असल्याची खात्री करा, हे requirement.txt आहे

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO वापरून Phi-3.5-Instruct चे क्वांटायझेशन**

टर्मिनलमध्ये, कृपया हा स्क्रिप्ट चालवा

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO वापरून Phi-3.5-Vision चे क्वांटायझेशन**

कृपया Python किंवा Jupyter lab मध्ये हा स्क्रिप्ट चालवा

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

### **🤖 Intel OpenVINO सह Phi-3.5 साठी नमुने**

| Labs    | परिचय | जा |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | तुमच्या AI PC मध्ये Phi-3.5 Instruct कसा वापरायचा ते शिका    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | तुमच्या AI PC मध्ये प्रतिमा विश्लेषणासाठी Phi-3.5 Vision कसा वापरायचा ते शिका      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | तुमच्या AI PC मध्ये व्हिडिओ विश्लेषणासाठी Phi-3.5 Vision कसा वापरायचा ते शिका    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **संसाधने**

1. Intel OpenVINO बद्दल अधिक जाणून घ्या [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.