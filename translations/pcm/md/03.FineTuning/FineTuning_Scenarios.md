## Fine Tuning Scenarios

![FineTuning with MS Services](../../../../translated_images/pcm/FinetuningwithMS.3d0cec8ae693e094.webp)

Dis section dey provide overview of fine-tuning scenarios for Microsoft Foundry and Azure environments, inside dem deployment models, infrastructure layers, and common optimization techniques wey people dey use.

**Platform**  
Dis one include managed services like Microsoft Foundry (wey dem bin dey call am Microsoft Foundry before) and Azure Machine Learning, wey dey provide model management, orchestration, experiment tracking, and deployment workflows.

**Infrastructure**  
Fine-tuning need scalable compute resources. For Azure environments, e dey normally include GPU-based virtual machines and CPU resources for light workloads, plus scalable storage for datasets and checkpoints.

**Tools & Framework**  
Fine-tuning workflows dey usually depend on frameworks and optimization libraries like Hugging Face Transformers, DeepSpeed, and PEFT (Parameter-Efficient Fine-Tuning).

The fine-tuning process with Microsoft technology cover platform services, compute infrastructure, and training frameworks. If person understand how these parts dey work together, developers fit take correct way adapt foundation models for specific tasks and production scenarios.

## Model as Service

Fine-tune the model with hosted fine-tuning, without the need to create and manage compute.

![MaaS Fine Tuning](../../../../translated_images/pcm/MaaSfinetune.3eee4630607aff0d.webp)

Serverless fine-tuning don dey available now for Phi-3, Phi-3.5, and Phi-4 model families, wey go allow developers quickly and easily customize the models for cloud and edge scenarios without the need to arrange compute.

## Model as a Platform 

Users dey manage their own compute so dem fit Fine-tune their models.

![Maap Fine Tuning](../../../../translated_images/pcm/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Fine-Tuning Techniques Comparison

|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Adapting pre-trained LLMs to specific tasks or domains|Yes|Yes|Yes|Yes|Yes|Yes|
|Fine-tuning for NLP tasks such as text classification, named entity recognition, and machine translation|Yes|Yes|Yes|Yes|Yes|Yes|
|Fine-tuning for QA tasks|Yes|Yes|Yes|Yes|Yes|Yes|
|Fine-tuning for generating human-like responses in chatbots|Yes|Yes|Yes|Yes|Yes|Yes|
|Fine-tuning for generating music, art, or other forms of creativity|Yes|Yes|Yes|Yes|Yes|Yes|
|Reducing computational and financial costs|Yes|Yes|Yes|Yes|Yes|Yes|
|Reducing memory usage|Yes|Yes|Yes|Yes|Yes|Yes|
|Using fewer parameters for efficient finetuning|Yes|Yes|Yes|No|No|Yes|
|Memory-efficient form of data parallelism that gives access to the aggregate GPU memory of all the GPU devices available|No|No|No|Yes|Yes|No|

> [!NOTE]
> LoRA, QLoRA, PEFT, and DoRA na parameter-efficient fine-tuning methods, but DeepSpeed and ZeRO dey focus on distributed training and memory optimization.

## Fine Tuning Performance Examples

![Finetuning Performance](../../../../translated_images/pcm/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get errors or mistakes. Di original document for e own language na di correct one. For important information, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong meaning wey fit show because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->