# Nastavitev Phi-3 z Microsoft Foundry

 Raziščimo, kako lahko nastavimo Microsoftov jezikovni model Phi-3 Mini z uporabo Microsoft Foundry. Nastavitev omogoča prilagoditev Phi-3 Mini za določena opravila, zaradi česar je še močnejši in bolj prilagojen kontekstu.

## Premisleki

- **Zmožnosti:** Kateri modeli so nastavljivi? Kaj lahko osnovni model naredi po nastavitvi?
- **Stroški:** Kakšen je cenovni model za nastavitev
- **Prilagodljivost:** Koliko lahko spremenim osnovni model – in na katere načine?
- **Udobje:** Kako poteka nastavitev – ali moram pisati lasten kodo? Ali moram prinesti lastne računske vire?
- **Varnost:** Nastavljeni modeli so znani po varnostnih tveganjih – ali obstajajo varovalke za zaščito pred nenamernimi škodami?

![AIFoundry Models](../../../../translated_images/sl/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Priprava za nastavitev

### Predpogoji

> [!NOTE]
> Za modele družine Phi-3 je ponudba nastavitve po modelu plačaj-po-porabi na voljo le z vozlišči ustvarjenimi v regijah **East US 2**.

- Naročnina Azure. Če še nimate naročnine Azure, ustvarite [plačljiv Azure račun](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go), da začnete.

- [AI Foundry projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure nadzor dostopa na podlagi vlog (Azure RBAC) se uporablja za dodeljevanje dostopa do operacij v Microsoft Foundry. Za izvedbo korakov v tem članku mora vaši uporabniški račun imeti dodeljeno vlogo __Azure AI Developer__ v skupini virov.

### Registracija ponudnika naročnine

Preverite, ali je naročnina registrirana pri ponudniku virov `Microsoft.Network`.

1. Prijavite se v [Azure portal](https://portal.azure.com).
1. Izberite **Naročnine** v levem meniju.
1. Izberite naročnino, ki jo želite uporabljati.
1. Izberite **Nastavitve AI projekta** > **Ponudniki virov** v levem meniju.
1. Potrdite, da je **Microsoft.Network** na seznamu ponudnikov virov. Če ga ni, ga dodajte.

### Priprava podatkov

Pripravite svoje učne in validacijske podatke za nastavitev modela. Vaši podatki za učenje in validacijo vsebujejo primere vhodov in izhodov, kako želite, da model deluje.

Poskrbite, da vsi vaši učni primeri sledijo pričakovani obliki za inferenco. Za učinkovito nastavitev modelov zagotovite uravnotežen in raznolik niz podatkov.

To vključuje ohranjanje ravnotežja podatkov, vključevanje raznih scenarijev in občasno izboljševanje učnih podatkov, da se uskladijo s pričakovanji resničnega sveta, kar vodi do natančnejših in bolj uravnoteženih odzivov modela.

Različni tipi modelov zahtevajo drugačno obliko učnih podatkov.

### Chat Completion

Učni in validacijski podatki, ki jih uporabljate, **morajo** biti formatirani kot JSON Lines (JSONL) dokument. Za `Phi-3-mini-128k-instruct` mora biti niz podatkov za nastavitev formatiran v pogovornem formatu, ki ga uporablja API za zaključevalne pogovore.

### Primer formata datoteke

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Podprta vrsta datoteke je JSON Lines. Datoteke se naložijo v privzeti shrambi podatkov in so na voljo v vašem projektu.

## Nastavitev Phi-3 z Microsoft Foundry

Microsoft Foundry omogoča prilagajanje velikih jezikovnih modelov na osebne podatkovne množice z uporabo procesa, znanega kot nastavitev. Nastavitev prinaša veliko vrednost z omogočanjem prilagoditve in optimizacije za specifična opravila in aplikacije. To vodi do izboljšane zmogljivosti, stroškovne učinkovitosti, znižane zakasnitve in prilagojenih rezultatov.

![Finetune AI Foundry](../../../../translated_images/sl/AIFoundryfinetune.193aaddce48d553c.webp)

### Ustvarjanje novega projekta

1. Prijavite se v [Microsoft Foundry](https://ai.azure.com).

1. Izberite **+New project**, da ustvarite nov projekt v Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/sl/select-new-project.cd31c0404088d7a3.webp)

1. Izvedite naslednje naloge:

    - Ime projekta (Hub name). Mora biti edinstvena vrednost.
    - Izberite **Hub**, ki ga boste uporabljali (po potrebi ustvarite novega).

    ![FineTuneSelect](../../../../translated_images/sl/create-project.ca3b71298b90e420.webp)

1. Izvedite naslednje korake za ustvarjanje novega vozlišča (huba):

    - Vnesite **Ime huba**. Mora biti edinstvena vrednost.
    - Izberite svojo Azure **naročnino**.
    - Izberite **Skupino virov**, ki jo boste uporabljali (po potrebi ustvarite novo).
    - Izberite **Lokacijo**, ki jo želite uporabljati.
    - Izberite **Connect Azure AI Services**, ki jih boste uporabljali (po potrebi ustvarite nove).
    - Izberite **Connect Azure AI Search** na **Preskoči povezovanje**.

    ![FineTuneSelect](../../../../translated_images/sl/create-hub.49e53d235e80779e.webp)

1. Izberite **Naprej (Next)**.
1. Izberite **Ustvari projekt (Create a project)**.

### Priprava podatkov

Pred nastavlatvijo zberite ali ustvarite niz podatkov, ki so povezani z nalogo, kot so navodila za klepet, pari vprašanje-odgovor ali katerikoli drug ustrezni besedilni podatki. Očistite in predobdelajte te podatke z odstranjevanjem šuma, obravnavanjem manjkajočih vrednosti in tokenizacijo besedila.

### Nastavitev Phi-3 modelov v Microsoft Foundry

> [!NOTE]
> Nastavitev modelov Phi-3 je trenutno podprta le v projektih, ki so locirani v East US 2.

1. Izberite **Model catalog** na levi strani zavihka.

1. V polju za iskanje vtipkajte *phi-3* in izberite phi-3 model, ki ga želite uporabiti.

    ![FineTuneSelect](../../../../translated_images/sl/select-model.60ef2d4a6a3cec57.webp)

1. Izberite **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/sl/select-finetune.a976213b543dd9d8.webp)

1. Vnesite **Ime nastavljenega modela**.

    ![FineTuneSelect](../../../../translated_images/sl/finetune1.c2b39463f0d34148.webp)

1. Izberite **Naprej (Next)**.

1. Izvedite naslednje naloge:

    - Izberite **vrsto naloge (task type)** na **Chat completion**.
    - Izberite **učno podatkovno množico**, ki jo želite uporabiti. Lahko jo naložite preko Microsoft Foundry ali iz lokalnega okolja.

    ![FineTuneSelect](../../../../translated_images/sl/finetune2.43cb099b1a94442d.webp)

1. Izberite **Naprej (Next)**.

1. Naložite **validacijske podatke**, ki jih želite uporabiti, ali pa izberite **Samodejna razdelitev učnih podatkov (Automatic split of training data)**.

    ![FineTuneSelect](../../../../translated_images/sl/finetune3.fd96121b67dcdd92.webp)

1. Izberite **Naprej (Next)**.

1. Izvedite naslednje korake:

    - Izberite **množitelj velikosti paketa (Batch size multiplier)**, ki ga želite uporabiti.
    - Izberite **učno stopnjo (Learning rate)**, ki jo želite uporabiti.
    - Izberite **število epoher (Epochs)**, ki jih želite uporabiti.

    ![FineTuneSelect](../../../../translated_images/sl/finetune4.e18b80ffccb5834a.webp)

1. Izberite **Pošlji (Submit)**, da začnete postopek nastavitev.

    ![FineTuneSelect](../../../../translated_images/sl/select-submit.0a3802d581bac271.webp)


1. Ko je vaš model nastavljen, bo status prikazan kot **Completed (Zaključeno)**, kot je prikazano na spodnji sliki. Model lahko sedaj uvedete in ga uporabite v svoji aplikaciji, v igralnem polju ali v prompt flow. Za več informacij glejte [Kako uvesti Phi-3 družino majhnih jezikovnih modelov z Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/sl/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Za podrobnejše informacije o nastavitvi Phi-3 obiščite [Nastavitev Phi-3 modelov v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Čiščenje vaših nastavljenih modelov

Nastavljeni model lahko izbrišete s seznama nastavljenih modelov v [Microsoft Foundry](https://ai.azure.com) ali s strani z informacijami o modelu. Izberite nastavljen model za brisanje na strani z nastavitvami, nato izberite gumb Izbriši za odstranitev modela.

> [!NOTE]
> Po meri ustvarjenega modela ne morete izbrisati, če ima obstoječo uvedbo. Najprej morate izbrisati uvedbo modela, preden lahko izbrišete po meri ustvarjeni model.

## Stroški in kvote

### Stroški in kvote za Phi-3 modele nastavljene kot storitev

Phi modeli, nastavljeni kot storitev, so ponudba Microsofta in so integrirani z Microsoft Foundry za uporabo. Cena je na voljo med [uvoženjem](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ali nastavljenjem modelov pod zavihkom Cena in pogoji v čarovniku za uvedbo.

## Filtriranje vsebine

Modeli, uvedeni kot storitev s plačilom po uporabi, so zaščiteni z Azure AI Content Safety. Ko so uvedeni na končnih točkah v realnem času, se lahko odločite, da te zmožnosti ne uporabljate. S omogočeno varnostjo vsebine Azure AI prehajtata tako poziv kot odgovor skozi ansambel klasifikacijskih modelov, katerih cilj je zaznati in preprečiti izhod škodljive vsebine. Sistem filtriranja vsebine zaznava in ukrepa glede posebnih kategorij potencialno škodljive vsebine tako v vhodnih pozivih kot v izhodnih odgovorih. Preberite več o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfiguracija nastavitve**

Hiperparametri: Določite hiperparametre, kot so učna stopnja, velikost paketa in število učnih epoh.

**Funkcija izgube**

Izberite primerno funkcijo izgube za svojo nalogo (npr. križna entropija).

**Optimizator**

Izberite optimizator (npr. Adam) za posodobitve gradienta med učenjem.

**Postopek nastavitev**

- Naložite predhodno naučen model: Naložite kontrolno točko Phi-3 Mini.
- Dodajte lastne plasti: Dodajte nalogi specifične plasti (npr. glava za klasifikacijo za navodila klepeta).

**Učenje modela**  
Nastavite model z uporabo pripravljenega nabora podatkov. Spremljajte napredek učenja in po potrebi prilagodite hiperparametre.

**Evaluacija in validacija**

Validacijski niz: Razdelite podatke na učni in validacijski niz.

**Ocenite zmogljivost**

Uporabite metrike, kot so natančnost, F1-ocena ali zapletenost (perplexity), da ocenite zmogljivost modela.

## Shrani nastavljeni model

**Kontrolna točka**  
Shranjujte kontrolno točko nastavljenega modela za prihodnjo rabo.

## Uvedba

- Uvedite kot spletno storitev: Uvedite svoj nastavljen model kot spletno storitev v Microsoft Foundry.
- Preizkusite končno točko: Pošljite testna vprašanja do uvedene končne točke, da preverite delovanje.

## Iterirajte in izboljšujte

Iterirajte: Če zmogljivost ni zadovoljiva, iterirajte z nastavitvijo hiperparametrov, dodajanjem več podatkov ali nastavite za dodatne epohe.

## Spremljajte in izpopolnjujte

Neprestano spremljajte vedenje modela in ga po potrebi izboljšujte.

## Prilagodite in razširite

Nastavitve za različne naloge: Phi-3 Mini lahko nastavite za različne naloge poleg navodil za klepet. Raziščite druge uporabe!  
Eksperimentirajte: Preizkusite različne arhitekture, kombinacije plasti in tehnike za izboljšanje zmogljivosti.

> [!NOTE]
> Nastavitev je iterativen proces. Eksperimentirajte, učite se in prilagajajte svoj model, da dosežete najboljše rezultate za svojo specifično nalogo!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v jeziku, v katerem je bil napisan, se šteje za avtoritativni vir. Za kritične informacije priporočamo strokovni prevod s strani človeka. Za kakršne koli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->