<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-07T14:49:45+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "mo"
}
-->
# **Quantifying Phi Family**

Model quantization means mapping the parameters (like weights and activation values) in a neural network model from a large range (usually continuous) to a smaller, finite range. This technique reduces the model’s size and computational load, improving efficiency in resource-limited environments such as mobile or embedded devices. Quantization compresses the model by lowering parameter precision but introduces some accuracy loss. Therefore, it’s important to balance model size, computational cost, and precision during quantization. Common methods include fixed-point and floating-point quantization. Choose the right strategy based on your specific scenario and needs.

We aim to deploy GenAI models on edge devices, enabling more devices like mobiles, AI PC/Copilot+PC, and traditional IoT devices to enter GenAI scenarios. With quantized models, deployment can be tailored to different edge devices. Together with model acceleration frameworks and hardware vendor quantization models, we can create better SLM application scenarios.

In quantization, different precisions exist (INT4, INT8, FP16, FP32). Below is an overview of commonly used precisions:

### **INT4**

INT4 quantization is an aggressive method that converts model weights and activations into 4-bit integers. Due to the smaller range and lower precision, INT4 usually causes greater accuracy loss. However, compared to INT8, it further reduces storage and computational demands. INT4 is relatively rare in practice because too low precision can significantly degrade model performance. Also, not all hardware supports INT4 operations, so hardware compatibility must be considered when choosing this method.

### **INT8**

INT8 quantization converts model weights and activations from floating point to 8-bit integers. Although INT8’s range and precision are lower, it significantly reduces storage and computation needs. The model’s weights and activations undergo quantization with scaling and offset to preserve floating point information as much as possible. During inference, these values are dequantized back to floating point for calculations, then re-quantized to INT8 for the next step. This approach provides adequate accuracy in most cases while maintaining high computational efficiency.

### **FP16**

FP16, or 16-bit floating point (float16), halves memory usage compared to 32-bit float (float32), which is advantageous in large-scale deep learning. FP16 allows loading bigger models or handling more data within the same GPU memory limits. As modern GPUs increasingly support FP16 operations, it can also speed up computation. However, FP16 has lower precision, which can sometimes cause numerical instability or precision loss.

### **FP32**

FP32 offers higher precision and accurately represents a wide range of values. It’s preferred for complex mathematical operations or when high-precision results are needed. However, higher accuracy means more memory usage and longer computation times. For large deep learning models with many parameters and huge data, FP32 may lead to insufficient GPU memory or slower inference.

On mobile or IoT devices, Phi-3.x models can be converted to INT4, while AI PC / Copilot PC can use higher precisions like INT8, FP16, or FP32.

Currently, different hardware vendors offer frameworks supporting generative models, such as Intel's OpenVINO, Qualcomm's QNN, Apple's MLX, and Nvidia's CUDA, combined with model quantization for local deployment.

Technically, we support various formats after quantization, like PyTorch / Tensorflow formats, GGUF, and ONNX. I have compared GGUF and ONNX formats and their application scenarios. I recommend the ONNX quantization format due to its strong support from both model frameworks and hardware. In this chapter, we focus on ONNX Runtime for GenAI, OpenVINO, and Apple MLX for model quantization (if you have better methods, feel free to contribute via PR).

**This chapter includes**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.

---

Could you please clarify what language or dialect "mo" refers to? This will help me provide the correct translation.