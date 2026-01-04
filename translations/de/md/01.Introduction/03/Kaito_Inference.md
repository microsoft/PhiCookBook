<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-04T06:55:25+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "de"
}
-->
## Inferenz mit Kaito 

[Kaito](https://github.com/Azure/kaito) ist ein Operator, der die Bereitstellung von AI/ML-Inferenzmodellen in einem Kubernetes-Cluster automatisiert.

Kaito weist im Vergleich zu den meisten gängigen Modell-Bereitstellungsmethoden, die auf virtuellen Maschinen basieren, folgende wichtige Unterschiede auf:

- Verwalten von Modell-Dateien mittels Container-Images. Ein HTTP-Server wird bereitgestellt, um Inferenzaufrufe mithilfe der Modellbibliothek auszuführen.
- Vermeidung des Abstimmens von Bereitstellungsparametern an die GPU-Hardware durch Bereitstellung vordefinierter Konfigurationen.
- Automatisches Bereitstellen von GPU-Knoten basierend auf Modellanforderungen.
- Hosten großer Modell-Images im öffentlichen Microsoft Container Registry (MCR), sofern die Lizenz es erlaubt.

Mit Kaito wird der Workflow zur Integration großer AI-Inferenzmodelle in Kubernetes weitgehend vereinfacht.


## Architektur

Kaito folgt dem klassischen Kubernetes Custom Resource Definition(CRD)/controller Designmuster. Der Benutzer verwaltet eine `workspace` benutzerdefinierte Ressource, die die GPU-Anforderungen und die Inferenzspezifikation beschreibt. Die Kaito-Controller automatisieren die Bereitstellung, indem sie die `workspace`-Ressource abgleichen.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine-Architektur" alt="KAITO RAGEngine-Architektur">
</div>

Die obige Abbildung zeigt die Übersicht der Kaito-Architektur. Ihre Hauptkomponenten bestehen aus:

- **Workspace controller**: Er gleicht die `workspace` benutzerdefinierte Ressource ab, erstellt `machine` (weiter unten erläutert) benutzerdefinierte Ressourcen, um die automatische Bereitstellung von Knoten auszulösen, und erzeugt die Inferenz-Workload (`deployment` oder `statefulset`) basierend auf den vordefinierten Modellkonfigurationen.
- **Node provisioner controller**: Der Name des Controllers lautet *gpu-provisioner* im [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Er verwendet das `machine` CRD, das von [Karpenter](https://sigs.k8s.io/karpenter) stammt, um mit dem workspace controller zu interagieren. Er integriert sich mit Azure Kubernetes Service(AKS) APIs, um neue GPU-Knoten zum AKS-Cluster hinzuzufügen. 
> Hinweis: Der [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ist eine Open-Source-Komponente. Er kann durch andere Controller ersetzt werden, wenn diese die [Karpenter-core](https://sigs.k8s.io/karpenter) APIs unterstützen.

## Installation

Bitte lesen Sie die Installationsanleitung [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ACR-Pfad für Tuning-Ausgang
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Der Workspace-Status kann mit dem folgenden Befehl verfolgt werden. Wenn die WORKSPACEREADY-Spalte `True` wird, wurde das Modell erfolgreich bereitgestellt.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Anschließend kann man die Cluster-IP des Inferenzdienstes finden und einen temporären `curl`-Pod verwenden, um den Service-Endpunkt im Cluster zu testen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Schnellstart Inferenz Phi-3 mit Adaptern

Nach der Installation von Kaito kann man die folgenden Befehle ausprobieren, um einen Inferenzdienst zu starten.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ACR-Ausgabepfad für Tuning
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Der Workspace-Status kann mit dem folgenden Befehl verfolgt werden. Wenn die WORKSPACEREADY-Spalte `True` wird, wurde das Modell erfolgreich bereitgestellt.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Anschließend kann man die Cluster-IP des Inferenzdienstes finden und einen temporären `curl`-Pod verwenden, um den Service-Endpunkt im Cluster zu testen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mit dem KI‑Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle, menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->