<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:22:57+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "no"
}
-->
## Finjustering med Kaito

[Kaito](https://github.com/Azure/kaito) er en operator som automatiserer distribusjon av AI/ML-inferensmodeller i et Kubernetes-kluster.

Kaito har følgende viktige forskjeller sammenlignet med de fleste vanlige metoder for modell-distribusjon som er bygget på virtuelle maskin-infrastrukturer:

- Håndterer modellfiler ved hjelp av containerbilder. En HTTP-server tilbys for å utføre inferensanrop ved bruk av modellbiblioteket.
- Unngår behovet for å justere distribusjonsparametere for å tilpasse GPU-maskinvaren ved å tilby forhåndsinnstilte konfigurasjoner.
- Automatisk provisjonering av GPU-noder basert på modellens krav.
- Vert store modellbilder i det offentlige Microsoft Container Registry (MCR) hvis lisensen tillater det.

Med Kaito blir arbeidsflyten for å ta i bruk store AI-inferensmodeller i Kubernetes i stor grad forenklet.

## Arkitektur

Kaito følger det klassiske Kubernetes Custom Resource Definition (CRD)/controller-designmønsteret. Brukeren administrerer en `workspace` custom resource som beskriver GPU-kravene og inferensspesifikasjonen. Kaito-kontrollere automatiserer distribusjonen ved å synkronisere `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Figuren over viser en oversikt over Kaito-arkitekturen. Hovedkomponentene består av:

- **Workspace controller**: Den synkroniserer `workspace` custom resource, oppretter `machine` (forklart nedenfor) custom resources for å utløse automatisk node-provisjonering, og oppretter inferensarbeidsbelastningen (`deployment` eller `statefulset`) basert på modellens forhåndskonfigurasjoner.
- **Node provisioner controller**: Controlleren heter *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den bruker `machine` CRD som stammer fra [Karpenter](https://sigs.k8s.io/karpenter) for å kommunisere med workspace controller. Den integreres med Azure Kubernetes Service (AKS) API-er for å legge til nye GPU-noder i AKS-klusteret.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) er en åpen kildekode-komponent. Den kan erstattes av andre controllere hvis de støtter [Karpenter-core](https://sigs.k8s.io/karpenter) API-er.

## Oversiktsvideo  
[Se Kaito-demoen](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installasjon

Vennligst sjekk installasjonsveiledningen [her](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Komme i gang raskt

Etter å ha installert Kaito, kan man prøve følgende kommandoer for å starte en finjusteringstjeneste.

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

Status for workspace kan følges ved å kjøre følgende kommando. Når WORKSPACEREADY-kolonnen blir `True`, er modellen distribuert med suksess.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Deretter kan man finne inferenstjenestens cluster-ip og bruke en midlertidig `curl`-pod for å teste tjenesteendepunktet i klusteret.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.