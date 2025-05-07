<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-05-07T13:47:43+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "ru"
}
-->
# **Создайте собственный чат GitHub Copilot для Visual Studio Code с семейством Microsoft Phi-3**

Вы уже использовали workspace agent в GitHub Copilot Chat? Хотите создать собственного агента для кода вашей команды? Этот практический курс предлагает объединить open source модель для создания корпоративного бизнес-агента по работе с кодом.

## **Основы**

### **Почему стоит выбрать Microsoft Phi-3**

Phi-3 — это семейство моделей, включающее phi-3-mini, phi-3-small и phi-3-medium, различающиеся параметрами обучения для генерации текста, завершения диалогов и генерации кода. Также существует phi-3-vision на основе Vision. Это решение подходит для предприятий и команд, которые хотят создавать офлайн-генеративные AI-решения.

Рекомендуется ознакомиться с этой ссылкой [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Расширение GitHub Copilot Chat предоставляет интерфейс чата, который позволяет взаимодействовать с GitHub Copilot и получать ответы на вопросы, связанные с программированием, прямо в VS Code, без необходимости искать информацию в документации или на форумах.

Copilot Chat может использовать подсветку синтаксиса, отступы и другие элементы форматирования для улучшения читаемости ответов. В зависимости от типа вопроса, результат может содержать ссылки на контекст, который Copilot использовал для генерации ответа, например, исходные файлы или документацию, а также кнопки для доступа к функционалу VS Code.

- Copilot Chat интегрируется в ваш рабочий процесс и помогает там, где это нужно:

- Начинайте чат прямо из редактора или терминала, чтобы получить помощь во время кодирования

- Используйте окно чата для постоянной поддержки AI-ассистента

- Запускайте Quick Chat, чтобы быстро задать вопрос и вернуться к работе

GitHub Copilot Chat можно использовать в различных сценариях:

- Ответы на вопросы по программированию и выбору оптимальных решений

- Объяснение чужого кода и предложения по улучшению

- Предложение исправлений кода

- Генерация unit-тестов

- Создание документации к коду

Рекомендуется ознакомиться с этой ссылкой [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Использование **@workspace** в Copilot Chat позволяет задавать вопросы по всему коду вашего проекта. Copilot интеллектуально находит релевантные файлы и символы, которые затем добавляет в ответ в виде ссылок и примеров кода.

Для ответа на ваш вопрос **@workspace** ищет информацию в тех же местах, что и разработчик при работе с кодом в VS Code:

- Все файлы в рабочей области, кроме тех, что игнорируются .gitignore

- Структура каталогов с вложенными папками и файлами

- Индекс поиска кода GitHub, если рабочая область — это репозиторий GitHub с индексом поиска

- Символы и определения в рабочей области

- Текущий выделенный текст или видимый текст в активном редакторе

Примечание: .gitignore игнорируется, если у вас открыт файл или выделен текст в игнорируемом файле.

Рекомендуется ознакомиться с этой ссылкой [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Подробнее о данном курсе**

GitHub Copilot значительно повысил эффективность программирования в компаниях, и многие организации хотят адаптировать его функционал под свои нужды. Многие предприятия создают кастомные расширения, похожие на GitHub Copilot, основанные на своих бизнес-сценариях и open source моделях. Для компаний такие расширения легче контролировать, но это может сказаться на пользовательском опыте. Ведь GitHub Copilot обладает более мощным функционалом для работы с общими сценариями и профессиональными задачами. Если удастся сохранить единый опыт использования, кастомизация корпоративного расширения станет более предпочтительной. GitHub Copilot Chat предоставляет API для расширения возможностей чата в корпоративных решениях. Поддержание единого пользовательского опыта при наличии кастомных функций — лучший подход.

В этом курсе основное внимание уделяется модели Phi-3 в сочетании с локальным NPU и гибридом Azure для создания кастомного агента в GitHub Copilot Chat ***@PHI3***, который помогает разработчикам генерировать код ***(@PHI3 /gen)*** и создавать код на основе изображений ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d095fe0b942687287803c03933d2d1d439d14e10fa1442a864d.ru.png)

### ***Примечание:*** 

В настоящее время курс реализован на AIPC Intel CPU и Apple Silicon. В дальнейшем планируется обновление версии для Qualcomm NPU.

## **Лабораторные работы**

| Название | Описание | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Установка(✅) | Настройка и установка необходимых окружений и инструментов | [Перейти](./HOL/AIPC/01.Installations.md) |[Перейти](./HOL/Apple/01.Installations.md) |
| Lab1 - Запуск Prompt flow с Phi-3-mini (✅) | Использование AIPC / Apple Silicon и локального NPU для генерации кода через Phi-3-mini | [Перейти](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Перейти](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Развертывание Phi-3-vision на Azure Machine Learning Service(✅) | Генерация кода с помощью развертывания модели Phi-3-vision из каталога Azure Machine Learning Service | [Перейти](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Перейти](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Создание агента @phi-3 в GitHub Copilot Chat(✅)  | Создание кастомного агента Phi-3 в GitHub Copilot Chat для генерации кода, графиков, RAG и др. | [Перейти](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Перейти](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Пример кода (✅)  | Скачать пример кода | [Перейти](../../../../../../../code/07.Lab/01/AIPC) | [Перейти](../../../../../../../code/07.Lab/01/Apple) |

## **Ресурсы**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Подробнее о GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Подробнее о GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Подробнее о GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Подробнее об Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Подробнее о каталоге моделей Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.