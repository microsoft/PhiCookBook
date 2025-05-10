<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:23:05+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "bn"
}
-->
# Hugging Face থেকে DataSet এবং সংশ্লিষ্ট ছবি ডাউনলোড করে ইমেজ ডেটা সেট তৈরি করা


### ওভারভিউ

এই স্ক্রিপ্টটি মেশিন লার্নিং-এর জন্য একটি ডেটাসেট তৈরি করে, যেখানে প্রয়োজনীয় ছবি ডাউনলোড করা হয়, যেসব সারিতে ছবি ডাউনলোড ব্যর্থ হয় সেগুলো ফিল্টার করা হয়, এবং ডেটাসেটটি CSV ফাইল হিসেবে সংরক্ষণ করা হয়।

### প্রয়োজনীয়তা

এই স্ক্রিপ্ট চালানোর আগে নিশ্চিত করুন যে নিম্নলিখিত লাইব্রেরিগুলো ইনস্টল করা আছে: `Pandas`, `Datasets`, `requests`, `PIL`, এবং `io`। এছাড়াও, লাইন ২-এ `'Insert_Your_Dataset'` আপনার Hugging Face থেকে ডেটাসেটের নাম দিয়ে প্রতিস্থাপন করতে হবে।

প্রয়োজনীয় লাইব্রেরি:

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

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` ফাংশনটি একটি URL থেকে ছবি ডাউনলোড করে এবং Pillow Image Library (PIL) এবং `io` মডিউল ব্যবহার করে লোকালি সংরক্ষণ করে। যদি ছবি সফলভাবে ডাউনলোড হয় তবে এটি True রিটার্ন করে, অন্যথায় False রিটার্ন করে। রিকোয়েস্ট ব্যর্থ হলে ফাংশনটি একটি এক্সসেপশনসহ এরর মেসেজ ছুঁড়ে দেয়।

### এটি কীভাবে কাজ করে

download_image ফাংশনটি দুইটি প্যারামিটার নেয়: image_url, অর্থাৎ ডাউনলোড করার ছবি URL এবং save_path, যেখানে ডাউনলোডকৃত ছবি সংরক্ষণ করা হবে।

ফাংশনটি কাজ করার ধাপগুলো:

প্রথমে requests.get মেথড ব্যবহার করে image_url এ GET রিকোয়েস্ট পাঠায়। এটি URL থেকে ছবি ডেটা নিয়ে আসে।

response.raise_for_status() লাইনটি চেক করে রিকোয়েস্ট সফল হয়েছে কি না। যদি রেসপন্স স্ট্যাটাস কোড কোনো এরর নির্দেশ করে (যেমন ৪০৪ - Not Found), তাহলে এটি এক্সসেপশন ছুঁড়ে দেয়। এর ফলে আমরা নিশ্চিত হই যে শুধুমাত্র সফল রিকোয়েস্টের ক্ষেত্রে ছবি ডাউনলোড করা হবে।

এরপর ছবি ডেটা PIL (Python Imaging Library) এর Image.open মেথডে পাঠানো হয়। এই মেথডটি ছবির ডেটা থেকে একটি Image অবজেক্ট তৈরি করে।

image.save(save_path) লাইনটি ছবিটি নির্দিষ্ট save_path এ সংরক্ষণ করে। save_path এ ফাইলের নাম এবং এক্সটেনশন অন্তর্ভুক্ত থাকতে হবে।

সবশেষে, ফাংশনটি True রিটার্ন করে জানায় যে ছবি সফলভাবে ডাউনলোড ও সংরক্ষণ হয়েছে। যদি কোনো এক্সসেপশন ঘটে, তাহলে তা ধরে একটি এরর মেসেজ প্রিন্ট করে এবং False রিটার্ন করে।

এই ফাংশনটি URL থেকে ছবি ডাউনলোড করে লোকালি সংরক্ষণ করার জন্য উপযোগী। এটি ডাউনলোড প্রক্রিয়ার সময় সম্ভাব্য ত্রুটিগুলো সামলায় এবং ডাউনলোড সফল হয়েছে কি না সে বিষয়ে ফিডব্যাক দেয়।

উল্লেখযোগ্য যে, HTTP রিকোয়েস্ট করার জন্য requests লাইব্রেরি ব্যবহার করা হয়, ছবির কাজের জন্য PIL লাইব্রেরি ব্যবহার করা হয়, এবং BytesIO ক্লাস ব্যবহার করে ছবির ডেটাকে বাইট স্ট্রিম হিসেবে হ্যান্ডেল করা হয়।



### উপসংহার

এই স্ক্রিপ্টটি মেশিন লার্নিংয়ের জন্য প্রয়োজনীয় ছবি ডাউনলোড করে, ডাউনলোড ব্যর্থ সারিগুলো ফিল্টার করে, এবং ডেটাসেটকে CSV ফাইলে সংরক্ষণ করে একটি সহজ উপায় প্রদান করে।

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

### নমুনা ডেটা সেট  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**অস্বীকারোক্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে অনুগ্রহ করে জানুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।