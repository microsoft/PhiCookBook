<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-08T05:14:19+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "hi"
}
-->
# Hugging Face से DataSet और संबंधित छवियों को डाउनलोड करके इमेज डेटा सेट बनाना


### अवलोकन

यह स्क्रिप्ट मशीन लर्निंग के लिए एक डेटासेट तैयार करती है, जिसमें आवश्यक छवियों को डाउनलोड करना, उन पंक्तियों को हटाना जहां छवि डाउनलोड विफल होती है, और डेटासेट को CSV फाइल के रूप में सेव करना शामिल है।

### आवश्यकताएँ

इस स्क्रिप्ट को चलाने से पहले, सुनिश्चित करें कि निम्नलिखित लाइब्रेरी इंस्टॉल हैं: `Pandas`, `Datasets`, `requests`, `PIL`, और `io`। साथ ही, लाइन 2 में `'Insert_Your_Dataset'` को Hugging Face से अपने डेटासेट के नाम से बदलना होगा।

आवश्यक लाइब्रेरी:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### कार्यप्रणाली

स्क्रिप्ट निम्नलिखित चरण करता है:

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` फ़ंक्शन Hugging Face से डेटासेट डाउनलोड करता है। यह फ़ंक्शन URL से छवि डाउनलोड करता है और उसे Pillow Image Library (PIL) और `io` मॉड्यूल का उपयोग करके लोकली सेव करता है। यदि छवि सफलतापूर्वक डाउनलोड हो जाती है तो यह True लौटाता है, अन्यथा False। जब अनुरोध विफल होता है तो यह त्रुटि संदेश के साथ एक exception भी फेंकता है।

### यह कैसे काम करता है

download_image फ़ंक्शन दो पैरामीटर लेता है: image_url, जो डाउनलोड की जाने वाली छवि का URL है, और save_path, जहां डाउनलोड की गई छवि को सेव किया जाएगा।

फ़ंक्शन का कार्य करने का तरीका इस प्रकार है:

यह requests.get मेथड का उपयोग करके image_url पर GET अनुरोध करता है। यह URL से छवि डेटा प्राप्त करता है।

response.raise_for_status() लाइन जांचती है कि अनुरोध सफल रहा या नहीं। यदि प्रतिक्रिया स्थिति कोड में कोई त्रुटि होती है (जैसे 404 - Not Found), तो यह exception फेंकता है। इससे यह सुनिश्चित होता है कि हम केवल तभी छवि डाउनलोड करेंगे जब अनुरोध सफल हो।

छवि डेटा को PIL (Python Imaging Library) के Image.open मेथड को दिया जाता है। यह मेथड छवि डेटा से एक Image ऑब्जेक्ट बनाता है।

image.save(save_path) लाइन छवि को निर्दिष्ट save_path पर सेव करता है। save_path में फाइल का नाम और एक्सटेंशन शामिल होना चाहिए।

अंत में, फ़ंक्शन True लौटाता है यह दर्शाने के लिए कि छवि सफलतापूर्वक डाउनलोड और सेव हो गई। यदि प्रक्रिया के दौरान कोई exception होता है, तो वह उसे पकड़ता है, एक त्रुटि संदेश प्रिंट करता है जो विफलता को दर्शाता है, और False लौटाता है।

यह फ़ंक्शन URL से छवियां डाउनलोड करने और उन्हें लोकली सेव करने के लिए उपयोगी है। यह डाउनलोड प्रक्रिया के दौरान संभावित त्रुटियों को संभालता है और बताता है कि डाउनलोड सफल रहा या नहीं।

ध्यान देने योग्य है कि HTTP अनुरोध करने के लिए requests लाइब्रेरी का उपयोग किया जाता है, छवियों के साथ काम करने के लिए PIL लाइब्रेरी का उपयोग होता है, और BytesIO क्लास का उपयोग छवि डेटा को बाइट्स के स्ट्रीम के रूप में संभालने के लिए किया जाता है।



### निष्कर्ष

यह स्क्रिप्ट मशीन लर्निंग के लिए आवश्यक छवियों को डाउनलोड करके, जहां छवि डाउनलोड विफल होती है उन पंक्तियों को हटाकर, और डेटासेट को CSV फाइल के रूप में सेव करके एक सुविधाजनक तरीका प्रदान करती है।

### नमूना स्क्रिप्ट

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

### नमूना कोड डाउनलोड  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### नमूना डेटा सेट  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।