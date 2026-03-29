# **Uporaba Phi-3 v Microsoft Foundry**

Z razvojem Generativne umetne inteligence upamo, da bomo z uporabo enotne platforme upravljali različne LLM in SLM, integracijo podatkov podjetij, fino prilagajanje/RAG operacije in ocenjevanje različnih podjetniških poslov po integraciji LLM in SLM itd., tako da bodo generativne AI Smart aplikacije bolje izvedene. [Microsoft Foundry](https://ai.azure.com) je podjetniška platforma za aplikacije generativne umetne inteligence.

![aistudo](../../../../translated_images/sl/aifoundry_home.f28a8127c96c7d93.webp)

Z Microsoft Foundry lahko ocenjujete odzive velikih jezikovnih modelov (LLM) in orkestrirate komponente aplikacij s spodbudami z uporabo prompt flow za boljše zmogljivosti. Platforma omogoča skalabilnost za preobrazbo dokazov koncepta v polnopravno produkcijo z lahkoto. Neprestano spremljanje in izboljšave podpirajo dolgoročni uspeh.

Model Phi-3 lahko hitro namestimo na Microsoft Foundry z nekaj preprostimi koraki, nato pa uporabimo Microsoft Foundry za dokončanje projektov, kot so Playground/Chat, fino prilagajanje, ocenjevanje in drugo, povezano s Phi-3.

## **1. Priprava**

Če imate na svojem računalniku že nameščen [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo), je uporaba te predloge enostavna kot zagon ukaza v novi mapi.

## Ročna ustvaritev

Ustvarjanje projekta in vozlišča v Microsoft Foundry je odličen način za organizacijo in upravljanje vašega AI dela. Tukaj je korak-po-korak vodič, da začnete:

### Ustvarjanje projekta v Microsoft Foundry

1. **Pojdite na Microsoft Foundry**: Prijavite se v portal Microsoft Foundry.
2. **Ustvarite projekt**:
   - Če že ste v projektu, izberite "Microsoft Foundry" zgoraj levo na strani, da se vrnete na domačo stran.
   - Izberite "+ Create project".
   - Vnesite ime projekta.
   - Če imate vozlišče, bo izbrano privzeto. Če imate dostop do več vozlišč, lahko izberete drugo iz spustnega menija. Če želite ustvariti novo vozlišče, izberite "Create new hub" in vnesite ime.
   - Izberite "Create".

### Ustvarjanje vozlišča v Microsoft Foundry

1. **Pojdite na Microsoft Foundry**: Prijavite se z vašim Azure računom.
2. **Ustvarite vozlišče**:
   - Izberite Upravljanje iz levega menija.
   - Izberite "All resources", nato puščico navzdol poleg "+ New project" in izberite "+ New hub".
   - V pogovornem oknu "Create a new hub" vnesite ime svojega vozlišča (npr. contoso-hub) in spremenite ostala polja po želji.
   - Izberite "Next", pregledajte informacije in nato izberite "Create".

Za podrobnejša navodila lahko pogledate uradno [Microsoftovo dokumentacijo](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Po uspešni ustvaritvi lahko dostopate do studia, ki ste ga ustvarili, preko [ai.azure.com](https://ai.azure.com/)

Na enem AI Foundry-ju je lahko več projektov. Ustvarite projekt v AI Foundry za pripravo.

Ustvarite Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Namestitev modela Phi v Microsoft Foundry**

Kliknite na možnost Explore projekta, da vstopite v Model Catalog in izberete Phi-3

Izberite Phi-3-mini-4k-instruct

Kliknite 'Deploy' za namestitev modela Phi-3-mini-4k-instruct

> [!NOTE]
>
> Pri nameščanju lahko izberete računsko moč

## **3. Playground Chat Phi v Microsoft Foundry**

Pojdite na stran za nameščanje, izberite Playground in klepetajte s Phi-3 v Microsoft Foundry

## **4. Namestitev modela iz Microsoft Foundry**

Za namestitev modela iz Azure Model Catalog sledite tem korakom:

- Prijavite se v Microsoft Foundry.
- Izberite model, ki ga želite namestiti, iz modelnega kataloga Microsoft Foundry.
- Na strani z informacijami o modelu izberite Deploy, nato izberite Serverless API z Azure AI Content Safety.
- Izberite projekt, v katerega želite namestiti model. Za uporabo ponudbe Serverless API mora vaše delovno okolje pripadati regiji East US 2 ali Sweden Central. Lahko prilagodite ime nameščanja.
- Na čarovniku za nameščanje izberite Cene in pogoje, da se seznanite s cenami in pogoji uporabe.
- Izberite Deploy. Počakajte, da je namestitev pripravljena in da ste preusmerjeni na stran z namestitvami.
- Izberite Odpri v playgroundu, da začnete interakcijo z modelom.
- Lahko se vrnete na stran z namestitvami, izberete namestitev in zabeležite cilj URL končne točke in skrivni ključ, ki ju lahko uporabite za klic namestitve in generiranje rezultatov.
- Podatke o končni točki, URL in dostopne ključe lahko vedno najdete v zavihku Build, kjer izberete Deployments iz sekcije Components.

> [!NOTE]
> Upoštevajte, da mora imeti vaš račun dovoljenja za vlogo Azure AI Developer v Skupini virov, da lahko izvedete te korake.

## **5. Uporaba Phi API v Microsoft Foundry**

Dostopate lahko do https://{Ime vašega projekta}.region.inference.ml.azure.com/swagger.json preko Get zahteve v Postman-u in ga kombinirate s ključi, da spoznate ponujene vmesnike

Zelo priročno lahko pridobite parametre zahtevka kot tudi parametre odziva.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->