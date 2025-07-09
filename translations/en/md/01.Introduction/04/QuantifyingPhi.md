<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-09T19:46:06+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "en"
}
-->
# **Quantifying Phi Family**

Model quantization refers to the process of mapping the parameters (such as weights and activation values) in a neural network model from a large value range (usually a continuous value range) to a smaller finite value range. This technology can reduce the size and computational complexity of the model and improve the operating efficiency of the model in resource-constrained environments such as mobile devices or embedded systems. Model quantization achieves compression by reducing the precision of parameters, but it also introduces some loss of accuracy. Therefore, during quantization, it is necessary to balance model size, computational complexity, and precision. Common quantization methods include fixed-point quantization, floating-point quantization, and others. You can choose the appropriate quantization strategy based on the specific scenario and requirements.

We aim to deploy GenAI models to edge devices and enable more devices to participate in GenAI scenarios, such as mobile devices, AI PCs/Copilot+PCs, and traditional IoT devices. Through quantized models, we can deploy them to various edge devices depending on the hardware. Combined with model acceleration frameworks and quantization models provided by hardware manufacturers, we can build better SLM application scenarios.

In quantization scenarios, we have different precisions (INT4, INT8, FP16, FP32). Below is an explanation of commonly used quantization precisions.

### **INT4**

INT4 quantization is an aggressive quantization method that converts the model’s weights and activation values into 4-bit integers. INT4 quantization usually results in greater precision loss due to the smaller representation range and lower accuracy. However, compared to INT8 quantization, INT4 can further reduce storage requirements and computational complexity. It should be noted that INT4 quantization is relatively rare in practical applications because the accuracy loss may significantly degrade model performance. Additionally, not all hardware supports INT4 operations, so hardware compatibility must be considered when selecting a quantization method.

### **INT8**

INT8 quantization converts a model’s weights and activations from floating-point numbers to 8-bit integers. Although the numerical range represented by INT8 integers is smaller and less precise, it significantly reduces storage and computation demands. In INT8 quantization, the model’s weights and activations undergo a quantization process, including scaling and offset, to preserve the original floating-point information as much as possible. During inference, these quantized values are dequantized back to floating-point numbers for computation, then quantized again to INT8 for the next step. This approach provides sufficient accuracy for most applications while maintaining high computational efficiency.

### **FP16**

The FP16 format, or 16-bit floating-point numbers (float16), halves the memory footprint compared to 32-bit floating-point numbers (float32), offering significant advantages in large-scale deep learning applications. FP16 allows loading larger models or processing more data within the same GPU memory limits. As modern GPU hardware increasingly supports FP16 operations, using FP16 can also improve computing speed. However, FP16 has inherent drawbacks, such as lower precision, which may cause numerical instability or precision loss in some cases.

### **FP32**

The FP32 format offers higher precision and can accurately represent a wide range of values. It is preferred in scenarios involving complex mathematical operations or when high-precision results are required. However, higher accuracy comes with increased memory usage and longer computation times. For large-scale deep learning models, especially those with many parameters and large datasets, FP32 may lead to insufficient GPU memory or slower inference speeds.

On mobile or IoT devices, we can convert Phi-3.x models to INT4, while AI PCs / Copilot PCs can use higher precisions such as INT8, FP16, or FP32.

Currently, different hardware manufacturers provide various frameworks to support generative models, such as Intel's OpenVINO, Qualcomm's QNN, Apple's MLX, and Nvidia's CUDA, combined with model quantization to enable local deployment.

From a technical perspective, we support different formats after quantization, such as PyTorch / Tensorflow formats, GGUF, and ONNX. I have compared the formats and their application scenarios between GGUF and ONNX. Here, I recommend the ONNX quantization format, which enjoys strong support from both model frameworks and hardware. In this chapter, we will focus on ONNX Runtime for GenAI, OpenVINO, and Apple MLX to perform model quantization (if you have better methods, feel free to submit a PR).

**This chapter includes**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.