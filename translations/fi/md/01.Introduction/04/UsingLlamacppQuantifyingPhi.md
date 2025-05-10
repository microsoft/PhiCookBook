<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:12:58+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "fi"
}
-->
# **Phi-perheen kvantisointi käyttäen llama.cpp:tä**

## **Mikä on llama.cpp**

llama.cpp on avoimen lähdekoodin ohjelmistokirjasto, joka on pääosin kirjoitettu C++:lla ja suorittaa päättelyä erilaisilla suurilla kielimalleilla (LLM), kuten Llama. Sen päätavoitteena on tarjota huipputason suorituskyky LLM-päättelyyn monenlaisilla laitteistoilla mahdollisimman vähäisellä asennuksella. Lisäksi kirjasto tarjoaa Python-sidoksia, jotka tarjoavat korkean tason API:n tekstin täydentämiseen sekä OpenAI-yhteensopivan verkkopalvelimen.

llama.cpp:n päätavoite on mahdollistaa LLM-päättely minimaalisella asennuksella ja huipputason suorituskyvyllä laajalla laitteistovalikoimalla – paikallisesti ja pilvessä.

- Pelkkä C/C++-toteutus ilman riippuvuuksia
- Apple silicon on ensiluokkainen – optimoitu ARM NEONin, Acceleraten ja Metalin avulla
- AVX, AVX2 ja AVX512 -tuki x86-arkkitehtuureille
- 1.5-bittinen, 2-bittinen, 3-bittinen, 4-bittinen, 5-bittinen, 6-bittinen ja 8-bittinen kokonaislukukvantisointi nopeampaan päättelyyn ja pienempään muistinkäyttöön
- Mukautetut CUDA-kernelit LLM:ien ajamiseen NVIDIA-GPU:illa (AMD-GPU-tuki HIPin kautta)
- Vulkan- ja SYCL-taustatuki
- CPU+GPU-hybridi päättely, joka osittain kiihdyttää malleja, jotka ovat suurempia kuin käytettävissä oleva VRAM-kapasiteetti

## **Phi-3.5:n kvantisointi käyttäen llama.cpp:tä**

Phi-3.5-Instruct-malli voidaan kvantisoida llama.cpp:llä, mutta Phi-3.5-Vision ja Phi-3.5-MoE eivät ole vielä tuettuja. llama.cpp:n muuntama formaatti on gguf, joka on myös laajimmin käytetty kvantisointiformaatti.

Hugging Facessa on suuri määrä kvantisoituja GGUF-muotoisia malleja. AI Foundry, Ollama ja LlamaEdge käyttävät llama.cpp:tä, joten GGUF-malleja käytetään myös usein.

### **Mikä on GGUF**

GGUF on binäärimuoto, joka on optimoitu mallien nopeaan lataukseen ja tallennukseen, tehden siitä erittäin tehokkaan päättelykäyttöön. GGUF on suunniteltu käytettäväksi GGML:n ja muiden suoritinten kanssa. GGUF:n on kehittänyt @ggerganov, joka on myös llama.cpp:n kehittäjä, suosittu C/C++-pohjainen LLM-päättelykehys. Alkujaan PyTorchin kaltaisissa kehyksissä kehitetyt mallit voidaan muuntaa GGUF-muotoon käytettäväksi näissä moottoreissa.

### **ONNX vs GGUF**

ONNX on perinteinen koneoppimisen/syväoppimisen formaatti, jota tuetaan hyvin eri tekoälykehyksissä ja jolla on hyviä käyttötarkoituksia reunalaitteissa. GGUF perustuu llama.cpp:hen ja voidaan sanoa, että se on syntynyt GenAI-aikakaudella. Molemmilla on samankaltaisia käyttötarkoituksia. Jos haluat paremman suorituskyvyn sulautetussa laitteistossa ja sovelluskerroksissa, ONNX voi olla valintasi. Jos käytät llama.cpp:n johdannaista kehystä ja teknologiaa, GGUF voi olla parempi.

### **Phi-3.5-Instructin kvantisointi käyttäen llama.cpp:tä**

**1. Ympäristön konfigurointi**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantisointi**

Phi-3.5-Instructin muuntaminen FP16 GGUF:ksi käyttäen llama.cpp:tä


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5:n kvantisointi INT4-muotoon


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

1. Lisätietoa llama.cpp:stä [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Lisätietoa onnxruntimesta [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Lisätietoa GGUF:stä [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on pidettävä auktoriteettisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.