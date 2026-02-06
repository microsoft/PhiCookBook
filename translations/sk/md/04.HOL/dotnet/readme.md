## Vitajte v Phi laboratóriách používajúcich C#

K dispozícii je výber laboratórií, ktoré ukazujú, ako integrovať rôzne výkonné verzie Phi modelov v prostredí .NET.

## Požiadavky

Pred spustením ukážky sa uistite, že máte nainštalované nasledovné:

**.NET 9:** Skontrolujte, či máte na svojom počítači nainštalovanú [najnovšiu verziu .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Voliteľné) Visual Studio alebo Visual Studio Code:** Budete potrebovať IDE alebo editor kódu, ktorý dokáže spúšťať .NET projekty. Odporúčame [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) alebo [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Použitie git:** naklonujte lokálne jednu z dostupných verzií Phi-3, Phi3.5 alebo Phi-4 z [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Stiahnite si Phi-4 ONNX modely** do svojho počítača:

### prejdite do priečinka, kde chcete modely uložiť

```bash
cd c:\phi\models
```

### pridajte podporu pre lfs

```bash
git lfs install 
```

### naklonujte a stiahnite Phi-4 mini instruct model a Phi-4 multimodálny model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Stiahnite si Phi-3 ONNX modely** do svojho počítača:

### naklonujte a stiahnite Phi-3 mini 4K instruct model a Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Dôležité:** Aktuálne ukážky sú navrhnuté na použitie ONNX verzií modelov. Predchádzajúce kroky naklonujú tieto modely.

## O laboratóriách

Hlavné riešenie obsahuje niekoľko ukážkových laboratórií, ktoré demonštrujú schopnosti Phi modelov pomocou C#.

| Projekt | Model | Popis |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 alebo Phi-3.5 | Ukážkový konzolový chat, ktorý umožňuje používateľovi klásť otázky. Projekt načítava lokálny ONNX Phi-3 model pomocou knižníc `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 alebo Phi-3.5 | Ukážkový konzolový chat, ktorý umožňuje používateľovi klásť otázky. Projekt načítava lokálny ONNX Phi-3 model pomocou knižníc `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 alebo Phi-3.5 | Ukážkový projekt, ktorý používa lokálny phi3 vision model na analýzu obrázkov. Projekt načítava lokálny ONNX Phi-3 Vision model pomocou knižníc `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 alebo Phi-3.5 | Ukážkový projekt, ktorý používa lokálny phi3 vision model na analýzu obrázkov. Projekt načítava lokálny ONNX Phi-3 Vision model pomocou knižníc `Microsoft.ML.OnnxRuntime`. Projekt tiež ponúka menu s rôznymi možnosťami interakcie s používateľom. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Ukážkový konzolový chat, ktorý umožňuje používateľovi klásť otázky. Projekt načítava lokálny ONNX Phi-4 model pomocou knižníc `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Ukážkový konzolový chat, ktorý umožňuje používateľovi klásť otázky. Projekt načítava lokálny ONNX Phi-4 model pomocou knižníc `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Ukážkový konzolový chat, ktorý umožňuje používateľovi klásť otázky. Projekt načítava lokálny ONNX Phi-4 model pomocou knižníc `Microsoft.ML.OnnxRuntimeGenAI` a implementuje `IChatClient` z `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Ukážkový konzolový chat, ktorý umožňuje používateľovi klásť otázky. Chat využíva pamäť. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Ukážkový projekt, ktorý používa lokálny Phi-4 model na analýzu obrázkov a zobrazuje výsledok v konzole. Projekt načítava lokálny Phi-4-`multimodal-instruct-onnx` model pomocou knižníc `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Ukážkový projekt, ktorý používa lokálny Phi-4 model na analýzu audio súboru, generuje prepis súboru a zobrazuje výsledok v konzole. Projekt načítava lokálny Phi-4-`multimodal-instruct-onnx` model pomocou knižníc `Microsoft.ML.OnnxRuntime`. |

## Ako spustiť projekty

Na spustenie projektov postupujte podľa týchto krokov:

1. Naklonujte repozitár do svojho počítača.

1. Otvorte terminál a prejdite do požadovaného projektu. Napríklad spustíme `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Spustite projekt príkazom

    ```bash
    dotnet run
    ```

1. Ukážkový projekt vyzve používateľa na zadanie vstupu a odpovie pomocou lokálneho modelu.

   Bežiaca ukážka vyzerá približne takto:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.