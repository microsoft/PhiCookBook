<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:25:08+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "fi"
}
-->
# **Phi-3:n käyttäminen Azure AI Foundryssa**

Generatiivisen tekoälyn kehittyessä toivomme käyttävämme yhtenäistä alustaa erilaisten LLM- ja SLM-mallien, yritysdatan integroinnin, hienosäädön/RAG-toimintojen sekä eri yritystoimintojen arvioinnin hallintaan LLM- ja SLM-mallien yhdistämisen jälkeen, jotta generatiivisen tekoälyn älykkäät sovellukset voidaan toteuttaa entistä paremmin. [Azure AI Foundry](https://ai.azure.com) on yritystason generatiivisen tekoälyn sovellusalusta.

![aistudo](../../../../translated_images/aifoundry_home.f28a8127c96c7d93d6fb1d0a69b635bc36834da1f0615d7d2b8be216021d9eeb.fi.png)

Azure AI Foundryn avulla voit arvioida suurten kielimallien (LLM) vastauksia ja orkestroida kehotteiden sovelluskomponentteja prompt flow’n avulla paremman suorituskyvyn saavuttamiseksi. Alusta tukee skaalautuvuutta, mikä helpottaa konseptien muuttamista täysimittaisiksi tuotantojärjestelmiksi. Jatkuva seuranta ja hienosäätö tukevat pitkäaikaista menestystä.

Voimme nopeasti ottaa Phi-3-mallin käyttöön Azure AI Foundryssa yksinkertaisin askelin ja käyttää Azure AI Foundrya Phi-3:een liittyvien Playground/Chat-, hienosäätö-, arviointi- ja muiden tehtävien suorittamiseen.

## **1. Valmistelut**

Jos sinulla on jo [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) asennettuna koneellesi, tämän mallipohjan käyttäminen on yhtä helppoa kuin suorittaa tämä komento uudessa hakemistossa.

## Manuaalinen luonti

Microsoft Azure AI Foundry -projektin ja hubin luominen on erinomainen tapa järjestää ja hallita tekoälytyötäsi. Tässä vaiheittainen opas alkuun pääsemiseksi:

### Projektin luominen Azure AI Foundryssa

1. **Siirry Azure AI Foundryyn**: Kirjaudu Azure AI Foundryn portaaliin.
2. **Luo projekti**:
   - Jos olet jo projektissa, valitse sivun vasemmasta yläkulmasta "Azure AI Foundry" siirtyäksesi kotisivulle.
   - Valitse "+ Create project".
   - Anna projektille nimi.
   - Jos sinulla on hub, se valitaan oletuksena. Jos sinulla on pääsy useampaan hubiin, voit valita toisen pudotusvalikosta. Jos haluat luoda uuden hubin, valitse "Create new hub" ja anna sille nimi.
   - Valitse "Create".

### Hubin luominen Azure AI Foundryssa

1. **Siirry Azure AI Foundryyn**: Kirjaudu sisään Azure-tililläsi.
2. **Luo hub**:
   - Valitse vasemman valikon Hallintakeskus (Management center).
   - Valitse "All resources", napsauta nuolta "+ New project" -kohdan vieressä ja valitse "+ New hub".
   - "Create a new hub" -valintaikkunassa anna hubillesi nimi (esim. contoso-hub) ja muokkaa muita kenttiä halutessasi.
   - Valitse "Next", tarkista tiedot ja valitse "Create".

Yksityiskohtaisempia ohjeita löydät virallisesta [Microsoftin dokumentaatiosta](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Onnistuneen luomisen jälkeen pääset luomaasi studioon osoitteessa [ai.azure.com](https://ai.azure.com/)

Yhdellä AI Foundrylla voi olla useita projekteja. Luo AI Foundryyn projekti valmistautuaksesi.

Luo Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Phi-mallin käyttöönotto Azure AI Foundryssa**

Valitse projektin Explore-vaihtoehto päästäksesi Model Catalogiin ja valitse Phi-3

Valitse Phi-3-mini-4k-instruct

Klikkaa 'Deploy' ottaaksesi Phi-3-mini-4k-instruct -mallin käyttöön

> [!NOTE]
>
> Voit valita laskentatehon käyttöönoton yhteydessä

## **3. Playground Chat Phi Azure AI Foundryssa**

Siirry käyttöönotto-sivulle, valitse Playground ja keskustele Azure AI Foundryn Phi-3:n kanssa

## **4. Mallin käyttöönotto Azure AI Foundrystä**

Mallin käyttöönottoon Azure Model Catalogista voit toimia seuraavasti:

- Kirjaudu Azure AI Foundryyn.
- Valitse käyttöönotettava malli Azure AI Foundryn mallikatalogista.
- Mallin Tiedot-sivulla valitse Deploy ja sitten Serverless API with Azure AI Content Safety.
- Valitse projekti, johon haluat ottaa mallin käyttöön. Serverless API -palvelun käyttö edellyttää, että työtila sijaitsee East US 2- tai Sweden Central -alueella. Voit muokata käyttöönoton nimeä.
- Käyttöönotto-velhon sivulla valitse Hinnoittelu ja ehdot tutustuaksesi hinnoitteluun ja käyttöehtoihin.
- Valitse Deploy. Odota, että käyttöönotto valmistuu ja sinut ohjataan Deployments-sivulle.
- Valitse Open in playground aloittaaksesi mallin kanssa vuorovaikutuksen.
- Voit palata Deployments-sivulle, valita käyttöönoton ja huomioida päätepisteen Target URL:n sekä Secret Keyn, joita voit käyttää kutsuaksesi käyttöönottoa ja luodaksesi vastauksia.
- Päätepisteen tiedot, URL ja käyttöavaimet löytyvät aina Build-välilehdeltä valitsemalla Components-osiossa Deployments.

> [!NOTE]
> Huomioithan, että tililläsi on oltava Azure AI Developer -roolipääsyt Resource Groupissa näiden toimenpiteiden suorittamiseksi.

## **5. Phi API:n käyttäminen Azure AI Foundryssa**

Voit käyttää osoitetta https://{Your project name}.region.inference.ml.azure.com/swagger.json Postmanin GET-pyynnöllä ja yhdistää sen Key-arvoon tutustuaksesi tarjottuihin rajapintoihin.

Saat pyynnön parametrit erittäin kätevästi sekä vastausparametrit.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.