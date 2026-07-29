# **Phi-perheen kvantisointi Generative AI -laajennuksilla onnxruntimelle**

## **Mitä ovat Generative AI -laajennukset onnxruntimelle**

Nämä laajennukset auttavat sinua suorittamaan generatiivista tekoälyä ONNX Runtime -ympäristössä ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Se tarjoaa generatiivisen tekoälyn silmukan ONNX-malleille, sisältäen päättelyn ONNX Runtimella, logitien käsittelyn, haun ja otannan sekä KV-välimuistin hallinnan. Kehittäjät voivat kutsua korkeantason generate()-metodia tai suorittaa mallin jokaisen iteraation silmukassa, generoi yhden tokenin kerrallaan ja tarvittaessa päivittää generoinnin parametreja silmukan sisällä. Se tukee ahnettua/beam-hakua ja TopP-, TopK-otantaa token-sekvenssien luomiseksi sekä sisäänrakennettua logitien käsittelyä, kuten toistoseuraamuksia. Voit myös helposti lisätä oman pisteytyksen.

Sovellustasolla voit käyttää Generative AI -laajennuksia onnxruntimelle rakentamaan sovelluksia C++/ C# / Python -kielillä. Mallitasolla voit käyttää sitä hienosäädettyjen mallien yhdistämiseen ja niihin liittyviin kvantitatiivisiin käyttöönottoihin.


## **Phi-3.5:n kvantisointi Generative AI -laajennuksilla onnxruntimelle**

### **Tuetut mallit**

Generative AI -laajennukset onnxruntimelle tukevat Microsoft Phin, Google Gemman, Mistralin ja Meta LLaMAn kvantisointimuunnoksia.


### **Mallinrakentaja Generative AI -laajennuksissa onnxruntimelle**

Mallinrakentaja nopeuttaa merkittävästi optimoitujen ja kvantisoitujen ONNX-mallien luontia, jotka toimivat ONNX Runtime generate() -rajapinnan kanssa.

Mallinrakentajan kautta voit kvantisoida mallin INT4, INT8, FP16, FP32 -muotoihin ja yhdistää erilaisia laitteistokiihdytysmenetelmiä kuten CPU, CUDA, DirectML, Mobile jne.

Mallinrakentajan käyttöä varten sinun tulee asentaa

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Asennuksen jälkeen voit suorittaa Mallinrakentajan skriptin terminaalista mallin formaatin ja kvantisoinnin muunnosten tekemistä varten.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Ymmärrä asiaankuuluvat parametrit

1. **model_name** Tämä on malli Hugging Face-palvelussa, kuten microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct jne. Se voi myös olla polku, johon tallennat mallin

2. **path_to_output_folder** Kvantisoidun muunnoksen tallennuspolku

3. **execution_provider** Erilainen laitteistokiihdytystuki, kuten cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Lataamme mallin Hugging Face:stä ja tallennamme sen väliaikaisesti paikallisesti




***Huomio：*** <ul>Vaikka Generative AI -laajennukset onnxruntimelle ovat vielä esikatseluvaiheessa, ne on sisällytetty Microsoft Oliveen, ja voit myös kutsua Generative AI -laajennusten Model Builder -toimintoja Microsoft Oliven kautta.</ul>

## **Kuinka käyttää Mallinrakentajaa Phi-3.5:n kvantisointiin**

Mallinrakentaja tukee nyt ONNX-mallien kvantisointia Phi-3.5 Instruct- ja Phi-3.5-Vision -malleille

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

3. Lataa nämä tiedostot Phi-3.5-vision-instruct -kansioosi

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Lataa tämä tiedosto models-kansioon
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Mene terminaaliin

    Muunna ONNX-tuki FP32:lla


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Huomio：**

1. Mallinrakentaja tukee nykyisin Phi-3.5-Instructin ja Phi-3.5-Visionin muunnoksia, mutta ei Phi-3.5-MoE:ta

2. Käyttääksesi ONNX:n kvantisoitua mallia, voit käyttää sitä Generative AI -laajennusten onnxruntime SDK:n kautta

3. Meidän tulee ottaa vastuullisempi tekoäly huomioon, joten mallin kvantisointi-muuntojen jälkeen on suositeltavaa tehdä tehokkaampaa tulostestausta

4. Kvantisoimalla CPU INT4-malli voimme ottaa sen käyttöön Edge-laitteissa, joissa on paremmat sovellusmahdollisuudet, joten olemme saaneet Phi-3.5-Instructin valmiiksi INT4:n osalta


## **Resurssit**

1. Lisätietoa Generative AI -laajennuksista onnxruntimelle [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI -laajennusten onnxruntime GitHub-repositorio [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->