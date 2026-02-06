# Přispívání

Tento projekt vítá příspěvky a návrhy. Většina příspěvků vyžaduje, abyste souhlasili s Contributor License Agreement (CLA), který potvrzuje, že máte právo a skutečně nám udělujete práva k použití vašeho příspěvku. Podrobnosti najdete na [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Když odešlete pull request, CLA bot automaticky zjistí, zda je potřeba poskytnout CLA, a označí PR odpovídajícím způsobem (např. kontrola stavu, komentář). Stačí postupovat podle pokynů bota. Toto je potřeba udělat pouze jednou pro všechny repozitáře používající náš CLA.

## Kodex chování

Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Pro více informací si přečtěte [Často kladené otázky k Kodexu chování](https://opensource.microsoft.com/codeofconduct/faq/) nebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s dalšími dotazy či připomínkami.

## Upozornění při vytváření issue

Prosíme, neotvírejte GitHub issues pro obecné dotazy na podporu, protože seznam na GitHubu by měl být využíván pro požadavky na nové funkce a hlášení chyb. Tímto způsobem můžeme lépe sledovat skutečné problémy nebo chyby v kódu a oddělit obecnou diskusi od samotného kódu.

## Jak přispět

### Pokyny pro pull requesty

Při odesílání pull requestu (PR) do repozitáře Phi-3 CookBook prosím dodržujte následující pravidla:

- **Forkněte repozitář**: Vždy si repozitář nejprve forknete na svůj účet, než začnete s úpravami.

- **Oddělené pull requesty (PR)**:
  - Každý typ změny odesílejte v samostatném pull requestu. Například opravy chyb a aktualizace dokumentace by měly být v oddělených PR.
  - Opravy překlepů a drobné aktualizace dokumentace lze v případě potřeby sloučit do jednoho PR.

- **Řešení konfliktů při slučování**: Pokud váš pull request vykazuje konflikty, aktualizujte si lokální větev `main`, aby odpovídala hlavnímu repozitáři, než začnete s úpravami.

- **Odesílání překladů**: Při odesílání PR s překlady zajistěte, aby složka s překlady obsahovala překlady všech souborů z původní složky.

### Pokyny pro psaní

Pro zajištění konzistence napříč všemi dokumenty prosím dodržujte následující pravidla:

- **Formátování URL**: Všechny URL uzavírejte do hranatých závorek následovaných kulatými, bez mezer uvnitř nebo kolem nich. Například: `[example](https://www.microsoft.com)`.

- **Relativní odkazy**: Pro relativní odkazy na soubory nebo složky v aktuálním adresáři používejte `./`, pro odkazy do nadřazeného adresáře `../`. Například: `[example](../../path/to/file)` nebo `[example](../../../path/to/file)`.

- **Ne používejte lokalizace specifické pro zemi**: Ujistěte se, že vaše odkazy neobsahují lokalizace specifické pro zemi, například `/en-us/` nebo `/en/`.

- **Ukládání obrázků**: Všechny obrázky ukládejte do složky `./imgs`.

- **Popisné názvy obrázků**: Obrázky pojmenovávejte popisně, používejte anglické znaky, čísla a pomlčky. Například: `example-image.jpg`.

## GitHub Workflows

Při odeslání pull requestu se spustí následující workflow, která ověří změny. Postupujte podle níže uvedených pokynů, aby váš pull request prošel kontrolami:

- [Kontrola nefunkčních relativních cest](../..)
- [Kontrola, že URL neobsahují lokalizaci](../..)

### Kontrola nefunkčních relativních cest

Toto workflow ověřuje, že všechny relativní cesty ve vašich souborech jsou správné.

1. Pro ověření funkčnosti odkazů proveďte v VS Code následující kroky:
    - Najetím myši na jakýkoli odkaz ve vašich souborech zobrazíte náhled.
    - Stiskněte **Ctrl + Klik** pro přechod na odkaz.
    - Pokud odkaz nefunguje lokálně, workflow se spustí a odkaz nebude fungovat ani na GitHubu.

1. Pro opravu problému využijte návrhy cest od VS Code:
    - Napište `./` nebo `../`.
    - VS Code vám nabídne dostupné možnosti na základě toho, co jste napsali.
    - Kliknutím na požadovaný soubor nebo složku ověřte správnost cesty.

Po přidání správné relativní cesty uložte a pushněte změny.

### Kontrola, že URL neobsahují lokalizaci

Toto workflow ověřuje, že žádná webová URL neobsahuje lokalizaci specifickou pro zemi. Jelikož je tento repozitář přístupný globálně, je důležité zajistit, aby URL neobsahovaly lokalizaci vaší země.

1. Pro ověření, že vaše URL neobsahují lokalizace, proveďte následující:
    - Zkontrolujte, zda se v URL nevyskytuje text jako `/en-us/`, `/en/` nebo jiná jazyková lokalizace.
    - Pokud tyto texty v URL nejsou, kontrolu projdete.

1. Pro opravu problému:
    - Otevřete soubor zvýrazněný workflow.
    - Odstraňte lokalizaci země z URL.

Po odstranění lokalizace uložte a pushněte změny.

### Kontrola nefunkčních URL

Toto workflow ověřuje, že všechny webové URL ve vašich souborech fungují a vracejí stavový kód 200.

1. Pro ověření funkčnosti URL proveďte následující:
    - Zkontrolujte stav URL ve vašich souborech.

2. Pro opravu nefunkčních URL:
    - Otevřete soubor obsahující nefunkční URL.
    - Aktualizujte URL na správnou.

Po opravě URL uložte a pushněte změny.

> [!NOTE]
>
> Může se stát, že kontrola URL selže, i když je odkaz dostupný. Může to být z několika důvodů, například:
>
> - **Síťová omezení:** Servery GitHub Actions mohou mít omezení přístupu k určitým URL.
> - **Problémy s časovým limitem:** URL, které odpovídají příliš pomalu, mohou způsobit chybu timeoutu ve workflow.
> - **Dočasné problémy se serverem:** Občasná nedostupnost serveru nebo údržba může způsobit dočasnou nedostupnost URL během ověřování.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.