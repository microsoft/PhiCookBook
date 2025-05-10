<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:55:54+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "el"
}
-->
### Παράδειγμα Σεναρίου

Φανταστείτε ότι έχετε μια εικόνα (`demo.png`) και θέλετε να δημιουργήσετε κώδικα Python που θα επεξεργάζεται αυτή την εικόνα και θα αποθηκεύει μια νέα έκδοσή της (`phi-3-vision.jpg`).

Ο παραπάνω κώδικας αυτοματοποιεί αυτή τη διαδικασία:

1. Ρυθμίζοντας το περιβάλλον και τις απαραίτητες ρυθμίσεις.
2. Δημιουργώντας ένα prompt που δίνει οδηγίες στο μοντέλο να δημιουργήσει τον απαιτούμενο κώδικα Python.
3. Στέλνοντας το prompt στο μοντέλο και συλλέγοντας τον παραγόμενο κώδικα.
4. Εξάγοντας και εκτελώντας τον παραγόμενο κώδικα.
5. Εμφανίζοντας τις αρχικές και επεξεργασμένες εικόνες.

Αυτή η προσέγγιση αξιοποιεί τη δύναμη της τεχνητής νοημοσύνης για να αυτοματοποιήσει εργασίες επεξεργασίας εικόνας, καθιστώντας τη διαδικασία πιο εύκολη και γρήγορη για την επίτευξη των στόχων σας.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Ας αναλύσουμε βήμα-βήμα τι κάνει ο συνολικός κώδικας:

1. **Εγκατάσταση Απαιτούμενου Πακέτου**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Αυτή η εντολή εγκαθιστά το πακέτο `langchain_nvidia_ai_endpoints`, εξασφαλίζοντας ότι είναι η πιο πρόσφατη έκδοση.

2. **Εισαγωγή Απαραίτητων Μονάδων**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Αυτές οι εισαγωγές φέρνουν τις απαραίτητες μονάδες για αλληλεπίδραση με τα NVIDIA AI endpoints, ασφαλή διαχείριση κωδικών, αλληλεπίδραση με το λειτουργικό σύστημα και κωδικοποίηση/αποκωδικοποίηση δεδομένων σε μορφή base64.

3. **Ορισμός Κλειδιού API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Αυτός ο κώδικας ελέγχει αν έχει οριστεί η μεταβλητή περιβάλλοντος `NVIDIA_API_KEY`. Αν όχι, ζητά από τον χρήστη να εισάγει με ασφάλεια το κλειδί API.

4. **Ορισμός Μοντέλου και Διαδρομής Εικόνας**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Εδώ ορίζεται το μοντέλο που θα χρησιμοποιηθεί, δημιουργείται ένα στιγμιότυπο `ChatNVIDIA` με το συγκεκριμένο μοντέλο και ορίζεται η διαδρομή προς το αρχείο της εικόνας.

5. **Δημιουργία Κειμενικού Prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Ορίζεται ένα κειμενικό prompt που δίνει οδηγίες στο μοντέλο να δημιουργήσει κώδικα Python για την επεξεργασία μιας εικόνας.

6. **Κωδικοποίηση Εικόνας σε Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Αυτός ο κώδικας διαβάζει το αρχείο εικόνας, το κωδικοποιεί σε base64 και δημιουργεί μια ετικέτα HTML εικόνας με τα κωδικοποιημένα δεδομένα.

7. **Συνδυασμός Κειμένου και Εικόνας σε Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```  
    Εδώ συνδυάζεται το κειμενικό prompt και η ετικέτα HTML της εικόνας σε μια ενιαία συμβολοσειρά.

8. **Δημιουργία Κώδικα με χρήση ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Αυτός ο κώδικας στέλνει το prompt στο `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Εξαγωγή Κώδικα Python από το Παραγόμενο Περιεχόμενο**:
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Αυτός ο κώδικας εξάγει τον πραγματικό κώδικα Python από το παραγόμενο περιεχόμενο αφαιρώντας τη μορφοποίηση markdown.

10. **Εκτέλεση του Παραγόμενου Κώδικα**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Εκτελεί τον εξαγόμενο κώδικα Python ως υποδιαδικασία και συλλέγει την έξοδό του.

11. **Εμφάνιση Εικόνων**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Αυτές οι γραμμές εμφανίζουν τις εικόνες χρησιμοποιώντας το module `IPython.display`.

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.