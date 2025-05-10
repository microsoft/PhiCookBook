<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:47:14+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "pl"
}
-->
# Phi-3-Vision-128K-Instruct Przegląd Projektu

## Model

Phi-3-Vision-128K-Instruct, lekki, nowoczesny model multimodalny, stanowi trzon tego projektu. Należy do rodziny modeli Phi-3 i obsługuje długość kontekstu do 128 000 tokenów. Model został wytrenowany na zróżnicowanym zbiorze danych, który obejmuje dane syntetyczne oraz starannie filtrowane, publicznie dostępne strony internetowe, kładąc nacisk na treści wysokiej jakości, wymagające rozumowania. Proces trenowania obejmował nadzorowane dostrajanie oraz bezpośrednią optymalizację preferencji, aby zapewnić precyzyjne przestrzeganie instrukcji, a także solidne środki bezpieczeństwa.

## Tworzenie przykładowych danych jest kluczowe z kilku powodów:

1. **Testowanie**: Przykładowe dane pozwalają testować aplikację w różnych scenariuszach bez wpływu na rzeczywiste dane. Jest to szczególnie ważne na etapach rozwoju i testów przedprodukcyjnych.

2. **Optymalizacja wydajności**: Mając przykładowe dane, które odzwierciedlają skalę i złożoność rzeczywistych danych, można zidentyfikować wąskie gardła wydajności i odpowiednio zoptymalizować aplikację.

3. **Prototypowanie**: Przykładowe dane mogą być używane do tworzenia prototypów i makiet, co pomaga lepiej zrozumieć wymagania użytkowników i uzyskać ich opinię.

4. **Analiza danych**: W data science przykładowe dane często służą do eksploracyjnej analizy danych, trenowania modeli oraz testowania algorytmów.

5. **Bezpieczeństwo**: Używanie przykładowych danych w środowiskach deweloperskich i testowych pomaga zapobiegać przypadkowym wyciekom wrażliwych, rzeczywistych danych.

6. **Nauka**: Jeśli uczysz się nowej technologii lub narzędzia, praca z przykładowymi danymi pozwala praktycznie zastosować zdobytą wiedzę.

Pamiętaj, że jakość przykładowych danych może znacząco wpłynąć na powyższe działania. Powinny one jak najwierniej odzwierciedlać strukturę i zmienność danych rzeczywistych.

### Tworzenie Przykładowych Danych
[Generate DataSet Script](./CreatingSampleData.md)

## Zbiór Danych

Dobrym przykładem przykładowego zbioru danych jest [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (dostępny na Huggingface).  
Przykładowy zbiór danych produktów Burberry wraz z metadanymi dotyczącymi kategorii produktów, ceny i tytułu zawiera łącznie 3 040 wierszy, z których każdy reprezentuje unikalny produkt. Ten zbiór pozwala testować zdolność modelu do rozumienia i interpretacji danych wizualnych, generując opisowy tekst, który oddaje skomplikowane detale wizualne oraz charakterystyczne cechy marki.

**Note:** Możesz użyć dowolnego zbioru danych zawierającego obrazy.

## Złożone Rozumowanie

Model musi rozumować o cenach i nazwach mając do dyspozycji tylko obraz. Wymaga to, aby model nie tylko rozpoznawał cechy wizualne, ale także rozumiał ich znaczenie w kontekście wartości produktu i marki. Poprzez syntezę precyzyjnych opisów tekstowych na podstawie obrazów, projekt pokazuje potencjał integracji danych wizualnych w celu zwiększenia wydajności i wszechstronności modeli w zastosowaniach praktycznych.

## Architektura Phi-3 Vision

Architektura modelu to multimodalna wersja Phi-3. Przetwarza zarówno dane tekstowe, jak i obrazy, integrując te wejścia w jedną sekwencję dla kompleksowego rozumienia i generowania. Model wykorzystuje oddzielne warstwy osadzania (embedding) dla tekstu i obrazów. Tokeny tekstowe są konwertowane na gęste wektory, natomiast obrazy przetwarzane są przez model wizji CLIP w celu wydobycia osadzeń cech. Następnie te osadzenia obrazów są projektowane tak, aby odpowiadały wymiarom osadzeń tekstu, co umożliwia ich bezproblemową integrację.

## Integracja Osadzeń Tekstu i Obrazów

Specjalne tokeny w sekwencji tekstowej wskazują miejsca, w które należy wstawić osadzenia obrazów. Podczas przetwarzania te specjalne tokeny są zastępowane odpowiednimi osadzeniami obrazów, co pozwala modelowi traktować tekst i obrazy jako jedną sekwencję. Prompt dla naszego zbioru danych jest sformatowany przy użyciu specjalnego tokenu <|image|> w następujący sposób:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Przykładowy Kod
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być traktowany jako źródło wiążące. W przypadku informacji o istotnym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.