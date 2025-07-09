<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-07-09T19:37:06+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "en"
}
-->
# **Introduce Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) is a visual workflow automation tool that lets users create automated workflows using pre-built templates and custom connectors. It’s designed to help developers and business analysts quickly build automated processes for tasks like data management, collaboration, and process optimization. With Prompt Flow, users can easily connect different services, applications, and systems to automate complex business processes.

Microsoft Prompt Flow is built to streamline the entire development cycle of AI applications powered by Large Language Models (LLMs). Whether you’re brainstorming, prototyping, testing, evaluating, or deploying LLM-based applications, Prompt Flow simplifies the process and helps you build production-quality LLM apps.

## Here are the key features and benefits of using Microsoft Prompt Flow:

**Interactive Authoring Experience**

Prompt Flow offers a visual layout of your flow’s structure, making it easy to understand and navigate your projects.  
It provides a notebook-style coding experience for efficient flow development and debugging.

**Prompt Variants and Tuning**

Create and compare multiple prompt variants to support an iterative refinement process. Evaluate the performance of different prompts and select the most effective ones.

**Built-in Evaluation Flows**

Evaluate the quality and effectiveness of your prompts and flows using built-in evaluation tools.  
Gain insights into how well your LLM-based applications are performing.

**Comprehensive Resources**

Prompt Flow includes a library of built-in tools, samples, and templates. These resources serve as a starting point for development, spark creativity, and speed up the process.

**Collaboration and Enterprise Readiness**

Enable team collaboration by allowing multiple users to work together on prompt engineering projects.  
Maintain version control and share knowledge efficiently. Streamline the entire prompt engineering process—from development and evaluation to deployment and monitoring.

## Evaluation in Prompt Flow

In Microsoft Prompt Flow, evaluation is key to measuring how well your AI models perform. Let’s look at how you can customize evaluation flows and metrics within Prompt Flow:

![PFVizualise](../../../../../imgs/01/05/PromptFlow/pfvisualize.png)

**Understanding Evaluation in Prompt Flow**

In Prompt Flow, a flow is a sequence of nodes that process input and generate output. Evaluation flows are special flows designed to assess the performance of a run based on specific criteria and goals.

**Key features of evaluation flows**

They usually run after the flow being tested, using its outputs. They calculate scores or metrics to measure the tested flow’s performance. Metrics can include accuracy, relevance scores, or other relevant measures.

### Customizing Evaluation Flows

**Defining Inputs**

Evaluation flows need to accept the outputs of the run being tested. Define inputs just like in standard flows.  
For example, if you’re evaluating a QnA flow, name an input “answer.” If evaluating a classification flow, name an input “category.” You may also need ground truth inputs (e.g., actual labels).

**Outputs and Metrics**

Evaluation flows produce results that measure the tested flow’s performance. Metrics can be calculated using Python or LLM (Large Language Models). Use the log_metric() function to record relevant metrics.

**Using Customized Evaluation Flows**

Create your own evaluation flow tailored to your specific tasks and goals. Customize metrics based on your evaluation objectives.  
Apply this customized evaluation flow to batch runs for large-scale testing.

## Built-in Evaluation Methods

Prompt Flow also offers built-in evaluation methods.  
You can submit batch runs and use these methods to evaluate how well your flow performs with large datasets.  
View evaluation results, compare metrics, and iterate as needed.  
Remember, evaluation is essential to ensure your AI models meet desired criteria and goals. Check the official documentation for detailed guidance on developing and using evaluation flows in Microsoft Prompt Flow.

In summary, Microsoft Prompt Flow empowers developers to build high-quality LLM applications by simplifying prompt engineering and providing a powerful development environment. If you’re working with LLMs, Prompt Flow is a valuable tool to explore. Visit the [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) for detailed instructions on developing and using evaluation flows in Microsoft Prompt Flow.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.