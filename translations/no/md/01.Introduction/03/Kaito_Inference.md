<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T12:38:13+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "no"
}
-->
## Inferens med Kaito 

[Kaito](https://github.com/Azure/kaito) er en operator som automatiserer utrulling av AI/ML inferensmodeller i en Kubernetes-klynge.

Kaito har følgende viktige forskjeller sammenlignet med de fleste mainstream metoder for modellutrulling som er bygget på toppen av virtuelle maskin-infrastrukturer:

- Håndterer modellfiler ved hjelp av containerbilder. En http-server tilbys for å utføre inferensanrop med modellbiblioteket.
- Unngår tuning av utrullingsparametere for å tilpasses GPU-maskinvare ved å tilby forhåndsinnstilte konfigurasjoner.
- Automatisk provisjonering av GPU-noder basert på Modellkrav.
- Vert store modellbilder i det offentlige Microsoft Container Registry (MCR) hvis lisensen tillater det.

Ved å bruke Kaito er arbeidsflyten for onboarding av store AI-inferensmodeller i Kubernetes i stor grad forenklet.


## Arkitektur

Kaito følger det klassiske Kubernetes Custom Resource Definition (CRD)/controller designmønsteret. Bruker administrerer en `workspace` custom resource som beskriver GPU-kravene og inferensspesifikasjonen. Kaito-kontrollerne automatiserer utrullingen ved å forene den `workspace` custom resource.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Figuren over viser en oversikt over Kaito-arkitekturen. Dens hovedkomponenter består av:

- **Workspace-kontroller**: Den forener `workspace` custom resource, oppretter `machine` (forklart nedenfor) custom resources for å trigge auto-provisjonering av noder, og oppretter inferensarbeidsmengden (`deployment` eller `statefulset`) basert på modellens forhåndskonfigurasjoner.
- **Node provisjonskontroller**: Kontrollerens navn er *gpu-provisioner* i [gpu-provisioner helm diagram](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den bruker `machine` CRD som stammer fra [Karpenter](https://sigs.k8s.io/karpenter) for å samhandle med workspace-kontrolleren. Den integreres med Azure Kubernetes Service (AKS) APIer for å legge til nye GPU-noder til AKS-klyngen. 
> Merk: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) er en åpen kilde-komponent. Den kan erstattes av andre controllere dersom de støtter [Karpenter-core](https://sigs.k8s.io/karpenter) APIer.

## Installasjon

Vennligst sjekk installasjonsveiledningen [her](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hurtigstart Inferens Phi-3
[Eksempelkode Inferens Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Justering av utgang ACR-bane
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Status for workspace kan følges ved å kjøre følgende kommando. Når WORKSPACEREADY-kolonnen blir `True`, er modellen rullet ut med suksess.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Deretter kan man finne tjenestens kluster-ip og bruke en temporær `curl` pod for å teste tjenesteendepunktet i klyngen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Hurtigstart Inferens Phi-3 med adaptere

Etter at Kaito er installert, kan man forsøke følgende kommandoer for å starte en inferenstjeneste.

[Eksempelkode Inferens Phi-3 med Adaptere](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Justere utgang ACR-sti
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Status for workspace kan følges ved å kjøre følgende kommando. Når WORKSPACEREADY-kolonnen blir `True`, er modellen rullet ut med suksess.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Deretter kan man finne tjenestens kluster-ip og bruke en temporær `curl` pod for å teste tjenesteendepunktet i klyngen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->