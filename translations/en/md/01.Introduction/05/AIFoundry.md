# **Using Microsoft Foundry for Evaluation**

![aistudo](../../../../../translated_images/en/AIFoundry.9e0b513e999a1c5a.webp)

Learn how to evaluate your generative AI application using [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Whether you're testing single-turn or multi-turn conversations, Microsoft Foundry offers tools to assess model performance and safety.

![aistudo](../../../../../translated_images/en/AIPortfolio.69da59a8e1eaa70f.webp)

## How to Evaluate Generative AI Apps with Microsoft Foundry
For detailed instructions, see the [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Here’s how to get started:

## Evaluating Generative AI Models in Microsoft Foundry

**Prerequisites**

- A test dataset in CSV or JSON format.
- A deployed generative AI model (such as Phi-3, GPT 3.5, GPT 4, or Davinci models).
- A runtime with a compute instance to perform the evaluation.

## Built-in Evaluation Metrics

Microsoft Foundry supports evaluation of both single-turn and complex multi-turn conversations.  
For Retrieval Augmented Generation (RAG) scenarios, where the model is grounded in specific data, you can measure performance using built-in evaluation metrics.  
You can also evaluate general single-turn question answering scenarios (non-RAG).

## Creating an Evaluation Run

From the Microsoft Foundry UI, go to either the Evaluate page or the Prompt Flow page.  
Follow the evaluation creation wizard to set up your evaluation run. You can optionally name your evaluation.  
Select the scenario that matches your application’s goals.  
Choose one or more evaluation metrics to measure the model’s output.

## Custom Evaluation Flow (Optional)

For more flexibility, you can create a custom evaluation flow tailored to your specific needs.

## Viewing Results

After completing the evaluation, you can log, view, and analyze detailed evaluation metrics within Microsoft Foundry. This helps you understand your application’s strengths and weaknesses.

**Note** Microsoft Foundry is currently in public preview, so it’s best used for experimentation and development. For production workloads, consider other options. For more information and step-by-step guidance, check the official [AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.