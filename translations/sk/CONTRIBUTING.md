<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:44:07+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sk"
}
-->
# Prispievanie

Tento projekt vítá príspevky a návrhy. Väčšina príspevkov vyžaduje, aby ste súhlasili s Contributor License Agreement (CLA), ktorý deklaruje, že máte právo a skutočne nám udeľujete práva na použitie vášho príspevku. Pre podrobnosti navštívte [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Keď odošlete pull request, CLA bot automaticky zistí, či je potrebné poskytnúť CLA, a príslušne označí PR (napr. kontrola stavu, komentár). Jednoducho postupujte podľa pokynov bota. Toto bude potrebné urobiť iba raz pre všetky repozitáre používajúce náš CLA.

## Kódex správania

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pre viac informácií si prečítajte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) alebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s ďalšími otázkami alebo pripomienkami.

## Upozornenia pri vytváraní issues

Prosím, neotvárajte GitHub issues pre všeobecné podporné otázky, keďže zoznam na GitHub by sa mal používať na požiadavky na funkcie a hlásenia chýb. Týmto spôsobom môžeme jednoduchšie sledovať skutočné problémy alebo chyby v kóde a udržať všeobecnú diskusiu oddelenú od samotného kódu.

## Ako prispieť

### Pokyny pre pull requesty

Pri odosielaní pull requestu (PR) do repozitára Phi-3 CookBook, prosím, dodržujte nasledujúce pokyny:

- **Forknite repozitár**: Vždy si najskôr forknete repozitár na svoj účet pred vykonaním zmien.

- **Oddelené pull requesty (PR)**:
  - Každý typ zmeny odosielajte v samostatnom pull requeste. Napríklad opravy chýb a aktualizácie dokumentácie by mali byť v samostatných PR.
  - Opravy preklepov a menšie aktualizácie dokumentácie je možné podľa potreby zlúčiť do jedného PR.

- **Riešenie konfliktov pri mergi**: Ak váš pull request ukazuje konflikty pri mergi, aktualizujte svoju lokálnu `main` vetvu tak, aby zodpovedala hlavnému repozitáru pred vykonaním zmien.

- **Podávanie prekladov**: Pri podávaní prekladového PR sa uistite, že prekladová zložka obsahuje preklady všetkých súborov v pôvodnej zložke.

### Pokyny pre preklady

> [!IMPORTANT]
>
> Pri preklade textu v tomto repozitári nepoužívajte strojový preklad. Preklady vykonávajte iba do jazykov, ktorým dobre rozumiete.

Ak ovládate neanglický jazyk, môžete pomôcť s prekladom obsahu. Postupujte podľa týchto krokov, aby boli vaše prekladateľské príspevky správne integrované, použite nasledujúce pokyny:

- **Vytvorte prekladovú zložku**: Prejdite do príslušnej sekcie a vytvorte prekladovú zložku pre jazyk, do ktorého prispievate. Napríklad:
  - Pre úvodnú sekciu: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Pre sekciu rýchleho štartu: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Pokračujte podľa tohto vzoru pre ďalšie sekcie (03.Inference, 04.Finetuning, atď.)

- **Aktualizujte relatívne cesty**: Pri preklade upravte štruktúru zložiek pridaním `../../` na začiatok relatívnych ciest v markdown súboroch, aby odkazy správne fungovali. Napríklad zmeňte:
  - `(../../imgs/01/phi3aisafety.png)` na `(../../../../imgs/01/phi3aisafety.png)`

- **Usporiadajte svoje preklady**: Každý preložený súbor umiestnite do príslušnej prekladovej zložky danej sekcie. Napríklad, ak prekladáte úvodnú sekciu do španielčiny, vytvoríte:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Odošlite kompletný PR**: Uistite sa, že všetky preložené súbory pre danú sekciu sú zahrnuté v jednom PR. Čiastočné preklady sekcie neprijímame. Pri podávaní prekladového PR sa uistite, že prekladová zložka obsahuje preklady všetkých súborov z pôvodnej zložky.

### Pokyny pre písanie

Aby bola zabezpečená konzistentnosť naprieč všetkými dokumentmi, používajte nasledujúce pokyny:

- **Formátovanie URL**: Všetky URL uzavrite do hranatých zátvoriek nasledovaných zátvorkami, bez medzier okolo alebo vo vnútri. Napríklad: `[example](https://www.microsoft.com)`.

- **Relatívne odkazy**: Používajte `./` pre relatívne odkazy smerujúce na súbory alebo zložky v aktuálnom adresári a `../` pre odkazy v nadradenom adresári. Napríklad: `[example](../../path/to/file)` alebo `[example](../../../path/to/file)`.

- **Nie lokálne špecifické jazyky**: Uistite sa, že vaše odkazy neobsahujú krajiny špecifické lokality. Napríklad, vyhnite sa `/en-us/` alebo `/en/`.

- **Ukladanie obrázkov**: Všetky obrázky ukladajte do zložky `./imgs`.

- **Popisné názvy obrázkov**: Obrázky pomenovávajte popisne, používajte anglické znaky, čísla a pomlčky. Napríklad: `example-image.jpg`.

## GitHub Workflows

Keď odošlete pull request, spustia sa nasledujúce workflowy na overenie zmien. Postupujte podľa pokynov nižšie, aby váš pull request úspešne prešiel kontrolami workflow:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Tento workflow zabezpečuje, že všetky relatívne cesty vo vašich súboroch sú správne.

1. Aby ste sa uistili, že vaše odkazy fungujú správne, vykonajte nasledujúce kroky vo VS Code:
    - Najazdite kurzorom na akýkoľvek odkaz v súboroch.
    - Stlačte **Ctrl + Kliknutie** pre navigáciu na odkaz.
    - Ak odkaz nefunguje lokálne, spustí sa workflow a na GitHub tiež nebude fungovať.

1. Na opravu tohto problému vykonajte nasledujúce kroky podľa návrhov ciest vo VS Code:
    - Napíšte `./` alebo `../`.
    - VS Code vám ponúkne dostupné možnosti podľa toho, čo ste napísali.
    - Kliknite na požadovaný súbor alebo zložku, aby ste sa uistili, že cesta je správna.

Keď pridáte správnu relatívnu cestu, uložte a pushnite zmeny.

### Check URLs Don't Have Locale

Tento workflow zabezpečuje, že žiadna webová URL neobsahuje lokalitu špecifickú pre krajinu. Keďže tento repozitár je globálne dostupný, je dôležité, aby URL neobsahovali lokalitu vašej krajiny.

1. Na overenie, že vaše URL neobsahujú krajinné lokality, vykonajte tieto kroky:

    - Skontrolujte text ako `/en-us/`, `/en/` alebo iné jazykové lokality v URL.
    - Ak tieto nie sú prítomné, kontrolu prejdete.

1. Na opravu tohto problému vykonajte tieto kroky:
    - Otvorte súbor zvýraznený workflowom.
    - Odstráňte krajinnú lokalitu z URL.

Po odstránení krajinskej lokality uložte a pushnite zmeny.

### Check Broken Urls

Tento workflow zabezpečuje, že každá webová URL vo vašich súboroch funguje a vracia stavový kód 200.

1. Na overenie, že vaše URL fungujú správne, vykonajte tieto kroky:
    - Skontrolujte stav URL vo vašich súboroch.

2. Na opravu nefunkčných URL vykonajte tieto kroky:
    - Otvorte súbor obsahujúci nefunkčnú URL.
    - Aktualizujte URL na správnu.

Keď URL opravíte, uložte a pushnite zmeny.

> [!NOTE]
>
> Môžu nastať prípady, keď kontrola URL zlyhá, hoci je odkaz dostupný. Môže to byť spôsobené niekoľkými dôvodmi, vrátane:
>
> - **Sieťové obmedzenia:** Servery GitHub actions môžu mať sieťové obmedzenia, ktoré bránia prístupu k určitým URL.
> - **Časové limity:** URL, ktoré odpovedajú príliš dlho, môžu spôsobiť timeout chybu vo workflow.
> - **Dočasné problémy servera:** Občasné výpadky alebo údržba servera môžu spôsobiť dočasnú nedostupnosť URL počas validácie.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.