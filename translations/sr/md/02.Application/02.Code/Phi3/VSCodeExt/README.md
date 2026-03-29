# **Направите свој Visual Studio Code GitHub Copilot Chat са Microsoft Phi-3 породицом**

Да ли сте користили агента радног простора у GitHub Copilot Chat? Желите ли да направите агента за код свог тима? Овај практични лабораторијски рад има за циљ да комбинује open source модел ради изградње код пословног агента на нивоу предузећа.

## **Основа**

### **Зашто одабрати Microsoft Phi-3**

Phi-3 је породична серија, укључујући phi-3-mini, phi-3-small и phi-3-medium на основу различитих параметара за тренирање за генерисање текста, завршетак дијалога и генерисање кода. Постоји и phi-3-vision заснован на Vision. Погодан је за предузећа или различите тимове за креирање офлајн генеративних AI решења.

Препоручује се читање овог линка [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat екстензија вам даје интерфејс за чет који вам омогућава да комуницирате са GitHub Copilot-ом и добијате одговоре на питања везана за програмирање директно унутар VS Code, без потребе да прелазите на документацију или претражујете онлајн форуме.

Copilot Chat може користити истицање синтаксе, увлачење и друге форматске карактеристике да би повећао јасноћу генерисаног одговора. У зависности од врсте питања корисника, резултат може садржати линкове ка контексту који је Copilot користио за генерисање одговора, као што су изворни фајлови или документација, или дугмад за приступ функцијама VS Code-а.

- Copilot Chat се интегрише у ваш развојни ток и пружа вам помоћ тамо где вам је потребна:

- Започните inline чет разговор директно из едитора или терминала за помоћ док програмирате

- Користите Chat view да имате AI асистента поред себе који вам помаже у сваком тренутку

- Покрените Quick Chat да поставите брзо питање и вратите се свом раду

Можете користити GitHub Copilot Chat у различитим сценаријима, као што су:

- Одговарање на питања о кодирању о томе како најбоље решити проблем

- Објашњавање туђег кода и предлагање побољшања

- Предлагање исправки кода

- Генерисање јединичних тест случајева

- Генерисање документације кода

Препоручује се читање овог линка [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Референцирање **@workspace** у Copilot Chat вам омогућава да постављате питања о целом вашем коду. На основу питања, Copilot интелигентно проналази релевантне фајлове и симболе, које затим користи у свом одговору као линкове и примере кода.

Да би одговорио на ваше питање, **@workspace** претражује исте изворе које би програмер користио приликом навигације кроз код у VS Code-у:

- Сви фајлови у радном простору, осим фајлова које .gitignore игнорише

- Структура директоријума са уређеним именима фолдера и фајлова

- GitHub-ов индекс претраге кода, ако је радни простор GitHub репозиторијум и индексиран је код претраге

- Симболи и дефиниције у радном простору

- Тренутно изабрани текст или видљиви текст у активном едитору

Напомена: .gitignore се заобилази ако имате отворен фајл или изабран текст унутар игнорисаног фајла.

Препоручује се читање овог линка [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Сазнајте више о овој лабораторији**

GitHub Copilot је значајно побољшао ефикасност програмирања у предузећима, и свака компанија жели да прилагоди релевантне функције GitHub Copilot-а. Многе компаније су прилагодиле екстензије сличне GitHub Copilot-у на основу својих пословних сценарија и open source модела. За предузећа, прилагођене екстензије су лакше за контролу, али то утиче и на корисничко искуство. Ипак, GitHub Copilot има снажније функције у раду са општим сценаријима и стручностима. Ако се искуство може одржати конзистентним, било би боље прилагодити сопствену екстензију предузећа. GitHub Copilot Chat пружа релевантне API-је за предузећа да прошире искуство у ћаскању. Одржавање конзистентног искуства и имање прилагођених функција је боље корисничко искуство.

Ова лабораторија углавном користи Phi-3 модел у комбинацији са локалним NPU-ом и Azure хибридом да изгради прилагођеног агента у GitHub Copilot Chat ***@PHI3*** који помаже развојним програмерима у предузећу да заврше генерисање кода***(@PHI3 /gen)*** и генеришу код на основу слика ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/sr/cover.1017ebc9a7c46d09.webp)

### ***Напомена:*** 

Ова лабораторија је тренутно имплементирана на AIPC Intel CPU и Apple Silicon. Наставићемо са ажурирањем Qualcomm верзије NPU.


## **Лабораторија**


| Назив | Опис | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Инсталације(✅) | Конфигуришите и инсталирајте повезана окружења и алате за инсталацију | [Иди](./HOL/AIPC/01.Installations.md) |[Иди](./HOL/Apple/01.Installations.md) |
| Lab1 - Покрени Prompt flow са Phi-3-mini (✅) | У комбинацији са AIPC / Apple Silicon, користећи локални NPU за креирање генерисања кода преко Phi-3-mini | [Иди](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Иди](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Деплоy Phi-3-vision на Azure Machine Learning Service(✅) | Генеришите код постављањем Azure Machine Learning Service Model каталога - Phi-3-vision слике | [Иди](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Иди](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Креирајте @phi-3 агента у GitHub Copilot Chat(✅)  | Направите прилагођеног Phi-3 агента у GitHub Copilot Chat за генерисање кода, генерисање кода графика, RAG, итд. | [Иди](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Иди](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Пример кода (✅)  | Преузмите пример кода | [Иди](../../../../../../../code/07.Lab/01/AIPC) | [Иди](../../../../../../../code/07.Lab/01/Apple) |


## **Ресурси**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Сазнајте више о GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Сазнајте више о GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Сазнајте више о GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Сазнајте више о Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Сазнајте више о Microsoft Foundry Model каталогу [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ограничење одговорности**:  
Овај документ је преведен помоћу AI сервиса за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на свом матерњем језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било какве неспоразуме или погрешне тумачења настале употребом овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->