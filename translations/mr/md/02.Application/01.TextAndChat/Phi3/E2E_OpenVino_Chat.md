<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:51:44+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "mr"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

हा कोड एक मॉडेल OpenVINO फॉरमॅटमध्ये एक्सपोर्ट करतो, ते लोड करतो, आणि दिलेल्या प्रॉम्प्टसाठी उत्तर तयार करण्यासाठी वापरतो.

1. **मॉडेल एक्सपोर्ट करणे**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - हा कमांड `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` वापरतो.

2. **आवश्यक लायब्ररी इम्पोर्ट करणे**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - या ओळी `transformers` library and the `optimum.intel.openvino` मॉड्यूलमधील क्लासेस इम्पोर्ट करतात, जे मॉडेल लोड आणि वापरण्यासाठी आवश्यक आहेत.

3. **मॉडेल डायरेक्टरी आणि कॉन्फिगरेशन सेट करणे**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` हा एक डिक्शनरी आहे जो OpenVINO मॉडेलसाठी लो लेटन्सी प्राधान्य देतो, एकच इन्फरन्स स्ट्रीम वापरतो, आणि कॅश डायरेक्टरी वापरत नाही.

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
   - ही ओळ दिलेल्या डायरेक्टरीमधून मॉडेल लोड करते, आधी सेट केलेल्या कॉन्फिगरेशननुसार. गरज पडल्यास रिमोट कोड एक्सिक्युशनसाठी परवानगी देखील देते.

5. **टोकनायझर लोड करणे**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - ही ओळ टोकनायझर लोड करते, जो मजकूर टोकन्समध्ये रूपांतरित करतो जे मॉडेल समजू शकते.

6. **टोकनायझरच्या अर्ग्युमेंट्स सेट करणे**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - हा डिक्शनरी सांगतो की टोकनायझेशनमध्ये स्पेशल टोकन्स जोडू नयेत.

7. **प्रॉम्प्ट परिभाषित करणे**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - ही स्ट्रिंग एक संभाषण प्रॉम्प्ट सेट करते जिथे वापरकर्ता AI सहाय्यकाला स्वतःची ओळख करून देण्यास सांगतो.

8. **प्रॉम्प्ट टोकनायझ करणे**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - ही ओळ प्रॉम्प्ट टोकन्समध्ये रूपांतरित करते जे मॉडेल प्रक्रिया करू शकते, आणि परिणाम PyTorch टेन्सर्समध्ये परत करते.

9. **उत्तर तयार करणे**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - ही ओळ इनपुट टोकन्सवरून मॉडेल वापरून उत्तर तयार करते, जास्तीत जास्त 1024 नवीन टोकन्सपर्यंत.

10. **उत्तर डीकोड करणे**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - ही ओळ तयार केलेले टोकन्स परत मानवी वाचनीय स्ट्रिंगमध्ये रूपांतरित करते, कोणतेही स्पेशल टोकन्स वगळून, आणि पहिला निकाल घेते.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत म्हणून मानला जावा. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.