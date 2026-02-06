# **Kukokotoa Phi-3.5 kwa kutumia Intel OpenVINO**

Intel ni mtengenezaji wa CPU wa jadi zaidi na wenye watumiaji wengi. Pamoja na kuibuka kwa ujifunzaji wa mashine na ujifunzaji wa kina, Intel pia imejiunga na ushindani wa kuharakisha AI. Kwa ajili ya utambuzi wa modeli, Intel haitumii tu GPU na CPU, bali pia hutumia NPU.

Tunatarajia kuweka Familia ya Phi-3.x upande wa mwisho, tukitumaini kuwa sehemu muhimu zaidi ya AI PC na Copilot PC. Kupakia modeli upande wa mwisho kunategemea ushirikiano wa watengenezaji mbalimbali wa vifaa. Sura hii inazingatia zaidi matumizi ya Intel OpenVINO kama modeli ya kiasi.

## **OpenVINO ni Nini**

OpenVINO ni kifaa cha chanzo huria kwa ajili ya kuboresha na kuweka modeli za ujifunzaji wa kina kutoka wingu hadi mwisho wa mtandao. Kina harakisha utambuzi wa ujifunzaji wa kina katika matumizi mbalimbali, kama AI ya kizazi, video, sauti, na lugha kwa kutumia modeli kutoka kwa mifumo maarufu kama PyTorch, TensorFlow, ONNX, na mingine. Badilisha na boresha modeli, na ziweke kwenye mchanganyiko wa vifaa na mazingira ya Intel®, ndani ya ofisi au kifaa, kwenye kivinjari au wingu.

Sasa kwa OpenVINO, unaweza haraka kukokotoa modeli ya GenAI kwenye vifaa vya Intel na kuharakisha marejeleo ya modeli.

Sasa OpenVINO inaunga mkono mabadiliko ya kukokotoa ya Phi-3.5-Vision na Phi-3.5 Instruct

### **Kuweka Mazingira**

Tafadhali hakikisha utegemezi wa mazingira yafuatayo yamewekwa, hii ni requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kukokotoa Phi-3.5-Instruct kwa kutumia OpenVINO**

Katika Terminal, tafadhali endesha script hii

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kukokotoa Phi-3.5-Vision kwa kutumia OpenVINO**

Tafadhali endesha script hii katika Python au Jupyter lab

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

### **🤖 Sampuli za Phi-3.5 na Intel OpenVINO**

| Maabara    | Utangulizi | Nenda |
| -------- | ------- |  ------- |
| 🚀 Maabara-Utangulizi Phi-3.5 Instruct  | Jifunze jinsi ya kutumia Phi-3.5 Instruct kwenye AI PC yako    |  [Nenda](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Maabara-Utangulizi Phi-3.5 Vision (picha) | Jifunze jinsi ya kutumia Phi-3.5 Vision kuchambua picha kwenye AI PC yako      |  [Nenda](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Maabara-Utangulizi Phi-3.5 Vision (video)   | Jifunze jinsi ya kutumia Phi-3.5 Vision kuchambua video kwenye AI PC yako    |  [Nenda](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Rasilimali**

1. Jifunze zaidi kuhusu Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.