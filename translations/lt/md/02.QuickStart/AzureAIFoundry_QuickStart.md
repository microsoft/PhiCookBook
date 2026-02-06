# **Naudojant Phi-3 Azure AI Foundry**

Plėtojant generatyvųjį dirbtinį intelektą (Generative AI), siekiame naudoti vieningą platformą, kuri leistų valdyti skirtingus LLM ir SLM modelius, integruoti įmonės duomenis, atlikti modelių pritaikymą/fine-tuning/RAG operacijas bei vertinti įvairias verslo sritis po LLM ir SLM integracijos. Tokiu būdu generatyvusis dirbtinis intelektas gali būti efektyviau pritaikytas išmaniosioms programoms. [Azure AI Foundry](https://ai.azure.com) yra įmonės lygio generatyvaus dirbtinio intelekto taikymo platforma.

![aistudo](../../../../imgs/01/02/03/aifoundry_home.png)

Naudodami Azure AI Foundry, galite vertinti didelių kalbos modelių (LLM) atsakymus ir organizuoti užklausų taikymo komponentus su „prompt flow“, siekiant geresnių rezultatų. Platforma užtikrina mastelio keitimą, leidžiantį lengvai pereiti nuo koncepcijos įrodymo iki pilnaverčio gamybos proceso. Nuolatinis stebėjimas ir tobulinimas užtikrina ilgalaikę sėkmę.

Phi-3 modelį galime greitai įdiegti Azure AI Foundry platformoje atlikdami paprastus veiksmus, o vėliau naudoti Azure AI Foundry, kad atliktume su Phi-3 susijusius darbus, tokius kaip Playground/Chat, pritaikymas (fine-tuning), vertinimas ir kt.

## **1. Pasiruošimas**

Jei jūsų kompiuteryje jau įdiegta [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo), šį šabloną galite naudoti tiesiog paleisdami komandą naujame kataloge.

## Rankinis kūrimas

Microsoft Azure AI Foundry projekto ir centro (hub) kūrimas yra puikus būdas organizuoti ir valdyti jūsų dirbtinio intelekto darbus. Štai žingsnis po žingsnio vadovas, kaip pradėti:

### Projekto kūrimas Azure AI Foundry

1. **Eikite į Azure AI Foundry**: Prisijunkite prie Azure AI Foundry portalo.
2. **Sukurkite projektą**:
   - Jei jau esate projekte, pasirinkite „Azure AI Foundry“ viršutiniame kairiajame puslapio kampe, kad grįžtumėte į pagrindinį puslapį.
   - Pasirinkite „+ Create project“.
   - Įveskite projekto pavadinimą.
   - Jei turite centrą (hub), jis bus pasirinktas pagal numatytuosius nustatymus. Jei turite prieigą prie daugiau nei vieno centro, galite pasirinkti kitą iš išskleidžiamojo meniu. Jei norite sukurti naują centrą, pasirinkite „Create new hub“ ir įveskite pavadinimą.
   - Pasirinkite „Create“.

### Centro kūrimas Azure AI Foundry

1. **Eikite į Azure AI Foundry**: Prisijunkite naudodami savo Azure paskyrą.
2. **Sukurkite centrą**:
   - Pasirinkite „Management center“ iš kairiojo meniu.
   - Pasirinkite „All resources“, tada spustelėkite rodyklę šalia „+ New project“ ir pasirinkite „+ New hub“.
   - Dialogo lange „Create a new hub“ įveskite centro pavadinimą (pvz., contoso-hub) ir, jei reikia, pakeiskite kitus laukus.
   - Pasirinkite „Next“, peržiūrėkite informaciją ir spustelėkite „Create“.

Daugiau detalių galite rasti oficialioje [Microsoft dokumentacijoje](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Sėkmingai sukūrus, galite pasiekti sukurtą studiją per [ai.azure.com](https://ai.azure.com/)

Viename AI Foundry gali būti keli projektai. Sukurkite projektą AI Foundry platformoje, kad pasiruoštumėte.

Sukurkite Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Phi modelio diegimas Azure AI Foundry**

Pasirinkite projekto „Explore“ parinktį, kad patektumėte į Model Catalog ir pasirinkite Phi-3.

Pasirinkite Phi-3-mini-4k-instruct.

Spustelėkite „Deploy“, kad įdiegtumėte Phi-3-mini-4k-instruct modelį.

> [!NOTE]
>
> Diegimo metu galite pasirinkti skaičiavimo galią.

## **3. Playground Chat Phi Azure AI Foundry**

Eikite į diegimo puslapį, pasirinkite „Playground“ ir bendraukite su Phi-3 Azure AI Foundry platformoje.

## **4. Modelio diegimas iš Azure AI Foundry**

Norėdami įdiegti modelį iš Azure Model Catalog, galite atlikti šiuos veiksmus:

- Prisijunkite prie Azure AI Foundry.
- Pasirinkite modelį, kurį norite įdiegti, iš Azure AI Foundry modelių katalogo.
- Modelio „Details“ puslapyje pasirinkite „Deploy“, tada pasirinkite „Serverless API with Azure AI Content Safety“.
- Pasirinkite projektą, kuriame norite įdiegti savo modelius. Norint naudoti „Serverless API“ pasiūlymą, jūsų darbo sritis turi būti East US 2 arba Sweden Central regione. Galite pritaikyti diegimo pavadinimą.
- Diegimo vedlyje pasirinkite „Pricing and terms“, kad sužinotumėte apie kainodarą ir naudojimo sąlygas.
- Pasirinkite „Deploy“. Palaukite, kol diegimas bus paruoštas, ir būsite nukreipti į „Deployments“ puslapį.
- Pasirinkite „Open in playground“, kad pradėtumėte sąveiką su modeliu.
- Galite grįžti į „Deployments“ puslapį, pasirinkti diegimą ir užsirašyti galinio taško (endpoint) URL ir slaptąjį raktą (Secret Key), kurį galite naudoti diegimui ir užklausų generavimui.
- Visada galite rasti galinio taško detales, URL ir prieigos raktus, naršydami „Build“ skiltyje ir pasirinkdami „Deployments“ iš „Components“ sekcijos.

> [!NOTE]
> Atkreipkite dėmesį, kad jūsų paskyra turi turėti Azure AI Developer rolės leidimus „Resource Group“, kad galėtumėte atlikti šiuos veiksmus.

## **5. Phi API naudojimas Azure AI Foundry**

Galite pasiekti https://{Jūsų projekto pavadinimas}.region.inference.ml.azure.com/swagger.json per Postman GET ir kartu su raktu sužinoti apie teikiamas sąsajas.

Labai patogiai galite gauti užklausos parametrus, taip pat atsakymo parametrus.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.