# **Создайте собственный GitHub Copilot Chat для Visual Studio Code с семейством Microsoft Phi-3**

Вы использовали агент рабочего пространства в GitHub Copilot Chat? Хотите создать собственного агента кода для вашей команды? Этот практический курс надеется объединить открытую модель для создания корпоративного бизнес-агента по работе с кодом.

## **Основы**

### **Почему выбирают Microsoft Phi-3**

Phi-3 — это семейство моделей, включающее phi-3-mini, phi-3-small и phi-3-medium, основанные на разных параметрах обучения для генерации текста, завершения диалогов и генерации кода. Также есть phi-3-vision, основанная на Vision. Она подходит для предприятий или различных команд для создания офлайн-решений на базе генеративного ИИ.

Рекомендуется ознакомиться с этой ссылкой [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Расширение GitHub Copilot Chat предоставляет интерфейс чата, который позволяет взаимодействовать с GitHub Copilot и получать ответы на вопросы, связанные с программированием, непосредственно в VS Code, без необходимости искать документацию или форумы онлайн.

Copilot Chat может использовать подсветку синтаксиса, отступы и другие функции форматирования для повышения ясности сгенерированного ответа. В зависимости от типа вашего вопроса результат может содержать ссылки на контекст, который Copilot использовал для генерации ответа, например файлы исходного кода или документацию, либо кнопки для доступа к функционалу VS Code.

- Copilot Chat интегрируется в ваш рабочий процесс разработчика и предоставляет помощь там, где это нужно:

- Начните разговор в чате прямо из редактора или терминала, чтобы получить помощь во время кодирования

- Используйте вид чата, чтобы иметь ИИ-ассистента на боевом экране в любое время

- Запустите Quick Chat, чтобы задать быстрый вопрос и вернуться к работе

Вы можете использовать GitHub Copilot Chat в различных сценариях, таких как:

- Ответы на вопросы по программированию о том, как лучше решить задачу

- Объяснение чужого кода и предложение улучшений

- Предложение исправлений кода

- Генерация тестов для кода

- Генерация документации к коду

Рекомендуется ознакомиться с этой ссылкой [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Обращение к **@workspace** в Copilot Chat позволяет задавать вопросы по всему вашему коду. Исходя из вопроса, Copilot интеллектуально извлекает релевантные файлы и символы, которые затем включаются в ответ в виде ссылок и примеров кода.

Чтобы ответить на ваш вопрос, **@workspace** ищет по тем же источникам, которые использует разработчик при навигации по коду в VS Code:

- Все файлы в рабочем пространстве, кроме файлов, игнорируемых .gitignore

- Структура каталогов с вложенными папками и именами файлов

- Индекс поиска кода GitHub, если рабочее пространство является репозиторием GitHub и индексируется поиском кода

- Символы и определения в рабочем пространстве

- Текущий выделенный текст или видимый текст в активном редакторе

Примечание: .gitignore игнорируется, если у вас открыт файл или выделен текст внутри игнорируемого файла.

Рекомендуется ознакомиться с этой ссылкой [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Подробнее об этом курсе**

GitHub Copilot значительно повысил эффективность программирования в предприятиях, и каждое предприятие хочет настроить соответствующие функции GitHub Copilot. Многие организации создали собственные расширения, похожие на GitHub Copilot, на основе своих бизнес-сценариев и открытых моделей. Для предприятий кастомные расширения проще контролировать, но это влияет и на пользовательский опыт. Ведь GitHub Copilot обладает более широкими возможностями в работе с общими сценариями и профессиональностью. Если удастся сохранить единый опыт, то будет лучше настроить собственное расширение для предприятия. GitHub Copilot Chat предоставляет соответствующие API для расширения опыта чата предприятиями. Поддержание согласованного пользовательского опыта и наличие кастомных функций дают лучший опыт для пользователей.

В этом курсе в основном используется модель Phi-3 в сочетании с локальным NPU и гибридом Azure для создания кастомного агента в GitHub Copilot Chat ***@PHI3***, чтобы помогать корпоративным разработчикам создавать код ***(@PHI3 /gen)*** и генерировать код на основе изображений ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/ru/cover.1017ebc9a7c46d09.webp)

### ***Примечание:*** 

Этот курс в настоящее время реализован на AIPC для Intel CPU и Apple Silicon. Мы продолжим обновления версии Qualcomm NPU.


## **Лаборатория**


| Название | Описание | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Установка(✅) | Конфигурирование и установка необходимых окружений и инструментов установки | [Перейти](./HOL/AIPC/01.Installations.md) |[Перейти](./HOL/Apple/01.Installations.md) |
| Lab1 - Запуск Prompt flow с Phi-3-mini (✅) | В сочетании с AIPC / Apple Silicon, использование локального NPU для создания генерации кода через Phi-3-mini | [Перейти](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Перейти](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Развертывание Phi-3-vision на Azure Machine Learning Service(✅) | Генерация кода с помощью развернутого в Azure Machine Learning Service каталога моделей — Phi-3-vision image | [Перейти](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Перейти](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Создание агента @phi-3 в GitHub Copilot Chat(✅)  | Создание кастомного агента Phi-3 в GitHub Copilot Chat для генерации кода, графиков, RAG и др. | [Перейти](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Перейти](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Пример кода (✅)  | Скачивание примера кода | [Перейти](../../../../../../../code/07.Lab/01/AIPC) | [Перейти](../../../../../../../code/07.Lab/01/Apple) |


## **Ресурсы**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Узнайте больше о GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Узнайте больше о GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Узнайте больше о GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Узнайте больше о Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Узнайте больше о каталоге моделей Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса искусственного интеллекта [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Исходный документ на оригинальном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется воспользоваться профессиональным переводом, выполненным человеком. Мы не несем ответственности за любые недоразумения или неверные толкования, вызванные использованием данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->