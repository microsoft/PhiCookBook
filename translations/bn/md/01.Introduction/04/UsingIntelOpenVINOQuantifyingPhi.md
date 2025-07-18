<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:00:21+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "bn"
}
-->
# **Intel OpenVINO ব্যবহার করে Phi-3.5 কোয়ান্টাইজেশন**

Intel হল সবচেয়ে প্রচলিত CPU নির্মাতা যার অনেক ব্যবহারকারী রয়েছে। মেশিন লার্নিং এবং ডিপ লার্নিংয়ের উত্থানের সাথে, Intel AI ত্বরান্বিত করার প্রতিযোগিতায় যোগ দিয়েছে। মডেল ইনফারেন্সের জন্য, Intel শুধুমাত্র GPU এবং CPU ব্যবহার করে না, বরং NPU ও ব্যবহার করে।

আমরা আশা করি Phi-3.x পরিবারকে এন্ড ডিভাইসে ডিপ্লয় করতে, যা AI PC এবং Copilot PC এর সবচেয়ে গুরুত্বপূর্ণ অংশ হয়ে উঠবে। এন্ড ডিভাইসে মডেল লোডিং বিভিন্ন হার্ডওয়্যার নির্মাতাদের সহযোগিতার উপর নির্ভর করে। এই অধ্যায়টি মূলত Intel OpenVINO কে কোয়ান্টিটেটিভ মডেল হিসেবে ব্যবহারের প্রেক্ষাপটে ফোকাস করে।

## **OpenVINO কী?**

OpenVINO হল একটি ওপেন-সোর্স টুলকিট যা ক্লাউড থেকে এজ পর্যন্ত ডিপ লার্নিং মডেল অপ্টিমাইজ এবং ডিপ্লয় করার জন্য ব্যবহৃত হয়। এটি বিভিন্ন ব্যবহারের ক্ষেত্রে ডিপ লার্নিং ইনফারেন্স দ্রুততর করে, যেমন জেনারেটিভ AI, ভিডিও, অডিও, এবং ভাষা, জনপ্রিয় ফ্রেমওয়ার্ক যেমন PyTorch, TensorFlow, ONNX ইত্যাদি থেকে মডেল নিয়ে। মডেল রূপান্তর এবং অপ্টিমাইজ করে, Intel® হার্ডওয়্যার এবং পরিবেশের মিশ্রণে, অন-প্রিমাইস এবং অন-ডিভাইসে, ব্রাউজার বা ক্লাউডে ডিপ্লয় করা যায়।

এখন OpenVINO দিয়ে, আপনি দ্রুত Intel হার্ডওয়্যারে GenAI মডেল কোয়ান্টাইজ করতে পারবেন এবং মডেল রেফারেন্স দ্রুততর করতে পারবেন।

এখন OpenVINO Phi-3.5-Vision এবং Phi-3.5 Instruct এর কোয়ান্টাইজেশন রূপান্তর সমর্থন করে।

### **পরিবেশ সেটআপ**

নিশ্চিত করুন নিচের পরিবেশ নির্ভরশীলতাগুলো ইনস্টল করা আছে, এটি requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO ব্যবহার করে Phi-3.5-Instruct কোয়ান্টাইজেশন**

টার্মিনালে নিচের স্ক্রিপ্টটি চালান

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO ব্যবহার করে Phi-3.5-Vision কোয়ান্টাইজেশন**

Python বা Jupyter lab এ নিচের স্ক্রিপ্টটি চালান

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

### **🤖 Intel OpenVINO সহ Phi-3.5 এর নমুনা**

| ল্যাবস    | পরিচিতি | যান |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | আপনার AI PC তে Phi-3.5 Instruct কীভাবে ব্যবহার করবেন শিখুন    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | আপনার AI PC তে Phi-3.5 Vision ব্যবহার করে ছবি বিশ্লেষণ করার পদ্ধতি শিখুন      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | আপনার AI PC তে Phi-3.5 Vision ব্যবহার করে ভিডিও বিশ্লেষণ করার পদ্ধতি শিখুন    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **রিসোর্সসমূহ**

1. Intel OpenVINO সম্পর্কে আরও জানুন [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub রিপোজিটরি [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।