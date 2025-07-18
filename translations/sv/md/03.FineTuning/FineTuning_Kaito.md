<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:22:36+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "sv"
}
-->
## Finjustering med Kaito

[Kaito](https://github.com/Azure/kaito) är en operator som automatiserar distributionen av AI/ML-inferensmodeller i en Kubernetes-kluster.

Kaito har följande viktiga skillnader jämfört med de flesta vanliga metoder för modellutplacering som bygger på virtuella maskinmiljöer:

- Hanterar modelfiler med hjälp av containerbilder. En HTTP-server tillhandahålls för att utföra inferensanrop med modellbiblioteket.
- Undviker att justera distributionsparametrar för att passa GPU-hårdvara genom att erbjuda förinställda konfigurationer.
- Auto-provisionerar GPU-noder baserat på modellens krav.
- Värd för stora modellbilder i den publika Microsoft Container Registry (MCR) om licensen tillåter.

Med Kaito förenklas arbetsflödet för att ta in stora AI-inferensmodeller i Kubernetes avsevärt.

## Arkitektur

Kaito följer det klassiska Kubernetes Custom Resource Definition (CRD)/controller-designmönstret. Användaren hanterar en `workspace` custom resource som beskriver GPU-kraven och inferensspecifikationen. Kaito-kontrollerna automatiserar distributionen genom att synkronisera `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Figuren ovan visar en översikt av Kaito-arkitekturen. Dess huvudsakliga komponenter består av:

- **Workspace controller**: Den synkroniserar `workspace` custom resource, skapar `machine` (förklaras nedan) custom resources för att trigga automatisk nodprovisionering och skapar inferensarbetsbelastningen (`deployment` eller `statefulset`) baserat på modellens förinställda konfigurationer.
- **Node provisioner controller**: Kontrollen heter *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den använder `machine` CRD som kommer från [Karpenter](https://sigs.k8s.io/karpenter) för att interagera med workspace-kontrollern. Den integreras med Azure Kubernetes Service (AKS) API:er för att lägga till nya GPU-noder i AKS-klustret.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) är en öppen källkodskomponent. Den kan ersättas av andra controllers om de stödjer [Karpenter-core](https://sigs.k8s.io/karpenter) API:er.

## Översiktsvideo  
[Titta på Kaito-demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

Vänligen se installationsanvisningarna [här](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Kom igång snabbt

Efter att ha installerat Kaito kan man prova följande kommandon för att starta en finjusteringstjänst.

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

Status för workspace kan följas genom att köra följande kommando. När kolumnen WORKSPACEREADY blir `True` har modellen distribuerats framgångsrikt.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Därefter kan man hitta inferenstjänstens kluster-IP och använda en temporär `curl`-pod för att testa tjänstens endpoint i klustret.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.