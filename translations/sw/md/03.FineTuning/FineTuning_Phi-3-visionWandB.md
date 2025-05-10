<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:49:41+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "sw"
}
-->
# Phi-3-Vision-128K-Instruct Muhtasari wa Mradi

## Mfano

Phi-3-Vision-128K-Instruct, mfano mwepesi wa hali ya juu wa multimodal, ni kiini cha mradi huu. Ni sehemu ya familia ya mifano ya Phi-3 na ina uwezo wa muktadha hadi tokeni 128,000. Mfano huu ulifundishwa kwa seti mbalimbali za data zinazojumuisha data bandia na tovuti za umma zilizochujwa kwa makini, zikisisitiza maudhui bora na yanayohitaji fikra za kina. Mchakato wa mafunzo ulijumuisha fine-tuning iliyoongozwa na optimization ya mapendeleo moja kwa moja ili kuhakikisha kufuata maagizo kwa usahihi, pamoja na hatua madhubuti za usalama.

## Kuunda data ya sampuli ni muhimu kwa sababu kadhaa:

1. **Upimaji**: Data ya sampuli inakuwezesha kupima programu yako katika hali tofauti bila kuathiri data halisi. Hii ni muhimu hasa katika hatua za maendeleo na majaribio.

2. **Kurekebisha Utendaji**: Kwa data ya sampuli inayofanana na ukubwa na ugumu wa data halisi, unaweza kubaini vikwazo vya utendaji na kuboresha programu yako ipasavyo.

3. **Uundaji wa Prototipu**: Data ya sampuli inaweza kutumika kuunda prototipu na mfano wa kazi, ambayo husaidia kuelewa mahitaji ya watumiaji na kupata mrejesho.

4. **Uchambuzi wa Data**: Katika sayansi ya data, data ya sampuli hutumika mara nyingi kwa uchambuzi wa awali, mafunzo ya modeli, na upimaji wa algoriti.

5. **Usalama**: Kutumia data ya sampuli katika mazingira ya maendeleo na majaribio husaidia kuzuia uvujaji wa data halisi yenye taarifa nyeti.

6. **Kujifunza**: Ikiwa unajifunza teknolojia au chombo kipya, kufanya kazi na data ya sampuli kunatoa njia ya vitendo ya kutumia unachojifunza.

Kumbuka, ubora wa data yako ya sampuli unaweza kuathiri shughuli hizi kwa kiasi kikubwa. Inapaswa kuwa karibu sana na data halisi kwa muundo na utofauti.

### Uundaji wa Data ya Sampuli
[Generate DataSet Script](./CreatingSampleData.md)

## Seti ya Data

Mfano mzuri wa seti ya data ya sampuli ni [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (inapatikana kwenye Huggingface). 
Seti ya data ya sampuli ya bidhaa za Burberry pamoja na metadata kuhusu aina ya bidhaa, bei, na kichwa ina jumla ya mistari 3,040, kila moja ikiwakilisha bidhaa tofauti. Seti hii inatuwezesha kupima uwezo wa mfano kuelewa na kufasiri data ya picha, ikitengeneza maandishi ya kuelezea yanayoshikilia maelezo ya kina ya kuona na sifa za kipekee za chapa.

**Note:** Unaweza kutumia seti yoyote ya data inayojumuisha picha.

## Fikra Ngumu

Mfano unahitaji kufikiria kuhusu bei na majina kwa kuzingatia picha pekee. Hii inahitaji mfano kutambua sifa za kuona na pia kuelewa maana yake katika thamani ya bidhaa na chapa. Kwa kutengeneza maelezo sahihi ya maandishi kutoka kwa picha, mradi unaonyesha uwezo wa kuunganisha data ya kuona ili kuboresha utendaji na ufanisi wa mifano katika matumizi halisi.

## Muundo wa Phi-3 Vision

Muundo wa mfano ni toleo la multimodal la Phi-3. Unashughulikia data za maandishi na picha, ukiunganisha pembejeo hizi kuwa mfuatano mmoja kwa ajili ya kuelewa na kazi za uzalishaji kwa kina. Mfano hutumia tabaka tofauti za embedding kwa maandishi na picha. Tokeni za maandishi hubadilishwa kuwa vekta zenye msongamano, wakati picha zinashughulikiwa kupitia mfano wa CLIP vision kupata embedding za sifa. Embedding hizi za picha kisha huwekwa kwenye vipimo vinavyolingana na embedding za maandishi, kuhakikisha zinaweza kuunganishwa kwa urahisi.

## Muunganiko wa Embedding za Maandishi na Picha

Tokeni maalum ndani ya mfuatano wa maandishi zinaonyesha mahali ambapo embedding za picha zinapaswa kuwekwa. Wakati wa usindikaji, tokeni hizi maalum zinabadilishwa na embedding za picha zinazolingana, kuruhusu mfano kushughulikia maandishi na picha kama mfuatano mmoja. Ombi kwa seti yetu ya data umeandaliwa kwa kutumia tokeni maalum <|image|> kama ifuatavyo:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Mfano wa Msimbo
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Kang'ang'ania**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.