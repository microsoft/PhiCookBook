<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:41:48+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ro"
}
-->
﻿## Bine ați venit la laboratoarele Phi folosind C#

Există o selecție de laboratoare care demonstrează cum să integrați diferitele versiuni puternice ale modelelor Phi într-un mediu .NET.

## Cerințe preliminare

Înainte de a rula exemplul, asigurați-vă că aveți instalat următorul software:

**.NET 9:** Asigurați-vă că aveți instalată [ultima versiune de .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) pe calculatorul dumneavoastră.

**(Opțional) Visual Studio sau Visual Studio Code:** Veți avea nevoie de un IDE sau editor de cod capabil să ruleze proiecte .NET. Se recomandă [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) sau [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Folosind git** clonați local una dintre versiunile disponibile Phi-3, Phi3.5 sau Phi-4 de pe [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Descărcați modelele Phi-4 ONNX** pe calculatorul dumneavoastră:

### navigați către folderul unde vor fi stocate modelele

```bash
cd c:\phi\models
```

### adăugați suport pentru lfs

```bash
git lfs install 
```

### clonați și descărcați modelul Phi-4 mini instruct și modelul Phi-4 multimodal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Descărcați modelele Phi-3 ONNX** pe calculatorul dumneavoastră:

### clonați și descărcați modelul Phi-3 mini 4K instruct și modelul Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Important:** Demo-urile curente sunt concepute să folosească versiunile ONNX ale modelului. Pașii anteriori clonează următoarele modele.

## Despre laboratoare

Soluția principală conține mai multe laboratoare exemplu care demonstrează capabilitățile modelelor Phi folosind C#.

| Proiect | Model | Descriere |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 sau Phi-3.5 | Exemplu de chat în consolă care permite utilizatorului să pună întrebări. Proiectul încarcă un model local ONNX Phi-3 folosind bibliotecile `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 sau Phi-3.5 | Exemplu de chat în consolă care permite utilizatorului să pună întrebări. Proiectul încarcă un model local ONNX Phi-3 folosind bibliotecile `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 sau Phi-3.5 | Acesta este un proiect exemplu care folosește un model local phi3 vision pentru a analiza imagini. Proiectul încarcă un model local ONNX Phi-3 Vision folosind bibliotecile `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 sau Phi-3.5 | Acesta este un proiect exemplu care folosește un model local phi3 vision pentru a analiza imagini. Proiectul încarcă un model local ONNX Phi-3 Vision folosind bibliotecile `Microsoft.ML.OnnxRuntime`. Proiectul oferă și un meniu cu diferite opțiuni pentru a interacționa cu utilizatorul. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Exemplu de chat în consolă care permite utilizatorului să pună întrebări. Proiectul încarcă un model local ONNX Phi-4 folosind bibliotecile `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Exemplu de chat în consolă care permite utilizatorului să pună întrebări. Proiectul încarcă un model local ONNX Phi-4 folosind bibliotecile `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Exemplu de chat în consolă care permite utilizatorului să pună întrebări. Proiectul încarcă un model local ONNX Phi-4 folosind bibliotecile `Microsoft.ML.OnnxRuntimeGenAI` și implementează `IChatClient` din `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Exemplu de chat în consolă care permite utilizatorului să pună întrebări. Chat-ul implementează memorie. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Acesta este un proiect exemplu care folosește un model local Phi-4 pentru a analiza imagini și afișează rezultatul în consolă. Proiectul încarcă un model local Phi-4-`multimodal-instruct-onnx` folosind bibliotecile `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Acesta este un proiect exemplu care folosește un model local Phi-4 pentru a analiza un fișier audio, generează transcrierea fișierului și afișează rezultatul în consolă. Proiectul încarcă un model local Phi-4-`multimodal-instruct-onnx` folosind bibliotecile `Microsoft.ML.OnnxRuntime`. |

## Cum să rulați proiectele

Pentru a rula proiectele, urmați acești pași:

1. Clonați depozitul pe calculatorul dumneavoastră.

1. Deschideți un terminal și navigați către proiectul dorit. De exemplu, să rulăm `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Rulați proiectul cu comanda

    ```bash
    dotnet run
    ```

1. Proiectul exemplu solicită o intrare de la utilizator și răspunde folosind modelul local.

   Demo-ul care rulează este similar cu acesta:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.