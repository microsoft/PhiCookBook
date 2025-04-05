<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "44a77501fe39a2eb2b776dfdf9953b67",
  "translation_date": "2025-04-04T18:47:57+00:00",
  "source_file": "md\\03.FineTuning\\CreatingSampleData.md",
  "language_code": "hi"
}
-->
# Hugging Face से डेटा सेट और संबंधित छवियों को डाउनलोड करके इमेज डेटा सेट तैयार करें

### अवलोकन

यह स्क्रिप्ट मशीन लर्निंग के लिए एक डेटा सेट तैयार करती है। इसमें आवश्यक छवियों को डाउनलोड करना, उन पंक्तियों को हटाना जहां छवि डाउनलोड विफल होती है, और डेटा सेट को CSV फ़ाइल के रूप में सहेजना शामिल है।

### आवश्यकताएँ

इस स्क्रिप्ट को चलाने से पहले, सुनिश्चित करें कि आपके पास निम्न लाइब्रेरीज़ इंस्टॉल हैं: `Pandas`, `Datasets`, `requests`, `PIL`, और `io`। आपको लाइन 2 में `'Insert_Your_Dataset'` को Hugging Face से अपने डेटा सेट के नाम से बदलने की आवश्यकता होगी।

आवश्यक लाइब्रेरीज़:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### कार्यक्षमता

यह स्क्रिप्ट निम्नलिखित चरणों को अंजाम देती है:

1. Hugging Face से `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` का उपयोग करके डेटा सेट डाउनलोड करती है। `download_image()` फ़ंक्शन URL से छवि डाउनलोड करता है और इसे स्थानीय रूप से Pillow Image Library (PIL) और `io` मॉड्यूल का उपयोग करके सहेजता है। यदि छवि सफलतापूर्वक डाउनलोड होती है, तो यह True लौटाता है; अन्यथा False। यदि अनुरोध विफल होता है, तो फ़ंक्शन त्रुटि संदेश के साथ एक अपवाद उठाता है।

### यह कैसे काम करता है

`download_image` फ़ंक्शन दो पैरामीटर लेता है: `image_url`, जो डाउनलोड की जाने वाली छवि का URL है, और `save_path`, जो वह स्थान है जहां डाउनलोड की गई छवि सहेजी जाएगी।

यहाँ बताया गया है कि यह फ़ंक्शन कैसे काम करता है:

- यह `requests.get` विधि का उपयोग करके `image_url` पर एक GET अनुरोध करता है। यह URL से छवि डेटा प्राप्त करता है।
- `response.raise_for_status()` पंक्ति जांचती है कि क्या अनुरोध सफल था। यदि प्रतिक्रिया स्थिति कोड किसी त्रुटि को इंगित करता है (जैसे, 404 - Not Found), तो यह एक अपवाद उठाएगा। यह सुनिश्चित करता है कि हम केवल तभी छवि डाउनलोड करना जारी रखें जब अनुरोध सफल हो।
- छवि डेटा को PIL (Python Imaging Library) मॉड्यूल से `Image.open` विधि में पास किया जाता है। यह विधि छवि डेटा से एक Image ऑब्जेक्ट बनाती है।
- `image.save(save_path)` पंक्ति छवि को निर्दिष्ट `save_path` पर सहेजती है। `save_path` में इच्छित फ़ाइल नाम और एक्सटेंशन शामिल होना चाहिए।
- अंत में, फ़ंक्शन True लौटाता है ताकि यह संकेत दिया जा सके कि छवि सफलतापूर्वक डाउनलोड और सहेजी गई। यदि प्रक्रिया के दौरान कोई अपवाद होता है, तो यह अपवाद को पकड़ता है, विफलता को इंगित करने वाला एक त्रुटि संदेश प्रिंट करता है, और False लौटाता है।

यह फ़ंक्शन URL से छवियाँ डाउनलोड करने और उन्हें स्थानीय रूप से सहेजने के लिए उपयोगी है। यह डाउनलोड प्रक्रिया के दौरान संभावित त्रुटियों को संभालता है और डाउनलोड सफल हुआ या नहीं, इसके बारे में प्रतिक्रिया प्रदान करता है।

यह ध्यान देने योग्य है कि HTTP अनुरोध करने के लिए `requests` लाइब्रेरी का उपयोग किया जाता है, छवियों पर काम करने के लिए `PIL` लाइब्रेरी का उपयोग किया जाता है, और `BytesIO` क्लास का उपयोग छवि डेटा को बाइट्स की स्ट्रीम के रूप में संभालने के लिए किया जाता है।

### निष्कर्ष

यह स्क्रिप्ट मशीन लर्निंग के लिए एक डेटा सेट तैयार करने का एक सुविधाजनक तरीका प्रदान करती है। इसमें आवश्यक छवियों को डाउनलोड करना, उन पंक्तियों को हटाना जहां छवि डाउनलोड विफल होती है, और डेटा सेट को CSV फ़ाइल के रूप में सहेजना शामिल है।

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
[नया डेटा सेट स्क्रिप्ट जनरेट करें](../../../../code/04.Finetuning/generate_dataset.py)

### नमूना डेटा सेट
[फाइनट्यूनिंग के LORA उदाहरण से नमूना डेटा सेट](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।