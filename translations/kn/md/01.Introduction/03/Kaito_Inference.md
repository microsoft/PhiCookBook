## ರೈತೊ ಸಹಿತ ನಿರ್ಣಯ 

[ಕೈತೊ](https://github.com/Azure/kaito) ಎಂಬುದು ಕುಬರ್‌ನೆಟೀಸ್ ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ AI/ML ನಿರ್ಣಯ ಮಾದರಿ ನಿಯೋಜನೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವ ಕಾರ್ಯಾಚರಣೆಗಾರನು.

ವರ್ಚುಯಲ್ ಮೆಷಿನ್ ಮೂಲಸೌಕರ್ಯಗಳ ಮೇಲೆ ನಿರ್ಮಿಸಲಾದ ಬಹು ಮейн‌ಸ್ಟ್ರೀಂ ಮಾದರಿ ನಿಯೋಜನೆ ವಿಧಾನಗಳಿಗಿಂತ ಕೈತೊ ಕೆಳಗಿನ ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಹೊಂದಿದೆ:

- ಮಾದರಿ ಕಡತಗಳನ್ನು ಕಂಟೈನರ್ ಚಿತ್ರಗಳ ಮೂಲಕ ನಿರ್ವಹಿಸು. ಮಾದರಿ ಪಠ್ಯಗ್ರಂಥಾಲಯ ಬಳಸಿ ನಿರ್ಣಯ ಕರೆಗಳನ್ನು ಮಾಡಲು http ಸರ್ವರ್ ಒದಗಿಸಲಾಗುತ್ತದೆ.
- GPU ಹಾರ್ಡ್‌ವೇರ್‌ಗೆ ಹೊಂದಿಕೊಳ್ಳುವಂತೆ ನಿಯೋಜನೆ ನಿಯತಾಂಕಗಳನ್ನು ಸೂಕ್ಷ್ಮಗೊಳಿಸುವುದನ್ನು ತಪ್ಪಿಸುವ ಮೂಲಕ ಹಿಂದಿತವರಿಗೆ ಗೂಡಿಮಾಡಿದ ಕಾನ್ಫಿಗರೇಶನ್ ಒದಗಿಸುವುದು.
- ಮಾದರಿ ಅಗತ್ಯಗಳನ್ನು ಆಧರಿಸಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ GPU ನೋಡ್‌ಗಳನ್ನು ಒದಗಿಸುವುದು.
- ಪರವಾನಗಿ ಅನುಮತಿಸಿದರೆ ಸಾರ್ವಜನಿಕ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಕಂಟೈನರ್ ರೆಜಿಸ್ಟ್ರಿ (MCR)ಯಲ್ಲಿ ದೊಡ್ಡ ಮಾದರಿ ಚಿತ್ರಗಳನ್ನು ಹೋಸ್ಟ್ ಮಾಡುವುದು.

ಕೈತೊ ಬಳಸಿ, ಕುಬರ್‌ನೆಟೀಸ್‌ನಲ್ಲಿ ದೊಡ್ಡ AI ನಿರ್ಣಯ ಮಾದರಿಗಳನ್ನು ಒಳಗೊಂಡಿರುವ ಕಾರ್ಯನಿರ್ವಹಣಾ ಪ್ರವಾಹ ಬಹಳ ಸರಳಗೊಳ್ಳುತ್ತದೆ.


## ವಾಸ್ತುಶಿಲ್ಪ

ಕೈತೊ ಪಾರಂಪರಿಕ ಕುಬರ್‌ನೆಟೀಸ್ ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್ ಡೆಫಿನಿಷನ್(CRD)/ಕಂಟ್ರೋಲ್ಲರ್ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಸರಿಸುತ್ತದೆ. ಬಳಕೆದಾರನು GPU ಅಗತ್ಯಗಳು ಮತ್ತು ನಿರ್ಣಯ ವಿವರಗಳನ್ನು ವಿವರಿಸುವ `workspace` ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್ ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತಾನೆ. ಕೈತೊ ಕಂಟ್ರೋಲ್ಲರ್‌ಗಳು `workspace` ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್ ಅನ್ನು ಸಮನ್ವಯಗೊಳಿಸುವ ಮೂಲಕ ನಿಯೋಜನೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುತ್ತವೆ.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

ಮೇಲಿನ ಚಿತ್ರವು ಕೈತೊ ವಾಸ್ತುಶಿಲ್ಪದ ಅವಲೋಕನವನ್ನು ನೀಡುತ್ತದೆ. ಅದರ ಪ್ರಮುಖ ಅಂಶಗಳು:

- **ವರ್ಕ್‌ಸ್ಪೇಸ್ ಕಂಟ್ರೋಲ್ಲರ್**: ಇದು `workspace` ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್ ಅನ್ವಯ ಸಮನ್ವಯಗೊಳ್ಳುತ್ತದೆ, ನೋಡ್ ಸ್ವಯಂ ನಿಯೋಜನೆಗೆ ಪ್ರೇರೇಪಣೆ ನೀಡಲು `machine` (ಕೆಳಗಿನ ವಿವರ) ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್‌ಗಳನ್ನು ರಚಿಸುತ್ತದೆ ಮತ್ತು ಮಾದರಿ ಪೂರ್ವನಿಗದಿತ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳ ಆಧಾರದ ಮೇಲೆ ನಿರ್ಣಯ ಕಾರ್ಯಭಾರ (`deployment` ಅಥವಾ `statefulset`) ರಚಿಸುತ್ತದೆ.
- **ನೋಡ್ ಪ್ರಾವಿಜನರ್ ಕಂಟ್ರೋಲ್ಲರ್**: ಈ ಕಂಟ್ರೋಲ್ಲರ್ ಹೆಸರೇ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ನಲ್ಲಿ *gpu-provisioner*. ಇದು [Karpenter](https://sigs.k8s.io/karpenter) ಮೂಲದ `machine` CRD ಬಳಸಿ ವರ್ಕ್‌ಸ್ಪೇಸ್ ಕಂಟ್ರೋಲ್ಲರ್ ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡುತ್ತದೆ. AKS ಕ್ಲಸ್ಟರ್‌ಗೆ ಹೊಸ GPU ನೋಡ್‌ಗಳನ್ನು ಸೇರಿಸಲು Azure Kubernetes Service(AKS) APIಗಳೊಂದಿಗೆ ಒಟ್ಟುಗೂಡಿಸುತ್ತದೆ.
> ಗಮನಿಸಿ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ಒಂದು खुलಿ ಮೂಲಾಂಶ ಘಟಕ. ಅದು [Karpenter-core](https://sigs.k8s.io/karpenter) APIಗಳನ್ನು ಬೆಂಬಲಿಸುವ ಇತರೆ ಕಂಟ್ರೋಲ್ಲರ್‌ಗಳಿಂದ ವಿನಿಮಯಗೊಳ್ಳಬಹುದಾಗಿದೆ.

## ಸ್ಥಾಪನೆ

ದಯವಿಟ್ಟು ಸ್ಥಾಪನಾ ಮಾರ್ಗದರ್ಶನವನ್ನು [ಇಲ್ಲಿ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ಪರಿಶೀಲಿಸಿ.

## ಶೀಘ್ರ ಆರಂಭ ನಿರ್ಣಯ Phi-3
[ನಮೂನಾ ಕೋಡ್ ನಿರ್ಣಯ Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ಔಟ್‌ಪುಟ್ ACR ಮಾರ್ಗವನ್ನು ಸರಿಹೊಂದಿಸಲಾಗುತ್ತಿದೆ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಚಾಲನೆಮಾಡಿ ವರ್ಕ್‌ಸ್ಪೇಸ್ ಸ್ಥಿತಿ ಹತ್ತಿರವಾಗಿರಬಹುದು. WORKSPACEREADY ಕಾಲಮ್ `True` ಆಗಿದಾಗ, ಮಾದರಿಯು ಯಶಸ್ವಿಯಾಗಿ ನಿಯೋಜಿಸಲಾಗಿದೆ.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

ಮುಂದೆ, ನಿರ್ಣಯ ಸೇವೆಯ ಕ್ಲಸ್ಟರ್ ಐಪಿಯನ್ನು ಪತ್ತೆಮಾಡಿ, ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ ಸೇವೆ ಅಂತ್ಯಬಿಂದುವನ್ನು ಪರೀಕ್ಷಿಸಲು ಒಂದು ತಾತ್ಕಾಲಿಕ `curl` ಪಾಡ್ ಅನ್ನು ಬಳಸಿ.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## ಅಡಾಪ್ಟರ್‌ಗಳೊಂದಿಗೆ ಶೀಘ್ರ ಆರಂಭ ನಿರ್ಣಯ Phi-3

ಕೈತೊ ಸ್ಥಾಪನೆಯ ನಂತರ, ನಿರ್ಣಯ ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಲು ಕೆಳಗಿನ ಆಜ್ಞೆಗಳನ್ನು ಪ್ರಯತ್ನಿಸಬಹುದು.

[ಅಡಾಪ್ಟರ್‌ಗಳೊಂದಿಗೆ ನಿರ್ಣಯ Phi-3 ನಂೂನೆ ಕೋಡ್](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ಆಉಟ್ಪುಟ್ ACR ಮಾರ್ಗವನ್ನು ಟ್ಯೂನಿಂಗ್ ಮಾಡುವುದು
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

ಕೆಳಗಿನ ಆಜ್ಞೆ ಚಲಾಯಿಸಿ ವರ್ಕ್‌ಸ್ಪೇಸ್ ಸ್ಥಿತಿಯನ್ನು ಹತ್ತಿರವಾಗಿರಬಹುದು. WORKSPACEREADY ಕಾಲಮ್ `True` ಆಗಿದಾಗ, ಮಾದರಿಯು ಯಶಸ್ವಿಯಾಗಿ ನಿಯೋಜಿಸಲಾಗಿದೆ.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

ಮುಂದಕ್ಕೆ, ನಿರ್ಣಯ ಸೇವೆಯ ಕ್ಲಸ್ಟರ್ ಐಪಿಯನ್ನು ಕಂಡುಹಿಡಿದು, ಕ್ಲಸ್ಟರ್‌ನಲ್ಲಿ ಸೇವೆ ಅಂತ್ಯವನ್ನು ಪರೀಕ್ಷಿಸಲು ತಾತ್ಕಾಲಿಕ `curl` ಪಾಡ್ ಅನ್ನು ಬಳಸಿ.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತ್ಯಾಗಪತ್ರ**:  
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಗೆ ಪ್ರಯತ್ನಿಸುತ್ತೇವೆ ಎನಿಸಿಕೊಂಡರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದು ಎಂಬದನ್ನು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿರಿಸಿ. ಮೂಲ ಭಾಷೆಯ ದಾಖಲೆ ಅನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸುವುದು ಸೂಕ್ತ. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->