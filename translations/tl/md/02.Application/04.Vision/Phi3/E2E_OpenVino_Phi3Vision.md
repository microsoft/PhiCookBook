<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:01:39+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "tl"
}
-->
Ipinapakita ng demo na ito kung paano gamitin ang pretrained model para gumawa ng Python code base sa isang larawan at text prompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Narito ang paliwanag nang hakbang-hakbang:

1. **Imports at Setup**:
   - Ini-import ang mga kinakailangang library at modules, kasama na ang `requests`, `PIL` para sa pagproseso ng larawan, at `transformers` para sa paghawak ng model at pagproseso.

2. **Pag-load at Pag-display ng Larawan**:
   - Binubuksan ang isang image file (`demo.png`) gamit ang `PIL` library at ipinapakita ito.

3. **Pagdeklara ng Prompt**:
   - Gumagawa ng mensahe na naglalaman ng larawan at kahilingan na gumawa ng Python code para i-proseso ang larawan at i-save ito gamit ang `plt` (matplotlib).

4. **Pag-load ng Processor**:
   - Ina-load ang `AutoProcessor` mula sa pretrained model na tinukoy sa `out_dir` na directory. Ang processor na ito ang maghahandle ng text at image inputs.

5. **Paglikha ng Prompt**:
   - Ginagamit ang `apply_chat_template` method para i-format ang mensahe sa prompt na angkop sa model.

6. **Pagproseso ng Inputs**:
   - Pinoproseso ang prompt at larawan sa mga tensor na maiintindihan ng model.

7. **Pagtatakda ng Generation Arguments**:
   - Itinatakda ang mga argumento para sa proseso ng generation ng model, kabilang ang maximum na bilang ng bagong tokens na gagawin at kung gagamitin ang sampling sa output.

8. **Pag-generate ng Code**:
   - Nagge-generate ang model ng Python code base sa inputs at generation arguments. Ginagamit ang `TextStreamer` para i-handle ang output, nilalaktawan ang prompt at special tokens.

9. **Output**:
   - Ipinapakita ang nagawang code, na dapat ay naglalaman ng Python code para i-proseso ang larawan at i-save ito ayon sa prompt.

Ipinapakita ng demo na ito kung paano gamitin ang pretrained model gamit ang OpenVino para gumawa ng code nang dynamic base sa input ng user at mga larawan.

**Pagtatanggol**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.