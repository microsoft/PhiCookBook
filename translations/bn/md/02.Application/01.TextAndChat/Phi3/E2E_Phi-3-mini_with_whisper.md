<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:16:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "bn"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## ওভারভিউ

Interactive Phi 3 Mini 4K Instruct Chatbot একটি টুল যা ব্যবহারকারীদের Microsoft Phi 3 Mini 4K instruct ডেমোর সাথে টেক্সট বা অডিও ইনপুটের মাধ্যমে ইন্টারঅ্যাক্ট করার সুযোগ দেয়। এই চ্যাটবটটি বিভিন্ন কাজের জন্য ব্যবহার করা যেতে পারে, যেমন অনুবাদ, আবহাওয়ার আপডেট, এবং সাধারণ তথ্য সংগ্রহ।

### শুরু করা

এই চ্যাটবট ব্যবহার করতে, নিচের নির্দেশনাগুলো অনুসরণ করুন:

1. একটি নতুন [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) খুলুন
2. নোটবুকের প্রধান উইন্ডোতে, আপনি একটি চ্যাটবক্স ইন্টারফেস দেখতে পাবেন যেখানে একটি টেক্সট ইনপুট বক্স এবং "Send" বাটন থাকবে।
3. টেক্সট-ভিত্তিক চ্যাটবট ব্যবহার করতে, আপনার মেসেজটি টেক্সট ইনপুট বক্সে টাইপ করুন এবং "Send" বাটনে ক্লিক করুন। চ্যাটবট একটি অডিও ফাইল রেসপন্স করবে যা সরাসরি নোটবুকের ভিতর থেকে প্লে করা যাবে।

**Note**: এই টুলটি চালানোর জন্য GPU এবং Microsoft Phi-3 ও OpenAI Whisper মডেলগুলোর অ্যাক্সেস প্রয়োজন, যা স্পিচ রিকগনিশন এবং অনুবাদের জন্য ব্যবহৃত হয়।

### GPU প্রয়োজনীয়তা

এই ডেমো চালানোর জন্য আপনার ১২ জিবি GPU মেমোরি প্রয়োজন।

**Microsoft-Phi-3-Mini-4K instruct** ডেমোটি GPU-তে চালানোর জন্য মেমোরির প্রয়োজনীয়তা বিভিন্ন ফ্যাক্টরের উপর নির্ভর করে, যেমন ইনপুট ডেটার আকার (অডিও বা টেক্সট), অনুবাদের ভাষা, মডেলের গতি, এবং GPU-র উপলব্ধ মেমোরি।

সাধারণত, Whisper মডেল GPU-তে চালানোর জন্য ডিজাইন করা হয়েছে। Whisper মডেল চালানোর জন্য সুপারিশকৃত ন্যূনতম GPU মেমোরি ৮ জিবি, তবে প্রয়োজনে এটি বড় মেমোরিও সামলাতে পারে।

বেশি ডেটা বা অনুরোধের উচ্চ পরিমাণ মডেলে চালালে বেশি GPU মেমোরি প্রয়োজন হতে পারে এবং পারফরম্যান্স সমস্যা দেখা দিতে পারে। আপনার ব্যবহারের ক্ষেত্রে বিভিন্ন কনফিগারেশন দিয়ে পরীক্ষা করে মেমোরি ব্যবহারের পর্যবেক্ষণ করা এবং উপযুক্ত সেটিংস নির্ধারণ করা উত্তম।

## E2E স্যাম্পল Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper এর জন্য

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) নামক জুপিটার নোটবুকটি দেখায় কিভাবে Microsoft Phi 3 Mini 4K instruct ডেমো ব্যবহার করে অডিও বা লিখিত টেক্সট ইনপুট থেকে টেক্সট তৈরি করা যায়। নোটবুকটি কয়েকটি ফাংশন সংজ্ঞায়িত করে:

1. `tts_file_name(text)`: এই ফাংশন ইনপুট টেক্সটের ভিত্তিতে একটি ফাইল নাম তৈরি করে যা জেনারেট করা অডিও ফাইল সংরক্ষণের জন্য ব্যবহৃত হয়।
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: এই ফাংশন Edge TTS API ব্যবহার করে ইনপুট টেক্সটের চাঙ্কের তালিকা থেকে একটি অডিও ফাইল তৈরি করে। ইনপুট প্যারামিটারগুলো হলো চাঙ্কের তালিকা, স্পিচ রেট, ভয়েস নাম, এবং জেনারেট করা অডিও ফাইল সংরক্ষণের আউটপুট পাথ।
1. `talk(input_text)`: এই ফাংশন Edge TTS API ব্যবহার করে একটি অডিও ফাইল তৈরি করে এবং /content/audio ডিরেক্টরির মধ্যে র‍্যান্ডম ফাইল নাম দিয়ে সংরক্ষণ করে। ইনপুট প্যারামিটার হলো স্পিচে রূপান্তরিত করার জন্য ইনপুট টেক্সট।
1. `run_text_prompt(message, chat_history)`: এই ফাংশন Microsoft Phi 3 Mini 4K instruct ডেমো ব্যবহার করে একটি মেসেজ ইনপুট থেকে অডিও ফাইল তৈরি করে এবং সেটি চ্যাট ইতিহাসে যোগ করে।
1. `run_audio_prompt(audio, chat_history)`: এই ফাংশন Whisper মডেল API ব্যবহার করে একটি অডিও ফাইলকে টেক্সটে রূপান্তর করে এবং সেটি `run_text_prompt()` ফাংশনে পাঠায়।
1. কোডটি একটি Gradio অ্যাপ চালু করে যা ব্যবহারকারীদের Phi 3 Mini 4K instruct ডেমোর সাথে মেসেজ টাইপ করে বা অডিও ফাইল আপলোড করে ইন্টারঅ্যাক্ট করার সুযোগ দেয়। আউটপুট অ্যাপের ভিতরে টেক্সট মেসেজ হিসেবে প্রদর্শিত হয়।

## সমস্যা সমাধান

Cuda GPU ড্রাইভার ইনস্টল করা

1. নিশ্চিত করুন আপনার লিনাক্স অ্যাপ্লিকেশন আপ টু ডেট আছে

    ```bash
    sudo apt update
    ```

1. Cuda ড্রাইভার ইনস্টল করুন

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Cuda ড্রাইভার লোকেশন রেজিস্টার করুন

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU মেমোরি সাইজ চেক করুন (প্রয়োজন ১২ জিবি GPU মেমোরি)

    ```bash
    nvidia-smi
    ```

1. ক্যাশ খালি করুন: যদি আপনি PyTorch ব্যবহার করেন, তাহলে torch.cuda.empty_cache() কল করে সমস্ত অব্যবহৃত ক্যাশড মেমোরি মুক্ত করতে পারেন যাতে অন্য GPU অ্যাপ্লিকেশনগুলো ব্যবহার করতে পারে

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda চেক করুন

    ```bash
    nvcc --version
    ```

1. Hugging Face টোকেন তৈরি করতে নিচের কাজগুলো করুন:

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) এ যান।
    - **New token** নির্বাচন করুন।
    - আপনি যে প্রজেক্টের জন্য ব্যবহার করতে চান তার **Name** লিখুন।
    - **Type** থেকে **Write** নির্বাচন করুন।

> **Note**
>
> যদি নিচের ত্রুটিটি পান:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> এটি সমাধানের জন্য, আপনার টার্মিনালে নিচের কমান্ডটি টাইপ করুন।
>
> ```bash
> sudo ldconfig
> ```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।