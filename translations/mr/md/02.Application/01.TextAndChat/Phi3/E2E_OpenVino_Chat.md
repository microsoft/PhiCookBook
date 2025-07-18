<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:03:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "mr"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

हा कोड OpenVINO फॉरमॅटमध्ये मॉडेल निर्यात करतो, ते लोड करतो आणि दिलेल्या प्रॉम्प्टवर प्रतिसाद तयार करण्यासाठी वापरतो.

1. **मॉडेल निर्यात करणे**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - हा कमांड `optimum-cli` टूल वापरून मॉडेल OpenVINO फॉरमॅटमध्ये निर्यात करतो, जे कार्यक्षम इन्फरन्ससाठी ऑप्टिमाइझ केलेले आहे.
   - निर्यात होणारे मॉडेल `"microsoft/Phi-3-mini-4k-instruct"` आहे, जे मागील संदर्भावर आधारित मजकूर तयार करण्याच्या कामासाठी सेट केलेले आहे.
   - मॉडेलचे वेट्स 4-बिट इंटिजर (`int4`) मध्ये क्वांटाइज केलेले आहेत, ज्यामुळे मॉडेलचा आकार कमी होतो आणि प्रक्रिया जलद होते.
   - `group-size`, `ratio`, आणि `sym` सारखे इतर पॅरामीटर्स क्वांटायझेशन प्रक्रियेला अधिक बारीकसारीक करण्यासाठी वापरले जातात.
   - निर्यात केलेले मॉडेल `./model/phi3-instruct/int4` या फोल्डरमध्ये जतन केले जाते.

2. **आवश्यक लायब्ररी आयात करणे**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - या ओळी `transformers` लायब्ररी आणि `optimum.intel.openvino` मॉड्यूलमधील क्लासेस आयात करतात, जे मॉडेल लोड आणि वापरण्यासाठी आवश्यक आहेत.

3. **मॉडेल डायरेक्टरी आणि कॉन्फिगरेशन सेट करणे**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` मध्ये मॉडेल फाइल्स कुठे आहेत ते दिलेले आहे.
   - `ov_config` हा एक डिक्शनरी आहे जो OpenVINO मॉडेलसाठी कमी विलंबता, एकच इन्फरन्स स्ट्रीम वापरणे आणि कॅशे डायरेक्टरी न वापरणे यासाठी कॉन्फिगर करतो.

4. **मॉडेल लोड करणे**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - ही ओळ दिलेल्या डायरेक्टरीमधून मॉडेल लोड करते, आधी सेट केलेल्या कॉन्फिगरेशनसह. आवश्यक असल्यास रिमोट कोड एक्सिक्युशनसाठी परवानगी देखील देते.

5. **टोकनायझर लोड करणे**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - ही ओळ टोकनायझर लोड करते, जो मजकूर टोकन्समध्ये रूपांतरित करण्यासाठी जबाबदार आहे जे मॉडेल समजू शकते.

6. **टोकनायझरचे पॅरामीटर्स सेट करणे**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - हा डिक्शनरी टोकनायझेशन आउटपुटमध्ये विशेष टोकन्स जोडू नयेत हे निर्दिष्ट करतो.

7. **प्रॉम्प्ट परिभाषित करणे**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - हा स्ट्रिंग एक संभाषण प्रॉम्प्ट सेट करतो जिथे वापरकर्ता AI सहाय्यकाला स्वतःची ओळख करून देण्यास सांगतो.

8. **प्रॉम्प्ट टोकनायझ करणे**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - ही ओळ प्रॉम्प्टला टोकन्समध्ये रूपांतरित करते जे मॉडेल प्रक्रिया करू शकते, आणि परिणाम PyTorch टेन्सर स्वरूपात परत करते.

9. **प्रतिसाद तयार करणे**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - ही ओळ इनपुट टोकन्सवर आधारित प्रतिसाद तयार करण्यासाठी मॉडेल वापरते, जास्तीत जास्त 1024 नवीन टोकन्सपर्यंत.

10. **प्रतिसाद डीकोड करणे**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - ही ओळ तयार केलेले टोकन्स परत मानवी वाचनीय मजकूरात रूपांतरित करते, कोणतेही विशेष टोकन्स वगळून, आणि पहिला निकाल परत आणते.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.