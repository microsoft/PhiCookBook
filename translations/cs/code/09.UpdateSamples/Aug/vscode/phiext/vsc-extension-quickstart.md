# Vítejte u vaší VS Code rozšíření

## Co je ve složce

* Tato složka obsahuje všechny soubory potřebné pro vaše rozšíření.
* `package.json` - manifestový soubor, ve kterém deklarujete své rozšíření a příkaz.
  * Ukázkový plugin zaregistruje příkaz a definuje jeho název a jméno příkazu. Díky těmto informacím může VS Code zobrazit příkaz v paletě příkazů. Plugin se zatím nemusí načítat.
* `src/extension.ts` - hlavní soubor, kde implementujete svůj příkaz.
  * Soubor exportuje jednu funkci, `activate`, která je volána poprvé, když je rozšíření aktivováno (v tomto případě spuštěním příkazu). Uvnitř funkce `activate` voláme `registerCommand`.
  * Jako druhý parametr do `registerCommand` předáváme funkci obsahující implementaci příkazu.

## Nastavení

* nainstalujte doporučená rozšíření (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint)

## Začněte hned

* Stiskněte `F5` pro otevření nového okna s načteným rozšířením.
* Spusťte svůj příkaz z palety příkazů stisknutím (`Ctrl+Shift+P` nebo `Cmd+Shift+P` na Macu) a napište `Hello World`.
* Nastavte breakpointy ve svém kódu v `src/extension.ts` pro ladění rozšíření.
* Výstup z rozšíření najdete v debug konzoli.

## Proveďte změny

* Po změně kódu v `src/extension.ts` můžete rozšíření znovu spustit z debug panelu.
* Také můžete znovu načíst (`Ctrl+R` nebo `Cmd+R` na Macu) okno VS Code s vaším rozšířením, aby se změny projevily.

## Prozkoumejte API

* Kompletní sadu našeho API otevřete v souboru `node_modules/@types/vscode/index.d.ts`.

## Spusťte testy

* Nainstalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Spusťte úlohu "watch" přes příkaz **Tasks: Run Task**. Ujistěte se, že běží, jinak testy nemusí být nalezeny.
* Otevřete zobrazení Testování z aktivity a klikněte na tlačítko "Run Test" nebo použijte klávesovou zkratku `Ctrl/Cmd + ; A`
* Výsledek testu uvidíte ve zobrazení Test Results.
* Měňte soubor `src/test/extension.test.ts` nebo vytvářejte nové testovací soubory ve složce `test`.
  * Poskytnutý test runner bude brát v potaz pouze soubory odpovídající vzoru `**.test.ts`.
  * Ve složce `test` můžete vytvářet podsložky pro lepší organizaci testů.

## Pokročilé možnosti

* Zmenšete velikost rozšíření a zlepšete dobu spuštění pomocí [balení rozšíření](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikujte své rozšíření](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na tržišti VS Code rozšíření.
* Automatizujte sestavení nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.