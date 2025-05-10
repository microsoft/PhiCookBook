<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:41:35+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "nl"
}
-->
## Fijn afstemmen met Kaito

[Kaito](https://github.com/Azure/kaito) is een operator die het uitrollen van AI/ML-inferentiemodellen in een Kubernetes-cluster automatiseert.

Kaito onderscheidt zich op de volgende belangrijke punten van de meeste gangbare methoden voor modeluitrol die zijn gebaseerd op virtuele machine-infrastructuren:

- Beheer modelbestanden met containerimages. Er wordt een http-server geleverd om inferentie-aanroepen uit te voeren met behulp van de modellibrary.
- Vermijd het afstemmen van uitrolparameters op GPU-hardware door vooraf ingestelde configuraties te bieden.
- Automatische provisioning van GPU-knooppunten op basis van modelvereisten.
- Host grote modelimages in de publieke Microsoft Container Registry (MCR) als de licentie dit toestaat.

Met Kaito wordt de workflow voor het onboarden van grote AI-inferentiemodellen in Kubernetes sterk vereenvoudigd.

## Architectuur

Kaito volgt het klassieke Kubernetes Custom Resource Definition (CRD)/controller ontwerp. De gebruiker beheert een `workspace` custom resource die de GPU-vereisten en de inferentiespecificatie beschrijft. Kaito-controllers automatiseren de uitrol door de `workspace` custom resource te reconciliëren.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

De bovenstaande afbeelding toont een overzicht van de Kaito-architectuur. De belangrijkste componenten bestaan uit:

- **Workspace controller**: Deze reconcileert de `workspace` custom resource, maakt `machine` (hieronder uitgelegd) custom resources aan om automatische provisioning van knooppunten te starten, en maakt de inferentieworkload (`deployment` of `statefulset`) aan op basis van de vooraf ingestelde modelconfiguraties.
- **Node provisioner controller**: De controller heet *gpu-provisioner* in de [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Hij gebruikt de `machine` CRD afkomstig van [Karpenter](https://sigs.k8s.io/karpenter) om te communiceren met de workspace controller. Hij integreert met de Azure Kubernetes Service (AKS) API's om nieuwe GPU-knooppunten toe te voegen aan het AKS-cluster.
> Note: De [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is een open source component. Deze kan vervangen worden door andere controllers, mits zij de [Karpenter-core](https://sigs.k8s.io/karpenter) API's ondersteunen.

## Overzichtsvideo  
[Bekijk de Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installatie

Bekijk de installatie-instructies [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Snel aan de slag

Na het installeren van Kaito kan men de volgende commando’s proberen om een fijn-afstemmingsdienst te starten.

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

De status van de workspace kan worden gevolgd met het volgende commando. Wanneer de WORKSPACEREADY-kolom `True` wordt, is het model succesvol uitgerold.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Vervolgens kan men het cluster-ip van de inferentiedienst opzoeken en een tijdelijke `curl` pod gebruiken om de service-endpoint in het cluster te testen.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de originele taal moet als de gezaghebbende bron worden beschouwd. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.