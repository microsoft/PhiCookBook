# **Ποσοτικοποίηση του Phi-3.5 με το Apple MLX Framework**

Το MLX είναι ένα πλαίσιο για μηχανική μάθηση σε Apple silicon, που δημιουργήθηκε από την ομάδα έρευνας μηχανικής μάθησης της Apple.

Το MLX έχει σχεδιαστεί από ερευνητές μηχανικής μάθησης για ερευνητές μηχανικής μάθησης. Το πλαίσιο στοχεύει να είναι φιλικό προς τον χρήστη, αλλά ταυτόχρονα αποδοτικό για την εκπαίδευση και την ανάπτυξη μοντέλων. Ο σχεδιασμός του πλαισίου είναι επίσης απλός σε επίπεδο ιδεών. Σκοπεύουμε να το κάνουμε εύκολο για τους ερευνητές να επεκτείνουν και να βελτιώσουν το MLX, με στόχο την γρήγορη εξερεύνηση νέων ιδεών.

Τα LLMs μπορούν να επιταχυνθούν σε συσκευές Apple Silicon μέσω του MLX, και τα μοντέλα μπορούν να τρέξουν τοπικά με μεγάλη ευκολία.

Τώρα το Apple MLX Framework υποστηρίζει τη μετατροπή ποσοτικοποίησης των Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), και Phi-3.5-MoE (**Apple MLX Framework support**). Ας το δοκιμάσουμε παρακάτω:

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

### **🤖 Παραδείγματα για το Phi-3.5 με Apple MLX**

| Labs    | Εισαγωγή | Μετάβαση |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 Instruct με το Apple MLX framework   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 Vision για ανάλυση εικόνας με το Apple MLX framework     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 MoE με το Apple MLX framework  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Πόροι**

1. Μάθετε για το Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.