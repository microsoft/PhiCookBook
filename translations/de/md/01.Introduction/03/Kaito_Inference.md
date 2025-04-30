<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-03-27T07:30:43+00:00",
  "source_file": "md\\01.Introduction\\03\\Kaito_Inference.md",
  "language_code": "de"
}
-->
## Inferenz mit Kaito 

[Kaito](https://github.com/Azure/kaito) ist ein Operator, der die Bereitstellung von KI/ML-Inferenzmodellen in einem Kubernetes-Cluster automatisiert.

Kaito bietet im Vergleich zu den meisten gängigen Modellbereitstellungsmethoden, die auf virtuellen Maschinen basieren, folgende wichtige Unterschiede:

- Modelldateien werden mithilfe von Container-Images verwaltet. Ein HTTP-Server wird bereitgestellt, um Inferenzaufrufe mithilfe der Modellbibliothek auszuführen.
- Vorkonfigurierte Einstellungen vermeiden die Anpassung von Bereitstellungsparametern an GPU-Hardware.
- Automatische Bereitstellung von GPU-Knoten basierend auf den Modellanforderungen.
- Große Modell-Images können in der öffentlichen Microsoft Container Registry (MCR) gehostet werden, sofern die Lizenz dies erlaubt.

Mit Kaito wird der Workflow zur Integration großer KI-Inferenzmodelle in Kubernetes erheblich vereinfacht.

## Architektur

Kaito folgt dem klassischen Kubernetes-Designmuster für benutzerdefinierte Ressourcen (CRD) und Controller. Der Benutzer verwaltet eine `workspace` benutzerdefinierte Ressource, die die GPU-Anforderungen und die Inferenzspezifikation beschreibt. Kaito-Controller automatisieren die Bereitstellung, indem sie die `workspace` benutzerdefinierte Ressource abgleichen.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito Architektur" alt="Kaito Architektur">
</div>

Die obige Abbildung zeigt eine Übersicht der Kaito-Architektur. Zu den Hauptkomponenten gehören:

- **Workspace-Controller**: Dieser gleicht die `workspace` benutzerdefinierte Ressource ab, erstellt `machine` (unten erklärt) benutzerdefinierte Ressourcen, um die automatische Bereitstellung von Knoten auszulösen, und erstellt die Inferenz-Workload (`deployment` oder `statefulset`) basierend auf den vorkonfigurierten Modelleinstellungen.
- **Node-Provisioner-Controller**: Der Name des Controllers ist *gpu-provisioner* im [gpu-provisioner Helm Chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Er verwendet die `machine` CRD, die von [Karpenter](https://sigs.k8s.io/karpenter) stammt, um mit dem Workspace-Controller zu interagieren. Der Controller integriert sich mit den Azure Kubernetes Service (AKS)-APIs, um neue GPU-Knoten zum AKS-Cluster hinzuzufügen.
> Hinweis: Der [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ist eine Open-Source-Komponente. Er kann durch andere Controller ersetzt werden, sofern diese die [Karpenter-core](https://sigs.k8s.io/karpenter) APIs unterstützen.

## Installation

Die Installationsanleitung finden Sie [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Schnelleinstieg Inferenz Phi-3
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

Der Status des Workspaces kann durch den folgenden Befehl verfolgt werden. Sobald die Spalte WORKSPACEREADY den Wert `True` zeigt, wurde das Modell erfolgreich bereitgestellt.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Anschließend kann die Cluster-IP des Inferenzdienstes gefunden und ein temporärer `curl`-Pod verwendet werden, um den Dienstendpunkt im Cluster zu testen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Schnelleinstieg Inferenz Phi-3 mit Adaptern

Nach der Installation von Kaito können folgende Befehle verwendet werden, um einen Inferenzdienst zu starten.

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

Der Status des Workspaces kann durch den folgenden Befehl verfolgt werden. Sobald die Spalte WORKSPACEREADY den Wert `True` zeigt, wurde das Modell erfolgreich bereitgestellt.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Anschließend kann die Cluster-IP des Inferenzdienstes gefunden und ein temporärer `curl`-Pod verwendet werden, um den Dienstendpunkt im Cluster zu testen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.