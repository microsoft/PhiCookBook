## Tere tulemast Phi laboritesse, kasutades C#

Siin on valik laboreid, mis näitavad, kuidas integreerida võimsaid Phi mudelite erinevaid versioone .NET keskkonnas.

## Eeltingimused

Enne näidise käivitamist veendu, et sul on paigaldatud järgmised:

**.NET 9:** Veendu, et sul on [viimane .NET versioon](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) paigaldatud.

**(Valikuline) Visual Studio või Visual Studio Code:** Sul on vaja IDE-d või koodiredaktorit, mis suudab käivitada .NET projekte. Soovitatav on kasutada [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) või [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Git kasutamine:** klooni lokaalselt üks saadaval olevatest Phi-3, Phi3.5 või Phi-4 versioonidest [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) kaudu.

**Laadi alla Phi-4 ONNX mudelid** oma arvutisse:

### liigu kausta, kuhu mudelid salvestada

```bash
cd c:\phi\models
```

### lisa lfs tugi

```bash
git lfs install 
```

### klooni ja laadi alla Phi-4 mini instruct mudel ja Phi-4 multimodaalne mudel

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Laadi alla Phi-3 ONNX mudelid** oma arvutisse:

### klooni ja laadi alla Phi-3 mini 4K instruct mudel ja Phi-3 vision 128K mudel

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Oluline:** Praegused demod on loodud kasutama mudeli ONNX versioone. Eelnevad sammud kloonivad järgmised mudelid.

## Laborite kohta

Peamine lahendus sisaldab mitmeid näidislaboreid, mis demonstreerivad Phi mudelite võimekust C# abil.

| Projekt | Mudel | Kirjeldus |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 või Phi-3.5 | Näidiskonsooli vestlus, mis võimaldab kasutajal küsimusi esitada. Projekt laadib lokaalse ONNX Phi-3 mudeli, kasutades `Microsoft.ML.OnnxRuntime` teeke. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 või Phi-3.5 | Näidiskonsooli vestlus, mis võimaldab kasutajal küsimusi esitada. Projekt laadib lokaalse ONNX Phi-3 mudeli, kasutades `Microsoft.Semantic.Kernel` teeke. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 või Phi-3.5 | Näidisprojekt, mis kasutab kohalikku Phi-3 vision mudelit piltide analüüsimiseks. Projekt laadib lokaalse ONNX Phi-3 Vision mudeli, kasutades `Microsoft.ML.OnnxRuntime` teeke. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 või Phi-3.5 | Näidisprojekt, mis kasutab kohalikku Phi-3 vision mudelit piltide analüüsimiseks. Projekt laadib lokaalse ONNX Phi-3 Vision mudeli, kasutades `Microsoft.ML.OnnxRuntime` teeke. Projekt esitab ka menüü erinevate valikutega kasutajaga suhtlemiseks. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Näidiskonsooli vestlus, mis võimaldab kasutajal küsimusi esitada. Projekt laadib lokaalse ONNX Phi-4 mudeli, kasutades `Microsoft.ML.OnnxRuntime` teeke. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Näidiskonsooli vestlus, mis võimaldab kasutajal küsimusi esitada. Projekt laadib lokaalse ONNX Phi-4 mudeli, kasutades `Semantic Kernel` teeke. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Näidiskonsooli vestlus, mis võimaldab kasutajal küsimusi esitada. Projekt laadib lokaalse ONNX Phi-4 mudeli, kasutades `Microsoft.ML.OnnxRuntimeGenAI` teeke ja rakendab `IChatClient` `Microsoft.Extensions.AI` kaudu. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Näidiskonsooli vestlus, mis võimaldab kasutajal küsimusi esitada. Vestlus rakendab mälu. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Näidisprojekt, mis kasutab kohalikku Phi-4 mudelit piltide analüüsimiseks ja kuvab tulemuse konsoolis. Projekt laadib lokaalse Phi-4-`multimodal-instruct-onnx` mudeli, kasutades `Microsoft.ML.OnnxRuntime` teeke. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Näidisprojekt, mis kasutab kohalikku Phi-4 mudelit helifaili analüüsimiseks, genereerib faili transkriptsiooni ja kuvab tulemuse konsoolis. Projekt laadib lokaalse Phi-4-`multimodal-instruct-onnx` mudeli, kasutades `Microsoft.ML.OnnxRuntime` teeke. |

## Kuidas projekte käivitada

Projektide käivitamiseks järgi järgmisi samme:

1. Klooni repositoorium oma arvutisse.

1. Ava terminal ja liigu soovitud projekti kausta. Näiteks käivitame `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Käivita projekt käsuga

    ```bash
    dotnet run
    ```

1. Näidisprojekt küsib kasutaja sisendit ja vastab, kasutades kohalikku mudelit.

   Käivitatud demo näeb välja umbes selline:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.