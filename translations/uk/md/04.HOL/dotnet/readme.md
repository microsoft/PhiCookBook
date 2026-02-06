## Ласкаво просимо до лабораторій Phi з використанням C#

Тут представлено набір лабораторій, які демонструють, як інтегрувати різні потужні версії моделей Phi у середовищі .NET.

## Вимоги

Перед запуском прикладу переконайтеся, що у вас встановлено:

**.NET 9:** Переконайтеся, що на вашому комп’ютері встановлено [останні версії .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Опційно) Visual Studio або Visual Studio Code:** Вам знадобиться IDE або редактор коду, який підтримує запуск .NET проектів. Рекомендуються [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) або [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Використовуючи git** клонувати локально одну з доступних версій Phi-3, Phi3.5 або Phi-4 з [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Завантажте ONNX моделі Phi-4** на свій комп’ютер:

### перейдіть до папки для збереження моделей

```bash
cd c:\phi\models
```

### додайте підтримку lfs

```bash
git lfs install 
```

### клонувати та завантажити модель Phi-4 mini instruct і модель Phi-4 мультимодальну

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Завантажте ONNX моделі Phi-3** на свій комп’ютер:

### клонувати та завантажити модель Phi-3 mini 4K instruct і модель Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Важливо:** Поточні демо призначені для використання ONNX версій моделей. Попередні кроки клонують наступні моделі.

## Про лабораторії

Головне рішення містить кілька прикладів лабораторій, які демонструють можливості моделей Phi з використанням C#.

| Проєкт | Модель | Опис |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 або Phi-3.5 | Приклад консольного чату, який дозволяє користувачу ставити запитання. Проєкт завантажує локальну ONNX модель Phi-3 за допомогою бібліотек `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 або Phi-3.5 | Приклад консольного чату, який дозволяє користувачу ставити запитання. Проєкт завантажує локальну ONNX модель Phi-3 за допомогою бібліотек `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 або Phi-3.5 | Це приклад проєкту, який використовує локальну модель phi3 vision для аналізу зображень. Проєкт завантажує локальну ONNX модель Phi-3 Vision за допомогою бібліотек `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 або Phi-3.5 | Це приклад проєкту, який використовує локальну модель phi3 vision для аналізу зображень. Проєкт завантажує локальну ONNX модель Phi-3 Vision за допомогою бібліотек `Microsoft.ML.OnnxRuntime`. Проєкт також пропонує меню з різними опціями для взаємодії з користувачем. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Приклад консольного чату, який дозволяє користувачу ставити запитання. Проєкт завантажує локальну ONNX модель Phi-4 за допомогою бібліотек `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Приклад консольного чату, який дозволяє користувачу ставити запитання. Проєкт завантажує локальну ONNX модель Phi-4 за допомогою бібліотек `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Приклад консольного чату, який дозволяє користувачу ставити запитання. Проєкт завантажує локальну ONNX модель Phi-4 за допомогою бібліотек `Microsoft.ML.OnnxRuntimeGenAI` та реалізує `IChatClient` з `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Приклад консольного чату, який дозволяє користувачу ставити запитання. Чат підтримує пам’ять. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Це приклад проєкту, який використовує локальну модель Phi-4 для аналізу зображень з відображенням результату в консолі. Проєкт завантажує локальну модель Phi-4-`multimodal-instruct-onnx` за допомогою бібліотек `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Це приклад проєкту, який використовує локальну модель Phi-4 для аналізу аудіофайлу, генерує транскрипт файлу та відображає результат у консолі. Проєкт завантажує локальну модель Phi-4-`multimodal-instruct-onnx` за допомогою бібліотек `Microsoft.ML.OnnxRuntime`. |

## Як запускати проєкти

Щоб запустити проєкти, виконайте наступні кроки:

1. Клонуйте репозиторій на свій комп’ютер.

1. Відкрийте термінал і перейдіть до потрібного проєкту. Наприклад, запустимо `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Запустіть проєкт командою

    ```bash
    dotnet run
    ```

1. Приклад запитує введення користувача і відповідає, використовуючи локальну модель.

   Запущене демо виглядає приблизно так:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.