<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:40:05+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "tl"
}
-->
## Maligayang Pagdating sa Phi labs gamit ang C#

Mayroong iba't ibang labs na nagpapakita kung paano isama ang makapangyarihang iba't ibang bersyon ng Phi models sa isang .NET na kapaligiran.

## Mga Kinakailangan

Bago patakbuhin ang halimbawa, siguraduhing naka-install ang mga sumusunod:

**.NET 9:** Tiyaking mayroon kang [pinakabagong bersyon ng .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) na naka-install sa iyong makina.

**(Opsyonal) Visual Studio o Visual Studio Code:** Kailangan mo ng isang IDE o code editor na kayang magpatakbo ng mga .NET na proyekto. Inirerekomenda ang [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) o [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Gamit ang git** i-clone nang lokal ang isa sa mga available na bersyon ng Phi-3, Phi3.5 o Phi-4 mula sa [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**I-download ang Phi-4 ONNX models** sa iyong lokal na makina:

### pumunta sa folder kung saan itatago ang mga modelo

```bash
cd c:\phi\models
```

### idagdag ang suporta para sa lfs

```bash
git lfs install 
```

### i-clone at i-download ang Phi-4 mini instruct model at ang Phi-4 multi modal model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**I-download ang Phi-3 ONNX models** sa iyong lokal na makina:

### i-clone at i-download ang Phi-3 mini 4K instruct model at Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Mahalaga:** Ang kasalukuyang mga demo ay dinisenyo upang gamitin ang ONNX na mga bersyon ng modelo. Ang mga naunang hakbang ay nag-clone ng mga sumusunod na modelo.

## Tungkol sa mga Labs

Ang pangunahing solusyon ay may ilang sample Labs na nagpapakita ng kakayahan ng mga Phi models gamit ang C#.

| Proyekto | Modelo | Paglalarawan |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 o Phi-3.5 | Sample na console chat na nagpapahintulot sa user na magtanong. Ang proyekto ay naglo-load ng lokal na ONNX Phi-3 model gamit ang `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 o Phi-3.5 | Sample na console chat na nagpapahintulot sa user na magtanong. Ang proyekto ay naglo-load ng lokal na ONNX Phi-3 model gamit ang `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 o Phi-3.5 | Isang sample na proyekto na gumagamit ng lokal na phi3 vision model para suriin ang mga larawan. Ang proyekto ay naglo-load ng lokal na ONNX Phi-3 Vision model gamit ang `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 o Phi-3.5 | Isang sample na proyekto na gumagamit ng lokal na phi3 vision model para suriin ang mga larawan. Ang proyekto ay naglo-load ng lokal na ONNX Phi-3 Vision model gamit ang `Microsoft.ML.OnnxRuntime` libraries. Nagpapakita rin ang proyekto ng menu na may iba't ibang opsyon para makipag-ugnayan sa user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample na console chat na nagpapahintulot sa user na magtanong. Ang proyekto ay naglo-load ng lokal na ONNX Phi-4 model gamit ang `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample na console chat na nagpapahintulot sa user na magtanong. Ang proyekto ay naglo-load ng lokal na ONNX Phi-4 model gamit ang `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample na console chat na nagpapahintulot sa user na magtanong. Ang proyekto ay naglo-load ng lokal na ONNX Phi-4 model gamit ang `Microsoft.ML.OnnxRuntimeGenAI` libraries at nagpapatupad ng `IChatClient` mula sa `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample na console chat na nagpapahintulot sa user na magtanong. Ang chat ay may memorya. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Isang sample na proyekto na gumagamit ng lokal na Phi-4 model para suriin ang mga larawan at ipakita ang resulta sa console. Ang proyekto ay naglo-load ng lokal na Phi-4-`multimodal-instruct-onnx` model gamit ang `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Isang sample na proyekto na gumagamit ng lokal na Phi-4 model para suriin ang isang audio file, gumawa ng transcript ng file, at ipakita ang resulta sa console. Ang proyekto ay naglo-load ng lokal na Phi-4-`multimodal-instruct-onnx` model gamit ang `Microsoft.ML.OnnxRuntime` libraries. |

## Paano Patakbuhin ang mga Proyekto

Para patakbuhin ang mga proyekto, sundin ang mga hakbang na ito:

1. I-clone ang repository sa iyong lokal na makina.

1. Buksan ang terminal at pumunta sa nais na proyekto. Halimbawa, patakbuhin natin ang `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Patakbuhin ang proyekto gamit ang utos

    ```bash
    dotnet run
    ```

1. Hihingin ng sample na proyekto ang input ng user at sasagot gamit ang lokal na modelo.

   Ang tumatakbong demo ay kahalintulad ng ganito:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.