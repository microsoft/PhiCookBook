<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:08:29+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "en"
}
-->
# Evaluate the Fine-tuned Phi-3 / Phi-3.5 Model in Azure AI Foundry Focusing on Microsoft's Responsible AI Principles

This end-to-end (E2E) sample is based on the guide "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" from the Microsoft Tech Community.

## Overview

### How can you evaluate the safety and performance of a fine-tuned Phi-3 / Phi-3.5 model in Azure AI Foundry?

Fine-tuning a model can sometimes lead to unintended or undesired responses. To ensure that the model remains safe and effective, it's important to evaluate its potential to generate harmful content and its ability to produce accurate, relevant, and coherent responses. In this tutorial, you will learn how to evaluate the safety and performance of a fine-tuned Phi-3 / Phi-3.5 model integrated with Prompt flow in Azure AI Foundry.

Here is Azure AI Foundry's evaluation process.

![Architecture of tutorial.](../../../../../../translated_images/en/architecture.10bec55250f5d6a4.webp)

*Image Source: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> For more detailed information and to explore additional resources about Phi-3 / Phi-3.5, please visit the [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prerequisites

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 model

### Table of Contents

1. [**Scenario 1: Introduction to Azure AI Foundry's Prompt flow evaluation**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduction to safety evaluation](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduction to performance evaluation](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Evaluating the Phi-3 / Phi-3.5 model in Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Before you begin](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Deploy Azure OpenAI to evaluate the Phi-3 / Phi-3.5 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluate the fine-tuned Phi-3 / Phi-3.5 model using Azure AI Foundry's Prompt flow evaluation](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Congratulations!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introduction to Azure AI Foundry's Prompt flow evaluation**

### Introduction to safety evaluation

To ensure that your AI model is ethical and safe, it's crucial to evaluate it against Microsoft's Responsible AI Principles. In Azure AI Foundry, safety evaluations allow you to assess your model’s vulnerability to jailbreak attacks and its potential to generate harmful content, which aligns directly with these principles.

![Safety evaluation.](../../../../../../translated_images/en/safety-evaluation.083586ec88dfa950.webp)

*Image Source: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft’s Responsible AI Principles

Before starting the technical steps, it's important to understand Microsoft's Responsible AI Principles, an ethical framework designed to guide the responsible development, deployment, and operation of AI systems. These principles ensure AI technologies are built fairly, transparently, and inclusively. They form the foundation for evaluating AI model safety.

Microsoft's Responsible AI Principles include:

- **Fairness and Inclusiveness**: AI systems should treat everyone fairly and avoid treating similar groups differently. For example, when AI systems provide guidance on medical treatment, loan applications, or employment, they should make consistent recommendations for people with similar symptoms, financial situations, or qualifications.

- **Reliability and Safety**: To build trust, AI systems must operate reliably, safely, and consistently. They should function as designed, respond safely to unexpected situations, and resist harmful manipulation. Their behavior and the range of conditions they handle reflect the scenarios developers anticipated during design and testing.

- **Transparency**: When AI systems influence decisions with significant impacts on people’s lives, it’s essential that people understand how those decisions were made. For example, a bank might use AI to decide creditworthiness, or a company might use AI to select the most qualified job candidates.

- **Privacy and Security**: As AI becomes more widespread, protecting privacy and securing personal and business data becomes increasingly important and complex. AI requires careful attention to privacy and data security because access to data is essential for making accurate and informed predictions and decisions.

- **Accountability**: Those who design and deploy AI systems must be accountable for how their systems operate. Organizations should follow industry standards to establish accountability norms. These norms ensure AI systems are not the final authority on decisions affecting people’s lives and that humans maintain meaningful control over highly autonomous AI systems.

![Fill hub.](../../../../../../translated_images/en/responsibleai2.c07ef430113fad8c.webp)

*Image Source: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> To learn more about Microsoft's Responsible AI Principles, visit [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Safety metrics

In this tutorial, you will evaluate the safety of the fine-tuned Phi-3 model using Azure AI Foundry's safety metrics. These metrics help assess the model's potential to generate harmful content and its vulnerability to jailbreak attacks. The safety metrics include:

- **Self-harm-related Content**: Checks if the model tends to produce content related to self-harm.
- **Hateful and Unfair Content**: Checks if the model tends to produce hateful or unfair content.
- **Violent Content**: Checks if the model tends to produce violent content.
- **Sexual Content**: Checks if the model tends to produce inappropriate sexual content.

Evaluating these aspects ensures the AI model does not generate harmful or offensive content, aligning it with societal values and regulatory standards.

![Evaluate based on safety.](../../../../../../translated_images/en/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introduction to performance evaluation

To ensure your AI model performs as expected, it’s important to evaluate it against performance metrics. In Azure AI Foundry, performance evaluations help you assess your model’s effectiveness in generating accurate, relevant, and coherent responses.

![Safety evaluation.](../../../../../../translated_images/en/performance-evaluation.48b3e7e01a098740.webp)

*Image Source: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Performance metrics

In this tutorial, you will evaluate the performance of the fine-tuned Phi-3 / Phi-3.5 model using Azure AI Foundry's performance metrics. These metrics help assess the model’s ability to generate accurate, relevant, and coherent responses. The performance metrics include:

- **Groundedness**: Measures how well the generated answers align with the input source information.
- **Relevance**: Measures how pertinent the generated responses are to the questions asked.
- **Coherence**: Measures how smoothly the generated text flows, reads naturally, and resembles human language.
- **Fluency**: Measures the language proficiency of the generated text.
- **GPT Similarity**: Compares the generated response with the ground truth for similarity.
- **F1 Score**: Calculates the overlap ratio of words between the generated response and the source data.

These metrics help evaluate the model’s effectiveness in producing accurate, relevant, and coherent responses.

![Evaluate based on performance.](../../../../../../translated_images/en/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenario 2: Evaluating the Phi-3 / Phi-3.5 model in Azure AI Foundry**

### Before you begin

This tutorial follows the previous blog posts, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" and "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In those posts, we walked through fine-tuning a Phi-3 / Phi-3.5 model in Azure AI Foundry and integrating it with Prompt flow.

In this tutorial, you will deploy an Azure OpenAI model as an evaluator in Azure AI Foundry and use it to evaluate your fine-tuned Phi-3 / Phi-3.5 model.

Before starting, ensure you have the following prerequisites, as described in the previous tutorials:

1. A prepared dataset to evaluate the fine-tuned Phi-3 / Phi-3.5 model.
1. A Phi-3 / Phi-3.5 model that has been fine-tuned and deployed to Azure Machine Learning.
1. A Prompt flow integrated with your fine-tuned Phi-3 / Phi-3.5 model in Azure AI Foundry.

> [!NOTE]
> You will use the *test_data.jsonl* file, located in the data folder from the **ULTRACHAT_200k** dataset downloaded in the previous blog posts, as the dataset to evaluate the fine-tuned Phi-3 / Phi-3.5 model.

#### Integrate the custom Phi-3 / Phi-3.5 model with Prompt flow in Azure AI Foundry (Code first approach)
> [!NOTE]  
> If you followed the low-code approach described in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", you can skip this exercise and move on to the next one.  
> However, if you used the code-first approach outlined in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" to fine-tune and deploy your Phi-3 / Phi-3.5 model, the process for connecting your model to Prompt Flow is a bit different. You will learn how to do this in this exercise.
To proceed, you need to integrate your fine-tuned Phi-3 / Phi-3.5 model into Prompt flow in Azure AI Foundry.

#### Create Azure AI Foundry Hub

You need to create a Hub before creating the Project. A Hub functions like a Resource Group, allowing you to organize and manage multiple Projects within Azure AI Foundry.

1. Sign in to [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Select **All hubs** from the left side tab.

1. Select **+ New hub** from the navigation menu.

    ![Create hub.](../../../../../../translated_images/en/create-hub.5be78fb1e21ffbf1.webp)

1. Complete the following:

    - Enter a **Hub name**. It must be unique.
    - Select your Azure **Subscription**.
    - Choose the **Resource group** to use (create a new one if needed).
    - Select the **Location** you want to use.
    - Select the **Connect Azure AI Services** to use (create a new one if needed).
    - For **Connect Azure AI Search**, choose **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/en/fill-hub.baaa108495c71e34.webp)

1. Select **Next**.

#### Create Azure AI Foundry Project

1. In the Hub you created, select **All projects** from the left side tab.

1. Select **+ New project** from the navigation menu.

    ![Select new project.](../../../../../../translated_images/en/select-new-project.cd31c0404088d7a3.webp)

1. Enter a **Project name**. It must be unique.

    ![Create project.](../../../../../../translated_images/en/create-project.ca3b71298b90e420.webp)

1. Select **Create a project**.

#### Add a custom connection for the fine-tuned Phi-3 / Phi-3.5 model

To integrate your custom Phi-3 / Phi-3.5 model with Prompt flow, you need to save the model's endpoint and key in a custom connection. This setup ensures access to your custom Phi-3 / Phi-3.5 model in Prompt flow.

#### Set API key and endpoint URI of the fine-tuned Phi-3 / Phi-3.5 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigate to the Azure Machine Learning workspace you created.

1. Select **Endpoints** from the left side tab.

    ![Select endpoints.](../../../../../../translated_images/en/select-endpoints.ee7387ecd68bd18d.webp)

1. Select the endpoint you created.

    ![Select endpoints.](../../../../../../translated_images/en/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Select **Consume** from the navigation menu.

1. Copy your **REST endpoint** and **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/en/copy-endpoint-key.0650c3786bd646ab.webp)

#### Add the Custom Connection

1. Visit [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigate to the Azure AI Foundry project you created.

1. In the Project, select **Settings** from the left side tab.

1. Select **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/en/select-new-connection.fa0f35743758a74b.webp)

1. Select **Custom keys** from the navigation menu.

    ![Select custom keys.](../../../../../../translated_images/en/select-custom-keys.5a3c6b25580a9b67.webp)

1. Complete the following:

    - Select **+ Add key value pairs**.
    - For the key name, enter **endpoint** and paste the endpoint you copied from Azure ML Studio into the value field.
    - Select **+ Add key value pairs** again.
    - For the key name, enter **key** and paste the key you copied from Azure ML Studio into the value field.
    - After adding the keys, select **is secret** to keep the key hidden.

    ![Add connection.](../../../../../../translated_images/en/add-connection.ac7f5faf8b10b0df.webp)

1. Select **Add connection**.

#### Create Prompt flow

You have added a custom connection in Azure AI Foundry. Now, let's create a Prompt flow using the following steps. Then, you will connect this Prompt flow to the custom connection to use the fine-tuned model within the Prompt flow.

1. Navigate to the Azure AI Foundry project you created.

1. Select **Prompt flow** from the left side tab.

1. Select **+ Create** from the navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/en/select-promptflow.18ff2e61ab9173eb.webp)

1. Select **Chat flow** from the navigation menu.

    ![Select chat flow.](../../../../../../translated_images/en/select-flow-type.28375125ec9996d3.webp)

1. Enter a **Folder name** to use.

    ![Select chat flow.](../../../../../../translated_images/en/enter-name.02ddf8fb840ad430.webp)

1. Select **Create**.

#### Set up Prompt flow to chat with your custom Phi-3 / Phi-3.5 model

You need to integrate the fine-tuned Phi-3 / Phi-3.5 model into a Prompt flow. However, the existing Prompt flow provided is not designed for this purpose. Therefore, you must redesign the Prompt flow to enable integration of the custom model.

1. In the Prompt flow, rebuild the existing flow by doing the following:

    - Select **Raw file mode**.
    - Delete all existing code in the *flow.dag.yml* file.
    - Add the following code to *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/en/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Add the following code to *integrate_with_promptflow.py* to use the custom Phi-3 / Phi-3.5 model in Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/en/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> For more detailed information on using Prompt flow in Azure AI Foundry, see [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Select **Chat input** and **Chat output** to enable chatting with your model.

    ![Select Input Output.](../../../../../../translated_images/en/select-input-output.c187fc58f25fbfc3.webp)

1. Now you are ready to chat with your custom Phi-3 / Phi-3.5 model. In the next exercise, you will learn how to start Prompt flow and use it to chat with your fine-tuned Phi-3 / Phi-3.5 model.

> [!NOTE]
>
> The rebuilt flow should look like the image below:
>
> ![Flow example](../../../../../../translated_images/en/graph-example.82fd1bcdd3fc545b.webp)
>

#### Start Prompt flow

1. Select **Start compute sessions** to start Prompt flow.

    ![Start compute session.](../../../../../../translated_images/en/start-compute-session.9acd8cbbd2c43df1.webp)

1. Select **Validate and parse input** to refresh parameters.

    ![Validate input.](../../../../../../translated_images/en/validate-input.c1adb9543c6495be.webp)

1. Select the **Value** of the **connection** to the custom connection you created. For example, *connection*.

    ![Connection.](../../../../../../translated_images/en/select-connection.1f2b59222bcaafef.webp)

#### Chat with your custom Phi-3 / Phi-3.5 model

1. Select **Chat**.

    ![Select chat.](../../../../../../translated_images/en/select-chat.0406bd9687d0c49d.webp)

1. Here’s an example of the results: Now you can chat with your custom Phi-3 / Phi-3.5 model. It’s recommended to ask questions based on the data used for fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/en/chat-with-promptflow.1cf8cea112359ada.webp)

### Deploy Azure OpenAI to evaluate the Phi-3 / Phi-3.5 model

To evaluate the Phi-3 / Phi-3.5 model in Azure AI Foundry, you need to deploy an Azure OpenAI model. This model will be used to assess the performance of the Phi-3 / Phi-3.5 model.

#### Deploy Azure OpenAI

1. Sign in to [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigate to the Azure AI Foundry project you created.

    ![Select Project.](../../../../../../translated_images/en/select-project-created.5221e0e403e2c9d6.webp)

1. In the Project, select **Deployments** from the left side tab.

1. Select **+ Deploy model** from the navigation menu.

1. Select **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/en/deploy-openai-model.95d812346b25834b.webp)

1. Select the Azure OpenAI model you want to use. For example, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/en/select-openai-model.959496d7e311546d.webp)

1. Select **Confirm**.

### Evaluate the fine-tuned Phi-3 / Phi-3.5 model using Azure AI Foundry's Prompt flow evaluation

### Start a new evaluation

1. Visit [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigate to the Azure AI Foundry project you created.

    ![Select Project.](../../../../../../translated_images/en/select-project-created.5221e0e403e2c9d6.webp)

1. In the Project, select **Evaluation** from the left side tab.

1. Select **+ New evaluation** from the navigation menu.

    ![Select evaluation.](../../../../../../translated_images/en/select-evaluation.2846ad7aaaca7f4f.webp)

1. Select **Prompt flow** evaluation.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/en/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Complete the following:

    - Enter an evaluation name. It must be unique.
    - Select **Question and answer without context** as the task type, since the **ULTRACHAT_200k** dataset used in this tutorial does not include context.
    - Select the prompt flow you want to evaluate.

    ![Prompt flow evaluation.](../../../../../../translated_images/en/evaluation-setting1.4aa08259ff7a536e.webp)

1. Select **Next**.

1. Complete the following:

    - Select **Add your dataset** to upload the dataset. For example, upload the test dataset file like *test_data.json1*, included with the **ULTRACHAT_200k** dataset.
    - Choose the appropriate **Dataset column** that matches your dataset. For example, if using the **ULTRACHAT_200k** dataset, select **${data.prompt}** as the dataset column.

    ![Prompt flow evaluation.](../../../../../../translated_images/en/evaluation-setting2.07036831ba58d64e.webp)

1. Select **Next**.

1. Configure the performance and quality metrics:

    - Select the performance and quality metrics you want to use.
    - Select the Azure OpenAI model you created for evaluation. For example, **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/en/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Configure the risk and safety metrics:

    - Select the risk and safety metrics you want to use.
    - Choose the threshold for calculating the defect rate. For example, select **Medium**.
    - For **question**, set **Data source** to **{$data.prompt}**.
    - For **answer**, set **Data source** to **{$run.outputs.answer}**.
    - For **ground_truth**, set **Data source** to **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/en/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Select **Next**.

1. Select **Submit** to start the evaluation.

1. The evaluation will take some time to complete. You can monitor progress in the **Evaluation** tab.

### Review the Evaluation Results
> [!NOTE]
> The results shown below are meant to demonstrate the evaluation process. In this tutorial, we used a model fine-tuned on a relatively small dataset, which might result in less than optimal outcomes. Actual results can vary greatly depending on the size, quality, and diversity of the dataset, as well as the specific model configuration.
Once the evaluation is complete, you can review the results for both performance and safety metrics.

1. Performance and quality metrics:

    - Assess the model’s ability to generate coherent, fluent, and relevant responses.

    ![Evaluation result.](../../../../../../translated_images/en/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Risk and safety metrics:

    - Verify that the model’s outputs are safe and comply with Responsible AI Principles, avoiding any harmful or offensive content.

    ![Evaluation result.](../../../../../../translated_images/en/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. You can scroll down to see the **Detailed metrics result**.

    ![Evaluation result.](../../../../../../translated_images/en/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. By evaluating your custom Phi-3 / Phi-3.5 model on both performance and safety metrics, you can ensure the model is not only effective but also follows responsible AI practices, making it ready for real-world use.

## Congratulations!

### You’ve completed this tutorial

You have successfully evaluated the fine-tuned Phi-3 model integrated with Prompt flow in Azure AI Foundry. This is a crucial step to ensure your AI models not only perform well but also align with Microsoft’s Responsible AI principles, helping you build trustworthy and reliable AI applications.

![Architecture.](../../../../../../translated_images/en/architecture.10bec55250f5d6a4.webp)

## Clean Up Azure Resources

Clean up your Azure resources to avoid extra charges on your account. Go to the Azure portal and delete the following resources:

- The Azure Machine Learning resource.
- The Azure Machine Learning model endpoint.
- The Azure AI Foundry Project resource.
- The Azure AI Foundry Prompt flow resource.

### Next Steps

#### Documentation

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Training Content

- [Introduction to Microsoft’s Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.