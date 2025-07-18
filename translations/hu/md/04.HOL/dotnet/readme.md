<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:40:44+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "hu"
}
-->
﻿## Üdvözlünk a Phi laborokban C# használatával

Különböző laborok állnak rendelkezésre, amelyek bemutatják, hogyan lehet integrálni a Phi modellek különböző verzióit egy .NET környezetben.

## Előfeltételek

A minta futtatása előtt győződj meg róla, hogy a következők telepítve vannak:

**.NET 9:** Győződj meg róla, hogy a gépeden a [legfrissebb .NET verzió](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) telepítve van.

**(Opcionális) Visual Studio vagy Visual Studio Code:** Szükséged lesz egy IDE-re vagy kódszerkesztőre, amely képes .NET projekteket futtatni. Ajánlott a [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) vagy a [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Git használata:** Klónozd le helyileg a Phi-3, Phi3.5 vagy Phi-4 verziók egyikét a [Hugging Face-ről](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Phi-4 ONNX modellek letöltése** a helyi gépedre:

### Navigálj a mappába, ahová a modelleket tárolni szeretnéd

```bash
cd c:\phi\models
```

### Add hozzá az lfs támogatást

```bash
git lfs install 
```

### Klónozd és töltsd le a Phi-4 mini instruct modellt és a Phi-4 multimodális modellt

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX modellek letöltése** a helyi gépedre:

### Klónozd és töltsd le a Phi-3 mini 4K instruct modellt és a Phi-3 vision 128K modellt

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Fontos:** A jelenlegi demók az ONNX verziókat használják. A fenti lépések ezeknek a modelleknek a klónozását végzik el.

## A laborokról

A fő megoldás több mintát tartalmazó labort, amelyek bemutatják a Phi modellek képességeit C# használatával.

| Projekt | Modell | Leírás |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 vagy Phi-3.5 | Konzolos chat minta, amely lehetővé teszi a felhasználó számára kérdések feltevését. A projekt egy helyi ONNX Phi-3 modellt tölt be a `Microsoft.ML.OnnxRuntime` könyvtárak segítségével. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 vagy Phi-3.5 | Konzolos chat minta, amely lehetővé teszi a felhasználó számára kérdések feltevését. A projekt egy helyi ONNX Phi-3 modellt tölt be a `Microsoft.Semantic.Kernel` könyvtárak segítségével. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 vagy Phi-3.5 | Ez egy minta projekt, amely egy helyi phi3 vision modellt használ képek elemzésére. A projekt egy helyi ONNX Phi-3 Vision modellt tölt be a `Microsoft.ML.OnnxRuntime` könyvtárak segítségével. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 vagy Phi-3.5 | Ez egy minta projekt, amely egy helyi phi3 vision modellt használ képek elemzésére. A projekt egy helyi ONNX Phi-3 Vision modellt tölt be a `Microsoft.ML.OnnxRuntime` könyvtárak segítségével. A projekt emellett menüt is kínál különböző opciókkal a felhasználóval való interakcióhoz. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Konzolos chat minta, amely lehetővé teszi a felhasználó számára kérdések feltevését. A projekt egy helyi ONNX Phi-4 modellt tölt be a `Microsoft.ML.OnnxRuntime` könyvtárak segítségével. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Konzolos chat minta, amely lehetővé teszi a felhasználó számára kérdések feltevését. A projekt egy helyi ONNX Phi-4 modellt tölt be a `Semantic Kernel` könyvtárak segítségével. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Konzolos chat minta, amely lehetővé teszi a felhasználó számára kérdések feltevését. A projekt egy helyi ONNX Phi-4 modellt tölt be a `Microsoft.ML.OnnxRuntimeGenAI` könyvtárak segítségével, és megvalósítja az `IChatClient` interfészt a `Microsoft.Extensions.AI`-ból. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Konzolos chat minta, amely lehetővé teszi a felhasználó számára kérdések feltevését. A chat memóriát is használ. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Ez egy minta projekt, amely egy helyi Phi-4 modellt használ képek elemzésére, az eredményt a konzolon jeleníti meg. A projekt egy helyi Phi-4-`multimodal-instruct-onnx` modellt tölt be a `Microsoft.ML.OnnxRuntime` könyvtárak segítségével. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Ez egy minta projekt, amely egy helyi Phi-4 modellt használ egy hangfájl elemzésére, a fájl átiratának generálására és az eredmény konzolon való megjelenítésére. A projekt egy helyi Phi-4-`multimodal-instruct-onnx` modellt tölt be a `Microsoft.ML.OnnxRuntime` könyvtárak segítségével. |

## Hogyan futtasd a projekteket

A projektek futtatásához kövesd az alábbi lépéseket:

1. Klónozd le a repozitóriumot a helyi gépedre.

1. Nyiss meg egy terminált, és navigálj a kívánt projekthez. Például futtassuk a `LabsPhi4-Chat-01OnnxRuntime` projektet.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Futtasd a projektet a következő paranccsal

    ```bash
    dotnet run
    ```

1. A minta projekt kér egy felhasználói bemenetet, és a helyi modell segítségével válaszol.

   A futó demo hasonló ehhez:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.