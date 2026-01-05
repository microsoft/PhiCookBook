<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T09:55:18+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ro"
}
-->
## Inferență cu Kaito 

[Kaito](https://github.com/Azure/kaito) este un operator care automatizează implementarea modelelor AI/ML pentru inferență într-un cluster Kubernetes.

Kaito are următoarele diferențieri cheie față de majoritatea metodologiilor mainstream de implementare a modelelor construite pe infrastructuri de mașini virtuale:

- Gestionează fișierele modelului folosind imagini de container. Este furnizat un server http pentru a efectua apeluri de inferență folosind biblioteca modelului.
- Evită ajustarea parametrilor de implementare pentru a se potrivi hardware-ului GPU prin furnizarea de configurații predefinite.
- Provizionare automată a nodurilor GPU bazată pe cerințele modelului.
- Găzduiește imagini mari ale modelului în Registrul Public Microsoft Container (MCR) dacă licența permite.

Folosind Kaito, fluxul de lucru pentru integrarea modelelor mari de inferență AI în Kubernetes este mult simplificat.


## Arhitectură

Kaito urmează modelul clasic de proiectare Kubernetes Custom Resource Definition(CRD)/controller. Utilizatorul gestionează o resursă personalizată `workspace` care descrie cerințele GPU și specificația de inferență. Controller-ele Kaito vor automatiza implementarea prin reconcilierea resursei personalizate `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Figura de mai sus prezintă o imagine de ansamblu a arhitecturii Kaito. Componentele sale principale sunt:

- **Controller-ul Workspace**: Reconciliatează resursa personalizată `workspace`, creează resurse personalizate `machine` (explicate mai jos) pentru a declanșa provizionarea automată a nodurilor și creează sarcina de inferență (`deployment` sau `statefulset`) pe baza configurațiilor predefinite ale modelului.
- **Controller-ul de provizionare a nodurilor**: Numele controller-ului este *gpu-provisioner* în [chart-ul helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utilizează CRD-ul `machine` originar din [Karpenter](https://sigs.k8s.io/karpenter) pentru a interacționa cu controller-ul workspace. Se integrează cu API-urile Azure Kubernetes Service (AKS) pentru a adăuga noi noduri GPU în clusterul AKS. 
> Notă: Componenta [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) este open source. Poate fi înlocuită cu alți controllere dacă acestea suportă API-urile [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalare

Vă rugăm să consultați ghidul de instalare [aici](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Pornire rapidă Inferență Phi-3
[Cod Eșantion Inferență Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Reglarea traseului de ieșire ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Starea workspace-ului poate fi urmărită rulând comanda de mai jos. Când coloana WORKSPACEREADY devine `True`, modelul a fost implementat cu succes.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Ulterior, se poate găsi IP-ul clusterului al serviciului de inferență și se poate utiliza un pod temporal `curl` pentru a testa punctul de acces al serviciului din cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Pornire rapidă Inferență Phi-3 cu adaptoare

După instalarea Kaito, se pot încerca următoarele comenzi pentru a porni un serviciu de inferență.

[Cod Eșantion Inferență Phi-3 cu Adaptoare](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Reglarea căii de ieșire ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Starea workspace-ului poate fi urmărită rulând comanda de mai jos. Când coloana WORKSPACEREADY devine `True`, modelul a fost implementat cu succes.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Ulterior, se poate găsi IP-ul clusterului al serviciului de inferență și se poate utiliza un pod temporal `curl` pentru a testa punctul de acces al serviciului din cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->