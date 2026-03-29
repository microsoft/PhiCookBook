# Evaluate di Fine-tuned Phi-3 / Phi-3.5 Model for Microsoft Foundry Wey Sharp Focus on Microsoft Responsible AI Principles

Dis end-to-end (E2E) sample dey based on di guide "[Evaluate Fine-tuned Phi-3 / 3.5 Models for Microsoft Foundry Wey Sharp Focus on Microsoft Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" from Microsoft Tech Community.

## Overview

### How you fit evaluate di safety and performance of fine-tuned Phi-3 / Phi-3.5 model for Microsoft Foundry?

Fine-tuning one model fit sometimes make am give unwanted or wrong answers. To make sure sey di model still dey safe and correct, e important to evaluate di model if e fit produce bad content and if e fit give correct, relevant, and smooth answers. For dis tutorial, you go learn how to evaluate di safety and performance of fine-tuned Phi-3 / Phi-3.5 model wey dem join with Prompt flow for Microsoft Foundry.

See di Microsoft Foundry evaluation process.

![Architecture of tutorial.](../../../../../../translated_images/pcm/architecture.10bec55250f5d6a4.webp)

*Image Source: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> For more better info and to see more resources about Phi-3 / Phi-3.5, abeg visit [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prerequisites

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 model

### Table of Contents

1. [**Scenario 1: Introduction to Microsoft Foundry's Prompt flow evaluation**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Introduction to safety evaluation](#introduction-to-safety-evaluation)
    - [Introduction to performance evaluation](#introduction-to-performance-evaluation)

1. [**Scenario 2: Evaluating the Phi-3 / Phi-3.5 model in Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Before you begin](#before-you-begin)
    - [Deploy Azure OpenAI to evaluate the Phi-3 / Phi-3.5 model](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Evaluate the fine-tuned Phi-3 / Phi-3.5 model using Microsoft Foundry's Prompt flow evaluation](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Congratulations!](#congratulations)

## **Scenario 1: Introduction to Microsoft Foundry's Prompt flow evaluation**

### Introduction to safety evaluation

To make sure sey your AI model dey ethical and safe, e dey very important to check am against Microsoft Responsible AI Principles dem. For Microsoft Foundry, safety evaluation make you fit check if your model fit get problem to jailbreak attacks and if e fit produce bad content, wey gatz align with dis principles.

![Safaty evaluation.](../../../../../../translated_images/pcm/safety-evaluation.083586ec88dfa950.webp)

*Image Source: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft Responsible AI Principles

Before you start di technical waka, e important make you sabi Microsoft Responsible AI Principles, na ethical framework wey dem make to guide responsible way to develop, deploy, and manage AI systems. Dem principles dey guide how to design, develop, and deploy AI systems responsibly, to make sure AI technology dey fair, transparent, and include everybody. Dem principles na di foundation wey you go use check if AI models dey safe.

Microsoft Responsible AI Principles include:

- **Fairness and Inclusiveness**: AI systems gatz treat everybody fair and no make any group suffer differently. For example, if AI dey yarn for medical treatment, loan applications, or job, e suppose give same advice to everybody wey get similar symptom, money matter, or qualification.

- **Reliability and Safety**: To build trust, e important sey AI systems dey reliable, safe, and consistent. Dem suppose fit waka di way dem design am, respond safe to things wey nobody expect, and no gree make bad people manipulate am. How dem dey behave and different condition dem fit handle na wetin di developers think about when dem design and test am.

- **Transparency**: When AI systems dey help make decisions wey fit affect people life well well, e important sey people understand how dem take do the decisions. For example, bank fit use AI decide if person fit get loan. Company fit use AI decide who good pass to employ.

- **Privacy and Security**: As AI dey everywhere, to protect privacy and secure personal and business info dey important and e no easy. AI need data to fit make correct and proper predictions and decisions about people, so privacy and security gatz dey tight.

- **Accountability**: People wey design and deploy AI systems gatz be responsible for how their systems dey work. Organizations suppose follow industry standard to make accountability norms. Dis norms fit make sure sey AI no be only authority for decisions wey fit affect people life. E fit also make sure sey humans still dey control AI system wey fit dey independent.

![Fill hub.](../../../../../../translated_images/pcm/responsibleai2.c07ef430113fad8c.webp)

*Image Source: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> To sabi more about Microsoft Responsible AI Principles, abeg visit [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Safety metrics

For dis tutorial, you go check the safety of fine-tuned Phi-3 model using Microsoft Foundry safety metrics dem. Dis metrics go help you know if model fit produce bad content or if e fit get problem with jailbreak attacks. Di safety metrics include:

- **Self-harm-related Content**: Check if model get tendency to produce content about self-harm.
- **Hateful and Unfair Content**: Check if model get tendency to produce content wey hate or be unfair.
- **Violent Content**: Check if model get tendency to produce violent content.
- **Sexual Content**: Check if model get tendency to produce inappropriate sexual content.

Checking dis ones go make sure sey AI model no go produce bad or offensive content, and e go align with society values and laws.

![Evaluate based on safety.](../../../../../../translated_images/pcm/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introduction to performance evaluation

To make sure sey your AI model dey perform as you expect, e dey important to check im performance using performance metrics. For Microsoft Foundry, performance evaluation allow you check how your model dey produce correct, relevant, and smooth answers.

![Safaty evaluation.](../../../../../../translated_images/pcm/performance-evaluation.48b3e7e01a098740.webp)

*Image Source: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Performance metrics

For dis tutorial, you go check performance of fine-tuned Phi-3 / Phi-3.5 model using Microsoft Foundry performance metrics dem. Dis metrics go help you know if model fit give correct, relevant, and coherent answers. Di performance metrics include:

- **Groundedness**: Check how well di generated answer match di info from di input source.
- **Relevance**: Check if di answer dey related well to di question wey dem ask.
- **Coherence**: Check if di generated text dey flow well, e clear, and e be like human talk.
- **Fluency**: Check how good di language of di generated text be.
- **GPT Similarity**: Compare di generated answer with di correct answer to see how similar dem be.
- **F1 Score**: Calculate how much words share for di generated answer and di source data.

Dis metrics go help you check if di model fit produce correct, relevant, and smooth answers.

![Evaluate based on performance.](../../../../../../translated_images/pcm/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenario 2: Evaluating the Phi-3 / Phi-3.5 model in Microsoft Foundry**

### Before you begin

Dis tutorial na continuation from di previous blog posts, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" and "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." For these posts, we show how to fine-tune Phi-3 / Phi-3.5 model for Microsoft Foundry and join am with Prompt flow.

For dis tutorial, you go deploy Azure OpenAI model as evaluator for Microsoft Foundry and use am to check your fine-tuned Phi-3 / Phi-3.5 model.

Before you start dis tutorial, make sure sey you get these prerequisites like how we describe am for previous tutorials:

1. Dataset wey you prepare to evaluate the fine-tuned Phi-3 / Phi-3.5 model.
1. Phi-3 / Phi-3.5 model wey you don fine-tune and deploy for Azure Machine Learning.
1. Prompt flow wey join your fine-tuned Phi-3 / Phi-3.5 model inside Microsoft Foundry.

> [!NOTE]
> You go use *test_data.jsonl* file, wey dey for data folder from **ULTRACHAT_200k** dataset wey you download for previous blog posts, as di dataset wey you go use check di fine-tuned Phi-3 / Phi-3.5 model.

#### Integrate di custom Phi-3 / Phi-3.5 model with Prompt flow for Microsoft Foundry(Code first approach)

> [!NOTE]
> If you follow di low-code way wey dem explain for "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", you fit skip dis exercise and go next one.
> But if you follow di code-first way wey dem explain for "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" to fine-tune and deploy your Phi-3 / Phi-3.5 model, di way to connect your model to Prompt flow small different. You go learn this method for dis exercise.

To continue, you gatz join your fine-tuned Phi-3 / Phi-3.5 model inside Prompt flow for Microsoft Foundry.

#### Create Microsoft Foundry Hub

You gatz create one Hub before you create Project. Hub dey act like Resource Group, e go help you organize and manage multiple Projects inside Microsoft Foundry.
1. Sign in [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Select **All hubs** from di left side tab.

1. Select **+ New hub** from di navigation menu.

    ![Create hub.](../../../../../../translated_images/pcm/create-hub.5be78fb1e21ffbf1.webp)

1. Do dis tin dem:

    - Enter **Hub name**. E for be unique value.
    - Select your Azure **Subscription**.
    - Select di **Resource group** wey you go use (make new one if e need).
    - Select di **Location** wey you like use.
    - Select di **Connect Azure AI Services** wey you go use (make new one if e need).
    - Select **Connect Azure AI Search** to **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/pcm/fill-hub.baaa108495c71e34.webp)

1. Select **Next**.

#### Create Microsoft Foundry Project

1. For di Hub wey you create, select **All projects** from di left side tab.

1. Select **+ New project** from di navigation menu.

    ![Select new project.](../../../../../../translated_images/pcm/select-new-project.cd31c0404088d7a3.webp)

1. Enter **Project name**. E for be unique value.

    ![Create project.](../../../../../../translated_images/pcm/create-project.ca3b71298b90e420.webp)

1. Select **Create a project**.

#### Add a custom connection for di fine-tuned Phi-3 / Phi-3.5 model

To join your custom Phi-3 / Phi-3.5 model with Prompt flow, you need save di model endpoint and key for custom connection. Dis arrangement go make sure say you fit access your custom Phi-3 / Phi-3.5 model for Prompt flow.

#### Set api key and endpoint uri of di fine-tuned Phi-3 / Phi-3.5 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Go di Azure Machine learning workspace wey you create.

1. Select **Endpoints** from di left side tab.

    ![Select endpoints.](../../../../../../translated_images/pcm/select-endpoints.ee7387ecd68bd18d.webp)

1. Select endpoint wey you create.

    ![Select endpoints.](../../../../../../translated_images/pcm/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Select **Consume** from di navigation menu.

1. Copy your **REST endpoint** and **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pcm/copy-endpoint-key.0650c3786bd646ab.webp)

#### Add di Custom Connection

1. Visit [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Go di Microsoft Foundry project wey you create.

1. For di Project wey you create, select **Settings** from di left side tab.

1. Select **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/pcm/select-new-connection.fa0f35743758a74b.webp)

1. Select **Custom keys** from di navigation menu.

    ![Select custom keys.](../../../../../../translated_images/pcm/select-custom-keys.5a3c6b25580a9b67.webp)

1. Do dis tin dem:

    - Select **+ Add key value pairs**.
    - For key name, enter **endpoint** and paste di endpoint wey you copy from Azure ML Studio inside di value field.
    - Select **+ Add key value pairs** again.
    - For key name, enter **key** and paste di key wey you copy from Azure ML Studio inside di value field.
    - After you add di keys, select **is secret** to sey di key no go show.

    ![Add connection.](../../../../../../translated_images/pcm/add-connection.ac7f5faf8b10b0df.webp)

1. Select **Add connection**.

#### Create Prompt flow

You don add custom connection for Microsoft Foundry. Now, make we create Prompt flow wit dis steps. Then, you go connect dis Prompt flow to di custom connection make you fit use di fine-tuned model inside di Prompt flow.

1. Go di Microsoft Foundry project wey you create.

1. Select **Prompt flow** from di left side tab.

1. Select **+ Create** from di navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/pcm/select-promptflow.18ff2e61ab9173eb.webp)

1. Select **Chat flow** from di navigation menu.

    ![Select chat flow.](../../../../../../translated_images/pcm/select-flow-type.28375125ec9996d3.webp)

1. Enter **Folder name** wey you go use.

    ![Select chat flow.](../../../../../../translated_images/pcm/enter-name.02ddf8fb840ad430.webp)

1. Select **Create**.

#### Set up Prompt flow to chat wit your custom Phi-3 / Phi-3.5 model

You need join di fine-tuned Phi-3 / Phi-3.5 model inside Prompt flow. But di Prompt flow wey dey now no design for dis kain tin. So, you gats redo di Prompt flow to fit join di custom model.

1. For di Prompt flow, do dis tin dem to rebuild di existing flow:

    - Select **Raw file mode**.
    - Delete all di code wey dey inside *flow.dag.yml* file.
    - Add di code wey follow to *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Select **Save**.

    ![Select raw file mode.](../../../../../../translated_images/pcm/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Add dis code below to *integrate_with_promptflow.py* to use di custom Phi-3 / Phi-3.5 model inside Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Setup for logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" na di name of di Custom Connection, "endpoint", "key" na di keys inside di Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log di complete JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/pcm/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> For more detailed info on how to use Prompt flow for Microsoft Foundry, you fit check [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Select **Chat input**, **Chat output** to enable chat wit your model.

    ![Select Input Output.](../../../../../../translated_images/pcm/select-input-output.c187fc58f25fbfc3.webp)

1. Now you ready to chat wit your custom Phi-3 / Phi-3.5 model. For di next exercise, you go learn how to start Prompt flow and use am to chat wit your fine-tuned Phi-3 / Phi-3.5 model.

> [!NOTE]
>
> Di rebuilt flow suppose look like dis picture below:
>
> ![Flow example](../../../../../../translated_images/pcm/graph-example.82fd1bcdd3fc545b.webp)
>

#### Start Prompt flow

1. Select **Start compute sessions** to start Prompt flow.

    ![Start compute session.](../../../../../../translated_images/pcm/start-compute-session.9acd8cbbd2c43df1.webp)

1. Select **Validate and parse input** to refresh parameters.

    ![Validate input.](../../../../../../translated_images/pcm/validate-input.c1adb9543c6495be.webp)

1. Select di **Value** of di **connection** to di custom connection wey you create. Example be say *connection*.

    ![Connection.](../../../../../../translated_images/pcm/select-connection.1f2b59222bcaafef.webp)

#### Chat wit your custom Phi-3 / Phi-3.5 model

1. Select **Chat**.

    ![Select chat.](../../../../../../translated_images/pcm/select-chat.0406bd9687d0c49d.webp)

1. See example of results: Now you fit chat wit your custom Phi-3 / Phi-3.5 model. E good make you ask questions wey based on di data wey dem use for fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/pcm/chat-with-promptflow.1cf8cea112359ada.webp)

### Deploy Azure OpenAI to evaluate di Phi-3 / Phi-3.5 model

To evaluate di Phi-3 / Phi-3.5 model for Microsoft Foundry, you need deploy Azure OpenAI model. Dis model go help evaluate di performance of di Phi-3 / Phi-3.5 model.

#### Deploy Azure OpenAI

1. Sign in to [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Go di Microsoft Foundry project wey you create.

    ![Select Project.](../../../../../../translated_images/pcm/select-project-created.5221e0e403e2c9d6.webp)

1. For di Project wey you create, select **Deployments** from di left side tab.

1. Select **+ Deploy model** from di navigation menu.

1. Select **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/pcm/deploy-openai-model.95d812346b25834b.webp)

1. Select di Azure OpenAI model wey you like use. Example be **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/pcm/select-openai-model.959496d7e311546d.webp)

1. Select **Confirm**.

### Evaluate di fine-tuned Phi-3 / Phi-3.5 model using Microsoft Foundry's Prompt flow evaluation

### Start new evaluation

1. Visit [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Go di Microsoft Foundry project wey you create.

    ![Select Project.](../../../../../../translated_images/pcm/select-project-created.5221e0e403e2c9d6.webp)

1. For di Project wey you create, select **Evaluation** from di left side tab.

1. Select **+ New evaluation** from di navigation menu.

    ![Select evaluation.](../../../../../../translated_images/pcm/select-evaluation.2846ad7aaaca7f4f.webp)

1. Select **Prompt flow** evaluation.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/pcm/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Do dis tin dem:

    - Enter the evaluation name. E for be unique value.
    - Select **Question and answer without context** as di task type. Because, di **UlTRACHAT_200k** dataset wey you dey use for dis tutorial no get context.
    - Select di prompt flow wey you want evaluate.

    ![Prompt flow evaluation.](../../../../../../translated_images/pcm/evaluation-setting1.4aa08259ff7a536e.webp)

1. Select **Next**.

1. Do dis tin dem:

    - Select **Add your dataset** to upload di dataset. Example, you fit upload di test dataset file, like *test_data.json1*, wey dey inside di **ULTRACHAT_200k** dataset wey you download.
    - Select di correct **Dataset column** wey match your dataset. Example, if you dey use **ULTRACHAT_200k** dataset, select **${data.prompt}** as di dataset column.

    ![Prompt flow evaluation.](../../../../../../translated_images/pcm/evaluation-setting2.07036831ba58d64e.webp)

1. Select **Next**.

1. Do dis tin dem to set performance and quality metrics:

    - Select di performance and quality metrics wey you want use.
    - Select di Azure OpenAI model wey you create for evaluation. Example, select **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pcm/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Do dis tin dem to set risk and safety metrics:

    - Select di risk and safety metrics wey you want use.
    - Select di threshold to calculate di defect rate wey you want use. Example, select **Medium**.
    - For **question**, select **Data source** to **{$data.prompt}**.
    - For **answer**, select **Data source** to **{$run.outputs.answer}**.
    - For **ground_truth**, select **Data source** to **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/pcm/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Select **Next**.

1. Select **Submit** to start di evaluation.

1. Di evaluation go take some time finish. You fit dey watch how e dey go for di **Evaluation** tab.

### Review di Evaluation Results

> [!NOTE]
> Di results wey dem show here na to explain di evaluation process. For dis tutorial, we use model wey dem fine-tune for small dataset, so e fit no get better results. Real results fit change well-well depending on di size, quality, and variety of di dataset wey you use, plus how di model settings be. 

Once evaluation complete, you fit check di results for both performance and safety metrics.
1. Performance and quality metrics:

    - check how well di model dey do to generate correct, smooth, and relevant answers.

    ![Evaluation result.](../../../../../../translated_images/pcm/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Risk and safety metrics:

    - Make sure say di model output safe and e follow Responsible AI Principles, no gree make e get any wahala or bad content.

    ![Evaluation result.](../../../../../../translated_images/pcm/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. You fit scroll down make you see **Detailed metrics result**.

    ![Evaluation result.](../../../../../../translated_images/pcm/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. By checking your own custom Phi-3 / Phi-3.5 model for both performance and safety metrics, you go sure say di model no just dey work well, e still dey follow responsible AI rules, make e ready to use for real-life.

## Congratulations!

### You don finish dis tutorial

You don successfully check di fine-tuned Phi-3 model wey dem connect with Prompt flow for Microsoft Foundry. Dis one na important step to make sure say your AI models no just dey perform well, dem still dey follow Microsoft Responsible AI principles to help you build trustworthy and reliable AI apps.

![Architecture.](../../../../../../translated_images/pcm/architecture.10bec55250f5d6a4.webp)

## Clean Up Azure Resources

Clear your Azure resources so that dem no go charge you extra money. Enter Azure portal and delete these resources:

- The Azure Machine learning resource.
- The Azure Machine learning model endpoint.
- The Microsoft Foundry Project resource.
- The Microsoft Foundry Prompt flow resource.

### Next Steps

#### Documentation

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Training Content

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokument don translate use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get mistake or no too correct. The original dokument wey dey im own language na im be the correct one. For important tori, e better make person wey sabi human translate am. We no go take responsibility for any yawa or wrong understanding wey fit happen as you take use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->