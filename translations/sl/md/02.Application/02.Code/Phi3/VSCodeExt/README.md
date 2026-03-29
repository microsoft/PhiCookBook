# **Zgradite svoj lasten Visual Studio Code GitHub Copilot Chat z družino Microsoft Phi-3**

Ste že uporabili agent delovnega prostora v GitHub Copilot Chat? Želite zgraditi svojega agenta kode za svojo ekipo? Ta praktična delavnica poskuša združiti odprtokodni model za izgradnjo poslovnega agenta za generiranje kode na podjetniški ravni.

## **Osnove**

### **Zakaj izbrati Microsoft Phi-3**

Phi-3 je družina modelov, ki vključuje phi-3-mini, phi-3-small in phi-3-medium, osnovane na različnih parametrih usposabljanja za generiranje besedila, dokončanje dialoga in generiranje kode. Obstaja tudi phi-3-vision, ki temelji na Vision. Primeren je za podjetja ali različne ekipe za ustvarjanje generativnih AI rešitev brez povezave.

Priporočamo, da preberete ta povezava [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Razširitev GitHub Copilot Chat vam zagotavlja klepetalni vmesnik, ki vam omogoča interakcijo z GitHub Copilotom in prejem odgovore na vprašanja glede programiranja neposredno v VS Code, brez potrebe po brskanju po dokumentaciji ali iskanju po spletnih forumih.

Copilot Chat lahko uporabi označevanje sintakse, zamike in druge oblikovne značilnosti, da izboljša jasnost generiranega odgovora. Glede na vrsto vprašanja uporabnika je rezultat lahko povezan z vsebinami, ki jih je Copilot uporabil pri generiranju odgovora, kot so datoteke izvorne kode ali dokumentacija, ali pa vsebuje gumbe za dostop do funkcionalnosti VS Code.

- Copilot Chat se integrira v vaš razvojni tok in vam nudi pomoč, kjer jo potrebujete:

- Začnite pogovor za klepet neposredno iz urejevalnika ali terminala za pomoč med kodiranjem

- Uporabite pogled Chat, da imate AI asistenta ob strani, ki vam pomaga kadarkoli

- Zaženite Quick Chat, da hitro zastavite vprašanje in se vrnete k svojemu delu

GitHub Copilot Chat lahko uporabljate v različnih situacijah, kot so:

- Odgovarjanje na vprašanja o programiranju, kako najbolje rešiti problem

- Razlaga kode druge osebe in predlogi za izboljšave

- Predlogi popravkov kode

- Generiranje primerov enotnih testov

- Generiranje dokumentacije kode

Priporočamo, da preberete ta povezava [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Reference na **@workspace** v Copilot Chat vam omogočajo, da postavite vprašanja o celotni vaši kodi. Glede na vprašanje Copilot inteligentno poišče ustrezne datoteke in simbole, ki jih nato v odgovoru navede kot povezave in primere kode.

Za odgovor na vaše vprašanje **@workspace** išče po istih virih, kot jih uporabnik uporablja pri navigaciji po kodi v VS Code:

- Vse datoteke v delovnem prostoru, razen tistih, ki jih prezre datoteka .gitignore

- Struktura imenikov z vključenimi podmapami in imeni datotek

- Indeks iskanja kode na GitHubu, če je delovni prostor GitHub repozitorij in indeksiran z iskanjem kode

- Simboli in definicije v delovnem prostoru

- Trenutno izbran tekst ali vidni tekst v aktivnem urejevalniku

Opomba: Datoteka .gitignore je prezrta, če imate odprto datoteko ali izbran tekst znotraj prezrte datoteke.

Priporočamo, da preberete ta povezava [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Več o tej delavnici**

GitHub Copilot je močno izboljšal programersko učinkovitost podjetij, in vsako podjetje upa, da lahko prilagodi relevantne funkcije GitHub Copilota. Mnoga podjetja so prilagodila Razširitve, podobne GitHub Copilotu, na podlagi svojih poslovnih scenarijev in odprtokodnih modelov. Za podjetja so prilagojene Razširitve lažje za nadzor, vendar to vpliva tudi na uporabniško izkušnjo. Navsezadnje ima GitHub Copilot močnejše funkcije za obravnavo splošnih scenarijev in strokovnosti. Če je mogoče ohraniti dosledno izkušnjo, je bolje prilagoditi lastno Razširitev podjetja. GitHub Copilot Chat ponuja relevantna API-jev za podjetja za razširitev izkušnje klepeta. Ohranjanje dosledne izkušnje in imeti prilagojene funkcije je boljša uporabniška izkušnja.

Ta delavnica večinoma uporablja model Phi-3, kombiniran z lokalnim NPU in hibridom Azure, za izdelavo prilagojenega agenta v GitHub Copilot Chat ***@PHI3***, ki pomaga podjetniškim razvijalcem dokončati generiranje kode ***(@PHI3 /gen)*** in generiranje kode na podlagi slik ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/sl/cover.1017ebc9a7c46d09.webp)

### ***Opomba:***

Ta delavnica je trenutno izvedena na AIPC Intel CPU in Apple Silicon. Nadaljevali bomo z nadgradnjo verzije Qualcomm NPU.


## **Delavnica**


| Ime | Opis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Namestitve(✅) | Konfigurirajte in namestite ustrezna okolja ter orodja za namestitev | [Pojdi](./HOL/AIPC/01.Installations.md) |[Pojdi](./HOL/Apple/01.Installations.md) |
| Lab1 - Zaženi Prompt flow s Phi-3-mini (✅) | V kombinaciji z AIPC / Apple Silicon, uporaba lokalnega NPU za ustvarjanje generiranja kode prek Phi-3-mini | [Pojdi](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Pojdi](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Namesti Phi-3-vision na Azure Machine Learning Service(✅) | Generirajte kodo s nameščanjem kataloga modelov Azure Machine Learning Service - Phi-3-vision slike | [Pojdi](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Pojdi](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Ustvari @phi-3 agenta v GitHub Copilot Chat(✅)  | Ustvari prilagojenega phi-3 agenta v GitHub Copilot Chat za dokončanje generiranja kode, generiranje kode grafov, RAG itd. | [Pojdi](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Pojdi](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Vzorec kode (✅)  | Prenesite vzorčno kodo | [Pojdi](../../../../../../../code/07.Lab/01/AIPC) | [Pojdi](../../../../../../../code/07.Lab/01/Apple) |


## **Viri**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Več o GitHub Copilotu [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Več o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Več o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Več o Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Več o Microsoft Foundryjevem Katalogu Modelov [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v izvorni jezik velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne napačne interpretacije ali nesporazume, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->