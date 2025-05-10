<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:30:32+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "sw"
}
-->
Katika muktadha wa Phi-3-mini, inference inahusu mchakato wa kutumia modeli kutabiri au kutoa matokeo kwa kutumia data ya kuingiza. Niruhusu nikupa maelezo zaidi kuhusu Phi-3-mini na uwezo wake wa inference.

Phi-3-mini ni sehemu ya mfululizo wa modeli za Phi-3 zilizotolewa na Microsoft. Modeli hizi zimeundwa ili kubadilisha kile kinachowezekana na Small Language Models (SLMs).

Hapa kuna mambo muhimu kuhusu Phi-3-mini na uwezo wake wa inference:

## **Muhtasari wa Phi-3-mini:**
- Phi-3-mini ina ukubwa wa parameters wa bilioni 3.8.
- Inaweza kuendeshwa si tu kwenye vifaa vya kawaida vya kompyuta bali pia kwenye vifaa vya edge kama simu za mkononi na vifaa vya IoT.
- Kutolewa kwa Phi-3-mini kunawawezesha watu binafsi na kampuni kuanzisha SLMs kwenye vifaa mbalimbali vya vifaa, hasa katika mazingira yenye rasilimali chache.
- Inashughulikia aina mbalimbali za modeli, ikiwa ni pamoja na muundo wa kawaida wa PyTorch, toleo lililopimwa la muundo wa gguf, na toleo lililopimwa la ONNX.

## **Kupata Phi-3-mini:**
Ili kupata Phi-3-mini, unaweza kutumia [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) katika programu ya Copilot. Semantic Kernel kwa kawaida inalingana na Azure OpenAI Service, modeli za chanzo huria kwenye Hugging Face, na modeli za eneo la karibu.
Unaweza pia kutumia [Ollama](https://ollama.com) au [LlamaEdge](https://llamaedge.com) kuita modeli zilizopimwa. Ollama inaruhusu watumiaji binafsi kuita modeli mbalimbali zilizopimwa, wakati LlamaEdge hutoa upatikanaji wa kuvuka majukwaa kwa modeli za GGUF.

## **Modeli Zilizopimwa:**
Watumiaji wengi wanapendelea kutumia modeli zilizopimwa kwa inference ya eneo la karibu. Kwa mfano, unaweza moja kwa moja kuendesha Ollama run Phi-3 au kuipanga offline kwa kutumia Modelfile. Modelfile inaeleza njia ya faili ya GGUF na muundo wa prompt.

## **Muwezekano wa AI ya Kizazi:**
Kuchanganya SLMs kama Phi-3-mini kunafungua fursa mpya za AI ya kizazi. Inference ni hatua ya kwanza tu; modeli hizi zinaweza kutumika kwa kazi mbalimbali katika mazingira yenye rasilimali chache, ucheleweshaji mdogo, na vizuizi vya gharama.

## **Kufungua AI ya Kizazi na Phi-3-mini: Mwongozo wa Inference na Utekelezaji**  
Jifunze jinsi ya kutumia Semantic Kernel, Ollama/LlamaEdge, na ONNX Runtime kupata na kufanya inference kwa modeli za Phi-3-mini, na gundua fursa za AI ya kizazi katika hali mbalimbali za matumizi.

**Sifa**
Inference ya modeli ya phi3-mini katika:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Kwa muhtasari, Phi-3-mini inawawezesha waendelezaji kuchunguza aina tofauti za modeli na kutumia AI ya kizazi katika hali mbalimbali za matumizi.

**Kiongeza cha kisheria**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebwi na majukumu kwa uelewa au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.