<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:13:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "sw"
}
-->
# Muhtasari wa Mradi wa Phi-3-Vision-128K-Instruct

## Mfano

Phi-3-Vision-128K-Instruct, mfano mwepesi wa kisasa wa multimodal, ndio msingi wa mradi huu. Ni sehemu ya familia ya mifano ya Phi-3 na ina uwezo wa kushughulikia muktadha wa hadi tokeni 128,000. Mfano huu ulifundishwa kwa kutumia seti mbalimbali za data zinazojumuisha data bandia na tovuti za umma zilizochujwa kwa makini, zikisisitiza maudhui ya ubora wa juu na yenye fikra za kina. Mchakato wa mafunzo ulijumuisha urekebishaji wa usimamizi na uboreshaji wa mapendeleo moja kwa moja ili kuhakikisha kufuata maagizo kwa usahihi, pamoja na hatua madhubuti za usalama.

## Kuunda data ya sampuli ni muhimu kwa sababu kadhaa:

1. **Upimaji**: Data ya sampuli inakuwezesha kupima programu yako katika hali mbalimbali bila kuathiri data halisi. Hii ni muhimu hasa katika hatua za maendeleo na majaribio.

2. **Kurekebisha Utendaji**: Kwa kutumia data ya sampuli inayofanana na ukubwa na ugumu wa data halisi, unaweza kubaini vikwazo vya utendaji na kuboresha programu yako ipasavyo.

3. **Uundaji wa Mifano**: Data ya sampuli inaweza kutumika kuunda mifano na maonyesho ya awali, ambayo husaidia kuelewa mahitaji ya watumiaji na kupata maoni.

4. **Uchambuzi wa Data**: Katika sayansi ya data, data ya sampuli hutumika mara nyingi kwa uchambuzi wa awali wa data, mafunzo ya modeli, na upimaji wa algoriti.

5. **Usalama**: Kutumia data ya sampuli katika mazingira ya maendeleo na majaribio kunaweza kusaidia kuzuia uvujaji wa data halisi nyeti kwa bahati mbaya.

6. **Kujifunza**: Ikiwa unajifunza teknolojia au chombo kipya, kufanya kazi na data ya sampuli kunaweza kutoa njia ya vitendo ya kutumia kile ulichojifunza.

Kumbuka, ubora wa data yako ya sampuli unaweza kuathiri sana shughuli hizi. Inapaswa kuwa karibu iwezekanavyo na data halisi kwa muundo na utofauti.

### Uundaji wa Data ya Sampuli
[Generate DataSet Script](./CreatingSampleData.md)

## Seti ya Data

Mfano mzuri wa seti ya data ya sampuli ni [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (inapatikana kwenye Huggingface).  
Seti ya data ya sampuli ya bidhaa za Burberry pamoja na metadata kuhusu aina ya bidhaa, bei, na kichwa ina jumla ya mistari 3,040, kila moja ikiwakilisha bidhaa ya kipekee. Seti hii ya data inatupa fursa ya kupima uwezo wa mfano kuelewa na kutafsiri data za kuona, ikizalisha maandishi ya kuelezea yanayoshikilia maelezo ya kina ya picha na sifa za kipekee za chapa.

**Note:** Unaweza kutumia seti yoyote ya data inayojumuisha picha.

## Fikra Ngumu

Mfano unahitaji kufikiri kuhusu bei na majina kwa kuzingatia picha pekee. Hii inahitaji mfano kutambua sifa za kuona na pia kuelewa maana yake kwa thamani ya bidhaa na chapa. Kwa kuunganisha maelezo sahihi ya maandishi kutoka kwa picha, mradi huu unaonyesha uwezo wa kuingiza data za kuona ili kuboresha utendaji na ufanisi wa mifano katika matumizi halisi.

## Muundo wa Phi-3 Vision

Muundo wa mfano ni toleo la multimodal la Phi-3. Unashughulikia data za maandishi na picha, ukizichanganya katika mfuatano mmoja kwa uelewa mpana na kazi za uzalishaji. Mfano hutumia tabaka tofauti za embedding kwa maandishi na picha. Tokeni za maandishi hubadilishwa kuwa vekta zenye msongamano, wakati picha zinashughulikiwa kupitia mfano wa kuona wa CLIP ili kutoa embeddings za sifa. Embeddings hizi za picha kisha huratibiwa ili zilingane na vipimo vya embeddings za maandishi, kuhakikisha zinaweza kuunganishwa kwa urahisi.

## Muungano wa Embeddings za Maandishi na Picha

Tokeni maalum ndani ya mfuatano wa maandishi zinaonyesha mahali ambapo embeddings za picha zinapaswa kuwekwa. Wakati wa usindikaji, tokeni hizi maalum zinabadilishwa na embeddings zinazolingana za picha, kuruhusu mfano kushughulikia maandishi na picha kama mfuatano mmoja. Ombi la seti yetu ya data limeandaliwa kwa kutumia tokeni maalum <|image|> kama ifuatavyo:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Mfano wa Msimbo
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.