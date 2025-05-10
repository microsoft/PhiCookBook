<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:09:00+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "ne"
}
-->
# Evaluate the Fine-tuned Phi-3 / Phi-3.5 Model in Azure AI Foundry Focusing on Microsoft's Responsible AI Principles

This end-to-end (E2E) sample is based on the guide "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" from the Microsoft Tech Community.

## Overview

### How can you evaluate the safety and performance of a fine-tuned Phi-3 / Phi-3.5 model in Azure AI Foundry?

Fine-tuning a model can sometimes cause unintended or unwanted responses. To make sure the model stays safe and effective, it’s important to assess its potential to produce harmful content and its ability to give accurate, relevant, and coherent answers. In this tutorial, you’ll learn how to evaluate the safety and performance of a fine-tuned Phi-3 / Phi-3.5 model integrated with Prompt flow in Azure AI Foundry.

Here is the evaluation process in Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.ne.png)

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

To ensure your AI model is ethical and safe, it’s essential to evaluate it against Microsoft's Responsible AI Principles. In Azure AI Foundry, safety evaluations let you check your model’s vulnerability to jailbreak attacks and its potential to produce harmful content, which aligns directly with these principles.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.ne.png)

*Image Source: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft’s Responsible AI Principles

Before diving into the technical steps, it’s important to understand Microsoft’s Responsible AI Principles, an ethical framework that guides the responsible development, deployment, and operation of AI systems. These principles ensure AI technologies are designed fairly, transparently, and inclusively. They form the basis for evaluating AI model safety.

Microsoft's Responsible AI Principles include:

- **Fairness and Inclusiveness**: AI systems should treat everyone fairly and avoid treating similar groups differently. For example, when AI systems provide advice on medical treatment, loan applications, or hiring, they should give consistent recommendations to people with similar symptoms, financial situations, or qualifications.

- **Reliability and Safety**: To build trust, AI systems must operate reliably, safely, and consistently. They should work as intended, handle unexpected situations safely, and resist harmful manipulation. Their behavior should reflect the range of conditions anticipated by developers during design and testing.

- **Transparency**: When AI systems help make decisions that significantly impact people’s lives, it’s crucial that people understand how those decisions were made. For example, a bank might use AI to decide creditworthiness or a company to select job candidates.

- **Privacy and Security**: As AI use grows, protecting privacy and securing personal and business data becomes increasingly important and complex. AI systems require careful handling of privacy and data security because they rely on data to make accurate and informed predictions.

- **Accountability**: Designers and deployers of AI systems must be accountable for how their systems perform. Organizations should follow industry standards to establish accountability norms, ensuring AI isn’t the final authority on decisions affecting people’s lives and that humans maintain meaningful control over highly autonomous AI systems.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.ne.png)

*Image Source: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> To learn more about Microsoft's Responsible AI Principles, visit the [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Safety metrics

In this tutorial, you will evaluate the safety of the fine-tuned Phi-3 model using Azure AI Foundry's safety metrics. These metrics help you assess the model’s potential to produce harmful content and its vulnerability to jailbreak attacks. The safety metrics include:

- **Self-harm-related Content**: Checks if the model tends to generate content related to self-harm.
- **Hateful and Unfair Content**: Checks if the model tends to generate hateful or unfair content.
- **Violent Content**: Checks if the model tends to generate violent content.
- **Sexual Content**: Checks if the model tends to generate inappropriate sexual content.

Evaluating these ensures the AI model avoids harmful or offensive content, aligning it with societal values and regulations.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.ne.png)

### Introduction to performance evaluation

To confirm your AI model performs as expected, it’s important to evaluate its effectiveness using performance metrics. In Azure AI Foundry, performance evaluations let you measure how well your model generates accurate, relevant, and coherent responses.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.ne.png)

*Image Source: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Performance metrics

In this tutorial, you will evaluate the performance of the fine-tuned Phi-3 / Phi-3.5 model using Azure AI Foundry's performance metrics. These metrics help you assess how well the model generates accurate, relevant, and coherent responses. The performance metrics include:

- **Groundedness**: Measures how well the generated answers align with the input source information.
- **Relevance**: Measures how pertinent the generated responses are to the questions asked.
- **Coherence**: Measures how smoothly the text flows, how natural it reads, and how human-like the language sounds.
- **Fluency**: Measures the language proficiency of the generated text.
- **GPT Similarity**: Compares the generated response with the ground truth to assess similarity.
- **F1 Score**: Calculates the ratio of shared words between the generated response and the source data.

These metrics help you evaluate how effectively the model produces accurate, relevant, and coherent answers.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.ne.png)

## **Scenario 2: Evaluating the Phi-3 / Phi-3.5 model in Azure AI Foundry**

### Before you begin

This tutorial follows the previous blog posts, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" and "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In those posts, we covered fine-tuning a Phi-3 / Phi-3.5 model in Azure AI Foundry and integrating it with Prompt flow.

In this tutorial, you will deploy an Azure OpenAI model as an evaluator in Azure AI Foundry and use it to evaluate your fine-tuned Phi-3 / Phi-3.5 model.

Before starting, ensure you have these prerequisites as described earlier:

1. A prepared dataset to evaluate the fine-tuned Phi-3 / Phi-3.5 model.
1. A Phi-3 / Phi-3.5 model that’s been fine-tuned and deployed to Azure Machine Learning.
1. A Prompt flow integrated with your fine-tuned Phi-3 / Phi-3.5 model in Azure AI Foundry.

> [!NOTE]
> You will use the *test_data.jsonl* file from the data folder of the **ULTRACHAT_200k** dataset downloaded in the previous blog posts as the dataset for evaluation.

#### Integrate the custom Phi-3 / Phi-3.5 model with Prompt flow in Azure AI Foundry (Code first approach)

> [!NOTE]
> If you followed the low-code approach described in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", you can skip this exercise and move on.
> However, if you followed the code-first approach described in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" to fine-tune and deploy your Phi-3 / Phi-3.5 model, the process of connecting your model to Prompt flow is slightly different. You will learn this process here.

To continue, you need to integrate your fine-tuned Phi-3 / Phi-3.5 model into Prompt flow in Azure AI Foundry.

#### Create Azure AI Foundry Hub

You need to create a Hub before creating a Project. A Hub works like a Resource Group, letting you organize and manage multiple Projects within Azure AI Foundry.

1. Sign in to [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Select **All hubs** from the left side menu.

1. Click **+ New hub** in the navigation bar.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.ne.png)

1. Complete the following:

    - Enter a **Hub name** (must be unique).
    - Select your Azure **Subscription**.
    - Select the **Resource group** to use (or create a new one).
    - Select the **Location** you want.
    - Select **Connect Azure AI Services** (or create a new one).
    - For **Connect Azure AI Search**, choose **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.ne.png)

1. **Next** चयन गर्नुहोस्।

#### Azure AI Foundry परियोजना सिर्जना गर्नुहोस्

1. तपाईंले सिर्जना गरेको Hub मा, बायाँपट्टि ट्याबबाट **All projects** चयन गर्नुहोस्।

1. नेभिगेशन मेनुबाट **+ New project** चयन गर्नुहोस्।

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.ne.png)

1. **Project name** प्रविष्ट गर्नुहोस्। यो एक अनौठो मान हुनुपर्छ।

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.ne.png)

1. **Create a project** चयन गर्नुहोस्।

#### fine-tuned Phi-3 / Phi-3.5 मोडेलको लागि कस्टम कनेक्शन थप्नुहोस्

तपाईंको कस्टम Phi-3 / Phi-3.5 मोडेललाई Prompt flow सँग एकीकृत गर्न, मोडेलको endpoint र key कस्टम कनेक्शनमा सुरक्षित गर्नु आवश्यक छ। यसले Prompt flow मा तपाईंको कस्टम मोडेल पहुँच सुनिश्चित गर्दछ।

#### fine-tuned Phi-3 / Phi-3.5 मोडेलको api key र endpoint uri सेट गर्नुहोस्

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) मा जानुहोस्।

1. तपाईंले सिर्जना गरेको Azure Machine learning workspace मा जानुहोस्।

1. बायाँपट्टि ट्याबबाट **Endpoints** चयन गर्नुहोस्।

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.ne.png)

1. तपाईंले सिर्जना गरेको endpoint चयन गर्नुहोस्।

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.ne.png)

1. नेभिगेशन मेनुबाट **Consume** चयन गर्नुहोस्।

1. तपाईंको **REST endpoint** र **Primary key** कपी गर्नुहोस्।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.ne.png)

#### कस्टम कनेक्शन थप्नुहोस्

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) मा जानुहोस्।

1. तपाईंले सिर्जना गरेको Azure AI Foundry परियोजनामा जानुहोस्।

1. तपाईंले सिर्जना गरेको परियोजनामा, बायाँपट्टि ट्याबबाट **Settings** चयन गर्नुहोस्।

1. **+ New connection** चयन गर्नुहोस्।

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.ne.png)

1. नेभिगेशन मेनुबाट **Custom keys** चयन गर्नुहोस्।

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.ne.png)

1. तलका कार्यहरू गर्नुहोस्:

    - **+ Add key value pairs** चयन गर्नुहोस्।
    - key नामको लागि **endpoint** लेख्नुहोस् र Azure ML Studio बाट कपी गरेको endpoint मान value क्षेत्रमा टाँस्नुहोस्।
    - फेरि **+ Add key value pairs** चयन गर्नुहोस्।
    - key नामको लागि **key** लेख्नुहोस् र Azure ML Studio बाट कपी गरेको key मान value क्षेत्रमा टाँस्नुहोस्।
    - key हरू थपिसकेपछि, key लाई खुल्ला हुनबाट रोक्न **is secret** चयन गर्नुहोस्।

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.ne.png)

1. **Add connection** चयन गर्नुहोस्।

#### Prompt flow सिर्जना गर्नुहोस्

तपाईंले Azure AI Foundry मा कस्टम कनेक्शन थप्नुभएको छ। अब तलका चरणहरू प्रयोग गरी Prompt flow सिर्जना गरौं। त्यसपछि, यो Prompt flow लाई कस्टम कनेक्शनसँग जोडेर fine-tuned मोडेल प्रयोग गर्न सकिनेछ।

1. तपाईंले सिर्जना गरेको Azure AI Foundry परियोजनामा जानुहोस्।

1. बायाँपट्टि ट्याबबाट **Prompt flow** चयन गर्नुहोस्।

1. नेभिगेशन मेनुबाट **+ Create** चयन गर्नुहोस्।

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.ne.png)

1. नेभिगेशन मेनुबाट **Chat flow** चयन गर्नुहोस्।

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.ne.png)

1. प्रयोग गर्न चाहेको **Folder name** प्रविष्ट गर्नुहोस्।

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.ne.png)

1. **Create** चयन गर्नुहोस्।

#### तपाईंको कस्टम Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्न Prompt flow सेट अप गर्नुहोस्

तपाईंले fine-tuned Phi-3 / Phi-3.5 मोडेललाई Prompt flow मा समावेश गर्न आवश्यक छ। तर, उपलब्ध Prompt flow यसका लागि डिजाइन गरिएको छैन। त्यसैले, तपाईंले Prompt flow पुनः डिजाइन गर्नुपर्नेछ जसले कस्टम मोडेललाई एकीकृत गर्न सक्षम बनाउँछ।

1. Prompt flow मा, तलका कार्यहरू गरेर हालको flow पुनर्निर्माण गर्नुहोस्:

    - **Raw file mode** चयन गर्नुहोस्।
    - *flow.dag.yml* फाइलमा रहेका सबै कोड मेटाउनुहोस्।
    - *flow.dag.yml* मा तलको कोड थप्नुहोस्।

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

    - **Save** चयन गर्नुहोस्।

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.ne.png)

1. *integrate_with_promptflow.py* मा तलको कोड थप्नुहोस् ताकि Prompt flow मा कस्टम Phi-3 / Phi-3.5 मोडेल प्रयोग गर्न सकियोस्।

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.ne.png)

> [!NOTE]
> Azure AI Foundry मा Prompt flow प्रयोग सम्बन्धी थप विस्तृत जानकारीको लागि, [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) हेर्न सक्नुहुन्छ।

1. तपाईंको मोडेलसँग कुराकानी सक्षम गर्न **Chat input**, **Chat output** चयन गर्नुहोस्।

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.ne.png)

1. अब तपाईंको कस्टम Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्न तयार हुनुहुन्छ। अर्को अभ्यासमा, तपाईंले कसरी Prompt flow सुरु गर्ने र यसलाई fine-tuned मोडेलसँग कुराकानी गर्न प्रयोग गर्ने सिक्नु हुनेछ।

> [!NOTE]
>
> पुनर्निर्मित flow तलको चित्र जस्तै देखिनु पर्छ:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.ne.png)
>

#### Prompt flow सुरु गर्नुहोस्

1. Prompt flow सुरु गर्न **Start compute sessions** चयन गर्नुहोस्।

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.ne.png)

1. प्यारामिटरहरू नवीकरण गर्न **Validate and parse input** चयन गर्नुहोस्।

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.ne.png)

1. तपाईंले सिर्जना गरेको कस्टम कनेक्शनको **connection** मान चयन गर्नुहोस्। उदाहरणका लागि, *connection*।

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.ne.png)

#### तपाईंको कस्टम Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्नुहोस्

1. **Chat** चयन गर्नुहोस्।

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.ne.png)

1. यहाँ नतिजाको उदाहरण छ: अब तपाईं आफ्नो कस्टम Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्न सक्नुहुन्छ। fine-tuning मा प्रयोग भएको डाटामा आधारित प्रश्न सोध्न सिफारिस गरिन्छ।

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.ne.png)

### Phi-3 / Phi-3.5 मोडेलको मूल्याङ्कन गर्न Azure OpenAI डिप्लोय गर्नुहोस्

Azure AI Foundry मा Phi-3 / Phi-3.5 मोडेल मूल्याङ्कन गर्न, Azure OpenAI मोडेल डिप्लोय गर्नु आवश्यक छ। यो मोडेल Phi-3 / Phi-3.5 मोडेलको प्रदर्शन मूल्याङ्कन गर्न प्रयोग गरिनेछ।

#### Azure OpenAI डिप्लोय गर्नुहोस्

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) मा साइन इन गर्नुहोस्।

1. तपाईंले सिर्जना गरेको Azure AI Foundry परियोजनामा जानुहोस्।

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.ne.png)

1. तपाईंले सिर्जना गरेको परियोजनामा, बायाँपट्टि ट्याबबाट **Deployments** चयन गर्नुहोस्।

1. नेभिगेशन मेनुबाट **+ Deploy model** चयन गर्नुहोस्।

1. **Deploy base model** चयन गर्नुहोस्।

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.ne.png)

1. प्रयोग गर्न चाहेको Azure OpenAI मोडेल चयन गर्नुहोस्। उदाहरणका लागि, **gpt-4o**।

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.ne.png)

1. **Confirm** चयन गर्नुहोस्।

### Azure AI Foundry को Prompt flow मूल्याङ्कन प्रयोग गरी fine-tuned Phi-3 / Phi-3.5 मोडेल मूल्याङ्कन गर्नुहोस्

### नयाँ मूल्याङ्कन सुरु गर्नुहोस्

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) मा जानुहोस्।

1. तपाईंले सिर्जना गरेको Azure AI Foundry परियोजनामा जानुहोस्।

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.ne.png)

1. तपाईंले सिर्जना गरेको परियोजनामा, बायाँपट्टि ट्याबबाट **Evaluation** चयन गर्नुहोस्।

1. नेभिगेशन मेनुबाट **+ New evaluation** चयन गर्नुहोस्।
![Select evaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.ne.png)

1. **Prompt flow** मूल्याङ्कन चयन गर्नुहोस्।

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.ne.png)

1. तलका कार्यहरू गर्नुहोस्:

    - मूल्याङ्कन नाम प्रविष्ट गर्नुहोस्। यो अनौठो मान हुनुपर्छ।
    - कार्य प्रकारको रूपमा **Question and answer without context** चयन गर्नुहोस्। किनभने यस ट्युटोरियलमा प्रयोग गरिएको **UlTRACHAT_200k** डेटासेटमा सन्दर्भ समावेश छैन।
    - तपाईंले मूल्याङ्कन गर्न चाहनुभएको prompt flow चयन गर्नुहोस्।

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.ne.png)

1. **Next** चयन गर्नुहोस्।

1. तलका कार्यहरू गर्नुहोस्:

    - डेटासेट अपलोड गर्न **Add your dataset** चयन गर्नुहोस्। उदाहरणका लागि, तपाईंले **ULTRACHAT_200k** डेटासेट डाउनलोड गर्दा समावेश गरिएको *test_data.json1* जस्तो टेस्ट डेटासेट फाइल अपलोड गर्न सक्नुहुन्छ।
    - तपाईंको डेटासेटसँग मेल खाने उपयुक्त **Dataset column** चयन गर्नुहोस्। उदाहरणका लागि, यदि तपाईं **ULTRACHAT_200k** डेटासेट प्रयोग गर्दै हुनुहुन्छ भने, **${data.prompt}** लाई dataset column को रूपमा चयन गर्नुहोस्।

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.ne.png)

1. **Next** चयन गर्नुहोस्।

1. प्रदर्शन र गुणस्तर मेट्रिक्स कन्फिगर गर्न तलका कार्यहरू गर्नुहोस्:

    - तपाईंले प्रयोग गर्न चाहनुभएको प्रदर्शन र गुणस्तर मेट्रिक्स चयन गर्नुहोस्।
    - मूल्याङ्कनको लागि तपाईंले सिर्जना गरेको Azure OpenAI मोडल चयन गर्नुहोस्। उदाहरणका लागि, **gpt-4o** चयन गर्नुहोस्।

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.ne.png)

1. जोखिम र सुरक्षा मेट्रिक्स कन्फिगर गर्न तलका कार्यहरू गर्नुहोस्:

    - तपाईंले प्रयोग गर्न चाहनुभएको जोखिम र सुरक्षा मेट्रिक्स चयन गर्नुहोस्।
    - दोष दर गणना गर्न चाहनुभएको थ्रेसहोल्ड चयन गर्नुहोस्। उदाहरणका लागि, **Medium** चयन गर्नुहोस्।
    - **question** को लागि, **Data source** लाई **{$data.prompt}** मा सेट गर्नुहोस्।
    - **answer** को लागि, **Data source** लाई **{$run.outputs.answer}** मा सेट गर्नुहोस्।
    - **ground_truth** को लागि, **Data source** लाई **{$data.message}** मा सेट गर्नुहोस्।

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.ne.png)

1. **Next** चयन गर्नुहोस्।

1. मूल्याङ्कन सुरु गर्न **Submit** चयन गर्नुहोस्।

1. मूल्याङ्कन पूरा हुन केही समय लाग्नेछ। तपाईं प्रगतिको निगरानी **Evaluation** ट्याबमा गर्न सक्नुहुन्छ।

### मूल्याङ्कन परिणामहरू समीक्षा गर्नुहोस्

> [!NOTE]
> तल प्रस्तुत परिणामहरू मूल्याङ्कन प्रक्रिया देखाउनका लागि हुन्। यस ट्युटोरियलमा, हामीले सानो डेटासेटमा फाइन-ट्युन गरिएको मोडल प्रयोग गरेका छौं, जसले उपयुक्त नतिजा नआउन सक्छ। वास्तविक नतिजा डेटासेटको आकार, गुणस्तर, विविधता र मोडलको विशेष कन्फिगरेसन अनुसार धेरै फरक हुन सक्छ।

मूल्याङ्कन पूरा भएपछि, तपाईं प्रदर्शन र सुरक्षा मेट्रिक्स दुवैका परिणामहरू समीक्षा गर्न सक्नुहुन्छ।

1. प्रदर्शन र गुणस्तर मेट्रिक्स:

    - मोडलले सुसंगत, प्रवाहमय, र सान्दर्भिक प्रतिक्रियाहरू उत्पादन गर्न कत्तिको प्रभावकारी छ भन्ने मूल्याङ्कन गर्नुहोस्।

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.ne.png)

1. जोखिम र सुरक्षा मेट्रिक्स:

    - मोडलका आउटपुटहरू सुरक्षित छन् र Responsible AI Principles अनुसार छन् कि छैनन्, कुनै हानिकारक वा आपत्तिजनक सामग्री छैन भनेर सुनिश्चित गर्नुहोस्।

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.ne.png)

1. तपाईं तल स्क्रोल गरेर **Detailed metrics result** हेर्न सक्नुहुन्छ।

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.ne.png)

1. तपाईंले आफ्नै Phi-3 / Phi-3.5 मोडललाई प्रदर्शन र सुरक्षा मेट्रिक्स दुवैसँग मूल्याङ्कन गरेर पुष्टि गर्न सक्नुहुन्छ कि मोडल प्रभावकारी मात्र होइन, जिम्मेवार AI अभ्यासहरूमा पनि आधारित छ, जसले यसलाई वास्तविक संसारमा प्रयोगको लागि तयार बनाउँछ।

## बधाई छ!

### तपाईंले यो ट्युटोरियल पूरा गर्नुभयो

तपाईंले सफलतापूर्वक Azure AI Foundry मा Prompt flow सँग एकीकृत फाइन-ट्युन गरिएको Phi-3 मोडलको मूल्याङ्कन गर्नुभयो। यो कदमले तपाईंका AI मोडलहरू राम्रो प्रदर्शन मात्र होइन, Microsoft का Responsible AI सिद्धान्तहरूमा आधारित भएर विश्वसनीय र भरपर्दो AI एप्लिकेसनहरू विकास गर्न मद्दत गर्दछ।

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.ne.png)

## Azure स्रोतहरू सफा गर्नुहोस्

तपाईंको खातामा अतिरिक्त शुल्क लाग्न नदिन Azure स्रोतहरू सफा गर्नुहोस्। Azure पोर्टलमा जानुहोस् र तलका स्रोतहरू मेटाउनुहोस्:

- Azure Machine learning स्रोत।
- Azure Machine learning मोडल एन्डपोइन्ट।
- Azure AI Foundry Project स्रोत।
- Azure AI Foundry Prompt flow स्रोत।

### अर्को कदमहरू

#### दस्तावेजीकरण

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### तालिम सामग्री

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### सन्दर्भ

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत भए तापनि, कृपया जान्नुहोस् कि स्वचालित अनुवादमा त्रुटि वा गलतफहमी हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।