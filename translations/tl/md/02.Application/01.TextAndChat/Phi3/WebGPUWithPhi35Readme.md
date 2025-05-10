<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:59:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "tl"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo para ipakita ang WebGPU at RAG Pattern

Ang RAG Pattern gamit ang Phi-3.5 Onnx Hosted model ay gumagamit ng Retrieval-Augmented Generation approach, pinagsasama ang lakas ng Phi-3.5 models at ONNX hosting para sa epektibong AI deployments. Mahalaga ang pattern na ito sa pag-fine-tune ng mga modelo para sa mga domain-specific na gawain, na nag-aalok ng kombinasyon ng kalidad, abot-kayang gastos, at kakayahang umintindi ng mahahabang konteksto. Bahagi ito ng Azure AI suite, na nagbibigay ng malawak na pagpipilian ng mga modelo na madaling hanapin, subukan, at gamitin, na tumutugon sa pangangailangan ng iba't ibang industriya para sa customisasyon.

## Ano ang WebGPU  
Ang WebGPU ay isang modernong web graphics API na idinisenyo para magbigay ng epektibong access sa graphics processing unit (GPU) ng device nang direkta mula sa mga web browser. Ito ay nilikha bilang kapalit ng WebGL, na may mga sumusunod na pangunahing pagpapabuti:

1. **Kompatibilidad sa mga Modernong GPU**: Ang WebGPU ay ginawa upang gumana nang maayos sa mga makabagong GPU architecture, gamit ang system APIs tulad ng Vulkan, Metal, at Direct3D 12.
2. **Pinahusay na Performance**: Sinusuportahan nito ang general-purpose GPU computations at mas mabilis na operasyon, kaya angkop para sa graphics rendering at machine learning tasks.
3. **Mga Advanced na Tampok**: Nagbibigay ang WebGPU ng access sa mas advanced na kakayahan ng GPU, na nagpapahintulot sa mas kumplikado at dynamic na graphics at computational workloads.
4. **Bawas sa Trabaho ng JavaScript**: Sa pamamagitan ng paglipat ng mas maraming gawain sa GPU, malaki ang nababawasan ng WebGPU sa trabaho ng JavaScript, na nagreresulta sa mas magandang performance at mas maayos na karanasan.

Kasulukuyan nang sinusuportahan ang WebGPU sa mga browser tulad ng Google Chrome, at patuloy ang pagsusumikap na palawakin ang suporta sa iba pang mga platform.

### 03.WebGPU  
Kinakailangang Kapaligiran:

**Sinusuportahang mga browser:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Paano I-enable ang WebGPU:

- Sa Chrome/Microsoft Edge  

I-enable ang `chrome://flags/#enable-unsafe-webgpu` flag.

#### Buksan ang Iyong Browser:  
Patakbuhin ang Google Chrome o Microsoft Edge.

#### Puntahan ang Flags Page:  
Sa address bar, i-type ang `chrome://flags` at pindutin ang Enter.

#### Hanapin ang Flag:  
Sa search box sa itaas ng pahina, i-type ang 'enable-unsafe-webgpu'

#### I-enable ang Flag:  
Hanapin ang #enable-unsafe-webgpu flag sa listahan ng mga resulta.

I-click ang dropdown menu sa tabi nito at piliin ang Enabled.

#### I-restart ang Iyong Browser:  

Pagkatapos i-enable ang flag, kailangan mong i-restart ang browser para magkabisa ang mga pagbabago. I-click ang Relaunch button na lalabas sa ibaba ng pahina.

- Para sa Linux, patakbuhin ang browser gamit ang `--enable-features=Vulkan`.  
- Sa Safari 18 (macOS 15), naka-enable na ang WebGPU bilang default.  
- Sa Firefox Nightly, i-type ang about:config sa address bar at `set dom.webgpu.enabled to true`.

### Pag-set up ng GPU para sa Microsoft Edge  

Narito ang mga hakbang para i-set up ang high-performance GPU para sa Microsoft Edge sa Windows:

- **Buksan ang Settings:** I-click ang Start menu at piliin ang Settings.  
- **System Settings:** Pumunta sa System at pagkatapos ay Display.  
- **Graphics Settings:** Mag-scroll pababa at i-click ang Graphics settings.  
- **Pumili ng App:** Sa ilalim ng “Choose an app to set preference,” piliin ang Desktop app at pagkatapos ay Browse.  
- **Piliin ang Edge:** Hanapin ang Edge installation folder (karaniwan ay `C:\Program Files (x86)\Microsoft\Edge\Application`) at piliin ang `msedge.exe`.  
- **Itakda ang Preference:** I-click ang Options, piliin ang High performance, at pagkatapos ay i-click ang Save.  
Sisiguruhin nito na gagamitin ng Microsoft Edge ang iyong high-performance GPU para sa mas magandang performance.  
- **I-restart** ang iyong makina para magkabisa ang mga setting na ito.

### Samples : Pakiclick ang [link na ito](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.