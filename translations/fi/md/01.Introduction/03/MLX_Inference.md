# **Inference Phi-3 Apple MLX -kehyksellä**

## **Mikä on MLX Framework**

MLX on taulukkoihin perustuva kehys koneoppimustutkimukseen Apple-sirulla, jonka on tuonut saataville Apple koneoppimustutkimus.

MLX on suunniteltu koneoppimustutkijoiden toimesta koneoppimustutkijoille. Kehyksen tarkoituksena on olla käyttäjäystävällinen, mutta silti tehokas mallien kouluttamiseen ja käyttöönottoon. Myös kehyksen rakenne on konseptuaalisesti yksinkertainen. Tavoitteenamme on tehdä MLX:n laajentamisesta ja parantamisesta helppoa tutkijoille, jotta uusia ideoita voidaan nopeasti kokeilla.

LLM-malleja voidaan kiihdyttää Apple Silicon -laitteissa MLX:n avulla, ja malleja voi ajaa paikallisesti erittäin kätevästi.

## **MLX:n käyttö Phi-3-mini -mallin inferenssiin**

### **1. Määritä MLX-ympäristösi**

1. Python 3.11.x
2. Asenna MLX-kirjasto


```bash

pip install mlx-lm

```

### **2. Phi-3-mini -mallin ajaminen terminaalissa MLX:llä**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Tuloksena (ympäristöni on Apple M1 Max, 64GB) on

![Terminal](../../../../../translated_images/fi/01.5cf57df8f7407cf9.webp)

### **3. Phi-3-mini -mallin kvantisointi MLX:llä terminaalissa**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Malli voidaan kvantisoida mlx_lm.convert-funktiolla, ja oletuskvantisointi on INT4. Tässä esimerkissä Phi-3-mini kvantisoidaan INT4-muotoon.

Malli voidaan kvantisoida mlx_lm.convert-funktiolla, ja oletuskvantisointi on INT4. Tässä esimerkissä Phi-3-mini kvantisoidaan INT4-muotoon. Kvantisoinnin jälkeen malli tallennetaan oletushakemistoon ./mlx_model

Voimme testata MLX:llä kvantisoitua mallia terminaalista


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Tuloksena on

![INT4](../../../../../translated_images/fi/02.7b188681a8eadbc1.webp)


### **4. Phi-3-mini -mallin ajaminen MLX:llä Jupyter Notebookissa**


![Notebook](../../../../../translated_images/fi/03.b9705a3a5aaa89f9.webp)

***Note:*** Lue tämä esimerkkitiedosto [klikkaa tästä](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Resurssit**

1. Lisätietoa Apple MLX Frameworkista [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub -repositorio [https://github.com/ml-explore](https://github.com/ml-explore)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.