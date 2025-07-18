<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:31:05+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ru"
}
-->
﻿## Добро пожаловать в Phi labs с использованием C#

Здесь представлен набор лабораторных работ, демонстрирующих, как интегрировать различные версии мощных моделей Phi в среде .NET.

## Требования

Перед запуском примера убедитесь, что у вас установлено следующее:

**.NET 9:** Убедитесь, что на вашем компьютере установлена [последняя версия .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Необязательно) Visual Studio или Visual Studio Code:** Вам понадобится IDE или редактор кода, способный запускать проекты .NET. Рекомендуются [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) или [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Используя git**, клонируйте локально одну из доступных версий Phi-3, Phi3.5 или Phi-4 с [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Скачайте модели Phi-4 ONNX** на свой компьютер:

### перейдите в папку для хранения моделей

```bash
cd c:\phi\models
```

### добавьте поддержку lfs

```bash
git lfs install 
```

### клонируйте и скачайте модель Phi-4 mini instruct и мультимодальную модель Phi-4

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Скачайте модели Phi-3 ONNX** на свой компьютер:

### клонируйте и скачайте модель Phi-3 mini 4K instruct и модель Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Важно:** Текущие демонстрации рассчитаны на использование ONNX-версий моделей. Предыдущие шаги клонируют следующие модели.

## О лабораторных работах

Основное решение содержит несколько примеров лабораторных работ, демонстрирующих возможности моделей Phi с использованием C#.

| Проект | Модель | Описание |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 или Phi-3.5 | Пример консольного чата, позволяющий пользователю задавать вопросы. Проект загружает локальную ONNX-модель Phi-3 с помощью библиотек `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 или Phi-3.5 | Пример консольного чата, позволяющий пользователю задавать вопросы. Проект загружает локальную ONNX-модель Phi-3 с помощью библиотек `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 или Phi-3.5 | Пример проекта, использующего локальную модель phi3 vision для анализа изображений. Проект загружает локальную ONNX-модель Phi-3 Vision с помощью библиотек `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 или Phi-3.5 | Пример проекта, использующего локальную модель phi3 vision для анализа изображений. Проект загружает локальную ONNX-модель Phi-3 Vision с помощью библиотек `Microsoft.ML.OnnxRuntime`. Также проект предлагает меню с различными опциями для взаимодействия с пользователем. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Пример консольного чата, позволяющий пользователю задавать вопросы. Проект загружает локальную ONNX-модель Phi-4 с помощью библиотек `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Пример консольного чата, позволяющий пользователю задавать вопросы. Проект загружает локальную ONNX-модель Phi-4 с помощью библиотек `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Пример консольного чата, позволяющий пользователю задавать вопросы. Проект загружает локальную ONNX-модель Phi-4 с помощью библиотек `Microsoft.ML.OnnxRuntimeGenAI` и реализует интерфейс `IChatClient` из `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Пример консольного чата, позволяющий пользователю задавать вопросы. В чате реализована память. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Пример проекта, использующего локальную модель Phi-4 для анализа изображений с выводом результата в консоль. Проект загружает локальную модель Phi-4-`multimodal-instruct-onnx` с помощью библиотек `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Пример проекта, использующего локальную модель Phi-4 для анализа аудиофайла, генерации транскрипта и вывода результата в консоль. Проект загружает локальную модель Phi-4-`multimodal-instruct-onnx` с помощью библиотек `Microsoft.ML.OnnxRuntime`. |

## Как запустить проекты

Чтобы запустить проекты, выполните следующие шаги:

1. Клонируйте репозиторий на свой компьютер.

1. Откройте терминал и перейдите в нужный проект. Например, запустим `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Запустите проект командой

    ```bash
    dotnet run
    ```

1. Пример проекта запросит ввод пользователя и ответит, используя локальную модель.

   Запущенная демонстрация будет выглядеть примерно так:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.