<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:50:49+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "sr"
}
-->
# Phi-3-Vision-128K-Instruct Pregled Projekta

## Model

Phi-3-Vision-128K-Instruct, lagani, najsavremeniji multimodalni model, je srž ovog projekta. Deo je Phi-3 porodice modela i podržava dužinu konteksta do 128.000 tokena. Model je treniran na raznovrsnom skupu podataka koji uključuje sintetičke podatke i pažljivo filtrirane javno dostupne sajtove, sa naglaskom na visokokvalitetan sadržaj koji zahteva rezonovanje. Proces treniranja je uključivao nadzirano fino podešavanje i direktnu optimizaciju preferencija kako bi se osiguralo precizno praćenje instrukcija, kao i robusne bezbednosne mere.

## Kreiranje uzoraka podataka je ključno iz nekoliko razloga:

1. **Testiranje**: Uzorci podataka omogućavaju testiranje aplikacije u različitim scenarijima bez uticaja na stvarne podatke. Ovo je naročito važno u fazama razvoja i pripreme.

2. **Podešavanje performansi**: Sa uzorcima podataka koji imitiraju obim i složenost stvarnih podataka, možete identifikovati uska grla u performansama i optimizovati aplikaciju u skladu sa tim.

3. **Prototipizacija**: Uzorci podataka se mogu koristiti za pravljenje prototipova i maketa, što pomaže u razumevanju korisničkih zahteva i dobijanju povratnih informacija.

4. **Analiza podataka**: U data science-u, uzorci podataka se često koriste za istraživačku analizu podataka, treniranje modela i testiranje algoritama.

5. **Bezbednost**: Korišćenje uzoraka podataka u razvojnom i test okruženju može pomoći u sprečavanju nenamernih curenja osetljivih stvarnih podataka.

6. **Učenje**: Ako učite novu tehnologiju ili alat, rad sa uzorcima podataka može biti praktičan način da primenite naučeno.

Imajte na umu da kvalitet vaših uzoraka podataka može značajno uticati na ove aktivnosti. Trebalo bi da budu što sličniji stvarnim podacima po strukturi i varijabilnosti.

### Kreiranje Uzoraka Podataka
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Dobar primer uzorka dataset-a je [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (dostupan na Huggingface).  
Ovaj uzorak podataka Burberry proizvoda, zajedno sa metapodacima o kategoriji proizvoda, ceni i nazivu, ima ukupno 3.040 redova, od kojih svaki predstavlja jedinstveni proizvod. Ovaj dataset nam omogućava da testiramo sposobnost modela da razume i interpretira vizuelne podatke, generišući opisne tekstove koji hvataju složene vizuelne detalje i karakteristike specifične za brend.

**Note:** Možete koristiti bilo koji dataset koji uključuje slike.

## Složeno rezonovanje

Model treba da rezonuje o cenama i imenima samo na osnovu slike. To zahteva da model ne samo prepozna vizuelne karakteristike, već i da razume njihove implikacije u smislu vrednosti proizvoda i brendiranja. Sintezujući precizne tekstualne opise iz slika, projekat ističe potencijal integracije vizuelnih podataka za unapređenje performansi i svestranosti modela u realnim aplikacijama.

## Phi-3 Vision Arhitektura

Arhitektura modela je multimodalna verzija Phi-3. Obradjuje i tekstualne i slikovne podatke, integrišući ove ulaze u jedinstveni niz za sveobuhvatno razumevanje i generisanje. Model koristi odvojene slojeve za ugradnju (embedding) teksta i slika. Tekstualni tokeni se pretvaraju u guste vektore, dok se slike obrađuju kroz CLIP vision model za izdvajanje karakterističnih ugradnji. Ove ugradnje slika se zatim projektuju tako da odgovaraju dimenzijama tekstualnih ugradnji, čime se omogućava njihova besprekorno integracija.

## Integracija Tekstualnih i Slikovnih Ugradnji

Specijalni tokeni unutar tekstualnog niza označavaju mesta na kojima treba ubaciti ugradnje slika. Tokom obrade, ovi specijalni tokeni se zamenjuju odgovarajućim ugradnjama slika, što omogućava modelu da tretira tekst i slike kao jedinstveni niz. Prompt za naš dataset je formatiran korišćenjem specijalnog <|image|> tokena na sledeći način:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Primer Koda
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати коначним и ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне интерпретације настале употребом овог превода.