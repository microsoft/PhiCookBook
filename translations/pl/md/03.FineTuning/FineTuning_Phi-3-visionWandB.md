<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:09:40+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "pl"
}
-->
# Phi-3-Vision-128K-Instruct Przegląd Projektu

## Model

Phi-3-Vision-128K-Instruct, lekki, nowoczesny model multimodalny, stanowi trzon tego projektu. Należy do rodziny modeli Phi-3 i obsługuje długość kontekstu do 128 000 tokenów. Model został wytrenowany na zróżnicowanym zbiorze danych, który obejmuje dane syntetyczne oraz starannie filtrowane, publicznie dostępne strony internetowe, kładąc nacisk na wysoką jakość i treści wymagające rozumowania. Proces treningu obejmował nadzorowane dostrajanie oraz bezpośrednią optymalizację preferencji, aby zapewnić precyzyjne przestrzeganie instrukcji, a także solidne środki bezpieczeństwa.

## Tworzenie przykładowych danych jest kluczowe z kilku powodów:

1. **Testowanie**: Przykładowe dane pozwalają testować aplikację w różnych scenariuszach bez wpływu na rzeczywiste dane. Jest to szczególnie ważne na etapach rozwoju i testów.

2. **Optymalizacja wydajności**: Dzięki przykładowym danym, które odzwierciedlają skalę i złożoność rzeczywistych danych, można zidentyfikować wąskie gardła wydajności i odpowiednio zoptymalizować aplikację.

3. **Prototypowanie**: Przykładowe dane mogą być użyte do tworzenia prototypów i makiet, co pomaga lepiej zrozumieć wymagania użytkowników i uzyskać ich opinie.

4. **Analiza danych**: W data science przykładowe dane często służą do eksploracyjnej analizy danych, treningu modeli i testowania algorytmów.

5. **Bezpieczeństwo**: Używanie przykładowych danych w środowiskach deweloperskich i testowych pomaga zapobiegać przypadkowemu wyciekowi wrażliwych danych rzeczywistych.

6. **Nauka**: Jeśli uczysz się nowej technologii lub narzędzia, praca na przykładowych danych daje praktyczną możliwość zastosowania zdobytej wiedzy.

Pamiętaj, że jakość przykładowych danych może znacząco wpłynąć na te działania. Powinny one jak najwierniej odzwierciedlać strukturę i zmienność danych rzeczywistych.

### Tworzenie przykładowych danych
[Generate DataSet Script](./CreatingSampleData.md)

## Zbiór danych

Dobrym przykładem przykładowego zbioru danych jest [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (dostępny na Huggingface).  
Przykładowy zbiór danych produktów Burberry wraz z metadanymi dotyczącymi kategorii produktów, ceny i tytułu, zawierający łącznie 3 040 wierszy, z których każdy reprezentuje unikalny produkt. Ten zbiór pozwala nam testować zdolność modelu do rozumienia i interpretacji danych wizualnych, generując opisowy tekst, który oddaje złożone detale wizualne oraz cechy charakterystyczne marki.

**Note:** Możesz użyć dowolnego zbioru danych zawierającego obrazy.

## Złożone rozumowanie

Model musi rozumować na temat cen i nazw, mając do dyspozycji jedynie obraz. Wymaga to od modelu nie tylko rozpoznawania cech wizualnych, ale także zrozumienia ich znaczenia w kontekście wartości produktu i marki. Poprzez syntezę precyzyjnych opisów tekstowych na podstawie obrazów, projekt podkreśla potencjał integracji danych wizualnych w celu zwiększenia wydajności i wszechstronności modeli w zastosowaniach praktycznych.

## Architektura Phi-3 Vision

Architektura modelu to multimodalna wersja Phi-3. Przetwarza zarówno dane tekstowe, jak i obrazowe, integrując te dane w jedną sekwencję dla kompleksowego zrozumienia i generowania. Model używa oddzielnych warstw osadzających (embedding) dla tekstu i obrazów. Tokeny tekstowe są konwertowane na gęste wektory, natomiast obrazy są przetwarzane przez model wizji CLIP w celu wyodrębnienia osadzeń cech. Te osadzenia obrazów są następnie projektowane tak, aby odpowiadały wymiarom osadzeń tekstowych, co pozwala na ich płynne połączenie.

## Integracja osadzeń tekstu i obrazu

Specjalne tokeny w sekwencji tekstowej wskazują miejsca, gdzie powinny zostać wstawione osadzenia obrazów. Podczas przetwarzania te specjalne tokeny są zastępowane odpowiednimi osadzeniami obrazów, co pozwala modelowi traktować tekst i obrazy jako jedną sekwencję. Prompt dla naszego zbioru danych jest sformatowany z użyciem specjalnego tokena <|image|> w następujący sposób:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Przykładowy kod
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.