<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T03:33:36+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "pl"
}
-->
# **Kwantyzacja rodziny Phi**

Kwantyzacja modelu odnosi się do procesu mapowania parametrów (takich jak wagi i wartości aktywacji) w modelu sieci neuronowej z szerokiego zakresu wartości (zwykle zakresu ciągłego) na mniejszy skończony zakres wartości. Ta technologia może zmniejszyć rozmiar i złożoność obliczeniową modelu oraz poprawić wydajność działania modelu w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne lub systemy wbudowane. Kwantyzacja modelu osiąga kompresję poprzez zmniejszenie precyzji parametrów, ale jednocześnie wprowadza pewną utratę dokładności. Dlatego w procesie kwantyzacji konieczne jest wyważenie rozmiaru modelu, złożoności obliczeniowej i precyzji. Do powszechnie stosowanych metod kwantyzacji należą kwantyzacja stałoprzecinkowa, kwantyzacja zmiennoprzecinkowa itp. Odpowiednią strategię kwantyzacji można dobrać w zależności od konkretnego scenariusza i potrzeb.

Mamy nadzieję wdrożyć model GenAI na urządzeniach brzegowych i umożliwić większej liczbie urządzeń wejście w scenariusze GenAI, takie jak urządzenia mobilne, AI PC/Copilot+PC oraz tradycyjne urządzenia IoT. Dzięki skwantyzowanym modelom możemy wdrażać je na różnych urządzeniach brzegowych w zależności od konkretnego sprzętu. W połączeniu z frameworkami przyspieszającymi działanie modeli oraz skwantyzowanymi modelami dostarczanymi przez producentów sprzętu, możemy budować lepsze scenariusze aplikacyjne SLM.

W scenariuszu kwantyzacji dysponujemy różnymi precyzjami (INT4, INT8, FP16, FP32). Poniżej znajduje się wyjaśnienie powszechnie stosowanych precyzji kwantyzacji

### **INT4**

Kwantyzacja INT4 to radykalna metoda kwantyzacji, która kwantyzuje wagi i wartości aktywacji modelu do 4-bitowych liczb całkowitych. Kwantyzacja INT4 zwykle powoduje większą utratę precyzji ze względu na mniejszy zakres reprezentacji i niższą rozdzielczość. Jednak w porównaniu z kwantyzacją INT8, INT4 może dodatkowo zmniejszyć wymagania dotyczące pamięci i złożoność obliczeniową modelu. Należy zauważyć, że kwantyzacja INT4 jest stosunkowo rzadko stosowana w praktyce, ponieważ zbyt niska precyzja może spowodować znaczące pogorszenie wydajności modelu. Ponadto nie wszystkie układy sprzętowe obsługują operacje INT4, więc przy wyborze metody kwantyzacji należy uwzględnić zgodność sprzętową.

### **INT8**

Kwantyzacja INT8 polega na przekształceniu wag i aktywacji modelu z reprezentacji zmiennoprzecinkowej na 8-bitowe liczby całkowite. Chociaż zakres wartości reprezentowany przez liczby INT8 jest mniejszy i mniej precyzyjny, może to znacząco zmniejszyć wymagania dotyczące przechowywania i obliczeń. W kwantyzacji INT8 wagi i wartości aktywacji modelu przechodzą proces kwantyzacji, obejmujący skalowanie i przesunięcie, aby jak najbardziej zachować oryginalne informacje zmiennoprzecinkowe. Podczas inferencji te skwantyzowane wartości są dekwantyzowane z powrotem do postaci zmiennoprzecinkowej do obliczeń, a następnie ponownie kwantyzowane do INT8 na kolejny krok. Ta metoda może zapewnić wystarczającą dokładność w większości zastosowań przy zachowaniu wysokiej wydajności obliczeniowej.

### **FP16**

Format FP16, czyli 16-bitowe liczby zmiennoprzecinkowe (float16), zmniejsza zapotrzebowanie na pamięć o połowę w porównaniu z 32-bitowymi liczbami zmiennoprzecinkowymi (float32), co ma istotne zalety w dużych zastosowaniach uczenia głębokiego. Format FP16 umożliwia ładowanie większych modeli lub przetwarzanie większej ilości danych w ramach tych samych ograniczeń pamięci GPU. W miarę jak nowoczesny sprzęt GPU coraz szerzej wspiera operacje FP16, użycie formatu FP16 może również przynieść poprawę szybkości obliczeń. Jednak format FP16 ma również swoje wady, mianowicie niższą precyzję, co w niektórych przypadkach może prowadzić do niestabilności numerycznej lub utraty dokładności.

### **FP32**

Format FP32 zapewnia wyższą precyzję i może dokładnie reprezentować szeroki zakres wartości. W scenariuszach, gdzie wykonywane są złożone operacje matematyczne lub wymagane są wyniki o wysokiej precyzji, preferowany jest format FP32. Jednak wysoka dokładność wiąże się również z większym wykorzystaniem pamięci i dłuższym czasem obliczeń. W przypadku dużych modeli uczenia głębokiego, zwłaszcza gdy występuje wiele parametrów modelu i ogromne ilości danych, format FP32 może powodować niewystarczającą pamięć GPU lub spadek szybkości inferencji.

Na urządzeniach mobilnych lub IoT możemy konwertować modele Phi-3.x do INT4, podczas gdy AI PC / Copilot PC mogą używać wyższych precyzji, takich jak INT8, FP16, FP 32.

Obecnie różni producenci sprzętu oferują różne frameworki wspierające modele generatywne, takie jak Intel OpenVINO, Qualcomm QNN, Apple MLX oraz Nvidia CUDA itd., które w połączeniu z kwantyzacją modelu umożliwiają lokalne wdrożenie.

Pod względem technologii po kwantyzacji mamy wsparcie różnych formatów, takich jak format PyTorch / TensorFlow, GGUF oraz ONNX. Wykonałem porównanie formatów i scenariuszy zastosowań między GGUF a ONNX. Tutaj rekomenduję format kwantyzacji ONNX, który ma dobre wsparcie od frameworków modelowych po sprzęt. W tym rozdziale skupimy się na ONNX Runtime for GenAI, OpenVINO oraz Apple MLX w celu przeprowadzenia kwantyzacji modelu (jeśli masz lepszy sposób, możesz również przesłać go do nas poprzez zgłoszenie PR).

**Ten rozdział obejmuje**

1. [Kwantyzacja Phi-3.5 / 4 przy użyciu llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kwantyzacja Phi-3.5 / 4 przy użyciu rozszerzeń Generative AI dla onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kwantyzacja Phi-3.5 / 4 przy użyciu Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kwantyzacja Phi-3.5 / 4 przy użyciu frameworku Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zrzeczenie się odpowiedzialności:
Ten dokument został przetłumaczony z użyciem usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenia były poprawne, należy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za wersję autorytatywną. W przypadku informacji istotnych o znaczeniu krytycznym zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->