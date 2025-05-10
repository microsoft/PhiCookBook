<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-05-09T22:16:45+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "tl"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

Ang RAG ay pinagsamang data retrieval at text generation. Ang structured at unstructured na data ng kumpanya ay nakaimbak sa vector database. Kapag naghahanap ng kaugnay na nilalaman, hinahanap ang kaugnay na buod at nilalaman para mabuo ang konteksto, at pinagsasama ito sa text completion ng LLM/SLM para makabuo ng output.

## RAG Process
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.tl.png)

## Fine-tuning
Ang fine-tuning ay nakabatay sa pagpapabuti ng isang partikular na modelo. Hindi kailangang simulan sa model algorithm, pero kailangang patuloy na mag-ipon ng data. Kung gusto mo ng mas tumpak na terminolohiya at wika sa mga aplikasyon sa industriya, fine-tuning ang mas magandang pagpipilian. Pero kung madalas magbago ang data, magiging komplikado ang fine-tuning.

## How to choose
Kung kailangan ng sagot na may kasamang panlabas na data, RAG ang pinakamainam na piliin.

Kung kailangan ng matatag at eksaktong kaalaman sa industriya, magandang piliin ang fine-tuning. Pinaprioritize ng RAG ang paghahanap ng kaugnay na nilalaman pero maaaring hindi palaging tama ang mga espesyalisadong detalye.

Ang fine-tuning ay nangangailangan ng mataas na kalidad na dataset, at kung maliit lang ang saklaw ng data, hindi ito gaanong makakaapekto. Mas flexible ang RAG.

Ang fine-tuning ay parang black box, isang metaphysics, at mahirap maintindihan ang internal na mekanismo. Pero ang RAG ay mas madaling matunton ang pinanggalingan ng data, kaya mas epektibong maiaayos ang mga hallucination o mali sa nilalaman at nagbibigay ng mas malinaw na transparency.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.