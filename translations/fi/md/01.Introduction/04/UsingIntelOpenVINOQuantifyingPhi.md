<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:02:28+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "fi"
}
-->
# **Phi-3.5:n kvantisointi Intel OpenVINO:lla**

Intel on perinteisin suorittimien valmistaja, jolla on paljon käyttäjiä. Koneoppimisen ja syväoppimisen nousun myötä Intel on myös liittynyt tekoälyn kiihdytyskilpailuun. Mallin päättelyssä Intel käyttää paitsi GPU:ita ja CPU:ita, myös NPU:ita.

Toivomme voivamme ottaa Phi-3.x -perheen käyttöön loppukäyttäjän laitteissa, pyrkien siitä tekoäly-PC:n ja Copilot-PC:n tärkein osa. Mallin lataaminen loppukäyttäjän laitteella riippuu eri laitevalmistajien yhteistyöstä. Tässä luvussa keskitytään pääasiassa Intel OpenVINO:n käyttötilanteeseen kvantitatiivisena mallina.


## **Mikä on OpenVINO**

OpenVINO on avoimen lähdekoodin työkalu syväoppimismallien optimointiin ja käyttöönottoon pilvestä reunalaitteisiin. Se nopeuttaa syväoppimisen päättelyä monissa käyttötapauksissa, kuten generatiivisessa tekoälyssä, videoissa, äänissä ja kielissä, hyödyntäen suosittuja kehyksiä kuten PyTorch, TensorFlow, ONNX ja muita. Muunna ja optimoi malleja, ja ota ne käyttöön erilaisissa Intel®-laitteissa ja ympäristöissä, paikallisesti tai laitteella, selaimessa tai pilvessä.

Nyt OpenVINO:n avulla voit nopeasti kvantisoida GenAI-mallin Intel-laitteistolla ja nopeuttaa mallin referenssiä.

OpenVINO tukee nyt Phi-3.5-Vision ja Phi-3.5 Instruct -mallien kvantisointimuunnosta.

### **Ympäristön asennus**

Varmista, että seuraavat ympäristöriippuvuudet on asennettu, tämä on requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Phi-3.5-Instructin kvantisointi OpenVINO:lla**

Aja tämä skripti terminaalissa

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Phi-3.5-Vision kvantisointi OpenVINO:lla**

Aja tämä skripti Pythonissa tai Jupyter labissa

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

### **🤖 Phi-3.5:n esimerkit Intel OpenVINO:lla**

| Labit    | Esittely | Siirry |
| -------- | ------- |  ------- |
| 🚀 Lab-esittely Phi-3.5 Instruct  | Opi käyttämään Phi-3.5 Instructia tekoäly-PC:ssäsi    |  [Siirry](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-esittely Phi-3.5 Vision (kuva) | Opi käyttämään Phi-3.5 Visionia kuvien analysointiin tekoäly-PC:ssäsi      |  [Siirry](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-esittely Phi-3.5 Vision (video)   | Opi käyttämään Phi-3.5 Visionia videoiden analysointiin tekoäly-PC:ssäsi    |  [Siirry](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **Resurssit**

1. Lisätietoja Intel OpenVINO:sta [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.