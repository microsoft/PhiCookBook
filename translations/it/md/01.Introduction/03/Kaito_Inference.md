<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T03:17:02+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "it"
}
-->
## Inferenza con Kaito 

[Kaito](https://github.com/Azure/kaito) è un operator che automatizza il deployment dei modelli di AI/ML per l'inferenza in un cluster Kubernetes.

Kaito presenta le seguenti differenze chiave rispetto alla maggior parte delle metodologie di deployment dei modelli diffuse, costruite su infrastrutture di macchine virtuali:

- Gestisce i file dei modelli usando immagini container. Viene fornito un server http per eseguire chiamate di inferenza utilizzando la libreria del modello.
- Evita di tarare i parametri di deployment per adattarli all'hardware GPU fornendo configurazioni preimpostate.
- Provisioning automatico dei nodi GPU in base ai requisiti del modello.
- Ospita immagini di modelli di grandi dimensioni nel Microsoft Container Registry (MCR) pubblico se la licenza lo consente.

Usando Kaito, il flusso di lavoro per l'onboarding di grandi modelli di inferenza AI in Kubernetes è notevolmente semplificato.


## Architettura

Kaito segue il classico pattern di progettazione Kubernetes Custom Resource Definition(CRD)/controller. L'utente gestisce una risorsa personalizzata `workspace` che descrive i requisiti GPU e la specifica di inferenza. I controller di Kaito automatizzano il deployment riconciliando la risorsa personalizzata `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="Architettura KAITO RAGEngine" alt="Architettura KAITO RAGEngine">
</div>

La figura sopra presenta la panoramica dell'architettura di Kaito. I suoi componenti principali sono:

- **Workspace controller**: Riconcilia la risorsa personalizzata `workspace`, crea risorse personalizzate `machine` (spiegate di seguito) per attivare il provisioning automatico dei nodi e crea il carico di lavoro di inferenza (`deployment` o `statefulset`) basato sulle configurazioni preimpostate del modello.
- **Node provisioner controller**: Il nome del controller è *gpu-provisioner* nello [chart Helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utilizza il CRD `machine` originato da [Karpenter](https://sigs.k8s.io/karpenter) per interagire con il controller del workspace. Si integra con le API di Azure Kubernetes Service(AKS) per aggiungere nuovi nodi GPU al cluster AKS. 
> Nota: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) è un componente open source. Può essere sostituito da altri controller se supportano le API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Installazione

Consulta le istruzioni di installazione [qui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Avvio rapido Inferenza Phi-3
[Esempio di codice per l'inferenza Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Percorso ACR di uscita per la taratura
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Lo stato del workspace può essere monitorato eseguendo il comando seguente. Quando la colonna WORKSPACEREADY diventa `True`, il modello è stato distribuito con successo.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Successivamente, è possibile trovare l'IP del cluster del servizio di inferenza e usare un pod temporaneo `curl` per testare l'endpoint del servizio nel cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Avvio rapido Inferenza Phi-3 con adattatori

Dopo aver installato Kaito, è possibile provare i seguenti comandi per avviare un servizio di inferenza.

[Esempio di codice Inferenza Phi-3 con adattatori](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Percorso di uscita ACR per la messa a punto
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Lo stato del workspace può essere monitorato eseguendo il comando seguente. Quando la colonna WORKSPACEREADY diventa `True`, il modello è stato distribuito con successo.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Successivamente, è possibile trovare l'IP del cluster del servizio di inferenza e usare un pod temporaneo `curl` per testare l'endpoint del servizio nel cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Dichiarazione di non responsabilità**:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci a garantire l'accuratezza, si segnala che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua d'origine deve essere considerato la fonte autorevole. Per informazioni di natura critica si consiglia una traduzione professionale eseguita da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->