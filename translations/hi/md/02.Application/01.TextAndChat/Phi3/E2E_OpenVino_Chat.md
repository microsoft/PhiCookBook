<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-08T05:42:55+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "hi"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

यह कोड एक मॉडल को OpenVINO फॉर्मेट में एक्सपोर्ट करता है, उसे लोड करता है, और दिए गए प्रॉम्प्ट के आधार पर प्रतिक्रिया जनरेट करता है।

1. **मॉडल एक्सपोर्ट करना**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - यह कमांड `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` का उपयोग करता है।

2. **आवश्यक लाइब्रेरी इम्पोर्ट करना**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - ये लाइनें `transformers` library and the `optimum.intel.openvino` मॉड्यूल से क्लासेस इम्पोर्ट करती हैं, जो मॉडल को लोड और उपयोग करने के लिए जरूरी हैं।

3. **मॉडल डायरेक्टरी और कॉन्फ़िगरेशन सेट करना**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` एक डिक्शनरी है जो OpenVINO मॉडल को कम लेटेंसी प्राथमिकता देने, एक इन्फरेंस स्ट्रीम उपयोग करने, और कैश डायरेक्टरी न उपयोग करने के लिए कॉन्फ़िगर करती है।

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
   - यह लाइन निर्दिष्ट डायरेक्टरी से मॉडल लोड करती है, जो पहले से परिभाषित कॉन्फ़िगरेशन सेटिंग्स का उपयोग करती है। जरूरत पड़ने पर रिमोट कोड एक्सेक्यूशन की अनुमति भी देती है।

5. **टोकनाइज़र लोड करना**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - यह लाइन टोकनाइज़र लोड करती है, जो टेक्स्ट को ऐसे टोकन्स में बदलने का काम करता है जिन्हें मॉडल समझ सके।

6. **टोकनाइज़र के आर्गुमेंट्स सेट करना**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - यह डिक्शनरी बताती है कि टोकनाइज़ किए गए आउटपुट में कोई स्पेशल टोकन्स नहीं जोड़े जाएंगे।

7. **प्रॉम्प्ट परिभाषित करना**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - यह स्ट्रिंग एक बातचीत का प्रॉम्प्ट सेट करती है जिसमें यूजर AI असिस्टेंट से अपना परिचय देने के लिए कहता है।

8. **प्रॉम्प्ट को टोकनाइज़ करना**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - यह लाइन प्रॉम्प्ट को ऐसे टोकन्स में बदलती है जिन्हें मॉडल प्रोसेस कर सके, और परिणाम PyTorch टेन्सर्स के रूप में लौटाती है।

9. **प्रतिक्रिया जनरेट करना**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - यह लाइन इनपुट टोकन्स के आधार पर मॉडल का उपयोग कर प्रतिक्रिया जनरेट करती है, जिसमें अधिकतम 1024 नए टोकन्स हो सकते हैं।

10. **प्रतिक्रिया डिकोड करना**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - यह लाइन जनरेट किए गए टोकन्स को मानव-पठनीय स्ट्रिंग में बदलती है, किसी भी स्पेशल टोकन्स को छोड़ते हुए, और पहला परिणाम प्राप्त करती है।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।