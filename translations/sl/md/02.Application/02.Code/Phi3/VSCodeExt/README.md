<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-05-09T19:18:17+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "sl"
}
-->
# **Izdelajte svoj Visual Studio Code GitHub Copilot Chat z Microsoft Phi-3 družino**

Ste že uporabljali workspace agenta v GitHub Copilot Chat? Želite ustvariti svojega agent za kodo za svojo ekipo? Ta praktična delavnica združuje odprtokodni model za izdelavo poslovnega agenta za kodo na ravni podjetja.

## **Osnove**

### **Zakaj izbrati Microsoft Phi-3**

Phi-3 je družina modelov, ki vključuje phi-3-mini, phi-3-small in phi-3-medium, prilagojene različnim parametrom učenja za generiranje besedila, dokončanje dialoga in generiranje kode. Obstaja tudi phi-3-vision, ki temelji na viziji. Primeren je za podjetja ali različne ekipe za ustvarjanje lokalnih rešitev generativne umetne inteligence.

Priporočamo branje te povezave [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Razširitev GitHub Copilot Chat vam ponuja klepetalni vmesnik, s katerim lahko komunicirate z GitHub Copilot in prejmete odgovore na vprašanja, povezana s programiranjem, neposredno v VS Code, brez potrebe po iskanju dokumentacije ali spletnih forumov.

Copilot Chat lahko uporablja označevanje sintakse, zamike in druge oblikovne funkcije za boljšo jasnost generiranih odgovorov. Glede na vrsto vprašanja uporabnika lahko rezultat vsebuje povezave do konteksta, ki ga je Copilot uporabil za generiranje odgovora, kot so izvorne datoteke ali dokumentacija, ali gumbe za dostop do funkcionalnosti VS Code.

- Copilot Chat se integrira v vaš razvojni proces in vam nudi pomoč, kjer jo potrebujete:

- Začnite pogovor v klepetu neposredno iz urejevalnika ali terminala, da dobite pomoč med pisanjem kode

- Uporabite pogled Chat, da imate AI asistenta ob strani, ki vam pomaga kadarkoli

- Zaženite Quick Chat za hitro vprašanje in hitro vrnitev k delu

GitHub Copilot Chat lahko uporabljate v različnih situacijah, na primer:

- Odgovarjanje na vprašanja o programiranju in iskanje najboljših rešitev

- Razlaganje kode drugih in predlaganje izboljšav

- Predlaganje popravkov kode

- Generiranje testnih primerov

- Generiranje dokumentacije kode

Priporočamo branje te povezave [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Uporaba **@workspace** v Copilot Chat vam omogoča, da postavljate vprašanja o celotni vaši kodi. Na podlagi vprašanja Copilot pametno poišče ustrezne datoteke in simbole, ki jih nato v odgovoru prikaže kot povezave in primere kode.

Za odgovor na vaše vprašanje **@workspace** preišče iste vire, kot bi jih razvijalec uporabil pri raziskovanju kode v VS Code:

- Vse datoteke v workspaceu, razen tistih, ki jih ignorira .gitignore datoteka

- Strukturo map z vključenimi podmapami in imeni datotek

- GitHubov indeks iskanja kode, če je workspace GitHub repozitorij in je indeksiran

- Simbole in definicije v workspaceu

- Trenutno izbran ali viden tekst v aktivnem urejevalniku

Opomba: .gitignore se prezre, če imate odprto datoteko ali izbran tekst znotraj ignorirane datoteke.

Priporočamo branje te povezave [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Več o tej delavnici**

GitHub Copilot je močno izboljšal učinkovitost programiranja v podjetjih, vsako podjetje pa želi prilagoditi funkcije GitHub Copilot svojim potrebam. Mnoge organizacije so na podlagi svojih poslovnih scenarijev in odprtokodnih modelov prilagodile razširitve, podobne GitHub Copilot. Za podjetja so prilagojene razširitve lažje za nadzor, vendar to lahko vpliva na uporabniško izkušnjo. GitHub Copilot ima namreč močnejše funkcije za splošne scenarije in strokovnost. Če je mogoče ohraniti enotno izkušnjo, je bolje prilagoditi lastno razširitev podjetja. GitHub Copilot Chat ponuja API-je za podjetja, da razširijo izkušnjo klepeta. Ohranjanje dosledne izkušnje in prilagojenih funkcij zagotavlja boljšo uporabniško izkušnjo.

Ta delavnica uporablja Phi-3 model v kombinaciji z lokalnim NPU in Azure hibridom za izdelavo prilagojenega agenta v GitHub Copilot Chat ***@PHI3***, ki pomaga razvijalcem v podjetju pri generiranju kode***(@PHI3 /gen)*** in generiranju kode na podlagi slik ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.sl.png)

### ***Opomba:*** 

Ta delavnica je trenutno izvedena na AIPC Intel CPU in Apple Silicon. Nadaljevali bomo z nadgradnjami za Qualcomm različico NPU.

## **Delavnica**

| Ime | Opis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Namestitve(✅) | Konfiguracija in namestitev okolij ter namestitvenih orodij | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Zagon Prompt flow s Phi-3-mini (✅) | V kombinaciji z AIPC / Apple Silicon, uporaba lokalnega NPU za generiranje kode preko Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Namestitev Phi-3-vision na Azure Machine Learning Service(✅) | Generiranje kode z namestitvijo Model Catalog - Phi-3-vision slike v Azure Machine Learning Service | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Ustvarjanje @phi-3 agenta v GitHub Copilot Chat(✅)  | Ustvarite prilagojen Phi-3 agent v GitHub Copilot Chat za dokončanje generiranja kode, generiranje kode grafov, RAG itd. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Vzorec kode (✅)  | Prenesite vzorec kode | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **Viri**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Več o GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Več o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Več o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Več o Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Več o Azure AI Foundry Model Catalog [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.