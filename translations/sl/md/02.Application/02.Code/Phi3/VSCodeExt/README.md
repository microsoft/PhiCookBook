<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:46:14+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "sl"
}
-->
# **Zgradi svoj Visual Studio Code GitHub Copilot Chat z družino Microsoft Phi-3**

Si že uporabljal agenta delovnega prostora v GitHub Copilot Chat? Želiš zgraditi svojega agenta za kodo za svojo ekipo? Ta praktični laboratorij združuje odprtokodni model za izdelavo poslovnega agenta za kodo na ravni podjetja.

## **Osnove**

### **Zakaj izbrati Microsoft Phi-3**

Phi-3 je družina modelov, ki vključuje phi-3-mini, phi-3-small in phi-3-medium, ki temeljijo na različnih parametrih učenja za generiranje besedila, dokončanje dialoga in generiranje kode. Obstaja tudi phi-3-vision, ki temelji na Vision. Primeren je za podjetja ali različne ekipe za ustvarjanje generativnih AI rešitev brez povezave.

Priporočamo branje te povezave [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Razširitev GitHub Copilot Chat ti omogoča klepetalni vmesnik, s katerim lahko komuniciraš z GitHub Copilot in prejemaš odgovore na vprašanja, povezana s programiranjem, neposredno v VS Code, brez potrebe po iskanju dokumentacije ali spletnih forumov.

Copilot Chat lahko uporablja označevanje sintakse, zamike in druge oblikovne elemente, da izboljša jasnost generiranih odgovorov. Glede na vrsto vprašanja uporabnika lahko rezultat vsebuje povezave do konteksta, ki ga je Copilot uporabil za generiranje odgovora, kot so datoteke izvorne kode ali dokumentacija, ali gumbe za dostop do funkcionalnosti VS Code.

- Copilot Chat se integrira v tvoj razvojni potek in ti nudi pomoč, kjer jo potrebuješ:

- Začni klepetalni pogovor neposredno iz urejevalnika ali terminala za pomoč med kodiranjem

- Uporabi pogled Chat, da imaš AI asistenta ob strani, ki ti lahko pomaga kadarkoli

- Zaženi Quick Chat za hitro vprašanje in se hitro vrni k delu

GitHub Copilot Chat lahko uporabljaš v različnih situacijah, kot so:

- Odgovarjanje na vprašanja o programiranju, kako najbolje rešiti problem

- Razlaga kode drugih in predlaganje izboljšav

- Predlaganje popravkov kode

- Generiranje enotnih testnih primerov

- Generiranje dokumentacije kode

Priporočamo branje te povezave [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Uporaba **@workspace** v Copilot Chat ti omogoča, da postaviš vprašanja o celotni kodi v tvojem delovnem prostoru. Na podlagi vprašanja Copilot inteligentno poišče ustrezne datoteke in simbole, ki jih nato v odgovoru prikaže kot povezave in primere kode.

Za odgovor na tvoje vprašanje **@workspace** preišče iste vire, kot bi jih razvijalec uporabil pri navigaciji po kodi v VS Code:

- Vse datoteke v delovnem prostoru, razen tistih, ki so izključene z datoteko .gitignore

- Strukturo imenikov z gnezdenimi mapami in imeni datotek

- Indeks iskanja kode GitHub, če je delovni prostor GitHub repozitorij in je indeksiran z iskanjem kode

- Simbole in definicije v delovnem prostoru

- Trenutno izbran ali viden tekst v aktivnem urejevalniku

Opomba: .gitignore se prezre, če imaš odprto datoteko ali izbran tekst znotraj izključene datoteke.

Priporočamo branje te povezave [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Več o tem laboratoriju**

GitHub Copilot je močno izboljšal učinkovitost programiranja v podjetjih, vsako podjetje pa si želi prilagoditi ustrezne funkcije GitHub Copilot. Mnoga podjetja so na podlagi svojih poslovnih scenarijev in odprtokodnih modelov prilagodila razširitve, podobne GitHub Copilot. Za podjetja so prilagojene razširitve lažje za nadzor, vendar to vpliva tudi na uporabniško izkušnjo. GitHub Copilot ima namreč močnejše funkcije za splošne scenarije in strokovnost. Če je mogoče ohraniti dosledno izkušnjo, je bolje prilagoditi lastno razširitev podjetja. GitHub Copilot Chat ponuja ustrezne API-je za podjetja, da razširijo izkušnjo klepeta. Ohranjanje dosledne izkušnje in hkrati prilagojene funkcije je boljša uporabniška izkušnja.

Ta laboratorij uporablja model Phi-3 v kombinaciji z lokalnim NPU in Azure hibridom za izdelavo prilagojenega agenta v GitHub Copilot Chat ***@PHI3***, ki pomaga razvijalcem v podjetju pri dokončanju generiranja kode ***(@PHI3 /gen)*** in generiranju kode na podlagi slik ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d09.sl.png)

### ***Opomba:***

Ta laboratorij je trenutno izveden na AIPC Intel CPU in Apple Silicon. Nadaljevali bomo z nadgradnjo različice Qualcomm NPU.

## **Laboratorij**

| Ime | Opis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Namestitve(✅) | Konfiguracija in namestitev povezanih okolij in namestitvenih orodij | [Pojdi](./HOL/AIPC/01.Installations.md) |[Pojdi](./HOL/Apple/01.Installations.md) |
| Lab1 - Zagon Prompt flow s Phi-3-mini (✅) | V kombinaciji z AIPC / Apple Silicon, uporaba lokalnega NPU za ustvarjanje generiranja kode preko Phi-3-mini | [Pojdi](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Pojdi](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Namestitev Phi-3-vision na Azure Machine Learning Service(✅) | Generiranje kode z namestitvijo Model Catalog Azure Machine Learning Service - Phi-3-vision image | [Pojdi](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Pojdi](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Ustvari @phi-3 agenta v GitHub Copilot Chat(✅)  | Ustvari prilagojenega Phi-3 agenta v GitHub Copilot Chat za dokončanje generiranja kode, generiranje grafične kode, RAG itd. | [Pojdi](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Pojdi](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Vzorec kode (✅)  | Prenesi vzorec kode | [Pojdi](../../../../../../../code/07.Lab/01/AIPC) | [Pojdi](../../../../../../../code/07.Lab/01/Apple) |

## **Viri**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Več o GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Več o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Več o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Več o Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Več o Model Catalog Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.