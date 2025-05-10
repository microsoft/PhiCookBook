<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:40:35+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "el"
}
-->
## Fine-Tuning με το Kaito 

Το [Kaito](https://github.com/Azure/kaito) είναι ένας operator που αυτοματοποιεί την ανάπτυξη μοντέλων AI/ML για inference σε ένα Kubernetes cluster.

Το Kaito έχει τα εξής βασικά πλεονεκτήματα σε σύγκριση με τις περισσότερες δημοφιλείς μεθόδους ανάπτυξης μοντέλων που βασίζονται σε υποδομές virtual machine:

- Διαχείριση αρχείων μοντέλου μέσω container images. Παρέχεται http server για την εκτέλεση inference κλήσεων χρησιμοποιώντας τη βιβλιοθήκη μοντέλου.
- Αποφυγή ρύθμισης παραμέτρων ανάπτυξης για να ταιριάξουν στο GPU hardware, μέσω προκαθορισμένων ρυθμίσεων.
- Αυτόματη παροχή GPU nodes βάσει των απαιτήσεων του μοντέλου.
- Φιλοξενία μεγάλων εικόνων μοντέλων στο δημόσιο Microsoft Container Registry (MCR), εφόσον το επιτρέπει η άδεια χρήσης.

Με το Kaito, η διαδικασία ενσωμάτωσης μεγάλων μοντέλων AI για inference στο Kubernetes απλοποιείται σημαντικά.


## Αρχιτεκτονική

Το Kaito ακολουθεί το κλασικό σχέδιο Custom Resource Definition (CRD) / controller του Kubernetes. Ο χρήστης διαχειρίζεται έναν `workspace` custom resource που περιγράφει τις απαιτήσεις GPU και τις προδιαγραφές inference. Οι controllers του Kaito αυτοματοποιούν την ανάπτυξη, συγχρονίζοντας τον `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Η παραπάνω εικόνα παρουσιάζει την επισκόπηση της αρχιτεκτονικής του Kaito. Τα κύρια συστατικά της είναι:

- **Workspace controller**: Συγχρονίζει τον `workspace` custom resource, δημιουργεί `machine` (περιγράφεται παρακάτω) custom resources για την ενεργοποίηση της αυτόματης παροχής κόμβων και δημιουργεί το inference workload (`deployment` ή `statefulset`) βάσει των προκαθορισμένων ρυθμίσεων του μοντέλου.
- **Node provisioner controller**: Ο controller ονομάζεται *gpu-provisioner* στο [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Χρησιμοποιεί το `machine` CRD που προέρχεται από το [Karpenter](https://sigs.k8s.io/karpenter) για να συνεργαστεί με τον workspace controller. Ενσωματώνεται με τα Azure Kubernetes Service (AKS) APIs για να προσθέτει νέους GPU κόμβους στο AKS cluster.
> Σημείωση: Το [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) είναι ένα ανοιχτού κώδικα συστατικό. Μπορεί να αντικατασταθεί από άλλους controllers εάν υποστηρίζουν τα [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Επισκόπηση βίντεο 
[Παρακολουθήστε το Demo του Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Εγκατάσταση

Παρακαλώ δείτε τις οδηγίες εγκατάστασης [εδώ](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Γρήγορη εκκίνηση

Μετά την εγκατάσταση του Kaito, μπορείτε να δοκιμάσετε τις παρακάτω εντολές για να ξεκινήσετε μια υπηρεσία fine-tuning.

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
```

```sh
$ cat examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

Η κατάσταση του workspace μπορεί να παρακολουθηθεί με την ακόλουθη εντολή. Όταν η στήλη WORKSPACEREADY γίνει `True`, το μοντέλο έχει αναπτυχθεί επιτυχώς.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Έπειτα, μπορείτε να βρείτε το cluster ip της υπηρεσίας inference και να χρησιμοποιήσετε ένα προσωρινό `curl` pod για να δοκιμάσετε το endpoint της υπηρεσίας μέσα στο cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από ανθρώπους. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.