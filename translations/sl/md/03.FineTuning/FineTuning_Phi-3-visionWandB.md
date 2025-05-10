<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:51:10+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "sl"
}
-->
# Phi-3-Vision-128K-Instruct Project Overview

## The Model

Phi-3-Vision-128K-Instruct je lahki, vrhunski multimodalni model, ki je osrednji del tega projekta. Spada v družino modelov Phi-3 in podpira dolžino konteksta do 128.000 tokenov. Model je bil treniran na raznoliki zbirki podatkov, ki vključuje sintetične podatke in skrbno filtrirane javno dostopne spletne strani, s poudarkom na vsebinah visoke kakovosti in z zahtevnim razmišljanjem. Proces treniranja je vključeval nadzorovano fino nastavitev in neposredno optimizacijo preferenc, da se zagotovi natančno sledenje navodilom ter močni varnostni ukrepi.

## Zakaj je ustvarjanje vzorčnih podatkov ključno:

1. **Testiranje**: Vzorčni podatki omogočajo testiranje vaše aplikacije v različnih scenarijih, ne da bi vplivali na dejanske podatke. To je še posebej pomembno v fazah razvoja in testiranja.

2. **Prilagajanje zmogljivosti**: Z vzorčnimi podatki, ki posnemajo obseg in kompleksnost pravih podatkov, lahko odkrijete ozka grla in optimizirate delovanje aplikacije.

3. **Prototipiranje**: Vzorčni podatki služijo za izdelavo prototipov in maket, kar pomaga pri razumevanju uporabniških zahtev in pridobivanju povratnih informacij.

4. **Analiza podatkov**: V podatkovni znanosti se vzorčni podatki pogosto uporabljajo za raziskovalno analizo, treniranje modelov in testiranje algoritmov.

5. **Varnost**: Uporaba vzorčnih podatkov v razvojnih in testnih okoljih pomaga preprečiti nenamerne uhajanja občutljivih pravih podatkov.

6. **Učenje**: Če se učite nove tehnologije ali orodja, delo z vzorčnimi podatki omogoča praktično uporabo naučenega.

Ne pozabite, da kakovost vzorčnih podatkov močno vpliva na te aktivnosti. Naj bodo čim bolj podobni pravim podatkom glede strukture in raznolikosti.

### Sample Data Creation
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Dober primer vzorčne zbirke podatkov je [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (na voljo na Huggingface).  
Vzorčni podatki Burberry izdelkov vključujejo metapodatke o kategoriji izdelka, ceni in naslovu, skupaj 3.040 vrstic, od katerih vsaka predstavlja edinstven izdelek. Ta zbirka podatkov nam omogoča testiranje modelove sposobnosti razumevanja in interpretacije vizualnih podatkov, ter generiranja opisnega besedila, ki zajema zapletene vizualne podrobnosti in značilnosti blagovne znamke.

**Note:** Uporabite lahko katerokoli zbirko podatkov, ki vključuje slike.

## Kompleksno razmišljanje

Model mora sklepati o cenah in imenih le na podlagi slike. To zahteva, da model ne prepozna samo vizualnih značilnosti, temveč tudi razume njihov pomen glede vrednosti izdelka in blagovne znamke. S sintetiziranjem natančnih besedilnih opisov iz slik projekt poudarja potencial vključevanja vizualnih podatkov za izboljšanje zmogljivosti in vsestranskosti modelov v realnih aplikacijah.

## Phi-3 Vision arhitektura

Arhitektura modela je multimodalna različica Phi-3. Obdeluje tako besedilo kot slikovne podatke, ki jih združi v enotno sekvenco za celovito razumevanje in generiranje. Model uporablja ločene plasti vdelave za besedilo in slike. Besedilni tokeni se pretvorijo v goste vektorje, slike pa obdeluje CLIP vision model za pridobivanje značilk. Te slikovne vdelave se nato projicirajo tako, da ustrezajo dimenzijam besedilnih vdelav, kar omogoča nemoteno integracijo.

## Integracija besedilnih in slikovnih vdelav

Posebni tokeni v besedilni sekvenci označujejo, kje naj se vstavi slikovne vdelave. Med obdelavo se ti posebni tokeni nadomestijo z ustreznimi slikovnimi vdelavami, kar omogoča modelu obravnavo besedila in slik kot ene same sekvence. Poziv za našo zbirko podatkov je oblikovan z uporabo posebnega tokena <|image|> na naslednji način:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Vzorec kode
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.