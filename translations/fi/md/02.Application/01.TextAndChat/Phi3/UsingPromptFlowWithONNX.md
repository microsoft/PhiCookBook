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

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.fi.png)

2. Asennuksen jälkeen avaa Prompt flow VS Code -laajennus, valitse **Installation dependencies** ja seuraa ohjeita Prompt flow SDK:n asentamiseksi ympäristöösi

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.fi.png)

3. Lataa [Esimerkkikoodi](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ja avaa se VS Codessa

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.fi.png)

4. Avaa **flow.dag.yaml** ja valitse Python-ympäristösi

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.fi.png)

   Avaa **chat_phi3_ort.py** ja muuta Phi-3.5-instruct ONNX -mallin sijainti

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.fi.png)

5. Suorita prompt flow testataksesi

Avaa **flow.dag.yaml** ja klikkaa visual editoria

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.fi.png)

Klikkaa tätä ja suorita testi

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.fi.png)

1. Voit ajaa eräajon terminaalissa saadaksesi lisää tuloksia


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Tulokset voit tarkistaa oletusselaimessasi


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.fi.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.