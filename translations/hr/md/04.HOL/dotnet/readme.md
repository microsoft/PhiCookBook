<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:42:43+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "hr"
}
-->
## Dobrodošli u Phi laboratorije koristeći C#

Dostupan je izbor laboratorija koji prikazuju kako integrirati moćne različite verzije Phi modela u .NET okruženju.

## Preduvjeti

Prije pokretanja primjera, provjerite imate li instalirano sljedeće:

**.NET 9:** Provjerite imate li [najnoviju verziju .NET-a](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) instaliranu na svom računalu.

**(Opcionalno) Visual Studio ili Visual Studio Code:** Trebat će vam IDE ili uređivač koda sposoban za pokretanje .NET projekata. Preporučuju se [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ili [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Koristeći git** lokalno klonirajte jednu od dostupnih verzija Phi-3, Phi3.5 ili Phi-4 s [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Preuzmite Phi-4 ONNX modele** na svoje lokalno računalo:

### navigirajte do mape za pohranu modela

```bash
cd c:\phi\models
```

### dodajte podršku za lfs

```bash
git lfs install 
```

### klonirajte i preuzmite Phi-4 mini instruct model i Phi-4 multimodalni model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Preuzmite Phi-3 ONNX modele** na svoje lokalno računalo:

### klonirajte i preuzmite Phi-3 mini 4K instruct model i Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Važno:** Trenutni primjeri su dizajnirani za korištenje ONNX verzija modela. Prethodni koraci kloniraju sljedeće modele.

## O laboratorijima

Glavno rješenje sadrži nekoliko primjera laboratorija koji demonstriraju mogućnosti Phi modela koristeći C#.

| Projekt | Model | Opis |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ili Phi-3.5 | Primjer konzolnog chata koji korisniku omogućuje postavljanje pitanja. Projekt učitava lokalni ONNX Phi-3 model koristeći `Microsoft.ML.OnnxRuntime` biblioteke. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 ili Phi-3.5 | Primjer konzolnog chata koji korisniku omogućuje postavljanje pitanja. Projekt učitava lokalni ONNX Phi-3 model koristeći `Microsoft.Semantic.Kernel` biblioteke. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 ili Phi-3.5 | Ovo je primjer projekta koji koristi lokalni phi3 vision model za analizu slika. Projekt učitava lokalni ONNX Phi-3 Vision model koristeći `Microsoft.ML.OnnxRuntime` biblioteke. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 ili Phi-3.5 | Ovo je primjer projekta koji koristi lokalni phi3 vision model za analizu slika. Projekt učitava lokalni ONNX Phi-3 Vision model koristeći `Microsoft.ML.OnnxRuntime` biblioteke. Projekt također prikazuje izbornik s različitim opcijama za interakciju s korisnikom. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Primjer konzolnog chata koji korisniku omogućuje postavljanje pitanja. Projekt učitava lokalni ONNX Phi-4 model koristeći `Microsoft.ML.OnnxRuntime` biblioteke. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Primjer konzolnog chata koji korisniku omogućuje postavljanje pitanja. Projekt učitava lokalni ONNX Phi-4 model koristeći `Semantic Kernel` biblioteke. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Primjer konzolnog chata koji korisniku omogućuje postavljanje pitanja. Projekt učitava lokalni ONNX Phi-4 model koristeći `Microsoft.ML.OnnxRuntimeGenAI` biblioteke i implementira `IChatClient` iz `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Primjer konzolnog chata koji korisniku omogućuje postavljanje pitanja. Chat implementira memoriju. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Ovo je primjer projekta koji koristi lokalni Phi-4 model za analizu slika i prikazuje rezultat u konzoli. Projekt učitava lokalni Phi-4-`multimodal-instruct-onnx` model koristeći `Microsoft.ML.OnnxRuntime` biblioteke. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Ovo je primjer projekta koji koristi lokalni Phi-4 model za analizu audio datoteke, generira transkript datoteke i prikazuje rezultat u konzoli. Projekt učitava lokalni Phi-4-`multimodal-instruct-onnx` model koristeći `Microsoft.ML.OnnxRuntime` biblioteke. |

## Kako pokrenuti projekte

Za pokretanje projekata slijedite ove korake:

1. Klonirajte repozitorij na svoje lokalno računalo.

1. Otvorite terminal i navigirajte do željenog projekta. Na primjer, pokrenimo `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Pokrenite projekt naredbom

    ```bash
    dotnet run
    ```

1. Primjer projekta traži unos korisnika i odgovara koristeći lokalni model.

   Pokrenuti demo izgleda slično ovome:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.