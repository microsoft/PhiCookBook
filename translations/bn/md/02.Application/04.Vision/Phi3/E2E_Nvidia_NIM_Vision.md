<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:54:32+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "bn"
}
-->
### উদাহরণ পরিস্থিতি

ধরুন আপনার কাছে একটি ছবি (`demo.png`) আছে এবং আপনি এমন Python কোড তৈরি করতে চান যা এই ছবিটি প্রক্রিয়াজাত করবে এবং একটি নতুন সংস্করণ সংরক্ষণ করবে (`phi-3-vision.jpg`)।

উপরের কোডটি এই প্রক্রিয়াটি স্বয়ংক্রিয়ভাবে সম্পন্ন করে:

1. পরিবেশ এবং প্রয়োজনীয় কনফিগারেশন সেট আপ করা।
2. এমন একটি প্রম্পট তৈরি করা যা মডেলকে প্রয়োজনীয় Python কোড জেনারেট করার নির্দেশ দেয়।
3. প্রম্পটটি মডেলে পাঠানো এবং জেনারেট করা কোড সংগ্রহ করা।
4. জেনারেট করা কোড বের করে চালানো।
5. মূল এবং প্রক্রিয়াজাত ছবি প্রদর্শন করা।

এই পদ্ধতিটি AI এর শক্তি ব্যবহার করে ইমেজ প্রসেসিং কাজগুলো স্বয়ংক্রিয় করে, আপনার লক্ষ্য অর্জন সহজ এবং দ্রুততর করে তোলে।

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

চলুন ধাপে ধাপে পুরো কোডটি কী করে তা বিশ্লেষণ করি:

1. **প্রয়োজনীয় প্যাকেজ ইনস্টল করুন**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    এই কমান্ডটি `langchain_nvidia_ai_endpoints` প্যাকেজটি ইনস্টল করে, নিশ্চিত করে যে এটি সর্বশেষ সংস্করণ।

2. **প্রয়োজনীয় মডিউল ইমপোর্ট করুন**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    এই ইমপোর্টগুলো NVIDIA AI endpoints এর সাথে ইন্টারঅ্যাকশনের জন্য, পাসওয়ার্ড নিরাপদে হ্যান্ডল করার জন্য, অপারেটিং সিস্টেমের সাথে কাজ করার জন্য এবং base64 ফরম্যাটে ডেটা এনকোড/ডিকোড করার জন্য প্রয়োজনীয় মডিউলগুলো নিয়ে আসে।

3. **API কী সেট করুন**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    এই কোডটি চেক করে `NVIDIA_API_KEY` পরিবেশ ভেরিয়েবল সেট করা আছে কিনা। যদি না থাকে, তাহলে ব্যবহারকারীকে নিরাপদভাবে API কী প্রবেশ করার জন্য অনুরোধ করে।

4. **মডেল এবং ছবি পথ নির্ধারণ করুন**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    এখানে ব্যবহৃত মডেল নির্ধারণ করা হয়, `ChatNVIDIA` এর একটি ইনস্ট্যান্স তৈরি করা হয় নির্দিষ্ট মডেল দিয়ে, এবং ছবির ফাইলের পথ নির্ধারণ করা হয়।

5. **টেক্সট প্রম্পট তৈরি করুন**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    এটি একটি টেক্সট প্রম্পট সংজ্ঞায়িত করে যা মডেলকে একটি ছবি প্রক্রিয়াজাত করার জন্য Python কোড তৈরি করার নির্দেশ দেয়।

6. **ছবিটি base64 এ এনকোড করুন**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    এই কোডটি ছবির ফাইলটি পড়ে, base64 এ এনকোড করে এবং এনকোড করা ডেটার সাথে একটি HTML ইমেজ ট্যাগ তৈরি করে।

7. **টেক্সট এবং ছবি একত্রিত করে প্রম্পট তৈরি করুন**:
    ```python
    prompt = f"{text} {image}"
    ```
    এটি টেক্সট প্রম্পট এবং HTML ইমেজ ট্যাগকে একত্রিত করে একটি স্ট্রিং তৈরি করে।

8. **ChatNVIDIA ব্যবহার করে কোড জেনারেট করুন**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    এই কোডটি প্রম্পটটি `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` স্ট্রিং-এ পাঠায়।

9. **জেনারেট করা কন্টেন্ট থেকে Python কোড বের করুন**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    এটি মার্কডাউন ফরম্যাটিং সরিয়ে জেনারেট করা কন্টেন্ট থেকে প্রকৃত Python কোড বের করে।

10. **জেনারেট করা কোড চালান**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    এটি বের করা Python কোড একটি সাবপ্রসেস হিসেবে চালায় এবং এর আউটপুট ক্যাপচার করে।

11. **ছবি প্রদর্শন করুন**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    এই লাইনগুলো `IPython.display` মডিউল ব্যবহার করে ছবিগুলো প্রদর্শন করে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে জানুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অমিল থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃপক্ষ সূত্র হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।