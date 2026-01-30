# Phi-3 modelio pritaikymas su Azure AI Foundry

Pažvelkime, kaip pritaikyti Microsoft Phi-3 Mini kalbos modelį naudojant Azure AI Foundry. Pritaikymas leidžia modelį pritaikyti specifinėms užduotims, padarant jį dar galingesnį ir kontekstualiai jautresnį.

## Svarstymai

- **Galimybės:** Kokius modelius galima pritaikyti? Ką bazinis modelis gali atlikti po pritaikymo?
- **Kaina:** Koks yra pritaikymo kainodaros modelis?
- **Pritaikomumas:** Kiek galima modifikuoti bazinį modelį – ir kokiais būdais?
- **Patogumas:** Kaip vyksta pritaikymas – ar reikia rašyti specialų kodą? Ar reikia turėti savo kompiuterinius resursus?
- **Saugumas:** Pritaikyti modeliai gali kelti saugumo riziką – ar yra apsaugos priemonių, kurios padėtų išvengti netyčinės žalos?

![AIFoundry Models](../../../../imgs/03/AIFoundry/AIFoundryModels.png)

## Pasiruošimas pritaikymui

### Būtinos sąlygos

> [!NOTE]
> Phi-3 šeimos modeliams „mokėk už naudojimą“ pritaikymo pasiūlymas galimas tik su centrais, sukurtais **East US 2** regionuose.

- Azure prenumerata. Jei neturite Azure prenumeratos, sukurkite [mokamą Azure paskyrą](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go), kad galėtumėte pradėti.

- [AI Foundry projektas](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure vaidmenimis pagrįsta prieiga (Azure RBAC) naudojama suteikti prieigą prie operacijų Azure AI Foundry. Norint atlikti veiksmus šiame straipsnyje, jūsų vartotojo paskyrai turi būti priskirtas __Azure AI Developer role__ vaidmuo išteklių grupėje.

### Prenumeratos teikėjo registracija

Patikrinkite, ar prenumerata yra registruota `Microsoft.Network` išteklių teikėjui.

1. Prisijunkite prie [Azure portalo](https://portal.azure.com).
1. Kairiajame meniu pasirinkite **Subscriptions**.
1. Pasirinkite prenumeratą, kurią norite naudoti.
1. Kairiajame meniu pasirinkite **AI project settings** > **Resource providers**.
1. Patikrinkite, ar **Microsoft.Network** yra išteklių teikėjų sąraše. Jei ne, pridėkite jį.

### Duomenų paruošimas

Paruoškite savo mokymo ir validacijos duomenis, kad galėtumėte pritaikyti modelį. Mokymo ir validacijos duomenų rinkiniai turi sudaryti įvesties ir išvesties pavyzdžius, kaip norėtumėte, kad modelis veiktų.

Įsitikinkite, kad visi mokymo pavyzdžiai atitinka numatytą formatą prognozėms. Kad modeliai būtų efektyviai pritaikyti, užtikrinkite subalansuotą ir įvairų duomenų rinkinį.

Tai apima duomenų balanso palaikymą, įvairių scenarijų įtraukimą ir periodišką mokymo duomenų tobulinimą, kad jie atitiktų realaus pasaulio lūkesčius, galiausiai užtikrinant tikslesnius ir subalansuotus modelio atsakymus.

Skirtingų tipų modeliams reikalingas skirtingas mokymo duomenų formatas.

### Pokalbių užbaigimas

Mokymo ir validacijos duomenys **turi** būti suformatuoti kaip JSON Lines (JSONL) dokumentas. `Phi-3-mini-128k-instruct` pritaikymo duomenų rinkinys turi būti suformatuotas pokalbių formatu, kuris naudojamas Chat completions API.

### Pavyzdinis failo formatas

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Palaikomas failo tipas yra JSON Lines. Failai įkeliami į numatytąją duomenų saugyklą ir tampa prieinami jūsų projekte.

## Phi-3 pritaikymas su Azure AI Foundry

Azure AI Foundry leidžia pritaikyti didelius kalbos modelius pagal jūsų asmeninius duomenų rinkinius naudojant procesą, vadinamą pritaikymu. Pritaikymas suteikia didelę vertę, leidžiant pritaikyti ir optimizuoti modelį specifinėms užduotims ir taikymams. Tai lemia geresnį našumą, mažesnes išlaidas, mažesnį vėlavimą ir pritaikytus rezultatus.

![Finetune AI Foundry](../../../../imgs/03/AIFoundry/AIFoundryfinetune.png)

### Naujo projekto kūrimas

1. Prisijunkite prie [Azure AI Foundry](https://ai.azure.com).

1. Pasirinkite **+New project**, kad sukurtumėte naują projektą Azure AI Foundry.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-new-project.png)

1. Atlikite šiuos veiksmus:

    - Projekto **Hub name**. Jis turi būti unikalus.
    - Pasirinkite **Hub**, kurį norite naudoti (jei reikia, sukurkite naują).

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/create-project.png)

1. Atlikite šiuos veiksmus, kad sukurtumėte naują centrą:

    - Įveskite **Hub name**. Jis turi būti unikalus.
    - Pasirinkite savo Azure **Subscription**.
    - Pasirinkite **Resource group**, kurią norite naudoti (jei reikia, sukurkite naują).
    - Pasirinkite **Location**, kurią norite naudoti.
    - Pasirinkite **Connect Azure AI Services**, kurią norite naudoti (jei reikia, sukurkite naują).
    - Pasirinkite **Connect Azure AI Search**, kad **praleistumėte prijungimą**.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/create-hub.png)

1. Pasirinkite **Next**.
1. Pasirinkite **Create a project**.

### Duomenų paruošimas

Prieš pritaikymą surinkite arba sukurkite duomenų rinkinį, susijusį su jūsų užduotimi, pvz., pokalbių instrukcijas, klausimų-atsakymų poras ar kitus svarbius tekstinius duomenis. Išvalykite ir apdorokite šiuos duomenis, pašalindami triukšmą, tvarkydami trūkstamas reikšmes ir atlikdami teksto tokenizaciją.

### Phi-3 modelių pritaikymas Azure AI Foundry

> [!NOTE]
> Phi-3 modelių pritaikymas šiuo metu palaikomas projektuose, esančiuose East US 2.

1. Kairiajame meniu pasirinkite **Model catalog**.

1. Įveskite *phi-3* į **paieškos laukelį** ir pasirinkite phi-3 modelį, kurį norite naudoti.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-model.png)

1. Pasirinkite **Fine-tune**.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-finetune.png)

1. Įveskite **Fine-tuned model name**.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune1.png)

1. Pasirinkite **Next**.

1. Atlikite šiuos veiksmus:

    - Pasirinkite **task type** kaip **Chat completion**.
    - Pasirinkite **Training data**, kuriuos norite naudoti. Galite juos įkelti per Azure AI Foundry arba iš savo vietinės aplinkos.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune2.png)

1. Pasirinkite **Next**.

1. Įkelkite **Validation data**, kuriuos norite naudoti, arba pasirinkite **Automatic split of training data**.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune3.png)

1. Pasirinkite **Next**.

1. Atlikite šiuos veiksmus:

    - Pasirinkite **Batch size multiplier**, kurį norite naudoti.
    - Pasirinkite **Learning rate**, kurį norite naudoti.
    - Pasirinkite **Epochs**, kurį norite naudoti.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune4.png)

1. Pasirinkite **Submit**, kad pradėtumėte pritaikymo procesą.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-submit.png)

1. Kai jūsų modelis bus pritaikytas, būsena bus rodoma kaip **Completed**, kaip parodyta paveikslėlyje žemiau. Dabar galite modelį diegti ir naudoti savo programoje, žaidimų aikštelėje arba prompt flow. Daugiau informacijos rasite [Kaip diegti Phi-3 šeimos mažus kalbos modelius su Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/completed.png)

> [!NOTE]
> Daugiau informacijos apie Phi-3 pritaikymą rasite [Phi-3 modelių pritaikymas Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Pritaikytų modelių valymas

Galite ištrinti pritaikytą modelį iš pritaikymo modelių sąrašo [Azure AI Foundry](https://ai.azure.com) arba iš modelio detalių puslapio. Pasirinkite pritaikytą modelį, kurį norite ištrinti, pritaikymo puslapyje, tada pasirinkite mygtuką Delete, kad ištrintumėte pritaikytą modelį.

> [!NOTE]
> Negalite ištrinti pritaikyto modelio, jei jis turi esamą diegimą. Pirmiausia turite ištrinti modelio diegimą, kad galėtumėte ištrinti pritaikytą modelį.

## Kaina ir kvotos

### Kainos ir kvotų svarstymai Phi-3 modeliams, pritaikytiems kaip paslauga

Phi modeliai, pritaikyti kaip paslauga, siūlomi Microsoft ir integruoti su Azure AI Foundry naudojimui. Kainas galite rasti [diegiant](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) arba pritaikant modelius, diegimo vedlio skirtuke Pricing and terms.

## Turinys filtravimas

Modeliai, diegiami kaip paslauga su „mokėk už naudojimą“, yra apsaugoti Azure AI Content Safety. Kai jie diegiami realaus laiko galiniuose taškuose, galite atsisakyti šios funkcijos. Su Azure AI turinio saugumu tiek užklausa, tiek atsakymas pereina per klasifikavimo modelių rinkinį, skirtą aptikti ir užkirsti kelią kenksmingo turinio generavimui. Turinio filtravimo sistema aptinka ir imasi veiksmų dėl specifinių potencialiai kenksmingo turinio kategorijų tiek įvesties užklausose, tiek išvesties atsakymuose. Sužinokite daugiau apie [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Pritaikymo konfigūracija**

Hiperparametrai: Nustatykite hiperparametrus, tokius kaip mokymosi greitis, paketų dydis ir mokymo epochų skaičius.

**Nuostolių funkcija**

Pasirinkite tinkamą nuostolių funkciją savo užduočiai (pvz., kryžminė entropija).

**Optimizatorius**

Pasirinkite optimizatorių (pvz., Adam) gradientų atnaujinimui mokymo metu.

**Pritaikymo procesas**

- Įkelkite iš anksto apmokytą modelį: Įkelkite Phi-3 Mini kontrolinį tašką.
- Pridėkite specialius sluoksnius: Pridėkite užduočiai skirtus sluoksnius (pvz., klasifikavimo galvą pokalbių instrukcijoms).

**Modelio mokymas**
Pritaikykite modelį naudodami paruoštą duomenų rinkinį. Stebėkite mokymo eigą ir prireikus koreguokite hiperparametrus.

**Vertinimas ir validacija**

Validacijos rinkinys: Padalinkite savo duomenis į mokymo ir validacijos rinkinius.

**Vertinkite našumą**

Naudokite metrikas, tokias kaip tikslumas, F1 balas ar sudėtingumas, kad įvertintumėte modelio našumą.

## Išsaugokite pritaikytą modelį

**Kontrolinis taškas**
Išsaugokite pritaikytą modelio kontrolinį tašką, kad galėtumėte jį naudoti ateityje.

## Diegimas

- Diegimas kaip internetinė paslauga: Diegkite pritaikytą modelį kaip internetinę paslaugą Azure AI Foundry.
- Testuokite galinį tašką: Siųskite testines užklausas į diegtą galinį tašką, kad patikrintumėte jo funkcionalumą.

## Iteracija ir tobulinimas

Iteracija: Jei našumas nėra patenkinamas, iteruokite koreguodami hiperparametrus, pridėdami daugiau duomenų arba pritaikydami papildomas epochas.

## Stebėjimas ir tobulinimas

Nuolat stebėkite modelio elgesį ir prireikus tobulinkite.

## Pritaikymas ir plėtra

Specialios užduotys: Phi-3 Mini gali būti pritaikytas įvairioms užduotims, neapsiribojant pokalbių instrukcijomis. Tyrinėkite kitus naudojimo atvejus!
Eksperimentavimas: Išbandykite skirtingas architektūras, sluoksnių derinius ir technikas, kad pagerintumėte našumą.

> [!NOTE]
> Pritaikymas yra iteracinis procesas. Eksperimentuokite, mokykitės ir pritaikykite savo modelį, kad pasiektumėte geriausius rezultatus savo specifinei užduočiai!

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.