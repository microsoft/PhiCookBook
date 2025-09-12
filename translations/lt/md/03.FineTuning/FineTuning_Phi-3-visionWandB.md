<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-09-12T14:43:55+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "lt"
}
-->
# Phi-3-Vision-128K-Instruct Projekto Apžvalga

## Modelis

Phi-3-Vision-128K-Instruct – tai lengvas, pažangus multimodalinis modelis, kuris yra šio projekto pagrindas. Jis priklauso Phi-3 modelių šeimai ir palaiko konteksto ilgį iki 128,000 žetonų. Modelis buvo apmokytas naudojant įvairialypį duomenų rinkinį, įskaitant sintetinę informaciją ir kruopščiai atrinktas viešai prieinamas svetaines, akcentuojant aukštos kokybės, sudėtingo mąstymo turinį. Mokymo procesas apėmė prižiūrimą smulkiąją derinimą ir tiesioginę pirmenybių optimizaciją, siekiant užtikrinti tikslų instrukcijų laikymąsi bei patikimas saugumo priemones.

## Kodėl svarbu kurti pavyzdinius duomenis:

1. **Testavimas**: Pavyzdiniai duomenys leidžia testuoti jūsų programą įvairiose situacijose, nepažeidžiant tikrų duomenų. Tai ypač svarbu kūrimo ir testavimo etapais.

2. **Našumo optimizavimas**: Naudojant pavyzdinius duomenis, kurie atspindi tikrų duomenų mastą ir sudėtingumą, galima nustatyti našumo trūkumus ir optimizuoti programą.

3. **Prototipų kūrimas**: Pavyzdiniai duomenys gali būti naudojami kuriant prototipus ir maketus, kurie padeda suprasti vartotojų poreikius ir gauti atsiliepimus.

4. **Duomenų analizė**: Duomenų moksle pavyzdiniai duomenys dažnai naudojami tiriamosios duomenų analizės, modelių mokymo ir algoritmų testavimo tikslais.

5. **Saugumas**: Naudojant pavyzdinius duomenis kūrimo ir testavimo aplinkose galima išvengti atsitiktinio jautrių tikrų duomenų nutekėjimo.

6. **Mokymasis**: Jei mokotės naujos technologijos ar įrankio, darbas su pavyzdiniais duomenimis gali būti praktiškas būdas pritaikyti įgytas žinias.

Atminkite, kad pavyzdinių duomenų kokybė gali reikšmingai paveikti šias veiklas. Jie turėtų būti kuo panašesni į tikrus duomenis pagal struktūrą ir įvairovę.

### Pavyzdinių duomenų kūrimas
[Duomenų rinkinio generavimo scenarijus](./CreatingSampleData.md)

## Duomenų rinkinys

Geras pavyzdinio duomenų rinkinio pavyzdys yra [DBQ/Burberry.Product.prices.United.States duomenų rinkinys](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (prieinamas Huggingface platformoje). 
Pavyzdinis Burberry produktų duomenų rinkinys kartu su metaduomenimis apie produktų kategoriją, kainą ir pavadinimą, iš viso turintis 3,040 eilučių, kiekviena atspindinti unikalų produktą. Šis duomenų rinkinys leidžia testuoti modelio gebėjimą suprasti ir interpretuoti vizualinius duomenis, generuojant aprašomąjį tekstą, kuris atspindi sudėtingas vizualines detales ir prekės ženklo specifines savybes.

**Pastaba:** Galite naudoti bet kokį duomenų rinkinį, kuriame yra vaizdų.

## Sudėtingas mąstymas

Modelis turi analizuoti kainas ir pavadinimus remdamasis tik vaizdu. Tai reikalauja, kad modelis ne tik atpažintų vizualines savybes, bet ir suprastų jų reikšmę produkto vertės ir prekės ženklo kontekste. Tiksliai generuodamas tekstinius aprašymus iš vaizdų, projektas pabrėžia vizualinių duomenų integravimo potencialą, siekiant pagerinti modelių našumą ir universalumą realiose situacijose.

## Phi-3 Vision Architektūra

Modelio architektūra yra multimodalinė Phi-3 versija. Ji apdoroja tiek tekstinius, tiek vaizdinius duomenis, integruodama šiuos įvesties duomenis į vieningą seką, skirtą išsamiam supratimui ir generavimo užduotims. Modelis naudoja atskirus įterpimo sluoksnius tekstui ir vaizdams. Teksto žetonai paverčiami tankiais vektoriais, o vaizdai apdorojami per CLIP vizijos modelį, kad būtų išgauti savybių įterpimai. Šie vaizdų įterpimai vėliau projektuojami taip, kad atitiktų teksto įterpimų matmenis, užtikrinant sklandžią integraciją.

## Teksto ir vaizdų įterpimų integracija

Specialūs žetonai teksto sekoje nurodo, kur turėtų būti įterpti vaizdų įterpimai. Apdorojimo metu šie specialūs žetonai pakeičiami atitinkamais vaizdų įterpimais, leidžiant modeliui apdoroti tekstą ir vaizdus kaip vieną seką. Mūsų duomenų rinkinio užklausa formatuojama naudojant specialų <|image|> žetoną, kaip parodyta:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Pavyzdinis kodas
- [Phi-3-Vision mokymo scenarijus](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias pavyzdys](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.