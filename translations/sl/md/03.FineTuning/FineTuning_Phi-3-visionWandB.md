<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:15:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "sl"
}
-->
# Phi-3-Vision-128K-Instruct Pregled projekta

## Model

Phi-3-Vision-128K-Instruct, lahkoten, najsodobnejši multimodalni model, je srce tega projekta. Spada v družino modelov Phi-3 in podpira dolžino konteksta do 128.000 tokenov. Model je bil treniran na raznoliki zbirki podatkov, ki vključuje sintetične podatke in skrbno filtrirane javno dostopne spletne strani, s poudarkom na vsebini visoke kakovosti, ki zahteva razmišljanje. Proces učenja je vključeval nadzorovano fino prilagajanje in neposredno optimizacijo preferenc, da se zagotovi natančno upoštevanje navodil, pa tudi robustne varnostne ukrepe.

## Ustvarjanje vzorčnih podatkov je ključno iz več razlogov:

1. **Testiranje**: Vzorčni podatki omogočajo testiranje vaše aplikacije v različnih scenarijih, ne da bi vplivali na resnične podatke. To je še posebej pomembno v fazah razvoja in testiranja.

2. **Prilagajanje zmogljivosti**: Z vzorčnimi podatki, ki posnemajo obseg in kompleksnost resničnih podatkov, lahko prepoznate ozka grla zmogljivosti in optimizirate aplikacijo.

3. **Prototipiranje**: Vzorčni podatki se lahko uporabijo za izdelavo prototipov in maket, kar pomaga pri razumevanju uporabniških zahtev in pridobivanju povratnih informacij.

4. **Analiza podatkov**: V podatkovni znanosti se vzorčni podatki pogosto uporabljajo za raziskovalno analizo podatkov, učenje modelov in testiranje algoritmov.

5. **Varnost**: Uporaba vzorčnih podatkov v razvojnih in testnih okoljih pomaga preprečiti nenamerne uhajanja občutljivih resničnih podatkov.

6. **Učenje**: Če se učite nove tehnologije ali orodja, delo z vzorčnimi podatki omogoča praktično uporabo naučenega.

Ne pozabite, da kakovost vaših vzorčnih podatkov pomembno vpliva na te aktivnosti. Ti naj bodo čim bolj podobni resničnim podatkom glede strukture in raznolikosti.

### Ustvarjanje vzorčnih podatkov
[Generate DataSet Script](./CreatingSampleData.md)

## Zbirka podatkov

Dober primer vzorčne zbirke podatkov je [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (na voljo na Huggingface).  
Vzorčna zbirka podatkov Burberry izdelkov skupaj z metapodatki o kategoriji izdelkov, ceni in naslovu vsebuje skupno 3.040 vrstic, vsaka predstavlja edinstven izdelek. Ta zbirka podatkov nam omogoča testiranje sposobnosti modela za razumevanje in interpretacijo vizualnih podatkov ter generiranje opisnega besedila, ki zajema zapletene vizualne podrobnosti in značilnosti blagovne znamke.

**Note:** Uporabite lahko katerokoli zbirko podatkov, ki vključuje slike.

## Kompleksno razmišljanje

Model mora sklepati o cenah in poimenovanju zgolj na podlagi slike. To zahteva, da model ne prepozna le vizualnih značilnosti, ampak tudi razume njihov pomen v smislu vrednosti izdelka in blagovne znamke. S sintetiziranjem natančnih besedilnih opisov iz slik projekt poudarja potencial integracije vizualnih podatkov za izboljšanje zmogljivosti in vsestranskosti modelov v resničnih aplikacijah.

## Arhitektura Phi-3 Vision

Arhitektura modela je multimodalna različica Phi-3. Obdeluje tako besedilne kot slikovne podatke in ju združuje v enotno zaporedje za celovito razumevanje in generiranje. Model uporablja ločene plasti za vdelavo besedila in slik. Besedilni tokeni se pretvorijo v goste vektorje, slike pa se obdelajo preko CLIP vision modela za pridobitev vdelav značilnosti. Te vdelave slik se nato projicirajo, da ustrezajo dimenzijam besedilnih vdelav, kar omogoča njihovo nemoteno integracijo.

## Integracija besedilnih in slikovnih vdelav

Posebni tokeni v besedilnem zaporedju označujejo, kje naj se vstavijo slikovne vdelave. Med obdelavo se ti posebni tokeni nadomestijo z ustreznimi slikovnimi vdelavami, kar omogoča modelu, da obravnava besedilo in slike kot eno zaporedje. Poziv za našo zbirko podatkov je oblikovan z uporabo posebnega tokena <|image|> na naslednji način:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Primer kode
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.