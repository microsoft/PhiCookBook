<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:51:00+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "hr"
}
-->
# Phi-3-Vision-128K-Instruct Pregled projekta

## Model

Phi-3-Vision-128K-Instruct, lagani, vrhunski multimodalni model, srž je ovog projekta. Dio je Phi-3 obitelji modela i podržava duljinu konteksta do 128.000 tokena. Model je treniran na raznolikom skupu podataka koji uključuje sintetičke podatke i pažljivo filtrirane javno dostupne web stranice, s naglaskom na visokokvalitetan sadržaj koji zahtijeva složeno zaključivanje. Proces treniranja uključivao je nadzirano fino podešavanje i izravnu optimizaciju preferencija kako bi se osigurala precizna usklađenost s uputama, kao i snažne sigurnosne mjere.

## Kreiranje uzoraka podataka ključno je iz nekoliko razloga:

1. **Testiranje**: Uzorci podataka omogućuju testiranje vaše aplikacije u različitim scenarijima bez utjecaja na stvarne podatke. Ovo je posebno važno u fazama razvoja i testiranja.

2. **Poboljšanje performansi**: Uz uzorke podataka koji oponašaju opseg i složenost stvarnih podataka, možete identificirati uska grla u performansama i optimizirati aplikaciju u skladu s tim.

3. **Prototipiranje**: Uzorci podataka mogu se koristiti za izradu prototipova i maketa, što pomaže u razumijevanju zahtjeva korisnika i prikupljanju povratnih informacija.

4. **Analiza podataka**: U znanosti o podacima, uzorci podataka često se koriste za istraživačku analizu podataka, treniranje modela i testiranje algoritama.

5. **Sigurnost**: Korištenje uzoraka podataka u razvojnom i testnom okruženju može pomoći u sprječavanju slučajnog curenja osjetljivih stvarnih podataka.

6. **Učenje**: Ako učite novu tehnologiju ili alat, rad s uzorcima podataka može pružiti praktičan način za primjenu naučenog.

Imajte na umu da kvaliteta vaših uzoraka podataka značajno utječe na ove aktivnosti. Trebali bi biti što bliži stvarnim podacima po strukturi i varijabilnosti.

### Kreiranje uzoraka podataka
[Generate DataSet Script](./CreatingSampleData.md)

## Skup podataka

Dobar primjer uzorka skupa podataka je [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (dostupno na Huggingface).  
Uzorak podataka Burberry proizvoda zajedno s metapodacima o kategoriji proizvoda, cijeni i naslovu, ukupno 3.040 redaka, od kojih svaki predstavlja jedinstveni proizvod. Ovaj skup podataka omogućuje testiranje sposobnosti modela da razumije i interpretira vizualne podatke, generirajući opisni tekst koji hvata složene vizualne detalje i karakteristike specifične za marku.

**Note:** Možete koristiti bilo koji skup podataka koji uključuje slike.

## Složeno zaključivanje

Model mora zaključivati o cijenama i nazivima samo na temelju slike. To zahtijeva da model ne samo prepozna vizualne značajke, već i razumije njihove implikacije u smislu vrijednosti proizvoda i brendiranja. Sintetiziranjem točnih tekstualnih opisa iz slika, projekt ističe potencijal integracije vizualnih podataka za poboljšanje performansi i svestranosti modela u stvarnim primjenama.

## Phi-3 Vision arhitektura

Arhitektura modela je multimodalna verzija Phi-3. Obradjuje i tekstualne i slikovne podatke, integrirajući ove ulaze u jedinstveni niz za sveobuhvatno razumijevanje i generiranje. Model koristi zasebne slojeve ugradnje za tekst i slike. Tekstualni tokeni se pretvaraju u guste vektore, dok se slike obrađuju putem CLIP vision modela za ekstrakciju značajki. Ti se slikovni ugradbeni vektori zatim projiciraju kako bi odgovarali dimenzijama tekstualnih ugradbenih vektora, osiguravajući njihovu besprijekornu integraciju.

## Integracija tekstualnih i slikovnih ugradbenih vektora

Posebni tokeni unutar tekstualnog niza označavaju mjesta gdje treba umetnuti slikovne ugradbene vektore. Tijekom obrade, ti posebni tokeni zamjenjuju se odgovarajućim slikovnim ugradbenim vektorima, omogućujući modelu da tretira tekst i slike kao jedan niz. Upit za naš skup podataka formatiran je korištenjem posebnog <|image|> tokena na sljedeći način:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Primjer koda
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.