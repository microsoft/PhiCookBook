<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-09T19:38:58+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "en"
}
-->
# **Using Azure AI Foundry for Evaluation**

![aistudo](../../../../../imgs/01/05/AIFoundry/AIFoundry.png)

Learn how to evaluate your generative AI application using [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Whether you're testing single-turn or multi-turn conversations, Azure AI Foundry offers tools to assess model performance and safety.

![aistudo](../../../../../imgs/01/05/AIFoundry/AIPortfolio.png)

## How to Evaluate Generative AI Apps with Azure AI Foundry
For detailed instructions, see the [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Here are the steps to get started:

## Evaluating Generative AI Models in Azure AI Foundry

**Prerequisites**

- A test dataset in CSV or JSON format.
- A deployed generative AI model (such as Phi-3, GPT 3.5, GPT 4, or Davinci models).
- A runtime with a compute instance to run the evaluation.

## Built-in Evaluation Metrics

Azure AI Foundry lets you evaluate both single-turn and complex multi-turn conversations.  
For Retrieval Augmented Generation (RAG) scenarios, where the model is grounded in specific data, you can measure performance using built-in evaluation metrics.  
You can also evaluate general single-turn question answering scenarios (non-RAG).

## Creating an Evaluation Run

From the Azure AI Foundry UI, go to either the Evaluate page or the Prompt Flow page.  
Follow the evaluation creation wizard to set up an evaluation run. You can provide an optional name for your evaluation.  
Select the scenario that matches your application's goals.  
Choose one or more evaluation metrics to assess the model’s output.

## Custom Evaluation Flow (Optional)

For more flexibility, you can create a custom evaluation flow tailored to your specific needs.

## Viewing Results

After running the evaluation, you can log, view, and analyze detailed evaluation metrics in Azure AI Foundry. This helps you understand your application's strengths and weaknesses.

**Note** Azure AI Foundry is currently in public preview, so it’s best used for experimentation and development. For production workloads, consider other options. For more details and step-by-step guidance, check the official [AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.