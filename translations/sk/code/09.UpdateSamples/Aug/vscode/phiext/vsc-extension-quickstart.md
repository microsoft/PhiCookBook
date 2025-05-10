<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:44:08+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "sk"
}
-->
# Vitajte vo vašom rozšírení VS Code

## Čo je v priečinku

* Tento priečinok obsahuje všetky súbory potrebné pre vaše rozšírenie.
* `package.json` - toto je manifestový súbor, v ktorom deklarujete svoje rozšírenie a príkaz.
  * Ukážkový plugin zaregistruje príkaz a definuje jeho názov a meno príkazu. Vďaka týmto informáciám môže VS Code zobraziť príkaz v palete príkazov. Plugin sa však zatiaľ nemusí načítať.
* `src/extension.ts` - toto je hlavný súbor, kde poskytnete implementáciu svojho príkazu.
  * Súbor exportuje jednu funkciu, `activate`, ktorá sa volá pri prvom aktivovaní rozšírenia (v tomto prípade spustením príkazu). Vo funkcii `activate` voláme `registerCommand`.
  * Funkciu obsahujúcu implementáciu príkazu odovzdávame ako druhý parameter do `registerCommand`.

## Nastavenie

* nainštalujte odporúčané rozšírenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint)


## Začnite hneď pracovať

* Stlačte `F5` pre otvorenie nového okna s načítaným rozšírením.
* Spustite svoj príkaz z palety príkazov stlačením (`Ctrl+Shift+P` alebo `Cmd+Shift+P` na Macu) a zadaním `Hello World`.
* Nastavte body prerušenia vo svojom kóde v `src/extension.ts` pre ladenie rozšírenia.
* Výstup z rozšírenia nájdete v debug konzole.

## Vykonajte zmeny

* Po zmene kódu v `src/extension.ts` môžete rozšírenie znova spustiť z debug panela.
* Tiež môžete obnoviť (`Ctrl+R` alebo `Cmd+R` na Macu) okno VS Code s vaším rozšírením, aby sa načítali zmeny.


## Preskúmajte API

* Kompletný súbor API môžete otvoriť otvorením súboru `node_modules/@types/vscode/index.d.ts`.

## Spustite testy

* Nainštalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Spustite úlohu "watch" cez príkaz **Tasks: Run Task**. Uistite sa, že beží, inak testy nemusia byť zistené.
* Otvorte zobrazenie Testing z aktivity panela a kliknite na tlačidlo Run Test, alebo použite klávesovú skratku `Ctrl/Cmd + ; A`
* Výsledky testov uvidíte v zobrazení Test Results.
* Robte zmeny v `src/test/extension.test.ts` alebo vytvárajte nové testovacie súbory v priečinku `test`.
  * Poskytnutý test runner bude brať do úvahy len súbory zodpovedajúce vzoru názvu `**.test.ts`.
  * V priečinku `test` môžete vytvárať ďalšie priečinky na usporiadanie testov podľa potreby.

## Pokročilé možnosti

* Zmenšite veľkosť rozšírenia a zrýchlite jeho spustenie [zbalením rozšírenia](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikujte svoje rozšírenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na trhu rozšírení VS Code.
* Automatizujte buildy nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.