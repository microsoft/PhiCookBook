<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-12-21T22:37:46+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "pcm"
}
-->
# **Make we introduce Promptflow**

 [Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) na visual workflow automation tool wey dey allow people build automated workflows by using pre-built templates and custom connectors. E design make developers and business analysts fit quickly build automated processes for work dem like data management, collaboration, and process optimization. With Prompt Flow, people fit quickly connect different services, applications, and systems, and automate complex business processes.

 Microsoft Prompt Flow na tool wey dem design to simplify the whole end-to-end development cycle for AI applications wey Large Language Models (LLMs) dey power. Whether you dey brainstorm, prototype, test, evaluate, or deploy LLM-based applications, Prompt Flow dey make the process easy and e dey help you build LLM apps wey ready for production.

## Na di key features and benefits wey you go get if you use Microsoft Prompt Flow:

**Interactive Authoring Experience**

Prompt Flow dey show visual representation of how your flow take be, so e dey easy to understand and waka around your projects.
E still get notebook-like coding experience wey make flow development and debugging fast and efficient.

**Prompt Variants and Tuning**

You fit create and compare different prompt variants to help you fine-tune stuff step-by-step. Test how different prompts dey perform and choose di ones wey better.

**Built-in Evaluation Flows**
Use the built-in evaluation tools to check the quality and effectiveness of your prompts and flows.
Make you sabi how well your LLM-based applications dey perform.

**Comprehensive Resources**

Prompt Flow get library of built-in tools, samples, and templates. These resources fit serve as starting point for development, give inspiration, and speed up the work.

**Collaboration and Enterprise Readiness**

E support team collaboration make many people fit work together on prompt engineering projects.
You fit maintain version control and share knowledge well. E dey streamline the whole prompt engineering process, from development and evaluation to deployment and monitoring.

## Evaluation in Prompt Flow 

For Microsoft Prompt Flow, evaluation dey play important role to check how well your AI models dey perform. Make we look how you fit customize evaluation flows and metrics inside Prompt Flow:

![PF Vizualize](../../../../../translated_images/pfvisualize.c1d9ca75baa2a222.pcm.png)

**Understanding Evaluation in Prompt Flow**

For Prompt Flow, flow mean sequence of nodes wey dey process input and generate output. Evaluation flows na special kind of flows wey dem design to assess how one run perform based on specific criteria and goals.

**Key features of evaluation flows**

Dem usually dey run after the flow wey dem dey test, using the outputs from that flow. Dem go calculate scores or metrics to measure how the tested flow take perform. Metrics fit include accuracy, relevance scores, or any other measures wey matter.

### Customizing Evaluation Flows

**Defining Inputs**

Evaluation flows need make dem accept the outputs of the run wey dem dey test. Define inputs same way you dey do for normal flows.
For example, if you dey evaluate QnA flow, name one input "answer." If you dey evaluate classification flow, name input "category." You fit still need ground truth inputs (like the actual labels).

**Outputs and Metrics**

Evaluation flows go produce results wey go measure how the tested flow perform. You fit calculate metrics using Python or LLM (Large Language Models). Use the log_metric() function to log the metrics wey matter.

**Using Customized Evaluation Flows**

Create your own evaluation flow wey match your specific tasks and objectives. Customize metrics based on wetin you wan evaluate.
Apply this customized evaluation flow to batch runs when you dey do large-scale testing.

## Built-in Evaluation Methods

Prompt Flow still get built-in evaluation methods.
You fit submit batch runs and use these methods to evaluate how your flow dey perform with large datasets.
View evaluation results, compare metrics, and iterate as you need.
Remember say evaluation important to make sure your AI models meet the criteria and goals wey you want. Check the official documentation for detailed steps on how to develop and use evaluation flows for Microsoft Prompt Flow.

To summarize, Microsoft Prompt Flow dey empower developers to build high-quality LLM applications by making prompt engineering simple and providing strong development environment. If you dey work with LLMs, Prompt Flow na tool wey worth to try. Explore the [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) for detailed instructions on how to develop and use evaluation flows for Microsoft Prompt Flow.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate wit AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note sey automatic translations fit get mistakes or wrong meanings. Di original dokument for im original language na di official/authoritative source. If na critical information, e better make professional human translator handle am. We no dey liable for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->