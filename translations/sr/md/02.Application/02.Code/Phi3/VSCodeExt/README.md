<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:45:28+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "sr"
}
-->
# **Направите свој Visual Studio Code GitHub Copilot Chat са Microsoft Phi-3 породицом**

Да ли сте користили workspace агента у GitHub Copilot Chat? Желите ли да направите агента за код вашег тима? Овај практични лабораторијски рад има за циљ да комбинује open source модел за изградњу пословног агента за код на нивоу предузећа.

## **Основа**

### **Зашто изабрати Microsoft Phi-3**

Phi-3 је серија модела која укључује phi-3-mini, phi-3-small и phi-3-medium, засноване на различитим параметрима тренинга за генерисање текста, завршетак дијалога и генерисање кода. Постоји и phi-3-vision заснован на Vision технологији. Погодан је за предузећа или различите тимове за креирање офлајн генеративних AI решења.

Препоручује се читање овог линка [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat екстензија вам пружа интерфејс за ћаскање који вам омогућава интеракцију са GitHub Copilot-ом и добијање одговора на питања везана за програмирање директно унутар VS Code-а, без потребе да претражујете документацију или онлајн форуме.

Copilot Chat може користити истицање синтаксе, увлачење и друге формате како би одговор био јаснији. У зависности од типа питања корисника, резултат може садржати линкове ка контексту који је Copilot користио за генерисање одговора, као што су изворни код или документација, или дугмад за приступ функцијама VS Code-а.

- Copilot Chat се интегрише у ваш развојни ток и пружа помоћ тамо где вам је потребна:

- Започните inline разговор директно из едитора или терминала за помоћ док кодите

- Користите Chat приказ да имате AI асистента поред себе који вам помаже у сваком тренутку

- Покрените Quick Chat да поставите брзо питање и вратите се свом раду

GitHub Copilot Chat можете користити у различитим сценаријима, као што су:

- Одговарање на питања о томе како најбоље решити проблем

- Објашњавање туђег кода и предлагање побољшања

- Предлагање исправки кода

- Генерисање јединичних тест случајева

- Генерисање документације кода

Препоручује се читање овог линка [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Референцирање **@workspace** у Copilot Chat-у вам омогућава да постављате питања у вези са целокупном базом кода. На основу питања, Copilot интелигентно проналази релевантне фајлове и симболе, које затим користи у одговору као линкове и примере кода.

Да би одговорио на ваше питање, **@workspace** претражује исте изворе које би програмер користио приликом навигације кроз код у VS Code-у:

- Сви фајлови у workspace-у, осим оних које .gitignore фајл игнорише

- Структура директоријума са угнежђеним именима фасцикли и фајлова

- GitHub-ов индекс претраге кода, ако је workspace GitHub репозиторијум и индексиран је код претраге

- Симболи и дефиниције у workspace-у

- Тренутно изабрани текст или видљиви текст у активном едитору

Напомена: .gitignore се игнорише ако имате отворен фајл или сте изабрали текст унутар игнорисаног фајла.

Препоручује се читање овог линка [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Сазнајте више о овом лабораторијском раду**

GitHub Copilot је знатно побољшао ефикасност програмирања у предузећима, и свака компанија жели да прилагоди релевантне функције GitHub Copilot-а. Многа предузећа су прилагодила екстензије сличне GitHub Copilot-у на основу својих пословних сценарија и open source модела. За предузећа, прилагођене екстензије су лакше за контролу, али то утиче и на корисничко искуство. Ипак, GitHub Copilot има јаче функције за опште сценарије и професионалност. Ако се искуство може одржати конзистентним, боље је прилагодити сопствену екстензију предузећа. GitHub Copilot Chat пружа релевантне API-је за предузећа да прошире искуство ћаскања. Одржавање конзистентног искуства уз прилагођене функције пружа боље корисничко искуство.

Овај лабораторијски рад углавном користи Phi-3 модел у комбинацији са локалним NPU и Azure хибридом за изградњу прилагођеног агента у GitHub Copilot Chat-у ***@PHI3*** који помаже развојним инжењерима у предузећима да заврше генерисање кода ***(@PHI3 /gen)*** и генеришу код на основу слика ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d09.sr.png)

### ***Напомена:*** 

Овај лабораторијски рад је тренутно имплементиран на AIPC Intel CPU и Apple Silicon. Наставићемо са ажурирањем Qualcomm верзије NPU.


## **Лабораторија**


| Назив | Опис | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Инсталације(✅) | Конфигурисање и инсталација релевантних окружења и алата за инсталацију | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Покретање Prompt flow са Phi-3-mini (✅) | У комбинацији са AIPC / Apple Silicon, коришћење локалног NPU за креирање генерисања кода преко Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Деплој Phi-3-vision на Azure Machine Learning Service(✅) | Генерисање кода деплојем Azure Machine Learning Service Model Catalog-а - Phi-3-vision слика | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Креирање @phi-3 агента у GitHub Copilot Chat(✅)  | Креирање прилагођеног Phi-3 агента у GitHub Copilot Chat-у за завршетак генерисања кода, генерисање графикона, RAG и сл. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Пример кода (✅)  | Преузимање пример кода | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Ресурси**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Сазнајте више о GitHub Copilot-у [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Сазнајте више о GitHub Copilot Chat-у [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Сазнајте више о GitHub Copilot Chat API-ју [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Сазнајте више о Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Сазнајте више о Azure AI Foundry Model Catalog-у [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.