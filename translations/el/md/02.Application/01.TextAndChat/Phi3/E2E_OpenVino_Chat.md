[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Αυτός ο κώδικας εξάγει ένα μοντέλο σε μορφή OpenVINO, το φορτώνει και το χρησιμοποιεί για να δημιουργήσει μια απάντηση σε ένα δοσμένο prompt.

1. **Εξαγωγή του Μοντέλου**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Αυτή η εντολή χρησιμοποιεί το εργαλείο `optimum-cli` για να εξάγει ένα μοντέλο στη μορφή OpenVINO, η οποία είναι βελτιστοποιημένη για αποδοτική εκτέλεση inference.  
   - Το μοντέλο που εξάγεται είναι το `"microsoft/Phi-3-mini-4k-instruct"`, και έχει ρυθμιστεί για την εργασία της δημιουργίας κειμένου βάσει προηγούμενου πλαισίου.  
   - Τα βάρη του μοντέλου κβαντίζονται σε 4-bit ακέραιους (`int4`), κάτι που βοηθά στη μείωση του μεγέθους του μοντέλου και στην επιτάχυνση της επεξεργασίας.  
   - Άλλες παράμετροι όπως `group-size`, `ratio` και `sym` χρησιμοποιούνται για την καλύτερη ρύθμιση της διαδικασίας κβαντισμού.  
   - Το εξαγόμενο μοντέλο αποθηκεύεται στον φάκελο `./model/phi3-instruct/int4`.

2. **Εισαγωγή Απαραίτητων Βιβλιοθηκών**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Αυτές οι γραμμές εισάγουν κλάσεις από τη βιβλιοθήκη `transformers` και το module `optimum.intel.openvino`, που χρειάζονται για τη φόρτωση και χρήση του μοντέλου.

3. **Ρύθμιση του Φακέλου Μοντέλου και της Διαμόρφωσης**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - Το `model_dir` καθορίζει πού αποθηκεύονται τα αρχεία του μοντέλου.  
   - Το `ov_config` είναι ένα λεξικό που ρυθμίζει το μοντέλο OpenVINO ώστε να δίνει προτεραιότητα στη χαμηλή καθυστέρηση, να χρησιμοποιεί ένα stream inference και να μην χρησιμοποιεί φάκελο cache.

4. **Φόρτωση του Μοντέλου**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Αυτή η γραμμή φορτώνει το μοντέλο από τον καθορισμένο φάκελο, χρησιμοποιώντας τις ρυθμίσεις που ορίστηκαν προηγουμένως. Επιτρέπει επίσης την εκτέλεση απομακρυσμένου κώδικα αν χρειαστεί.

5. **Φόρτωση του Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Αυτή η γραμμή φορτώνει τον tokenizer, ο οποίος είναι υπεύθυνος για τη μετατροπή του κειμένου σε tokens που μπορεί να κατανοήσει το μοντέλο.

6. **Ρύθμιση Παραμέτρων του Tokenizer**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Αυτό το λεξικό καθορίζει ότι δεν πρέπει να προστεθούν ειδικά tokens στην έξοδο του tokenizer.

7. **Ορισμός του Prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Αυτό το κείμενο ορίζει ένα prompt συνομιλίας όπου ο χρήστης ζητά από τον AI βοηθό να συστηθεί.

8. **Tokenization του Prompt**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Αυτή η γραμμή μετατρέπει το prompt σε tokens που μπορεί να επεξεργαστεί το μοντέλο, επιστρέφοντας το αποτέλεσμα ως PyTorch tensors.

9. **Δημιουργία Απάντησης**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Αυτή η γραμμή χρησιμοποιεί το μοντέλο για να δημιουργήσει μια απάντηση βασισμένη στα εισαγόμενα tokens, με μέγιστο αριθμό 1024 νέων tokens.

10. **Αποκωδικοποίηση της Απάντησης**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Αυτή η γραμμή μετατρέπει τα παραγόμενα tokens πίσω σε αναγνώσιμο κείμενο, παραλείποντας ειδικά tokens, και επιστρέφει το πρώτο αποτέλεσμα.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.