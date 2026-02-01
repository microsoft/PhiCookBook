## Συμπεράσματα με το Kaito 

Το [Kaito](https://github.com/Azure/kaito) είναι ένας χειριστής που αυτοματοποιεί την ανάπτυξη μοντέλων AI/ML συμπερασμάτων σε ένα σύμπλεγμα Kubernetes.

Το Kaito έχει τις ακόλουθες βασικές διαφορές σε σύγκριση με τις περισσότερες παραδοσιακές μεθοδολογίες ανάπτυξης μοντέλων που βασίζονται σε υποδομές εικονικών μηχανών:

- Διαχείριση αρχείων μοντέλου χρησιμοποιώντας εικόνες κοντέινερ. Παρέχεται ένας http server για εκτέλεση κλήσεων συμπερασμάτων χρησιμοποιώντας τη βιβλιοθήκη μοντέλου.
- Αποφυγή ρύθμισης παραμέτρων ανάπτυξης για προσαρμογή σε hardware GPU με την παροχή προκαθορισμένων ρυθμίσεων.
- Αυτόματη παροχή κόμβων GPU βάσει των απαιτήσεων του μοντέλου.
- Φιλοξενία μεγάλων εικόνων μοντέλων στο δημόσιο Microsoft Container Registry (MCR), εφόσον το επιτρέπει η άδεια χρήσης.

Με τη χρήση του Kaito, η ροή εργασίας για την ενσωμάτωση μεγάλων μοντέλων AI συμπερασμάτων στο Kubernetes απλοποιείται σημαντικά.


## Αρχιτεκτονική

Το Kaito ακολουθεί την κλασική σχεδίαση Kubernetes Custom Resource Definition(CRD)/controller. Ο χρήστης διαχειρίζεται έναν προσαρμοσμένο πόρο `workspace` που περιγράφει τις απαιτήσεις GPU και τις προδιαγραφές συμπερασμού. Οι χειριστές του Kaito αυτοματοποιούν την ανάπτυξη εναρμονίζοντας τον προσαρμοσμένο πόρο `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="Αρχιτεκτονική KAITO RAGEngine">
</div>

Το παραπάνω σχήμα παρουσιάζει μια επισκόπηση της αρχιτεκτονικής του Kaito. Τα κύρια συστατικά του αποτελούνται από:

- **Χειριστής Workspace**: Εναρμονίζει τον προσαρμοσμένο πόρο `workspace`, δημιουργεί προσαρμοσμένους πόρους `machine` (εξηγούνται παρακάτω) για να εκκινήσει την αυτόματη παροχή κόμβων, και δημιουργεί το φορτίο εργασίας συμπερασμού (`deployment` ή `statefulset`) βάσει των προκαθορισμένων ρυθμίσεων του μοντέλου.
- **Χειριστής παροχής κόμβου**: Το όνομα του χειριστή είναι *gpu-provisioner* στο [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Χρησιμοποιεί το CRD `machine` που προέρχεται από το [Karpenter](https://sigs.k8s.io/karpenter) για να αλληλεπιδράσει με τον χειριστή workspace. Ενσωματώνεται με τα APIs του Azure Kubernetes Service (AKS) για να προσθέσει νέους κόμβους GPU στο σύμπλεγμα AKS. 
> Σημείωση: Ο [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) είναι εξαρτημα ανοιχτού κώδικα. Μπορεί να αντικατασταθεί από άλλους χειριστές αν υποστηρίζουν τα APIs του [Karpenter-core](https://sigs.k8s.io/karpenter).

## Εγκατάσταση

Παρακαλώ ελέγξτε τις οδηγίες εγκατάστασης [εδώ](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Γρήγορη εκκίνηση Συμπερασμάτων Phi-3
[Δείγμα Κώδικα Συμπερασμάτων Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3
inference:
  preset:
    name: phi-3-mini-4k-instruct
    # Note: This configuration also works with the phi-3-mini-128k-instruct preset
```

```sh
$ cat examples/inference/kaito_workspace_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-4k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ρύθμιση της διαδρομής εξόδου ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Η κατάσταση του workspace μπορεί να παρακολουθείται εκτελώντας την ακόλουθη εντολή. Όταν η στήλη WORKSPACEREADY γίνει `True`, το μοντέλο έχει αναπτυχθεί με επιτυχία.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Στη συνέχεια, μπορεί κανείς να βρει το IP του συμπλέγματος της υπηρεσίας συμπερασμού και να χρησιμοποιήσει ένα προσωρινό pod `curl` για να δοκιμάσει το σημείο πρόσβασης της υπηρεσίας στο σύμπλεγμα.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Γρήγορη εκκίνηση Συμπερασμάτων Phi-3 με προσαρμογείς

Μετά την εγκατάσταση του Kaito, μπορεί κανείς να δοκιμάσει τις ακόλουθες εντολές για να ξεκινήσει μια υπηρεσία συμπερασμών.

[Δείγμα Κώδικα Συμπερασμών Phi-3 με Προσαρμογείς](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3-adapter
inference:
  preset:
    name: phi-3-mini-128k-instruct
  adapters:
    - source:
        name: "phi-3-adapter"
        image: "ACR_REPO_HERE.azurecr.io/ADAPTER_HERE:0.0.1"
      strength: "1.0"
```

```sh
$ cat examples/inference/kaito_workspace_phi_3_with_adapters.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ρύθμιση Διαδρομής Έξοδου ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Η κατάσταση του workspace μπορεί να παρακολουθείται εκτελώντας την ακόλουθη εντολή. Όταν η στήλη WORKSPACEREADY γίνει `True`, το μοντέλο έχει αναπτυχθεί με επιτυχία.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Στη συνέχεια, μπορεί κανείς να βρει το IP του συμπλέγματος της υπηρεσίας συμπερασμού και να χρησιμοποιήσει ένα προσωρινό pod `curl` για να δοκιμάσει το σημείο πρόσβασης της υπηρεσίας στο σύμπλεγμα.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση Ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλείσθε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρανοήσεις ή λανθασμένες ερμηνείες προκύψουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->