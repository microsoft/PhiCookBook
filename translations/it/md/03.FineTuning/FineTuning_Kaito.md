<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:40:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "it"
}
-->
## Messa a punto con Kaito

[Kaito](https://github.com/Azure/kaito) è un operatore che automatizza il deployment di modelli di inferenza AI/ML in un cluster Kubernetes.

Kaito presenta le seguenti differenze chiave rispetto alla maggior parte delle metodologie di deployment di modelli basate su infrastrutture di macchine virtuali:

- Gestisce i file modello utilizzando immagini container. Viene fornito un server http per effettuare chiamate di inferenza usando la libreria modello.
- Evita di dover regolare i parametri di deployment per adattarsi all’hardware GPU grazie a configurazioni preimpostate.
- Provisiona automaticamente i nodi GPU in base alle esigenze del modello.
- Ospita immagini di modelli di grandi dimensioni nel Microsoft Container Registry (MCR) pubblico, se la licenza lo permette.

Con Kaito, il flusso di lavoro per integrare modelli di inferenza AI di grandi dimensioni in Kubernetes è notevolmente semplificato.

## Architettura

Kaito segue il classico pattern di progettazione Kubernetes Custom Resource Definition (CRD)/controller. L’utente gestisce una risorsa personalizzata `workspace` che descrive i requisiti GPU e la specifica di inferenza. I controller di Kaito automatizzano il deployment riconciliando la risorsa personalizzata `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

La figura sopra mostra una panoramica dell’architettura di Kaito. I suoi componenti principali sono:

- **Workspace controller**: Riconcilia la risorsa personalizzata `workspace`, crea risorse personalizzate `machine` (spiegate più avanti) per attivare il provisioning automatico dei nodi, e crea il workload di inferenza (`deployment` o `statefulset`) basandosi sulle configurazioni preimpostate del modello.
- **Node provisioner controller**: Il controller si chiama *gpu-provisioner* nel [grafico helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utilizza la CRD `machine` proveniente da [Karpenter](https://sigs.k8s.io/karpenter) per interagire con il workspace controller. Si integra con le API di Azure Kubernetes Service (AKS) per aggiungere nuovi nodi GPU al cluster AKS.
> Note: Il componente open source [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) può essere sostituito da altri controller se supportano le API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video panoramica  
[Guarda la demo di Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installazione

Consulta la guida all’installazione [qui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Avvio rapido

Dopo aver installato Kaito, si possono provare i seguenti comandi per avviare un servizio di messa a punto.

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

Lo stato del workspace può essere monitorato eseguendo il comando seguente. Quando la colonna WORKSPACEREADY diventa `True`, il modello è stato distribuito con successo.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Successivamente, si può recuperare l’indirizzo IP del servizio di inferenza nel cluster e utilizzare un pod `curl` temporaneo per testare l’endpoint del servizio all’interno del cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.