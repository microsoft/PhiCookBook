<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-09T19:07:54+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "my"
}
-->
# Hugging Face မှ DataSet နှင့် ပတ်သက်သော ပုံများကို ဒေါင်းလုပ်လုပ်၍ ပုံဒေတာ စုစည်းမှု ဖန်တီးခြင်း

### အနှစ်ချုပ်

ဤ script သည် မက်ရှင်လေ့လာမှုအတွက် လိုအပ်သော ပုံများကို ဒေါင်းလုပ်လုပ်ပြီး၊ ပုံဒေါင်းလုပ် မအောင်မြင်သော အတန်းများကို ဖယ်ရှားကာ CSV ဖိုင်အဖြစ် သိမ်းဆည်းပေးသည်။

### လိုအပ်ချက်များ

ဤ script ကို အသုံးပြုရန်မတိုင်မီ `Pandas`, `Datasets`, `requests`, `PIL`, နှင့် `io` စသည့် 라이ဘရယ်ရီများကို ထည့်သွင်းထားရန် လိုအပ်သည်။ Hugging Face မှ သင့် dataset အမည်ကို line 2 တွင် `'Insert_Your_Dataset'` အစား ထည့်သွင်းရန် လိုအပ်သည်။

လိုအပ်သော 라이ဘရယ်ရီများ -

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### လုပ်ဆောင်ချက်များ

ဤ script သည် အောက်ပါအဆင့်များကို ဆောင်ရွက်သည် -

1. `load_dataset()` function ဖြင့် Hugging Face မှ dataset ကို ဒေါင်းလုပ်လုပ်သည်။
2. `to_pandas()` method ဖြင့် Hugging Face dataset ကို Pandas DataFrame အဖြစ် ပြောင်းလဲ၍ လွယ်ကူစွာ ကိုင်တွယ်နိုင်စေသည်။
3. Dataset နှင့် ပုံများ သိမ်းဆည်းရန် ဖိုလ်ဒါများ ဖန်တီးသည်။
4. DataFrame ၏ အတန်းတိုင်းကို iterate လုပ်ကာ ပုံဒေါင်းလုပ် မအောင်မြင်သော အတန်းများကို ဖယ်ရှားရန် custom `download_image()` function ဖြင့် ပုံဒေါင်းလုပ်လုပ်ပြီး၊ စစ်ထုတ်ထားသော အတန်းများကို `filtered_rows` ဟုခေါ်သော အသစ် DataFrame တွင် ထည့်သွင်းသည်။
5. စစ်ထုတ်ထားသော အတန်းများပါသော အသစ် DataFrame ကို CSV ဖိုင်အဖြစ် သိမ်းဆည်းသည်။
6. Dataset နှင့် ပုံများ သိမ်းဆည်းထားသော တည်နေရာကို ပြသသည်။

### Custom Function

`download_image()` function သည် URL မှ ပုံကို ဒေါင်းလုပ်လုပ်ကာ Pillow Image Library (PIL) နှင့် `io` module ကို အသုံးပြု၍ ဒေသခံသိုလှောင်သည်။ ပုံဒေါင်းလုပ် အောင်မြင်ပါက True ပြန်လည်ပေးပြီး မအောင်မြင်ပါက False ပြန်လည်ပေးသည်။ request မအောင်မြင်ပါက error message ဖြင့် exception ကိုလည်း ထုတ်ပေးသည်။

### ၎င်းသည် မည်သို့ လုပ်ဆောင်သနည်း

`download_image` function သည် image_url (ဒေါင်းလုပ်လုပ်မည့် ပုံ URL) နှင့် save_path (ဒေါင်းလုပ်ပြီး သိမ်းဆည်းမည့် လမ်းကြောင်း) ဆိုသော parameter နှစ်ခုကို လက်ခံသည်။

function ၏ လုပ်ဆောင်ပုံမှာ -

requests.get method ဖြင့် image_url သို့ GET request တစ်ခု လုပ်ဆောင်သည်။ ၎င်းက URL မှ ပုံဒေတာကို ရယူသည်။

response.raise_for_status() က request အောင်မြင်မှုကို စစ်ဆေးသည်။ status code တွင် အမှားရှိပါက (ဥပမာ 404 - မတွေ့ရှိခြင်း) exception တစ်ခု ထုတ်ပေးမည်ဖြစ်သည်။ ထို့ကြောင့် request အောင်မြင်မှသာ ပုံဒေါင်းလုပ် ဆက်လက်လုပ်ဆောင်မည်ဖြစ်သည်။

ပုံဒေတာကို PIL (Python Imaging Library) ၏ Image.open method သို့ ပေးပို့သည်။ ၎င်းက ပုံဒေတာမှ Image object တစ်ခု ဖန်တီးပေးသည်။

image.save(save_path) က ပုံကို save_path တွင် သိမ်းဆည်းပေးသည်။ save_path တွင် ဖိုင်နာမည်နှင့် extension ပါဝင်ရမည်။

နောက်ဆုံးတွင် function သည် ပုံဒေါင်းလုပ် အောင်မြင်ကြောင်း True ပြန်ပေးသည်။ လုပ်ငန်းစဉ်အတွင်း exception တစ်ခု ဖြစ်ပေါ်ပါက exception ကို ဖမ်းယူပြီး အမှားစာတမ်းကို ပုံဖော်ပြသကာ False ပြန်ပေးသည်။

ဤ function သည် URL များမှ ပုံများကို ဒေါင်းလုပ်လုပ်၍ ဒေသခံသိုလှောင်ရာတွင် အသုံးဝင်သည်။ ဒေါင်းလုပ်လုပ်စဉ် ဖြစ်နိုင်သော အမှားများကို ကိုင်တွယ်ပေးကာ ဒေါင်းလုပ် အောင်မြင်မှုအခြေအနေကို ပြန်လည်အသိပေးသည်။

requests 라이ဘရယ်ရီသည် HTTP request များလုပ်ရန်၊ PIL 라이ဘရယ်ရီသည် ပုံများကို ကိုင်တွယ်ရန်၊ BytesIO class သည် ပုံဒေတာကို bytes stream အဖြစ် ကိုင်တွယ်ရန် အသုံးပြုသည်။

### နိဂုံးချုပ်

ဤ script သည် မက်ရှင်လေ့လာမှုအတွက် လိုအပ်သော ပုံများကို ဒေါင်းလုပ်လုပ်ကာ၊ ပုံဒေါင်းလုပ် မအောင်မြင်သော အတန်းများကို ဖယ်ရှားပြီး dataset ကို CSV ဖိုင်အဖြစ် သိမ်းဆည်းရန် အဆင်ပြေသော နည်းလမ်းတစ်ခုဖြစ်သည်။

### နမူနာ Script

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

### နမူနာ Code ဒေါင်းလုပ်လုပ်ရန်  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### နမူနာ Data Set  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။