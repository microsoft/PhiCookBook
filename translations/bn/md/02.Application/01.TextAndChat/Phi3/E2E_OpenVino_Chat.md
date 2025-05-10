<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:51:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "bn"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

এই কোডটি একটি মডেল OpenVINO ফরম্যাটে রপ্তানি করে, সেটি লোড করে এবং একটি প্রদত্ত প্রম্পটের জন্য উত্তর তৈরি করতে ব্যবহার করে।

1. **মডেল রপ্তানি করা**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - এই কমান্ডটি `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` ব্যবহার করে।

2. **প্রয়োজনীয় লাইব্রেরি আমদানি করা**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - এই লাইনগুলো `transformers` library and the `optimum.intel.openvino` মডিউল থেকে ক্লাসগুলো আমদানি করে, যা মডেল লোড এবং ব্যবহার করার জন্য দরকার।

3. **মডেল ডিরেক্টরি এবং কনফিগারেশন সেট করা**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` একটি ডিকশনারি যা OpenVINO মডেলকে কম লেটেন্সি প্রাধান্য দিতে, এক ইনফারেন্স স্ট্রিম ব্যবহার করতে এবং কোনো ক্যাশ ডিরেক্টরি ব্যবহার না করতে কনফিগার করে।

4. **মডেল লোড করা**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - এই লাইনটি নির্দিষ্ট ডিরেক্টরি থেকে মডেল লোড করে, পূর্বে সংজ্ঞায়িত কনফিগারেশন সেটিংস ব্যবহার করে। প্রয়োজনে রিমোট কোড এক্সিকিউশনও অনুমতি দেয়।

5. **টোকেনাইজার লোড করা**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - এই লাইনটি টোকেনাইজার লোড করে, যা টেক্সটকে টোকেনে রূপান্তর করার জন্য দায়ী, যাতে মডেল তা বুঝতে পারে।

6. **টোকেনাইজার আর্গুমেন্ট সেট করা**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - এই ডিকশনারিটি নির্দিষ্ট করে যে স্পেশাল টোকেন টোকেনাইজড আউটপুটে যোগ করা হবে না।

7. **প্রম্পট সংজ্ঞায়িত করা**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - এই স্ট্রিংটি একটি কথোপকথনের প্রম্পট সেট করে যেখানে ব্যবহারকারী AI অ্যাসিস্ট্যান্টকে তার পরিচয় দিতে বলে।

8. **প্রম্পট টোকেনাইজ করা**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - এই লাইনটি প্রম্পটকে এমন টোকেনে রূপান্তর করে যা মডেল প্রক্রিয়াজাত করতে পারে, এবং ফলাফল PyTorch টেনসর হিসেবে ফেরত দেয়।

9. **উত্তর তৈরি করা**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - এই লাইনটি ইনপুট টোকেনের ভিত্তিতে মডেল ব্যবহার করে উত্তর তৈরি করে, সর্বোচ্চ ১০২৪ নতুন টোকেন পর্যন্ত।

10. **উত্তর ডিকোড করা**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - এই লাইনটি তৈরি হওয়া টোকেনগুলোকে আবার মানুষ পড়ার উপযোগী স্ট্রিংয়ে রূপান্তর করে, কোনো স্পেশাল টোকেন বাদ দিয়ে, এবং প্রথম ফলাফলটি নিয়ে আসে।

**বিজ্ঞপ্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নয়।