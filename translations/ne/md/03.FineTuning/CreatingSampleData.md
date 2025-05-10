<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:23:24+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "ne"
}
-->
# Hugging Face बाट DataSet र सम्बन्धित छविहरू डाउनलोड गरेर Image Data Set बनाउने


### अवलोकन

यो स्क्रिप्टले आवश्यक छविहरू डाउनलोड गरेर, जहाँ छवि डाउनलोड असफल हुन्छ त्यस्ता पङ्क्तिहरू फिल्टर गरी, र dataset लाई CSV फाइलको रूपमा सुरक्षित गरी मशीन लर्निंगका लागि dataset तयार पार्छ।

### आवश्यकताहरू

यो स्क्रिप्ट चलाउनुअघि, तलका लाइब्रेरीहरू इन्स्टल गरिएको सुनिश्चित गर्नुहोस्: `Pandas`, `Datasets`, `requests`, `PIL`, र `io`। साथै, लाइन २ मा `'Insert_Your_Dataset'` लाई Hugging Face बाट तपाईंको dataset को नामले प्रतिस्थापन गर्नुपर्नेछ।

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

स्क्रिप्टले तलका चरणहरू गर्दछ:

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` फङ्सन प्रयोग गरी Hugging Face बाट dataset डाउनलोड गर्छ। `download_image()` फङ्सनले URL बाट छवि डाउनलोड गरी Pillow Image Library (PIL) र `io` मोड्युलको प्रयोग गरी स्थानीय रूपमा सुरक्षित गर्छ। यदि छवि सफलतापूर्वक डाउनलोड भयो भने True फर्काउँछ, नभए False। अनुरोध असफल भएमा यो फङ्सनले त्रुटि सन्देशसहित exception पनि उठाउँछ।

### यो कसरी काम गर्छ

download_image फङ्सनले दुईवटा प्यारामिटर लिन्छ: image_url, जुन डाउनलोड गर्नुपर्ने छवि URL हो, र save_path, जहाँ डाउनलोड गरिएको छवि सुरक्षित गरिनेछ।

फङ्सनले यसरी काम गर्छ:

यो requests.get विधि प्रयोग गरी image_url मा GET अनुरोध गर्छ र URL बाट छवि डेटा प्राप्त गर्छ।

response.raise_for_status() ले अनुरोध सफल भयो कि भएन भनेर जाँच गर्छ। यदि response status code मा कुनै त्रुटि (जस्तै 404 - फेला परेन) छ भने exception उठाउँछ। यसले सुनिश्चित गर्छ कि छवि डाउनलोड गर्ने काम अनुरोध सफल हुँदा मात्र अगाडि बढोस्।

छवि डेटा PIL (Python Imaging Library) को Image.open विधिमा पठाइन्छ जसले Image वस्तु सिर्जना गर्छ।

image.save(save_path) ले छविलाई दिइएको save_path मा सुरक्षित गर्छ। save_path मा फाइल नाम र एक्सटेन्सन समावेश हुनुपर्छ।

अन्त्यमा, फङ्सनले True फर्काउँछ जुनले छवि सफलतापूर्वक डाउनलोड र सुरक्षित भएको जनाउँछ। कुनै पनि exception आयो भने, त्यो समातेर त्रुटि सन्देश छाप्छ र False फर्काउँछ।

यो फङ्सन URL बाट छवि डाउनलोड गरी स्थानीय रूपमा सुरक्षित गर्न उपयोगी छ। यसले डाउनलोड प्रक्रियामा सम्भावित त्रुटिहरू सम्हाल्छ र डाउनलोड सफल भयो कि भएन भन्ने जानकारी दिन्छ।

ध्यान दिनुहोस् requests लाइब्रेरी HTTP अनुरोध गर्न प्रयोग हुन्छ, PIL लाइब्रेरी छविहरूसँग काम गर्न प्रयोग हुन्छ, र BytesIO वर्ग छवि डेटा बाइट्सको स्ट्रिमको रूपमा सम्हाल्न प्रयोग हुन्छ।



### निष्कर्ष

यो स्क्रिप्टले आवश्यक छविहरू डाउनलोड गरी, डाउनलोड असफल भएका पङ्क्तिहरू फिल्टर गरी, र dataset लाई CSV फाइलको रूपमा सुरक्षित गरेर मशीन लर्निंगका लागि dataset तयार पार्ने सजिलो तरिका प्रदान गर्छ।

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

### नमूना Data Set  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा असत्यताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याहरूको लागि हामी जिम्मेवार छैनौं।