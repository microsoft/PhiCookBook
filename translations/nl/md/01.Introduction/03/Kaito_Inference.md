<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:51:41+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "nl"
}
-->
## Inference met Kaito

[Kaito](https://github.com/Azure/kaito) is een operator die het uitrollen van AI/ML inference modellen in een Kubernetes-cluster automatiseert.

Kaito onderscheidt zich op de volgende belangrijke punten van de meeste gangbare methoden voor modeluitrol die zijn gebouwd op virtuele machine-infrastructuren:

- Beheer modelbestanden via containerimages. Er wordt een http-server geleverd om inference-aanroepen uit te voeren met behulp van de modellibrary.
- Voorkom het afstemmen van uitrolparameters op GPU-hardware door vooraf ingestelde configuraties te bieden.
- Automatische provisioning van GPU-nodes op basis van modelvereisten.
- Host grote modelimages in de publieke Microsoft Container Registry (MCR) indien de licentie dit toestaat.

Met Kaito wordt de workflow voor het onboarden van grote AI inference modellen in Kubernetes sterk vereenvoudigd.

## Architectuur

Kaito volgt het klassieke Kubernetes Custom Resource Definition (CRD)/controller ontwerp patroon. De gebruiker beheert een `workspace` custom resource die de GPU-vereisten en de inference-specificatie beschrijft. Kaito-controllers automatiseren de uitrol door de `workspace` custom resource te reconciliëren.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

De bovenstaande afbeelding geeft een overzicht van de Kaito-architectuur. De belangrijkste componenten zijn:

- **Workspace controller**: Deze reconcileert de `workspace` custom resource, maakt `machine` (hieronder uitgelegd) custom resources aan om node auto provisioning te triggeren, en creëert de inference workload (`deployment` of `statefulset`) op basis van de vooraf ingestelde modelconfiguraties.
- **Node provisioner controller**: De controller heet *gpu-provisioner* in de [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Hij gebruikt de `machine` CRD afkomstig van [Karpenter](https://sigs.k8s.io/karpenter) om te communiceren met de workspace controller. Hij integreert met Azure Kubernetes Service (AKS) API’s om nieuwe GPU-nodes toe te voegen aan het AKS-cluster.
> Note: De [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is een open source component. Deze kan vervangen worden door andere controllers als zij [Karpenter-core](https://sigs.k8s.io/karpenter) API’s ondersteunen.

## Installatie

Bekijk de installatie-instructies [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Snel starten met Inference Phi-3
[Voorbeeldcode Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

De status van de workspace kan gevolgd worden met het volgende commando. Zodra de WORKSPACEREADY-kolom `True` wordt, is het model succesvol uitgerold.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Vervolgens kan men het cluster-ip van de inference service opzoeken en een tijdelijke `curl` pod gebruiken om de service endpoint binnen het cluster te testen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Snel starten met Inference Phi-3 met adapters

Na het installeren van Kaito kan men de volgende commando’s proberen om een inference service te starten.

[Voorbeeldcode Inference Phi-3 met Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

De status van de workspace kan gevolgd worden met het volgende commando. Zodra de WORKSPACEREADY-kolom `True` wordt, is het model succesvol uitgerold.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Vervolgens kan men het cluster-ip van de inference service opzoeken en een tijdelijke `curl` pod gebruiken om de service endpoint binnen het cluster te testen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.