<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:50:17+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "ro"
}
-->
# **Cuantificarea familiei Phi**

Cuantificarea modelului se referă la procesul de mapare a parametrilor (cum ar fi greutățile și valorile de activare) dintr-un model de rețea neuronală de la un interval mare de valori (de obicei un interval continuu) la un interval finit mai mic de valori. Această tehnologie poate reduce dimensiunea și complexitatea computațională a modelului și poate îmbunătăți eficiența de funcționare a modelului în medii cu resurse limitate, cum ar fi dispozitivele mobile sau sistemele încorporate. Cuantificarea modelului realizează compresia prin reducerea preciziei parametrilor, dar introduce și o anumită pierdere de precizie. Prin urmare, în procesul de cuantificare este necesar să se echilibreze dimensiunea modelului, complexitatea calculului și precizia. Metodele comune de cuantificare includ cuantificarea în punct fix, cuantificarea în virgulă mobilă etc. Poți alege strategia de cuantificare potrivită în funcție de scenariul și nevoile specifice.

Ne dorim să implementăm modelul GenAI pe dispozitive edge și să permitem mai multor dispozitive să intre în scenarii GenAI, cum ar fi dispozitive mobile, AI PC/Copilot+PC și dispozitive IoT tradiționale. Prin modelul cuantificat, îl putem implementa pe diferite dispozitive edge în funcție de tipul dispozitivului. Combinat cu cadrul de accelerare a modelului și modelul cuantificat oferit de producătorii de hardware, putem construi scenarii de aplicații SLM mai bune.

În scenariul de cuantificare, avem diferite precizii (INT4, INT8, FP16, FP32). Mai jos este o explicație a preciziilor de cuantificare utilizate frecvent.

### **INT4**

Cuantificarea INT4 este o metodă radicală de cuantificare care transformă greutățile și valorile de activare ale modelului în întregi pe 4 biți. Cuantificarea INT4 duce de obicei la o pierdere mai mare de precizie din cauza intervalului de reprezentare mai mic și a preciziei reduse. Totuși, comparativ cu cuantificarea INT8, INT4 poate reduce și mai mult cerințele de stocare și complexitatea calculului modelului. Trebuie menționat că cuantificarea INT4 este relativ rară în aplicațiile practice, deoarece precizia prea scăzută poate cauza o degradare semnificativă a performanței modelului. În plus, nu toate hardware-urile suportă operațiuni INT4, așa că compatibilitatea hardware trebuie luată în considerare la alegerea metodei de cuantificare.

### **INT8**

Cuantificarea INT8 este procesul de conversie a greutăților și activărilor unui model din numere în virgulă mobilă în întregi pe 8 biți. Deși intervalul numeric reprezentat de întregii INT8 este mai mic și mai puțin precis, aceasta poate reduce semnificativ cerințele de stocare și calcul. În cuantificarea INT8, greutățile și valorile de activare ale modelului trec printr-un proces de cuantificare, care include scalare și offset, pentru a păstra cât mai mult informația originală în virgulă mobilă. În timpul inferenței, aceste valori cuantificate sunt decuantificate înapoi în numere în virgulă mobilă pentru calcul, apoi cuantificate din nou în INT8 pentru pasul următor. Această metodă oferă o precizie suficientă în majoritatea aplicațiilor, menținând în același timp o eficiență computațională ridicată.

### **FP16**

Formatul FP16, adică numerele în virgulă mobilă pe 16 biți (float16), reduce la jumătate amprenta de memorie comparativ cu numerele pe 32 de biți (float32), ceea ce aduce avantaje semnificative în aplicațiile de învățare profundă la scară largă. Formatul FP16 permite încărcarea unor modele mai mari sau procesarea unui volum mai mare de date în limitele aceleiași memorii GPU. Pe măsură ce hardware-ul modern GPU continuă să suporte operațiuni FP16, utilizarea formatului FP16 poate aduce și îmbunătățiri ale vitezei de calcul. Totuși, formatul FP16 are și dezavantajele sale inerente, și anume precizia mai scăzută, care poate duce în unele cazuri la instabilitate numerică sau pierdere de precizie.

### **FP32**

Formatul FP32 oferă o precizie mai mare și poate reprezenta cu acuratețe un interval larg de valori. În scenariile în care se efectuează operații matematice complexe sau sunt necesare rezultate cu precizie ridicată, formatul FP32 este preferat. Totuși, precizia ridicată implică și un consum mai mare de memorie și un timp de calcul mai lung. Pentru modelele de învățare profundă la scară largă, în special când există mulți parametri și un volum uriaș de date, formatul FP32 poate cauza insuficiență de memorie GPU sau scăderea vitezei de inferență.

Pe dispozitive mobile sau IoT, putem converti modelele Phi-3.x în INT4, în timp ce AI PC / Copilot PC pot folosi precizii mai mari, cum ar fi INT8, FP16, FP32.

În prezent, diferiți producători de hardware au cadre diferite pentru a susține modelele generative, cum ar fi OpenVINO de la Intel, QNN de la Qualcomm, MLX de la Apple și CUDA de la Nvidia, combinate cu cuantificarea modelului pentru a realiza implementarea locală.

Din punct de vedere tehnologic, avem suport pentru diferite formate după cuantificare, cum ar fi formatele PyTorch / Tensorflow, GGUF și ONNX. Am realizat o comparație între formatele GGUF și ONNX și scenariile lor de aplicare. Aici recomand formatul de cuantificare ONNX, care are un suport bun de la cadrul modelului până la hardware. În acest capitol, ne vom concentra pe ONNX Runtime pentru GenAI, OpenVINO și Apple MLX pentru a efectua cuantificarea modelului (dacă ai o metodă mai bună, o poți propune printr-un PR).

**Acest capitol include**

1. [Cuantificarea Phi-3.5 / 4 folosind llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Cuantificarea Phi-3.5 / 4 folosind extensiile Generative AI pentru onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Cuantificarea Phi-3.5 / 4 folosind Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Cuantificarea Phi-3.5 / 4 folosind Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.