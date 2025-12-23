<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-12-22T01:17:40+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "kn"
}
-->
## Kaito ನೊಂದಿಗೆ ಇನ್ಫರೆನ್ಸ್ 

[Kaito](https://github.com/Azure/kaito) ಒಂದು ಆಪರೇಟರ್ ಆಗಿದ್ದು, Kubernetes ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ AI/ML ಇನ್ಫರೆನ್ಸ್ ಮಾದರಿಗಳ ನಿಯೋಜನೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುತ್ತದೆ.

Kaito ಕೆಳಗಿನ ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಹೊಂದಿದೆ ಮುಕ್ತಗೊಳಿಸುತ್ತದೆ:

- ಕಂಟೇನರ್ ಇಮೇಜ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಮಾದರಿ ಫೈಲ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು. ಮಾದರಿ ಲೈಬ್ರರಿಯನ್ನು ಉಪಯೋಗಿಸಿ ಇನ್ಫರೆನ್ಸ್ ಕರೆಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸಲು http ಸರ್ವರ್ ಒದಗಿಸಲಾಗಿದೆ.
- ಪ್ರೀಸೆಟ್ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳನ್ನು ಒದಗಿಸುವ ಮೂಲಕ GPU ಹಾರ್ಡ್‌ವೇರ್‌ಗೆ ಹೊಂದಿಸಲು ನಿಯೋಜನಾ ಪರಾಮೀಟರ್‌ಗಳನ್ನು ಟ್ಯೂನ್ ಮಾಡುವ ಅವಶ್ಯಕತೆಯನ್ನು ತಪ್ಪಿಸುತ್ತದೆ.
- ಮಾದರಿ ಅಗತ್ಯಗಳ ಆಧಾರದ ಮೇಲೆ GPU ನೋಡ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪ್ರೊವಿಷನ್ ಮಾಡುತ್ತದೆ.
- ಲೈಸೆನ್ಸ್ ಅನುಮತಿಸಿದರೆ ದೊಡ್ಡ ಮಾದರಿ ಇಮೇಜ್‌ಗಳನ್ನು ಸಾರ್ವಜನಿಕ Microsoft Container Registry (MCR) ನಲ್ಲಿ ಹೋಸ್ಟ್ ಮಾಡಬಹುದು.

Kaito ಅನ್ನು ಬಳಸಿ, Kubernetes ನಲ್ಲಿ ದೊಡ್ಡ AI ಇನ್ಫರ್‌ಮೆನ್ಸ್ ಮಾದರಿಗಳನ್ನು ಒನ್‌ಬೋರ್ಡ್ ಮಾಡುವ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಬಹಳಷ್ಟು ಸರಳಗೊಳಿಸಲಾಗಿದೆ.


## ವಾಸ್ತುಶಿಲ್ಪ

Kaito ಪರಂಪರাগত Kubernetes Custom Resource Definition(CRD)/controller ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಸರಿಸುತ್ತದೆ. ಬಳಕೆದಾರರು GPU ಅಗತ್ಯಗಳು ಮತ್ತು ಇನ್ಫರೆನ್ಸ್ ವಿವರಗಳನ್ನು ವರ್ಣಿಸುವ `workspace` ಕಸ್ಟಮ್ ರೆಸೋರ್ಸ್ ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತಾರೆ. Kaito controllers ಗಳು `workspace` ಕಸ್ಟಮ್ ರೆಸೋರ್ಸ್ ಅನ್ನು ಸಮನ್ವಯಗೊಳಿಸುವ ಮೂಲಕ ನಿಯೋಜನೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುತವೆ.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito ವಾಸ್ತುಶಿಲ್ಪ" alt="Kaito ವಾಸ್ತುಶಿಲ್ಪ">
</div>

ಮೇಲಿನ ಚಿತ್ರ Kaito ವಾಸ್ತುಶಿಲ್ಪ ಅವಲೋಕನವನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ. ಇದರ ಪ್ರಮುಖ ಘಟಕಗಳು ಒಳಗೊಂಡಿವೆ:

- **Workspace controller**: ಇದು `workspace` ಕಸ್ಟಮ್ ರೆಸೋರ್ಸ್ ಅನ್ನು ಸಮನ್ವಯಗೊಳಿಸುತ್ತದೆ, ನೋಡ್ ಸ್ವಯಂ ಪ್ರೊವಿಷನಿಂಗ್ ಅನ್ನು ಪ್ರೇರೇಪಿಸಲು `machine` (ಕೆಳಗೆ ವಿವರಿಸಲಾಗಿದೆ) ಕಸ್ಟಮ್ ರೆಸೋರ್ಸ್‌ಗಳನ್ನು ರಚಿಸುತ್ತದೆ, ಮತ್ತು ಮಾದರಿ ಪ್ರಿಸೆಟ್ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳ ಆಧಾರದ ಮೇಲೆ ಇನ್ಫರೆನ್ಸ್ ವರ್ಕ್‌ಲೋಡ್ (`deployment` ಅಥವಾ `statefulset`) ರಚಿಸುತ್ತದೆ.
- **Node provisioner controller**: The controller's name is *gpu-provisioner* in [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). It uses the `machine` CRD originated from [Karpenter](https://sigs.k8s.io/karpenter) to interact with the workspace controller. It integrates with Azure Kubernetes Service(AKS) APIs to add new GPU nodes to the AKS cluster. 
> ಗಮನಿಸಿ: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## ಸ್ಥಾಪನೆ

ದಯವಿಟ್ಟು ಸ್ಥಾಪನೆ ಮಾರ್ಗದರ್ಶನವನ್ನು [ಇಲ್ಲಿ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ಪರಿಶೀಲಿಸಿ.

## Phi-3 ಇನ್ಫರೆನ್ಸ್‌ಗೆ ತ್ವರಿತ ಪ್ರಾರಂಭ
[ಉದಾಹರಣಾ ಕೋಡ್: Phi-3 ಇನ್ಫರೆನ್ಸ್](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ಟ್ಯೂನಿಂಗ್ ಔಟ್‌ಪುಟ್ ACR ಮಾರ್ಗ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು 실행 ಮಾಡುವ ಮೂಲಕ workspace ಸ್ಥಿತಿಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದು. WORKSPACEREADY ಕಾಲಮ್ `True` ಆಗಿದ್ರೆ, ಮಾದರಿ ಯಶಸ್ವಿಯಾಗಿ ನಿಯೋಜಿಸಲಾಗಿದೆ.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

ಮುಂದೆ, ಇನ್ಫರೆನ್ಸ್ ಸೇವೆಯ ಕ್ಲಸ್ಟರ್ ip ಅನ್ನು ಕಂಡು, ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ ಸೇವೆ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಲು ತಾತ್ಕಾಲಿಕ `curl` ಪೊಡ್ ಅನ್ನು ಬಳಸಬಹುದು.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Phi-3 ಇನ್ಫರೆನ್ಸ್ ಅಡಾಪ್ಟರ್‌ಗಳೊಂದಿಗೆ ತ್ವರಿತ ಪ್ರಾರಂಭ

Kaito ಅನ್ನು ಸ್ಥಾಪಿಸಿದ ನಂತರ, ಇನ್ಫರೆನ್ಸ್ ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಲು ಕೆಳಗಿನ ಆಜ್ಞೆಗಳು ಪ್ರಯತ್ನಿಸಬಹುದು.

[ಉದಾಹರಣಾ ಕೋಡ್: Phi-3 ಇನ್ಫರೆನ್ಸ್ ಅಡಾಪ್ಟರ್‌ಗಳೊಂದಿಗೆ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ಔಟ್‌ಪುಟ್ ACR ಮಾರ್ಗದ ಟ್ಯೂನಿಂಗ್
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು 실행 ಮಾಡುವ ಮೂಲಕ workspace ಸ್ಥಿತಿಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದು. WORKSPACEREADY ಕಾಲಮ್ `True` ಆಗಿದ್ರೆ, ಮಾದರಿ ಯಶಸ್ವಿಯಾಗಿ ನಿಯೋಜಿಸಲಾಗಿದೆ.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

ಮುಂದೆ, ಇನ್ಫರೆನ್ಸ್ ಸೇವೆಯocluster ip ಅನ್ನು ಕಂಡು, ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ ಸೇವೆ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಲು ತಾತ್ಕಾಲಿಕ `curl` ಪೊಡ್ ಅನ್ನು ಬಳಸಬಹುದು.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕರಣ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಕಷ್ಟು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಶುದ್ಧತೆಗಳಾಗಿರಬಹುದೆಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಇರುವ ದಸ್ತಾವೇಜೆಯನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅರ್ಥಭ್ರಮೆ ಅಥವಾ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೆಗೆ ನಾವು ಜವಾಬ್ದಾರಿಯಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->