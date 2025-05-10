<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:36:47+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "fi"
}
-->
## **Kuinka käyttää Model Builderia Phi-3.5:n kvantisointiin**

Model Builder tukee nyt ONNX-mallien kvantisointia Phi-3.5 Instruct- ja Phi-3.5-Vision-malleille.

### **Phi-3.5-Instruct**

**CPU-kiihdytetty INT4-kvantisointimuunnos**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-kiihdytetty INT4-kvantisointimuunnos**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Aseta ympäristö terminaalissa

```bash

mkdir models

cd models 

```

2. Lataa microsoft/Phi-3.5-vision-instruct models-kansioon  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Lataa nämä tiedostot omaan Phi-3.5-vision-instruct -kansioosi

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Lataa tämä tiedosto models-kansioon  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Siirry terminaaliin

    Muunna ONNX-malli tukemaan FP32:ta

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Huomioita:**

1. Model Builder tukee tällä hetkellä Phi-3.5-Instruct- ja Phi-3.5-Vision-mallien muunnosta, mutta ei Phi-3.5-MoE:ta.

2. ONNX:n kvantisoitua mallia voi käyttää Generative AI extensions for onnxruntime SDK:n kautta.

3. Otetaan vastuullinen AI huomioon – mallin kvantisoinnin jälkeen suositellaan kattavampia tulostestejä.

4. Kvantisoimalla CPU:n INT4-mallin voimme ottaa sen käyttöön reunalaitteissa, joissa on paremmat sovelluskohteet. Tämän vuoksi olemme saattaneet Phi-3.5-Instructin INT4-tasolle.

## **Resurssit**

1. Lisätietoja Generative AI extensions for onnxruntime -laajennuksesta: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub-repositorio: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai tulkinnoista.