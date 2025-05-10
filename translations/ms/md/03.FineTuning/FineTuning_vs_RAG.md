<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-05-09T22:16:39+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "ms"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

RAG combines data retrieval with text generation. Both structured and unstructured enterprise data are stored in a vector database. When searching for relevant information, summaries and related content are retrieved to form a context, which is then used alongside the text completion capabilities of LLM/SLM to generate content.

## RAG Process
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.ms.png)

## Fine-tuning
Fine-tuning focuses on improving a specific model. It doesn’t require starting from the model algorithm itself, but data must be continuously accumulated. If you want more precise terminology and language tailored to industry applications, fine-tuning is the better option. However, if your data changes frequently, fine-tuning can become complex.

## How to choose
If your answers require incorporating external data, RAG is the best choice.

If you need to deliver stable and accurate industry knowledge, fine-tuning is a good option. RAG prioritizes retrieving relevant content but may not always capture specialized nuances perfectly.

Fine-tuning requires a high-quality dataset, and if the data scope is small, it won’t make much difference. RAG is more flexible.  
Fine-tuning is a black box, almost metaphysical, making it difficult to understand the internal workings. RAG, on the other hand, makes it easier to trace the data source, which helps effectively address hallucinations or content errors and offers better transparency.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.