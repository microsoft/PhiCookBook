<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:31:11+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "mr"
}
-->
# Olive वापरून Phi3 चे फाइन-ट्यूनिंग करा

या उदाहरणात तुम्ही Olive वापरून:

1. LoRA अ‍ॅडॉप्टर फाइन-ट्यून करून वाक्यांशांना Sad, Joy, Fear, Surprise मध्ये वर्गीकृत कराल.
1. अ‍ॅडॉप्टरचे वजन बेस मॉडेलमध्ये मर्ज कराल.
1. मॉडेलचे ऑप्टिमायझेशन आणि Quantize करून `int4` मध्ये रूपांतर कराल.

आम्ही तुम्हाला ONNX Runtime (ORT) Generate API वापरून फाइन-ट्यून केलेले मॉडेल कसे इन्फरन्स करायचे ते देखील दाखवू.

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
[Olive कॉन्फिगरेशन फाइल](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) मध्ये खालील *workflow* आणि *passes* आहेत:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

साधारणपणे, हा वर्कफ्लो:

1. Phi3 ला 150 स्टेप्ससाठी (तुम्ही बदलू शकता) [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) डेटा वापरून फाइन-ट्यून करेल.
1. LoRA अ‍ॅडॉप्टरचे वजन बेस मॉडेलमध्ये मर्ज करेल. त्यामुळे तुम्हाला ONNX फॉरमॅटमधील एकच मॉडेल आर्टिफॅक्ट मिळेल.
1. Model Builder मॉडेलला ONNX runtime साठी ऑप्टिमाइझ करेल आणि मॉडेलला `int4` मध्ये quantize करेल.

वर्कफ्लो चालवण्यासाठी, खालील कमांड वापरा:

```bash
olive run --config phrase-classification.json
```

Olive पूर्ण झाल्यानंतर, तुमचे ऑप्टिमाइझ्ड `int4` फाइन-ट्यून केलेले Phi3 मॉडेल येथे उपलब्ध असेल: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 फाइन-ट्यून केलेले Phi3 तुमच्या अ‍ॅप्लिकेशनमध्ये इंटिग्रेट करा

अ‍ॅप चालवण्यासाठी:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

हा प्रतिसाद वाक्यांशाचा एकच शब्द वर्गीकरण असावा (Sad/Joy/Fear/Surprise).

**सूचना**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, परंतु कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत म्हणून विचारात घ्यावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.