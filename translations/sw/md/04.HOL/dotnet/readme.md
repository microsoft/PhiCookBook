<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:40:26+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "sw"
}
-->
﻿## Karibu kwenye maabara za Phi zinazotumia C#

Kuna uteuzi wa maabara unaoonyesha jinsi ya kuunganisha matoleo tofauti yenye nguvu ya mifano ya Phi katika mazingira ya .NET.

## Mahitaji ya awali

Kabla ya kuendesha mfano, hakikisha umeweka yafuatayo:

**.NET 9:** Hakikisha umeweka [toleo la hivi karibuni la .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) kwenye kompyuta yako.

**(Hiari) Visual Studio au Visual Studio Code:** Utahitaji IDE au mhariri wa msimbo unaoweza kuendesha miradi ya .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) au [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) zinapendekezwa.

**Kutumia git** fanya clone kwa moja ya matoleo ya Phi-3, Phi3.5 au Phi-4 kutoka [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Pakua mifano ya Phi-4 ONNX** kwenye kompyuta yako:

### elekea kwenye folda ya kuhifadhi mifano

```bash
cd c:\phi\models
```

### ongeza msaada kwa lfs

```bash
git lfs install 
```

### fanya clone na pakua mfano wa Phi-4 mini instruct na mfano wa Phi-4 multimodal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Pakua mifano ya Phi-3 ONNX** kwenye kompyuta yako:

### fanya clone na pakua mfano wa Phi-3 mini 4K instruct na mfano wa Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Muhimu:** Maonyesho ya sasa yameundwa kutumia matoleo ya ONNX ya mfano. Hatua zilizopita hufanya clone ya mifano ifuatayo.

## Kuhusu Maabara

Suluhisho kuu lina maabara kadhaa za mfano zinazonyesha uwezo wa mifano ya Phi kwa kutumia C#.

| Mradi | Mfano | Maelezo |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 au Phi-3.5 | Mzungumzaji wa mfano wa console unaomruhusu mtumiaji kuuliza maswali. Mradi huu unachukua mfano wa ONNX Phi-3 ulioko ndani kwa kutumia maktaba za `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 au Phi-3.5 | Mzungumzaji wa mfano wa console unaomruhusu mtumiaji kuuliza maswali. Mradi huu unachukua mfano wa ONNX Phi-3 ulioko ndani kwa kutumia maktaba za `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 au Phi-3.5 | Huu ni mradi wa mfano unaotumia mfano wa phi3 vision ulioko ndani kuchambua picha. Mradi huu unachukua mfano wa ONNX Phi-3 Vision ulioko ndani kwa kutumia maktaba za `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 au Phi-3.5 | Huu ni mradi wa mfano unaotumia mfano wa phi3 vision ulioko ndani kuchambua picha. Mradi huu unachukua mfano wa ONNX Phi-3 Vision ulioko ndani kwa kutumia maktaba za `Microsoft.ML.OnnxRuntime`. Mradi pia unaonyesha menyu yenye chaguzi mbalimbali za kuingiliana na mtumiaji. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Mzungumzaji wa mfano wa console unaomruhusu mtumiaji kuuliza maswali. Mradi huu unachukua mfano wa ONNX Phi-4 ulioko ndani kwa kutumia maktaba za `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Mzungumzaji wa mfano wa console unaomruhusu mtumiaji kuuliza maswali. Mradi huu unachukua mfano wa ONNX Phi-4 ulioko ndani kwa kutumia maktaba za `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Mzungumzaji wa mfano wa console unaomruhusu mtumiaji kuuliza maswali. Mradi huu unachukua mfano wa ONNX Phi-4 ulioko ndani kwa kutumia maktaba za `Microsoft.ML.OnnxRuntimeGenAI` na kutekeleza `IChatClient` kutoka `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Mzungumzaji wa mfano wa console unaomruhusu mtumiaji kuuliza maswali. Mzungumzaji huyu ana kumbukumbu. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Huu ni mradi wa mfano unaotumia mfano wa Phi-4 ulioko ndani kuchambua picha na kuonyesha matokeo kwenye console. Mradi huu unachukua mfano wa Phi-4-`multimodal-instruct-onnx` ulioko ndani kwa kutumia maktaba za `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Huu ni mradi wa mfano unaotumia mfano wa Phi-4 ulioko ndani kuchambua faili la sauti, kutengeneza maandishi ya faili na kuonyesha matokeo kwenye console. Mradi huu unachukua mfano wa Phi-4-`multimodal-instruct-onnx` ulioko ndani kwa kutumia maktaba za `Microsoft.ML.OnnxRuntime`. |

## Jinsi ya Kuendesha Miradi

Ili kuendesha miradi, fuata hatua hizi:

1. Fanya clone ya hazina kwenye kompyuta yako.

1. Fungua terminal na elekea kwenye mradi unaotaka. Kwa mfano, tuchukue kuendesha `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Endesha mradi kwa amri

    ```bash
    dotnet run
    ```

1. Mradi wa mfano utauliza ingizo kutoka kwa mtumiaji na kujibu kwa kutumia mfano ulioko ndani.

   Demo inayotumika ni kama ifuatavyo:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.