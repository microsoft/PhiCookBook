# **Quantifying Phi Family**

Model quantization na di process wey dem dey use take map di parameters (like weights and activation values) for neural network model from big value range (wey dey continuous normally) go small finite value range. Dis technology fit reduce di size and computational complexity of di model and make di model work better for resource-constrained environments like mobile devices or embedded systems. Model quantization dey compress by reducing di precision of parameters, but e go still carry some precision loss. So for di quantization process, you gas balance di model size, computational complexity, and precision. Common quantization methods include fixed-point quantization, floating-point quantization, etc. You fit select di correct quantization strategy based on di scenario and wetin you need.

We wan deploy GenAI model to edge devices and mek more devices fit enter GenAI scenarios, like mobile devices, AI PC/Copilot+PC, and traditional IoT devices. Through di quantization model, we fit deploy am to different edge devices based on di device type. We fit combine am with di model acceleration framework and di quantization model wey hardware manufacturers provide so we fit build better SLM application scenarios.

For di quantization scenario, we get different precisions (INT4, INT8, FP16, FP32). Below na explanation of di common quantization precisions

### **INT4**

INT4 quantization na radical quantization method wey dey quantize di weights and activation values of di model into 4-bit integers. INT4 quantization normally dey cause bigger loss of precision because di range to represent am small and e get low precision. But compared to INT8 quantization, INT4 quantization fit reduce storage and computational complexity of di model even more. Make you sabi say INT4 quantization no too common for practical use because if accuracy too low e fit cause big drop for model performance. Also, not all hardware dey support INT4 operations, so you need check if hardware go work with am before you choose am.

### **INT8**

INT8 quantization na di way to change model’s weights and activations from floating point numbers go 8-bit integers. Even though di number range wey INT8 integers fit represent smaller and no too precise, e fit reduce storage and calculation requirements wella. For INT8 quantization, di model weights and activation values dey go through quantization process, wey get scaling and offset to keep original floating point information as much as e fit. During inference, di quantized values go turn back to floating point numbers for calculation, then dem go quantize am back to INT8 for di next step. Dis method fit provide enough accuracy for most apps and still dey efficient for computation.

### **FP16**

Di FP16 format, wey mean 16-bit floating point numbers (float16), dey reduce memory footprint by half compared to 32-bit floating point numbers (float32), and dis get big advantage for big deep learning applications. Di FP16 format fit make you load bigger models or process more data inside di same GPU memory limit. As modern GPU hardware still dey support FP16 operations, using FP16 fit also improve computing speed. But di FP16 format still get some kon, like e no too precise, and dis fit cause some numerical instability or precision loss sometimes.

### **FP32**

Di FP32 format get higher precision and fit correctly represent plenty range of values. For scenarios wey need complex mathematical operations or high-precision results, FP32 format dey preferred. But high accuracy mean say e go use more memory and calculation time go long. For big deep learning models, especially when plenty model parameters and data dey, FP32 format fit cause insufficient GPU memory or make inference speed slow down.

For mobile devices or IoT devices, we fit convert Phi-3.x models to INT4, while AI PC / Copilot PC fit use higher precision like INT8, FP16, FP32.

Right now, different hardware manufacturers get different frameworks to support generative models like Intel's OpenVINO, Qualcomm's QNN, Apple's MLX, and Nvidia's CUDA, combined with model quantization to make local deployment complete.

For technology side, we get different format supports after quantization like PyTorch / TensorFlow format, GGUF, and ONNX. I don compare GGUF and ONNX formats and their application scenarios. I recommend di ONNX quantization format because e get better support from model framework go hardware. For dis chapter, we go focus on ONNX Runtime for GenAI, OpenVINO, and Apple MLX to do model quantization (if you get better way, you fit also give am to us by submitting PR)

**Dis chapter include**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg sabi say automatic translation fit get some mistakes or wrong parts. Di original document wey dem write for im own language na di main correct one. If na serious information, e good make person wey sabi do human translation check am. We no go take any blame if person misunderstand or wrongly take wetin dis translation talk.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->