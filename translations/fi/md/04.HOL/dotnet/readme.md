<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:44:32+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "fi"
}
-->
﻿## Tervetuloa Phi-laboratorioihin C#:n kanssa

Tarjolla on valikoima laboratorioita, jotka näyttävät, miten eri Phi-mallien tehokkaita versioita integroidaan .NET-ympäristöön.

## Vaatimukset

Ennen esimerkin suorittamista varmista, että sinulla on seuraavat asennettuna:

**.NET 9:** Varmista, että koneellasi on asennettuna [uusin versio .NET:stä](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Valinnainen) Visual Studio tai Visual Studio Code:** Tarvitset IDE:n tai koodieditorin, joka pystyy ajamaan .NET-projekteja. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) tai [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ovat suositeltuja.

**Gitin käyttö:** kloonaa paikallisesti jokin saatavilla olevista Phi-3, Phi3.5 tai Phi-4 versioista osoitteesta [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Lataa Phi-4 ONNX-mallit** paikalliselle koneellesi:

### siirry kansioon, johon mallit tallennetaan

```bash
cd c:\phi\models
```

### lisää tuki lfs:lle

```bash
git lfs install 
```

### kloonaa ja lataa Phi-4 mini instruct -malli ja Phi-4 multimodaalimalli

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Lataa Phi-3 ONNX-mallit** paikalliselle koneellesi:

### kloonaa ja lataa Phi-3 mini 4K instruct -malli ja Phi-3 vision 128K -malli

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Tärkeää:** Nykyiset demot on suunniteltu käyttämään mallien ONNX-versioita. Edelliset vaiheet kloonaavat seuraavat mallit.

## Laboratorioista

Pääratkaisussa on useita esimerkkilaboratorioita, jotka demonstroivat Phi-mallien kyvykkyyksiä C#:n avulla.

| Projekti | Malli | Kuvaus |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 tai Phi-3.5 | Esimerkkikonsolikeskustelu, joka antaa käyttäjän esittää kysymyksiä. Projekti lataa paikallisen ONNX Phi-3 -mallin käyttäen `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Suorita projekti komennolla

    ```bash
    dotnet run
    ```

1. Esimerkkiprojekti pyytää käyttäjän syötteen ja vastaa paikallisen mallin avulla.

   Suoritettava demo näyttää tältä:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkintojen seurauksista.