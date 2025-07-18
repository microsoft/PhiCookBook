<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:56:15+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "en"
}
-->
# Using Windows GPU to create Prompt flow solution with Phi-3.5-Instruct ONNX 

The following document is an example of how to use PromptFlow with ONNX (Open Neural Network Exchange) for developing AI applications based on Phi-3 models.

PromptFlow is a suite of development tools designed to streamline the end-to-end development cycle of LLM-based (Large Language Model) AI applications, from ideation and prototyping to testing and evaluation.

By integrating PromptFlow with ONNX, developers can:

- Optimize Model Performance: Leverage ONNX for efficient model inference and deployment.
- Simplify Development: Use PromptFlow to manage the workflow and automate repetitive tasks.
- Enhance Collaboration: Facilitate better collaboration among team members by providing a unified development environment.

**Prompt flow** is a suite of development tools designed to streamline the end-to-end development cycle of LLM-based AI applications, from ideation, prototyping, testing, evaluation to production deployment and monitoring. It makes prompt engineering much easier and enables you to build LLM apps with production quality.

Prompt flow can connect to OpenAI, Azure OpenAI Service, and customizable models (Huggingface, local LLM/SLM). We hope to deploy Phi-3.5's quantized ONNX model to local applications. Prompt flow can help us better plan our business and complete local solutions based on Phi-3.5. In this example, we will combine ONNX Runtime GenAI Library to complete the Prompt flow solution based on Windows GPU.

## **Installation**

### **ONNX Runtime GenAI for Windows GPU**

Read this guideline to set ONNX Runtime GenAI for Windows GPU  [click here](./ORTWindowGPUGuideline.md)

### **Set up Prompt flow in VSCode**

1. Install Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.en.png)

2. After installing the Prompt flow VS Code Extension, click the extension and choose **Installation dependencies**. Follow this guideline to install the Prompt flow SDK in your environment.

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.en.png)

3. Download [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) and open this sample in VS Code.

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.en.png)

4. Open **flow.dag.yaml** to select your Python environment.

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.en.png)

   Open **chat_phi3_ort.py** to update the location of your Phi-3.5-instruct ONNX Model.

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.en.png)

5. Run your prompt flow to test it.

Open **flow.dag.yaml** and click the visual editor.

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.en.png)

After clicking this, run it to test.

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.en.png)

1. You can run batch commands in the terminal to check more results.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

You can view the results in your default browser.

![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.en.png)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.