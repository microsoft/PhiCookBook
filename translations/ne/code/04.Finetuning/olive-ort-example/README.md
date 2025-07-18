<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:25:27+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "ne"
}
-->
# Olive प्रयोग गरेर Phi3 लाई Fine-tune गर्ने

यस उदाहरणमा तपाईंले Olive प्रयोग गरेर:

1. LoRA एडाप्टरलाई Sad, Joy, Fear, Surprise मा वाक्यांश वर्गीकरण गर्न Fine-tune गर्ने।
1. एडाप्टरका तौलहरूलाई आधार मोडेलमा मर्ज गर्ने।
1. मोडेललाई `int4` मा अप्टिमाइज र क्वान्टाइज गर्ने।

हामीले ONNX Runtime (ORT) Generate API प्रयोग गरेर Fine-tuned मोडेल कसरी inference गर्ने पनि देखाउनेछौं।

> **⚠️ Fine-tuning को लागि, तपाईंलाई उपयुक्त GPU आवश्यक पर्छ - जस्तै A10, V100, A100।**

## 💾 इन्स्टल गर्ने

नयाँ Python भर्चुअल वातावरण बनाउनुहोस् (जस्तै `conda` प्रयोग गरेर):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

त्यसपछि, Olive र Fine-tuning workflow का लागि आवश्यक निर्भरता इन्स्टल गर्नुहोस्:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive प्रयोग गरेर Phi3 लाई Fine-tune गर्ने
[Olive कन्फिगरेसन फाइल](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) मा निम्न *workflow* र *passes* छन्:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

उच्च स्तरमा, यो workflow ले:

1. Phi3 लाई 150 स्टेप्स (तपाईंले परिवर्तन गर्न सक्नुहुन्छ) को लागि [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) डाटासँग Fine-tune गर्ने।
1. LoRA एडाप्टरका तौलहरूलाई आधार मोडेलमा मर्ज गर्ने। यसले ONNX फर्म्याटमा एकल मोडेल आर्टिफ्याक्ट दिनेछ।
1. Model Builder ले मोडेललाई ONNX runtime का लागि अप्टिमाइज गर्ने *र* मोडेललाई `int4` मा क्वान्टाइज गर्नेछ।

Workflow चलाउन:

```bash
olive run --config phrase-classification.json
```

Olive पूरा भएपछि, तपाईंको अप्टिमाइज गरिएको `int4` Fine-tuned Phi3 मोडेल यो स्थानमा उपलब्ध हुनेछ: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`।

## 🧑‍💻 Fine-tuned Phi3 लाई तपाईंको एप्लिकेशनमा समावेश गर्ने

एप्लिकेशन चलाउन:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

यो प्रतिक्रिया वाक्यांशको एकल शब्द वर्गीकरण हुनुपर्छ (Sad/Joy/Fear/Surprise)।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।