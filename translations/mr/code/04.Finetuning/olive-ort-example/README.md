<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:44:12+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "mr"
}
-->
# Olive वापरून Phi3 चे फाइन-ट्यूनिंग करा

या उदाहरणात तुम्ही Olive वापरून:

1. LoRA अ‍ॅडॉप्टर फाइन-ट्यून करून वाक्ये Sad, Joy, Fear, Surprise मध्ये वर्गीकृत कराल.
1. अ‍ॅडॉप्टरचे वजन बेस मॉडेलमध्ये मर्ज कराल.
1. मॉडेलचे ऑप्टिमायझेशन आणि क्वांटायझेशन `int4` मध्ये कराल.

आम्ही तुम्हाला ONNX Runtime (ORT) Generate API वापरून फाइन-ट्यून केलेले मॉडेल कसे इन्फरन्स करायचे तेही दाखवू.

> **⚠️ फाइन-ट्यूनिंगसाठी, तुमच्याकडे योग्य GPU असणे आवश्यक आहे - उदा. A10, V100, A100.**

## 💾 इन्स्टॉल करा

नवीन Python व्हर्च्युअल एन्व्हायर्नमेंट तयार करा (उदा. `conda` वापरून):

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
[Olive कॉन्फिगरेशन फाइल](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) मध्ये खालील *workflow* आणि *passes* आहेत:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

सामान्यतः, हा वर्कफ्लो:

1. Phi3 चे फाइन-ट्यूनिंग करेल (150 स्टेप्ससाठी, तुम्ही बदलू शकता) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) डेटा वापरून.
1. LoRA अ‍ॅडॉप्टरचे वजन बेस मॉडेलमध्ये मर्ज करेल. यामुळे ONNX फॉरमॅटमध्ये एकच मॉडेल आर्टिफॅक्ट तयार होईल.
1. Model Builder मॉडेल ONNX runtime साठी ऑप्टिमाइझ करेल *आणि* मॉडेल `int4` मध्ये क्वांटाइझ करेल.

वर्कफ्लो चालवण्यासाठी, खालील कमांड वापरा:

```bash
olive run --config phrase-classification.json
```

Olive पूर्ण झाल्यानंतर, तुमचे ऑप्टिमाइझ केलेले `int4` फाइन-ट्यून केलेले Phi3 मॉडेल येथे उपलब्ध असेल: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 फाइन-ट्यून केलेले Phi3 तुमच्या अ‍ॅप्लिकेशनमध्ये इंटीग्रेट करा

अ‍ॅप चालवण्यासाठी:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

हा प्रतिसाद वाक्याचा एक शब्द वर्गीकरण असेल (Sad/Joy/Fear/Surprise).

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेत फरक असू शकतो. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत म्हणून मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीसाठी आम्ही जबाबदार नाही.