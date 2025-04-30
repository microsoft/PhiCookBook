<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f766ec7e68d97f6009b58794b471d66",
  "translation_date": "2025-04-04T17:58:26+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "hi"
}
-->
# **Intel OpenVINO का उपयोग करके Phi-3.5 को क्वांटाइज करना**

Intel सबसे पारंपरिक CPU निर्माता है जिसके कई उपयोगकर्ता हैं। मशीन लर्निंग और डीप लर्निंग के बढ़ते प्रभाव के साथ, Intel ने भी AI एक्सेलेरेशन की दौड़ में भाग लिया है। मॉडल इन्फेरेंस के लिए, Intel न केवल GPUs और CPUs का उपयोग करता है, बल्कि NPUs का भी उपयोग करता है।

हम Phi-3.x फैमिली को एंड साइड पर तैनात करने की उम्मीद करते हैं, ताकि AI PC और Copilot PC का सबसे महत्वपूर्ण हिस्सा बन सकें। एंड साइड पर मॉडल को लोड करना विभिन्न हार्डवेयर निर्माताओं के सहयोग पर निर्भर करता है। यह अध्याय मुख्य रूप से Intel OpenVINO के एक क्वांटिटेटिव मॉडल के उपयोग पर केंद्रित है।

## **OpenVINO क्या है**

OpenVINO एक ओपन-सोर्स टूलकिट है जो क्लाउड से एज तक डीप लर्निंग मॉडल को ऑप्टिमाइज़ और डिप्लॉय करने के लिए उपयोग किया जाता है। यह विभिन्न उपयोग मामलों में डीप लर्निंग इन्फेरेंस को तेज करता है, जैसे जनरेटिव AI, वीडियो, ऑडियो, और भाषा, और यह PyTorch, TensorFlow, ONNX जैसे लोकप्रिय फ्रेमवर्क के मॉडलों के साथ काम करता है। मॉडलों को कन्वर्ट और ऑप्टिमाइज़ करें और Intel® हार्डवेयर और वातावरण के मिश्रण पर, ऑन-प्रिमाइसेस और ऑन-डिवाइस, ब्राउज़र या क्लाउड में डिप्लॉय करें।

अब OpenVINO के साथ, आप Intel हार्डवेयर में GenAI मॉडल को तेजी से क्वांटाइज कर सकते हैं और मॉडल संदर्भ को तेज कर सकते हैं।

अब OpenVINO Phi-3.5-Vision और Phi-3.5 Instruct के क्वांटाइजेशन कन्वर्ज़न को सपोर्ट करता है।

### **एनवायरनमेंट सेटअप**

कृपया सुनिश्चित करें कि निम्नलिखित एनवायरनमेंट डिपेंडेंसीज़ इंस्टॉल की गई हैं। यह `requirement.txt` है:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO का उपयोग करके Phi-3.5-Instruct को क्वांटाइज करना**

टर्मिनल में, कृपया इस स्क्रिप्ट को चलाएँ:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO का उपयोग करके Phi-3.5-Vision को क्वांटाइज करना**

कृपया इस स्क्रिप्ट को Python या Jupyter लैब में चलाएँ:

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

### **🤖 Intel OpenVINO के साथ Phi-3.5 के सैंपल्स**

| लैब्स    | परिचय | लिंक |
| -------- | ------- |  ------- |
| 🚀 लैब-परिचय Phi-3.5 Instruct  | जानें कि अपने AI PC में Phi-3.5 Instruct का उपयोग कैसे करें    |  [लिंक](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 लैब-परिचय Phi-3.5 Vision (इमेज) | जानें कि अपने AI PC में Phi-3.5 Vision का उपयोग करके इमेज का विश्लेषण कैसे करें      |  [लिंक](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 लैब-परिचय Phi-3.5 Vision (वीडियो)   | जानें कि अपने AI PC में Phi-3.5 Vision का उपयोग करके वीडियो का विश्लेषण कैसे करें    |  [लिंक](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **संसाधन**

1. Intel OpenVINO के बारे में अधिक जानें [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub रिपॉज़िटरी [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता बनाए रखने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।