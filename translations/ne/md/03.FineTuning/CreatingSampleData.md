<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:47:15+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ne"
}
-->
# Hugging Face बाट DataSet र सम्बन्धित तस्बिरहरू डाउनलोड गरेर Image Data Set तयार पार्ने

### अवलोकन

यो स्क्रिप्टले आवश्यक तस्बिरहरू डाउनलोड गरेर, तस्बिर डाउनलोड असफल भएका पङ्क्तिहरू फिल्टर गरेर, र डेटासेटलाई CSV फाइलको रूपमा सुरक्षित गरेर मेशिन लर्निङका लागि डेटासेट तयार पार्छ।

### पूर्वआवश्यकताहरू

यो स्क्रिप्ट चलाउनु अघि, तलका लाइब्रेरीहरू इन्स्टल गरिएको हुनुपर्छ: `Pandas`, `Datasets`, `requests`, `PIL`, र `io`। साथै, लाइन २ मा रहेको `'Insert_Your_Dataset'` लाई Hugging Face बाट तपाईंको डेटासेटको नामले प्रतिस्थापन गर्नुपर्नेछ।

आवश्यक लाइब्रेरीहरू:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### कार्यक्षमता

यो स्क्रिप्टले तलका चरणहरू पूरा गर्छ:

1. `load_dataset()` फंक्शन प्रयोग गरी Hugging Face बाट डेटासेट डाउनलोड गर्छ।
2. `to_pandas()` मेथड प्रयोग गरी Hugging Face डेटासेटलाई सजिलो रूपमा व्यवस्थापन गर्न Pandas DataFrame मा रूपान्तरण गर्छ।
3. डेटासेट र तस्बिरहरू सुरक्षित गर्न डाइरेक्टरीहरू बनाउँछ।
4. DataFrame को प्रत्येक पङ्क्तिमा गएर, कस्टम `download_image()` फंक्शन प्रयोग गरी तस्बिर डाउनलोड गर्न खोज्छ र जहाँ डाउनलोड असफल हुन्छ, ती पङ्क्तिहरूलाई फिल्टर गरेर नयाँ DataFrame `filtered_rows` मा थप्छ।
5. फिल्टर गरिएका पङ्क्तिहरूको नयाँ DataFrame बनाएर यसलाई CSV फाइलको रूपमा डिस्कमा सुरक्षित गर्छ।
6. डेटासेट र तस्बिरहरू कहाँ सुरक्षित गरिएको छ भन्ने सन्देश प्रिन्ट गर्छ।

### कस्टम फंक्शन

`download_image()` फंक्शनले URL बाट तस्बिर डाउनलोड गरी Pillow Image Library (PIL) र `io` मोड्युल प्रयोग गरेर स्थानीय रूपमा सुरक्षित गर्छ। यदि तस्बिर सफलतापूर्वक डाउनलोड भयो भने True र अन्यथा False फर्काउँछ। अनुरोध असफल हुँदा यो फंक्शनले त्रुटि सन्देशसहित अपवाद पनि फ्याँक्छ।

### यो कसरी काम गर्छ

`download_image` फंक्शनले दुईवटा प्यारामिटर लिन्छ: image_url, जुन डाउनलोड गर्नुपर्ने तस्बिरको URL हो, र save_path, जहाँ डाउनलोड गरिएको तस्बिर सुरक्षित गरिनेछ।

फंक्शनको काम गर्ने तरिका यसप्रकार छ:

यसले requests.get मेथड प्रयोग गरी image_url मा GET अनुरोध गर्छ। यसले URL बाट तस्बिरको डाटा ल्याउँछ।

response.raise_for_status() ले अनुरोध सफल भयो कि भएन जाँच गर्छ। यदि प्रतिक्रिया स्थिति कोडले त्रुटि जनाउँछ (जस्तै ४०४ - फेला परेन), भने अपवाद फ्याँकिन्छ। यसले सुनिश्चित गर्छ कि अनुरोध सफल भए मात्र तस्बिर डाउनलोड गरिन्छ।

तस्बिरको डाटा PIL (Python Imaging Library) को Image.open मेथडमा पठाइन्छ। यसले तस्बिर डाटाबाट Image वस्तु बनाउँछ।

image.save(save_path) ले तस्बिरलाई निर्दिष्ट गरिएको save_path मा सुरक्षित गर्छ। save_path मा फाइलको नाम र एक्सटेन्सन समावेश हुनुपर्छ।

अन्तमा, फंक्शनले तस्बिर सफलतापूर्वक डाउनलोड र सुरक्षित भएको जनाउन True फर्काउँछ। यदि कुनै अपवाद आउँछ भने, त्यो समातेर त्रुटि सन्देश प्रिन्ट गर्छ र False फर्काउँछ।

यो फंक्शन URL बाट तस्बिर डाउनलोड गरी स्थानीय रूपमा सुरक्षित गर्न उपयोगी छ। यसले डाउनलोड प्रक्रियामा सम्भावित त्रुटिहरूलाई सम्हाल्छ र सफलताबारे प्रतिक्रिया दिन्छ।

ध्यान दिनुहोस् कि requests लाइब्रेरी HTTP अनुरोध गर्न प्रयोग हुन्छ, PIL लाइब्रेरी तस्बिरसँग काम गर्न प्रयोग हुन्छ, र BytesIO क्लासले तस्बिर डाटालाई बाइट्सको स्ट्रिमको रूपमा सम्हाल्छ।

### निष्कर्ष

यो स्क्रिप्टले आवश्यक तस्बिरहरू डाउनलोड गरेर, तस्बिर डाउनलोड असफल भएका पङ्क्तिहरू फिल्टर गरेर, र डेटासेटलाई CSV फाइलको रूपमा सुरक्षित गरेर मेशिन लर्निङका लागि सजिलो तरिकाले डेटासेट तयार पार्न मद्दत गर्छ।

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
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।