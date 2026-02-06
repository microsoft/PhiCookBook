# **Phi-perheen kvantisointi käyttäen llama.cpp:tä**

## **Mikä on llama.cpp**

llama.cpp on avoimen lähdekoodin ohjelmistokirjasto, joka on pääasiassa kirjoitettu C++:lla ja suorittaa päättelyä erilaisilla suurilla kielimalleilla (LLM), kuten Llama. Sen päätavoitteena on tarjota huipputason suorituskyky LLM-päättelyyn laajalla valikoimalla laitteistoja mahdollisimman vähäisellä asennuksella. Lisäksi tälle kirjastolle on saatavilla Python-kirjasto, joka tarjoaa korkean tason API:n tekstin täydentämiseen sekä OpenAI-yhteensopivan web-palvelimen.

llama.cpp:n päätavoite on mahdollistaa LLM-päättely vähäisellä asennuksella ja huipputason suorituskyvyllä monenlaisilla laitteistoilla – paikallisesti ja pilvessä.

- Pelkkä C/C++-toteutus ilman riippuvuuksia
- Apple Silicon on ensiluokkainen tuki – optimoitu ARM NEONin, Acceleraten ja Metal-kehysten avulla
- AVX, AVX2 ja AVX512 -tuki x86-arkkitehtuureille
- 1,5-bittinen, 2-bittinen, 3-bittinen, 4-bittinen, 5-bittinen, 6-bittinen ja 8-bittinen kokonaislukukvantisointi nopeampaan päättelyyn ja pienempään muistinkäyttöön
- Räätälöidyt CUDA-ytimet LLM-mallien ajamiseen NVIDIA-GPU:illa (AMD-GPU-tuki HIPin kautta)
- Vulkan- ja SYCL-taustatuki
- CPU+GPU-hybridi-päättely osittaiseen nopeutukseen malleille, jotka ovat suurempia kuin käytettävissä oleva VRAM

## **Phi-3.5 kvantisointi llama.cpp:llä**

Phi-3.5-Instruct-malli voidaan kvantisoida käyttäen llama.cpp:tä, mutta Phi-3.5-Vision ja Phi-3.5-MoE eivät ole vielä tuettuja. llama.cpp muuntaa mallin gguf-muotoon, joka on myös yleisimmin käytetty kvantisointimuoto.

Hugging Face -palvelussa on suuri määrä kvantisoituja GGUF-muotoisia malleja. AI Foundry, Ollama ja LlamaEdge käyttävät llama.cpp:tä, joten GGUF-malleja käytetään usein myös heidän yhteydessä.

### **Mikä on GGUF**

GGUF on binäärimuoto, joka on optimoitu mallien nopeaan lataamiseen ja tallentamiseen, tehden siitä erittäin tehokkaan päättelyä varten. GGUF on suunniteltu käytettäväksi GGML:n ja muiden suorittimien kanssa. GGUF:n on kehittänyt @ggerganov, joka on myös llama.cpp:n kehittäjä, suosittu C/C++ LLM-päättelykehys. Alun perin PyTorchin kaltaisissa kehyksissä kehitetyt mallit voidaan muuntaa GGUF-muotoon käytettäväksi näissä moottoreissa.

### **ONNX vs GGUF**

ONNX on perinteinen koneoppimisen/syväoppimisen formaatti, jota tuetaan hyvin eri tekoälykehyksissä ja jolla on hyvät käyttötarkoitukset reunalaitteissa. GGUF puolestaan perustuu llama.cpp:hen ja voidaan sanoa, että se on syntynyt GenAI-aikakaudella. Molemmilla on samankaltaisia käyttötarkoituksia. Jos haluat paremman suorituskyvyn sulautetussa laitteistossa ja sovelluskerroksissa, ONNX voi olla valintasi. Jos käytät llama.cpp:n johdannaista kehystä ja teknologiaa, GGUF voi olla parempi vaihtoehto.

### **Phi-3.5-Instructin kvantisointi käyttäen llama.cpp:tä**

**1. Ympäristön konfigurointi**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantisointi**

Käyttämällä llama.cpp:tä muunna Phi-3.5-Instruct FP16 GGUF -muotoon


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 kvantisointi INT4-muotoon


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testaus**

Asenna llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Huom*** 

Jos käytät Apple Siliconia, asenna llama-cpp-python näin


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testaus


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resurssit**

1. Lisätietoja llama.cpp:stä [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Lisätietoja onnxruntimesta [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Lisätietoja GGUF:stä [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.