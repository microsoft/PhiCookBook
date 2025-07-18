<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:49:09+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "tl"
}
-->
# **Pag-quantify ng Phi Family**

Ang model quantization ay tumutukoy sa proseso ng pagmamapa ng mga parameter (tulad ng mga timbang at activation values) sa isang neural network model mula sa malawak na saklaw ng mga halaga (karaniwang tuloy-tuloy na saklaw) patungo sa mas maliit at tiyak na saklaw ng mga halaga. Ang teknolohiyang ito ay makatutulong upang paliitin ang laki at computational complexity ng modelo at mapabuti ang kahusayan ng pagpapatakbo nito sa mga kapaligirang may limitadong resources tulad ng mga mobile device o embedded systems. Nakakamit ng model quantization ang compression sa pamamagitan ng pagbabawas ng precision ng mga parameter, ngunit nagdudulot din ito ng kaunting pagkawala ng katumpakan. Kaya naman, sa proseso ng quantization, kailangang balansehin ang laki ng modelo, computational complexity, at precision. Kadalasang ginagamit na mga paraan ng quantization ay fixed-point quantization, floating-point quantization, at iba pa. Maaari kang pumili ng angkop na quantization strategy batay sa partikular na sitwasyon at pangangailangan.

Nais naming i-deploy ang GenAI model sa mga edge device at payagan ang mas maraming device na makapasok sa mga GenAI na senaryo, tulad ng mga mobile device, AI PC/Copilot+PC, at mga tradisyunal na IoT device. Sa pamamagitan ng quantization model, maaari natin itong i-deploy sa iba't ibang edge device depende sa uri ng device. Kapag pinagsama sa model acceleration framework at quantization model na ibinibigay ng mga hardware manufacturer, makakabuo tayo ng mas mahusay na mga SLM application scenario.

Sa quantization na senaryo, mayroon tayong iba't ibang precision (INT4, INT8, FP16, FP32). Narito ang paliwanag tungkol sa mga karaniwang ginagamit na quantization precision:

### **INT4**

Ang INT4 quantization ay isang matinding paraan ng quantization na nagko-convert ng mga timbang at activation values ng modelo sa 4-bit na mga integer. Karaniwang nagreresulta ito sa mas malaking pagkawala ng precision dahil sa mas maliit na saklaw ng representasyon at mas mababang katumpakan. Gayunpaman, kumpara sa INT8 quantization, ang INT4 ay mas nakakapagpaliit ng pangangailangan sa storage at computational complexity ng modelo. Dapat tandaan na ang INT4 quantization ay bihirang gamitin sa praktikal na aplikasyon dahil ang sobrang baba ng accuracy ay maaaring magdulot ng malaking pagbaba sa performance ng modelo. Bukod dito, hindi lahat ng hardware ay sumusuporta sa INT4 operations, kaya kailangang isaalang-alang ang compatibility ng hardware kapag pumipili ng quantization method.

### **INT8**

Ang INT8 quantization ay proseso ng pag-convert ng mga timbang at activation ng modelo mula sa floating point numbers patungo sa 8-bit na mga integer. Bagamat mas maliit ang numerical range at mas mababa ang precision ng INT8 integers, malaki ang naitutulong nito sa pagbabawas ng storage at computational requirements. Sa INT8 quantization, dumadaan ang mga timbang at activation values sa proseso ng quantization, kabilang ang scaling at offset, upang mapanatili ang orihinal na floating point na impormasyon hangga't maaari. Sa panahon ng inference, ang mga na-quantize na values ay dine-dequantize pabalik sa floating point numbers para sa kalkulasyon, at saka muling kino-convert sa INT8 para sa susunod na hakbang. Ang pamamaraang ito ay nagbibigay ng sapat na accuracy sa karamihan ng aplikasyon habang pinapanatili ang mataas na computational efficiency.

### **FP16**

Ang FP16 format, o 16-bit floating point numbers (float16), ay nagpapabawas ng memory footprint nang kalahati kumpara sa 32-bit floating point numbers (float32), na may malaking benepisyo sa malakihang deep learning applications. Pinapayagan ng FP16 format ang pag-load ng mas malalaking modelo o pagproseso ng mas maraming data sa loob ng parehong limitasyon ng GPU memory. Habang patuloy na sinusuportahan ng mga modernong GPU hardware ang FP16 operations, maaaring magdulot din ito ng pagbilis sa computing speed. Gayunpaman, may mga inherent na kahinaan ang FP16 format, tulad ng mas mababang precision, na maaaring magdulot ng numerical instability o pagkawala ng katumpakan sa ilang pagkakataon.

### **FP32**

Ang FP32 format ay nagbibigay ng mas mataas na precision at kayang tumpak na irepresenta ang malawak na hanay ng mga halaga. Sa mga senaryong nangangailangan ng komplikadong mathematical operations o mataas na precision na resulta, mas mainam gamitin ang FP32 format. Ngunit ang mataas na accuracy ay nangangahulugan din ng mas malaking paggamit ng memorya at mas matagal na oras ng kalkulasyon. Para sa malalaking deep learning models, lalo na kung maraming parameter at napakaraming data, maaaring magdulot ang FP32 ng kakulangan sa GPU memory o pagbaba ng inference speed.

Sa mga mobile device o IoT device, maaari nating i-convert ang Phi-3.x models sa INT4, habang ang AI PC / Copilot PC ay maaaring gumamit ng mas mataas na precision tulad ng INT8, FP16, FP32.

Sa kasalukuyan, may iba't ibang framework ang mga hardware manufacturer para suportahan ang generative models, tulad ng Intel OpenVINO, Qualcomm QNN, Apple MLX, at Nvidia CUDA, na pinagsasama sa model quantization para sa lokal na deployment.

Sa aspeto ng teknolohiya, may iba't ibang format support pagkatapos ng quantization, tulad ng PyTorch / Tensorflow format, GGUF, at ONNX. Nagsagawa ako ng paghahambing ng format at mga application scenario sa pagitan ng GGUF at ONNX. Dito, inirerekomenda ko ang ONNX quantization format dahil sa magandang suporta mula sa model framework hanggang sa hardware. Sa kabanatang ito, tututok tayo sa ONNX Runtime para sa GenAI, OpenVINO, at Apple MLX para isagawa ang model quantization (kung may mas magandang paraan, maaari rin kayong magbigay sa pamamagitan ng pagsusumite ng PR).

**Kasama sa kabanatang ito**

1. [Pag-quantize ng Phi-3.5 / 4 gamit ang llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Pag-quantize ng Phi-3.5 / 4 gamit ang Generative AI extensions para sa onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Pag-quantize ng Phi-3.5 / 4 gamit ang Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Pag-quantize ng Phi-3.5 / 4 gamit ang Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.