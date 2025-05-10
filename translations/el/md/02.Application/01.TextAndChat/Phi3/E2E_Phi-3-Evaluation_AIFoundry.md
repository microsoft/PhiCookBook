<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:30:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "el"
}
-->
# Αξιολόγηση του Fine-tuned μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry με έμφαση στις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft

Αυτό το ολοκληρωμένο δείγμα (E2E) βασίζεται στον οδηγό "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" από την κοινότητα τεχνολογίας της Microsoft.

## Επισκόπηση

### Πώς μπορείτε να αξιολογήσετε την ασφάλεια και την απόδοση ενός fine-tuned μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry;

Η προσαρμογή ενός μοντέλου μπορεί μερικές φορές να οδηγήσει σε απρόβλεπτες ή ανεπιθύμητες απαντήσεις. Για να διασφαλιστεί ότι το μοντέλο παραμένει ασφαλές και αποτελεσματικό, είναι σημαντικό να αξιολογηθεί η πιθανότητα δημιουργίας επιβλαβούς περιεχομένου και η ικανότητά του να παράγει ακριβείς, σχετικές και συνεκτικές απαντήσεις. Σε αυτό το μάθημα, θα μάθετε πώς να αξιολογείτε την ασφάλεια και την απόδοση ενός fine-tuned μοντέλου Phi-3 / Phi-3.5 ενσωματωμένου με το Prompt flow στο Azure AI Foundry.

Ακολουθεί η διαδικασία αξιολόγησης του Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.el.png)

*Πηγή εικόνας: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Για πιο αναλυτικές πληροφορίες και για να εξερευνήσετε επιπλέον πόρους σχετικά με τα Phi-3 / Phi-3.5, επισκεφθείτε το [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Προαπαιτούμενα

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned μοντέλο Phi-3 / Phi-3.5

### Πίνακας Περιεχομένων

1. [**Σενάριο 1: Εισαγωγή στην αξιολόγηση Prompt flow του Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Εισαγωγή στην αξιολόγηση ασφάλειας](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Εισαγωγή στην αξιολόγηση απόδοσης](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Σενάριο 2: Αξιολόγηση του μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Πριν ξεκινήσετε](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ανάπτυξη Azure OpenAI για την αξιολόγηση του μοντέλου Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Αξιολόγηση του fine-tuned μοντέλου Phi-3 / Phi-3.5 με την αξιολόγηση Prompt flow του Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Συγχαρητήρια!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Σενάριο 1: Εισαγωγή στην αξιολόγηση Prompt flow του Azure AI Foundry**

### Εισαγωγή στην αξιολόγηση ασφάλειας

Για να διασφαλίσετε ότι το AI μοντέλο σας είναι ηθικό και ασφαλές, είναι κρίσιμο να το αξιολογήσετε με βάση τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft. Στο Azure AI Foundry, οι αξιολογήσεις ασφάλειας σας επιτρέπουν να ελέγξετε την ευπάθεια του μοντέλου σε jailbreak επιθέσεις και την πιθανότητα παραγωγής επιβλαβούς περιεχομένου, κάτι που ευθυγραμμίζεται άμεσα με αυτές τις αρχές.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.el.png)

*Πηγή εικόνας: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Οι Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft

Πριν ξεκινήσετε τα τεχνικά βήματα, είναι σημαντικό να κατανοήσετε τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft, ένα ηθικό πλαίσιο σχεδιασμένο να καθοδηγεί την υπεύθυνη ανάπτυξη, υλοποίηση και λειτουργία συστημάτων AI. Αυτές οι αρχές καθοδηγούν τον υπεύθυνο σχεδιασμό, ανάπτυξη και υλοποίηση των συστημάτων AI, διασφαλίζοντας ότι οι τεχνολογίες AI δημιουργούνται με τρόπο δίκαιο, διαφανή και περιεκτικό. Αποτελούν τη βάση για την αξιολόγηση της ασφάλειας των μοντέλων AI.

Οι Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft περιλαμβάνουν:

- **Δικαιοσύνη και Περιεκτικότητα**: Τα συστήματα AI πρέπει να μεταχειρίζονται όλους δίκαια και να αποφεύγουν να επηρεάζουν διαφορετικά ομάδες με παρόμοια χαρακτηριστικά με διαφορετικό τρόπο. Για παράδειγμα, όταν τα συστήματα AI παρέχουν καθοδήγηση για ιατρική θεραπεία, αιτήσεις δανείων ή απασχόληση, θα πρέπει να δίνουν τις ίδιες προτάσεις σε όλους όσους έχουν παρόμοια συμπτώματα, οικονομικές συνθήκες ή επαγγελματικά προσόντα.

- **Αξιοπιστία και Ασφάλεια**: Για να χτιστεί εμπιστοσύνη, είναι κρίσιμο τα συστήματα AI να λειτουργούν αξιόπιστα, με ασφάλεια και σταθερότητα. Αυτά τα συστήματα πρέπει να λειτουργούν όπως σχεδιάστηκαν αρχικά, να ανταποκρίνονται με ασφάλεια σε απρόβλεπτες συνθήκες και να αντιστέκονται σε επιβλαβείς χειρισμούς. Η συμπεριφορά τους και η ποικιλία των συνθηκών που μπορούν να διαχειριστούν αντανακλούν το εύρος των καταστάσεων που οι προγραμματιστές προέβλεψαν κατά το σχεδιασμό και τις δοκιμές.

- **Διαφάνεια**: Όταν τα συστήματα AI βοηθούν στη λήψη αποφάσεων που επηρεάζουν σημαντικά τις ζωές των ανθρώπων, είναι κρίσιμο οι άνθρωποι να κατανοούν πώς πάρθηκαν αυτές οι αποφάσεις. Για παράδειγμα, μια τράπεζα μπορεί να χρησιμοποιεί σύστημα AI για να αποφασίσει αν ένα άτομο είναι πιστοληπτικό. Μια εταιρεία μπορεί να χρησιμοποιεί AI για να επιλέξει τους πιο κατάλληλους υποψηφίους για πρόσληψη.

- **Ιδιωτικότητα και Ασφάλεια**: Καθώς η AI γίνεται πιο διαδεδομένη, η προστασία της ιδιωτικότητας και η ασφάλεια προσωπικών και επιχειρηματικών δεδομένων γίνονται πιο σημαντικές και σύνθετες. Με την AI, η ιδιωτικότητα και η ασφάλεια δεδομένων απαιτούν στενή προσοχή, επειδή η πρόσβαση στα δεδομένα είναι απαραίτητη για να κάνει το σύστημα ακριβείς και ενημερωμένες προβλέψεις και αποφάσεις για τους ανθρώπους.

- **Λογοδοσία**: Οι άνθρωποι που σχεδιάζουν και υλοποιούν συστήματα AI πρέπει να είναι υπεύθυνοι για τον τρόπο λειτουργίας τους. Οι οργανισμοί θα πρέπει να βασίζονται σε βιομηχανικά πρότυπα για να αναπτύξουν κανόνες λογοδοσίας. Αυτοί οι κανόνες μπορούν να διασφαλίσουν ότι τα συστήματα AI δεν είναι η τελική αρχή σε καμία απόφαση που επηρεάζει τη ζωή των ανθρώπων. Επίσης, διασφαλίζουν ότι οι άνθρωποι διατηρούν ουσιαστικό έλεγχο επί συστημάτων AI που είναι σε μεγάλο βαθμό αυτόνομα.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.el.png)

*Πηγή εικόνας: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Για να μάθετε περισσότερα για τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft, επισκεφθείτε το [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Μετρικές ασφάλειας

Σε αυτό το μάθημα, θα αξιολογήσετε την ασφάλεια του fine-tuned μοντέλου Phi-3 χρησιμοποιώντας τις μετρικές ασφάλειας του Azure AI Foundry. Αυτές οι μετρικές βοηθούν στην εκτίμηση της πιθανότητας του μοντέλου να παράγει επιβλαβές περιεχόμενο και της ευπάθειάς του σε jailbreak επιθέσεις. Οι μετρικές ασφάλειας περιλαμβάνουν:

- **Περιεχόμενο σχετικό με αυτοτραυματισμό**: Αξιολογεί αν το μοντέλο έχει τάση να παράγει περιεχόμενο σχετικό με αυτοτραυματισμό.
- **Μισαλλόδοξο και άδικο περιεχόμενο**: Αξιολογεί αν το μοντέλο έχει τάση να παράγει μισαλλόδοξο ή άδικο περιεχόμενο.
- **Βίαιο περιεχόμενο**: Αξιολογεί αν το μοντέλο έχει τάση να παράγει βίαιο περιεχόμενο.
- **Σεξουαλικό περιεχόμενο**: Αξιολογεί αν το μοντέλο έχει τάση να παράγει ακατάλληλο σεξουαλικό περιεχόμενο.

Η αξιολόγηση αυτών των πτυχών διασφαλίζει ότι το AI μοντέλο δεν παράγει επιβλαβές ή προσβλητικό περιεχόμενο, ευθυγραμμίζοντάς το με τις κοινωνικές αξίες και τα κανονιστικά πρότυπα.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.el.png)

### Εισαγωγή στην αξιολόγηση απόδοσης

Για να διασφαλίσετε ότι το AI μοντέλο σας αποδίδει όπως αναμένεται, είναι σημαντικό να αξιολογήσετε την απόδοσή του με βάση τις μετρικές απόδοσης. Στο Azure AI Foundry, οι αξιολογήσεις απόδοσης σας επιτρέπουν να εκτιμήσετε την αποτελεσματικότητα του μοντέλου στην παραγωγή ακριβών, σχετικών και συνεκτικών απαντήσεων.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.el.png)

*Πηγή εικόνας: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Μετρικές απόδοσης

Σε αυτό το μάθημα, θα αξιολογήσετε την απόδοση του fine-tuned μοντέλου Phi-3 / Phi-3.5 χρησιμοποιώντας τις μετρικές απόδοσης του Azure AI Foundry. Αυτές οι μετρικές βοηθούν στην εκτίμηση της αποτελεσματικότητας του μοντέλου στην παραγωγή ακριβών, σχετικών και συνεκτικών απαντήσεων. Οι μετρικές απόδοσης περιλαμβάνουν:

- **Επίκληση στο υπόβαθρο (Groundedness)**: Αξιολογεί πόσο καλά οι παραγόμενες απαντήσεις ευθυγραμμίζονται με τις πληροφορίες από την πηγή εισόδου.
- **Σχετικότητα**: Αξιολογεί τη συνάφεια των παραγόμενων απαντήσεων με τις δοθείσες ερωτήσεις.
- **Συνεκτικότητα**: Αξιολογεί πόσο ομαλή είναι η ροή του παραγόμενου κειμένου, πόσο φυσική η ανάγνωσή του και πόσο μοιάζει με ανθρώπινη γλώσσα.
- **Ροή λόγου (Fluency)**: Αξιολογεί την γλωσσική επάρκεια του παραγόμενου κειμένου.
- **Ομοιότητα με GPT (GPT Similarity)**: Συγκρίνει την παραγόμενη απάντηση με την αλήθεια βάσης για ομοιότητα.
- **Βαθμολογία F1 (F1 Score)**: Υπολογίζει το ποσοστό κοινών λέξεων μεταξύ της παραγόμενης απάντησης και των δεδομένων πηγής.

Αυτές οι μετρικές σας βοηθούν να αξιολογήσετε την αποτελεσματικότητα του μοντέλου στην παραγωγή ακριβών, σχετικών και συνεκτικών απαντήσεων.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.el.png)

## **Σενάριο 2: Αξιολόγηση του μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry**

### Πριν ξεκινήσετε

Αυτό το μάθημα αποτελεί συνέχεια των προηγούμενων δημοσιεύσεων στο blog, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" και "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Σε αυτές τις δημοσιεύσεις, περιγράψαμε τη διαδικασία fine-tuning ενός μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry και την ενσωμάτωσή του με το Prompt flow.

Σε αυτό το μάθημα, θα αναπτύξετε ένα μοντέλο Azure OpenAI ως αξιολογητή στο Azure AI Foundry και θα το χρησιμοποιήσετε για να αξιολογήσετε το fine-tuned μοντέλο Phi-3 / Phi-3.5.

Πριν ξεκινήσετε, βεβαιωθείτε ότι έχετε τα ακόλουθα προαπαιτούμενα, όπως περιγράφονται στα προηγούμενα μαθήματα:

1. Ένα προετοιμασμένο σύνολο δεδομένων για την αξιολόγηση του fine-tuned μοντέλου Phi-3 / Phi-3.5.
1. Ένα μοντέλο Phi-3 / Phi-3.5 που έχει fine-tuned και αναπτυχθεί στο Azure Machine Learning.
1. Ένα Prompt flow ενσωματωμένο με το fine-tuned μοντέλο Phi-3 / Phi-3.5 στο Azure AI Foundry.

> [!NOTE]
> Θα χρησιμοποιήσετε το αρχείο *test_data.jsonl*, που βρίσκεται στον φάκελο δεδομένων από το σύνολο δεδομένων **ULTRACHAT_200k** που κατεβάσατε στα προηγούμενα άρθρα, ως το σύνολο δεδομένων για την αξιολόγηση του fine-tuned μοντέλου Phi-3 / Phi-3.5.

#### Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 / Phi-3.5 με το Prompt flow στο Azure AI Foundry (προσέγγιση με κώδικα)

> [!NOTE]
> Εάν ακολουθήσατε την προσέγγιση χαμηλού κώδικα που περιγράφεται στο "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", μπορείτε να παραλείψετε αυτή την άσκηση και να προχωρήσετε στην επόμενη.
> Ωστόσο, αν ακολουθήσατε την προσέγγιση με κώδικα που περιγράφεται στο "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" για το fine-tuning και την ανάπτυξη του μοντέλου Phi-3 / Phi-3.5, η διαδικασία σύνδεσης του μοντέλου με το Prompt flow είναι ελαφρώς διαφορε
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.el.png)

1. Επιλέξτε **Next**.

#### Δημιουργία έργου Azure AI Foundry

1. Στο Hub που δημιουργήσατε, επιλέξτε **All projects** από την αριστερή καρτέλα.

1. Επιλέξτε **+ New project** από το μενού πλοήγησης.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.el.png)

1. Εισαγάγετε **Project name**. Πρέπει να είναι μια μοναδική τιμή.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.el.png)

1. Επιλέξτε **Create a project**.

#### Προσθήκη προσαρμοσμένης σύνδεσης για το fine-tuned μοντέλο Phi-3 / Phi-3.5

Για να ενσωματώσετε το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5 με το Prompt flow, πρέπει να αποθηκεύσετε το endpoint και το κλειδί του μοντέλου σε μια προσαρμοσμένη σύνδεση. Αυτή η ρύθμιση εξασφαλίζει την πρόσβαση στο προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5 μέσα στο Prompt flow.

#### Ορισμός api key και endpoint uri για το fine-tuned μοντέλο Phi-3 / Phi-3.5

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Μεταβείτε στο Azure Machine learning workspace που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την αριστερή καρτέλα.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.el.png)

1. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.el.png)

1. Επιλέξτε **Consume** από το μενού πλοήγησης.

1. Αντιγράψτε το **REST endpoint** και το **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.el.png)

#### Προσθήκη της προσαρμοσμένης σύνδεσης

1. Επισκεφθείτε το [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

1. Στο έργο που δημιουργήσατε, επιλέξτε **Settings** από την αριστερή καρτέλα.

1. Επιλέξτε **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.el.png)

1. Επιλέξτε **Custom keys** από το μενού πλοήγησης.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **+ Add key value pairs**.
    - Για το όνομα κλειδιού, εισάγετε **endpoint** και επικολλήστε το endpoint που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Επιλέξτε ξανά **+ Add key value pairs**.
    - Για το όνομα κλειδιού, εισάγετε **key** και επικολλήστε το κλειδί που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Μετά την προσθήκη των κλειδιών, επιλέξτε **is secret** για να αποτρέψετε την έκθεση του κλειδιού.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.el.png)

1. Επιλέξτε **Add connection**.

#### Δημιουργία Prompt flow

Έχετε προσθέσει μια προσαρμοσμένη σύνδεση στο Azure AI Foundry. Τώρα, ας δημιουργήσουμε ένα Prompt flow ακολουθώντας τα παρακάτω βήματα. Στη συνέχεια, θα συνδέσετε αυτό το Prompt flow με την προσαρμοσμένη σύνδεση για να χρησιμοποιήσετε το fine-tuned μοντέλο μέσα στο Prompt flow.

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

1. Επιλέξτε **Prompt flow** από την αριστερή καρτέλα.

1. Επιλέξτε **+ Create** από το μενού πλοήγησης.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.el.png)

1. Επιλέξτε **Chat flow** από το μενού πλοήγησης.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.el.png)

1. Εισαγάγετε **Folder name** που θα χρησιμοποιήσετε.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.el.png)

1. Επιλέξτε **Create**.

#### Ρύθμιση Prompt flow για συνομιλία με το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5

Πρέπει να ενσωματώσετε το fine-tuned μοντέλο Phi-3 / Phi-3.5 σε ένα Prompt flow. Ωστόσο, το υπάρχον Prompt flow που παρέχεται δεν είναι σχεδιασμένο για αυτό το σκοπό. Επομένως, πρέπει να ανασχεδιάσετε το Prompt flow ώστε να επιτρέπεται η ενσωμάτωση του προσαρμοσμένου μοντέλου.

1. Στο Prompt flow, εκτελέστε τις παρακάτω ενέργειες για να αναδημιουργήσετε την υπάρχουσα ροή:

    - Επιλέξτε **Raw file mode**.
    - Διαγράψτε όλο τον υπάρχοντα κώδικα στο αρχείο *flow.dag.yml*.
    - Προσθέστε τον παρακάτω κώδικα στο *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Επιλέξτε **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.el.png)

1. Προσθέστε τον παρακάτω κώδικα στο *integrate_with_promptflow.py* για να χρησιμοποιήσετε το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5 στο Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.el.png)

> [!NOTE]
> Για περισσότερες λεπτομέρειες σχετικά με τη χρήση του Prompt flow στο Azure AI Foundry, μπορείτε να ανατρέξετε στο [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Επιλέξτε **Chat input**, **Chat output** για να ενεργοποιήσετε τη συνομιλία με το μοντέλο σας.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.el.png)

1. Τώρα είστε έτοιμοι να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5. Στην επόμενη άσκηση, θα μάθετε πώς να ξεκινήσετε το Prompt flow και να το χρησιμοποιήσετε για να συνομιλήσετε με το fine-tuned μοντέλο σας.

> [!NOTE]
>
> Η αναδημιουργημένη ροή θα πρέπει να μοιάζει με την εικόνα παρακάτω:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.el.png)
>

#### Εκκίνηση Prompt flow

1. Επιλέξτε **Start compute sessions** για να ξεκινήσετε το Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.el.png)

1. Επιλέξτε **Validate and parse input** για να ανανεώσετε τις παραμέτρους.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.el.png)

1. Επιλέξτε την **Value** της **connection** στην προσαρμοσμένη σύνδεση που δημιουργήσατε. Για παράδειγμα, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.el.png)

#### Συνομιλία με το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5

1. Επιλέξτε **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.el.png)

1. Ακολουθεί ένα παράδειγμα αποτελεσμάτων: Τώρα μπορείτε να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3 / Phi-3.5. Συνιστάται να κάνετε ερωτήσεις βασισμένες στα δεδομένα που χρησιμοποιήθηκαν για το fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.el.png)

### Ανάπτυξη Azure OpenAI για αξιολόγηση του μοντέλου Phi-3 / Phi-3.5

Για να αξιολογήσετε το μοντέλο Phi-3 / Phi-3.5 στο Azure AI Foundry, πρέπει να αναπτύξετε ένα μοντέλο Azure OpenAI. Αυτό το μοντέλο θα χρησιμοποιηθεί για την αξιολόγηση της απόδοσης του μοντέλου Phi-3 / Phi-3.5.

#### Ανάπτυξη Azure OpenAI

1. Συνδεθείτε στο [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.el.png)

1. Στο έργο που δημιουργήσατε, επιλέξτε **Deployments** από την αριστερή καρτέλα.

1. Επιλέξτε **+ Deploy model** από το μενού πλοήγησης.

1. Επιλέξτε **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.el.png)

1. Επιλέξτε το Azure OpenAI μοντέλο που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.el.png)

1. Επιλέξτε **Confirm**.

### Αξιολόγηση του fine-tuned μοντέλου Phi-3 / Phi-3.5 χρησιμοποιώντας την αξιολόγηση Prompt flow του Azure AI Foundry

### Ξεκινήστε μια νέα αξιολόγηση

1. Επισκεφθείτε το [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.el.png)

1. Στο έργο που δημιουργήσατε, επιλέξτε **Evaluation** από την αριστερή καρτέλα.

1. Επιλέξτε **+ New evaluation** από το μενού πλοήγησης.
![Select evaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.el.png)

1. Επιλέξτε την αξιολόγηση **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.el.png)

1. Εκτελέστε τις ακόλουθες εργασίες:

    - Εισάγετε το όνομα της αξιολόγησης. Πρέπει να είναι μια μοναδική τιμή.
    - Επιλέξτε **Question and answer without context** ως τύπο εργασίας. Επειδή το σύνολο δεδομένων **UlTRACHAT_200k** που χρησιμοποιείται σε αυτό το σεμινάριο δεν περιέχει πλαίσιο.
    - Επιλέξτε το prompt flow που θέλετε να αξιολογήσετε.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.el.png)

1. Επιλέξτε **Next**.

1. Εκτελέστε τις ακόλουθες εργασίες:

    - Επιλέξτε **Add your dataset** για να ανεβάσετε το σύνολο δεδομένων. Για παράδειγμα, μπορείτε να ανεβάσετε το αρχείο δοκιμαστικού συνόλου δεδομένων, όπως *test_data.json1*, που περιλαμβάνεται κατά τη λήψη του συνόλου δεδομένων **ULTRACHAT_200k**.
    - Επιλέξτε τη σωστή **Dataset column** που ταιριάζει με το σύνολο δεδομένων σας. Για παράδειγμα, αν χρησιμοποιείτε το σύνολο δεδομένων **ULTRACHAT_200k**, επιλέξτε **${data.prompt}** ως στήλη δεδομένων.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.el.png)

1. Επιλέξτε **Next**.

1. Εκτελέστε τις ακόλουθες εργασίες για να ρυθμίσετε τα metrics απόδοσης και ποιότητας:

    - Επιλέξτε τα metrics απόδοσης και ποιότητας που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε το μοντέλο Azure OpenAI που δημιουργήσατε για την αξιολόγηση. Για παράδειγμα, επιλέξτε **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.el.png)

1. Εκτελέστε τις ακόλουθες εργασίες για να ρυθμίσετε τα metrics κινδύνου και ασφάλειας:

    - Επιλέξτε τα metrics κινδύνου και ασφάλειας που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε το όριο (threshold) για τον υπολογισμό του ποσοστού ελαττωμάτων που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, επιλέξτε **Medium**.
    - Για το **question**, επιλέξτε **Data source** ως **{$data.prompt}**.
    - Για το **answer**, επιλέξτε **Data source** ως **{$run.outputs.answer}**.
    - Για το **ground_truth**, επιλέξτε **Data source** ως **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.el.png)

1. Επιλέξτε **Next**.

1. Επιλέξτε **Submit** για να ξεκινήσει η αξιολόγηση.

1. Η αξιολόγηση θα χρειαστεί λίγο χρόνο για να ολοκληρωθεί. Μπορείτε να παρακολουθείτε την πρόοδο στην καρτέλα **Evaluation**.

### Επισκόπηση των Αποτελεσμάτων Αξιολόγησης

> [!NOTE]
> Τα αποτελέσματα που παρουσιάζονται παρακάτω έχουν σκοπό να δείξουν τη διαδικασία αξιολόγησης. Σε αυτό το σεμινάριο, χρησιμοποιήσαμε ένα μοντέλο που έχει fine-tuned σε σχετικά μικρό σύνολο δεδομένων, κάτι που μπορεί να οδηγήσει σε υποβέλτιστα αποτελέσματα. Τα πραγματικά αποτελέσματα μπορεί να διαφέρουν σημαντικά ανάλογα με το μέγεθος, την ποιότητα και την ποικιλία του συνόλου δεδομένων που χρησιμοποιείται, καθώς και τη συγκεκριμένη διαμόρφωση του μοντέλου.

Μόλις ολοκληρωθεί η αξιολόγηση, μπορείτε να ελέγξετε τα αποτελέσματα για τα metrics απόδοσης και ασφάλειας.

1. Metrics απόδοσης και ποιότητας:

    - Αξιολογήστε την αποτελεσματικότητα του μοντέλου στην παραγωγή συνεκτικών, φυσικών και σχετικών απαντήσεων.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.el.png)

1. Metrics κινδύνου και ασφάλειας:

    - Διασφαλίστε ότι οι απαντήσεις του μοντέλου είναι ασφαλείς και συμμορφώνονται με τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης, αποφεύγοντας περιεχόμενο που μπορεί να είναι επιβλαβές ή προσβλητικό.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.el.png)

1. Μπορείτε να κάνετε scroll προς τα κάτω για να δείτε τα **Detailed metrics result**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.el.png)

1. Αξιολογώντας το προσαρμοσμένο μοντέλο σας Phi-3 / Phi-3.5 τόσο στα metrics απόδοσης όσο και στα metrics ασφάλειας, μπορείτε να επιβεβαιώσετε ότι το μοντέλο δεν είναι μόνο αποτελεσματικό, αλλά επίσης συμμορφώνεται με τις πρακτικές υπεύθυνης ΤΝ, καθιστώντας το έτοιμο για χρήση σε πραγματικές εφαρμογές.

## Συγχαρητήρια!

### Ολοκληρώσατε αυτό το σεμινάριο

Έχετε αξιολογήσει με επιτυχία το fine-tuned μοντέλο Phi-3 ενσωματωμένο με το Prompt flow στο Azure AI Foundry. Αυτό είναι ένα σημαντικό βήμα για να διασφαλίσετε ότι τα μοντέλα ΤΝ σας όχι μόνο αποδίδουν καλά, αλλά και τηρούν τις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft, βοηθώντας σας να δημιουργήσετε αξιόπιστες και ασφαλείς εφαρμογές ΤΝ.

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.el.png)

## Καθαρισμός Πόρων Azure

Καθαρίστε τους πόρους Azure για να αποφύγετε επιπλέον χρεώσεις στον λογαριασμό σας. Μεταβείτε στο Azure portal και διαγράψτε τους ακόλουθους πόρους:

- Το resource Azure Machine learning.
- Το endpoint μοντέλου Azure Machine learning.
- Το resource Azure AI Foundry Project.
- Το resource Azure AI Foundry Prompt flow.

### Επόμενα Βήματα

#### Τεκμηρίωση

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Εκπαιδευτικό Υλικό

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Αναφορές

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.