# **Създайте собствен Visual Studio Code GitHub Copilot Chat с Microsoft Phi-3 Family**

Използвали ли сте workspace агент в GitHub Copilot Chat? Искате ли да създадете собствен код агент за вашия екип? Тази практическа лаборатория има за цел да комбинира отворения модел с цел изграждане на корпоративен бизнес агент за кодиране.

## **Основи**

### **Защо да изберете Microsoft Phi-3**

Phi-3 е семейство серии, включващо phi-3-mini, phi-3-small и phi-3-medium, базирани на различни тренировъчни параметри за генериране на текст, диалогично завършване и генериране на код. Има и phi-3-vision, базиран на Vision. Подходящ е за предприятия или различни екипи за създаване на офлайн генеративни AI решения.

Препоръчително е да прочетете тази връзка [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Разширението GitHub Copilot Chat ви предоставя чат интерфейс, който ви позволява да взаимодействате с GitHub Copilot и да получавате отговори на въпроси, свързани с кода, директно във VS Code, без да се налага да навигирате през документация или да търсите в онлайн форуми.

Copilot Chat може да използва оцветяване на синтаксиса, отстъпи и други форматни функции, за да направи генерирания отговор по-ясен. В зависимост от типа въпрос от потребителя, резултатът може да съдържа връзки към контекст, използван от Copilot за генериране на отговора, като изходни кодови файлове или документация, или бутони за достъп до функционалности на VS Code.

- Copilot Chat се интегрира във вашия разработчиески поток и ви помага там, където имате нужда:

- Започнете чат конверсация директно от редактора или терминала, за да получите помощ докато кодирате

- Използвайте Chat изгледа, за да имате AI асистент под ръка по всяко време

- Стартирайте Quick Chat, за да зададете бърз въпрос и да се върнете към работата си

Можете да използвате GitHub Copilot Chat в различни сценарии, като например:

- Отговаряне на въпроси за кодирането за най-доброто решаване на проблем

- Обяснение на чужд код и предлагане на подобрения

- Предлагане на корекции на код

- Генериране на тестови единици

- Генериране на документация за код

Препоръчително е да прочетете тази връзка [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Позоваването на **@workspace** в Copilot Chat ви позволява да задавате въпроси за целия си кодов базис. Въз основа на въпроса, Copilot интелигентно извлича релевантни файлове и символи, които след това елементи при отговора си като връзки и кодови примери.

За да отговори на въпроса ви, **@workspace** търси през същите източници, които един разработчик би използвал при навигация из кода във VS Code:

- Всички файлове в работното пространство, с изключение на файлове, игнорирани от .gitignore файл

- Структурата на директории с вложени папки и имена на файлове

- Индекса за търсене на код на GitHub, ако работното пространство е GitHub репозитория и е индексиран от търсенето

- Символи и дефиниции в работното пространство

- В момента избрания текст или видимия текст в активния редактор

Забележка: .gitignore се игнорира, ако имате отворен файл или е избран текст във файл, който е игнориран.

Препоръчително е да прочетете тази връзка [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Научете повече за тази лаборатория**

GitHub Copilot значително подобри ефективността на програмиране в предприятията и всяко предприятие желае да персонализира съответните функции на GitHub Copilot. Много предприятия са създали персонализирани разширения, подобни на GitHub Copilot, базирани на собствените им бизнес сценарии и отворени модели. За предприятията персонализираните разширения са по-лесни за контрол, но това също влияе на потребителското изживяване. Все пак GitHub Copilot има по-силни функции при справяне с общи сценарии и професионалност. Ако може да се запази еднообразно изживяване, по-добре е да се персонализира собственото разширение на предприятието. GitHub Copilot Chat предоставя съответни API-та за предприятията да разширят чата. Поддържането на последователно изживяване и наличието на персонализирани функции е по-добро потребителско изживяване.

Тази лаборатория основно използва модела Phi-3 в комбинация с локалния NPU и хибрид Azure за изграждане на персонализиран Агент в GitHub Copilot Chat ***@PHI3*** за подпомагане на корпоративните разработчици при завършване на генериране на код ***(@PHI3 /gen)*** и генериране на код на базата на изображения ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/bg/cover.1017ebc9a7c46d09.webp)

### ***Забележка:*** 

Тази лаборатория е в момента реализирана в AIPC за Intel CPU и Apple Silicon. Ще продължим да обновяваме Qualcomm версията на NPU.


## **Лаборатория**


| Име | Описание | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Инсталации(✅) | Конфигуриране и инсталиране на свързаните среди и инструменти | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Изпълнение на Prompt flow с Phi-3-mini (✅) | В комбинация с AIPC / Apple Silicon, използване на локален NPU за генериране на код чрез Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Разгръщане на Phi-3-vision в Azure Machine Learning Service(✅) | Генериране на код чрез разгръщане на каталог моделите на Azure Machine Learning Service - Phi-3-vision image | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Създаване на @phi-3 агент в GitHub Copilot Chat(✅)  | Създаване на персонализиран Phi-3 агент в GitHub Copilot Chat за завършване на генериране на код, генериране на графичен код, RAG и др. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Примерен код (✅)  | Изтегляне на примерен код | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Ресурси**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Научете повече за GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Научете повече за GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Научете повече за API на GitHub Copilot Chat [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Научете повече за Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Научете повече за каталог моделите на Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->