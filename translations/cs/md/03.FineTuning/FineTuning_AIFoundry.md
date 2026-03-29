# Ladění Phi-3 pomocí Microsoft Foundry

Pojďme prozkoumat, jak doladit jazykový model Phi-3 Mini od Microsoftu pomocí Microsoft Foundry. Ladění umožňuje přizpůsobit Phi-3 Mini konkrétním úkolům, díky čemuž je ještě výkonnější a lépe chápe kontext.

## Úvahy

- **Schopnosti:** Které modely lze doladit? Co lze základní model doladit, aby dělal?
- **Cena:** Jaký je cenový model ladění
- **Přizpůsobitelnost:** Do jaké míry mohu modifikovat základní model – a jakými způsoby?
- **Pohodlí:** Jak ladění vlastně probíhá – musím psát vlastní kód? Musím přinést vlastní výpočetní výkon?
- **Bezpečnost:** Laděné modely jsou známy riziky z hlediska bezpečnosti – existují nějaké ochranné mechanismy, aby se předešlo nechtěným škodám?

![AIFoundry Models](../../../../translated_images/cs/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Příprava na ladění

### Požadavky

> [!NOTE]
> Pro modely rodiny Phi-3 je nabídka ladění s platbou podle využití dostupná pouze s huby vytvořenými v regionech **East US 2**.

- Předplatné Azure. Pokud nemáte předplatné Azure, vytvořte si [placený účet Azure](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) pro začátek.

- Projekt v [AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- K řízení přístupů k operacím v Microsoft Foundry se používá řízení přístupu založené na rolích Azure (Azure RBAC). Pro provedení kroků v tomto článku musí být vašemu uživatelskému účtu přiřazena __role Azure AI Developer__ ke skupině prostředků.

### Registrace poskytovatele předplatného

Ověřte, zda je předplatné registrováno pro poskytovatele zdrojů `Microsoft.Network`.

1. Přihlaste se do [Azure portálu](https://portal.azure.com).
1. Vyberte **Předplatné** z levého menu.
1. Vyberte předplatné, které chcete použít.
1. Vyberte **Nastavení AI projektu** > **Poskytovatelé zdrojů** z levého menu.
1. Potvrďte, že seznam poskytovatelů zahrnuje **Microsoft.Network**. Pokud ne, přidejte jej.

### Příprava dat

Připravte si tréninková a validační data pro ladění vašeho modelu. Vaše tréninková a validační data se skládají z příkladů vstupů a výstupů, jak by měl model pracovat.

Ujistěte se, že všechny tréninkové příklady odpovídají očekávanému formátu pro inferenci. Pro efektivní ladění modelů zajistěte vyvážený a různorodý dataset.

To zahrnuje udržování rovnováhy dat, zahrnutí různých scénářů a pravidelnou úpravu tréninkových dat, aby odpovídala reálným očekáváním, což vede k přesnějším a vyváženějším odpovědím modelu.

Různé typy modelů vyžadují odlišný formát tréninkových dat.

### Chat Completion

Tréninková a validační data, která použijete, **musí** být ve formátu JSON Lines (JSONL). Pro `Phi-3-mini-128k-instruct` musí být dataset pro ladění ve formátu konverzačním, jaký používá API Chat completions.

### Ukázkový formát souboru

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Podporovaný typ souboru je JSON Lines. Soubory jsou nahrané do výchozího úložiště a zpřístupněné ve vašem projektu.

## Ladění Phi-3 pomocí Microsoft Foundry

Microsoft Foundry umožňuje přizpůsobit velké jazykové modely vašim osobním datovým sadám pomocí procesu zvaného ladění (fine-tuning). Ladění poskytuje významnou hodnotu umožněním přizpůsobení a optimalizace pro konkrétní úkoly a aplikace. Zlepšuje výkon, nákladovou efektivitu, snižuje latenci a umožňuje cílené výstupy.

![Finetune AI Foundry](../../../../translated_images/cs/AIFoundryfinetune.193aaddce48d553c.webp)

### Vytvoření nového projektu

1. Přihlaste se do [Microsoft Foundry](https://ai.azure.com).

1. Vyberte **+Nový projekt** pro vytvoření nového projektu v Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/cs/select-new-project.cd31c0404088d7a3.webp)

1. Proveďte následující úkony:

    - Název projektu **Hub name**. Musí být unikátní.
    - Vyberte **Hub**, který chcete použít (v případě potřeby vytvořte nový).

    ![FineTuneSelect](../../../../translated_images/cs/create-project.ca3b71298b90e420.webp)

1. Pro vytvoření nového hubu proveďte tyto úkony:

    - Zadejte **Hub name**. Musí být unikátní.
    - Vyberte vaše Azure **Předplatné**.
    - Vyberte **Resource group**, kterou chcete použít (vytvořte novou, pokud potřebujete).
    - Vyberte **Umístění** (Location), které chcete použít.
    - Vyberte **Connect Azure AI Services**, které chcete použít (vytvořte nové, pokud potřebujete).
    - U **Connect Azure AI Search** vyberte **Přeskočit připojení**.

    ![FineTuneSelect](../../../../translated_images/cs/create-hub.49e53d235e80779e.webp)

1. Vyberte **Další**.
1. Vyberte **Vytvořit projekt**.

### Příprava dat

Před laděním shromážděte nebo vytvořte dataset související s vaším úkolem, například instrukce pro chat, páry otázek a odpovědí nebo jiné relevantní textové údaje. Data očistěte a předzpracujte odstraněním šumu, vyřešením chybějících hodnot a tokenizací textu.

### Ladění modelů Phi-3 v Microsoft Foundry

> [!NOTE]
> Ladění modelů Phi-3 je momentálně podporováno pouze v projektech lokalizovaných v East US 2.

1. Z levé záložky vyberte **Katalog modelů**.

1. Do **vyhledávacího pole** zadejte *phi-3* a vyberte model phi-3, který chcete použít.

    ![FineTuneSelect](../../../../translated_images/cs/select-model.60ef2d4a6a3cec57.webp)

1. Klikněte na **Doladit** (Fine-tune).

    ![FineTuneSelect](../../../../translated_images/cs/select-finetune.a976213b543dd9d8.webp)

1. Zadejte název **Doladěného modelu**.

    ![FineTuneSelect](../../../../translated_images/cs/finetune1.c2b39463f0d34148.webp)

1. Vyberte **Další**.

1. Proveďte následující:

    - Vyberte **typ úkolu** jako **Chat completion**.
    - Vyberte **Tréninková data**, která chcete použít. Můžete je nahrát přes data Microsoft Foundry nebo ze svého lokálního prostředí.

    ![FineTuneSelect](../../../../translated_images/cs/finetune2.43cb099b1a94442d.webp)

1. Vyberte **Další**.

1. Nahrajte **Validační data**, která chcete použít. nebo si můžete zvolit **Automatické rozdělení tréninkových dat**.

    ![FineTuneSelect](../../../../translated_images/cs/finetune3.fd96121b67dcdd92.webp)

1. Vyberte **Další**.

1. Proveďte následující:

    - Vyberte **Násobitel velikosti dávky** (Batch size multiplier), který chcete použít.
    - Vyberte **Učební rychlost** (Learning rate), kterou chcete použít.
    - Vyberte počet **Epoch**.

    ![FineTuneSelect](../../../../translated_images/cs/finetune4.e18b80ffccb5834a.webp)

1. Vyberte **Odeslat** (Submit) pro spuštění procesu ladění.

    ![FineTuneSelect](../../../../translated_images/cs/select-submit.0a3802d581bac271.webp)


1. Jakmile je model doladěný, stav se zobrazí jako **Dokončeno** (Completed), viz obrázek níže. Nyní můžete model nasadit a používat jej ve vlastní aplikaci, v playgroundu nebo v prompt flow. Více informací najdete v [Jak nasadit rodinu malých jazykových modelů Phi-3 pomocí Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/cs/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Pro podrobnější informace o ladění Phi-3 navštivte prosím [Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Odstranění doladěných modelů

Můžete smazat doladěný model ze seznamu laděných modelů v [Microsoft Foundry](https://ai.azure.com) nebo ze stránky s detaily modelu. Vyberte doladěný model, který chcete smazat na stránce ladění, a poté klikněte na tlačítko Smazat.

> [!NOTE]
> Nemůžete smazat vlastní model, pokud má existující nasazení. Nejdříve musíte smazat nasazení modelu, aby bylo možné odstranit vlastní model.

## Náklady a limity

### Úvahy o nákladech a limitech pro modely Phi-3 laděné jako služba

Modely Phi laděné jako služba nabízí Microsoft a jsou integrovány s Microsoft Foundry pro použití. Cena je dostupná při [nasazení](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) nebo ladění modelů v záložce Ceny a podmínky v průvodci nasazením.

## Filtrace obsahu

Modely nasazené jako služba s platbou podle využití jsou chráněny Azure AI Content Safety. Při nasazení na real-time endpoint můžete tuto funkci zvolit k vypnutí. S povolenou ochranou Azure AI Content Safety prochází jak prompt, tak výstupy sadou klasifikačních modelů, které detekují a zabraňují výstupu škodlivého obsahu. Systém filtrování detekuje a zasahuje proti specifickým kategoriím potenciálně škodlivého obsahu ve vstupních prompty i výstupních odpovědích. Více informací o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfigurace ladění**

Hyperparametry: Definujte hyperparametry jako učební rychlost, velikost dávky a počet epochs.

**Funkce ztráty**

Vyberte vhodnou funkci ztráty pro váš úkol (např. cross-entropy).

**Optimalizátor**

Zvolte optimalizátor (např. Adam) pro aktualizace gradientu během tréninku.

**Proces ladění**

- Načtení předtrénovaného modelu: Načtěte checkpoint Phi-3 Mini.
- Přidání vlastních vrstev: Přidejte vrstvy specifické pro úkol (např. klasifikační hlavu pro chatové instrukce).

**Trénink modelu**  
Doladte model pomocí připraveného datasetu. Sledujte průběh tréninku a podle potřeby upravujte hyperparametry.

**Vyhodnocení a validace**

Validační sada: Rozdělte data na tréninkovou a validační část.

**Vyhodnocení výkonu**

Použijte metriky jako přesnost, F1-skóre nebo perplexitu k hodnocení výkonnosti modelu.

## Uložení doladěného modelu

**Checkpoint**  
Uložte checkpoint doladěného modelu pro pozdější využití.

## Nasazení

- Nasazení jako webová služba: Nasazte doladěný model jako webovou službu v Microsoft Foundry.
- Testování endpointu: Posílejte testovací dotazy na nasazený endpoint a ověřte jeho funkčnost.

## Iterace a zlepšení

Iterujte: Pokud není výkon uspokojivý, dolaďte hyperparametry, přidejte více dat nebo pokračujte v ladění další epochy.

## Monitorování a dolaďování

Nepřetržitě sledujte chování modelu a dolaďujte jej podle potřeby.

## Přizpůsobení a rozšíření

Vlastní úkoly: Phi-3 Mini lze ladit pro různé úkoly nad rámec chatových instrukcí. Prozkoumejte další scénáře použití!  
Experimentujte: Zkoušejte různé architektury, kombinace vrstev a techniky pro zlepšení výkonu.

> [!NOTE]
> Ladění je iterativní proces. Experimentujte, učte se a upravujte model tak, aby dosáhl nejlepších výsledků pro váš konkrétní úkol!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornění**:  
Tento dokument byl přeložen pomocí služby automatického překladu [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->