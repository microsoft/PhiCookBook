<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7739575218e3244a58516832ad88a9a2",
  "translation_date": "2025-04-04T12:04:29+00:00",
  "source_file": "md\\01.Introduction\\03\\Kaito_Inference.md",
  "language_code": "mo"
}
-->
## Inference with Kaito

[Kaito](https://github.com/Azure/kaito) è un operatore che automatizza il deployment dei modelli di inferenza AI/ML in un cluster Kubernetes.

Kaito presenta le seguenti differenze principali rispetto alla maggior parte delle metodologie di deployment dei modelli basate su infrastrutture di macchine virtuali:

- Gestisce i file del modello utilizzando immagini container. Viene fornito un server http per eseguire chiamate di inferenza utilizzando la libreria del modello.
- Evita la necessità di ottimizzare i parametri di deployment per adattarsi all'hardware GPU grazie a configurazioni preimpostate.
- Effettua il provisioning automatico dei nodi GPU in base ai requisiti del modello.
- Ospita immagini di modelli di grandi dimensioni nel Microsoft Container Registry (MCR) pubblico, se la licenza lo consente.

Con Kaito, il flusso di lavoro per integrare modelli di inferenza AI di grandi dimensioni in Kubernetes è notevolmente semplificato.

## Architettura

Kaito segue il classico pattern di progettazione Kubernetes Custom Resource Definition (CRD)/controller. L'utente gestisce una risorsa personalizzata `workspace` che descrive i requisiti GPU e le specifiche di inferenza. I controller di Kaito automatizzeranno il deployment riconciliando la risorsa personalizzata `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Architettura Kaito" alt="Architettura Kaito">
</div>

La figura sopra presenta una panoramica dell'architettura di Kaito. I suoi principali componenti includono:

- **Workspace controller**: Riconcilia la risorsa personalizzata `workspace`, crea risorse personalizzate `machine` (spiegate di seguito) per avviare il provisioning automatico dei nodi e genera il carico di lavoro di inferenza (`deployment` o `statefulset`) basandosi sulle configurazioni preimpostate del modello.
- **Node provisioner controller**: Il nome del controller è *gpu-provisioner* nel [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utilizza la CRD `machine` originata da [Karpenter](https://sigs.k8s.io/karpenter) per interagire con il workspace controller. Si integra con le API di Azure Kubernetes Service (AKS) per aggiungere nuovi nodi GPU al cluster AKS.
> Nota: Il [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) è un componente open source. Può essere sostituito da altri controller se supportano le API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Installazione

Consulta la guida all'installazione [qui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Avvio rapido Inferenza Phi-3
[Codice di esempio Inferenza Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Lo stato del workspace può essere monitorato eseguendo il seguente comando. Quando la colonna WORKSPACEREADY diventa `True`, il modello è stato distribuito con successo.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Successivamente, si può individuare l'indirizzo IP del servizio di inferenza nel cluster e utilizzare un pod temporaneo `curl` per testare l'endpoint del servizio nel cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Avvio rapido Inferenza Phi-3 con adattatori

Dopo aver installato Kaito, si possono provare i seguenti comandi per avviare un servizio di inferenza.

[Codice di esempio Inferenza Phi-3 con Adattatori](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Lo stato del workspace può essere monitorato eseguendo il seguente comando. Quando la colonna WORKSPACEREADY diventa `True`, il modello è stato distribuito con successo.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Successivamente, si può individuare l'indirizzo IP del servizio di inferenza nel cluster e utilizzare un pod temporaneo `curl` per testare l'endpoint del servizio nel cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

It seems like you want the text translated into "mo." Could you clarify what "mo" refers to? Are you referring to a specific language or dialect, such as Maori, Mongolian, or something else? Let me know so I can assist you better!