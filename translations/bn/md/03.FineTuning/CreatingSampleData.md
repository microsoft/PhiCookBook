# Hugging Face থেকে DataSet এবং সংশ্লিষ্ট ছবি ডাউনলোড করে ইমেজ ডেটাসেট তৈরি করা

### ওভারভিউ

এই স্ক্রিপ্টটি মেশিন লার্নিংয়ের জন্য একটি ডেটাসেট প্রস্তুত করে, যেখানে প্রয়োজনীয় ছবি ডাউনলোড করা হয়, যেসব সারির ছবি ডাউনলোড ব্যর্থ হয় সেগুলো ফিল্টার করা হয়, এবং ডেটাসেটটি CSV ফাইল হিসেবে সংরক্ষণ করা হয়।

### প্রয়োজনীয়তা

এই স্ক্রিপ্ট চালানোর আগে নিশ্চিত করুন যে নিম্নলিখিত লাইব্রেরিগুলো ইনস্টল করা আছে: `Pandas`, `Datasets`, `requests`, `PIL`, এবং `io`। এছাড়াও, লাইন ২-এ `'Insert_Your_Dataset'` এর জায়গায় আপনার Hugging Face থেকে ডেটাসেটের নাম বসাতে হবে।

প্রয়োজনীয় লাইব্রেরি:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### কার্যকারিতা

স্ক্রিপ্টটি নিম্নলিখিত ধাপগুলো সম্পাদন করে:

1. `load_dataset()` ফাংশন ব্যবহার করে Hugging Face থেকে ডেটাসেট ডাউনলোড করে।
2. `to_pandas()` মেথড ব্যবহার করে Hugging Face ডেটাসেটকে সহজে পরিচালনার জন্য Pandas DataFrame-এ রূপান্তর করে।
3. ডেটাসেট এবং ছবি সংরক্ষণের জন্য ডিরেক্টরি তৈরি করে।
4. DataFrame-এর প্রতিটি সারির মাধ্যমে ইটারেট করে, কাস্টম `download_image()` ফাংশন ব্যবহার করে ছবি ডাউনলোড করে, এবং যেসব সারির ছবি ডাউনলোড ব্যর্থ হয় সেগুলো ফিল্টার করে নতুন DataFrame `filtered_rows`-এ যোগ করে।
5. ফিল্টার করা সারিগুলো নিয়ে একটি নতুন DataFrame তৈরি করে সেটি ডিস্কে CSV ফাইল হিসেবে সংরক্ষণ করে।
6. ডেটাসেট এবং ছবি কোথায় সংরক্ষিত হয়েছে তা নির্দেশ করে একটি বার্তা প্রিন্ট করে।

### কাস্টম ফাংশন

`download_image()` ফাংশনটি একটি URL থেকে ছবি ডাউনলোড করে এবং Pillow Image Library (PIL) ও `io` মডিউল ব্যবহার করে লোকালি সংরক্ষণ করে। ছবি সফলভাবে ডাউনলোড হলে এটি True রিটার্ন করে, অন্যথায় False রিটার্ন করে। যদি রিকোয়েস্ট ব্যর্থ হয়, তাহলে এটি ত্রুটির বার্তা সহ একটি এক্সসেপশন ছুঁড়ে দেয়।

### এটি কীভাবে কাজ করে

`download_image` ফাংশনটি দুটি প্যারামিটার নেয়: image_url, যা ডাউনলোড করার ছবির URL, এবং save_path, যেখানে ডাউনলোড করা ছবি সংরক্ষণ করা হবে।

ফাংশনটি কাজ করার ধাপগুলো:

প্রথমে এটি requests.get মেথড ব্যবহার করে image_url-এ GET রিকোয়েস্ট পাঠায়। এটি URL থেকে ছবি ডেটা আনে।

`response.raise_for_status()` লাইনটি চেক করে রিকোয়েস্ট সফল হয়েছে কিনা। যদি রেসপন্স স্ট্যাটাস কোডে কোনো ত্রুটি থাকে (যেমন ৪০৪ - Not Found), তাহলে এটি একটি এক্সসেপশন ছুঁড়ে দেয়। এর ফলে আমরা নিশ্চিত হই যে শুধুমাত্র সফল রিকোয়েস্টের ক্ষেত্রে ছবি ডাউনলোড করা হবে।

এরপর ছবির ডেটা PIL (Python Imaging Library) এর Image.open মেথডে পাঠানো হয়। এই মেথডটি ছবির ডেটা থেকে একটি Image অবজেক্ট তৈরি করে।

`image.save(save_path)` লাইনটি ছবিটিকে নির্দিষ্ট save_path-এ সংরক্ষণ করে। save_path-এ ফাইলের নাম এবং এক্সটেনশন থাকতে হবে।

শেষে, ফাংশনটি True রিটার্ন করে জানায় যে ছবি সফলভাবে ডাউনলোড ও সংরক্ষণ হয়েছে। যদি কোনো এক্সসেপশন ঘটে, তাহলে এটি এক্সসেপশন ধরে, ব্যর্থতার বার্তা প্রিন্ট করে এবং False রিটার্ন করে।

এই ফাংশনটি URL থেকে ছবি ডাউনলোড করে লোকালি সংরক্ষণ করার জন্য উপযোগী। এটি ডাউনলোডের সময় সম্ভাব্য ত্রুটিগুলো হ্যান্ডেল করে এবং ডাউনলোড সফল হয়েছে কিনা সে সম্পর্কে ফিডব্যাক দেয়।

উল্লেখযোগ্য যে, requests লাইব্রেরি HTTP রিকোয়েস্ট করার জন্য, PIL লাইব্রেরি ছবি নিয়ে কাজ করার জন্য, এবং BytesIO ক্লাস ছবি ডেটাকে বাইট স্ট্রিম হিসেবে হ্যান্ডেল করার জন্য ব্যবহৃত হয়।

### উপসংহার

এই স্ক্রিপ্টটি মেশিন লার্নিংয়ের জন্য ডেটাসেট প্রস্তুত করার একটি সহজ উপায় প্রদান করে, যেখানে প্রয়োজনীয় ছবি ডাউনলোড করা হয়, ছবি ডাউনলোড ব্যর্থ সারিগুলো ফিল্টার করা হয়, এবং ডেটাসেট CSV ফাইল হিসেবে সংরক্ষণ করা হয়।

### নমুনা স্ক্রিপ্ট

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### নমুনা কোড ডাউনলোড  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### নমুনা ডেটাসেট  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।