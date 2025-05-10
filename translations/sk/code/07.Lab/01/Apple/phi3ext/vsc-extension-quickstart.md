<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:10:13+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sk"
}
-->
# Vitajte vo vašom rozšírení VS Code

## Čo sa nachádza v priečinku

* Tento priečinok obsahuje všetky súbory potrebné pre vaše rozšírenie.
* `package.json` - toto je manifestový súbor, v ktorom deklarujete svoje rozšírenie a príkaz.
  * Ukážkový plugin zaregistruje príkaz a definuje jeho názov a meno príkazu. Na základe týchto informácií môže VS Code zobraziť príkaz v palete príkazov. Plugin sa však ešte nemusí načítať.
* `src/extension.ts` - toto je hlavný súbor, kde implementujete svoj príkaz.
  * Súbor exportuje jednu funkciu, `activate`, ktorá sa zavolá pri prvom aktivovaní rozšírenia (v tomto prípade vykonaním príkazu). Vo funkcii `activate` voláme `registerCommand`.
  * Funkciu obsahujúcu implementáciu príkazu odovzdávame ako druhý parameter do `registerCommand`.

## Nastavenie

* Nainštalujte odporúčané rozšírenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint)


## Rýchly štart

* Stlačte `F5` na otvorenie nového okna s načítaným rozšírením.
* Spustite svoj príkaz z palety príkazov stlačením (`Ctrl+Shift+P` alebo `Cmd+Shift+P` na Macu) a zadaním `Hello World`.
* Nastavte breakpointy vo svojom kóde v `src/extension.ts` na ladenie rozšírenia.
* Výstup z rozšírenia nájdete v debug konzole.

## Úpravy

* Po zmene kódu v `src/extension.ts` môžete rozšírenie znova spustiť z debug panela.
* Tiež môžete znovu načítať (`Ctrl+R` alebo `Cmd+R` na Macu) okno VS Code s vaším rozšírením, aby sa prejavili zmeny.


## Preskúmajte API

* Kompletný súbor nášho API môžete otvoriť v súbore `node_modules/@types/vscode/index.d.ts`.

## Spustenie testov

* Nainštalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Spustite úlohu "watch" cez príkaz **Tasks: Run Task**. Uistite sa, že beží, inak sa testy nemusia objaviť.
* Otvorte zobrazenie Testing z aktivity a kliknite na tlačidlo Run Test, alebo použite klávesovú skratku `Ctrl/Cmd + ; A`
* Výsledky testov uvidíte v zobrazení Test Results.
* Robte zmeny v `src/test/extension.test.ts` alebo vytvárajte nové testovacie súbory v priečinku `test`.
  * Poskytnutý test runner bude brať do úvahy len súbory zodpovedajúce vzoru názvu `**.test.ts`.
  * Môžete si vytvárať priečinky v `test` na ľubovoľnú štruktúru testov.

## Pokročilé možnosti

* Znížte veľkosť rozšírenia a zrýchlite jeho spustenie pomocou [zabalenia rozšírenia](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikujte svoje rozšírenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na trhu rozšírení VS Code.
* Automatizujte zostavy nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.