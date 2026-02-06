[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

यह कोड एक मॉडल को OpenVINO फॉर्मेट में एक्सपोर्ट करता है, उसे लोड करता है, और दिए गए प्रॉम्प्ट के आधार पर प्रतिक्रिया उत्पन्न करने के लिए उपयोग करता है।

1. **मॉडल का एक्सपोर्ट करना**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - यह कमांड `optimum-cli` टूल का उपयोग करके मॉडल को OpenVINO फॉर्मेट में एक्सपोर्ट करता है, जो कुशल इनफेरेंस के लिए अनुकूलित है।
   - एक्सपोर्ट किया जा रहा मॉडल `"microsoft/Phi-3-mini-4k-instruct"` है, और इसे पिछले संदर्भ के आधार पर टेक्स्ट जनरेट करने के कार्य के लिए सेट किया गया है।
   - मॉडल के वेट्स को 4-बिट इंटीजर (`int4`) में क्वांटाइज़ किया गया है, जिससे मॉडल का आकार कम होता है और प्रोसेसिंग तेज़ होती है।
   - `group-size`, `ratio`, और `sym` जैसे अन्य पैरामीटर क्वांटाइज़ेशन प्रक्रिया को बेहतर बनाने के लिए उपयोग किए जाते हैं।
   - एक्सपोर्ट किया गया मॉडल `./model/phi3-instruct/int4` डायरेक्टरी में सेव किया जाता है।

2. **आवश्यक लाइब्रेरी इम्पोर्ट करना**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - ये लाइनें `transformers` लाइब्रेरी और `optimum.intel.openvino` मॉड्यूल से क्लासेस इम्पोर्ट करती हैं, जो मॉडल को लोड और उपयोग करने के लिए जरूरी हैं।

3. **मॉडल डायरेक्टरी और कॉन्फ़िगरेशन सेट करना**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` यह बताता है कि मॉडल फाइलें कहाँ स्टोर हैं।
   - `ov_config` एक डिक्शनरी है जो OpenVINO मॉडल को कम विलंबता (low latency) प्राथमिकता देने, एक इनफेरेंस स्ट्रीम उपयोग करने, और कैश डायरेक्टरी न उपयोग करने के लिए कॉन्फ़िगर करती है।

4. **मॉडल लोड करना**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - यह लाइन निर्दिष्ट डायरेक्टरी से मॉडल को लोड करती है, पहले से परिभाषित कॉन्फ़िगरेशन सेटिंग्स का उपयोग करते हुए। यह आवश्यक होने पर रिमोट कोड निष्पादन की अनुमति भी देती है।

5. **टोकनाइज़र लोड करना**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - यह लाइन टोकनाइज़र को लोड करती है, जो टेक्स्ट को ऐसे टोकन में बदलने का काम करता है जिन्हें मॉडल समझ सके।

6. **टोकनाइज़र आर्गुमेंट्स सेट करना**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - यह डिक्शनरी बताती है कि टोकनाइज़ किए गए आउटपुट में स्पेशल टोकन नहीं जोड़े जाएंगे।

7. **प्रॉम्प्ट परिभाषित करना**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - यह स्ट्रिंग एक बातचीत का प्रॉम्प्ट सेट करती है जहाँ यूजर AI असिस्टेंट से खुद का परिचय देने को कहता है।

8. **प्रॉम्प्ट को टोकनाइज़ करना**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - यह लाइन प्रॉम्प्ट को ऐसे टोकन में बदलती है जिन्हें मॉडल प्रोसेस कर सके, और परिणाम को PyTorch टेन्सर के रूप में लौटाती है।

9. **प्रतिक्रिया उत्पन्न करना**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - यह लाइन इनपुट टोकन के आधार पर मॉडल का उपयोग करके प्रतिक्रिया उत्पन्न करती है, जिसमें अधिकतम 1024 नए टोकन हो सकते हैं।

10. **प्रतिक्रिया को डिकोड करना**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - यह लाइन जनरेट किए गए टोकन को फिर से मानव-पठनीय स्ट्रिंग में बदलती है, किसी भी स्पेशल टोकन को छोड़ते हुए, और पहला परिणाम प्राप्त करती है।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।