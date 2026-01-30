# Hugging Face वरून DataSet आणि संबंधित प्रतिमा डाउनलोड करून इमेज डेटा सेट तयार करा


### आढावा

हा स्क्रिप्ट मशीन लर्निंगसाठी डेटा सेट तयार करतो, ज्यामध्ये आवश्यक प्रतिमा डाउनलोड केल्या जातात, ज्या रकाने प्रतिमा डाउनलोड करण्यात अयशस्वी होतात त्या फिल्टर केल्या जातात, आणि नंतर डेटा सेट CSV फाईल म्हणून जतन केला जातो.

### पूर्वअट

हा स्क्रिप्ट चालवण्यापूर्वी, खालील लायब्ररी इन्स्टॉल असल्याची खात्री करा: `Pandas`, `Datasets`, `requests`, `PIL`, आणि `io`. तसेच, लाइन 2 मध्ये `'Insert_Your_Dataset'` या ठिकाणी तुमच्या Hugging Face मधील डेटा सेटचे नाव टाका.

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

1. `load_dataset()` फंक्शन वापरून Hugging Face वरून डेटा सेट डाउनलोड करतो.
2. `to_pandas()` मेथड वापरून Hugging Face डेटा सेटला Pandas DataFrame मध्ये रूपांतरित करतो, ज्यामुळे हाताळणी सोपी होते.
3. डेटा सेट आणि प्रतिमा जतन करण्यासाठी फोल्डर तयार करतो.
4. DataFrame मधील प्रत्येक रकान्यावरून फेरफटका मारून, कस्टम `download_image()` फंक्शन वापरून प्रतिमा डाउनलोड करतो, आणि ज्या रकान्यांमध्ये प्रतिमा डाउनलोड अयशस्वी होते त्या रकाने फिल्टर करून नवीन DataFrame `filtered_rows` मध्ये जोडतो.
5. फिल्टर केलेल्या रकान्यांसह नवीन DataFrame तयार करतो आणि तो CSV फाईल म्हणून डिस्कवर जतन करतो.
6. डेटा सेट आणि प्रतिमा कुठे जतन झाल्या आहेत हे सूचित करणारा संदेश प्रिंट करतो.

### कस्टम फंक्शन

`download_image()` फंक्शन URL वरून प्रतिमा डाउनलोड करते आणि Pillow Image Library (PIL) आणि `io` मॉड्यूल वापरून स्थानिकपणे जतन करते. प्रतिमा यशस्वीपणे डाउनलोड झाली तर True परत करते, अन्यथा False. विनंती अयशस्वी झाल्यास, त्रुटी संदेशासह अपवाद उचलतो.

### हे कसे कार्य करते

`download_image` फंक्शनला दोन पॅरामीटर्स दिले जातात: image_url, म्हणजे डाउनलोड करायची प्रतिमेची URL, आणि save_path, म्हणजे प्रतिमा जतन करण्याचा मार्ग.

फंक्शन कसे कार्य करते:

requests.get मेथड वापरून image_url वर GET विनंती केली जाते. यामुळे URL वरून प्रतिमेचा डेटा मिळतो.

response.raise_for_status() ही ओळ तपासते की विनंती यशस्वी झाली आहे का. जर प्रतिसाद स्थिती कोडमध्ये त्रुटी असेल (उदा. 404 - सापडले नाही), तर अपवाद उचलला जातो. यामुळे फक्त यशस्वी विनंती झाल्यासच प्रतिमा डाउनलोड करण्यास पुढे जावे.

प्रतिमा डेटा नंतर PIL (Python Imaging Library) मधील Image.open मेथडला दिला जातो. ही मेथड प्रतिमा डेटावरून Image ऑब्जेक्ट तयार करते.

image.save(save_path) ही ओळ प्रतिमा दिलेल्या save_path वर जतन करते. save_path मध्ये आवश्यक फाईल नाव आणि एक्सटेंशन असावे.

शेवटी, फंक्शन True परत करते जे दर्शवते की प्रतिमा यशस्वीपणे डाउनलोड आणि जतन झाली आहे. जर कोणताही अपवाद आला, तर तो पकडून त्रुटी संदेश प्रिंट करतो आणि False परत करतो.

हा फंक्शन URL वरून प्रतिमा डाउनलोड करण्यासाठी आणि स्थानिकपणे जतन करण्यासाठी उपयुक्त आहे. तो डाउनलोड प्रक्रियेदरम्यान संभाव्य त्रुटी हाताळतो आणि डाउनलोड यशस्वी झाला की नाही याची माहिती देतो.

requests लायब्ररी HTTP विनंत्या करण्यासाठी वापरली जाते, PIL लायब्ररी प्रतिमांसोबत काम करण्यासाठी वापरली जाते, आणि BytesIO वर्ग प्रतिमा डेटाला बाइट्सच्या प्रवाहाप्रमाणे हाताळण्यासाठी वापरला जातो.



### निष्कर्ष

हा स्क्रिप्ट आवश्यक प्रतिमा डाउनलोड करून, प्रतिमा डाउनलोड अयशस्वी झालेल्या रकान्यांना फिल्टर करून, आणि डेटा सेट CSV फाईल म्हणून जतन करून मशीन लर्निंगसाठी डेटा सेट तयार करण्याचा सोयीस्कर मार्ग प्रदान करतो.

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

### नमुना कोड डाउनलोड  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### नमुना डेटा सेट  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.