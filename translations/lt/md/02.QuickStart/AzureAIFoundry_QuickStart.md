# **Phi-3 naudojimas Microsoft Foundry**

Su Generatyvios AI plėtra tikimės naudoti vieningą platformą skirtingiems LLM ir SLM valdyti, įmonių duomenų integracijai, smulkiam derinimui/RAG operacijoms ir skirtingų įmonių verslo vertinimui po LLM ir SLM integracijos, kad generatyvioji AI galėtų geriau įgyvendinti išmaniąsias programas. [Microsoft Foundry](https://ai.azure.com) yra įmonės lygio generatyvios AI programų platforma.

![aistudo](../../../../translated_images/lt/aifoundry_home.f28a8127c96c7d93.webp)

Naudodami Microsoft Foundry galite vertinti didelių kalbų modelių (LLM) atsakymus ir orkestruoti užklausų programos komponentus su prompt flow geresniam veikimui. Platforma palengvina skalę, leidžiančią lengvai perkelti konceptų įrodymus į pilnai veikiančią produkciją. Nuolatinis stebėjimas ir tobulinimas palaiko ilgalaikę sėkmę.

Galime greitai diegti Phi-3 modelį Microsoft Foundry per paprastus žingsnius, o tada naudoti Microsoft Foundry, kad užbaigtume su Phi-3 susijusį Playground/Chat, smulkų derinimą, vertinimą ir kitus susijusius darbus.

## **1. Paruošimas**

Jei jau turite [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) įdiegtą savo kompiuteryje, naudoti šį šabloną yra taip paprasta kaip paleisti šią komandą naujame kataloge.

## Rankinis kūrimas

Microsoft Foundry projekto ir hub kūrimas yra puikus būdas organizuoti ir valdyti jūsų AI darbus. Štai nuoseklus vadovas, kuris padės jums pradėti:

### Projekto kūrimas Microsoft Foundry

1. **Eikite į Microsoft Foundry**: Prisijunkite prie Microsoft Foundry portalo.
2. **Sukurkite projektą**:
   - Jei esate projekte, pasirinkite „Microsoft Foundry“ viršutiniame kairiajame puslapio kampe, kad pereitumėte į Pradžios puslapį.
   - Pasirinkite „+ Sukurti projektą“.
   - Įveskite projekto pavadinimą.
   - Jei turite hub, jis bus pasirinktas pagal nutylėjimą. Jei turite prieigą prie daugiau nei vieno hub, galite pasirinkti kitą iš išskleidžiamojo sąrašo. Jei norite sukurti naują hub, pasirinkite „Sukurti naują hub“ ir pateikite pavadinimą.
   - Paspauskite „Sukurti“.

### Hub kūrimas Microsoft Foundry

1. **Eikite į Microsoft Foundry**: Prisijunkite su savo Azure paskyra.
2. **Sukurkite hub**:
   - Kairiajame meniu pasirinkite Valdymo centrą.
   - Pasirinkite „Visi ištekliai“, tada rodyklę žemyn šalia „+ Naujas projektas“ ir pasirinkite „+ Naujas hub“.
   - „Sukurti naują hub“ lange įveskite savo hub pavadinimą (pvz., contoso-hub) ir pagal poreikį pakeiskite kitus laukus.
   - Paspauskite „Toliau“, peržiūrėkite informaciją ir tada pasirinkite „Sukurti“.

Daugiau detalių galite rasti oficialioje [Microsoft dokumentacijoje](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Sėkmingai sukūrę, galite pasiekti savo studiją per [ai.azure.com](https://ai.azure.com/).

Viename AI Foundry gali būti keli projektai. Sukurkite projektą AI Foundry, kad pasiruoštumėte.

Sukurkite Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Phi modelio diegimas Microsoft Foundry**

Spustelėkite projekto „Explore“ parinktį, kad patektumėte į Modelių katalogą ir pasirinkite Phi-3

Pasirinkite Phi-3-mini-4k-instruct

Spustelėkite „Deploy“, kad įdiegtumėte Phi-3-mini-4k-instruct modelį

> [!NOTE]
>
> Diegdami galite pasirinkti skaičiavimo galią

## **3. Playground Chat Phi Microsoft Foundry**

Eikite į diegimo puslapį, pasirinkite Playground ir kalbėkitės su Microsoft Foundry Phi-3

## **4. Modelio diegimas iš Microsoft Foundry**

Norėdami įdiegti modelį iš Azure Modelių katalogo, atlikite šiuos žingsnius:

- Prisijunkite prie Microsoft Foundry.
- Pasirinkite modelį, kurį norite įdiegti iš Microsoft Foundry modelių katalogo.
- Modelio detalumo puslapyje pasirinkite „Deploy“, tada „Serverless API su Azure AI turinio saugumu“.
- Pasirinkite projektą, kuriame norite įdiegti modelius. Norint naudotis Serverless API pasiūlymu, jūsų darbo sritis turi priklausyti East US 2 arba Sweden Central regionui. Galite pritaikyti Diegimo pavadinimą.
- Diegimo vedlyje pasirinkite kainodarą ir sąlygas, jei norite sužinoti apie kainas ir naudojimo sąlygas.
- Paspauskite „Deploy“. Palaukite, kol diegimas bus paruoštas ir būsite nukreipti į Diegimų puslapį.
- Pasirinkite „Open in playground“, kad pradėtumėte sąveikauti su modeliu.
- Galite sugrįžti į Diegimų puslapį, pasirinkti diegimą ir atkreipti dėmesį į pabaigos taško Target URL ir Slaptojo rakto reikšmes, kurias galite naudoti kviesdami diegimą ir generuodami užbaigimus.
- Visada galite rasti pabaigos taško detales, URL ir prieigos raktus pereidami į Build skirtuką ir pasirinkdami Deployments iš Components skyriaus.

> [!NOTE]
> Atkreipkite dėmesį, kad jūsų paskyra turi turėti Azure AI Developer rolės teises Resursų grupėje, kad galėtumėte atlikti šiuos veiksmus.

## **5. Phi API naudojimas Microsoft Foundry**

Per Postman GET galite pasiekti https://{Jūsų projekto pavadinimas}.region.inference.ml.azure.com/swagger.json ir derinti su Raktu, kad sužinotumėte apie pateiktus sąsajų tipus

Galite labai patogiai gauti užklausų parametrus ir atsakymų parametrus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuotas vertimas gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama naudoti profesionalų žmogišką vertimą. Mes neatsakome už bet kokius nesusipratimus ar interpretacijos klaidas, kylančias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->