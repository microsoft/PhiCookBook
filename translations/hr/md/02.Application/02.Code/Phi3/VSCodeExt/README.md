# **Izgradite vlastiti Visual Studio Code GitHub Copilot Chat s Microsoft Phi-3 obitelji**

Jeste li koristili workspace agenta u GitHub Copilot Chatu? Želite li izgraditi vlastitog agenata koda za svoj tim? Ovaj praktični laboratorij se nada kombinirati open source model za izgradnju enterprise razine poslovnog agenata za kodiranje.

## **Osnove**

### **Zašto odabrati Microsoft Phi-3**

Phi-3 je obitelj serija, uključujući phi-3-mini, phi-3-small i phi-3-medium temeljene na različitim parametrima treniranja za generiranje teksta, dovršavanje dijaloga i generiranje koda. Postoji i phi-3-vision temeljen na Visionu. Pogodan je za poduzeća ili različite timove za stvaranje offline generativnih AI rješenja.

Preporučeno za čitanje na ovom linku [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat proširenje pruža vam sučelje chata koje vam omogućuje interakciju s GitHub Copilotom i primanje odgovora na pitanja vezana uz kodiranje direktno unutar VS Code-a, bez potrebe za pregledavanjem dokumentacije ili traženjem na online forumima.

Copilot Chat može koristiti sintaksno isticanje, uvlake i druge funkcionalnosti oblikovanja za veću jasnoću generiranog odgovora. Ovisno o vrsti pitanja korisnika, rezultat može sadržavati poveznice na kontekst koji je Copilot koristio za generiranje odgovora, poput izvornog koda ili dokumentacije, ili gumbe za pristup funkcionalnostima VS Code-a.

- Copilot Chat se uklapa u vaš razvojni tijek i pruža vam pomoć tamo gdje vam treba:

- Pokrenite inline chat razgovor direktno iz editora ili terminala za pomoć dok kodirate

- Koristite Chat prikaz da imate AI asistenta sa strane koji vam može pomoći u bilo kojem trenutku

- Pokrenite Quick Chat za brzo postavljanje pitanja i vraćanje na ono što radite

GitHub Copilot Chat možete koristiti u raznim scenarijima, kao što su:

- Odgovaranje na pitanja o kodiranju kako najbolje riješiti problem

- Objašnjavanje tuđeg koda i predlaganje poboljšanja

- Predlaganje popravaka koda

- Generiranje jedinica testnih slučajeva

- Generiranje dokumentacije koda

Preporučeno za čitanje na ovom linku [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Referenciranje **@workspace** u Copilot Chatu omogućuje vam postavljanje pitanja o cijeloj bazi koda. Na temelju pitanja Copilot inteligentno pronalazi relevantne datoteke i simbole, koje zatim navodi u svom odgovoru kao poveznice i primjere koda.

Za odgovaranje na vaše pitanje, **@workspace** pretražuje iste izvore koje bi programer koristio pri navigaciji bazom koda u VS Code-u:

- Sve datoteke u prostoru za rad, osim datoteka koje su ignorirane putem .gitignore datoteke

- Strukturu direktorija s ugniježđenim imenima mapa i datoteka

- GitHubov kodni indeks pretraživanja, ako je prostor za rad GitHub repozitorij indeksiran kodnim pretraživanjem

- Simbole i definicije u prostoru za rad

- Trenutno odabrani tekst ili vidljivi tekst u aktivnom editoru

Napomena: .gitignore se zaobilazi ako imate otvorenu datoteku ili odabrani tekst unutar ignorirane datoteke.

Preporučeno za čitanje na ovom linku [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Saznajte više o ovom laboratoriju**

GitHub Copilot je znatno poboljšao programersku učinkovitost u poduzećima, a svako poduzeće želi prilagoditi relevantne funkcionalnosti GitHub Copilota. Mnoga poduzeća su prilagodila proširenja slična GitHub Copilotu temeljena na vlastitim poslovnim scenarijima i open source modelima. Za poduzeća su prilagođena proširenja lakša za kontrolu, ali to također može utjecati na korisničko iskustvo. Uostalom, GitHub Copilot ima snažnije funkcije za rješavanje općih scenarija i profesionalnosti. Ako se iskustvo može održavati dosljednim, bilo bi bolje prilagoditi vlastito proširenje poduzeća. GitHub Copilot Chat pruža relevantne API-je za poduzeća kako bi proširila iskustvo chata. Održavanje dosljednog iskustva s prilagođenim funkcijama je bolje korisničko iskustvo.

Ovaj laboratorij koristi uglavnom Phi-3 model u kombinaciji s lokalnim NPU-om i Azure hibridom za izradu prilagođenog Agenta u GitHub Copilot Chatu ***@PHI3*** za pomoć enterprise programerima u dovršavanju generiranja koda***(@PHI3 /gen)*** i generiranju koda na temelju slika ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/hr/cover.1017ebc9a7c46d09.webp)

### ***Napomena:*** 

Ovaj laboratorij je trenutno implementiran na AIPC Intel CPU i Apple Silicon platformama. Nastavit ćemo ažurirati Qualcomm verziju NPU-a.


## **Laboratorij**


| Naziv | Opis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalacije(✅) | Konfiguracija i instalacija povezanih okruženja i alata za instalaciju | [Idi](./HOL/AIPC/01.Installations.md) |[Idi](./HOL/Apple/01.Installations.md) |
| Lab1 - Pokretanje Prompt flow s Phi-3-mini (✅) | Kombinirano s AIPC / Apple Silicon, korištenjem lokalnog NPU-a za stvaranje generiranja koda pomoću Phi-3-mini | [Idi](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Idi](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Postavljanje Phi-3-vision na Azure Machine Learning Service(✅) | Generiranje koda postavljanjem Model Kataloga Azure Machine Learning Service - Phi-3-vision slike | [Idi](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Idi](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Izradite @phi-3 agenta u GitHub Copilot Chatu(✅)  | Izrada vlastitog Phi-3 agenta u GitHub Copilot Chatu za dovršavanje generiranja koda, generiranja koda za grafikone, RAG itd. | [Idi](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Idi](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Primjer Koda (✅)  | Preuzmite primjer koda | [Idi](../../../../../../../code/07.Lab/01/AIPC) | [Idi](../../../../../../../code/07.Lab/01/Apple) |


## **Resursi**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Saznajte više o GitHub Copilotu [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Saznajte više o GitHub Copilot Chatu [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Saznajte više o GitHub Copilot Chat API-ju [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Saznajte više o Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Saznajte više o Microsoft Foundry Model Katalogu [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->