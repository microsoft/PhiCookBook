<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-05-09T20:23:15+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "mr"
}
-->
# Hugging Face कडून DataSet आणि संबंधित प्रतिमा डाउनलोड करून Image Data Set तयार करा


### आढावा

हा स्क्रिप्ट मशीन लर्निंगसाठी dataset तयार करतो, आवश्यक प्रतिमा डाउनलोड करतो, ज्या ओळींमध्ये प्रतिमा डाउनलोड अयशस्वी होतात त्या फिल्टर करतो, आणि dataset CSV फाईल म्हणून जतन करतो.

### पूर्वअटी

हा स्क्रिप्ट चालवण्यापूर्वी खालील लायब्ररी इंस्टॉल असाव्यात: `Pandas`, `Datasets`, `requests`, `PIL`, आणि `io`. तसेच, लाइन 2 मध्ये `'Insert_Your_Dataset'` या ठिकाणी तुमच्या Hugging Face मधील dataset चे नाव टाकावे लागेल.

आवश्यक लायब्ररी:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### कार्यप्रणाली

हा स्क्रिप्ट खालील टप्पे पार पाडतो:

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` फंक्शन वापरून Hugging Face कडून dataset डाउनलोड करतो. `download_image()` फंक्शन URL वरून प्रतिमा डाउनलोड करते आणि Pillow Image Library (PIL) आणि `io` मॉड्यूल वापरून ती स्थानिकरित्या जतन करते. प्रतिमा यशस्वीपणे डाउनलोड झाली तर True परत करते, अन्यथा False. जर विनंती अयशस्वी झाली तर हे फंक्शन त्रुटी संदेशासह exception देखील उचलते.

### हे कसे कार्य करते

`download_image` फंक्शनला दोन पॅरामीटर्स लागतात: image_url, म्हणजे डाउनलोड करायची प्रतिमेची URL, आणि save_path, म्हणजे डाउनलोड केलेली प्रतिमा ज्या ठिकाणी जतन करायची आहे तो मार्ग.

फंक्शन कसे कार्य करते:

सुरुवातीला requests.get पद्धत वापरून image_url वर GET विनंती करते. त्यामुळे URL वरून प्रतिमेचा डेटा मिळतो.

`response.raise_for_status()` ओळ तपासते की विनंती यशस्वी झाली आहे का. जर प्रतिसादाचा status code त्रुटी दर्शवित असेल (उदा. 404 - Not Found), तर exception उचलले जाईल. यामुळे प्रतिमा फक्त यशस्वी विनंती झाल्यासच डाउनलोड होईल.

प्रतिमा डेटा नंतर PIL (Python Imaging Library) च्या Image.open पद्धतीला दिला जातो, ज्यामुळे Image ऑब्जेक्ट तयार होतो.

`image.save(save_path)` ओळ प्रतिमा दिलेल्या save_path वर जतन करते. save_path मध्ये फाईलचे नाव आणि एक्स्टेंशन असणे आवश्यक आहे.

शेवटी, फंक्शन True परत करते जे दर्शविते की प्रतिमा यशस्वीपणे डाउनलोड आणि जतन झाली आहे. जर कोणतीही त्रुटी आली तर ती पकडून त्रुटी संदेश प्रिंट करते आणि False परत करते.

हा फंक्शन URL वरून प्रतिमा डाउनलोड करून स्थानिकरित्या जतन करण्यासाठी उपयुक्त आहे. तो डाउनलोड प्रक्रियेत येणाऱ्या संभाव्य त्रुटी हाताळतो आणि डाउनलोड यशस्वी झाला की नाही याबाबत फीडबॅक देतो.

यासाठी requests लायब्ररी HTTP विनंत्या करण्यासाठी, PIL लायब्ररी प्रतिमांसोबत काम करण्यासाठी, आणि BytesIO वर्ग प्रतिमा डेटा बाइट्सच्या स्ट्रीमसारखा हाताळण्यासाठी वापरला जातो.



### निष्कर्ष

हा स्क्रिप्ट मशीन लर्निंगसाठी dataset तयार करण्याचा सोयीस्कर मार्ग प्रदान करतो ज्यात आवश्यक प्रतिमा डाउनलोड करणे, प्रतिमा डाउनलोड अयशस्वी झालेल्या ओळी फिल्टर करणे, आणि dataset CSV फाईल म्हणून जतन करणे यांचा समावेश आहे.

### नमुना स्क्रिप्ट

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

### नमुना कोड डाउनलोड करा  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### नमुना Data Set  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**सूचना**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेत फरक असू शकतो. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता, व्यावसायिक मानवी भाषांतर करण्याचा सल्ला दिला जातो. या भाषांतराच्या वापरामुळे झालेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागीसाठी आम्ही जबाबदार नाही.