<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-12-22T01:49:06+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "pcm"
}
-->
# **Quantifying Phi Family**

Model quantization na di process wey dey map di parameters (such as weights and activation values) for neural network model from a large value range (usually a continuous value range) go smaller finite value range. Dis technology fit reduce di size and computational complexity of di model and improve di operating efficiency of di model for resource-constrained environments like mobile devices or embedded systems. Model quantization dey achieve compression by reducing di precision of parameters, but e still go introduce some loss of precision. So, for di quantization process, e important to balance di model size, computational complexity, and precision. Common quantization methods include fixed-point quantization, floating-point quantization, etc. You fit choose di appropriate quantization strategy based on di specific scenario and needs.

We wan deploy GenAI model to edge devices make more devices fit enter GenAI scenarios, like mobile devices, AI PC/Copilot+PC, and traditional IoT devices. Through di quantized model, we fit deploy am to different edge devices based on di device. Combine am with di model acceleration framework and quantization model weh hardware manufacturers provide, we fit build better SLM application scenarios.

For quantization scenario, we get different precisions (INT4, INT8, FP16, FP32). Below na explanation of di commonly used quantization precisions

### **INT4**

INT4 quantization na extreme quantization method wey dey quantize di weights and activation values of di model into 4-bit integers. INT4 quantization normally dey result for bigger loss of precision because di representation range small and precision low. But, compared to INT8 quantization, INT4 fit further reduce di storage requirements and computational complexity of di model. Make you note say INT4 quantization dey relatively rare for practical applications, because too low accuracy fit cause significant degradation for model performance. In addition, not all hardware dey support INT4 operations, so hardware compatibility gats dey considered when you dey choose quantization method.

### **INT8**

INT8 quantization na di process of converting model’s weights and activations from floating point numbers to 8-bit integers. Even though di numerical range wey INT8 integers represent smaller and less precise, e fit greatly reduce storage and calculation requirements. For INT8 quantization, di weights and activation values of di model go through quantization process, including scaling and offset, to preserve di original floating point information as much as possible. During inference, these quantized values go dequantize back to floating point numbers for calculation, and then dem go quantize back to INT8 for di next step. Dis method fit provide sufficient accuracy for most applications while e still maintain high computational efficiency.

### **FP16**

The FP16 format, that be 16-bit floating point numbers (float16), reduce di memory footprint by half compared to 32-bit floating point numbers (float32), wey get significant advantages for large-scale deep learning applications. FP16 format allow make you load larger models or process more data inside di same GPU memory limits. As modern GPU hardware dey continue to support FP16 operations, using FP16 fit also bring improvements in computing speed. However, FP16 get e own disadvantages, namely lower precision, wey fit lead to numerical instability or loss of precision for some cases.

### **FP32**

The FP32 format dey provide higher precision and fit represent wide range of values accurately. For scenarios wey complex mathematical operations dey performed or where high-precision results dey required, FP32 format na wetin dem prefer. But high accuracy still mean more memory usage and longer calculation time. For large-scale deep learning models, especially when model parameters plenti and data plenty, FP32 fit cause insufficient GPU memory or drop for inference speed.

For mobile devices or IoT devices, we fit convert Phi-3.x models to INT4, while AI PC / Copilot PC fit use higher precision like INT8, FP16, FP32.

Now, different hardware manufacturers get different frameworks to support generative models, such as Intel's OpenVINO, Qualcomm's QNN, Apple's MLX, and Nvidia's CUDA, etc., we fit combine dem with model quantization to complete local deployment.

For technology side, we get different format support after quantization, such as PyTorch / Tensorflow format, GGUF, and ONNX. I don do format comparison and application scenarios between GGUF and ONNX. Here I recommend ONNX quantization format, which get good support from di model frameworks down to hardware. For this chapter, we go focus on ONNX Runtime for GenAI, OpenVINO, and Apple MLX to perform model quantization (if you get better way, you fit still give am to us by submitting PR)

**This chapter includes**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate wit AI translation service (Co-op Translator — https://github.com/Azure/co-op-translator). Even though we dey try make am correct, make you sabi say automatic translations fit get errors or mistakes. Di original dokument for im own language na di authoritative source. If na serious or critical information, e better make professional human translator do am. We no dey liable for any misunderstanding or wrong interpretation wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->