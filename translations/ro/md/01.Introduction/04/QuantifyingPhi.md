# **Cuantificarea Familiei Phi**

Cuantificarea modelului se referă la procesul de mapare a parametrilor (cum ar fi greutățile și valorile de activare) dintr-un model de rețea neurală dintr-un interval mare de valori (de obicei un interval continuu de valori) într-un interval finit mai mic de valori. Această tehnologie poate reduce dimensiunea și complexitatea computațională a modelului și poate îmbunătăți eficiența de operare a modelului în medii cu resurse limitate, cum ar fi dispozitivele mobile sau sistemele încorporate. Cuantificarea modelului realizează compresia prin reducerea preciziei parametrilor, dar introduce și o anumită pierdere de precizie. Prin urmare, în procesul de cuantificare este necesar să se echilibreze dimensiunea modelului, complexitatea computațională și precizia. Metodele uzuale de cuantificare includ cuantificarea în punct fix, cuantificarea în virgulă flotantă etc. Puteți alege strategia de cuantificare potrivită în funcție de scenariul specific și de nevoi.

Dorim să implementăm modelul GenAI pe dispozitive edge și să permitem mai multor dispozitive să intre în scenarii GenAI, cum ar fi dispozitivele mobile, AI PC/Copilot+PC, și dispozitive IoT tradiționale. Prin intermediul modelului cuantificat, îl putem implementa pe diferite dispozitive edge în funcție de dispozitiv. Combinate cu cadrul de accelerație a modelului și modelul de cuantificare furnizate de producătorii hardware, putem construi scenarii mai bune de aplicații SLM.

În scenariul de cuantificare, avem precizii diferite (INT4, INT8, FP16, FP32). Următorul text oferă o explicație a preciziilor de cuantificare folosite frecvent.

### **INT4**

Cuantificarea INT4 este o metodă radicală care cuantifică greutățile și valorile de activare ale modelului în întregi de 4 biți. Cuantificarea INT4 de obicei rezultă într-o pierdere mai mare de precizie din cauza intervalului de reprezentare mai mic și a preciziei reduse. Totuși, comparativ cu cuantificarea INT8, cuantificarea INT4 poate reduce și mai mult cerințele de stocare și complexitatea de calcul ale modelului. Este important de menționat că cuantificarea INT4 este relativ rară în aplicațiile practice, deoarece o precizie prea scăzută poate cauza o degradare semnificativă a performanței modelului. În plus, nu toate hardware-urile suportă operații INT4, deci trebuie luată în considerare compatibilitatea hardware când se alege o metodă de cuantificare.

### **INT8**

Cuantificarea INT8 este procesul de conversie a greutăților și activărilor unui model din numere în virgulă flotantă în întregi pe 8 biți. Deși intervalul numeric reprezentat de întregii INT8 este mai mic și mai puțin precis, poate reduce semnificativ cerințele de stocare și calcul. În cuantificarea INT8, greutățile și valorile de activare ale modelului trec printr-un proces de cuantificare ce include scalare și offset pentru a păstra cât mai mult informația originală în virgulă flotantă. În timpul inferenței, aceste valori cuantificate sunt transformate înapoi în numere în virgulă flotantă pentru calcule, apoi cuantificate din nou în INT8 pentru pasul următor. Această metodă poate oferi o precizie suficientă în majoritatea aplicațiilor păstrând în același timp o eficiență computațională ridicată.

### **FP16**

Formatul FP16, adică numere în virgulă flotantă pe 16 biți (float16), reduce amprenta de memorie la jumătate în comparație cu numerele pe 32 biți (float32), ceea ce are avantaje semnificative în aplicațiile de învățare profundă la scară largă. Formatul FP16 permite încărcarea unor modele mai mari sau procesarea unui volum mai mare de date în limitele aceleiași memorii GPU. Pe măsură ce hardware-ul GPU modern continuă să suporte operații FP16, folosirea formatului FP16 poate aduce și îmbunătățiri ale vitezei de calcul. Totuși, formatul FP16 are și dezavantajul său inerent, anume precizia mai mică, care poate duce la instabilitate numerică sau pierdere de precizie în unele cazuri.

### **FP32**

Formatul FP32 oferă o precizie mai mare și poate reprezenta corect o gamă largă de valori. În scenariile în care se efectuează operații matematice complexe sau se cer rezultate de înaltă precizie, formatul FP32 este preferat. Totuși, o precizie ridicată implică și un consum mai mare de memorie și un timp de calcul mai lung. Pentru modele de învățare profundă la scară largă, în special când există mulți parametri și un volum mare de date, formatul FP32 poate genera insuficiență de memorie GPU sau o scădere a vitezei de inferență.

Pe dispozitive mobile sau dispozitive IoT, putem converti modelele Phi-3.x la INT4, în timp ce AI PC / Copilot PC pot folosi precizii mai mari, cum ar fi INT8, FP16, FP32.

În prezent, diferiți producători de hardware au cadre diferite pentru a susține modelele generative, cum ar fi OpenVINO de la Intel, QNN de la Qualcomm, MLX de la Apple și CUDA de la Nvidia, combinate cu cuantificarea modelului pentru a realiza implementarea locală.

Din punct de vedere tehnic, avem suport pentru formate diferite după cuantificare, precum formatele PyTorch / TensorFlow, GGUF și ONNX. Am realizat o comparație între formatele GGUF și ONNX și scenariile lor de aplicare. Aici recomand formatul de cuantificare ONNX, care are un suport bun de la cadrul modelului până la hardware. În acest capitol ne vom concentra pe ONNX Runtime pentru GenAI, OpenVINO și Apple MLX pentru efectuarea cuantificării modelului (dacă aveți o metodă mai bună, o puteți propune prin trimiterea unui PR).

**Acest capitol include**

1. [Cuantificarea Phi-3.5 / 4 folosind llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Cuantificarea Phi-3.5 / 4 folosind extensiile Generative AI pentru onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Cuantificarea Phi-3.5 / 4 folosind Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Cuantificarea Phi-3.5 / 4 folosind Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->