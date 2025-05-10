<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:02:16+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "ro"
}
-->
Acest demo arată cum să folosești un model pretrained pentru a genera cod Python pe baza unei imagini și a unui prompt text.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Iată o explicație pas cu pas:

1. **Importuri și configurare**:
   - Sunt importate bibliotecile și modulele necesare, inclusiv `requests`, `PIL` pentru procesarea imaginilor și `transformers` pentru gestionarea modelului și procesare.

2. **Încărcarea și afișarea imaginii**:
   - Un fișier imagine (`demo.png`) este deschis folosind biblioteca `PIL` și afișat.

3. **Definirea promptului**:
   - Este creat un mesaj care include imaginea și o cerere de a genera cod Python pentru a procesa imaginea și a o salva folosind `plt` (matplotlib).

4. **Încărcarea procesorului**:
   - `AutoProcessor` este încărcat dintr-un model pretrained specificat de directorul `out_dir`. Acest procesor va gestiona inputurile text și imagine.

5. **Crearea promptului**:
   - Metoda `apply_chat_template` este folosită pentru a formata mesajul într-un prompt potrivit pentru model.

6. **Procesarea inputurilor**:
   - Promptul și imaginea sunt procesate în tensori pe care modelul îi poate interpreta.

7. **Setarea argumentelor pentru generare**:
   - Sunt definite argumentele pentru procesul de generare al modelului, inclusiv numărul maxim de tokeni noi de generat și dacă se face sampling al rezultatului.

8. **Generarea codului**:
   - Modelul generează codul Python bazat pe inputuri și argumentele de generare. `TextStreamer` este folosit pentru a gestiona outputul, sărind peste prompt și tokenii speciali.

9. **Output**:
   - Codul generat este afișat, acesta ar trebui să includă cod Python pentru procesarea imaginii și salvarea acesteia conform promptului.

Acest demo ilustrează cum să folosești un model pretrained cu OpenVino pentru a genera cod dinamic pe baza inputului utilizatorului și a imaginilor.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.