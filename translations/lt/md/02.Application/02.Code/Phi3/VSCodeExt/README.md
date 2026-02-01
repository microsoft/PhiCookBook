# **Sukurkite savo Visual Studio Code GitHub Copilot Chat su Microsoft Phi-3 šeima**

Ar jau naudojote darbo srities agentą GitHub Copilot Chat? Norite sukurti savo komandos kodo agentą? Ši praktinė laboratorija siekia sujungti atvirojo kodo modelį, kad būtų sukurtas įmonės lygio kodo verslo agentas.

## **Pagrindai**

### **Kodėl verta rinktis Microsoft Phi-3**

Phi-3 yra šeimos serija, apimanti phi-3-mini, phi-3-small ir phi-3-medium, pagrįsta skirtingais mokymo parametrais tekstų generavimui, dialogų užbaigimui ir kodo generavimui. Taip pat yra phi-3-vision, pagrįstas Vision. Jis tinkamas įmonėms ar skirtingoms komandoms kurti neprisijungusius generatyvios AI sprendimus.

Rekomenduojama perskaityti šią nuorodą [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat plėtinys suteikia pokalbių sąsają, leidžiančią bendrauti su GitHub Copilot ir gauti atsakymus į su kodavimu susijusius klausimus tiesiogiai VS Code aplinkoje, nereikalaujant naršyti dokumentacijoje ar ieškoti atsakymų interneto forumuose.

Copilot Chat gali naudoti sintaksės paryškinimą, įtrauką ir kitas formatavimo funkcijas, kad atsakymai būtų aiškesni. Atsižvelgiant į vartotojo klausimo tipą, rezultatas gali apimti nuorodas į kontekstą, kurį Copilot naudojo atsakymui generuoti, pvz., šaltinio kodo failus ar dokumentaciją, arba mygtukus, leidžiančius pasiekti VS Code funkcionalumą.

- Copilot Chat integruojasi į jūsų kūrėjo darbo eigą ir teikia pagalbą ten, kur jos reikia:

- Pradėkite pokalbį tiesiogiai iš redaktoriaus ar terminalo, kad gautumėte pagalbą kodavimo metu

- Naudokite pokalbių peržiūrą, kad turėtumėte AI asistentą šalia bet kuriuo metu

- Paleiskite greitą pokalbį, kad užduotumėte trumpą klausimą ir grįžtumėte prie savo darbo

GitHub Copilot Chat galite naudoti įvairiose situacijose, tokiose kaip:

- Atsakymai į kodavimo klausimus, kaip geriausiai išspręsti problemą

- Kito žmogaus kodo paaiškinimas ir patobulinimų siūlymas

- Kodo taisymų siūlymas

- Vienetinių testų generavimas

- Kodo dokumentacijos generavimas

Rekomenduojama perskaityti šią nuorodą [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


### **Microsoft GitHub Copilot Chat @workspace**

Naudojant **@workspace** Copilot Chat, galite užduoti klausimus apie visą savo kodų bazę. Atsižvelgiant į klausimą, Copilot protingai surenka atitinkamus failus ir simbolius, kuriuos jis naudoja atsakyme kaip nuorodas ir kodo pavyzdžius.

Norėdamas atsakyti į jūsų klausimą, **@workspace** ieško tų pačių šaltinių, kuriuos kūrėjas naudotų naršydamas kodų bazę VS Code:

- Visi failai darbo srityje, išskyrus tuos, kurie ignoruojami .gitignore faile

- Katalogo struktūra su įdėtais aplankais ir failų pavadinimais

- GitHub kodo paieškos indeksas, jei darbo sritis yra GitHub saugykla ir indeksuota kodo paieškoje

- Simboliai ir apibrėžimai darbo srityje

- Šiuo metu pasirinktas tekstas arba matomas tekstas aktyviame redaktoriuje

Pastaba: .gitignore yra apeinamas, jei turite atidarytą failą arba pasirinkote tekstą ignoruojamame faile.

Rekomenduojama perskaityti šią nuorodą [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Sužinokite daugiau apie šią laboratoriją**

GitHub Copilot labai pagerino įmonių programavimo efektyvumą, ir kiekviena įmonė tikisi pritaikyti GitHub Copilot susijusias funkcijas. Daugelis įmonių pritaikė plėtinius, panašius į GitHub Copilot, remdamiesi savo verslo scenarijais ir atvirojo kodo modeliais. Įmonėms pritaikyti plėtiniai yra lengviau valdomi, tačiau tai taip pat veikia vartotojo patirtį. Juk GitHub Copilot turi stipresnes funkcijas sprendžiant bendrus scenarijus ir profesionalumą. Jei patirtis gali būti išlaikyta nuosekli, būtų geriau pritaikyti įmonės plėtinį. GitHub Copilot Chat teikia atitinkamus API, kad įmonės galėtų plėsti pokalbių patirtį. Išlaikyti nuoseklią patirtį ir turėti pritaikytas funkcijas yra geresnė vartotojo patirtis.

Ši laboratorija daugiausia naudoja Phi-3 modelį, derinamą su vietiniu NPU ir Azure hibridu, kad sukurtų pritaikytą agentą GitHub Copilot Chat ***@PHI3***, kuris padėtų įmonių kūrėjams atlikti kodo generavimą ***(@PHI3 /gen)*** ir generuoti kodą pagal vaizdus ***(@PHI3 /img)***.

![PHI3](../../../../../../../imgs/02/vscodeext/cover.png)

### ***Pastaba:*** 

Ši laboratorija šiuo metu įgyvendinama Intel CPU ir Apple Silicon AIPC. Mes toliau atnaujinsime Qualcomm NPU versiją.


## **Laboratorija**


| Pavadinimas | Aprašymas | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Įdiegimai(✅) | Konfigūruokite ir įdiekite susijusias aplinkas ir įrankius | [Eiti](./HOL/AIPC/01.Installations.md) |[Eiti](./HOL/Apple/01.Installations.md) |
| Lab1 - Paleiskite Prompt flow su Phi-3-mini (✅) | Derinant su AIPC / Apple Silicon, naudojant vietinį NPU, sukurkite kodo generavimą per Phi-3-mini | [Eiti](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Eiti](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Diegti Phi-3-vision Azure Machine Learning Service(✅) | Generuokite kodą diegdami Azure Machine Learning Service Model Catalog - Phi-3-vision vaizdą | [Eiti](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Eiti](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Sukurkite @phi-3 agentą GitHub Copilot Chat(✅)  | Sukurkite pritaikytą Phi-3 agentą GitHub Copilot Chat, kad atliktumėte kodo generavimą, grafų generavimą, RAG ir kt. | [Eiti](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Eiti](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Pavyzdinis kodas (✅)  | Atsisiųskite pavyzdinį kodą | [Eiti](../../../../../../../code/07.Lab/01/AIPC) | [Eiti](../../../../../../../code/07.Lab/01/Apple) |


## **Ištekliai**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Sužinokite daugiau apie GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Sužinokite daugiau apie GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Sužinokite daugiau apie GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Sužinokite daugiau apie Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Sužinokite daugiau apie Azure AI Foundry Model Catalog [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.