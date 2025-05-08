<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-07T13:59:17+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "zh"
}
-->
# 使用 Windows GPU 创建基于 Phi-3.5-Instruct ONNX 的 Prompt flow 解决方案

以下文档示例展示了如何使用 PromptFlow 和 ONNX（开放神经网络交换格式）来开发基于 Phi-3 模型的 AI 应用。

PromptFlow 是一套开发工具，旨在简化基于大语言模型（LLM）的 AI 应用从构思、原型设计到测试和评估的端到端开发流程。

通过将 PromptFlow 与 ONNX 集成，开发者可以：

- 优化模型性能：利用 ONNX 实现高效的模型推理和部署。
- 简化开发流程：使用 PromptFlow 管理工作流并自动化重复任务。
- 增强协作效率：通过统一的开发环境促进团队成员之间更好的协作。

**Prompt flow** 是一套开发工具，设计用于简化基于 LLM 的 AI 应用的端到端开发周期，从构思、原型设计、测试、评估到生产部署和监控。它使得 prompt 工程变得更加轻松，帮助你构建具有生产质量的 LLM 应用。

Prompt flow 可以连接 OpenAI、Azure OpenAI 服务以及可定制模型（Huggingface、本地 LLM/SLM）。我们希望将 Phi-3.5 的量化 ONNX 模型部署到本地应用中。Prompt flow 能帮助我们更好地规划业务，并基于 Phi-3.5 完成本地解决方案。在本示例中，我们将结合 ONNX Runtime GenAI 库，基于 Windows GPU 完成 Prompt flow 解决方案。

## **安装**

### **Windows GPU 的 ONNX Runtime GenAI**

阅读此指南以设置 Windows GPU 版 ONNX Runtime GenAI [点击这里](./ORTWindowGPUGuideline.md)

### **在 VSCode 中设置 Prompt flow**

1. 安装 Prompt flow VS Code 扩展

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.zh.png)

2. 安装完 Prompt flow VS Code 扩展后，点击该扩展，选择 **Installation dependencies**，按照指南在你的环境中安装 Prompt flow SDK

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.zh.png)

3. 下载 [示例代码](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf)，并使用 VS Code 打开该示例

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.zh.png)

4. 打开 **flow.dag.yaml** 选择你的 Python 环境

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.zh.png)

   打开 **chat_phi3_ort.py** 修改 Phi-3.5-instruct ONNX 模型的位置

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.zh.png)

5. 运行你的 prompt flow 进行测试

打开 **flow.dag.yaml**，点击可视化编辑器

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.zh.png)

点击后运行以进行测试

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.zh.png)

1. 你也可以在终端运行批处理以查看更多结果


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

你可以在默认浏览器中查看结果


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.zh.png)

**免责声明**：  
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译而成。尽管我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的原文版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而引起的任何误解或误释承担责任。