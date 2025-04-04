<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "418c693c63cc0e817dc560558f730a7a",
  "translation_date": "2025-04-04T12:11:35+00:00",
  "source_file": "md\\01.Introduction\\04\\QuantifyingPhi.md",
  "language_code": "mo"
}
-->
# **Phi Family Quantization**

Quantization of models involves converting the parameters (like weights and activation values) of a neural network from a broad range of values (often continuous) to a smaller, finite range. This technique helps reduce model size and computational complexity, improving the efficiency of the model in environments with limited resources, such as mobile devices or embedded systems. While quantization compresses models by lowering parameter precision, it also introduces some accuracy loss. Therefore, it’s essential to strike a balance between model size, computational complexity, and accuracy during quantization. Common methods include fixed-point quantization and floating-point quantization. You can select the most suitable strategy based on specific scenarios and requirements.

We aim to deploy GenAI models to edge devices, enabling broader access to GenAI applications, such as on mobile devices, AI PCs/Copilot PCs, and traditional IoT devices. By leveraging quantized models, we can adapt deployments to various edge devices. Coupled with acceleration frameworks and quantization models provided by hardware vendors, we can build more optimized SLM application scenarios.

In quantization, we work with different levels of precision (INT4, INT8, FP16, FP32). Below is an overview of commonly used quantization precisions.

### **INT4**

INT4 quantization is an aggressive approach that converts model weights and activations into 4-bit integers. Due to the narrower representation range and reduced precision, INT4 quantization often results in greater accuracy loss. However, compared to INT8, INT4 can further lower storage demands and computational complexity. It's worth noting that INT4 quantization is less commonly used in practice because the reduced accuracy can significantly impact model performance. Additionally, not all hardware supports INT4 operations, so hardware compatibility must be considered when selecting this method.

### **INT8**

INT8 quantization involves transforming model weights and activations from floating-point numbers to 8-bit integers. While INT8 offers a smaller numerical range and lower precision, it drastically reduces storage and computation requirements. During INT8 quantization, the model’s weights and activations undergo processes like scaling and offsetting to retain as much of the original floating-point data as possible. During inference, quantized values are temporarily dequantized back to floating-point numbers for calculations before being re-quantized to INT8 for subsequent steps. This approach balances computational efficiency with sufficient accuracy for most applications.

### **FP16**

FP16, or 16-bit floating-point numbers (float16), cuts memory usage in half compared to FP32 (32-bit floating-point numbers), making it advantageous for large-scale deep learning tasks. FP16 allows larger models or more data to be processed within the same GPU memory constraints. With modern GPUs increasingly supporting FP16 operations, this format can also enhance computation speeds. However, FP16’s reduced precision may cause numerical instability or accuracy loss in certain cases.

### **FP32**

FP32 provides higher precision and can represent a broader range of values. It’s the preferred choice for scenarios requiring complex mathematical operations or high-accuracy results. However, this higher precision comes at the cost of increased memory usage and longer computation times. For large-scale deep learning models, FP32 may lead to GPU memory limitations or slower inference speeds due to the sheer volume of parameters and data.

For mobile or IoT devices, Phi-3.x models can be converted to INT4, whereas AI PCs/Copilot PCs can utilize higher precisions like INT8, FP16, or FP32.

Currently, various hardware manufacturers provide frameworks to support generative models, including Intel's OpenVINO, Qualcomm's QNN, Apple's MLX, and Nvidia's CUDA. These frameworks, combined with quantized models, facilitate local deployment.

From a technical standpoint, different formats are supported after quantization, such as PyTorch/TensorFlow, GGUF, and ONNX. I’ve compared GGUF and ONNX formats in terms of application scenarios. Here, I recommend the ONNX quantization format due to its robust support across model frameworks and hardware. In this chapter, we will focus on ONNX Runtime for GenAI, OpenVINO, and Apple MLX for model quantization. (If you have a better approach, feel free to submit it via PR.)

**This chapter includes**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

It seems like you are asking for a translation of the provided disclaimer text into "mo." Could you clarify what "mo" refers to? Are you referring to a specific language, such as Maori, Mongolian, or something else?