[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

এই কোডটি একটি মডেল OpenVINO ফরম্যাটে রপ্তানি করে, সেটি লোড করে এবং একটি নির্দিষ্ট প্রম্পটের জন্য উত্তর তৈরি করতে ব্যবহার করে।

1. **মডেল রপ্তানি করা**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - এই কমান্ডটি `optimum-cli` টুল ব্যবহার করে একটি মডেল OpenVINO ফরম্যাটে রপ্তানি করে, যা দক্ষ ইনফারেন্সের জন্য অপ্টিমাইজ করা হয়েছে।
   - রপ্তানি করা মডেলটি হলো `"microsoft/Phi-3-mini-4k-instruct"`, যা পূর্ববর্তী প্রসঙ্গের ভিত্তিতে টেক্সট তৈরি করার কাজের জন্য সেটআপ করা হয়েছে।
   - মডেলের ওজনগুলো ৪-বিট ইন্টিজার (`int4`) এ কোয়ান্টাইজ করা হয়েছে, যা মডেলের আকার কমায় এবং প্রক্রিয়াকরণ দ্রুত করে।
   - `group-size`, `ratio`, এবং `sym` এর মতো অন্যান্য প্যারামিটারগুলো কোয়ান্টাইজেশন প্রক্রিয়া সূক্ষ্মভাবে নিয়ন্ত্রণ করতে ব্যবহৃত হয়।
   - রপ্তানি করা মডেলটি `./model/phi3-instruct/int4` ডিরেক্টরিতে সংরক্ষণ করা হয়।

2. **প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করা**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - এই লাইনগুলো `transformers` লাইব্রেরি এবং `optimum.intel.openvino` মডিউল থেকে ক্লাসগুলো ইমপোর্ট করে, যা মডেল লোড এবং ব্যবহারের জন্য প্রয়োজন।

3. **মডেল ডিরেক্টরি এবং কনফিগারেশন সেট করা**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` নির্দেশ করে মডেল ফাইলগুলো কোথায় সংরক্ষিত আছে।
   - `ov_config` একটি ডিকশনারি যা OpenVINO মডেলকে কম লেটেন্সি, একক ইনফারেন্স স্ট্রিম ব্যবহার এবং ক্যাশ ডিরেক্টরি ব্যবহার না করার জন্য কনফিগার করে।

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
   - এই লাইনটি পূর্বে নির্ধারিত ডিরেক্টরি থেকে মডেল লোড করে, এবং কনফিগারেশন সেটিংস প্রয়োগ করে। প্রয়োজনে রিমোট কোড এক্সিকিউশনও অনুমোদিত।

5. **টোকেনাইজার লোড করা**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - এই লাইনটি টোকেনাইজার লোড করে, যা টেক্সটকে মডেল বুঝতে পারার মতো টোকেনে রূপান্তর করে।

6. **টোকেনাইজার আর্গুমেন্ট সেট করা**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - এই ডিকশনারিটি নির্দেশ করে যে টোকেনাইজড আউটপুটে বিশেষ টোকেন যোগ করা হবে না।

7. **প্রম্পট নির্ধারণ করা**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - এই স্ট্রিংটি একটি কথোপকথনের প্রম্পট সেট করে যেখানে ব্যবহারকারী AI সহকারীকে তার পরিচয় দিতে বলে।

8. **প্রম্পট টোকেনাইজ করা**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - এই লাইনটি প্রম্পটকে টোকেনে রূপান্তর করে যা মডেল প্রক্রিয়াকরণ করতে পারে, এবং ফলাফল PyTorch টেনসর হিসেবে ফেরত দেয়।

9. **উত্তর তৈরি করা**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - এই লাইনটি ইনপুট টোকেনের ভিত্তিতে মডেল ব্যবহার করে উত্তর তৈরি করে, সর্বোচ্চ ১০২৪ নতুন টোকেন পর্যন্ত।

10. **উত্তর ডিকোড করা**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - এই লাইনটি তৈরি করা টোকেনগুলোকে আবার মানুষের পড়ার উপযোগী স্ট্রিংয়ে রূপান্তর করে, বিশেষ টোকেনগুলো বাদ দিয়ে, এবং প্রথম ফলাফলটি নিয়ে আসে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।