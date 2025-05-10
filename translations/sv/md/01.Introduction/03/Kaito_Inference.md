<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:53:18+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sv"
}
-->
## Inferens med Kaito

[Kaito](https://github.com/Azure/kaito) är en operator som automatiserar distributionen av AI/ML-inferensmodeller i en Kubernetes-kluster.

Kaito har följande viktiga skillnader jämfört med de flesta vanliga metoder för modell-distribution som bygger på virtuella maskin-infrastrukturer:

- Hanterar modellfiler med hjälp av containerbilder. En http-server tillhandahålls för att utföra inferensanrop med modellbiblioteket.
- Undviker att justera distributionsparametrar för att passa GPU-hårdvara genom att erbjuda förinställda konfigurationer.
- Auto-provisionerar GPU-noder baserat på modellens krav.
- Värdar stora modellbilder i den publika Microsoft Container Registry (MCR) om licensen tillåter.

Med Kaito förenklas arbetsflödet för att ta in stora AI-inferensmodeller i Kubernetes avsevärt.

## Arkitektur

Kaito följer den klassiska Kubernetes Custom Resource Definition (CRD)/controller-designmönstret. Användaren hanterar en `workspace` custom resource som beskriver GPU-kraven och inferensspecifikationen. Kaito controllers automatiserar distributionen genom att samordna `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Figuren ovan visar en översikt av Kaito-arkitekturen. Dess huvudkomponenter består av:

- **Workspace controller**: Den samordnar `workspace` custom resource, skapar `machine` (förklaras nedan) custom resources för att trigga automatisk nodprovisionering, och skapar inferensarbetsbelastningen (`deployment` eller `statefulset`) baserat på modellens förinställda konfigurationer.
- **Node provisioner controller**: Controller-namnet är *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den använder `machine` CRD från [Karpenter](https://sigs.k8s.io/karpenter) för att kommunicera med workspace controller. Den integreras med Azure Kubernetes Service (AKS) API:er för att lägga till nya GPU-noder i AKS-klustret.  
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) är en öppen källkods-komponent. Den kan ersättas av andra controllers om de stöder [Karpenter-core](https://sigs.k8s.io/karpenter) API:er.

## Installation

Vänligen se installationsanvisningarna [här](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Kom igång snabbt med Inferens Phi-3
[Exempelkod Inferens Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Status för workspace kan följas genom att köra följande kommando. När WORKSPACEREADY-kolumnen blir `True` har modellen distribuerats framgångsrikt.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Därefter kan man hitta inferenstjänstens kluster-ip och använda en temporär `curl` pod för att testa tjänstens slutpunkt i klustret.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Kom igång snabbt med Inferens Phi-3 med adapters

Efter att ha installerat Kaito kan man prova följande kommandon för att starta en inferenstjänst.

[Exempelkod Inferens Phi-3 med Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status för workspace kan följas genom att köra följande kommando. När WORKSPACEREADY-kolumnen blir `True` har modellen distribuerats framgångsrikt.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Därefter kan man hitta inferenstjänstens kluster-ip och använda en temporär `curl` pod för att testa tjänstens slutpunkt i klustret.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.