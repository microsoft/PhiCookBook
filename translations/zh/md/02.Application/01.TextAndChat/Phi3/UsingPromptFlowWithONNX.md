<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:57:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "zh"
}
-->
# 使用 Windows GPU 创建基于 Phi-3.5-Instruct ONNX 的 Prompt flow 解决方案

以下文档示例展示了如何使用 PromptFlow 结合 ONNX（开放神经网络交换格式）来开发基于 Phi-3 模型的 AI 应用。

PromptFlow 是一套开发工具，旨在简化基于大型语言模型（LLM）的 AI 应用从构思、原型设计到测试和评估的端到端开发流程。

通过将 PromptFlow 与 ONNX 集成，开发者可以：

- 优化模型性能：利用 ONNX 实现高效的模型推理和部署。
- 简化开发流程：使用 PromptFlow 管理工作流并自动化重复任务。
- 增强协作：通过提供统一的开发环境，促进团队成员间更好的协作。

**Prompt flow** 是一套开发工具，旨在简化基于 LLM 的 AI 应用从构思、原型设计、测试、评估到生产部署和监控的完整开发周期。它让提示工程变得更加轻松，使你能够构建具备生产质量的 LLM 应用。

Prompt flow 可以连接 OpenAI、Azure OpenAI 服务以及可定制模型（Huggingface、本地 LLM/SLM）。我们希望将 Phi-3.5 的量化 ONNX 模型部署到本地应用中。Prompt flow 可以帮助我们更好地规划业务，并基于 Phi-3.5 完成本地解决方案。在本示例中，我们将结合 ONNX Runtime GenAI 库，基于 Windows GPU 完成 Prompt flow 解决方案。

## **安装**

### **适用于 Windows GPU 的 ONNX Runtime GenAI**

请阅读本指南以设置适用于 Windows GPU 的 ONNX Runtime GenAI  [点击这里](./ORTWindowGPUGuideline.md)

### **在 VSCode 中设置 Prompt flow**

1. 安装 Prompt flow VS Code 扩展

![pfvscode](../../../../../../translated_images/zh/pfvscode.eff93dfc66a42cbe.png)

2. 安装 Prompt flow VS Code 扩展后，点击扩展，选择 **Installation dependencies**，按照指南在你的环境中安装 Prompt flow SDK

![pfsetup](../../../../../../translated_images/zh/pfsetup.b46e93096f5a254f.png)

3. 下载 [示例代码](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf)，并使用 VS Code 打开该示例

![pfsample](../../../../../../translated_images/zh/pfsample.8d89e70584ffe7c4.png)

4. 打开 **flow.dag.yaml** 选择你的 Python 环境

![pfdag](../../../../../../translated_images/zh/pfdag.264a77f7366458ff.png)

   打开 **chat_phi3_ort.py** 修改你的 Phi-3.5-instruct ONNX 模型路径

![pfphi](../../../../../../translated_images/zh/pfphi.72da81d74244b45f.png)

5. 运行你的 prompt flow 进行测试

打开 **flow.dag.yaml**，点击可视化编辑器

![pfv](../../../../../../translated_images/zh/pfv.ba8a81f34b20f603.png)

点击后运行测试

![pfflow](../../../../../../translated_images/zh/pfflow.4e1135a089b1ce1b.png)

1. 你也可以在终端批量运行以查看更多结果

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

你可以在默认浏览器中查看结果

![pfresult](../../../../../../translated_images/zh/pfresult.c22c826f8062d7cb.png)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。