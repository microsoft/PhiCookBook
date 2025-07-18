<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:43:02+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "sl"
}
-->
## Dobrodošli v Phi laboratorijih z uporabo C#

Na voljo je izbor laboratorijev, ki prikazujejo, kako integrirati različne zmogljive različice Phi modelov v .NET okolju.

## Zahteve

Pred zagonom vzorca poskrbite, da imate nameščeno naslednje:

**.NET 9:** Prepričajte se, da imate na svojem računalniku nameščeno [najnovejšo različico .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Neobvezno) Visual Studio ali Visual Studio Code:** Potrebovali boste IDE ali urejevalnik kode, ki podpira zagon .NET projektov. Priporočamo [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ali [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Z uporabo git** lokalno klonirajte eno od razpoložljivih različic Phi-3, Phi3.5 ali Phi-4 iz [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Prenesite Phi-4 ONNX modele** na svoj lokalni računalnik:

### pojdite v mapo, kamor boste shranili modele

```bash
cd c:\phi\models
```

### dodajte podporo za lfs

```bash
git lfs install 
```

### klonirajte in prenesite Phi-4 mini instruct model in Phi-4 multimodalni model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Prenesite Phi-3 ONNX modele** na svoj lokalni računalnik:

### klonirajte in prenesite Phi-3 mini 4K instruct model in Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Pomembno:** Trenutni primeri so zasnovani za uporabo ONNX različic modelov. Prejšnji koraki klonirajo naslednje modele.

## O laboratorijih

Glavna rešitev vsebuje več vzorčnih laboratorijev, ki prikazujejo zmogljivosti Phi modelov z uporabo C#.

| Projekt | Model | Opis |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ali Phi-3.5 | Vzorec konzolnega klepeta, ki uporabniku omogoča postavljanje vprašanj. Projekt naloži lokalni ONNX Phi-3 model z uporabo knjižnic `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 ali Phi-3.5 | Vzorec konzolnega klepeta, ki uporabniku omogoča postavljanje vprašanj. Projekt naloži lokalni ONNX Phi-3 model z uporabo knjižnic `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 ali Phi-3.5 | Vzorec projekta, ki uporablja lokalni phi3 vision model za analizo slik. Projekt naloži lokalni ONNX Phi-3 Vision model z uporabo knjižnic `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 ali Phi-3.5 | Vzorec projekta, ki uporablja lokalni phi3 vision model za analizo slik. Projekt naloži lokalni ONNX Phi-3 Vision model z uporabo knjižnic `Microsoft.ML.OnnxRuntime`. Projekt prav tako prikazuje meni z različnimi možnostmi za interakcijo z uporabnikom. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Vzorec konzolnega klepeta, ki uporabniku omogoča postavljanje vprašanj. Projekt naloži lokalni ONNX Phi-4 model z uporabo knjižnic `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Vzorec konzolnega klepeta, ki uporabniku omogoča postavljanje vprašanj. Projekt naloži lokalni ONNX Phi-4 model z uporabo knjižnic `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Vzorec konzolnega klepeta, ki uporabniku omogoča postavljanje vprašanj. Projekt naloži lokalni ONNX Phi-4 model z uporabo knjižnic `Microsoft.ML.OnnxRuntimeGenAI` in implementira `IChatClient` iz `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Vzorec konzolnega klepeta, ki uporabniku omogoča postavljanje vprašanj. Klepet uporablja pomnilnik. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Vzorec projekta, ki uporablja lokalni Phi-4 model za analizo slik in prikaz rezultatov v konzoli. Projekt naloži lokalni Phi-4-`multimodal-instruct-onnx` model z uporabo knjižnic `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Vzorec projekta, ki uporablja lokalni Phi-4 model za analizo zvočne datoteke, generira prepis datoteke in prikaže rezultat v konzoli. Projekt naloži lokalni Phi-4-`multimodal-instruct-onnx` model z uporabo knjižnic `Microsoft.ML.OnnxRuntime`. |

## Kako zagnati projekte

Za zagon projektov sledite tem korakom:

1. Klonirajte repozitorij na svoj lokalni računalnik.

1. Odprite terminal in se premaknite v želeni projekt. Na primer, zaženimo `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Zaženite projekt z ukazom

    ```bash
    dotnet run
    ```

1. Vzorec projekta zahteva vnos uporabnika in odgovarja z uporabo lokalnega modela.

   Tekajoči demo je podoben temu:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.