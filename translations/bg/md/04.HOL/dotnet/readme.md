<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:42:06+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "bg"
}
-->
﻿## Добре дошли в лабораториите Phi с C#

Предлагат се няколко лаборатории, които показват как да се интегрират мощните различни версии на Phi моделите в .NET среда.

## Изисквания

Преди да стартирате примера, уверете се, че имате инсталирано следното:

**.NET 9:** Уверете се, че имате [най-новата версия на .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) инсталирана на вашия компютър.

**(По избор) Visual Studio или Visual Studio Code:** Ще ви трябва IDE или редактор на код, който може да изпълнява .NET проекти. Препоръчват се [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) или [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Използване на git** – клонирайте локално една от наличните версии Phi-3, Phi3.5 или Phi-4 от [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Изтеглете Phi-4 ONNX моделите** на вашия локален компютър:

### навигирайте до папката, където ще съхранявате моделите

```bash
cd c:\phi\models
```

### добавете поддръжка за lfs

```bash
git lfs install 
```

### клонирайте и изтеглете Phi-4 mini instruct модела и Phi-4 мултимодалния модел

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Изтеглете Phi-3 ONNX моделите** на вашия локален компютър:

### клонирайте и изтеглете Phi-3 mini 4K instruct модела и Phi-3 vision 128K модела

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Важно:** Текущите демонстрации са проектирани да използват ONNX версиите на модела. Предходните стъпки клонират следните модели.

## За лабораториите

Основното решение съдържа няколко примерни лаборатории, които демонстрират възможностите на Phi моделите с C#.

| Проект | Модел | Описание |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 или Phi-3.5 | Примерен конзолен чат, който позволява на потребителя да задава въпроси. Проектът зарежда локален ONNX Phi-3 модел с помощта на библиотеките `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 или Phi-3.5 | Примерен конзолен чат, който позволява на потребителя да задава въпроси. Проектът зарежда локален ONNX Phi-3 модел с помощта на библиотеките `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 или Phi-3.5 | Това е примерен проект, който използва локален phi3 vision модел за анализ на изображения. Проектът зарежда локален ONNX Phi-3 Vision модел с помощта на библиотеките `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 или Phi-3.5 | Това е примерен проект, който използва локален phi3 vision модел за анализ на изображения. Проектът зарежда локален ONNX Phi-3 Vision модел с помощта на библиотеките `Microsoft.ML.OnnxRuntime`. Проектът също така представя меню с различни опции за взаимодействие с потребителя. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Примерен конзолен чат, който позволява на потребителя да задава въпроси. Проектът зарежда локален ONNX Phi-4 модел с помощта на библиотеките `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Примерен конзолен чат, който позволява на потребителя да задава въпроси. Проектът зарежда локален ONNX Phi-4 модел с помощта на библиотеките `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Примерен конзолен чат, който позволява на потребителя да задава въпроси. Проектът зарежда локален ONNX Phi-4 модел с помощта на библиотеките `Microsoft.ML.OnnxRuntimeGenAI` и имплементира `IChatClient` от `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Примерен конзолен чат, който позволява на потребителя да задава въпроси. Чатът поддържа памет. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Това е примерен проект, който използва локален Phi-4 модел за анализ на изображения и показва резултата в конзолата. Проектът зарежда локален Phi-4-`multimodal-instruct-onnx` модел с помощта на библиотеките `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Това е примерен проект, който използва локален Phi-4 модел за анализ на аудио файл, генерира транскрипция на файла и показва резултата в конзолата. Проектът зарежда локален Phi-4-`multimodal-instruct-onnx` модел с помощта на библиотеките `Microsoft.ML.OnnxRuntime`. |

## Как да стартирате проектите

За да стартирате проектите, следвайте тези стъпки:

1. Клонирайте репозитория на вашия локален компютър.

1. Отворете терминал и навигирайте до желания проект. Например, нека стартираме `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Стартирайте проекта с командата

    ```bash
    dotnet run
    ```

1. Примерният проект ще поиска въвеждане от потребителя и ще отговори, използвайки локалния модел.

   Стартиращото демо изглежда подобно на това:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.