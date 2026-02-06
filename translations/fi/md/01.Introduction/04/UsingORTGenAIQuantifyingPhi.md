## **Kuinka käyttää Model Builderia Phi-3.5:n kvantisointiin**

Model Builder tukee nyt ONNX-mallien kvantisointia Phi-3.5 Instruct- ja Phi-3.5-Vision-malleille.

### **Phi-3.5-Instruct**

**CPU-kiihdytetty kvantisoitu INT4-muunnos**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-kiihdytetty kvantisoitu INT4-muunnos**

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

3. Lataa nämä tiedostot Phi-3.5-vision-instruct -kansioosi

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Lataa tämä tiedosto models-kansioon  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Siirry terminaaliin

    Muunna ONNX-tuki FP32-muotoon

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Huomio:**

1. Model Builder tukee tällä hetkellä Phi-3.5-Instruct- ja Phi-3.5-Vision-mallien muunnosta, mutta ei Phi-3.5-MoE-mallia.

2. ONNX:n kvantisoitua mallia voi käyttää Generative AI extensions for onnxruntime -SDK:n kautta.

3. Vastuullisemman tekoälyn vuoksi mallin kvantisoinnin jälkeen suositellaan tehokkaampaa tulosten testausta.

4. Kvantisoimalla CPU INT4 -mallin voimme ottaa sen käyttöön reunalaitteissa, joissa on paremmat sovellusmahdollisuudet, joten Phi-3.5-Instruct on saatu valmiiksi INT4-tasolla.

## **Resurssit**

1. Lisätietoja Generative AI extensions for onnxruntime -laajennuksesta: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub-repositorio: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.