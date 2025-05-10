<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:33:54+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "tl"
}
-->
# **Pagkwenta sa Phi Family**

Ang model quantization nagtumong sa proseso sa pag-mapa sa mga parameter (sama sa weights ug activation values) sa usa ka neural network model gikan sa dako nga range sa mga value (kasagaran usa ka continuous nga range) ngadto sa mas gamay ug limitado nga range sa mga value. Kini nga teknolohiya makatabang sa pagpakunhod sa gidak-on ug computational complexity sa model ug mapauswag ang efficiency sa operasyon sa model ilabi na sa mga lugar nga kulang sa resources sama sa mobile devices o embedded systems. Ang model quantization makab-ot ang compression pinaagi sa pagpakunhod sa precision sa mga parameter, apan kini usab nagdala og pipila ka pagkawala sa precision. Busa, sa proseso sa quantization, kinahanglan nga balansehon ang gidak-on sa model, computational complexity, ug precision. Kasagaran nga mga pamaagi sa quantization naglakip sa fixed-point quantization, floating-point quantization, ug uban pa. Mahimo nimo pilion ang angay nga quantization strategy base sa espesipikong sitwasyon ug panginahanglan.

Gusto namo nga ma-deploy ang GenAI model sa edge devices ug tugotan nga daghang mga device ang mosulod sa GenAI scenarios, sama sa mobile devices, AI PC/Copilot+PC, ug tradisyonal nga IoT devices. Pinaagi sa quantization model, mahimo namo kini i-deploy sa lain-laing edge devices base sa klase sa device. Pinaagi sa kombinasyon sa model acceleration framework ug quantization model nga gihatag sa mga hardware manufacturers, mahimo kami magtukod og mas maayo nga mga SLM application scenarios.

Sa quantization nga sitwasyon, adunay lain-laing precision (INT4, INT8, FP16, FP32). Ania ang pagpasabot sa kasagarang gigamit nga quantization precision

### **INT4**

Ang INT4 quantization usa ka radikal nga pamaagi sa quantization nga nag-quantize sa weights ug activation values sa model ngadto sa 4-bit nga integers. Kasagaran, ang INT4 quantization nagresulta og mas dako nga pagkawala sa precision tungod sa gamay nga representation range ug ubos nga precision. Apan, kung itandi sa INT8 quantization, ang INT4 quantization makapakunhod pa gyud sa storage requirements ug computational complexity sa model. Angay hinumduman nga ang INT4 quantization medyo talagsaon gamiton sa praktis tungod kay ang sobra ka ubos nga accuracy mahimong makapahinay sa performance sa model. Dugang pa, dili tanan hardware nagsuporta sa INT4 operations, busa kinahanglan nga tagdon ang compatibility sa hardware sa pagpili sa quantization method.

### **INT8**

Ang INT8 quantization mao ang proseso sa pag-convert sa weights ug activations sa model gikan sa floating point numbers ngadto sa 8-bit integers. Bisan pa man nga ang numerical range nga gipakita sa INT8 integers mas gamay ug dili kaayo precise, kini makatabang sa dako nga pagpakunhod sa storage ug computational requirements. Sa INT8 quantization, ang weights ug activation values sa model moagi sa proseso sa quantization, lakip ang scaling ug offset, aron mapreserbar ang orihinal nga floating point nga impormasyon kutob sa mahimo. Sa inference, kini nga mga quantized values i-dequantize balik ngadto sa floating point numbers alang sa kalkulasyon, ug dayon i-quantize usab balik ngadto sa INT8 alang sa sunod nga lakang. Kini nga pamaagi makahatag og igo nga accuracy sa kadaghanan sa mga aplikasyon samtang nagpadayon sa taas nga computational efficiency.

### **FP16**

Ang FP16 format, nga mao ang 16-bit floating point numbers (float16), nagpakunhod sa memory footprint sa tunga kung ikompara sa 32-bit floating point numbers (float32), nga dako kaayong bentaha sa dagkong deep learning applications. Ang FP16 format nagtugot sa pag-load og mas dagkong mga model o pagproseso og mas daghang data sulod sa parehas nga GPU memory limitasyon. Samtang ang modernong GPU hardware nagpadayon sa pagsuporta sa FP16 operations, ang paggamit sa FP16 format mahimong makahatag usab og pagpasayon sa computing speed. Apan, ang FP16 format adunay mga inherent nga kakulian, sama sa mas ubos nga precision nga usahay makadala sa numerical instability o pagkawala sa precision sa pipila ka mga kaso.

### **FP32**

Ang FP32 format naghatag og mas taas nga precision ug makapakita sa halapad nga range sa mga value nga tukma. Sa mga sitwasyon diin komplikado ang mga mathematical operations o kinahanglan ang taas nga precision sa resulta, mas angay gamiton ang FP32 format. Apan, ang taas nga accuracy nagpasabot usab og mas dako nga paggamit sa memorya ug mas dugay nga oras sa kalkulasyon. Para sa dagkong deep learning models, labi na kung daghan ang model parameters ug daghan ang data, ang FP32 format mahimong hinungdan sa kakulang sa GPU memory o paghinay sa inference speed.

Sa mobile devices o IoT devices, mahimo nato i-convert ang Phi-3.x models ngadto sa INT4, samtang ang AI PC / Copilot PC mahimo gamitan og mas taas nga precision sama sa INT8, FP16, FP32.

Sa pagkakaron, lain-laing hardware manufacturers adunay lain-laing frameworks nga nagsuporta sa generative models, sama sa Intel's OpenVINO, Qualcomm's QNN, Apple's MLX, ug Nvidia's CUDA, ug uban pa, nga gisagol sa model quantization aron makompleto ang local deployment.

Sa teknikal nga bahin, adunay lain-laing format nga gisugyot human sa quantization, sama sa PyTorch / Tensorflow format, GGUF, ug ONNX. Nakahimo ko og comparison sa format ug mga application scenarios tali sa GGUF ug ONNX. Dinhi, akong girekomenda ang ONNX quantization format, nga maayo ang suporta gikan sa model framework hangtod sa hardware. Niining kapituloha, magpunting kita sa ONNX Runtime para sa GenAI, OpenVINO, ug Apple MLX sa pagperform sa model quantization (kung naa kay mas maayo nga paagi, mahimo usab nimo kini i-share pinaagi sa pag-submit og PR)

**Kini nga kapitulo naglakip sa**

1. [Quantizing Phi-3.5 / 4 gamit ang llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 gamit ang Generative AI extensions para sa onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 gamit ang Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 gamit ang Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mga mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.