<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:36:08+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "cs"
}
-->
# **Phi 家族的量化**

模型量化是指将神经网络模型中的参数（如权重和激活值）从较大的取值范围（通常是连续值范围）映射到较小的有限取值范围的过程。该技术可以减小模型的体积和计算复杂度，提高模型在移动设备或嵌入式系统等资源受限环境下的运行效率。模型量化通过降低参数的精度实现压缩，但也会带来一定的精度损失。因此，在量化过程中，需要在模型大小、计算复杂度和精度之间进行权衡。常见的量化方法包括定点量化、浮点量化等。你可以根据具体场景和需求选择合适的量化策略。

我们希望将 GenAI 模型部署到边缘设备，允许更多设备进入 GenAI 场景，如移动设备、AI PC/Copilot+PC 以及传统物联网设备。通过量化模型，我们可以基于不同设备将其部署到不同的边缘设备。结合硬件厂商提供的模型加速框架和量化模型，我们可以构建更优的 SLM 应用场景。

在量化场景中，我们有不同的精度（INT4、INT8、FP16、FP32）。以下是常用量化精度的说明：

### **INT4**

INT4 量化是一种激进的量化方法，将模型的权重和激活值量化为 4 位整数。由于表示范围更小、精度更低，INT4 量化通常会导致较大的精度损失。但与 INT8 量化相比，INT4 量化能进一步减少模型的存储需求和计算复杂度。需要注意的是，INT4 量化在实际应用中较为少见，因为过低的精度可能导致模型性能显著下降。此外，并非所有硬件都支持 INT4 操作，因此在选择量化方法时需考虑硬件兼容性。

### **INT8**

INT8 量化是将模型的权重和激活值从浮点数转换为 8 位整数的过程。尽管 INT8 整数的数值范围较小且精度较低，但它可以显著减少存储和计算需求。在 INT8 量化中，模型的权重和激活值经过量化处理，包括缩放和偏移，以尽可能保留原始浮点信息。在推理过程中，这些量化值会被反量化回浮点数进行计算，然后再量化回 INT8 用于下一步。这种方法在大多数应用中能够提供足够的精度，同时保持较高的计算效率。

### **FP16**

FP16 格式，即 16 位浮点数（float16），相比 32 位浮点数（float32）减少了一半的内存占用，在大规模深度学习应用中具有显著优势。FP16 格式允许在相同的 GPU 内存限制下加载更大模型或处理更多数据。随着现代 GPU 硬件持续支持 FP16 操作，使用 FP16 格式还可能带来计算速度的提升。然而，FP16 格式也有其固有缺点，即精度较低，某些情况下可能导致数值不稳定或精度损失。

### **FP32**

FP32 格式提供更高的精度，能够准确表示更广泛的数值范围。在执行复杂数学运算或需要高精度结果的场景下，优先选择 FP32 格式。但高精度也意味着更多的内存占用和更长的计算时间。对于大规模深度学习模型，尤其是模型参数众多且数据量巨大的情况下，FP32 格式可能导致 GPU 内存不足或推理速度下降。

在移动设备或物联网设备上，我们可以将 Phi-3.x 模型转换为 INT4，而 AI PC / Copilot PC 则可以使用更高精度，如 INT8、FP16、FP32。

目前，不同硬件厂商有不同的框架支持生成模型，如 Intel 的 OpenVINO、Qualcomm 的 QNN、Apple 的 MLX 和 Nvidia 的 CUDA 等，结合模型量化实现本地部署。

在技术层面，量化后我们支持不同格式，如 PyTorch / Tensorflow 格式、GGUF 和 ONNX。我做过 GGUF 和 ONNX 的格式对比及应用场景推荐，这里推荐 ONNX 量化格式，它在模型框架到硬件支持方面表现良好。本章将重点介绍使用 ONNX Runtime for GenAI、OpenVINO 及 Apple MLX 进行模型量化（如果你有更好的方法，也欢迎通过提交 PR 贡献给我们）。

**本章内容包括**

1. [使用 llama.cpp 量化 Phi-3.5 / 4](./UsingLlamacppQuantifyingPhi.md)

2. [使用 onnxruntime 生成式 AI 扩展量化 Phi-3.5 / 4](./UsingORTGenAIQuantifyingPhi.md)

3. [使用 Intel OpenVINO 量化 Phi-3.5 / 4](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [使用 Apple MLX 框架量化 Phi-3.5 / 4](./UsingAppleMLXQuantifyingPhi.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.