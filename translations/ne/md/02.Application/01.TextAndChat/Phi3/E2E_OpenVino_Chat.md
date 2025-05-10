<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:52:06+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "ne"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

यो कोडले मोडेललाई OpenVINO ढाँचामा निर्यात गर्छ, लोड गर्छ, र दिइएको प्रॉम्प्टमा प्रतिक्रिया जनाउन प्रयोग गर्छ।

1. **मोडेल निर्यात गर्दै**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - यो कमाण्डले `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` प्रयोग गर्छ।

2. **आवश्यक लाइब्रेरीहरू आयात गर्दै**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - यी लाइनहरूले `transformers` library and the `optimum.intel.openvino` मोड्युलबाट क्लासहरू आयात गर्छन्, जुन मोडेल लोड र प्रयोग गर्न आवश्यक छन्।

3. **मोडेल डाइरेक्टरी र कन्फिगरेसन सेट गर्दै**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` एउटा डिक्शनरी हो जसले OpenVINO मोडेललाई कम विलम्बता प्राथमिकता दिन, एक इनफरेन्स स्ट्रिम प्रयोग गर्न, र क्यास डाइरेक्टरी नबनाउन कन्फिगर गर्छ।

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
   - यो लाइनले टोकनाइजर लोड गर्छ, जसले टेक्स्टलाई मोडेलले बुझ्न सक्ने टोकनहरूमा रूपान्तरण गर्छ।

6. **टोकनाइजरका लागि आर्गुमेन्टहरू सेट गर्दै**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - यो डिक्शनरीले विशेष टोकनहरू टोकनाइज्ड आउटपुटमा थप्न नहुने निर्दिष्ट गर्छ।

7. **प्रॉम्प्ट परिभाषित गर्दै**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - यो स्ट्रिङले एउटा संवाद प्रॉम्प्ट सेट गर्छ जहाँ प्रयोगकर्ताले AI सहायकलाई आफूलाई परिचय गराउन भन्छ।

8. **प्रॉम्प्टलाई टोकनाइज गर्दै**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - यो लाइनले प्रॉम्प्टलाई मोडेलले प्रक्रिया गर्न सक्ने टोकनहरूमा रूपान्तरण गर्छ, र परिणामलाई PyTorch टेन्सरको रूपमा फर्काउँछ।

9. **प्रतिक्रिया उत्पन्न गर्दै**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - यो लाइनले मोडेललाई इनपुट टोकनहरूको आधारमा प्रतिक्रिया उत्पन्न गर्न प्रयोग गर्छ, अधिकतम 1024 नयाँ टोकनसम्म।

10. **प्रतिक्रियालाई डिकोड गर्दै**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - यो लाइनले उत्पन्न टोकनहरूलाई मानवीय पढ्न मिल्ने स्ट्रिङमा रूपान्तरण गर्छ, कुनै विशेष टोकनहरू छोड्दै, र पहिलो परिणाम प्राप्त गर्छ।

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। मूल दस्तावेज़लाई यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।