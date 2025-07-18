<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:00:40+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ne"
}
-->
# **Intel OpenVINO प्रयोग गरी Phi-3.5 को क्वान्टाइजेशन**

Intel सबैभन्दा परम्परागत CPU निर्माता हो जसका धेरै प्रयोगकर्ता छन्। मेसिन लर्निङ र डीप लर्निङको उदयसँगै, Intel ले पनि AI एक्सेलेरेशनको प्रतिस्पर्धामा भाग लिएको छ। मोडेल इन्फरेन्सका लागि Intel ले GPU र CPU मात्र होइन, NPU पनि प्रयोग गर्छ।

हामी Phi-3.x परिवारलाई अन्तिम पक्षमा डिप्लोय गर्न चाहन्छौं, जसले AI PC र Copilot PC को सबैभन्दा महत्वपूर्ण भाग बन्ने आशा राख्छ। अन्तिम पक्षमा मोडेल लोडिङ विभिन्न हार्डवेयर निर्माताहरूको सहकार्यमा निर्भर गर्दछ। यो अध्याय मुख्य रूपमा Intel OpenVINO को क्वान्टिटेटिभ मोडेलको प्रयोग परिदृश्यमा केन्द्रित छ।

## **OpenVINO के हो**

OpenVINO एक खुला स्रोत उपकरण हो जसले क्लाउडदेखि एजसम्म डीप लर्निङ मोडेलहरूलाई अनुकूलन र डिप्लोय गर्न मद्दत गर्छ। यसले विभिन्न प्रयोग केसहरूमा डीप लर्निङ इन्फरेन्सलाई छिटो बनाउँछ, जस्तै जेनेरेटिभ AI, भिडियो, अडियो, र भाषा, लोकप्रिय फ्रेमवर्कहरू जस्तै PyTorch, TensorFlow, ONNX बाट मोडेलहरूसँग। मोडेलहरूलाई रूपान्तरण र अनुकूलन गरी Intel® हार्डवेयर र वातावरणहरूमा, अन-प्रिमाइस र डिभाइसमा, ब्राउजर वा क्लाउडमा डिप्लोय गर्न सकिन्छ।

अब OpenVINO सँग, तपाईं Intel हार्डवेयरमा छिटो GenAI मोडेल क्वान्टाइज गर्न र मोडेल रेफरेन्सलाई छिटो बनाउन सक्नुहुन्छ।

अहिले OpenVINO ले Phi-3.5-Vision र Phi-3.5 Instruct को क्वान्टाइजेशन रूपान्तरणलाई समर्थन गर्दछ।

### **पर्यावरण सेटअप**

कृपया तलका वातावरण निर्भरताहरू इन्स्टल गरिएको छ भनी सुनिश्चित गर्नुहोस्, यो requirement.txt हो

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO प्रयोग गरी Phi-3.5-Instruct को क्वान्टाइजेशन**

Terminal मा, कृपया यो स्क्रिप्ट चलाउनुहोस्

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO प्रयोग गरी Phi-3.5-Vision को क्वान्टाइजेशन**

Python वा Jupyter lab मा यो स्क्रिप्ट चलाउनुहोस्

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

### **🤖 Intel OpenVINO सँग Phi-3.5 का नमूनाहरू**

| Labs    | परिचय | जानुहोस् |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | तपाईंको AI PC मा Phi-3.5 Instruct कसरी प्रयोग गर्ने सिक्नुहोस्    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | तपाईंको AI PC मा Phi-3.5 Vision प्रयोग गरी तस्बिर विश्लेषण कसरी गर्ने सिक्नुहोस्      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | तपाईंको AI PC मा Phi-3.5 Vision प्रयोग गरी भिडियो विश्लेषण कसरी गर्ने सिक्नुहोस्    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **स्रोतहरू**

1. Intel OpenVINO बारे थप जान्न [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भने पनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।