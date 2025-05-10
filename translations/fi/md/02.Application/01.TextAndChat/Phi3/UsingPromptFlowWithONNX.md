<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:53:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "fi"
}
-->
# Windowsin GPU:n käyttäminen Prompt flow -ratkaisun luomiseen Phi-3.5-Instruct ONNX:n kanssa

Seuraava dokumentti on esimerkki siitä, miten PromptFlowa käytetään ONNX:n (Open Neural Network Exchange) kanssa Phi-3 -mallien pohjalta kehitettyjen tekoälysovellusten luomiseen.

PromptFlow on kehitystyökalupaketti, joka helpottaa LLM-pohjaisten (Large Language Model) tekoälysovellusten koko kehityssykliä ideoinnista ja prototypoinnista testaukseen ja arviointiin.

Integroimalla PromptFlow ONNX:n kanssa kehittäjät voivat:

- Optimoida mallin suorituskykyä: Hyödyntää ONNX:ää tehokkaaseen mallin päättelyyn ja käyttöönottoon.
- Yksinkertaistaa kehitystä: Käyttää PromptFlowta työnkulun hallintaan ja toistuvien tehtävien automatisointiin.
- Parantaa yhteistyötä: Mahdollistaa paremman tiimityön tarjoamalla yhtenäisen kehitysympäristön.

**Prompt flow** on kehitystyökalupaketti, joka helpottaa LLM-pohjaisten tekoälysovellusten koko kehityssykliä ideoinnista, prototypoinnin, testauksen ja arvioinnin kautta tuotantoon ja seurantaan asti. Se tekee prompt-tekniikasta paljon helpompaa ja mahdollistaa LLM-sovellusten rakentamisen tuotantolaatuisina.

Prompt flow voi yhdistää OpenAI:hin, Azure OpenAI Serviceen sekä räätälöitäviin malleihin (Huggingface, paikalliset LLM/SLM). Tavoitteenamme on ottaa käyttöön Phi-3.5:n kvantisoitu ONNX-malli paikallisissa sovelluksissa. Prompt flow voi auttaa meitä suunnittelemaan liiketoimintaa paremmin ja toteuttamaan paikallisia ratkaisuja Phi-3.5:n pohjalta. Tässä esimerkissä yhdistämme ONNX Runtime GenAI -kirjaston ja toteutamme Prompt flow -ratkaisun Windows GPU:lla.

## **Asennus**

### **ONNX Runtime GenAI Windows GPU:lle**

Lue tämä ohje ONNX Runtime GenAI:n asentamiseksi Windows GPU:lle [klikkaa tästä](./ORTWindowGPUGuideline.md)

### **Prompt flow:n käyttöönotto VSCodessa**

1. Asenna Prompt flow VS Code -laajennus

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.fi.png)

2. Laajennuksen asennuksen jälkeen klikkaa laajennusta ja valitse **Installation dependencies** asentaaksesi Prompt flow SDK:n ympäristöösi tämän ohjeen mukaan

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.fi.png)

3. Lataa [Esimerkkikoodi](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ja avaa se VS Codessa

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.fi.png)

4. Avaa **flow.dag.yaml** ja valitse Python-ympäristösi

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.fi.png)

   Avaa **chat_phi3_ort.py** ja vaihda Phi-3.5-instruct ONNX -mallin sijainti

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.fi.png)

5. Suorita prompt flow testataksesi

Avaa **flow.dag.yaml** ja klikkaa visual editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.fi.png)

klikkauksen jälkeen suorita testi

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.fi.png)

1. Voit ajaa eräajon terminaalissa nähdäksesi lisää tuloksia


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Tulokset voit tarkistaa oletusselaimessasi


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.fi.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.