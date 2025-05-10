<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:25:21+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "pl"
}
-->
# **Kwantyfikacja rodziny Phi**

Kwantyzacja modelu odnosi się do procesu mapowania parametrów (takich jak wagi i wartości aktywacji) w modelu sieci neuronowej z szerokiego zakresu wartości (zwykle ciągłego) na mniejszy, skończony zakres wartości. Ta technologia pozwala zmniejszyć rozmiar i złożoność obliczeniową modelu oraz poprawić jego wydajność w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne czy systemy wbudowane. Kwantyzacja modelu osiąga kompresję przez redukcję precyzji parametrów, ale wprowadza też pewne straty dokładności. Dlatego w procesie kwantyzacji należy wyważyć rozmiar modelu, złożoność obliczeniową oraz precyzję. Do popularnych metod kwantyzacji należą kwantyzacja stałoprzecinkowa, zmiennoprzecinkowa itp. W zależności od konkretnego scenariusza i potrzeb można wybrać odpowiednią strategię kwantyzacji.

Chcemy wdrożyć model GenAI na urządzenia brzegowe i umożliwić większej liczbie urządzeń udział w scenariuszach GenAI, takich jak urządzenia mobilne, AI PC/Copilot+PC oraz tradycyjne urządzenia IoT. Dzięki modelowi kwantyzacji możemy wdrażać go na różnych urządzeniach brzegowych w zależności od sprzętu. W połączeniu z frameworkiem przyspieszającym model oraz modelem kwantyzacji dostarczanym przez producentów sprzętu, możemy tworzyć lepsze scenariusze zastosowań SLM.

W scenariuszu kwantyzacji mamy różne precyzje (INT4, INT8, FP16, FP32). Poniżej znajduje się wyjaśnienie najczęściej stosowanych precyzji kwantyzacji.

### **INT4**

Kwantyzacja INT4 to radykalna metoda, która kwantyzuje wagi i wartości aktywacji modelu do 4-bitowych liczb całkowitych. Kwantyzacja INT4 zwykle skutkuje większą utratą precyzji ze względu na mniejszy zakres reprezentacji i niższą dokładność. Jednak w porównaniu do kwantyzacji INT8, INT4 pozwala jeszcze bardziej zmniejszyć wymagania dotyczące pamięci i złożoność obliczeniową modelu. Należy zauważyć, że kwantyzacja INT4 jest stosunkowo rzadka w praktyce, ponieważ zbyt niska dokładność może znacząco pogorszyć wydajność modelu. Dodatkowo nie każdy sprzęt obsługuje operacje INT4, więc przy wyborze metody kwantyzacji trzeba uwzględnić kompatybilność sprzętową.

### **INT8**

Kwantyzacja INT8 polega na konwersji wag i wartości aktywacji modelu z liczb zmiennoprzecinkowych na 8-bitowe liczby całkowite. Chociaż zakres liczbowy reprezentowany przez liczby INT8 jest mniejszy i mniej precyzyjny, pozwala to znacząco zmniejszyć wymagania dotyczące pamięci i obliczeń. W kwantyzacji INT8 wagi i wartości aktywacji przechodzą proces kwantyzacji, obejmujący skalowanie i przesunięcie, aby jak najlepiej zachować informacje z oryginalnych liczb zmiennoprzecinkowych. Podczas inferencji te skwantyzowane wartości są dekwantyzowane z powrotem do liczb zmiennoprzecinkowych do obliczeń, a następnie ponownie kwantyzowane do INT8 na kolejny etap. Ta metoda zapewnia wystarczającą dokładność w większości zastosowań przy zachowaniu wysokiej efektywności obliczeniowej.

### **FP16**

Format FP16, czyli 16-bitowe liczby zmiennoprzecinkowe (float16), zmniejsza zużycie pamięci o połowę w porównaniu do 32-bitowych liczb zmiennoprzecinkowych (float32), co stanowi istotną zaletę w dużych zastosowaniach uczenia głębokiego. Format FP16 pozwala na ładowanie większych modeli lub przetwarzanie większej ilości danych w ramach tych samych ograniczeń pamięci GPU. Wraz z rosnącym wsparciem sprzętowym dla operacji FP16 na nowoczesnych GPU, użycie formatu FP16 może również przyspieszyć obliczenia. Jednak format FP16 ma też swoje wady, przede wszystkim niższą precyzję, co w niektórych przypadkach może prowadzić do niestabilności numerycznej lub utraty dokładności.

### **FP32**

Format FP32 zapewnia wyższą precyzję i potrafi dokładnie reprezentować szeroki zakres wartości. W scenariuszach, gdzie wykonywane są złożone operacje matematyczne lub wymagane są wyniki o wysokiej dokładności, preferowany jest format FP32. Jednak wysoka precyzja wiąże się z większym zużyciem pamięci i dłuższym czasem obliczeń. W przypadku dużych modeli uczenia głębokiego, zwłaszcza gdy jest dużo parametrów i ogromne ilości danych, format FP32 może powodować niewystarczającą pamięć GPU lub spowolnienie inferencji.

Na urządzeniach mobilnych lub IoT możemy konwertować modele Phi-3.x do INT4, podczas gdy AI PC / Copilot PC mogą korzystać z wyższej precyzji, takiej jak INT8, FP16, FP32.

Obecnie różni producenci sprzętu oferują różne frameworki wspierające modele generatywne, takie jak Intel OpenVINO, Qualcomm QNN, Apple MLX czy Nvidia CUDA, które w połączeniu z kwantyzacją modeli umożliwiają lokalne wdrożenia.

Pod względem technicznym mamy wsparcie dla różnych formatów po kwantyzacji, takich jak PyTorch / Tensorflow, GGUF oraz ONNX. Przeprowadziłem porównanie formatów oraz scenariuszy zastosowań między GGUF a ONNX. Polecam format kwantyzacji ONNX, który jest dobrze wspierany od frameworku modelu aż po sprzęt. W tym rozdziale skupimy się na ONNX Runtime dla GenAI, OpenVINO oraz Apple MLX do przeprowadzania kwantyzacji modeli (jeśli masz lepsze rozwiązanie, możesz je zaproponować przez zgłoszenie PR).

**Ten rozdział obejmuje**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uważany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.