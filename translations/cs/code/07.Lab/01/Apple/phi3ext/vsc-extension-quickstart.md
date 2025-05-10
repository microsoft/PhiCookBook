<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:10:03+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "cs"
}
-->
# Добро пожаловать в ваше расширение VS Code

## Что находится в папке

* В этой папке содержатся все файлы, необходимые для вашего расширения.
* `package.json` - это манифест, в котором вы объявляете свое расширение и команду.
  * Пример плагина регистрирует команду и задает ее заголовок и имя команды. Благодаря этой информации VS Code может показать команду в палитре команд. При этом плагин еще не загружается.
* `src/extension.ts` - это основной файл, где вы реализуете логику вашей команды.
  * Файл экспортирует одну функцию, `activate`, которая вызывается при первом активации расширения (в данном случае при выполнении команды). Внутри функции `activate` мы вызываем `registerCommand`.
  * В качестве второго параметра в `registerCommand` передается функция с реализацией команды.

## Настройка

* Установите рекомендуемые расширения (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner и dbaeumer.vscode-eslint)


## Быстрый старт

* Нажмите `F5`, чтобы открыть новое окно с загруженным расширением.
* Запустите команду из палитры команд, нажав (`Ctrl+Shift+P` или `Cmd+Shift+P` на Mac) и введя `Hello World`.
* Установите точки останова в коде внутри `src/extension.ts` для отладки расширения.
* Просматривайте вывод расширения в консоли отладки.

## Внесение изменений

* После изменения кода в `src/extension.ts` вы можете перезапустить расширение с панели отладки.
* Также можно перезагрузить окно VS Code с расширением, нажав (`Ctrl+R` или `Cmd+R` на Mac), чтобы применить изменения.


## Изучение API

* Полный набор нашего API можно открыть, открыв файл `node_modules/@types/vscode/index.d.ts`.

## Запуск тестов

* Установите [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Запустите задачу "watch" через команду **Tasks: Run Task**. Убедитесь, что она запущена, иначе тесты не будут обнаружены.
* Откройте представление Testing на панели активности и нажмите кнопку Run Test, или используйте горячую клавишу `Ctrl/Cmd + ; A`
* Просматривайте результаты тестов в представлении Test Results.
* Вносите изменения в `src/test/extension.test.ts` или создавайте новые тестовые файлы внутри папки `test`.
  * Предоставленный тест-раннер учитывает только файлы, соответствующие шаблону имени `**.test.ts`.
  * Вы можете создавать подпапки внутри `test` для удобной организации тестов.

## Двигайтесь дальше

* Уменьшите размер расширения и ускорьте время запуска, [собрав расширение в один пакет](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Опубликуйте расширение](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) на маркетплейсе VS Code.
* Автоматизируйте сборки, настроив [непрерывную интеграцию](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje využít profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.