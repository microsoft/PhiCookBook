Această demonstrație arată cum să folosești un model pretrained pentru a genera cod Python pe baza unei imagini și a unui prompt text.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Iată o explicație pas cu pas:

1. **Importuri și Configurare**:
   - Sunt importate bibliotecile și modulele necesare, inclusiv `requests`, `PIL` pentru procesarea imaginilor și `transformers` pentru gestionarea modelului și procesarea datelor.

2. **Încărcarea și Afișarea Imagini**:
   - Un fișier imagine (`demo.png`) este deschis folosind biblioteca `PIL` și afișat.

3. **Definirea Promptului**:
   - Se creează un mesaj care include imaginea și o cerere de a genera cod Python pentru a procesa imaginea și a o salva folosind `plt` (matplotlib).

4. **Încărcarea Procesorului**:
   - `AutoProcessor` este încărcat dintr-un model pretrained specificat de directorul `out_dir`. Acest procesor va gestiona inputurile de text și imagine.

5. **Crearea Promptului**:
   - Metoda `apply_chat_template` este folosită pentru a formata mesajul într-un prompt potrivit pentru model.

6. **Procesarea Inputurilor**:
   - Promptul și imaginea sunt procesate în tensori pe care modelul îi poate înțelege.

7. **Setarea Argumentelor pentru Generare**:
   - Sunt definite argumentele pentru procesul de generare al modelului, inclusiv numărul maxim de tokeni noi de generat și dacă se va face sampling al outputului.

8. **Generarea Codului**:
   - Modelul generează codul Python pe baza inputurilor și a argumentelor de generare. `TextStreamer` este folosit pentru a gestiona outputul, sărind peste prompt și tokenii speciali.

9. **Output**:
   - Codul generat este afișat, acesta ar trebui să includă cod Python pentru procesarea imaginii și salvarea acesteia conform specificațiilor din prompt.

Această demonstrație ilustrează cum să folosești un model pretrained cu OpenVino pentru a genera cod dinamic bazat pe inputul utilizatorului și imagini.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.