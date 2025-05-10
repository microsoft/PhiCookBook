<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:42:38+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "cs"
}
-->
# Welcome to your VS Code Extension

## Что в папке

* В этой папке находятся все необходимые файлы для вашего расширения.
* `package.json` - это файл манифеста, в котором вы объявляете ваше расширение и команду.
  * Пример плагина регистрирует команду и задаёт её заголовок и имя команды. Благодаря этой информации VS Code может показать команду в палитре команд. Плагин при этом ещё не загружается.
* `src/extension.ts` - это основной файл, где вы реализуете вашу команду.
  * Файл экспортирует одну функцию, `activate`, которая вызывается при первом активации расширения (в данном случае при выполнении команды). Внутри функции `activate` вызывается `registerCommand`.
  * В качестве второго параметра в `registerCommand` передаётся функция с реализацией команды.

## Настройка

* Установите рекомендуемые расширения (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner и dbaeumer.vscode-eslint)


## Быстрый старт

* Нажмите `F5`, чтобы открыть новое окно с загруженным расширением.
* Запустите команду через палитру команд, нажав (`Ctrl+Shift+P` или `Cmd+Shift+P` на Mac) и введя `Hello World`.
* Устанавливайте точки останова в вашем коде внутри `src/extension.ts` для отладки расширения.
* Результаты работы расширения выводятся в консоли отладки.

## Внесение изменений

* Вы можете перезапустить расширение через панель отладки после изменения кода в `src/extension.ts`.
* Также можно перезагрузить (`Ctrl+R` или `Cmd+R` на Mac) окно VS Code с вашим расширением, чтобы применить изменения.


## Изучение API

* Полный набор API доступен в файле `node_modules/@types/vscode/index.d.ts`.

## Запуск тестов

* Установите [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Запустите задачу "watch" через команду **Tasks: Run Task**. Убедитесь, что она запущена, иначе тесты могут не обнаружиться.
* Откройте представление Testing на панели активности и нажмите кнопку Run Test или используйте горячую клавишу `Ctrl/Cmd + ; A`.
* Результаты тестов отображаются в окне Test Results.
* Вносите изменения в `src/test/extension.test.ts` или создавайте новые тесты в папке `test`.
  * Тестовый раннер учитывает только файлы, соответствующие шаблону имени `**.test.ts`.
  * Вы можете создавать папки внутри `test` для удобной организации тестов.

## Продвинутые возможности

* Уменьшите размер расширения и ускорьте запуск, [упаковывая расширение](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Опубликуйте расширение](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) в маркетплейсе VS Code.
* Автоматизируйте сборки с помощью [непрерывной интеграции](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.