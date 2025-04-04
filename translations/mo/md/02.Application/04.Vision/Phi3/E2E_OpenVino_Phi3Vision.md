<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "69d48385b1f1b31dd20dbb2405031bff",
  "translation_date": "2025-04-04T13:01:55+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_OpenVino_Phi3Vision.md",
  "language_code": "mo"
}
-->
This demo yi faaka gaɓe faɗa yadda za a yi amfani da samfurin da aka horar da shi don samar da lambar Python bisa hoton da kuma rubutun tambaya.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Ga bayanin mataki-mataki:

1. **Shigo da abubuwan da ake bukata da Tsarawa**:
   - Ana shigo da ɗakunan karatu da kuma modules da ake bukata, ciki har da `requests`, `PIL` don sarrafa hotuna, da `transformers` don sarrafa samfurin da kuma aiwatarwa.

2. **Loda da Nuna Hoton**:
   - Ana buɗe fayil ɗin hoto (`demo.png`) ta amfani da ɗakin karatu `PIL` kuma ana nuna shi.

3. **Kirkirar Tambaya**:
   - Saƙo yana ƙirƙirwa wanda ya haɗa da hoton da kuma buƙatar samar da lambar Python don sarrafa hoton da adana shi ta amfani da `plt` (matplotlib).

4. **Loda Processor**:
   - Ana loda `AutoProcessor` daga samfurin da aka horar da shi wanda aka ayyana ta `out_dir` directory. Wannan processor ɗin zai sarrafa rubutu da shigarwar hotuna.

5. **Kirkirar Tambaya**:
   - Ana amfani da `apply_chat_template` don tsara saƙon cikin tambaya da ya dace da samfurin.

6. **Sarrafawa Shigarwa**:
   - Ana sarrafa tambaya da hoton cikin tensors da samfurin zai iya fahimta.

7. **Kafa Zaɓuɓɓukan Samarwa**:
   - Ana ayyana zaɓuɓɓuka don tsarin samarwa na samfurin, ciki har da adadin sabon tokens da za a samar da kuma ko za a yi sampling na fitarwa.

8. **Samar da Lambar**:
   - Samfurin yana samar da lambar Python bisa shigarwar da kuma zaɓuɓɓukan samarwa. Ana amfani da `TextStreamer` don sarrafa fitarwa, yana tsallake tambaya da alamu na musamman.

9. **Fitarwa**:
   - Ana buga lambar da aka samar, wanda yakamata ya haɗa da lambar Python don sarrafa hoton da adana shi kamar yadda aka bayyana a tambaya.

Wannan demo yana nuna yadda za a yi amfani da samfurin da aka horar da shi ta OpenVino don samar da lamba ta atomatik bisa shigarwar mai amfani da hotuna.

It seems you are requesting a translation into "mo." Could you clarify what "mo" refers to? Are you referring to a specific language or dialect? For example, is it Maori, Mongolian, or something else? Please provide more details so I can assist you accurately!