<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:01:46+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "sw"
}
-->
Demo hii inaonyesha jinsi ya kutumia modeli iliyofunzwa tayari kuunda msimbo wa Python kulingana na picha na maelezo ya maandishi.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Hapa kuna maelezo hatua kwa hatua:

1. **Imports na Usanidi**:
   - Maktaba na moduli muhimu zinapakiwa, zikiwemo `requests`, `PIL` kwa usindikaji wa picha, na `transformers` kwa kushughulikia modeli na usindikaji.

2. **Kupakia na Kuonyesha Picha**:
   - Faili la picha (`demo.png`) linafunguliwa kwa kutumia maktaba ya `PIL` na kuonyeshwa.

3. **Kufafanua Prompt**:
   - Ujumbe unaotumia picha na ombi la kuunda msimbo wa Python wa kusindika picha na kuihifadhi kwa kutumia `plt` (matplotlib) unatengenezwa.

4. **Kupakia Processor**:
   - `AutoProcessor` inapakiwa kutoka kwa modeli iliyofunzwa tayari iliyoko kwenye saraka ya `out_dir`. Processor hii itashughulikia maingizo ya maandishi na picha.

5. **Kutengeneza Prompt**:
   - Mbinu ya `apply_chat_template` inatumiwa kuunda prompt inayofaa kwa modeli.

6. **Kusindika Maingizo**:
   - Prompt na picha husindika kuwa tensors ambazo modeli inaweza kuelewa.

7. **Kuweka Vigezo vya Uundaji**:
   - Vigezo vya mchakato wa uundaji wa modeli vinafafanuliwa, ikiwa ni pamoja na idadi kubwa ya tokeni mpya za kuunda na kama sampuli itatumika.

8. **Kuumba Msimbo**:
   - Modeli huunda msimbo wa Python kulingana na maingizo na vigezo vya uundaji. `TextStreamer` hutumika kushughulikia matokeo, ikiruka prompt na tokeni maalum.

9. **Matokeo**:
   - Msimbo ulioundwa unachapishwa, ambao unapaswa kujumuisha msimbo wa Python wa kusindika picha na kuihifadhi kama ilivyoelezwa kwenye prompt.

Demo hii inaonyesha jinsi ya kutumia modeli iliyofunzwa tayari kwa OpenVino kuunda msimbo kwa njia ya mabadiliko kulingana na maingizo ya mtumiaji na picha.

**Kauli ya Kukataa**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatutawajibika kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.