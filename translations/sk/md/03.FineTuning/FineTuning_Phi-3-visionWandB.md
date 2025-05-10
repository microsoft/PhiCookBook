<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:50:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "sk"
}
-->
# Phi-3-Vision-128K-Instruct Prehľad projektu

## Model

Phi-3-Vision-128K-Instruct, ľahký, špičkový multimodálny model, je jadrom tohto projektu. Patrí do rodiny modelov Phi-3 a podporuje kontext dlhý až 128 000 tokenov. Model bol trénovaný na rôznorodom datasete, ktorý zahŕňa syntetické dáta a starostlivo filtrované verejne dostupné webové stránky, pričom dôraz bol kladený na kvalitný obsah vyžadujúci uvažovanie. Tréning zahŕňal riadené doladenie a priame optimalizovanie preferencií, aby sa zabezpečila presná zhoda s inštrukciami, ako aj robustné bezpečnostné opatrenia.

## Vytváranie vzorových dát je dôležité z niekoľkých dôvodov:

1. **Testovanie**: Vzorové dáta umožňujú testovať vašu aplikáciu v rôznych situáciách bez ovplyvnenia reálnych dát. To je obzvlášť dôležité vo fáze vývoja a testovania.

2. **Ladenie výkonu**: S použitím vzorových dát, ktoré napodobňujú rozsah a zložitosť reálnych dát, môžete identifikovať úzke miesta vo výkone a optimalizovať aplikáciu.

3. **Prototypovanie**: Vzorové dáta sa dajú použiť na vytváranie prototypov a makiet, čo pomáha lepšie pochopiť požiadavky používateľov a získať spätnú väzbu.

4. **Analýza dát**: V dátovej vede sa vzorové dáta často používajú na prieskumnú analýzu, tréning modelov a testovanie algoritmov.

5. **Bezpečnosť**: Použitie vzorových dát vo vývojových a testovacích prostrediach pomáha predísť náhodnému úniku citlivých reálnych dát.

6. **Vzdelávanie**: Ak sa učíte novú technológiu alebo nástroj, práca so vzorovými dátami vám poskytne praktickú možnosť aplikovať získané znalosti.

Pamätajte, že kvalita vašich vzorových dát môže výrazne ovplyvniť tieto aktivity. Mali by byť čo najbližšie k reálnym dátam z hľadiska štruktúry a variability.

### Vytváranie vzorových dát  
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Dobrým príkladom vzorového datasetu je [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (dostupný na Huggingface).  
Vzorka dát Burberry produktov spolu s metadátami o kategórii produktov, cene a názve obsahuje celkovo 3 040 riadkov, z ktorých každý predstavuje jedinečný produkt. Tento dataset nám umožňuje testovať schopnosť modelu porozumieť a interpretovať vizuálne dáta, generovať popisný text zachytávajúci detailné vizuálne prvky a charakteristiky značky.

**Note:** Môžete použiť akýkoľvek dataset, ktorý obsahuje obrázky.

## Zložité uvažovanie

Model musí uvažovať o cenách a názvoch iba na základe obrázka. To vyžaduje, aby model nielen rozpoznal vizuálne prvky, ale aj pochopil ich význam z hľadiska hodnoty produktu a značky. Synthézou presných textových popisov z obrázkov projekt ukazuje potenciál integrácie vizuálnych dát na zlepšenie výkonu a všestrannosti modelov v reálnych aplikáciách.

## Architektúra Phi-3 Vision

Architektúra modelu je multimodálna verzia Phi-3. Spracováva textové aj obrazové dáta a integruje tieto vstupy do jednotného poradia pre komplexné porozumenie a generovanie. Model používa samostatné embedding vrstvy pre text a obrázky. Textové tokeny sa prevádzajú na husté vektory, zatiaľ čo obrázky spracováva CLIP vision model na extrakciu featur embeddingov. Tieto embeddingy obrázkov sú následne premietnuté tak, aby zodpovedali rozmerom textových embeddingov, čo zabezpečuje ich bezproblémovú integráciu.

## Integrácia textových a obrazových embeddingov

Špeciálne tokeny v textovej sekvencii označujú miesta, kde by sa mali vložiť embeddingy obrázkov. Počas spracovania sú tieto špeciálne tokeny nahradené príslušnými embeddingami obrázkov, čo umožňuje modelu pracovať s textom aj obrázkami ako s jednou sekvenciou. Prompt pre náš dataset je formátovaný pomocou špeciálneho tokenu <|image|> nasledovne:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Ukážkový kód
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.