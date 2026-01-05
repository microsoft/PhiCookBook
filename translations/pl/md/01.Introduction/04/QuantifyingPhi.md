<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T14:26:57+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "pl"
}
-->
# **Kwotowanie rodziny Phi**

Kwotowanie modelu odnosi się do procesu mapowania parametrów (takich jak wagi i wartości aktywacji) w modelu sieci neuronowej z dużego zakresu wartości (zazwyczaj zakresu ciągłego) na mniejszy skończony zakres wartości. Technologia ta może zmniejszyć rozmiar i złożoność obliczeniową modelu oraz poprawić efektywność działania modelu w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne czy systemy wbudowane. Kwotowanie modelu osiąga kompresję poprzez redukcję precyzji parametrów, ale jednocześnie wprowadza pewną utratę dokładności. W związku z tym w procesie kwotowania konieczne jest wyważenie rozmiaru modelu, złożoności obliczeniowej oraz precyzji. Do popularnych metod kwotowania należą kwotowanie stałopunktowe, kwotowanie zmiennoprzecinkowe itp. Możesz wybrać odpowiednią strategię kwotowania zgodnie z konkretnym scenariuszem i potrzebami.

Chcemy wdrożyć model GenAI na urządzenia brzegowe i umożliwić większej liczbie urządzeń wejście w scenariusze GenAI, takie jak urządzenia mobilne, AI PC/Copilot+PC oraz tradycyjne urządzenia IoT. Poprzez model kwotowania możemy wdrażać go na różnych urządzeniach brzegowych w zależności od różnych urządzeń. W połączeniu z ramami przyspieszającymi model i modelem kwotowania dostarczonymi przez producentów sprzętu, możemy budować lepsze scenariusze aplikacji SLM.

W scenariuszu kwotowania mamy różne precyzje (INT4, INT8, FP16, FP32). Poniżej znajduje się wyjaśnienie powszechnie używanych precyzji kwotowania

### **INT4**

Kwotowanie INT4 to radykalna metoda kwotowania, która kwantyfikuje wagi i wartości aktywacji modelu do 4-bitowych liczb całkowitych. Kwotowanie INT4 zazwyczaj powoduje większą utratę precyzji ze względu na mniejszy zakres reprezentacji i niższą precyzję. Jednak w porównaniu z kwotowaniem INT8, kwotowanie INT4 może jeszcze bardziej zmniejszyć wymagania dotyczące pamięci i złożoność obliczeniową modelu. Należy zauważyć, że kwotowanie INT4 jest stosunkowo rzadkie w praktycznych zastosowaniach, ponieważ zbyt niska dokładność może powodować znaczne pogorszenie wydajności modelu. Ponadto nie każdy sprzęt obsługuje operacje INT4, dlatego przy wyborze metody kwotowania należy uwzględnić kompatybilność sprzętową.

### **INT8**

Kwotowanie INT8 to proces konwersji wag i aktywacji modelu z liczb zmiennoprzecinkowych na 8-bitowe liczby całkowite. Chociaż zakres liczbowy reprezentowany przez liczby całkowite INT8 jest mniejszy i mniej precyzyjny, może to znacząco zmniejszyć wymagania dotyczące przechowywania i obliczeń. W kwotowaniu INT8 wagi i wartości aktywacji modelu przechodzą proces kwotowania, obejmujący skalowanie i przesunięcie, mający na celu możliwie najlepsze zachowanie oryginalnych informacji zmiennoprzecinkowych. Podczas inferencji te skwantowane wartości zostaną zdekwantowane z powrotem do liczb zmiennoprzecinkowych do obliczeń, a następnie ponownie zakwotowane do INT8 dla kolejnego kroku. Ta metoda może zapewnić wystarczającą dokładność w większości zastosowań przy jednoczesnym utrzymaniu wysokiej wydajności obliczeniowej.

### **FP16**

Format FP16, czyli 16-bitowe liczby zmiennoprzecinkowe (float16), zmniejsza zapotrzebowanie na pamięć o połowę w porównaniu z 32-bitowymi liczbami zmiennoprzecinkowymi (float32), co ma znaczące zalety w zastosowaniach dużych modeli uczenia głębokiego. Format FP16 pozwala na ładowanie większych modeli lub przetwarzanie większej ilości danych w ramach tych samych ograniczeń pamięci GPU. W miarę jak nowoczesny sprzęt GPU coraz bardziej wspiera operacje FP16, użycie formatu FP16 może także przynieść poprawę szybkości obliczeń. Jednak format FP16 ma też swoje wrodzone wady, mianowicie niższą precyzję, która może prowadzić do niestabilności numerycznej lub utraty dokładności w niektórych przypadkach.

### **FP32**

Format FP32 zapewnia wyższą precyzję i może dokładnie reprezentować szeroki zakres wartości. W scenariuszach, w których wykonywane są złożone operacje matematyczne lub wymagane są wyniki o wysokiej precyzji, preferowany jest format FP32. Jednak wysoka dokładność oznacza także większe zużycie pamięci i dłuższy czas obliczeń. W przypadku dużych modeli uczenia głębokiego, zwłaszcza gdy jest wiele parametrów modelu i ogromna ilość danych, format FP32 może powodować niewystarczającą pamięć GPU lub spadek prędkości inferencji.

Na urządzeniach mobilnych lub IoT możemy konwertować modele Phi-3.x do INT4, podczas gdy AI PC / Copilot PC mogą używać wyższej precyzji, takiej jak INT8, FP16, FP32.

Obecnie różni producenci sprzętu mają różne ramy wspierające modele generatywne, takie jak OpenVINO firmy Intel, QNN firmy Qualcomm, MLX firmy Apple i CUDA firmy Nvidia, itp., łączone z kwotowaniem modelu do lokalnego wdrożenia.

Pod względem technicznym mamy różne wsparcie formatów po kwotowaniu, takie jak format PyTorch / TensorFlow, GGUF i ONNX. Wykonałem porównanie formatów i scenariuszy zastosowań między GGUF a ONNX. Tutaj polecam format kwotowania ONNX, który ma dobre wsparcie od ram modelu po sprzęt. W tym rozdziale skupimy się na ONNX Runtime dla GenAI, OpenVINO i Apple MLX w celu wykonania kwotowania modelu (jeśli masz lepszy sposób, możesz go również przekazać, przesyłając PR).

**Ten rozdział zawiera**

1. [Kwotowanie Phi-3.5 / 4 za pomocą llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kwotowanie Phi-3.5 / 4 za pomocą rozszerzeń Generative AI dla onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kwotowanie Phi-3.5 / 4 za pomocą Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kwotowanie Phi-3.5 / 4 za pomocą Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uważany za autorytatywne źródło. W przypadku istotnych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonywanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->