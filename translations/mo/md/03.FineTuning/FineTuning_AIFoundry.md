<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-05-07T13:12:42+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "mo"
}
-->
# Fine-tuning Phi-3 with Azure AI Foundry

Let’s explore how to fine-tune Microsoft’s Phi-3 Mini language model using Azure AI Foundry. Fine-tuning lets you adapt Phi-3 Mini to specific tasks, making it even more powerful and context-aware.

## Considerations

- **Capabilities:** Which models can be fine-tuned? What can the base model be fine-tuned to do?
- **Cost:** What’s the pricing model for fine-tuning?
- **Customizability:** How much can I modify the base model – and in what ways?
- **Convenience:** How does fine-tuning actually work – do I need to write custom code? Do I need to provide my own compute?
- **Safety:** Fine-tuned models can have safety risks – are there any guardrails to prevent unintended harm?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.0e1b16f7d0b09b73e15278aa4351740ed2076b3bdde88c48e6839f8f8cf640c7.mo.png)

## Preparation for fine-tuning

### Prerequisites

> [!NOTE]
> For Phi-3 family models, the pay-as-you-go fine-tune option is only available with hubs created in **East US 2** regions.

- An Azure subscription. If you don’t have one, create a [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) to get started.

- An [AI Foundry project](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure AI Foundry. Your user account must have the __Azure AI Developer role__ assigned on the resource group to perform the steps in this article.

### Subscription provider registration

Make sure your subscription is registered with the `Microsoft.Network` resource provider.

1. Sign in to the [Azure portal](https://portal.azure.com).
1. Select **Subscriptions** from the left menu.
1. Choose the subscription you want to use.
1. Select **AI project settings** > **Resource providers** from the left menu.
1. Confirm that **Microsoft.Network** is listed as a resource provider. If not, add it.

### Data preparation

Prepare your training and validation data to fine-tune your model. These datasets should include input-output examples demonstrating how you want the model to perform.

Ensure all training examples follow the expected format for inference. To fine-tune models effectively, use a balanced and diverse dataset.

This means maintaining data balance, covering various scenarios, and periodically refining training data to reflect real-world expectations. This leads to more accurate and well-rounded model responses.

Different model types require different formats for training data.

### Chat Completion

Training and validation data **must** be formatted as a JSON Lines (JSONL) document. For `Phi-3-mini-128k-instruct`, the fine-tuning dataset must follow the conversational format used by the Chat completions API.

### Example file format

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

The supported file type is JSON Lines. Files are uploaded to the default datastore and made available in your project.

## Fine-Tuning Phi-3 with Azure AI Foundry

Azure AI Foundry allows you to customize large language models to your own datasets through fine-tuning. This process adds value by enabling customization and optimization for specific tasks and applications. Benefits include improved performance, cost efficiency, lower latency, and tailored outputs.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.193aaddce48d553ce078eabed1526dfa300ae7fac7840e10b38fb50ea86b436c.mo.png)

### Create a New Project

1. Sign in to [Azure AI Foundry](https://ai.azure.com).

1. Click **+New project** to create a new project.

    ![FineTuneSelect](../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.mo.png)

1. Complete the following:

    - Enter a unique **Hub name**.
    - Select the **Hub** to use (or create a new one if needed).

    ![FineTuneSelect](../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.mo.png)

1. To create a new hub, do the following:

    - Enter a unique **Hub name**.
    - Select your Azure **Subscription**.
    - Choose the **Resource group** (or create a new one if needed).
    - Select the **Location**.
    - Select **Connect Azure AI Services** (or create a new one if needed).
    - For **Connect Azure AI Search**, choose **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/create-hub.49e53d235e80779e95293c08654daf213e003b942a2fa81045b994c088acad7f.mo.png)

1. Click **Next**.
1. Click **Create a project**.

### Data Preparation

Before fine-tuning, gather or create a dataset relevant to your task, such as chat instructions, question-answer pairs, or other related text data. Clean and preprocess the data by removing noise, handling missing values, and tokenizing the text.

### Fine-tune Phi-3 models in Azure AI Foundry

> [!NOTE]
> Fine-tuning of Phi-3 models is currently supported only in projects located in East US 2.

1. Select **Model catalog** from the left side menu.

1. Search for *phi-3* in the **search bar** and select the Phi-3 model you want to use.

    ![FineTuneSelect](../../../../translated_images/select-model.60ef2d4a6a3cec57c3c45a8404613f25f8ad41534a209a88f5549e95d21320f8.mo.png)

1. Click **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.a976213b543dd9d8d621e322d186ff670c3fb92bbba8435e6bcd4e79b9aab251.mo.png)

1. Enter the **Fine-tuned model name**.

    ![FineTuneSelect](../../../../translated_images/finetune1.c2b39463f0d34148be1473af400e30e936c425f1cb8d5dbefcf9454008923402.mo.png)

1. Click **Next**.

1. Complete the following:

    - Select **task type** as **Chat completion**.
    - Upload your **Training data** either via Azure AI Foundry’s data storage or from your local environment.

    ![FineTuneSelect](../../../../translated_images/finetune2.43cb099b1a94442df8f77c70e22fce46849329882a9e278ab1d87df196a63c4c.mo.png)

1. Click **Next**.

1. Upload your **Validation data** or choose **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/finetune3.fd96121b67dcdd928568f64970980db22685ef54a4e48d1cc8d139c1ecb8c99f.mo.png)

1. Click **Next**.

1. Configure the following:

    - Choose the **Batch size multiplier**.
    - Set the **Learning rate**.
    - Specify the number of **Epochs**.

    ![FineTuneSelect](../../../../translated_images/finetune4.e18b80ffccb5834a2690f855223a6e007bd8ca771663f7b0f5dbefb3c47850c3.mo.png)

1. Click **Submit** to start fine-tuning.

    ![FineTuneSelect](../../../../translated_images/select-submit.0a3802d581bac27168ae1a8667026ad7f6c5f9188615113968272dbe1f7f774d.mo.png)

1. After fine-tuning completes, the status will show as **Completed**, as in the image below. You can then deploy the model and use it in your application, playground, or prompt flow. For more details, see [How to deploy Phi-3 family of small language models with Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.4dc8d2357144cdef5ba7303f42e9f1fca2baa37049bcededb5392d51cb21cc03.mo.png)

> [!NOTE]
> For more detailed information on fine-tuning Phi-3, visit [Fine-tune Phi-3 models in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Cleaning up your fine-tuned models

You can delete a fine-tuned model from the fine-tuning model list in [Azure AI Foundry](https://ai.azure.com) or from the model details page. Select the fine-tuned model you want to delete on the Fine-tuning page, then click the Delete button.

> [!NOTE]
> You cannot delete a custom model if it has an active deployment. You must first delete the deployment before deleting the custom model.

## Cost and quotas

### Cost and quota considerations for Phi-3 models fine-tuned as a service

Phi models fine-tuned as a service are offered by Microsoft and integrated with Azure AI Foundry. Pricing details can be found during [deployment](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) or fine-tuning under the Pricing and terms tab in the deployment wizard.

## Content filtering

Models deployed as pay-as-you-go services are protected by Azure AI Content Safety. When deployed to real-time endpoints, you can opt out of this feature. With content safety enabled, both prompts and completions pass through multiple classification models designed to detect and block harmful content. The system identifies and acts on specific categories of potentially harmful content in both input and output. Learn more about [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Fine-Tuning Configuration**

Set hyperparameters such as learning rate, batch size, and number of training epochs.

**Loss Function**

Choose a suitable loss function for your task (e.g., cross-entropy).

**Optimizer**

Select an optimizer (e.g., Adam) to update gradients during training.

**Fine-Tuning Process**

- Load Pre-Trained Model: Load the Phi-3 Mini checkpoint.
- Add Custom Layers: Include task-specific layers (e.g., classification head for chat instructions).

**Train the Model**

Fine-tune the model with your prepared dataset. Monitor training progress and adjust hyperparameters as needed.

**Evaluation and Validation**

Split your data into training and validation sets.

**Evaluate Performance**

Use metrics like accuracy, F1-score, or perplexity to measure performance.

## Save Fine-Tuned Model

**Checkpoint**

Save the fine-tuned model checkpoint for future use.

## Deployment

- Deploy as a Web Service: Deploy your fine-tuned model as a web service in Azure AI Foundry.
- Test the Endpoint: Send test queries to verify functionality.

## Iterate and Improve

If results aren’t satisfactory, iterate by adjusting hyperparameters, adding more data, or fine-tuning for more epochs.

## Monitor and Refine

Continuously monitor model behavior and refine as needed.

## Customize and Extend

Fine-tune Phi-3 Mini for tasks beyond chat instructions. Explore new use cases!

Experiment with different architectures, layer combinations, and techniques to boost performance.

> [!NOTE]
> Fine-tuning is an iterative process. Experiment, learn, and adapt your model to get the best results for your specific task!

**Disclaimer**:  
Dis dokumento ha bin translaited yusando AI translait servis [Co-op Translator](https://github.com/Azure/co-op-translator). Dile we strav fo akyurasí, plis be awér dat otoméitid translaitions me kontéin érors or inakíurasis. Di orijinal dokumento in its neitiv langwidz shud bi konsiderd di otoritatív sors. Fo kritikál informéishon, profesionál human translait is rekoménded. Wi ar not laiyabl fo eni misandérstandings or misinterpretéishons arising from di yus of dis translaiton.