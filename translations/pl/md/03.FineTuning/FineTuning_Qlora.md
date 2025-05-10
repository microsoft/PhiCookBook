<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:52:01+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "pl"
}
-->
**Dostrajanie Phi-3 za pomocą QLoRA**

Dostrajanie modelu językowego Phi-3 Mini firmy Microsoft z użyciem [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA pomoże poprawić rozumienie konwersacji oraz generowanie odpowiedzi.

Aby ładować modele w 4 bitach za pomocą transformers i bitsandbytes, musisz zainstalować accelerate oraz transformers ze źródła i upewnić się, że masz najnowszą wersję biblioteki bitsandbytes.

**Przykłady**
- [Dowiedz się więcej z tego przykładowego notatnika](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Przykład skryptu Python do FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Przykład dostrajania na Hugging Face Hub z LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Przykład dostrajania na Hugging Face Hub z QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.