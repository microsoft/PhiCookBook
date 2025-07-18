<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:46:12+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "pl"
}
-->
# **Kwantyzacja rodziny Phi**

Kwantyzacja modelu odnosi się do procesu mapowania parametrów (takich jak wagi i wartości aktywacji) w modelu sieci neuronowej z szerokiego zakresu wartości (zwykle ciągłego) na mniejszy, skończony zakres wartości. Ta technologia pozwala zmniejszyć rozmiar i złożoność obliczeniową modelu oraz poprawić jego wydajność w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne czy systemy wbudowane. Kwantyzacja modelu osiąga kompresję poprzez obniżenie precyzji parametrów, ale wiąże się to również z pewną utratą dokładności. Dlatego w procesie kwantyzacji konieczne jest wyważenie rozmiaru modelu, złożoności obliczeniowej oraz precyzji. Do popularnych metod kwantyzacji należą kwantyzacja stałoprzecinkowa, zmiennoprzecinkowa itp. Wybór odpowiedniej strategii kwantyzacji zależy od konkretnego scenariusza i potrzeb.

Chcemy wdrożyć model GenAI na urządzeniach brzegowych i umożliwić większej liczbie urządzeń udział w scenariuszach GenAI, takich jak urządzenia mobilne, AI PC/Copilot+PC oraz tradycyjne urządzenia IoT. Dzięki modelowi kwantyzacji możemy wdrażać go na różnych urządzeniach brzegowych w zależności od sprzętu. W połączeniu z frameworkiem przyspieszającym model oraz modelem kwantyzacji dostarczonym przez producentów sprzętu, możemy tworzyć lepsze scenariusze zastosowań SLM.

W scenariuszu kwantyzacji mamy różne precyzje (INT4, INT8, FP16, FP32). Poniżej znajduje się wyjaśnienie najczęściej stosowanych precyzji kwantyzacji.

### **INT4**

Kwantyzacja INT4 to radykalna metoda kwantyzacji, która przekształca wagi i wartości aktywacji modelu na 4-bitowe liczby całkowite. Kwantyzacja INT4 zwykle powoduje większą utratę precyzji ze względu na mniejszy zakres reprezentacji i niższą dokładność. Jednak w porównaniu do kwantyzacji INT8, INT4 pozwala jeszcze bardziej zmniejszyć wymagania dotyczące pamięci i złożoność obliczeniową modelu. Należy zauważyć, że kwantyzacja INT4 jest stosunkowo rzadka w praktyce, ponieważ zbyt niska dokładność może znacząco pogorszyć wydajność modelu. Ponadto nie każdy sprzęt obsługuje operacje INT4, dlatego przy wyborze metody kwantyzacji trzeba uwzględnić kompatybilność sprzętową.

### **INT8**

Kwantyzacja INT8 to proces konwersji wag i aktywacji modelu z liczb zmiennoprzecinkowych na 8-bitowe liczby całkowite. Chociaż zakres liczbowy reprezentowany przez liczby INT8 jest mniejszy i mniej precyzyjny, pozwala to znacznie zmniejszyć wymagania dotyczące pamięci i obliczeń. W kwantyzacji INT8 wagi i wartości aktywacji modelu przechodzą proces kwantyzacji, obejmujący skalowanie i przesunięcie, aby jak najlepiej zachować oryginalne informacje zmiennoprzecinkowe. Podczas inferencji te skwantyzowane wartości są dekwantyzowane z powrotem do liczb zmiennoprzecinkowych do obliczeń, a następnie ponownie kwantyzowane do INT8 na kolejny krok. Ta metoda zapewnia wystarczającą dokładność w większości zastosowań, jednocześnie utrzymując wysoką efektywność obliczeniową.

### **FP16**

Format FP16, czyli 16-bitowe liczby zmiennoprzecinkowe (float16), zmniejsza zużycie pamięci o połowę w porównaniu do 32-bitowych liczb zmiennoprzecinkowych (float32), co ma istotne zalety w dużych zastosowaniach uczenia głębokiego. Format FP16 pozwala na ładowanie większych modeli lub przetwarzanie większej ilości danych w ramach tych samych ograniczeń pamięci GPU. W miarę jak nowoczesny sprzęt GPU coraz lepiej wspiera operacje FP16, użycie tego formatu może również przyspieszyć obliczenia. Jednak format FP16 ma też swoje wady, przede wszystkim niższą precyzję, co w niektórych przypadkach może prowadzić do niestabilności numerycznej lub utraty dokładności.

### **FP32**

Format FP32 oferuje wyższą precyzję i może dokładnie reprezentować szeroki zakres wartości. W scenariuszach, gdzie wykonywane są złożone operacje matematyczne lub wymagane są wyniki o wysokiej precyzji, preferowany jest format FP32. Jednak wysoka dokładność oznacza też większe zużycie pamięci i dłuższy czas obliczeń. W przypadku dużych modeli uczenia głębokiego, zwłaszcza gdy jest wiele parametrów i ogromne ilości danych, format FP32 może powodować niewystarczającą pamięć GPU lub spowolnienie inferencji.

Na urządzeniach mobilnych lub IoT możemy konwertować modele Phi-3.x do INT4, podczas gdy AI PC / Copilot PC mogą korzystać z wyższej precyzji, takiej jak INT8, FP16, FP32.

Obecnie różni producenci sprzętu oferują różne frameworki wspierające modele generatywne, takie jak OpenVINO Intela, QNN Qualcomma, MLX Apple’a czy CUDA Nvidii, które w połączeniu z kwantyzacją modelu umożliwiają lokalne wdrożenie.

Pod względem technologicznym mamy różne formaty wsparcia po kwantyzacji, takie jak formaty PyTorch / Tensorflow, GGUF oraz ONNX. Przygotowałem porównanie formatów i scenariuszy zastosowań między GGUF a ONNX. Polecam format kwantyzacji ONNX, który ma dobre wsparcie od frameworków modelowych aż po sprzęt. W tym rozdziale skupimy się na ONNX Runtime dla GenAI, OpenVINO oraz Apple MLX do przeprowadzania kwantyzacji modelu (jeśli masz lepsze rozwiązanie, możesz je również przesłać, tworząc PR).

**Ten rozdział zawiera**

1. [Kwantyzacja Phi-3.5 / 4 za pomocą llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kwantyzacja Phi-3.5 / 4 za pomocą rozszerzeń Generative AI dla onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kwantyzacja Phi-3.5 / 4 za pomocą Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kwantyzacja Phi-3.5 / 4 za pomocą Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.