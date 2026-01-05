<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T08:41:27+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "nl"
}
-->
## Inferentie met Kaito 

[Kaito](https://github.com/Azure/kaito) is een operator die het AI/ML inferentiemodel-implementatieproces in een Kubernetes-cluster automatiseert.

Kaito heeft de volgende belangrijke verschillen in vergelijking met de meeste gangbare modelimplementatiemethoden die gebouwd zijn op virtual machine-infrastructuren:

- Beheer modelbestanden met containerafbeeldingen. Er wordt een http-server geleverd om inferentieoproepen uit te voeren met behulp van de modellibrary.
- Voorkom het afstemmen van implementatieparameters op GPU-hardware door vooraf ingestelde configuraties te bieden.
- Automatisch GPU-knooppunten voorzien op basis van modelvereisten.
- Host grote modelafbeeldingen in het openbare Microsoft Container Registry (MCR) als de licentie dit toelaat.

Met Kaito wordt de workflow voor het onboarden van grote AI-inferentiemodellen in Kubernetes grotendeels vereenvoudigd.


## Architectuur

Kaito volgt het klassieke Kubernetes Custom Resource Definition(CRD)/controller-ontwerppatroon. Gebruikers beheren een `workspace` custom resource die de GPU-vereisten en de inferentiespecificatie beschrijft. Kaito-controllers automatiseren de implementatie door de `workspace` custom resource te reconciliëren.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

De bovenstaande afbeelding toont het overzicht van de Kaito-architectuur. De belangrijkste componenten bestaan uit:

- **Workspace controller**: Deze reconcileert de `workspace` custom resource, maakt `machine` (hieronder uitgelegd) custom resources aan om het automatisch voorzien van knooppunten te triggeren en maakt de inferentielast (`deployment` of `statefulset`) op basis van de vooraf ingestelde modelconfiguraties.
- **Node provisioner controller**: De controller heet *gpu-provisioner* in de [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Hij gebruikt de `machine` CRD afkomstig van [Karpenter](https://sigs.k8s.io/karpenter) om te communiceren met de workspace controller. Hij integreert met Azure Kubernetes Service (AKS)-API’s om nieuwe GPU-knooppunten toe te voegen aan het AKS-cluster. 
> Opmerking: De [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is een open-source component. Hij kan worden vervangen door andere controllers als deze de [Karpenter-core](https://sigs.k8s.io/karpenter) API’s ondersteunen.

## Installatie

Bekijk de installatiehandleiding [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Snelstart inferentie Phi-3
[Voorbeeldcode Inferentie Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Afstemmen Uitvoer ACR Pad
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

De status van de workspace kan worden gevolgd door het volgende commando uit te voeren. Wanneer de kolom WORKSPACEREADY `True` wordt, is het model succesvol geïmplementeerd.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Vervolgens kan men het cluster-ip van de inferentie-service vinden en een tijdelijke `curl`-pod gebruiken om de service-endpoint binnen het cluster te testen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Snelstart inferentie Phi-3 met adapters

Na het installeren van Kaito kan men de volgende commando’s proberen om een inferentieservice te starten.

[Voorbeeldcode Inferentie Phi-3 met adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Afstemmen uitvoer ACR-pad
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

De status van de workspace kan worden gevolgd door het volgende commando uit te voeren. Wanneer de kolom WORKSPACEREADY `True` wordt, is het model succesvol geïmplementeerd.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Vervolgens kan men het cluster-ip van de inferentie-service vinden en een tijdelijke `curl`-pod gebruiken om de service-endpoint binnen het cluster te testen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onjuistheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->