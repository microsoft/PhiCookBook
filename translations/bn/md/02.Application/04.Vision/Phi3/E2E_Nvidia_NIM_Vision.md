### উদাহরণ পরিস্থিতি

ধরা যাক আপনার কাছে একটি ছবি (`demo.png`) আছে এবং আপনি এমন একটি Python কোড তৈরি করতে চান যা এই ছবিটি প্রক্রিয়াজাত করে এবং একটি নতুন সংস্করণ সংরক্ষণ করে (`phi-3-vision.jpg`)।

উপরের কোডটি এই প্রক্রিয়াটি স্বয়ংক্রিয় করে:

1. পরিবেশ এবং প্রয়োজনীয় কনফিগারেশন সেট আপ করা।
2. এমন একটি প্রম্পট তৈরি করা যা মডেলকে প্রয়োজনীয় Python কোড তৈরি করার নির্দেশ দেয়।
3. প্রম্পটটি মডেলের কাছে পাঠানো এবং তৈরি হওয়া কোড সংগ্রহ করা।
4. তৈরি হওয়া কোড বের করে চালানো।
5. মূল এবং প্রক্রিয়াজাত ছবিগুলো প্রদর্শন করা।

এই পদ্ধতিটি AI এর ক্ষমতা ব্যবহার করে ছবি প্রক্রিয়াকরণ কাজগুলো স্বয়ংক্রিয় করে, যা আপনার কাজকে সহজ এবং দ্রুত করে তোলে।

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

চলুন ধাপে ধাপে পুরো কোডটি কী করে তা বিশ্লেষণ করি:

1. **প্রয়োজনীয় প্যাকেজ ইনস্টল করুন**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    এই কমান্ডটি `langchain_nvidia_ai_endpoints` প্যাকেজটি ইনস্টল করে, নিশ্চিত করে এটি সর্বশেষ সংস্করণ।

2. **প্রয়োজনীয় মডিউলগুলো ইম্পোর্ট করুন**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    এই ইম্পোর্টগুলো NVIDIA AI এন্ডপয়েন্টের সাথে ইন্টারঅ্যাকশন, পাসওয়ার্ড নিরাপদে হ্যান্ডেল করা, অপারেটিং সিস্টেমের সাথে কাজ করা এবং base64 ফরম্যাটে ডেটা এনকোড/ডিকোড করার জন্য প্রয়োজনীয় মডিউলগুলো নিয়ে আসে।

3. **API কী সেট আপ করুন**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    এই কোডটি চেক করে `NVIDIA_API_KEY` পরিবেশ ভেরিয়েবল সেট করা আছে কিনা। না থাকলে, এটি ব্যবহারকারীকে নিরাপদে তাদের API কী প্রবেশ করার জন্য অনুরোধ করে।

4. **মডেল এবং ছবি পাথ নির্ধারণ করুন**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    এখানে ব্যবহৃত মডেল সেট করা হয়, `ChatNVIDIA` এর একটি ইনস্ট্যান্স তৈরি করা হয় নির্দিষ্ট মডেল দিয়ে, এবং ছবির ফাইলের পাথ নির্ধারণ করা হয়।

5. **টেক্সট প্রম্পট তৈরি করুন**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    এটি একটি টেক্সট প্রম্পট সংজ্ঞায়িত করে যা মডেলকে ছবি প্রক্রিয়াজাত করার জন্য Python কোড তৈরি করার নির্দেশ দেয়।

6. **ছবিটি base64 এ এনকোড করুন**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    এই কোডটি ছবির ফাইলটি পড়ে, base64 এ এনকোড করে, এবং এনকোড করা ডেটা দিয়ে একটি HTML ইমেজ ট্যাগ তৈরি করে।

7. **টেক্সট এবং ছবিকে প্রম্পটে একত্রিত করুন**:
    ```python
    prompt = f"{text} {image}"
    ```
    এটি টেক্সট প্রম্পট এবং HTML ইমেজ ট্যাগকে একত্রিত করে একটি স্ট্রিং তৈরি করে।

8. **ChatNVIDIA ব্যবহার করে কোড তৈরি করুন**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    এই কোডটি প্রম্পটটি `ChatNVIDIA` মডেলের কাছে পাঠায় এবং তৈরি হওয়া কোডটি অংশে অংশে সংগ্রহ করে, প্রতিটি অংশ প্রিন্ট এবং `code` স্ট্রিংয়ে যোগ করে।

9. **তৈরি হওয়া কন্টেন্ট থেকে Python কোড বের করুন**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    এই অংশটি মার্কডাউন ফরম্যাটিং সরিয়ে প্রকৃত Python কোড বের করে।

10. **তৈরি হওয়া কোড চালান**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    এটি বের করা Python কোডটি সাবপ্রসেস হিসেবে চালায় এবং এর আউটপুট ক্যাপচার করে।

11. **ছবিগুলো প্রদর্শন করুন**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    এই লাইনগুলো `IPython.display` মডিউল ব্যবহার করে ছবিগুলো প্রদর্শন করে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।