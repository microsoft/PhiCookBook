# Fine-tuning Phi-3 wit Microsoft Foundry

 Make we explore how to fine-tune Microsoft Phi-3 Mini language model using Microsoft Foundry. Fine-tuning dey allow you to adapt Phi-3 Mini to specific tasks, make am even more powerful and sabi context.

## Considerations

- **Capabilities:** Which models fit fine tune? Wetin the base model fit fine tune to do?
- **Cost:** How dem dey charge for fine tuning
**Customizability:** How much I fit modify the base model – and how I fit take do am?
- **Convenience:** How fine tuning really dey happen – I suppose write custom code? I suppose bring my own compute?
- **Safety:** Fine tuned models dey get safety wahala – any guards for place to protect against accidental harm?

![AIFoundry Models](../../../../translated_images/pcm/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Preparation for fine-tuning

### Prerequisites

> [!NOTE]
> For Phi-3 family models, pay-as-you-go fine-tune dey only available if your hubs dey **East US 2** regions.

- Azure subscription. If you no get Azure subscription, create [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) to start.

- [AI Foundry project](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure role-based access controls (Azure RBAC) dey grant access for Microsoft Foundry operations. To do these steps for this article, your user account must get __Azure AI Developer role__ for the resource group.

### Subscription provider registration

Make sure say subscription dey registered to `Microsoft.Network` resource provider.

1. Sign in to [Azure portal](https://portal.azure.com).
1. Choose **Subscriptions** from left menu.
1. Choose the subscription wey you wan use.
1. Choose **AI project settings** > **Resource providers** from left menu.
1. Confirm say **Microsoft.Network** dey the list of resource providers. If no, add am.

### Data preparation

Prepare your training and validation data wey you go use fine-tune your model. Your training and validation data dey consist of input and output examples of how you want model to perform.

Make sure all your training examples follow the format wey dem expect for inference. To fine-tune model well, get balanced and different kind data.

This one mean sey you go maintain data balance, include different situations, and dey always improve training data to match real-life expectations, so model go dey more correct and balanced.

Different model types need different training data format.

### Chat Completion

The training and validation data wey you use **supposed** to be JSON Lines (JSONL) document. For `Phi-3-mini-128k-instruct` fine-tuning dataset suppose dey conversational format wey Chat completions API dey use.

### Example file format

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

The kind file wey e support na JSON Lines. Files go upload go default datastore and e go available for your project.

## Fine-Tuning Phi-3 wit Microsoft Foundry

Microsoft Foundry dey let you customize large language models to your own datasets by doing fine-tuning. Fine-tuning dey add value by allowing customization and optimization for specific tasks and apps. E dey make performance better, cost cheaper, response time short, and output fit your needs.

![Finetune AI Foundry](../../../../translated_images/pcm/AIFoundryfinetune.193aaddce48d553c.webp)

### Create New Project

1. Sign in to [Microsoft Foundry](https://ai.azure.com).

1. Click **+New project** to create new project for Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/pcm/select-new-project.cd31c0404088d7a3.webp)

1. Do these things:

    - Project **Hub name**. E must be unique.
    - Choose **Hub** to use (if no, create new one).

    ![FineTuneSelect](../../../../translated_images/pcm/create-project.ca3b71298b90e420.webp)

1. Do these to create new hub:

    - Put **Hub name**. E must be unique.
    - Choose your Azure **Subscription**.
    - Choose **Resource group** to use (or create new one).
    - Choose the **Location** you want use.
    - Choose **Connect Azure AI Services** (or create new one).
    - Choose **Connect Azure AI Search** and select **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/pcm/create-hub.49e53d235e80779e.webp)

1. Click **Next**.
1. Click **Create a project**.

### Data Preparation

Before fine-tuning, gather or build dataset wey relate to your task, like chat instructions, question-answer pairs, or other related text data. Clean and prepare am by removing noise, fixing missing values, and tokenizing the text.

### Fine-tune Phi-3 models for Microsoft Foundry

> [!NOTE]
> Fine-tuning Phi-3 models dey supported only for projects wey dey East US 2.

1. Click **Model catalog** from the left tab.

1. Type *phi-3* for **search bar** and choose the phi-3 model wey you want use.

    ![FineTuneSelect](../../../../translated_images/pcm/select-model.60ef2d4a6a3cec57.webp)

1. Click **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/pcm/select-finetune.a976213b543dd9d8.webp)

1. Put the **Fine-tuned model name**.

    ![FineTuneSelect](../../../../translated_images/pcm/finetune1.c2b39463f0d34148.webp)

1. Click **Next**.

1. Do these:

    - Choose **task type** to **Chat completion**.
    - Choose **Training data** you wan use. You fit upload am from Microsoft Foundry data or from your local machine.

    ![FineTuneSelect](../../../../translated_images/pcm/finetune2.43cb099b1a94442d.webp)

1. Click **Next**.

1. Upload **Validation data** you want, or choose **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/pcm/finetune3.fd96121b67dcdd92.webp)

1. Click **Next**.

1. Do these:

    - Choose **Batch size multiplier** you want.
    - Choose **Learning rate** you want.
    - Choose **Epochs** you want.

    ![FineTuneSelect](../../../../translated_images/pcm/finetune4.e18b80ffccb5834a.webp)

1. Click **Submit** to start fine-tuning.

    ![FineTuneSelect](../../../../translated_images/pcm/select-submit.0a3802d581bac271.webp)


1. When your model don finish fine-tune, e go show status as **Completed** like for image below. Now you fit deploy am and use am for your app, play ground, or prompt flow. For more info, check [How to deploy Phi-3 family of small language models with Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/pcm/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> For full info on fine-tuning Phi-3, make you visit [Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Cleaning up your fine-tuned models

You fit delete fine-tuned model from fine-tuning model list for [Microsoft Foundry](https://ai.azure.com) or from model details page. Choose the fine-tuned model wey you want delete for Fine-tuning page, then click Delete button to remove am.

> [!NOTE]
> You no fit delete custom model wey get deployment. You must first delete your model deployment before you fit delete custom model.

## Cost and quotas

### Cost and quota considerations for Phi-3 models fine-tuned as a service

Phi models fine-tuned as service na Microsoft dey provide, and dem dey integrate am with Microsoft Foundry for use. You fit see pricing when [deploying](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) or fine-tuning models under Pricing and terms tab for deployment wizard.

## Content filtering

Models wey deploy as service pay-as-you-go, dem protected by Azure AI Content Safety. When you deploy am to real-time endpoints, you fit choose to opt out. If Azure AI content safety dey enabled, both prompt and completion go pass classification models weh dey detect and stop harmful content. The content filtering system dey detect and act on particular kinds of harmful content for both input prompts and output completions. Learn more about [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Fine-Tuning Configuration**

Hyperparameters: Define hyperparameters like learning rate, batch size, and number of training epochs.

**Loss Function**

Choose the correct loss function for your task (e.g., cross-entropy).

**Optimizer**

Select optimizer (e.g., Adam) to update gradient during training.

**Fine-Tuning Process**

- Load Pre-Trained Model: Load Phi-3 Mini checkpoint.
- Add Custom Layers: Add layers specific for task (e.g., classification head for chat instructions).

**Train the Model**
Fine-tune model using your prepared dataset. Monitor training progress and adjust hyperparameters if needed.

**Evaluation and Validation**

Validation Set: Split your data into training and validation sets.

**Evaluate Performance**

Use metrics like accuracy, F1-score, or perplexity to check model performance.

## Save Fine-Tuned Model

**Checkpoint**
Save the fine-tuned model checkpoint so you fit use am later.

## Deployment

- Deploy as Web Service: Deploy your fine-tuned model as web service for Microsoft Foundry.
- Test the Endpoint: Send test queries to the deployed endpoint to check how e work.

## Iterate and Improve

Iterate: If performance no good, keep adjusting hyperparameters, add more data, or fine-tune for more epochs.

## Monitor and Refine

Always monitor the model behavior and refine if e necessary.

## Customize and Extend

Custom Tasks: Phi-3 Mini fit fine-tune for different tasks outside chat instructions. Try other use cases!
Experiment: Test different architectures, layer combinations, and techniques to boost performance.

> [!NOTE]
> Fine-tuning na iterative process. Try, learn, and adjust your model to get the best result for your specific task!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automated translation fit get some errors or wrong tins. Di original dokument for dia own language na di correct source. For important mata, na professional human translation dem suppose use. We no responsible for any confusion or wrong understanding wey fit happen from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->