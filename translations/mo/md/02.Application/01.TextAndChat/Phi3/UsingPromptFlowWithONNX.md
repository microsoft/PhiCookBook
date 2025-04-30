<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "20c7e34651318736a2606d351fcc37d0",
  "translation_date": "2025-04-04T12:44:57+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPromptFlowWithONNX.md",
  "language_code": "mo"
}
-->
# Using Windows GPU to create Prompt flow solution with Phi-3.5-Instruct ONNX

The following document provides an example of how to use PromptFlow with ONNX (Open Neural Network Exchange) to develop AI applications based on Phi-3 models.

PromptFlow is a set of development tools designed to simplify the entire development process of LLM-based (Large Language Model) AI applications, from brainstorming and prototyping to testing and evaluation.

By combining PromptFlow with ONNX, developers can:

- Optimize Model Performance: Utilize ONNX for efficient model inference and deployment.
- Simplify Development: Employ PromptFlow to manage workflows and automate repetitive tasks.
- Enhance Collaboration: Improve teamwork by offering a unified development environment.

**Prompt flow** is a suite of tools aimed at streamlining the entire development lifecycle of LLM-based AI applications, including ideation, prototyping, testing, evaluation, production deployment, and monitoring. It simplifies prompt engineering and allows you to create LLM apps with production-level quality.

Prompt flow supports connections to OpenAI, Azure OpenAI Service, and customizable models (Huggingface, local LLM/SLM). Our goal is to deploy Phi-3.5's quantized ONNX model to local applications. Prompt flow helps us better plan our projects and complete local solutions using Phi-3.5. In this example, we will integrate the ONNX Runtime GenAI Library to build a Prompt flow solution using Windows GPU.

## **Installation**

### **ONNX Runtime GenAI for Windows GPU**

Refer to this guide to set up ONNX Runtime GenAI for Windows GPU [click here](./ORTWindowGPUGuideline.md)

### **Set up Prompt flow in VSCode**

1. Install the Prompt flow VS Code Extension.

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.mo.png)

2. After installing the Prompt flow VS Code Extension, click on the extension and select **Installation dependencies**. Follow the provided guide to install the Prompt flow SDK in your environment.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.mo.png)

3. Download [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) and open the sample using VS Code.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.mo.png)

4. Open **flow.dag.yaml** and select your Python environment.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.mo.png)

   Open **chat_phi3_ort.py** and update the path to your Phi-3.5-instruct ONNX Model.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.mo.png)

5. Run your Prompt flow for testing.

Open **flow.dag.yaml** and click on the visual editor.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.mo.png)

After clicking this, execute the flow to test.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.mo.png)

1. You can run a batch in the terminal to view additional results.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

You can view the results in your default browser.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.mo.png)

It seems like you requested translation to "mo," but could you clarify what language or dialect "mo" refers to? For example, are you referring to Māori, Montenegrin, or another language? Let me know so I can assist you better!