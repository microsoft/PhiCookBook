<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:41:03+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "fi"
}
-->
# **Rakenna oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 -perheellä**

Oletko käyttänyt workspace-agenttia GitHub Copilot Chatissa? Haluatko rakentaa oman tiimisi koodiavustajan? Tämä käytännön harjoitus yhdistää avoimen lähdekoodin mallin luodakseen yritystason koodiliiketoiminta-agentin.

## **Perusteet**

### **Miksi valita Microsoft Phi-3**

Phi-3 on perhesarja, joka sisältää phi-3-mini, phi-3-small ja phi-3-medium -mallit, jotka perustuvat erilaisiin koulutusparametreihin tekstin generointiin, dialogin täydentämiseen ja koodin luomiseen. Lisäksi on phi-3-vision, joka perustuu Visioniin. Se sopii yrityksille tai eri tiimeille offline-generatiivisten tekoälyratkaisujen luomiseen.

Suositeltavaa lukea tämä linkki [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat -laajennus tarjoaa keskustelukäyttöliittymän, jonka avulla voit olla vuorovaikutuksessa GitHub Copilotin kanssa ja saada vastauksia koodaukseen liittyviin kysymyksiin suoraan VS Codessa ilman, että sinun tarvitsee selata dokumentaatiota tai etsiä vastauksia verkkoyhteisöistä.

Copilot Chat voi käyttää syntaksin korostusta, sisennystä ja muita muotoiluominaisuuksia selkeyttääkseen luotua vastausta. Käyttäjän kysymyksen tyypistä riippuen tulos voi sisältää linkkejä kontekstiin, jota Copilot käytti vastauksen luomiseen, kuten lähdekooditiedostoja tai dokumentaatiota, tai painikkeita VS Coden toimintojen käyttämiseen.

- Copilot Chat integroituu kehittäjän työnkulkuun ja tarjoaa apua juuri silloin kun sitä tarvitset:

- Aloita keskustelu suoraan editorista tai terminaalista saadaksesi apua koodauksen aikana

- Käytä Chat-näkymää, jossa AI-avustaja on aina valmiina auttamaan

- Käynnistä Quick Chat esittääksesi nopean kysymyksen ja palataksesi nopeasti takaisin työhösi

Voit käyttää GitHub Copilot Chatia monissa tilanteissa, kuten:

- Vastaamaan koodauskysymyksiin parhaista ratkaisuista

- Selittämään toisen kirjoittamaa koodia ja ehdottamaan parannuksia

- Ehdottamaan koodikorjauksia

- Generoimaan yksikkötestitapauksia

- Generoimaan koodidokumentaatiota

Suositeltavaa lukea tämä linkki [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Viittaaminen **@workspace**-avainsanaan Copilot Chatissa antaa sinun esittää kysymyksiä koko koodikannastasi. Kysymyksen perusteella Copilot hakee älykkäästi relevantteja tiedostoja ja symboleja, joita se käyttää vastauksessaan linkkeinä ja koodiesimerkkeinä.

Vastatakseen kysymykseesi **@workspace** etsii samoista lähteistä, joita kehittäjä käyttäisi navigoidessaan koodikantaa VS Codessa:

- Kaikki työtilan tiedostot, paitsi .gitignore-tiedostolla ohitetut tiedostot

- Hakemistorakenne, mukaan lukien alikansiot ja tiedostonimet

- GitHubin koodihakemisto, jos työtila on GitHub-repositorio ja indeksoitu koodihakua varten

- Symbolit ja määritelmät työtilassa

- Tällä hetkellä valittu teksti tai näkyvä teksti aktiivisessa editorissa

Huom: .gitignore ohitetaan, jos sinulla on tiedosto auki tai teksti valittuna ohitetussa tiedostossa.

Suositeltavaa lukea tämä linkki [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Lisätietoja tästä harjoituksesta**

GitHub Copilot on parantanut merkittävästi yritysten ohjelmointitehokkuutta, ja jokainen yritys haluaa räätälöidä GitHub Copilotin toimintoja omiin tarpeisiinsa. Monet yritykset ovat räätälöineet GitHub Copilotin kaltaisia laajennuksia omien liiketoimintaskenaarioidensa ja avoimen lähdekoodin mallien pohjalta. Yrityksille räätälöidyt laajennukset ovat helpommin hallittavissa, mutta tämä vaikuttaa myös käyttäjäkokemukseen. GitHub Copilot on nimittäin vahvempi yleisten skenaarioiden ja ammatillisuuden käsittelyssä. Jos käyttökokemus voidaan pitää yhtenäisenä, on parempi räätälöidä yrityksen oma laajennus. GitHub Copilot Chat tarjoaa yrityksille API-rajapintoja chat-kokemuksen laajentamiseen. Yhtenäisen kokemuksen ylläpitäminen ja räätälöityjen toimintojen tarjoaminen on parempi käyttäjäkokemus.

Tässä harjoituksessa käytetään pääasiassa Phi-3-mallia yhdistettynä paikalliseen NPU:hun ja Azure-hybridiin rakentaakseen räätälöidyn agentin GitHub Copilot Chatiin ***@PHI3*** auttamaan yrityskehittäjiä koodin generoinnissa***(@PHI3 /gen)*** ja kuviin perustuvassa koodin generoinnissa ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d095fe0b942687287803c03933d2d1d439d14e10fa1442a864d.fi.png)

### ***Huom:***

Tämä harjoitus on tällä hetkellä toteutettu Intel CPU:n ja Apple Siliconin AIPC:ssä. Päivitämme jatkossa Qualcommin NPU-version.

## **Harjoitus**

| Nimi | Kuvaus | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Asennukset(✅) | Määritä ja asenna tarvittavat ympäristöt ja asennustyökalut | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Suorita Prompt flow Phi-3-minin kanssa (✅) | Yhdistetty AIPC / Apple Silicon, paikallisen NPU:n avulla koodin generointi Phi-3-minin kautta | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Ota Phi-3-vision käyttöön Azure Machine Learning Service -palvelussa(✅) | Luo koodi käyttämällä Azure Machine Learning Servicen Model Catalog - Phi-3-vision kuvaa | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Luo @phi-3 agentti GitHub Copilot Chatiin(✅)  | Luo räätälöity Phi-3-agentti GitHub Copilot Chatiin koodin generointiin, graafisen koodin luomiseen, RAG:iin jne. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Esimerkkikoodi (✅)  | Lataa esimerkkikoodi | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **Resurssit**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Lisätietoja GitHub Copilotista [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Lisätietoja GitHub Copilot Chatista [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Lisätietoja GitHub Copilot Chat API:sta [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Lisätietoja Azure AI Foundrysta [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Lisätietoja Azure AI Foundryn Model Catalogista [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.