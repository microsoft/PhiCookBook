## Добродошли у Phi лабораторије користећи C#

Постоји избор лабораторија које показују како интегрисати моћне различите верзије Phi модела у .NET окружењу.

## Захтеви

Пре покретања примера, уверите се да имате инсталирано следеће:

**.NET 9:** Проверите да ли имате [најновију верзију .NET-а](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) инсталирану на вашем рачунару.

**(Опционо) Visual Studio или Visual Studio Code:** Потребан вам је IDE или уређивач кода који може да покреће .NET пројекте. Препоручују се [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) или [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Коришћење git-а** клонирајте локално једну од доступних Phi-3, Phi3.5 или Phi-4 верзија са [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Преузмите Phi-4 ONNX моделе** на ваш локални рачунар:

### идите у фасциклу за чување модела

```bash
cd c:\phi\models
```

### додајте подршку за lfs

```bash
git lfs install 
```

### клонирајте и преузмите Phi-4 mini instruct модел и Phi-4 мултимодални модел

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Преузмите Phi-3 ONNX моделе** на ваш локални рачунар:

### клонирајте и преузмите Phi-3 mini 4K instruct модел и Phi-3 vision 128K модел

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Важно:** Тренутни демо примери су дизајнирани да користе ONNX верзије модела. Претходни кораци клонирају следеће моделе.

## О лабораторијама

Главно решење садржи неколико пример лабораторија које демонстрирају могућности Phi модела користећи C#.

| Пројекат | Модел | Опис |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 или Phi-3.5 | Пример конзолног ћаскања који омогућава кориснику да поставља питања. Пројекат учитава локални ONNX Phi-3 модел користећи `Microsoft.ML.OnnxRuntime` библиотеке. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 или Phi-3.5 | Пример конзолног ћаскања који омогућава кориснику да поставља питања. Пројекат учитава локални ONNX Phi-3 модел користећи `Microsoft.Semantic.Kernel` библиотеке. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 или Phi-3.5 | Ово је пример пројекта који користи локални phi3 vision модел за анализу слика. Пројекат учитава локални ONNX Phi-3 Vision модел користећи `Microsoft.ML.OnnxRuntime` библиотеке. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 или Phi-3.5 | Ово је пример пројекта који користи локални phi3 vision модел за анализу слика. Пројекат учитава локални ONNX Phi-3 Vision модел користећи `Microsoft.ML.OnnxRuntime` библиотеке. Пројекат такође приказује мени са различитим опцијама за интеракцију са корисником. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Пример конзолног ћаскања који омогућава кориснику да поставља питања. Пројекат учитава локални ONNX Phi-4 модел користећи `Microsoft.ML.OnnxRuntime` библиотеке. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Пример конзолног ћаскања који омогућава кориснику да поставља питања. Пројекат учитава локални ONNX Phi-4 модел користећи `Semantic Kernel` библиотеке. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Пример конзолног ћаскања који омогућава кориснику да поставља питања. Пројекат учитава локални ONNX Phi-4 модел користећи `Microsoft.ML.OnnxRuntimeGenAI` библиотеке и имплементира `IChatClient` из `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Пример конзолног ћаскања који омогућава кориснику да поставља питања. Ћаскање има имплементирану меморију. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Ово је пример пројекта који користи локални Phi-4 модел за анализу слика и приказ резултата у конзоли. Пројекат учитава локални Phi-4-`multimodal-instruct-onnx` модел користећи `Microsoft.ML.OnnxRuntime` библиотеке. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Ово је пример пројекта који користи локални Phi-4 модел за анализу аудио фајла, генерише транскрипт фајла и приказује резултат у конзоли. Пројекат учитава локални Phi-4-`multimodal-instruct-onnx` модел користећи `Microsoft.ML.OnnxRuntime` библиотеке. |

## Како покренути пројекте

Да бисте покренули пројекте, пратите ове кораке:

1. Клонирајте репозиторијум на ваш локални рачунар.

1. Отворите терминал и идите у жељени пројекат. На пример, покренимо `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Покрените пројекат командом

    ```bash
    dotnet run
    ```

1. Пример пројекта тражи унос од корисника и одговара користећи локални модел.

   Тренутни демо изгледа слично овоме:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.