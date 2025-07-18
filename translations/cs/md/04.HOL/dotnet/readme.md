<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:41:11+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "cs"
}
-->
﻿## Vítejte v Phi laboratořích používajících C#

K dispozici je výběr laboratoří, které ukazují, jak integrovat různé výkonné verze modelů Phi v prostředí .NET.

## Požadavky

Před spuštěním ukázky se ujistěte, že máte nainstalováno:

**.NET 9:** Zkontrolujte, že máte na svém počítači nainstalovanou [nejnovější verzi .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Volitelné) Visual Studio nebo Visual Studio Code:** Budete potřebovat IDE nebo editor kódu, který umí spouštět .NET projekty. Doporučujeme [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) nebo [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Pomocí git** si lokálně naklonujte jednu z dostupných verzí Phi-3, Phi3.5 nebo Phi-4 z [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Stáhněte si Phi-4 ONNX modely** do svého počítače:

### přejděte do složky pro uložení modelů

```bash
cd c:\phi\models
```

### přidejte podporu pro lfs

```bash
git lfs install 
```

### naklonujte a stáhněte Phi-4 mini instruct model a Phi-4 multimodální model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Stáhněte si Phi-3 ONNX modely** do svého počítače:

### naklonujte a stáhněte Phi-3 mini 4K instruct model a Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Důležité:** Aktuální ukázky jsou navrženy pro použití ONNX verzí modelů. Výše uvedené kroky naklonují následující modely.

## O laboratořích

Hlavní řešení obsahuje několik ukázkových laboratoří, které demonstrují schopnosti modelů Phi pomocí C#.

| Projekt | Model | Popis |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 nebo Phi-3.5 | Ukázkový konzolový chat, který umožňuje uživateli klást otázky. Projekt načítá lokální ONNX Phi-3 model pomocí knihoven `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 nebo Phi-3.5 | Ukázkový konzolový chat, který umožňuje uživateli klást otázky. Projekt načítá lokální ONNX Phi-3 model pomocí knihoven `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 nebo Phi-3.5 | Ukázkový projekt, který používá lokální phi3 vision model k analýze obrázků. Projekt načítá lokální ONNX Phi-3 Vision model pomocí knihoven `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 nebo Phi-3.5 | Ukázkový projekt, který používá lokální phi3 vision model k analýze obrázků. Projekt načítá lokální ONNX Phi-3 Vision model pomocí knihoven `Microsoft.ML.OnnxRuntime`. Projekt také nabízí menu s různými možnostmi interakce s uživatelem. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Ukázkový konzolový chat, který umožňuje uživateli klást otázky. Projekt načítá lokální ONNX Phi-4 model pomocí knihoven `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Ukázkový konzolový chat, který umožňuje uživateli klást otázky. Projekt načítá lokální ONNX Phi-4 model pomocí knihoven `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Ukázkový konzolový chat, který umožňuje uživateli klást otázky. Projekt načítá lokální ONNX Phi-4 model pomocí knihoven `Microsoft.ML.OnnxRuntimeGenAI` a implementuje `IChatClient` z `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Ukázkový konzolový chat, který umožňuje uživateli klást otázky. Chat využívá paměť. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Ukázkový projekt, který používá lokální Phi-4 model k analýze obrázků a zobrazuje výsledek v konzoli. Projekt načítá lokální Phi-4-`multimodal-instruct-onnx` model pomocí knihoven `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Ukázkový projekt, který používá lokální Phi-4 model k analýze audio souboru, generuje přepis souboru a zobrazuje výsledek v konzoli. Projekt načítá lokální Phi-4-`multimodal-instruct-onnx` model pomocí knihoven `Microsoft.ML.OnnxRuntime`. |

## Jak spustit projekty

Pro spuštění projektů postupujte podle těchto kroků:

1. Naklonujte repozitář do svého počítače.

1. Otevřete terminál a přejděte do požadovaného projektu. Například spusťme `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Spusťte projekt příkazem

    ```bash
    dotnet run
    ```

1. Ukázkový projekt vyzve uživatele k zadání vstupu a odpovídá pomocí lokálního modelu.

   Běžící demo vypadá přibližně takto:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.