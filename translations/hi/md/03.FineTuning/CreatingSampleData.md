<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:46:33+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "hi"
}
-->
# Hugging Face से DataSet और संबंधित छवियाँ डाउनलोड करके इमेज डेटा सेट बनाना


### अवलोकन

यह स्क्रिप्ट मशीन लर्निंग के लिए एक डेटासेट तैयार करती है, जिसमें आवश्यक छवियाँ डाउनलोड करना, उन पंक्तियों को फ़िल्टर करना जहाँ छवि डाउनलोड विफल होती है, और डेटासेट को CSV फ़ाइल के रूप में सहेजना शामिल है।

### आवश्यकताएँ

इस स्क्रिप्ट को चलाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित लाइब्रेरीज़ इंस्टॉल हैं: `Pandas`, `Datasets`, `requests`, `PIL`, और `io`। आपको लाइन 2 में `'Insert_Your_Dataset'` को Hugging Face से अपने डेटासेट के नाम से बदलना होगा।

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

स्क्रिप्ट निम्नलिखित चरणों को पूरा करती है:

1. `load_dataset()` फ़ंक्शन का उपयोग करके Hugging Face से डेटासेट डाउनलोड करती है।
2. `to_pandas()` मेथड का उपयोग करके Hugging Face डेटासेट को Pandas DataFrame में बदलती है ताकि इसे आसानी से संभाला जा सके।
3. डेटासेट और छवियों को सहेजने के लिए डायरेक्टरी बनाती है।
4. DataFrame की प्रत्येक पंक्ति पर जाकर, कस्टम `download_image()` फ़ंक्शन का उपयोग करके छवि डाउनलोड करती है, और जहाँ डाउनलोड विफल होता है उन पंक्तियों को फ़िल्टर कर नए DataFrame `filtered_rows` में जोड़ती है।
5. फ़िल्टर की गई पंक्तियों के साथ नया DataFrame बनाती है और इसे CSV फ़ाइल के रूप में डिस्क पर सहेजती है।
6. एक संदेश प्रिंट करती है जो बताता है कि डेटासेट और छवियाँ कहाँ सहेजी गई हैं।

### कस्टम फ़ंक्शन

`download_image()` फ़ंक्शन एक URL से छवि डाउनलोड करता है और इसे स्थानीय रूप से Pillow Image Library (PIL) और `io` मॉड्यूल का उपयोग करके सहेजता है। यदि छवि सफलतापूर्वक डाउनलोड हो जाती है तो यह True लौटाता है, अन्यथा False। यदि अनुरोध विफल होता है तो यह त्रुटि संदेश के साथ एक exception भी उठाता है।

### यह कैसे काम करता है

`download_image` फ़ंक्शन दो पैरामीटर लेता है: image_url, जो डाउनलोड की जाने वाली छवि का URL है, और save_path, जहाँ डाउनलोड की गई छवि सहेजी जाएगी।

फ़ंक्शन इस प्रकार काम करता है:

यह requests.get मेथड का उपयोग करके image_url पर GET अनुरोध करता है। इससे URL से छवि डेटा प्राप्त होता है।

`response.raise_for_status()` यह जांचता है कि अनुरोध सफल था या नहीं। यदि प्रतिक्रिया स्थिति कोड में कोई त्रुटि होती है (जैसे 404 - Not Found), तो यह exception उठाएगा। इससे सुनिश्चित होता है कि हम केवल तभी छवि डाउनलोड करें जब अनुरोध सफल हो।

फिर छवि डेटा को PIL (Python Imaging Library) के Image.open मेथड को दिया जाता है। यह मेथड छवि डेटा से एक Image ऑब्जेक्ट बनाता है।

`image.save(save_path)` लाइन छवि को निर्दिष्ट save_path पर सहेजती है। save_path में फ़ाइल का नाम और एक्सटेंशन शामिल होना चाहिए।

अंत में, फ़ंक्शन True लौटाता है यह दर्शाने के लिए कि छवि सफलतापूर्वक डाउनलोड और सहेजी गई। यदि प्रक्रिया के दौरान कोई exception होता है, तो इसे पकड़ता है, विफलता का संदेश प्रिंट करता है, और False लौटाता है।

यह फ़ंक्शन URL से छवियाँ डाउनलोड करने और उन्हें स्थानीय रूप से सहेजने के लिए उपयोगी है। यह डाउनलोड प्रक्रिया के दौरान संभावित त्रुटियों को संभालता है और डाउनलोड की सफलता के बारे में प्रतिक्रिया देता है।

यह ध्यान देने योग्य है कि requests लाइब्रेरी HTTP अनुरोध करने के लिए, PIL लाइब्रेरी छवियों के साथ काम करने के लिए, और BytesIO क्लास छवि डेटा को बाइट्स के स्ट्रीम के रूप में संभालने के लिए उपयोग की जाती है।


### निष्कर्ष

यह स्क्रिप्ट आवश्यक छवियाँ डाउनलोड करके, उन पंक्तियों को फ़िल्टर करके जहाँ छवि डाउनलोड विफल होती है, और डेटासेट को CSV फ़ाइल के रूप में सहेजकर मशीन लर्निंग के लिए डेटासेट तैयार करने का एक सुविधाजनक तरीका प्रदान करती है।

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

### नमूना डेटासेट  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।