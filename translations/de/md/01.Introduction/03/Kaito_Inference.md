<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-07T10:44:19+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "de"
}
-->
## Inferenz mit Kaito

[Kaito](https://github.com/Azure/kaito) ist ein Operator, der die Bereitstellung von AI/ML-Inferenzmodellen in einem Kubernetes-Cluster automatisiert.

Kaito hebt sich durch folgende wesentliche Merkmale von den meisten gängigen Methoden zur Modellauslieferung ab, die auf virtuellen Maschinen basieren:

- Verwaltung von Modell-Dateien über Container-Images. Ein HTTP-Server wird bereitgestellt, um Inferenzaufrufe mit der Modellbibliothek durchzuführen.
- Vermeidung der Anpassung von Bereitstellungsparametern an die GPU-Hardware durch vordefinierte Konfigurationen.
- Automatische Bereitstellung von GPU-Knoten basierend auf den Modellanforderungen.
- Hosting großer Modell-Images im öffentlichen Microsoft Container Registry (MCR), sofern die Lizenz dies erlaubt.

Mit Kaito wird der Workflow zur Integration großer AI-Inferenzmodelle in Kubernetes deutlich vereinfacht.

## Architektur

Kaito folgt dem klassischen Kubernetes Custom Resource Definition (CRD)/Controller-Designmuster. Der Benutzer verwaltet eine `workspace` Custom Resource, die die GPU-Anforderungen und die Inferenzspezifikation beschreibt. Die Kaito-Controller automatisieren die Bereitstellung, indem sie die `workspace` Custom Resource abgleichen.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Die obige Abbildung zeigt einen Überblick über die Kaito-Architektur. Die Hauptkomponenten bestehen aus:

- **Workspace-Controller**: Er gleicht die `workspace` Custom Resource ab, erstellt `machine` (unten erklärt) Custom Resources, um die automatische Bereitstellung von Knoten auszulösen, und erstellt die Inferenz-Workloads (`deployment` oder `statefulset`) basierend auf den vordefinierten Modellkonfigurationen.
- **Node Provisioner Controller**: Der Controller heißt *gpu-provisioner* im [gpu-provisioner Helm Chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Er verwendet die `machine` CRD, die von [Karpenter](https://sigs.k8s.io/karpenter) stammt, um mit dem Workspace-Controller zu interagieren. Er integriert sich in die Azure Kubernetes Service (AKS) APIs, um neue GPU-Knoten zum AKS-Cluster hinzuzufügen.
> Hinweis: Der [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ist eine Open-Source-Komponente. Er kann durch andere Controller ersetzt werden, sofern diese die [Karpenter-core](https://sigs.k8s.io/karpenter) APIs unterstützen.

## Installation

Bitte beachten Sie die Installationsanleitung [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Schnellstart Inferenz Phi-3
[Beispielcode Inferenz Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Den Status des Workspace kann man mit folgendem Befehl verfolgen. Sobald die Spalte WORKSPACEREADY auf `True` steht, wurde das Modell erfolgreich bereitgestellt.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Anschließend kann man die Cluster-IP des Inferenzdienstes ermitteln und einen temporären `curl`-Pod verwenden, um den Service-Endpunkt im Cluster zu testen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Schnellstart Inferenz Phi-3 mit Adaptern

Nach der Installation von Kaito kann man folgende Befehle ausprobieren, um einen Inferenzdienst zu starten.

[Beispielcode Inferenz Phi-3 mit Adaptern](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Den Status des Workspace kann man mit folgendem Befehl verfolgen. Sobald die Spalte WORKSPACEREADY auf `True` steht, wurde das Modell erfolgreich bereitgestellt.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Anschließend kann man die Cluster-IP des Inferenzdienstes ermitteln und einen temporären `curl`-Pod verwenden, um den Service-Endpunkt im Cluster zu testen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.