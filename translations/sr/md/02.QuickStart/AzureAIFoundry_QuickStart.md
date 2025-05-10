<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-05-09T20:15:18+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "sr"
}
-->
# **Korišćenje Phi-3 u Azure AI Foundry**

Sa razvojem Generativne AI, cilj nam je da koristimo jedinstvenu platformu za upravljanje različitim LLM i SLM modelima, integraciju podataka preduzeća, fine-tuning/RAG operacije i evaluaciju različitih poslovnih procesa nakon integracije LLM i SLM, kako bi generativna AI mogla bolje da podrži pametne aplikacije. [Azure AI Foundry](https://ai.azure.com) je platforma za generativne AI aplikacije na nivou preduzeća.

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.sr.png)

Uz Azure AI Foundry, možete evaluirati odgovore velikih jezičkih modela (LLM) i orkestrirati komponente aplikacija sa prompt flow za bolje performanse. Platforma omogućava skalabilnost za jednostavnu transformaciju prototipa u punopravnu produkciju. Kontinuirano praćenje i usavršavanje podržavaju dugoročni uspeh.

Brzo možemo da implementiramo Phi-3 model na Azure AI Foundry kroz jednostavne korake, a zatim koristiti Azure AI Foundry za radove vezane za Phi-3 kao što su Playground/Chat, fine-tuning, evaluacija i druge aktivnosti.

## **1. Priprema**

Ako već imate instaliran [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) na vašem računaru, korišćenje ovog šablona je jednostavno kao pokretanje ove komande u novom direktorijumu.

## Ručno kreiranje

Kreiranje Microsoft Azure AI Foundry projekta i hub-a je odličan način da organizujete i upravljate svojim AI radom. Evo korak-po-korak vodiča za početak:

### Kreiranje projekta u Azure AI Foundry

1. **Idite na Azure AI Foundry**: Prijavite se na portal Azure AI Foundry.
2. **Kreirajte projekat**:
   - Ako ste u nekom projektu, izaberite "Azure AI Foundry" u gornjem levom uglu stranice da biste prešli na početnu stranu.
   - Izaberite "+ Create project".
   - Unesite ime projekta.
   - Ako imate hub, on će biti podrazumevano izabran. Ako imate pristup više hub-ova, možete izabrati drugi sa padajuće liste. Ako želite da napravite novi hub, izaberite "Create new hub" i unesite ime.
   - Izaberite "Create".

### Kreiranje hub-a u Azure AI Foundry

1. **Idite na Azure AI Foundry**: Prijavite se sa vašim Azure nalogom.
2. **Kreirajte hub**:
   - Izaberite Management center iz levog menija.
   - Izaberite "All resources", zatim strelicu pored "+ New project" i izaberite "+ New hub".
   - U dijalogu "Create a new hub" unesite ime za vaš hub (npr. contoso-hub) i po potrebi izmenite ostala polja.
   - Izaberite "Next", pregledajte informacije i zatim izaberite "Create".

Za detaljnije upute, možete pogledati zvaničnu [Microsoft dokumentaciju](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Nakon uspešnog kreiranja, možete pristupiti studiju koji ste napravili preko [ai.azure.com](https://ai.azure.com/)

Na jednom AI Foundry može biti više projekata. Napravite projekat u AI Foundry kao pripremu.

Kreirajte Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Implementacija Phi modela u Azure AI Foundry**

Kliknite na opciju Explore u okviru projekta da uđete u Model Catalog i izaberete Phi-3

Izaberite Phi-3-mini-4k-instruct

Kliknite 'Deploy' da biste implementirali Phi-3-mini-4k-instruct model

> [!NOTE]
>
> Možete izabrati računarsku snagu prilikom implementacije

## **3. Playground Chat Phi u Azure AI Foundry**

Idite na stranicu za implementaciju, izaberite Playground i ćaskajte sa Phi-3 u Azure AI Foundry

## **4. Implementacija modela iz Azure AI Foundry**

Da biste implementirali model iz Azure Model Catalog-a, pratite sledeće korake:

- Prijavite se u Azure AI Foundry.
- Izaberite model koji želite da implementirate iz Azure AI Foundry model kataloga.
- Na stranici sa detaljima modela izaberite Deploy, zatim Serverless API sa Azure AI Content Safety.
- Izaberite projekat u kojem želite da implementirate modele. Da biste koristili Serverless API, vaš workspace mora biti u regionu East US 2 ili Sweden Central. Možete prilagoditi ime implementacije.
- Na čarobnjaku za implementaciju izaberite Pricing and terms da saznate o cenama i uslovima korišćenja.
- Izaberite Deploy. Sačekajte da implementacija bude spremna i da budete preusmereni na stranicu Deployments.
- Izaberite Open in playground da započnete interakciju sa modelom.
- Možete se vratiti na stranicu Deployments, izabrati implementaciju i zabeležiti endpoint-ov Target URL i Secret Key, koje možete koristiti za pozivanje implementacije i generisanje odgovora.
- Detalje o endpoint-u, URL i pristupnim ključevima uvek možete pronaći u Build tabu, u sekciji Components pod Deployments.

> [!NOTE]
> Imajte na umu da vaš nalog mora imati Azure AI Developer ulogu na Resource Group-u da biste mogli da izvršavate ove korake.

## **5. Korišćenje Phi API-ja u Azure AI Foundry**

Možete pristupiti https://{Your project name}.region.inference.ml.azure.com/swagger.json preko Postman GET zahteva i kombinovati ga sa Key-om da biste se upoznali sa dostupnim interfejsima

Vrlo lako možete dobiti parametre zahteva, kao i parametre odgovora.

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране стручног човека. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати употребом овог превода.