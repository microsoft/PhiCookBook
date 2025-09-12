<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-09-12T14:47:35+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "lt"
}
-->
## Sveiki atvykę į Phi laboratorijas naudojant C#

Čia rasite laboratorijų rinkinį, kuris parodo, kaip integruoti skirtingas galingas Phi modelių versijas .NET aplinkoje.

## Reikalavimai

Prieš paleisdami pavyzdį, įsitikinkite, kad turite įdiegę šiuos dalykus:

**.NET 9:** Įsitikinkite, kad jūsų kompiuteryje įdiegta [naujausia .NET versija](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Pasirinktinai) Visual Studio arba Visual Studio Code:** Jums reikės IDE arba kodo redaktoriaus, kuris palaiko .NET projektų vykdymą. Rekomenduojama naudoti [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) arba [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Naudojant git** lokaliai nuklonuokite vieną iš galimų Phi-3, Phi3.5 arba Phi-4 versijų iš [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Atsisiųskite Phi-4 ONNX modelius** į savo kompiuterį:

### pereikite į aplanką, kuriame bus saugomi modeliai

```bash
cd c:\phi\models
```

### pridėkite lfs palaikymą

```bash
git lfs install 
```

### nuklonuokite ir atsisiųskite Phi-4 mini instruct modelį ir Phi-4 multimodal modelį

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Atsisiųskite Phi-3 ONNX modelius** į savo kompiuterį:

### nuklonuokite ir atsisiųskite Phi-3 mini 4K instruct modelį ir Phi-3 vision 128K modelį

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Svarbu:** Dabartiniai demonstraciniai projektai yra sukurti naudoti ONNX modelių versijas. Ankstesni žingsniai nuklonuoja šiuos modelius.

## Apie laboratorijas

Pagrindinis sprendimas apima kelis pavyzdinius laboratorijų projektus, kurie demonstruoja Phi modelių galimybes naudojant C#.

| Projektas | Modelis | Aprašymas |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 arba Phi-3.5 | Pavyzdinis konsolės pokalbis, leidžiantis vartotojui užduoti klausimus. Projektas įkelia vietinį ONNX Phi-3 modelį naudojant `Microsoft.ML.OnnxRuntime` bibliotekas. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 arba Phi-3.5 | Pavyzdinis konsolės pokalbis, leidžiantis vartotojui užduoti klausimus. Projektas įkelia vietinį ONNX Phi-3 modelį naudojant `Microsoft.Semantic.Kernel` bibliotekas. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 arba Phi-3.5 | Tai pavyzdinis projektas, kuris naudoja vietinį Phi-3 vision modelį vaizdų analizei. Projektas įkelia vietinį ONNX Phi-3 Vision modelį naudojant `Microsoft.ML.OnnxRuntime` bibliotekas. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 arba Phi-3.5 | Tai pavyzdinis projektas, kuris naudoja vietinį Phi-3 vision modelį vaizdų analizei. Projektas įkelia vietinį ONNX Phi-3 Vision modelį naudojant `Microsoft.ML.OnnxRuntime` bibliotekas. Projektas taip pat pateikia meniu su įvairiomis sąveikos su vartotoju galimybėmis. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Pavyzdinis konsolės pokalbis, leidžiantis vartotojui užduoti klausimus. Projektas įkelia vietinį ONNX Phi-4 modelį naudojant `Microsoft.ML.OnnxRuntime` bibliotekas. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Pavyzdinis konsolės pokalbis, leidžiantis vartotojui užduoti klausimus. Projektas įkelia vietinį ONNX Phi-4 modelį naudojant `Semantic Kernel` bibliotekas. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Pavyzdinis konsolės pokalbis, leidžiantis vartotojui užduoti klausimus. Projektas įkelia vietinį ONNX Phi-4 modelį naudojant `Microsoft.ML.OnnxRuntimeGenAI` bibliotekas ir įgyvendina `IChatClient` iš `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Pavyzdinis konsolės pokalbis, leidžiantis vartotojui užduoti klausimus. Pokalbis įgyvendina atmintį. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Tai pavyzdinis projektas, kuris naudoja vietinį Phi-4 modelį vaizdų analizei, rodydamas rezultatą konsolėje. Projektas įkelia vietinį Phi-4-`multimodal-instruct-onnx` modelį naudojant `Microsoft.ML.OnnxRuntime` bibliotekas. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Tai pavyzdinis projektas, kuris naudoja vietinį Phi-4 modelį garso failo analizei, generuoja failo transkriptą ir rodo rezultatą konsolėje. Projektas įkelia vietinį Phi-4-`multimodal-instruct-onnx` modelį naudojant `Microsoft.ML.OnnxRuntime` bibliotekas. |

## Kaip paleisti projektus

Norėdami paleisti projektus, atlikite šiuos veiksmus:

1. Nuklonuokite saugyklą į savo kompiuterį.

1. Atidarykite terminalą ir pereikite į norimą projektą. Pavyzdžiui, paleiskime `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Paleiskite projektą naudodami komandą

    ```bash
    dotnet run
    ```

1. Pavyzdinis projektas paprašys vartotojo įvesties ir atsakys naudodamas vietinį modelį.

   Veikiantis demonstracinis projektas atrodo panašiai kaip šis:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.