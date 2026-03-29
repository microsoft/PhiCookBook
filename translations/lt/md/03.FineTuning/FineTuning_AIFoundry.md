# Tikslinis Phi-3 pritaikymas su Microsoft Foundry

 Pažvelkime, kaip pritaikyti Microsoft Phi-3 Mini kalbos modelį naudojant Microsoft Foundry. Tikslinis pritaikymas leidžia pritaikyti Phi-3 Mini konkrečioms užduotims, padarant jį dar galingesniu ir jautresniu kontekstui.

## Apsvarstymai

- **Galimybės:** Kokie modeliai yra pritaikomi tiksliniam pritaikymui? Kam bazinis modelis gali būti pritaikytas?
- **Kaina:** Koks yra tikslinio pritaikymo kainų modelis?
- **Priderinamumas:** Kiek galiu modifikuoti bazinį modelį – ir kokiais būdais?
- **Patogumas:** Kaip iš tikrųjų vyksta tikslinis pritaikymas – ar reikia rašyti savą kodą? Ar reikia atsivežti savo skaičiavimo išteklius?
- **Saugumas:** Tiksliai pritaikyti modeliai žinomi, kad turi saugumo rizikų – ar yra įdiegtos apsaugos nuo nepageidaujamos žalos?

![AIFoundry Models](../../../../translated_images/lt/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Paruošimas tiksliniam pritaikymui

### Išankstiniai reikalavimai

> [!NOTE]
> Phi-3 modelių šeimos atveju, mokėjimas pagal naudojimą siūlomas tik su "hub‘ais", sukurtais **East US 2** regionuose.

- Azure prenumerata. Jei neturite Azure prenumeratos, sukurkite [mokamą Azure paskyrą](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) pradžiai.

- [AI Foundry projektas](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure pareigybių pagrindu veikianti prieigos kontrolė (Azure RBAC) naudojama suteikti leidimus operacijoms Microsoft Foundry. Norėdami atlikti šio straipsnio veiksmus, jūsų vartotojo paskyrai turi būti priskirta __Azure AI Developer rolė__ išteklių grupėje.

### Prenumeratos teikėjo registracija

Patikrinkite, ar prenumerata yra registruota prie `Microsoft.Network` išteklių teikėjo.

1. Prisijunkite prie [Azure portalo](https://portal.azure.com).
1. Kairiajame meniu pasirinkite **Subscriptions**.
1. Pasirinkite prenumeratą, kurią norite naudoti.
1. Kairiajame meniu pasirinkite **AI project settings** > **Resource providers**.
1. Patikrinkite, ar sąraše yra **Microsoft.Network**. Jei ne, pridėkite jį.

### Duomenų paruošimas

Paruoškite mokymo ir validavimo duomenis, kad galėtumėte tiksliai pritaikyti modelį. Jūsų mokymo ir validavimo duomenų rinkiniai turi sudaryti įvesčių ir išvesčių pavyzdžius, kaip norite, kad modelis veiktų.

Įsitikinkite, kad visi mokymo pavyzdžiai atitinka numatytą spėjimo formatą. Norint efektyviai tiksliai pritaikyti modelius, užtikrinkite subalansuotą ir įvairialypį duomenų rinkinį.

Tai reiškia duomenų pusiausvyros palaikymą, įvairių scenarijų įtraukimą ir periodišką mokymo duomenų tobulinimą, kad jie atitiktų realaus pasaulio lūkesčius, galutiniame rezultate leidžiant tiksliau ir subalansuotiau atsakyti.

Skirtingi modelių tipai reikalauja skirtingo mokymo duomenų formato.

### Pokalbių užbaigimas

Naudojami mokymo ir validavimo duomenys **privalo** būti suformatuoti kaip JSON Lines (JSONL) dokumentas. `Phi-3-mini-128k-instruct` atveju tikslinio pritaikymo duomenų rinkinys turi būti suformatuotas pokalbio formatu, naudojamu Chat completions API.

### Pavyzdinis failo formatas

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Palaikomas failo tipas yra JSON Lines. Failai įkeliami į numatytąją duomenų saugyklą ir pasiekiami jūsų projekte.

## Tikslinis Phi-3 pritaikymas su Microsoft Foundry

Microsoft Foundry leidžia pritaikyti didelius kalbos modelius prie savo asmeninių duomenų rinkinių naudojant procesą, žinomą kaip tikslinis pritaikymas. Tikslinis pritaikymas suteikia didelę vertę, leidžiant pritaikyti ir optimizuoti modelį specifinėms užduotims ir programoms. Tai pagerina našumą, padidina kaštų efektyvumą, sumažina delsą ir leidžia gauti pritaikytą rezultatą.

![Finetune AI Foundry](../../../../translated_images/lt/AIFoundryfinetune.193aaddce48d553c.webp)

### Sukurti naują projektą

1. Prisijunkite prie [Microsoft Foundry](https://ai.azure.com).

1. Pasirinkite **+New project**, norėdami sukurti naują projektą Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/lt/select-new-project.cd31c0404088d7a3.webp)

1. Atlikite šiuos veiksmus:

    - Projekto **Hub pavadinimas**. Jis turi būti unikalus.
    - Pasirinkite **Hub**, kurį norite naudoti (sukurkite naują, jei reikia).

    ![FineTuneSelect](../../../../translated_images/lt/create-project.ca3b71298b90e420.webp)

1. Atlikite šiuos veiksmus, kad sukurtumėte naują hub'ą:

    - Įveskite **Hub pavadinimą**. Jis turi būti unikalus.
    - Pasirinkite savo Azure **Prenumeratą**.
    - Pasirinkite **Išteklių grupę** (Resource group), kurią norite naudoti (sukurkite naują, jei reikia).
    - Pasirinkite **Vietovę** (Location), kurią norite naudoti.
    - Pasirinkite **Connect Azure AI Services** (prijungti Azure AI paslaugas), jei reikia, sukurkite naują.
    - Pasirinkite **Connect Azure AI Search** ir **Praleiskite prijungimą** (Skip connecting).

    ![FineTuneSelect](../../../../translated_images/lt/create-hub.49e53d235e80779e.webp)

1. Paspauskite **Next**.
1. Paspauskite **Create a project**.

### Duomenų paruošimas

Prieš tikslinį pritaikymą, surinkite arba sukurkite duomenų rinkinį, susijusį su jūsų užduotimi, pavyzdžiui, pokalbių instrukcijas, klausimų-atsakymų poras ar kitus tekstinius duomenis. Išvalykite ir apdorokite šiuos duomenis, pašalindami triukšmą, trūkstamas reikšmes ir tokenizuodami tekstą.

### Tikslinis Phi-3 modelių pritaikymas Microsoft Foundry

> [!NOTE]
> Phi-3 modelių tikslinis pritaikymas šiuo metu palaikomas tik projektuose, esančiuose East US 2 regione.

1. Kairėje pusėje pasirinkite **Model catalog** (modelių katalogas).

1. Įveskite *phi-3* į **paieškos laukelį** ir pasirinkite norimą naudoti phi-3 modelį.

    ![FineTuneSelect](../../../../translated_images/lt/select-model.60ef2d4a6a3cec57.webp)

1. Paspauskite **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/lt/select-finetune.a976213b543dd9d8.webp)

1. Įveskite **Tiksliai pritaikyto modelio pavadinimą**.

    ![FineTuneSelect](../../../../translated_images/lt/finetune1.c2b39463f0d34148.webp)

1. Paspauskite **Next**.

1. Atlikite šiuos veiksmus:

    - Pasirinkite **užduoties tipą** kaip **Chat completion**.
    - Pasirinkite **mokymo duomenis**, kuriuos norite naudoti. Juos galite įkelti per Microsoft Foundry duomenų saugyklą arba iš savo vietinės aplinkos.

    ![FineTuneSelect](../../../../translated_images/lt/finetune2.43cb099b1a94442d.webp)

1. Paspauskite **Next**.

1. Įkelkite norimus naudoti **validavimo duomenis** arba pasirinkite **Automatic split of training data** (automatinis mokymo duomenų skaidymas).

    ![FineTuneSelect](../../../../translated_images/lt/finetune3.fd96121b67dcdd92.webp)

1. Paspauskite **Next**.

1. Atlikite šiuos veiksmus:

    - Pasirinkite norimą **paketo dydžio daugiklį** (Batch size multiplier).
    - Pasirinkite norimą **mokymosi greitį** (Learning rate).
    - Pasirinkite norimą **epokų skaičių** (Epochs).

    ![FineTuneSelect](../../../../translated_images/lt/finetune4.e18b80ffccb5834a.webp)

1. Paspauskite **Submit**, kad pradėtumėte tikslinį pritaikymą.

    ![FineTuneSelect](../../../../translated_images/lt/select-submit.0a3802d581bac271.webp)


1. Kai modelis bus pritaikytas, būsena bus rodoma kaip **Completed**, kaip parodyta žemiau. Dabar galite diegti modelį ir naudoti jį savo programoje, žaidimų aikštelėje ar prompt flow. Daugiau informacijos žr. [Kaip diegti Phi-3 mažus kalbos modelius su Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/lt/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Daugiau informacijos apie Phi-3 tikslinį pritaikymą rasite [Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Ištrinkite savo tiksliai pritaikytus modelius

Galite ištrinti tiksliai pritaikytą modelį iš tikslinio pritaikymo modelių sąrašo [Microsoft Foundry](https://ai.azure.com) arba iš modelio detalių puslapio. Pasirinkite tiksliai pritaikytą modelį iš Fine-tuning puslapio, tada paspauskite mygtuką Delete, kad ištrintumėte modelį.

> [!NOTE]
> Negalite ištrinti vartotojo modelio, jei jam yra esama diegimo instancija. Pirmiausia turite ištrinti modelio diegimą, tada galėsite ištrinti modelį.

## Kaina ir kvotos

### Phi-3 modelių tikslinio pritaikymo kaip paslaugos kaštų ir kvotų apsvarstymai

Phi modeliai, tiksliai pritaikyti kaip paslauga, yra teikiami Microsoft ir integruoti su Microsoft Foundry naudojimui. Kainodarą rasite [diegimo](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) arba tikslinio pritaikymo metu diegimo vedlio skiltyje Kainos ir sąlygos.

## Turinys filtravimas

Modeliai, diegiami kaip paslauga su mokėjimu pagal naudojimą, yra apsaugoti Azure AI Content Safety. Kai juos diegiate realaus laiko galiniuose taškuose, galite pasirinkti atsisakyti šios funkcijos. Įjungus Azure AI turinio saugumą, tiek promptas, tiek atsakymai pereina per klasifikavimo modelių grupę, skirtą aptikti ir užkirsti kelią kenksmingam turiniui. Turinys yra filtruojamas ir kontroliuojamas tam tikrų kategorijų galimai kenksmingo turinio tiek įvesties promptuose, tiek išvesties atsakymuose. Sužinokite daugiau apie [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Tikslinio pritaikymo konfigūracija**

Hipermetrai: Apibrėžkite hipermetrus, tokius kaip mokymosi greitis, paketo dydis ir epochų skaičius.

**Nuostolių funkcija**

Pasirinkite užduočiai tinkamą nuostolių funkciją (pvz., kryžminę entropiją).

**Optimizatorius**

Pasirinkite optimizatorių (pvz., Adam) gradientų atnaujinimams mokymo metu.

**Tikslinio pritaikymo procesas**

- Įkelkite iš anksto apmokytą modelį: įkelkite Phi-3 Mini kontrolinį tašką.
- Pridėkite pasirinktines sluoksnius: pridėkite užduočiai skirtus sluoksnius (pvz., klasifikavimo galvutę pokalbių instrukcijoms).

**Modelio apmokymas**
Tiksliai pritaikykite modelį naudodami paruoštą duomenų rinkinį. Stebėkite mokymosi eigą ir prireikus koreguokite hipermetrus.

**Vertinimas ir validacija**

Validacijos rinkinys: Duomenis pasidalinkite į mokymo ir validacijos rinkinius.

**Našumo vertinimas**

Naudokite metrikas, tokias kaip tikslumas, F1 balas arba painiava, modelio našumui įvertinti.

## Išsaugoti tiksliai pritaikytą modelį

**Kontrolinis taškas**
Išsaugokite tiksliai pritaikyto modelio kontrolinį tašką būsimam naudojimui.

## Diegimas

- Diegimas kaip žiniatinklio paslauga: Įdiekite savo tiksliai pritaikytą modelį kaip žiniatinklio paslaugą Microsoft Foundry.
- Testuokite galinį tašką: Siųskite testinius užklausimus į diegtą galinį tašką, kad patikrintumėte jo funkcionavimą.

## Kartojimas ir tobulinimas

Kartokite: jei našumas nėra patenkinamas, kartokite procesą koreguodami hipermetrus, pridėdami daugiau duomenų arba pratęsdami mokymą dar kelioms epokoms.

## Stebėjimas ir tobulinimas

Nuolat stebėkite modelio elgesį ir tobulinkite jį, kai reikia.

## Pritaikymas ir išplėtimas

Vartotojo užduotys: Phi-3 Mini gali būti tiksliai pritaikytas įvairioms užduotims, ne tik pokalbių instrukcijoms. Ištirkite kitas galimybes!
Eksperimentai: Išbandykite skirtingas architektūras, sluoksnių derinius ir technikas našumui pagerinti.

> [!NOTE]
> Tikslinis pritaikymas yra iteratyvus procesas. Eksperimentuokite, mokykitės ir pritaikykite savo modelį, kad pasiektumėte geriausius rezultatus savo konkrečiai užduočiai!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritatyviu šaltiniu. Kritinė informacija turėtų būti verčiama profesionaliai žmogaus. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, atsirandančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->