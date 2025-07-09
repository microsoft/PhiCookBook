<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-09T19:21:17+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "en"
}
-->
# Using Windows GPU to create Prompt flow solution with Phi-3.5-Instruct ONNX 

The following document is an example of how to use PromptFlow with ONNX (Open Neural Network Exchange) to develop AI applications based on Phi-3 models.

PromptFlow is a set of development tools designed to simplify the entire development cycle of LLM-based (Large Language Model) AI applications, from ideation and prototyping to testing and evaluation.

By integrating PromptFlow with ONNX, developers can:

- Optimize Model Performance: Use ONNX for efficient model inference and deployment.
- Simplify Development: Use PromptFlow to manage workflows and automate repetitive tasks.
- Enhance Collaboration: Improve teamwork by providing a unified development environment.

**Prompt flow** is a set of development tools designed to streamline the full development cycle of LLM-based AI applications, from ideation, prototyping, testing, and evaluation to production deployment and monitoring. It makes prompt engineering much easier and allows you to build LLM apps with production-level quality.

Prompt flow can connect to OpenAI, Azure OpenAI Service, and customizable models (Huggingface, local LLM/SLM). Our goal is to deploy Phi-3.5's quantized ONNX model to local applications. Prompt flow helps us better plan our business and complete local solutions based on Phi-3.5. In this example, we will combine ONNX Runtime GenAI Library to build the Prompt flow solution using Windows GPU.

## **Installation**

### **ONNX Runtime GenAI for Windows GPU**

Follow this guide to set up ONNX Runtime GenAI for Windows GPU [click here](./ORTWindowGPUGuideline.md)

### **Set up Prompt flow in VSCode**

1. Install the Prompt flow VS Code Extension

![pfvscode](../../../../../../imgs/02/pfonnx/pfvscode.png)

2. After installing the Prompt flow VS Code Extension, click the extension and select **Installation dependencies**. Follow this guide to install the Prompt flow SDK in your environment.

![pfsetup](../../../../../../imgs/02/pfonnx/pfsetup.png)

3. Download the [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) and open it in VS Code.

![pfsample](../../../../../../imgs/02/pfonnx/pfsample.png)

4. Open **flow.dag.yaml** to select your Python environment.

![pfdag](../../../../../../imgs/02/pfonnx/pfdag.png)

   Open **chat_phi3_ort.py** to update the location of your Phi-3.5-instruct ONNX Model.

![pfphi](../../../../../../imgs/02/pfonnx/pfphi.png)

5. Run your prompt flow to test it.

Open **flow.dag.yaml** and click the visual editor.

![pfv](../../../../../../imgs/02/pfonnx/pfv.png)

After clicking this, run it to test.

![pfflow](../../../../../../imgs/02/pfonnx/pfflow.png)

1. You can also run batch commands in the terminal to check more results.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

You can view the results in your default browser.

![pfresult](../../../../../../imgs/02/pfonnx/pfresult.png)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.