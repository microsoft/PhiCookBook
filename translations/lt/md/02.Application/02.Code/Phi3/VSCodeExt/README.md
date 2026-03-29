# **Sukurkite savo Visual Studio Code GitHub Copilot Chat su Microsoft Phi-3 šeima**

Ar naudojote darbo vietos agentą GitHub Copilot Chat? Ar norite sukurti savo komandos kodo agentą? Šis praktinis užsiėmimas siekia sujungti atvirojo kodo modelį, kad būtų sukurtas įmonės lygio kodo verslo agentas.

## **Pagrindai**

### **Kodėl pasirinkti Microsoft Phi-3**

Phi-3 yra šeimos serija, įskaitant phi-3-mini, phi-3-small ir phi-3-medium, paremtus skirtingais mokymo parametrais teksto generavimui, dialogų užbaigimui ir kodo generavimui. Taip pat yra phi-3-vision, paremta Vision. Tai tinka įmonėms arba skirtingoms komandoms kurti neprisijungusias generatyvios AI sprendimų versijas.

Rekomenduojama perskaityti šią nuorodą [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat plėtinys suteikia jums pokalbių sąsają, leidžiančią bendrauti su GitHub Copilot ir gauti atsakymus į su programavimu susijusius klausimus tiesiai VS Code aplinkoje, nereikalaujant naršyti dokumentacijos ar ieškoti internete forumuose.

Copilot Chat gali naudoti sintaksės paryškinimą, įtrauką ir kitas formatavimo funkcijas, siekdamas aiškiau pateikti generuotą atsakymą. Priklausomai nuo vartotojo klausimo tipo, rezultatas gali turėti nuorodų į kontekstą, kurį Copilot naudojo generuodamas atsakymą, pavyzdžiui, programinio kodo failus ar dokumentaciją, arba mygtukus prieigai prie VS Code funkcionalumo.

- Copilot Chat integruojasi į jūsų kūrėjo srautus ir teikia pagalbą ten, kur jos reikia:

- Pradėkite pokalbių pokalbį tiesiogiai iš redaktoriaus arba terminalo, norėdami gauti pagalbą programuojant

- Naudokite Chat rodinį, kad bet kada turėtumėte AI asistentą šone

- Paleiskite Quick Chat, kad užduotumėte greitą klausimą ir grįžtumėte prie savo darbo

GitHub Copilot Chat galite naudoti įvairiose situacijose, tokiose kaip:

- Atsakyti į programavimo klausimus, kaip geriausiai išspręsti problemą

- Paaiškinti kieno nors kito kodą ir pasiūlyti tobulinimus

- Siūlyti kodo pataisas

- Generuoti vienetinių testų atvejus

- Generuoti kodo dokumentaciją

Rekomenduojama perskaityti šią nuorodą [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Naudojant **@workspace** Copilot Chat galite užduoti klausimus apie visą savo kodo bazę. Atsižvelgiant į klausimą, Copilot protingai suranda atitinkamus failus ir simbolius, kuriuos vėliau nurodo savo atsakyme kaip nuorodas ir kodo pavyzdžius.

Norėdamas atsakyti į jūsų klausimą, **@workspace** ieško tose pačiose šaltiniuose, kuriuos kūrėjas naudotų naršydamas kodo bazę VS Code:

- Visi failai darbo vietoje, išskyrus tuos, kurie yra ignoruojami pagal .gitignore failą

- Katalogų struktūra su įdėtais aplankais ir failų pavadinimais

- GitHub kodo paieškos indeksas, jei darbo vieta yra GitHub saugykla ir indeksuota kodo paieška

- Simboliai ir apibrėžimai darbo vietoje

- Šiuo metu pažymėtas tekstas arba matomas tekstas aktyviame redaktoriuje

Pastaba: .gitignore yra apeinamas, jei atvėrėte failą arba pažymėjote tekstą ignoruojamame faile.

Rekomenduojama perskaityti šią nuorodą [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Sužinokite daugiau apie šį laboratorinį darbą**

GitHub Copilot labai pagerino įmonių programavimo efektyvumą, ir kiekviena įmonė siekia pritaikyti atitinkamas GitHub Copilot funkcijas pagal savo poreikius. Daugelis įmonių yra sukūrusios pritaikytus plėtinius, panašius į GitHub Copilot, remdamiesi savo verslo scenarijais ir atvirojo kodo modeliais. Įmonėms pritaikyti plėtiniai yra lengviau valdomi, bet tai taip pat veikia vartotojo patirtį. Visgi GitHub Copilot turi stipresnes funkcijas bendrų scenarijų ir profesionalumo srityse. Jei patirtis gali būti nuosekli, būtų geriau pritaikyti įmonės savą plėtinį. GitHub Copilot Chat suteikia įmonėms atitinkamus API, kad plečiamų pokalbių patirtį. Išlaikyti nuoseklią patirtį ir turėti pritaikytas funkcijas – tai geresnė vartotojo patirtis.

Ši laboratorija daugiausia naudoja Phi-3 modelį, derinant vietinį NPU ir Azure hibridą, kad būtų sukurtas pritaikytas agentas GitHub Copilot Chat ***@PHI3***, padedantis įmonių kūrėjams pabaigti kodo generavimą ***(@PHI3 /gen)*** bei generuoti kodą pagal paveikslėlius ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/lt/cover.1017ebc9a7c46d09.webp)

### ***Pastaba:***

Šis laboratorinis darbas šiuo metu įgyvendinamas Intel CPU ir Apple Silicon AIPC. Toliau bus atnaujinama Qualcomm versija su NPU.


## **Laboratorija**


| Pavadinimas | Aprašymas | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Įdiegimas(✅) | Konfigūruoti ir įdiegti susijusias aplinkas ir įdiegimo įrankius | [Eiti](./HOL/AIPC/01.Installations.md) |[Eiti](./HOL/Apple/01.Installations.md) |
| Lab1 - Paleisti užklausų srautą su Phi-3-mini (✅) | Derinant su AIPC / Apple Silicon naudoti vietinį NPU generuojant kodą per Phi-3-mini | [Eiti](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Eiti](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Diegti Phi-3-vision Azure Machine Learning Service aplinkoje(✅) | Generuoti kodą diegiant Azure Machine Learning Service modelių katalogą - Phi-3-vision vaizdą | [Eiti](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Eiti](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Sukurti @phi-3 agentą GitHub Copilot Chat aplinkoje(✅)  | Sukurti pritaikytą Phi-3 agentą GitHub Copilot Chat, kad užbaigtų kodo generavimą, grafų generavimą, RAG ir kt. | [Eiti](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Eiti](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Pavyzdinis kodas (✅)  | Atsisiųsti pavyzdinį kodą | [Eiti](../../../../../../../code/07.Lab/01/AIPC) | [Eiti](../../../../../../../code/07.Lab/01/Apple) |


## **Ištekliai**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Sužinokite daugiau apie GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Sužinokite daugiau apie GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Sužinokite daugiau apie GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Sužinokite daugiau apie Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Sužinokite daugiau apie Microsoft Foundry modelių katalogą [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->