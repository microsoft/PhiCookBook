<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:02:45+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "ne"
}
-->
# Olive प्रयोग गरेर Phi3 लाई Fine-tune गर्ने

यस उदाहरणमा तपाईंले Olive प्रयोग गरेर:

1. LoRA adapter लाई fine-tune गरेर वाक्यांशहरूलाई Sad, Joy, Fear, Surprise मा वर्गीकरण गर्ने।
1. Adapter को weights लाई base model मा merge गर्ने।
1. मोडेललाई `int4` मा optimize र quantize गर्ने।

हामीले ONNX Runtime (ORT) Generate API प्रयोग गरेर fine-tuned मोडेल कसरी inference गर्ने पनि देखाउनेछौं।

> **⚠️ Fine-tuning को लागि, तपाईंलाई उपयुक्त GPU आवश्यक पर्छ - जस्तै A10, V100, A100।**

## 💾 स्थापना

नयाँ Python virtual environment बनाउनुहोस् (जस्तै `conda` प्रयोग गरेर):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

त्यसपछि, Olive र fine-tuning workflow का लागि आवश्यक dependencies स्थापना गर्नुहोस्:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive प्रयोग गरेर Phi3 लाई Fine-tune गर्ने
[Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) मा निम्न *workflow* र *passes* छन्:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

उच्च स्तरमा, यो workflow ले:

1. Phi3 लाई fine-tune गर्नेछ (150 steps का लागि, जुन तपाईंले परिवर्तन गर्न सक्नुहुन्छ) [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) डाटाको प्रयोग गरेर।
1. LoRA adapter weights लाई base model मा merge गर्नेछ। यसले तपाईंलाई ONNX format मा एकल मोडेल artifact दिनेछ।
1. Model Builder ले मोडेललाई ONNX runtime का लागि optimize गर्नेछ र मोडेललाई `int4` मा quantize गर्नेछ।

Workflow चलाउन, यो कमाण्ड चलाउनुहोस्:

```bash
olive run --config phrase-classification.json
```

जब Olive पूरा हुन्छ, तपाईंको optimized `int4` fine-tuned Phi3 मोडेल यो स्थानमा उपलब्ध हुनेछ: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`।

## 🧑‍💻 Fine-tuned Phi3 लाई तपाईंको एप्लिकेशनमा समावेश गर्ने

एप्लिकेशन चलाउन:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

यो प्रतिक्रिया वाक्यांशको एकल शब्द वर्गीकरण हुनुपर्छ (Sad/Joy/Fear/Surprise)।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भने पनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।