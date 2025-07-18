<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:36:04+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "it"
}
-->
## Benvenuti ai Phi labs con C#

È disponibile una selezione di lab che mostrano come integrare le potenti diverse versioni dei modelli Phi in un ambiente .NET.

## Prerequisiti

Prima di eseguire l'esempio, assicurati di avere installato quanto segue:

**.NET 9:** Verifica di avere installato la [versione più recente di .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) sulla tua macchina.

**(Opzionale) Visual Studio o Visual Studio Code:** Ti servirà un IDE o un editor di codice in grado di eseguire progetti .NET. Si consiglia [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) o [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Usando git** clona localmente una delle versioni disponibili Phi-3, Phi3.5 o Phi-4 da [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Scarica i modelli Phi-4 ONNX** sulla tua macchina locale:

### naviga nella cartella dove salvare i modelli

```bash
cd c:\phi\models
```

### aggiungi il supporto per lfs

```bash
git lfs install 
```

### clona e scarica il modello Phi-4 mini instruct e il modello Phi-4 multimodale

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Scarica i modelli Phi-3 ONNX** sulla tua macchina locale:

### clona e scarica il modello Phi-3 mini 4K instruct e il modello Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Importante:** Le demo attuali sono progettate per utilizzare le versioni ONNX del modello. I passaggi precedenti clonano i seguenti modelli.

## Informazioni sui Labs

La soluzione principale contiene diversi sample Labs che dimostrano le capacità dei modelli Phi usando C#.

| Progetto | Modello | Descrizione |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 o Phi-3.5 | Chat console di esempio che permette all’utente di fare domande. Il progetto carica un modello ONNX Phi-3 locale usando le librerie `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 o Phi-3.5 | Chat console di esempio che permette all’utente di fare domande. Il progetto carica un modello ONNX Phi-3 locale usando le librerie `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 o Phi-3.5 | Progetto di esempio che utilizza un modello phi3 vision locale per analizzare immagini. Il progetto carica un modello ONNX Phi-3 Vision locale usando le librerie `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 o Phi-3.5 | Progetto di esempio che utilizza un modello phi3 vision locale per analizzare immagini. Il progetto carica un modello ONNX Phi-3 Vision locale usando le librerie `Microsoft.ML.OnnxRuntime`. Il progetto presenta anche un menu con diverse opzioni per interagire con l’utente. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Chat console di esempio che permette all’utente di fare domande. Il progetto carica un modello ONNX Phi-4 locale usando le librerie `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Chat console di esempio che permette all’utente di fare domande. Il progetto carica un modello ONNX Phi-4 locale usando le librerie `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Chat console di esempio che permette all’utente di fare domande. Il progetto carica un modello ONNX Phi-4 locale usando le librerie `Microsoft.ML.OnnxRuntimeGenAI` e implementa `IChatClient` da `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Chat console di esempio che permette all’utente di fare domande. La chat implementa la memoria. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Progetto di esempio che utilizza un modello Phi-4 locale per analizzare immagini mostrando il risultato in console. Il progetto carica un modello Phi-4-`multimodal-instruct-onnx` locale usando le librerie `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Progetto di esempio che utilizza un modello Phi-4 locale per analizzare un file audio, generare la trascrizione del file e mostrare il risultato in console. Il progetto carica un modello Phi-4-`multimodal-instruct-onnx` locale usando le librerie `Microsoft.ML.OnnxRuntime`. |

## Come eseguire i progetti

Per eseguire i progetti, segui questi passaggi:

1. Clona il repository sulla tua macchina locale.

1. Apri un terminale e naviga nel progetto desiderato. Ad esempio, eseguiamo `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Esegui il progetto con il comando

    ```bash
    dotnet run
    ```

1. Il progetto di esempio chiede un input all’utente e risponde usando il modello locale.

   La demo in esecuzione è simile a questa:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.