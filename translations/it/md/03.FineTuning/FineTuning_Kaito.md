<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:21:41+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "it"
}
-->
## Fine-Tuning con Kaito

[Kaito](https://github.com/Azure/kaito) è un operatore che automatizza il deployment di modelli di inferenza AI/ML in un cluster Kubernetes.

Kaito presenta le seguenti differenze chiave rispetto alla maggior parte delle metodologie di deployment di modelli basate su infrastrutture di macchine virtuali:

- Gestisce i file dei modelli utilizzando immagini container. Viene fornito un server http per eseguire chiamate di inferenza usando la libreria del modello.
- Evita di dover regolare i parametri di deployment per adattarsi all’hardware GPU grazie a configurazioni preimpostate.
- Provvede automaticamente ai nodi GPU in base ai requisiti del modello.
- Ospita immagini di modelli di grandi dimensioni nel Microsoft Container Registry (MCR) pubblico, se la licenza lo consente.

Con Kaito, il flusso di lavoro per l’integrazione di grandi modelli di inferenza AI in Kubernetes è notevolmente semplificato.

## Architettura

Kaito segue il classico pattern di progettazione Kubernetes Custom Resource Definition (CRD)/controller. L’utente gestisce una risorsa personalizzata `workspace` che descrive i requisiti GPU e la specifica di inferenza. I controller di Kaito automatizzano il deployment riconciliando la risorsa personalizzata `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

La figura sopra mostra una panoramica dell’architettura di Kaito. I suoi componenti principali sono:

- **Workspace controller**: Riconcilia la risorsa personalizzata `workspace`, crea risorse personalizzate `machine` (spiegate di seguito) per attivare il provisioning automatico dei nodi e crea il carico di lavoro di inferenza (`deployment` o `statefulset`) basandosi sulle configurazioni preimpostate del modello.
- **Node provisioner controller**: Il controller si chiama *gpu-provisioner* nel [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utilizza il CRD `machine` originato da [Karpenter](https://sigs.k8s.io/karpenter) per interagire con il workspace controller. Si integra con le API di Azure Kubernetes Service (AKS) per aggiungere nuovi nodi GPU al cluster AKS.
> Nota: Il [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) è un componente open source. Può essere sostituito da altri controller se supportano le API di [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video panoramica  
[Guarda la demo di Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installazione

Consulta la guida all’installazione [qui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Avvio rapido

Dopo aver installato Kaito, è possibile provare i seguenti comandi per avviare un servizio di fine-tuning.

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

Successivamente, è possibile trovare l’IP del servizio di inferenza nel cluster e utilizzare un pod temporaneo `curl` per testare l’endpoint del servizio all’interno del cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.