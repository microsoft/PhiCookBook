# **Korištenje Phi-3 u Microsoft Foundry**

S razvojem Generativne AI, nadamo se koristiti jedinstvenu platformu za upravljanje različitim LLM i SLM, integraciju podataka poduzeća, fino podešavanje/RAG operacije i evaluaciju različitih poslovanja poduzeća nakon integracije LLM i SLM, itd., kako bi se generativna AI mogla pametnije primijeniti u aplikacijama. [Microsoft Foundry](https://ai.azure.com) je platforma za generativne AI aplikacije na razini poduzeća.

![aistudo](../../../../translated_images/hr/aifoundry_home.f28a8127c96c7d93.webp)

S Microsoft Foundry možete procijeniti odgovore velikih jezičnih modela (LLM) i orkestrirati komponente aplikacije za upite pomoću prompt flow za bolje performanse. Platforma omogućava skalabilnost za lakšu transformaciju prototipova u punopravnu proizvodnju. Kontinuirano praćenje i usavršavanje podržavaju dugoročni uspjeh.

Phi-3 model možemo brzo implementirati na Microsoft Foundry kroz jednostavne korake, a zatim koristiti Microsoft Foundry za dovršetak rada povezanog s Playground/Chat za Phi-3, fino podešavanje, evaluaciju i drugo.

## **1. Priprema**

Ako već imate instaliran [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) na svom računalu, korištenje ovog predloška jednostavno je kao pokretanje ove naredbe u novom direktoriju.

## Ručno stvaranje

Stvaranje Microsoft Foundry projekta i centra izvrstan je način za organizaciju i upravljanje vašim AI radom. Evo vodiča korak po korak koji će vam pomoći da započnete:

### Stvaranje projekta u Microsoft Foundry

1. **Idite na Microsoft Foundry**: Prijavite se na Microsoft Foundry portal.
2. **Stvorite projekt**:
   - Ako ste u projektu, odaberite "Microsoft Foundry" u gornjem lijevom kutu stranice za povratak na početnu stranicu.
   - Odaberite "+ Create project".
   - Unesite naziv projekta.
   - Ako imate hub, automatski će biti odabran. Ako imate pristup više hubova, možete odabrati drugi s padajućeg izbornika. Ako želite stvoriti novi hub, odaberite "Create new hub" i unesite naziv.
   - Odaberite "Create".

### Stvaranje huba u Microsoft Foundry

1. **Idite na Microsoft Foundry**: Prijavite se sa svojim Azure računom.
2. **Stvorite hub**:
   - Odaberite Management center iz lijevog izbornika.
   - Odaberite "All resources", zatim strelicu prema dolje pored "+ New project" i odaberite "+ New hub".
   - U dijalogu "Create a new hub" unesite naziv svog huba (npr. contoso-hub) i po potrebi prilagodite ostala polja.
   - Odaberite "Next", pregledajte informacije, zatim odaberite "Create".

Za detaljnije upute, možete pogledati službenu [Microsoft dokumentaciju](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Nakon uspješnog stvaranja, možete pristupiti svom studiju putem [ai.azure.com](https://ai.azure.com/)

Na jednom AI Foundry može biti više projekata. Stvorite projekt u AI Foundry za pripremu.

Stvaranje Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Implementacija Phi modela u Microsoft Foundry**

Kliknite na opciju Explore projekta da uđete u Model Catalog i odaberete Phi-3

Odaberite Phi-3-mini-4k-instruct

Kliknite 'Deploy' za implementaciju modela Phi-3-mini-4k-instruct

> [!NOTE]
>
> Prilikom implementacije možete odabrati računalnu snagu

## **3. Playground Chat Phi u Microsoft Foundry**

Idite na stranicu implementacije, odaberite Playground i razgovarajte s Phi-3 u Microsoft Foundry

## **4. Implementacija modela iz Microsoft Foundry**

Za implementaciju modela iz Azure Model Catalog-a slijedite ove korake:

- Prijavite se u Microsoft Foundry.
- Odaberite model koji želite implementirati iz Microsoft Foundry kataloga modela.
- Na stranici s detaljima modela odaberite Deploy, zatim Serverless API s Azure AI Content Safety.
- Odaberite projekt u kojem želite implementirati svoje modele. Za korištenje Serverless API usluge, vaš radni prostor mora biti u regiji East US 2 ili Sweden Central. Možete prilagoditi naziv implementacije.
- U čarobnjaku za implementaciju odaberite cijene i uvjete kako biste saznali o cijenama i uvjetima korištenja.
- Odaberite Deploy. Pričekajte da implementacija bude spremna i da budete preusmjereni na stranicu Deployments.
- Odaberite Open in playground za početak interakcije s modelom.
- Možete se vratiti na stranicu Deployments, odabrati implementaciju i zabilježiti URL krajnje točke (Target URL) i Tajni ključ (Secret Key), koje možete koristiti za pozivanje implementacije i generiranje rezultata.
- Detalje krajnje točke, URL i pristupne ključeve uvijek možete pronaći tako da idete na karticu Build i odaberete Deployments u odjeljku Components.

> [!NOTE]
> Imajte na umu da vaš račun mora imati dozvole uloga Azure AI Developer na Resource Group da biste mogli izvršiti ove korake.

## **5. Korištenje Phi API u Microsoft Foundry**

Pristupiti možete https://{Your project name}.region.inference.ml.azure.com/swagger.json kroz Postman GET i povezati s ključem za upoznavanje ponuđenih sučelja

Vrlo je jednostavno dobiti parametre zahtjeva kao i parametre odgovora.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI prevoditeljske usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->