# **ការបង្កើតទម្រង់ Quantized របស់ Phi-3.5 ដោយប្រើ Intel OpenVINO**

Intel គឺជា​ក្រុមហ៊ុនផលិត CPU ដែលមានប្រវត្តិបុរាណ និងមានអ្នកប្រើជាច្រើន។ ជាមួយនឹងការរីកចម្រើននៃ machine learning និង deep learning ក៏ដូចជា Intel បានចូលរួមប្រកួតប្រជែងក្នុងការបង្កើនល្បឿនសម្រាប់ AI ផងដែរ។ សម្រាប់ការបញ្ចេញលទ្ធផលម៉ូដែល (model inference) Intel មិនបានប្រើតែ GPUs និង CPUs ប៉ុណ្ណោះទេ ប៉ុន្តែថែមទាំងប្រើ NPUs ផងដែរ។

យើងបង្ហាញបំណងចង់ចែកចាយ Phi-3.x Family នៅផ្នែកចុងឧបករណ៍ (end side) ដើម្បីក្លាយជា​ផ្នែកសំខាន់បំផុតនៃ AI PC និង Copilot PC។ ការផ្ទុកម៉ូដែលនៅផ្នែកចុងឧបករណ៍ត្រូវការការសហការពីក្រុមហ៊ុនផលិតឧបករណ៍ផ្សេងៗគ្នា។ ជំពូកនេះផ្តោតសំខាន់លើស្ថានភាពប្រើប្រាស់ Intel OpenVINO ជាសម្រាប់ម៉ូដែលដែលបានបម្លែងជា Quantized។

## **OpenVINO ជាអ្វី**

OpenVINO គឺជាគ្រឿងឧបករណ៍បើកប្រភពសម្រាប់បង្កើនប្រសិទ្ធភាព និងចែកចាយម៉ូដែល deep learning ចាប់ពី cloud ដល់ edge។ វាសមហេតុឱ្យការបញ្ចេញលទ្ធផល deep learning លឿនឡើងក្នុងករណីប្រើប្រាស់ជាច្រើន ដូចជា generative AI, វីដេអូ, សំឡេង និងភាសា ដោយគាំទ្រម៉ូដែលពី framework ទូទៅដូចជា PyTorch, TensorFlow, ONNX និងផ្សេងទៀត។ អ្នកអាចបម្លែង និងអុបទីម៉ៃស៍ម៉ូដែល ហើយចែកចាយលើឧបករណ៍ Intel® និងបរិយាកាសផ្សេងៗ ទាំងនៅលើ premise និងលើឧបករណ៍, ក្នុងកម្មវិធីរុករកឬក្នុង cloud។

ឥឡូវនេះជាមួយ OpenVINO អ្នកអាចធ្វើការបម្លែងជា quantize សម្រាប់ម៉ូដែល GenAI លើឧបករណ៍ Intel បានយ៉ាងលឿន និងបង្កើនល្បឿនយោងម៉ូដែល។

ឥឡូវនេះ OpenVINO គាំទ្រការបម្លែង quantization របស់ Phi-3.5-Vision និង Phi-3.5 Instruct

### **ការ​រៀបចំ​បរិយាកាស**

សូមប្រាកដថាការពឹងផ្អែកបរិយាកាសដូចខាងក្រោមត្រូវបានដំឡើង នេះជារាយនាម requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **ការបង្កើតទម្រង់ Quantized របស់ Phi-3.5-Instruct ដោយប្រើ OpenVINO**

នៅក្នុង Terminal សូមរត់ស្គ្រីបនេះ


```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **ការបង្កើតទម្រង់ Quantized របស់ Phi-3.5-Vision ដោយប្រើ OpenVINO**

សូមរត់ស្គ្រីបនេះក្នុង Python ឬ Jupyter lab

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

### **🤖 ឧទាហរណ៍សម្រាប់ Phi-3.5 ជាមួយ Intel OpenVINO**

| Labs    | Introduce | Go |
| -------- | ------- |  ------- |
| 🚀 លាប-ណែនាំ Phi-3.5 Instruct  | រៀនពីវិធីប្រើ Phi-3.5 Instruct លើ AI PC របស់អ្នក    |  [ចូល](../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 លាប-ណែនាំ Phi-3.5 Vision (រូបភាព) | រៀនពីវិធីប្រើ Phi-3.5 Vision ដើម្បីវិភាគរូបភាពលើ AI PC របស់អ្នក      |  [ចូល](../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 លាប-ណែនាំ Phi-3.5 Vision (វីដេអូ)   | រៀនពីវិធីប្រើ Phi-3.5 Vision ដើម្បីវិភាគវីដេអូលើ AI PC របស់អ្នក    |  [ចូល](../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **ធនធាន**

1. រៀនបន្ថែមអំពី Intel OpenVINO https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html

2. Intel OpenVINO GitHub Repo https://github.com/openvinotoolkit/openvino.genai

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារ​នេះ​ត្រូវបាន​បកប្រែ​ដោយ​ប្រើ​សេវាកម្ម​បកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបី​យើងខិតខំ​ស្វែងរកភាព​ត្រឹមត្រូវក៏ដោយ សូមយកចិត្តទុកដាក់ថា ការបកប្រែ​ដោយស្វ័យប្រវត្តិ​អាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារ​ដើម​នៅក្នុង​ភាសា​ដើម គួរត្រូវបានចាត់ទុកថាជា​ប្រភពដែលអាចទុកចិត្តបាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរអោយប្រើការបកប្រែ​ដោយមនុស្ស​ជាអ្នកជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសៗណាមួយ ដែលកើតមាន​ពីការប្រើប្រាស់​ការ​បកប្រែ​នេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->