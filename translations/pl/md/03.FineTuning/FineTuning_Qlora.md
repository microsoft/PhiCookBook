**Dostrajanie Phi-3 za pomocą QLoRA**

Dostrajanie modelu językowego Phi-3 Mini firmy Microsoft przy użyciu [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA pomoże poprawić rozumienie konwersacji oraz generowanie odpowiedzi.

Aby załadować modele w 4 bitach za pomocą transformers i bitsandbytes, musisz zainstalować accelerate oraz transformers ze źródła i upewnić się, że masz najnowszą wersję biblioteki bitsandbytes.

**Przykłady**
- [Dowiedz się więcej dzięki temu przykładowemu notatnikowi](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Przykład skryptu Python do dostrajania](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Przykład dostrajania na Hugging Face Hub z użyciem LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Przykład dostrajania na Hugging Face Hub z użyciem QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.