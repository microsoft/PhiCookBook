<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:01:29+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "fi"
}
-->
# Windows GPU:n käyttäminen Prompt flow -ratkaisun luomiseen Phi-3.5-Instruct ONNX:llä

Seuraava dokumentti on esimerkki siitä, miten PromptFlowa käytetään ONNX:n (Open Neural Network Exchange) kanssa Phi-3 -mallien pohjalta kehitettyjen tekoälysovellusten rakentamiseen.

PromptFlow on kehitystyökalupaketti, joka on suunniteltu sujuvoittamaan koko LLM-pohjaisten (Large Language Model) tekoälysovellusten kehityssykliä ideoinnista ja prototypoinnista testaukseen ja arviointiin.

Integroimalla PromptFlow ONNX:n kanssa kehittäjät voivat:

- Optimoida mallin suorituskyvyn: Hyödyntää ONNX:ää tehokkaaseen mallin päättelyyn ja käyttöönottoon.
- Yksinkertaistaa kehitystä: Käyttää PromptFlowta työnkulun hallintaan ja toistuvien tehtävien automatisointiin.
- Parantaa yhteistyötä: Mahdollistaa paremman tiimityön tarjoamalla yhtenäisen kehitysympäristön.

**Prompt flow** on kehitystyökalupaketti, joka on suunniteltu sujuvoittamaan koko LLM-pohjaisten tekoälysovellusten kehityssykliä ideoinnista, prototypoinnista, testauksesta ja arvioinnista aina tuotantoon käyttöönottoon ja seurantaan asti. Se tekee prompt-tekniikasta paljon helpompaa ja mahdollistaa tuotantolaatuisten LLM-sovellusten rakentamisen.

Prompt flow voi yhdistää OpenAI:hin, Azure OpenAI Serviceen sekä räätälöitäviin malleihin (Huggingface, paikalliset LLM/SLM). Tavoitteenamme on ottaa Phi-3.5:n kvantisoitu ONNX-malli käyttöön paikallisissa sovelluksissa. Prompt flow auttaa meitä suunnittelemaan liiketoimintaamme paremmin ja toteuttamaan paikallisia ratkaisuja Phi-3.5:n pohjalta. Tässä esimerkissä yhdistämme ONNX Runtime GenAI -kirjaston Prompt flow -ratkaisun toteuttamiseksi Windows GPU:lla.

## **Asennus**

### **ONNX Runtime GenAI Windows GPU:lle**

Lue tämä ohje ONNX Runtime GenAI:n asentamiseksi Windows GPU:lle [klikkaa tästä](./ORTWindowGPUGuideline.md)

### **Prompt flow -ympäristön asennus VSCodeen**

1. Asenna Prompt flow VS Code -laajennus

![pfvscode](../../../../../../translated_images/fi/pfvscode.eff93dfc66a42cbe.webp)

2. Asennuksen jälkeen avaa Prompt flow VS Code -laajennus, valitse **Installation dependencies** ja seuraa ohjeita Prompt flow SDK:n asentamiseksi ympäristöösi

![pfsetup](../../../../../../translated_images/fi/pfsetup.b46e93096f5a254f.webp)

3. Lataa [Esimerkkikoodi](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ja avaa se VS Codessa

![pfsample](../../../../../../translated_images/fi/pfsample.8d89e70584ffe7c4.webp)

4. Avaa **flow.dag.yaml** ja valitse Python-ympäristösi

![pfdag](../../../../../../translated_images/fi/pfdag.264a77f7366458ff.webp)

   Avaa **chat_phi3_ort.py** ja muuta Phi-3.5-instruct ONNX -mallin sijainti

![pfphi](../../../../../../translated_images/fi/pfphi.72da81d74244b45f.webp)

5. Suorita prompt flow testataksesi

Avaa **flow.dag.yaml** ja klikkaa visual editoria

![pfv](../../../../../../translated_images/fi/pfv.ba8a81f34b20f603.webp)

Klikkaa tätä ja suorita testi

![pfflow](../../../../../../translated_images/fi/pfflow.4e1135a089b1ce1b.webp)

1. Voit ajaa eräajon terminaalissa saadaksesi lisää tuloksia


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Tulokset voit tarkistaa oletusselaimessasi


![pfresult](../../../../../../translated_images/fi/pfresult.c22c826f8062d7cb.webp)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.