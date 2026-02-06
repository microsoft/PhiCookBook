# **Pagsusukat ng Pamilya ng Phi**

Ang model quantization ay tumutukoy sa proseso ng pagmamapa ng mga parameter (tulad ng mga timbang at halaga ng aktibasyon) sa isang neural network model mula sa malaking hanay ng mga halaga (karaniwang isang tuloy-tuloy na hanay ng mga halaga) patungo sa mas maliit na hangganang hanay ng mga halaga. Ang teknolohiyang ito ay maaaring magpaliit ng laki at komplikasyon sa pagkalkula ng modelo at mapabuti ang kahusayan ng pagpapatakbo ng modelo sa mga kapaligirang may limitadong yaman tulad ng mga mobile device o naka-embed na mga sistema. Nakakamit ng model quantization ang compression sa pamamagitan ng pagbabawas ng precision ng mga parameter, ngunit nagdudulot din ito ng ilang pagkawala ng precision. Kaya, sa proseso ng quantization, kinakailangang balansehin ang laki ng modelo, komplikasyon sa pagkalkula, at precision. Ang mga karaniwang pamamaraan ng quantization ay kinabibilangan ng fixed-point quantization, floating-point quantization, at iba pa. Maaari kang pumili ng angkop na estratehiya ng quantization ayon sa partikular na sitwasyon at pangangailangan.

Nais naming i-deploy ang GenAI model sa mga edge device at payagan ang mas maraming device na makapasok sa mga senaryo ng GenAI, tulad ng mga mobile device, AI PC/Copilot+PC, at tradisyonal na mga IoT device. Sa pamamagitan ng quantization model, maaari naming ideploy ito sa iba't ibang mga edge device base sa iba't ibang device. Pinaghalo sa framework ng pagbilis ng modelo at quantization model na ibinibigay ng mga hardware manufacturer, makakabuo kami ng mas mahusay na SLM na mga senaryo ng aplikasyon.

Sa senaryo ng quantization, mayroon kaming iba't ibang precision (INT4, INT8, FP16, FP32). Narito ang paliwanag ng mga karaniwang ginagamit na quantization precisions

### **INT4**

Ang INT4 quantization ay isang radikal na pamamaraan ng quantization na nag-quantize ng mga timbang at halaga ng aktibasyon ng modelo sa 4-bit na mga integer. Karaniwang nagreresulta ang INT4 quantization sa mas malaking pagkawala ng precision dahil sa mas maliit na saklaw ng representasyon at mas mababang precision. Gayunpaman, kumpara sa INT8 quantization, ang INT4 quantization ay maaaring higit pang magpaliit ng mga kinakailangang storage at komplikasyon sa pagkalkula ng modelo. Dapat tandaan na ang INT4 quantization ay medyo bihira sa praktikal na aplikasyon, dahil ang sobrang babang accuracy ay maaaring magdulot ng malaking pagbaba ng pagganap ng modelo. Bukod dito, hindi lahat ng hardware ay sumusuporta sa mga operasyon ng INT4, kaya't kailangang isaalang-alang ang compatibility ng hardware kapag pumipili ng pamamaraan ng quantization.

### **INT8**

Ang INT8 quantization ay ang proseso ng pag-convert ng mga timbang at aktibasyon ng modelo mula sa floating point numbers patungo sa 8-bit na mga integer. Bagaman ang saklaw ng mga numerong kinakatawan ng mga integer ng INT8 ay mas maliit at hindi gaanong tumpak, maaari nitong malaki ang mabawasan ang pangangailangan sa storage at pagkalkula. Sa INT8 quantization, ang mga timbang at aktibasyon ng modelo ay dumadaan sa proseso ng quantization, kabilang ang scaling at offset, upang mapanatili ang orihinal na impormasyon ng floating point hangga't maaari. Sa panahon ng inference, ang mga na-quantize na halagang ito ay dine-dequantize pabalik sa floating point numbers para sa pagkalkula, at pagkatapos ay quantize muli pabalik sa INT8 para sa susunod na hakbang. Ang pamamaraang ito ay maaaring magbigay ng sapat na precision sa karamihan ng mga aplikasyon habang pinananatili ang mataas na kahusayan sa pagkalkula.

### **FP16**

Ang FP16 na format, ibig sabihin ay 16-bit na floating point numbers (float16), ay nagpapabawas ng memory footprint nang kalahati kumpara sa 32-bit na floating point numbers (float32), na may makabuluhang mga pakinabang sa mga malakihang aplikasyon ng deep learning. Pinapayagan ng FP16 format na mag-load ng mas malalaking modelo o magproseso ng mas maraming data sa loob ng parehong limitasyon ng memorya ng GPU. Habang patuloy na sinusuportahan ng mga modernong GPU hardware ang mga operasyon ng FP16, maaaring magdulot din ang paggamit ng FP16 ng mga pagpapabuti sa bilis ng pagkalkula. Gayunpaman, mayroon ding inherent na mga kahinaan ang FP16 format, partikular ang mas mababang precision, na maaaring magdulot ng numerikal na hindi katatagan o pagkawala ng precision sa ilang mga kaso.

### **FP32**

Ang FP32 na format ay nagbibigay ng mas mataas na precision at maaaring tumpak na kumatawan sa malawak na hanay ng mga halaga. Sa mga senaryong nagsasagawa ng komplikadong mga matematikal na operasyon o kinakailangan ang mataas na precision na mga resulta, mas pinipili ang FP32 na format. Gayunpaman, ang mataas na katumpakan ay nangangahulugan din ng mas malaking paggamit ng memorya at mas mahabang oras ng pagkalkula. Para sa mga malalaking modelo ng deep learning, lalo na kapag maraming mga parameter ng modelo at napakalaking dami ng data, maaaring magdulot ang FP32 ng kakulangan sa memorya ng GPU o pagbaba ng bilis ng inference.

Sa mga mobile device o IoT device, maaari nating i-convert ang mga Phi-3.x na modelo sa INT4, habang ang AI PC / Copilot PC ay maaaring gumamit ng mas mataas na precision tulad ng INT8, FP16, FP32.

Sa kasalukuyan, may iba't ibang mga framework na sinusuportahan ng iba't ibang hardware manufacturer para sa mga generative model, tulad ng OpenVINO ng Intel, QNN ng Qualcomm, MLX ng Apple, at CUDA ng Nvidia, at iba pa, na pinaghalo sa quantization ng modelo upang makumpleto ang lokal na deployment.

Sa aspeto ng teknolohiya, mayroon tayong iba't ibang suporta sa format pagkatapos ng quantization, tulad ng PyTorch / TensorFlow format, GGUF, at ONNX. Nakagawa na ako ng paghahambing ng format at mga senaryo ng aplikasyon sa pagitan ng GGUF at ONNX. Dito inirerekomenda ko ang ONNX quantization format, na may mabuting suporta mula sa framework ng modelo hanggang sa hardware. Sa kabanatang ito, tututok tayo sa ONNX Runtime para sa GenAI, OpenVINO, at Apple MLX upang magsagawa ng quantization ng modelo (kung may mas maganda kang paraan, maaari mo rin itong ibigay sa amin sa pamamagitan ng pagsumite ng PR)

**Kasama sa kabanatang ito**

1. [Pagsusukat ng Phi-3.5 / 4 gamit ang llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Pagsusukat ng Phi-3.5 / 4 gamit ang Generative AI extensions para sa onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Pagsusukat ng Phi-3.5 / 4 gamit ang Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Pagsusukat ng Phi-3.5 / 4 gamit ang Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring mangyari mula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->