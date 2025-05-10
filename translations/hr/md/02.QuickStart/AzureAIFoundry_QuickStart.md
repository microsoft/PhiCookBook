<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-05-09T20:15:30+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "hr"
}
-->
# **Korištenje Phi-3 u Azure AI Foundry**

S razvojem Generativne AI, cilj nam je koristiti jedinstvenu platformu za upravljanje različitim LLM i SLM modelima, integraciju podataka poduzeća, fine-tuning/RAG operacije te evaluaciju različitih poslovnih procesa nakon integracije LLM i SLM, kako bi generativna AI mogla bolje podržavati pametne aplikacije. [Azure AI Foundry](https://ai.azure.com) je platforma za generativne AI aplikacije na razini poduzeća.

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.hr.png)

S Azure AI Foundry možete evaluirati odgovore velikih jezičnih modela (LLM) i orkestrirati komponente prompt aplikacija pomoću prompt flow-a za bolje performanse. Platforma omogućava skalabilnost i jednostavnu transformaciju koncepta u punu proizvodnju. Kontinuirano praćenje i usavršavanje podržavaju dugoročni uspjeh.

Phi-3 model možemo brzo implementirati na Azure AI Foundry kroz jednostavne korake, a zatim koristiti Azure AI Foundry za završetak poslova vezanih uz Phi-3 kao što su Playground/Chat, fine-tuning, evaluacija i drugo.

## **1. Priprema**

Ako već imate instaliran [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) na svom računalu, korištenje ovog predloška je jednostavno kao pokretanje ove naredbe u novom direktoriju.

## Ručno kreiranje

Kreiranje Microsoft Azure AI Foundry projekta i hub-a odličan je način za organizaciju i upravljanje vašim AI radom. Evo vodiča korak po korak kako započeti:

### Kreiranje projekta u Azure AI Foundry

1. **Idite na Azure AI Foundry**: Prijavite se u Azure AI Foundry portal.
2. **Kreirajte projekt**:
   - Ako ste unutar projekta, odaberite "Azure AI Foundry" u gornjem lijevom kutu stranice da biste otišli na početnu stranicu.
   - Odaberite "+ Create project".
   - Unesite ime projekta.
   - Ako imate hub, on će biti odabran po defaultu. Ako imate pristup više hub-ova, možete odabrati drugi iz padajućeg izbornika. Ako želite kreirati novi hub, odaberite "Create new hub" i unesite ime.
   - Odaberite "Create".

### Kreiranje hub-a u Azure AI Foundry

1. **Idite na Azure AI Foundry**: Prijavite se sa svojim Azure računom.
2. **Kreirajte hub**:
   - Odaberite Management center iz lijevog izbornika.
   - Odaberite "All resources", zatim strelicu prema dolje pored "+ New project" i odaberite "+ New hub".
   - U dijalogu "Create a new hub" unesite ime za svoj hub (npr. contoso-hub) i prilagodite ostala polja po želji.
   - Odaberite "Next", pregledajte informacije, zatim odaberite "Create".

Za detaljnije upute možete pogledati službenu [Microsoft dokumentaciju](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Nakon uspješnog kreiranja, možete pristupiti svom studiju putem [ai.azure.com](https://ai.azure.com/)

Na jednom AI Foundry može postojati više projekata. Kreirajte projekt u AI Foundry kao pripremu.

Kreirajte Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Implementacija Phi modela u Azure AI Foundry**

Kliknite opciju Explore unutar projekta da uđete u Model Catalog i odaberete Phi-3

Odaberite Phi-3-mini-4k-instruct

Kliknite 'Deploy' za implementaciju Phi-3-mini-4k-instruct modela

> [!NOTE]
>
> Tijekom implementacije možete odabrati računalnu snagu

## **3. Playground Chat Phi u Azure AI Foundry**

Idite na stranicu implementacije, odaberite Playground i započnite chat s Phi-3 u Azure AI Foundry

## **4. Implementacija modela iz Azure AI Foundry**

Za implementaciju modela iz Azure Model Catalog-a, slijedite ove korake:

- Prijavite se u Azure AI Foundry.
- Odaberite model koji želite implementirati iz Azure AI Foundry model kataloga.
- Na stranici s detaljima modela odaberite Deploy, zatim odaberite Serverless API s Azure AI Content Safety.
- Odaberite projekt u kojem želite implementirati modele. Za korištenje Serverless API usluge, vaš workspace mora pripadati regiji East US 2 ili Sweden Central. Možete prilagoditi ime implementacije.
- U čarobnjaku za implementaciju odaberite Pricing and terms da biste saznali informacije o cijenama i uvjetima korištenja.
- Odaberite Deploy. Pričekajte dok implementacija ne bude spremna i dok ne budete preusmjereni na stranicu Deployments.
- Odaberite Open in playground za početak interakcije s modelom.
- Možete se vratiti na stranicu Deployments, odabrati implementaciju i zabilježiti Target URL i Secret Key krajnje točke koje možete koristiti za pozivanje implementacije i generiranje odgovora.
- Detalje krajnje točke, URL i pristupne ključeve uvijek možete pronaći tako da odete na Build karticu i odaberete Deployments iz sekcije Components.

> [!NOTE]
> Imajte na umu da vaš račun mora imati dozvole uloga Azure AI Developer na Resource Group za izvođenje ovih koraka.

## **5. Korištenje Phi API-ja u Azure AI Foundry**

Možete pristupiti https://{Your project name}.region.inference.ml.azure.com/swagger.json putem Postman GET zahtjeva i kombinirati ga s Key kako biste se upoznali s dostupnim sučeljima

Vrlo je jednostavno dobiti parametre zahtjeva, kao i parametre odgovora.

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.