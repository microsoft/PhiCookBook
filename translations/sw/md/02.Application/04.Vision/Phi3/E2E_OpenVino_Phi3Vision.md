<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:05:04+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "sw"
}
-->
Demo hii inaonyesha jinsi ya kutumia modeli iliyofunzwa tayari kuunda msimbo wa Python kulingana na picha na maelezo ya maandishi.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Hapa kuna maelezo hatua kwa hatua:

1. **Imports na Usanidi**:
   - Maktaba na moduli muhimu zinazoingizwa, ikiwa ni pamoja na `requests`, `PIL` kwa usindikaji wa picha, na `transformers` kwa kushughulikia modeli na usindikaji.

2. **Kupakia na Kuonyesha Picha**:
   - Faili la picha (`demo.png`) linafunguliwa kwa kutumia maktaba ya `PIL` na kuonyeshwa.

3. **Kufafanua Maelezo**:
   - Ujumbe unaotumia picha na ombi la kuunda msimbo wa Python wa kusindika picha na kuihifadhi kwa kutumia `plt` (matplotlib).

4. **Kupakia Processor**:
   - `AutoProcessor` inapakiwa kutoka kwa modeli iliyofunzwa tayari inayopatikana kwenye saraka ya `out_dir`. Processor hii itashughulikia maandishi na picha.

5. **Kuumba Maelezo**:
   - Njia ya `apply_chat_template` inatumiwa kuunda maelezo yanayofaa kwa modeli.

6. **Kusindika Ingizo**:
   - Maelezo na picha vinabadilishwa kuwa tensors ambazo modeli inaweza kuelewa.

7. **Kuweka Mipangilio ya Uundaji**:
   - Mipangilio ya mchakato wa uundaji wa modeli inaainishwa, ikiwa ni pamoja na idadi kubwa ya tokeni mpya za kuunda na kama matokeo yatapasuliwa.

8. **Kuunda Msimbo**:
   - Modeli inaunda msimbo wa Python kulingana na ingizo na mipangilio ya uundaji. `TextStreamer` inatumiwa kushughulikia matokeo, ikiepuka maelezo na tokeni maalum.

9. **Matokeo**:
   - Msimbo ulioundwa unaandikwa, ambao unapaswa kujumuisha msimbo wa Python wa kusindika picha na kuihifadhi kama ilivyoelezwa katika maelezo.

Demo hii inaonyesha jinsi ya kutumia modeli iliyofunzwa tayari kwa kutumia OpenVino kuunda msimbo kwa njia ya mabadiliko kulingana na ingizo la mtumiaji na picha.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.