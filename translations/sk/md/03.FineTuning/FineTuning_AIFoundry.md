# Doladenie Phi-3 pomocou Microsoft Foundry

 Preskúmajme, ako doladiť jazykový model Phi-3 Mini od Microsoftu pomocou Microsoft Foundry. Doladenie vám umožňuje prispôsobiť Phi-3 Mini špecifickým úlohám, čím ho robí ešte výkonnejším a viac kontextovo uvedomelým.

## Úvahy

- **Schopnosti:** Ktoré modely je možné doladiť? Čo môže základný model po doladení robiť?
- **Náklady:** Aký je cenový model doladenia
**Prispôsobiteľnosť:** Do akej miery môžem modifikovať základný model – a akým spôsobom?
- **Pohodlie:** Ako prebieha doladenie – musím písať vlastný kód? Musím priniesť vlastný výpočtový výkon?
- **Bezpečnosť:** Doladené modely môžu predstavovať bezpečnostné riziká – sú na mieste nejaké ochranné opatrenia proti neúmyselnému poškodeniu?

![AIFoundry Models](../../../../translated_images/sk/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Príprava na doladenie

### Predpoklady

> [!NOTE]
> Pre modely rodiny Phi-3 je ponuka doladenia podľa modelu pay-as-you-go dostupná len pre huby vytvorené v regiónoch **East US 2**.

- Predplatné Azure. Ak ešte nemáte predplatné Azure, vytvorte si [platený Azure účet](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go), aby ste mohli začať.

- [Projekt AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Pre udelenie prístupu k operáciám v Microsoft Foundry sa používajú riadenia prístupu na základe rolí Azure (Azure RBAC). Aby ste mohli vykonať kroky v tomto článku, musí byť váš používateľský účet priradený k role __Azure AI Developer__ v rámci zdrojovej skupiny.

### Registrácia poskytovateľa predplatného

Overte, či je predplatné registrované u poskytovateľa zdrojov `Microsoft.Network`.

1. Prihláste sa do [Azure portálu](https://portal.azure.com).
1. Z ľavého menu vyberte **Predplatné**.
1. Vyberte predplatné, ktoré chcete použiť.
1. Z ľavého menu vyberte **Nastavenia AI projektu** > **Poskytovatelia zdrojov**.
1. Potvrďte, že **Microsoft.Network** je v zozname poskytovateľov zdrojov. Ak nie, pridajte ho.

### Príprava dát

Pripravte si trénovacie a validačné dáta na doladenie vášho modelu. Vaše trénovacie a validačné datasety pozostávajú z príkladov vstupov a výstupov, ktoré definujú, ako by mal model fungovať.

Uistite sa, že všetky vaše trénovacie príklady zodpovedajú očakávanému formátu pre inferenciu. Na efektívne doladenie modelov zabezpečte vyvážený a rôznorodý dataset.

Toto zahŕňa udržiavanie rovnováhy dát, zahrnujúce rôzne scenáre a pravidelnú úpravu trénovacích dát tak, aby zodpovedali reálnym očakávaniam, čo vedie k presnejším a vyváženým odpovediam modelu.

Rôzne typy modelov vyžadujú rôzny formát trénovacích dát.

### Chat Completion

Trénovacie a validačné dáta, ktoré použijete, **musia** byť naformátované ako JSON Lines (JSONL) dokument. Pre `Phi-3-mini-128k-instruct` musí byť dataset na doladenie naformátovaný v konverzačnom formáte používanom API Chat completions.

### Príklad formátu súboru

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Podporovaný typ súboru je JSON Lines. Súbory sa nahrajú do predvoleného úložiska a sprístupnia sa vo vašom projekte.

## Doladenie Phi-3 pomocou Microsoft Foundry

Microsoft Foundry umožňuje prispôsobiť veľké jazykové modely vašim osobným datasetom pomocou procesu nazývaného doladenie. Doladenie prináša významnú hodnotu umožnením prispôsobenia a optimalizácie pre konkrétne úlohy a aplikácie. Vedie k zlepšeniu výkonu, úspore nákladov, zníženiu latencie a prispôsobeným výstupom.

![Finetune AI Foundry](../../../../translated_images/sk/AIFoundryfinetune.193aaddce48d553c.webp)

### Vytvorenie nového projektu

1. Prihláste sa do [Microsoft Foundry](https://ai.azure.com).

1. Kliknite na **+Nový projekt** pre vytvorenie nového projektu v Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/sk/select-new-project.cd31c0404088d7a3.webp)

1. Vykonajte nasledujúce kroky:

    - Názov **Hubu projektu**. Musí byť jedinečná hodnota.
    - Vyberte **Hub**, ktorý chcete použiť (v prípade potreby vytvorte nový).

    ![FineTuneSelect](../../../../translated_images/sk/create-project.ca3b71298b90e420.webp)

1. Pre vytvorenie nového hubu vykonajte nasledujúce úlohy:

    - Zadajte **Názov hubu**. Musí byť jedinečný.
    - Vyberte vaše Azure **predplatné**.
    - Vyberte **zdrojovú skupinu** na použitie (v prípade potreby vytvorte novú).
    - Vyberte **Lokalitu**, ktorú chcete použiť.
    - Vyberte **Pripojiť Azure AI služby** na použitie (v prípade potreby vytvorte nové).
    - Vyberte **Pripojiť Azure AI vyhľadávanie** a vyberte **Preskočiť pripojenie**.

    ![FineTuneSelect](../../../../translated_images/sk/create-hub.49e53d235e80779e.webp)

1. Kliknite na **Ďalej**.
1. Kliknite na **Vytvoriť projekt**.

### Príprava dát

Pred doladením zhromaždite alebo vytvorte dataset relevantný k vašej úlohe, napríklad chat inštrukcie, otázky s odpoveďami alebo iné relevantné textové dáta. Dáta vyčistite a predspracujte odstránením šumu, ošetrením chýbajúcich hodnôt a tokenizáciou textu.

### Doladenie Phi-3 modelov v Microsoft Foundry

> [!NOTE]
> Doladenie Phi-3 modelov je momentálne podporované iba v projektoch umiestnených v East US 2.

1. Z ľavého menu vyberte **Katalóg modelov**.

1. Do **vyhľadávacieho poľa** zadajte *phi-3* a vyberte model phi-3, ktorý chcete použiť.

    ![FineTuneSelect](../../../../translated_images/sk/select-model.60ef2d4a6a3cec57.webp)

1. Kliknite na **Doladiť**.

    ![FineTuneSelect](../../../../translated_images/sk/select-finetune.a976213b543dd9d8.webp)

1. Zadajte **Názov doladeného modelu**.

    ![FineTuneSelect](../../../../translated_images/sk/finetune1.c2b39463f0d34148.webp)

1. Kliknite na **Ďalej**.

1. Vykonajte nasledujúce úlohy:

    - Vyberte **typ úlohy** na **Chat completion**.
    - Vyberte **tréningové dáta**, ktoré chcete použiť. Môžete ich nahrať z dát Microsoft Foundry alebo z lokálneho prostredia.

    ![FineTuneSelect](../../../../translated_images/sk/finetune2.43cb099b1a94442d.webp)

1. Kliknite na **Ďalej**.

1. Nahrajte **validačné dáta**, ktoré chcete použiť, alebo vyberte **Automatické rozdelenie tréningových dát**.

    ![FineTuneSelect](../../../../translated_images/sk/finetune3.fd96121b67dcdd92.webp)

1. Kliknite na **Ďalej**.

1. Vykonajte nasledujúce kroky:

    - Vyberte **násobiteľ veľkosti dávky** (Batch size multiplier).
    - Vyberte **učiacu rýchlosť** (Learning rate).
    - Vyberte počet **epoch**.

    ![FineTuneSelect](../../../../translated_images/sk/finetune4.e18b80ffccb5834a.webp)

1. Kliknite na **Odoslať** na spustenie procesu doladenia.

    ![FineTuneSelect](../../../../translated_images/sk/select-submit.0a3802d581bac271.webp)


1. Po doladení modelu sa stav zobrazí ako **Dokončené**, ako je zobrazené na obrázku nižšie. Teraz môžete model nasadiť a používať ho vo svojej aplikácii, na pracovnej ploche (playground) alebo v prompt flow. Pre viac informácií pozrite [Ako nasadiť Phi-3 rodinu malých jazykových modelov pomocou Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/sk/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Pre podrobnejšie informácie o doladení Phi-3 navštívte [Doladenie Phi-3 modelov v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Čistenie vašich doladených modelov

Doladený model môžete zmazať zo zoznamu doladených modelov v [Microsoft Foundry](https://ai.azure.com) alebo zo stránky detailov modelu. Vyberte doladený model, ktorý chcete vymazať z stránky Doladenie, a potom kliknite na tlačidlo Vymazať.

> [!NOTE]
> Vlastný model nemôžete vymazať, ak má existujúce nasadenie. Najprv musíte vymazať nasadenie modelu, až potom môžete zmazať vlastný model.

## Náklady a kvóty

### Náklady a obmedzenia pre Phi-3 modely doladené ako služba

Phi modely doladené ako služba sú ponúkané spoločnosťou Microsoft a integrované s Microsoft Foundry na použitie. Ceny nájdete pri [nasadzovaní](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) alebo doladení modelov pod záložkou Ceny a podmienky v sprievodcovi nasadením.

## Filtrácia obsahu

Modely nasadené ako služba podľa modelu pay-as-you-go sú chránené službou Azure AI Content Safety. Pri nasadení na realtime koncové body je možné túto možnosť vypnúť. Pri zapnutej službe Azure AI Content Safety prechádza vstupný prompt aj výstupné dokončenia cez súbor klasifikačných modelov zameraných na detekciu a zabránenie výstupu škodlivého obsahu. Systém filtrácie obsahu detekuje a prijíma opatrenia na konkrétne kategórie potenciálne škodlivého obsahu vo vstupných promptoch aj výstupoch. Viac informácií o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfigurácia doladenia**

Hiperparametre: Definujte hyperparametre ako učebnú rýchlosť, veľkosť dávky a počet tréningových epoch.

**Funkcia straty**

Vyberte vhodnú funkciu straty pre vašu úlohu (napríklad cross-entropy).

**Optimalizátor**

Vyberte optimalizátor (napr. Adam) pre aktualizácie gradientu počas tréningu.

**Proces doladenia**

- Načítanie predtrénovaného modelu: Načítajte checkpoint Phi-3 Mini.
- Pridanie vlastných vrstiev: Pridajte vrstvy špecifické pre úlohu (napr. triediacu hlavu pre chat inštrukcie).

**Tréning modelu**
Doladte model pomocou pripravenej množiny dát. Sledujte priebeh trénovania a podľa potreby upravujte hyperparametre.

**Hodnotenie a validácia**

Validačná množina: Rozdeľte dáta na trénovacie a validačné.

**Vyhodnotenie výkonu**

Použite metriky ako presnosť (accuracy), F1-skóre alebo perplexitu na hodnotenie výkonu modelu.

## Uloženie doladeného modelu

**Checkpoint**
Uložte checkpoint doladeného modelu pre budúce použitie.

## Nasadenie

- Nasadenie ako webová služba: Nasadte doladený model ako webovú službu v Microsoft Foundry.
- Testovanie koncového bodu: Pošlite testovacie dotazy na nasadený koncový bod, aby ste overili jeho funkčnosť.

## Iterujte a zlepšujte

Iterujte: Ak výkon nie je uspokojivý, upravujte hyperparametre, pridávajte viac dát alebo doladzte na viac epoch.

## Monitorujte a dolaďujte

Neustále sledujte správanie modelu a dolaďujte ho podľa potreby.

## Prispôsobujte a rozširujte

Vlastné úlohy: Phi-3 Mini môžete doladiť pre rôzne úlohy okrem chat inštrukcií. Preskúmajte ďalšie možnosti využitia!
Experimentujte: Vyskúšajte rôzne architektúry, kombinácie vrstiev a techniky na zlepšenie výkonu.

> [!NOTE]
> Doladenie je iteratívny proces. Experimentujte, učte sa a prispôsobujte svoj model, aby ste dosiahli najlepšie výsledky pre vašu konkrétnu úlohu!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nepochopenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->