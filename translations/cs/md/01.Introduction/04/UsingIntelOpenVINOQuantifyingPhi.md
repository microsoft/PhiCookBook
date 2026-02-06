# **Kvantilace Phi-3.5 pomocí Intel OpenVINO**

Intel je nejtradičnější výrobce CPU s mnoha uživateli. S nástupem strojového učení a hlubokého učení se Intel také zapojil do soutěže o akceleraci AI. Pro inferenci modelů Intel využívá nejen GPU a CPU, ale také NPU.

Doufáme, že nasadíme rodinu Phi-3.x na koncovou stranu, s cílem stát se nejdůležitější součástí AI PC a Copilot PC. Načítání modelu na koncovém zařízení závisí na spolupráci různých výrobců hardwaru. Tato kapitola se zaměřuje především na aplikační scénář Intel OpenVINO jako kvantitativního modelu.

## **Co je OpenVINO**

OpenVINO je open-source sada nástrojů pro optimalizaci a nasazení modelů hlubokého učení od cloudu až po edge. Urychluje inferenci hlubokého učení v různých případech použití, jako je generativní AI, video, audio a jazyk, s modely z populárních frameworků jako PyTorch, TensorFlow, ONNX a dalších. Převádí a optimalizuje modely a nasazuje je na různorodý Intel® hardware a prostředí, lokálně i na zařízení, v prohlížeči nebo v cloudu.

S OpenVINO nyní můžete rychle kvantizovat GenAI model na Intel hardwaru a zrychlit referenční model.

OpenVINO nyní podporuje kvantizační převod Phi-3.5-Vision a Phi-3.5 Instruct.

### **Nastavení prostředí**

Ujistěte se, že máte nainstalované následující závislosti, jedná se o requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantilace Phi-3.5-Instruct pomocí OpenVINO**

V terminálu spusťte tento skript

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantilace Phi-3.5-Vision pomocí OpenVINO**

Spusťte tento skript v Pythonu nebo Jupyter labu

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

### **🤖 Ukázky pro Phi-3.5 s Intel OpenVINO**

| Laboratoře    | Popis | Jít |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučte se, jak používat Phi-3.5 Instruct ve vašem AI PC    |  [Jít](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (obrázek) | Naučte se, jak používat Phi-3.5 Vision k analýze obrázků ve vašem AI PC      |  [Jít](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Naučte se, jak používat Phi-3.5 Vision k analýze videa ve vašem AI PC    |  [Jít](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Zdroje**

1. Více o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.