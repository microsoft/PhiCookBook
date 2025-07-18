<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:25:18+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "mr"
}
-->
# Olive वापरून Phi3 चे फाइन-ट्यूनिंग करा

या उदाहरणात तुम्ही Olive वापरून:

1. LoRA अ‍ॅडॉप्टर फाइन-ट्यून करून वाक्यांशांना Sad, Joy, Fear, Surprise मध्ये वर्गीकृत कराल.
1. अ‍ॅडॉप्टरचे वजन बेस मॉडेलमध्ये मर्ज कराल.
1. मॉडेलचे ऑप्टिमायझेशन आणि Quantize करून `int4` मध्ये रूपांतर कराल.

आम्ही तुम्हाला ONNX Runtime (ORT) Generate API वापरून फाइन-ट्यून केलेले मॉडेल कसे इन्फर करायचे तेही दाखवू.

> **⚠️ फाइन-ट्यूनिंगसाठी, तुमच्याकडे योग्य GPU असणे आवश्यक आहे - उदाहरणार्थ, A10, V100, A100.**

## 💾 इन्स्टॉल करा

नवीन Python व्हर्च्युअल एन्व्हायर्नमेंट तयार करा (उदाहरणार्थ, `conda` वापरून):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

नंतर, Olive आणि फाइन-ट्यूनिंग वर्कफ्लो साठी आवश्यक dependencies इन्स्टॉल करा:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive वापरून Phi3 चे फाइन-ट्यूनिंग करा
[Olive कॉन्फिगरेशन फाइल](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) मध्ये खालील *वर्कफ्लो* आणि *पास* आहेत:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

सारांशात, हा वर्कफ्लो:

1. Phi3 चे फाइन-ट्यूनिंग करेल (150 स्टेप्ससाठी, जे तुम्ही बदलू शकता) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) डेटाचा वापर करून.
1. LoRA अ‍ॅडॉप्टरचे वजन बेस मॉडेलमध्ये मर्ज करेल. त्यामुळे ONNX फॉरमॅटमध्ये एकच मॉडेल तयार होईल.
1. Model Builder मॉडेलला ONNX runtime साठी ऑप्टिमाइझ करेल आणि `int4` मध्ये Quantize करेल.

वर्कफ्लो चालवण्यासाठी, खालील कमांड वापरा:

```bash
olive run --config phrase-classification.json
```

Olive पूर्ण झाल्यावर, तुमचे ऑप्टिमाइझ्ड `int4` फाइन-ट्यून केलेले Phi3 मॉडेल येथे उपलब्ध असेल: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 फाइन-ट्यून केलेले Phi3 तुमच्या अ‍ॅप्लिकेशनमध्ये इंटिग्रेट करा

अ‍ॅप चालवण्यासाठी:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

या प्रतिसादात वाक्यांशाचा एकच शब्द वर्गीकरण असावा (Sad/Joy/Fear/Surprise).

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.