<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:04:56+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "tl"
}
-->
Ipinapakita ng demo na ito kung paano gamitin ang pretrained na modelo upang gumawa ng Python code base sa isang larawan at text prompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Narito ang paliwanag nang hakbang-hakbang:

1. **Mga Import at Setup**:
   - Ina-import ang mga kinakailangang library at module, kabilang ang `requests`, `PIL` para sa pagproseso ng larawan, at `transformers` para sa paghawak ng modelo at pagproseso.

2. **Pag-load at Pagpapakita ng Larawan**:
   - Binubuksan ang isang image file (`demo.png`) gamit ang `PIL` library at ipinapakita ito.

3. **Pagdeklara ng Prompt**:
   - Gumagawa ng mensahe na naglalaman ng larawan at kahilingan na gumawa ng Python code para iproseso ang larawan at i-save ito gamit ang `plt` (matplotlib).

4. **Pag-load ng Processor**:
   - Ina-load ang `AutoProcessor` mula sa pretrained na modelo na tinukoy sa `out_dir` directory. Ang processor na ito ang maghahandle ng text at image inputs.

5. **Paglikha ng Prompt**:
   - Ginagamit ang `apply_chat_template` method para i-format ang mensahe sa isang prompt na angkop para sa modelo.

6. **Pagproseso ng Inputs**:
   - Pinoproseso ang prompt at larawan upang maging tensors na maiintindihan ng modelo.

7. **Pagtatakda ng Generation Arguments**:
   - Itinatakda ang mga argumento para sa proseso ng pag-generate ng modelo, kabilang ang maximum na bilang ng bagong tokens na gagawin at kung gagamitin ba ang sampling sa output.

8. **Pag-generate ng Code**:
   - Gumagawa ang modelo ng Python code base sa inputs at generation arguments. Ginagamit ang `TextStreamer` para hawakan ang output, na nilalaktawan ang prompt at mga special tokens.

9. **Output**:
   - Ipinapakita ang nagawang code, na dapat ay naglalaman ng Python code para iproseso ang larawan at i-save ito ayon sa prompt.

Ipinapakita ng demo na ito kung paano gamitin ang pretrained na modelo gamit ang OpenVino upang gumawa ng code nang dinamiko base sa input ng user at mga larawan.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.