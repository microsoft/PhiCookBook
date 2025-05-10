<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:44:21+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "ne"
}
-->
# Phi3 लाई Olive प्रयोग गरेर Fine-tune गर्ने

यस उदाहरणमा तपाईं Olive प्रयोग गरेर:

1. LoRA adapter लाई fine-tune गरेर वाक्यांशहरूलाई Sad, Joy, Fear, Surprise मा वर्गीकरण गर्ने।
1. Adapter का weights लाई base model मा merge गर्ने।
1. Model लाई optimize र quantize गरेर `int4` मा परिणत गर्ने।

हामीले fine-tuned model लाई ONNX Runtime (ORT) Generate API प्रयोग गरी कसरी inference गर्ने पनि देखाउनेछौं।

> **⚠️ Fine-tuning गर्नका लागि उपयुक्त GPU आवश्यक छ - जस्तै, A10, V100, A100।**

## 💾 Install

नयाँ Python virtual environment बनाउनुहोस् (उदाहरणका लागि `conda` प्रयोग गरेर):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

पछि, Olive र fine-tuning workflow का लागि आवश्यक dependencies install गर्नुहोस्:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive प्रयोग गरेर Phi3 लाई Fine-tune गर्ने
[Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) मा निम्न *workflow* र *passes* छन्:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

सारांशमा, यो workflow ले:

1. Phi3 लाई fine-tune गर्ने (150 steps का लागि, तपाईंले परिवर्तन गर्न सक्नुहुन्छ) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) डाटाको प्रयोग गरी।
1. LoRA adapter weights लाई base model मा merge गर्ने। यसले ONNX format मा एकल model artifact दिनेछ।
1. Model Builder ले model लाई ONNX runtime का लागि optimize गर्ने *र* model लाई `int4` मा quantize गर्नेछ।

Workflow चलाउनका लागि:

```bash
olive run --config phrase-classification.json
```

Olive सकिएपछि, तपाईंको optimized `int4` fine-tuned Phi3 model यो ठेगानामा उपलब्ध हुनेछ: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`।

## 🧑‍💻 Fine-tuned Phi3 लाई तपाईंको application मा integrate गर्ने

App चलाउनका लागि:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

यसले वाक्यांशको एक शब्द classification दिनेछ (Sad/Joy/Fear/Surprise)।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सटीकता सुनिश्चित गर्न प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्यामा हामी जिम्मेवार छैनौं।