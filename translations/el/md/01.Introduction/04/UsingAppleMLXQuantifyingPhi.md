<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:44:28+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "el"
}
-->
# **Ποσοτικοποίηση Phi-3.5 με το Apple MLX Framework**


Το MLX είναι ένα πλαίσιο για μηχανική μάθηση σε Apple silicon, δημιουργημένο από την ομάδα έρευνας μηχανικής μάθησης της Apple.

Το MLX έχει σχεδιαστεί από ερευνητές μηχανικής μάθησης για ερευνητές μηχανικής μάθησης. Το πλαίσιο έχει στόχο να είναι φιλικό προς τον χρήστη, αλλά ταυτόχρονα αποδοτικό για εκπαίδευση και ανάπτυξη μοντέλων. Ο ίδιος ο σχεδιασμός του πλαισίου είναι επίσης απλός στην κατανόηση. Σκοπεύουμε να διευκολύνουμε τους ερευνητές να επεκτείνουν και να βελτιώσουν το MLX, με στόχο την γρήγορη εξερεύνηση νέων ιδεών.

Τα LLMs μπορούν να επιταχυνθούν σε συσκευές Apple Silicon μέσω του MLX, και τα μοντέλα μπορούν να τρέξουν τοπικά με μεγάλη ευκολία.

Τώρα το Apple MLX Framework υποστηρίζει τη μετατροπή ποσοτικοποίησης για Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), και Phi-3.5-MoE (**Apple MLX Framework support**). Ας το δοκιμάσουμε παρακάτω:

### **Phi-3.5-Instruct**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```


### **Phi-3.5-Vision**


```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```



### **🤖 Παραδείγματα για Phi-3.5 με Apple MLX**

| Εργαστήρια    | Εισαγωγή | Μετάβαση |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 Instruct με το Apple MLX framework   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (εικόνα) | Μάθετε πώς να αναλύετε εικόνες με το Phi-3.5 Vision μέσω του Apple MLX framework     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 MoE με το Apple MLX framework  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **Πόροι**

1. Μάθετε για το Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από ανθρώπινο μεταφραστή. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.