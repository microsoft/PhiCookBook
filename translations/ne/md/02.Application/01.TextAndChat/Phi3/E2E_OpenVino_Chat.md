[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

यो कोडले मोडेललाई OpenVINO ढाँचामा निर्यात गर्छ, त्यसलाई लोड गर्छ, र दिइएको प्रॉम्प्टको आधारमा प्रतिक्रिया उत्पन्न गर्न प्रयोग गर्छ।

1. **मोडेल निर्यात गर्दै**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - यो कमाण्डले `optimum-cli` उपकरण प्रयोग गरेर मोडेललाई OpenVINO ढाँचामा निर्यात गर्छ, जुन प्रभावकारी इन्फरेन्सका लागि अनुकूलित छ।
   - निर्यात गरिने मोडेल `"microsoft/Phi-3-mini-4k-instruct"` हो, र यो अघिल्लो सन्दर्भको आधारमा पाठ उत्पन्न गर्ने कार्यका लागि सेट गरिएको छ।
   - मोडेलका तौलहरू ४-बिट इन्टिजर (`int4`) मा क्वान्टाइज गरिएका छन्, जसले मोडेलको आकार घटाउन र प्रक्रिया छिटो बनाउन मद्दत गर्छ।
   - `group-size`, `ratio`, र `sym` जस्ता अन्य प्यारामिटरहरूले क्वान्टाइजेशन प्रक्रियालाई थप परिमार्जन गर्छन्।
   - निर्यात गरिएको मोडेल `./model/phi3-instruct/int4` डाइरेक्टरीमा सुरक्षित गरिन्छ।

2. **आवश्यक लाइब्रेरीहरू आयात गर्दै**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - यी लाइनहरूले `transformers` लाइब्रेरी र `optimum.intel.openvino` मोड्युलबाट क्लासहरू आयात गर्छन्, जुन मोडेल लोड र प्रयोग गर्न आवश्यक हुन्छ।

3. **मोडेल डाइरेक्टरी र कन्फिगरेसन सेट गर्दै**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` ले मोडेल फाइलहरू कहाँ राखिएको छ भनेर जनाउँछ।
   - `ov_config` एउटा डिक्सनरी हो जसले OpenVINO मोडेललाई कम विलम्बता प्राथमिकता दिन, एक इन्फरेन्स स्ट्रिम प्रयोग गर्न, र क्यास डाइरेक्टरी नचलाउन कन्फिगर गर्छ।

4. **मोडेल लोड गर्दै**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - यो लाइनले निर्दिष्ट गरिएको डाइरेक्टरीबाट मोडेल लोड गर्छ, पहिले परिभाषित कन्फिगरेसन सेटिङहरू प्रयोग गर्दै। आवश्यक परेमा रिमोट कोड एक्सिक्युसन पनि अनुमति दिन्छ।

5. **टोकनाइजर लोड गर्दै**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - यो लाइनले टोकनाइजर लोड गर्छ, जुन पाठलाई मोडेलले बुझ्ने टोकनहरूमा रूपान्तरण गर्ने जिम्मेवार हुन्छ।

6. **टोकनाइजरका आर्गुमेन्टहरू सेट गर्दै**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - यो डिक्सनरीले टोकनाइज गरिएको आउटपुटमा विशेष टोकनहरू थप्न नहुने निर्दिष्ट गर्छ।

7. **प्रॉम्प्ट परिभाषित गर्दै**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - यो स्ट्रिङले एउटा संवाद प्रॉम्प्ट सेट गर्छ जहाँ प्रयोगकर्ताले AI सहायकलाई आफ्नो परिचय दिन भन्छ।

8. **प्रॉम्प्टलाई टोकनाइज गर्दै**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - यो लाइनले प्रॉम्प्टलाई मोडेलले प्रक्रिया गर्न सक्ने टोकनहरूमा रूपान्तरण गर्छ, र परिणामलाई PyTorch टेन्सरको रूपमा फर्काउँछ।

9. **प्रतिक्रिया उत्पन्न गर्दै**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - यो लाइनले मोडेललाई इनपुट टोकनहरूको आधारमा प्रतिक्रिया उत्पन्न गर्न प्रयोग गर्छ, अधिकतम १०२४ नयाँ टोकनसम्म।

10. **प्रतिक्रियालाई डिकोड गर्दै**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - यो लाइनले उत्पन्न टोकनहरूलाई फेरि मानवले पढ्न सक्ने स्ट्रिङमा रूपान्तरण गर्छ, कुनै विशेष टोकनहरू छोड्दै, र पहिलो परिणाम प्राप्त गर्छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।