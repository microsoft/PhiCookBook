# Sukurkite vaizdų duomenų rinkinį atsisiųsdami duomenų rinkinį iš Hugging Face ir susijusius vaizdus

### Apžvalga

Šis scenarijus paruošia duomenų rinkinį mašininio mokymosi tikslams, atsisiųsdamas reikalingus vaizdus, pašalindamas eilutes, kuriose nepavyksta atsisiųsti vaizdų, ir išsaugodamas duomenų rinkinį CSV formato faile.

### Būtinos sąlygos

Prieš vykdydami šį scenarijų, įsitikinkite, kad įdiegėte šias bibliotekas: `Pandas`, `Datasets`, `requests`, `PIL` ir `io`. Taip pat turėsite pakeisti `'Insert_Your_Dataset'` 2 eilutėje savo duomenų rinkinio pavadinimu iš Hugging Face.

Reikalingos bibliotekos:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalumas

Scenarijus atlieka šiuos veiksmus:

1. Atsisiunčia duomenų rinkinį iš Hugging Face naudojant funkciją `load_dataset()`.
2. Konvertuoja Hugging Face duomenų rinkinį į Pandas DataFrame, kad būtų lengviau manipuliuoti, naudojant metodą `to_pandas()`.
3. Sukuria katalogus duomenų rinkiniui ir vaizdams išsaugoti.
4. Pašalina eilutes, kuriose nepavyksta atsisiųsti vaizdų, iteruojant per kiekvieną DataFrame eilutę, atsisiunčiant vaizdą naudojant pritaikytą funkciją `download_image()` ir pridedant filtruotą eilutę į naują DataFrame, pavadintą `filtered_rows`.
5. Sukuria naują DataFrame su filtruotomis eilutėmis ir išsaugo jį diske kaip CSV failą.
6. Išspausdina pranešimą, nurodantį, kur buvo išsaugotas duomenų rinkinys ir vaizdai.

### Pritaikyta funkcija

Funkcija `download_image()` atsisiunčia vaizdą iš URL ir išsaugo jį lokaliai, naudodama Pillow vaizdų biblioteką (PIL) ir modulį `io`. Ji grąžina True, jei vaizdas sėkmingai atsisiųstas, ir False, jei ne. Funkcija taip pat išmeta išimtį su klaidos pranešimu, jei užklausa nepavyksta.

### Kaip tai veikia

Funkcija `download_image` priima du parametrus: `image_url`, kuris yra vaizdo URL, kurį reikia atsisiųsti, ir `save_path`, kuris yra kelias, kur bus išsaugotas atsisiųstas vaizdas.

Štai kaip veikia funkcija:

1. Ji pradeda GET užklausą į `image_url` naudodama metodą `requests.get`. Tai leidžia gauti vaizdo duomenis iš URL.
2. `response.raise_for_status()` patikrina, ar užklausa buvo sėkminga. Jei atsakymo statuso kodas rodo klaidą (pvz., 404 - Nerasta), bus išmesta išimtis. Tai užtikrina, kad tęsiame vaizdo atsisiuntimą tik tuo atveju, jei užklausa buvo sėkminga.
3. Vaizdo duomenys perduodami į metodą `Image.open` iš PIL (Python Imaging Library) modulio. Šis metodas sukuria vaizdo objektą iš vaizdo duomenų.
4. `image.save(save_path)` išsaugo vaizdą nurodytame `save_path`. `save_path` turėtų apimti norimą failo pavadinimą ir plėtinį.
5. Galiausiai funkcija grąžina True, nurodydama, kad vaizdas buvo sėkmingai atsisiųstas ir išsaugotas. Jei proceso metu įvyksta kokia nors išimtis, ji ją pagauna, išspausdina klaidos pranešimą, nurodantį nesėkmę, ir grąžina False.

Ši funkcija yra naudinga atsisiunčiant vaizdus iš URL ir išsaugant juos lokaliai. Ji tvarko galimas klaidas atsisiuntimo proceso metu ir pateikia grįžtamąjį ryšį apie tai, ar atsisiuntimas buvo sėkmingas.

Verta paminėti, kad biblioteka `requests` naudojama HTTP užklausoms atlikti, biblioteka `PIL` naudojama darbui su vaizdais, o klasė `BytesIO` naudojama vaizdo duomenims tvarkyti kaip baitų srautui.

### Išvada

Šis scenarijus suteikia patogų būdą paruošti duomenų rinkinį mašininio mokymosi tikslams, atsisiųsdamas reikalingus vaizdus, pašalindamas eilutes, kuriose nepavyksta atsisiųsti vaizdų, ir išsaugodamas duomenų rinkinį CSV formato faile.

### Pavyzdinis scenarijus

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

### Pavyzdinis kodo atsisiuntimas 
[Generuoti naujo duomenų rinkinio scenarijų](../../../../code/04.Finetuning/generate_dataset.py)

### Pavyzdinis duomenų rinkinys
[Pavyzdinis duomenų rinkinys iš LORA smulkinimo pavyzdžio](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.