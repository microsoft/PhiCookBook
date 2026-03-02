## 微调场景

![FineTuning with MS Services](../../../../translated_images/zh-CN/FinetuningwithMS.3d0cec8ae693e094.webp)

本节概述了 Microsoft Foundry 和 Azure 环境中的微调场景，包括部署模型、基础设施层以及常用的优化技术。

**平台**  
包括托管服务，如 Microsoft Foundry（原 Azure AI Foundry）和 Azure 机器学习，提供模型管理、编排、实验跟踪和部署工作流。

**基础设施**  
微调需要可扩展的计算资源。在 Azure 环境中，这通常包括基于 GPU 的虚拟机和用于轻量级工作负载的 CPU 资源，以及用于数据集和检查点的可扩展存储。

**工具与框架**  
微调工作流通常依赖于诸如 Hugging Face Transformers、DeepSpeed 和 PEFT（参数高效微调）等框架和优化库。

使用微软技术的微调过程涵盖平台服务、计算基础设施和训练框架。通过理解这些组件如何协同工作，开发人员能够高效地将基础模型适配到特定任务和生产场景中。

## 模型即服务

使用托管微调功能微调模型，无需创建和管理计算资源。

![MaaS Fine Tuning](../../../../translated_images/zh-CN/MaaSfinetune.3eee4630607aff0d.webp)

无服务器微调现已支持 Phi-3、Phi-3.5 和 Phi-4 模型系列，开发者可以快速轻松地为云端和边缘场景定制模型，无需安排计算资源。

## 模型即平台

用户自行管理计算资源以进行模型微调。

![Maap Fine Tuning](../../../../translated_images/zh-CN/MaaPFinetune.fd3829c1122f5d1c.webp)

[微调示例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 微调技术对比

|场景|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|将预训练大语言模型适配到特定任务或领域|是|是|是|是|是|是|
|针对文本分类、命名实体识别和机器翻译等NLP任务微调|是|是|是|是|是|是|
|针对问答任务微调|是|是|是|是|是|是|
|为聊天机器人生成类人响应进行微调|是|是|是|是|是|是|
|为生成音乐、艺术或其他创意形式微调|是|是|是|是|是|是|
|降低计算和财务成本|是|是|是|是|是|是|
|减少内存使用|是|是|是|是|是|是|
|使用更少参数实现高效微调|是|是|是|否|否|是|
|一种内存高效的数据并行形式，可访问所有GPU设备的总GPU内存|否|否|否|是|是|否|

> [!NOTE]
> LoRA、QLoRA、PEFT 和 DoRA 是参数高效微调方法，而 DeepSpeed 和 ZeRO 侧重于分布式训练和内存优化。

## 微调性能示例

![Finetuning Performance](../../../../translated_images/zh-CN/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档通过AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或曲解承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->