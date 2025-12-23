<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-12-21T17:21:55+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "pcm"
}
-->
# **Mek Phi-3 be industry expert**

To put the Phi-3 model into an industry, you need to add industry business data to the Phi-3 model. We have two different options, the first is RAG (Retrieval Augmented Generation) and the second is Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG na data retrieval + text generation. Di structured data and unstructured data wey belong to di enterprise dey store for di vector database. When you dey search for relevant content, you go find di relevant summary and content to form context, and di text completion capability of LLM/SLM go combine to generate content.


### **Fine-tuning**

Fine-tuning na to improve one particular model. You no need start from di model algorithm, but you gots dey accumulate data steady. If you want more precise terminology and language expression for industry applications, fine-tuning na your better choice. But if your data dey change quick, fine-tuning fit become complicated.

### **How to choose**

1. If our answer requires the introduction of external data, RAG na the best choice

2. If you need to output stable and precise industry knowledge, fine-tuning go be good choice. RAG dey prioritize pull relevant content but e no go always nail di specialized nuances.

3. Fine-tuning need high-quality data set, and if na only small range of data, e no go make much difference. RAG dey more flexible

4. Fine-tuning na black box, e be like metaphysics, and e hard to understand di internal mechanism. But RAG fit make am easier to find di source of di data, so you fit effectively adjust hallucinations or content errors and give better transparency.


### **Scenarios**

1. Vertical industries need specific professional vocabulary and expressions, ***Fine-tuning*** go be di best choice

2. QA system wey dey involve di synthesis of different knowledge points, ***RAG*** go be di best choice

3. Di combination of automated business flow ***RAG + Fine-tuning*** na di best choice


## **How to use RAG**

![RAG](../../../../translated_images/rag.2014adc59e6f6007bafac13e800a6cbc3e297fbb9903efe20a93129bd13987e9.pcm.png)


A vector database na collection of data wey dem store in mathematical form. Vector databases dey make am easier for machine learning models to remember previous inputs, e dey enable machine learning to support use cases like search, recommendations, and text generation. Data fit dey identified based on similarity metrics rather than exact matches, which allow computer models to understand di context of di data.

Vector database na di key to make RAG work. We fit convert data into vector storage through vector models such as text-embedding-3, jina-ai-embedding, etc.

To sabi more about how to create RAG application [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo) 


## **How to use Fine-tuning**

Di commonly used algorithms for Fine-tuning na Lora and QLora. How to choose?
- [Make you sabi more with dis sample notebook](../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example wey show Python FineTuning sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora and QLora**

![LoRA](../../../../translated_images/qlora.e6446c988ee04ca08807488bb7d9e2c0ea7ef4af9d000fc6d13032b4ac2de18d.pcm.png)


LoRA (Low-Rank Adaptation) and QLoRA (Quantized Low-Rank Adaptation) na techniques wey dem dey use to fine-tune large language models (LLMs) using Parameter Efficient Fine Tuning (PEFT). PEFT techniques dem design make e possible to train models more efficiently than traditional methods. 
LoRA na standalone finetuning technique wey reduce memory footprint by applying a low-rank approximation to di weight update matrix. E dey offer fast training times and e dey maintain performance wey near to traditional fine-tuning methods. 

QLoRA na extended version of LoRA wey incorporate quantization techniques to further reduce memory usage. QLoRA dey quantize di precision of di weight parameters inside di pre-trained LLM to 4-bit precision, wey dey more memory efficient than LoRA. However, QLoRA training dey about 30% slower than LoRA training because of di extra quantization and dequantization steps. 

QLoRA dey use LoRA as accessory to fix di errors wey quantization introduce. QLoRA dey enable fine-tuning of massive models wey get billions of parameters on relatively small, highly available GPUs. For example, QLoRA fit fine-tune one 70B parameter model wey normally require 36 GPUs with only 2

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:

Dis document don translate wit AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get mistakes or no too accurate. The original document for im own language na the authority you suppose follow. If na important mata, e better make professional human translator do am. We no go take responsibility for any misunderstanding or wrong interpretation wey fit happen because of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->