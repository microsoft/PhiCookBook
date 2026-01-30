## Kaito ಜೊತೆ ಫೈನ್-ಟ್ಯೂನಿಂಗ್ 

[Kaito](https://github.com/Azure/kaito) is an operator that automates the AI/ML inference model deployment in a Kubernetes cluster.

Kaito ಕ್ಕೆ ವರ್ಚುವಲ್ ಮೆಷಿನ್ ಮೂಲಭೂತ ಸೌಲಭ್ಯಗಳ ಮೇಲೆ ನಿರ್ಮಿತ ಬಹುಪ್ರಚಲಿತ ಮಾದರಿ ನಿಯೋಜನೆ ವಿಧಾನಗಳಿಗಿಂತ ಕೆಳಗಿನ ಪ್ರಮುಖ ವಿಭಿನ್ನತೆಗಳಿವೆ:

- ಕಂಟೈನರ್ ಇಮೇಜ್‌ಗಳನ್ನು ಬಳಸಿ ಮಾದರಿ ಫೈಲ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. ಮಾದರಿ ಲೈಬ್ರರಿಯನ್ನು ಬಳಸಿ ಇನ್ಫರೆನ್ಸ್ ಕರೆಗಳನ್ನು ನಡೆಸಲು ಒಂದು HTTP ಸರ್ವರ್ ಒದಗಿಸಲಾಗಿದೆ.
- ಪ್ರಿಸೆಟ್ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳನ್ನು ಒದಗಿಸುವ ಮೂಲಕ GPU ಹಾರ್ಡ್‌ವೇರ್‌ಗೆ ಹೊಂದಿಸಲು ನಿಯೋಜನೆ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಟ್ಯೂನ್ ಮಾಡಬೇಕಾಗುವುದನ್ನು ತಪ್ಪಿಸುತ್ತದೆ.
- ಮಾದರಿ ಅವಶ್ಯಕತೆಗಳ ಆಧಾರದ ಮೇಲೆ GPU ನೋಡ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಒದಗಿಸುತ್ತದೆ.
- ಲೈಸೆನ್ಸ್ ಅನುಮತಿಸಿದರೆ ದೊಡ್ಡ ಮಾದರಿ ಇಮೇಜ್‌ಗಳನ್ನು ಸಾರ್ವಜನಿಕ Microsoft Container Registry (MCR) ನಲ್ಲಿ ಹೋಸ್ಟ್ ಮಾಡಬಹುದು.

Kaito ಬಳಸಿ, Kubernetes ನಲ್ಲಿ ದೊಡ್ಡ AI ಇನ್ಫರೆನ್ಸ್ ಮಾದರಿಗಳನ್ನು ಆನ್‌ಬೋರ್ಡ್ ಮಾಡುವ ಕೆಲಸ ಬಹಳಷ್ಟು ಸರಳವಾಗುತ್ತದೆ.


## ವಾಸ್ತುಶಿಲ್ಪ

Kaito classic Kubernetes Custom Resource Definition(CRD)/controller design pattern ಅನ್ನು ಅನುಸರಿಸುತ್ತದೆ. ಬಳಕೆದಾರರು GPU ಅಗತ್ಯಗಳು ಮತ್ತು ಇನ್ಫರೆನ್ಸ್ ಸ್ಪೆಸಿಫಿಕೇಶನ್ ಅನ್ನು ವಿವರಿಸುವ `workspace` ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್ ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತಾರೆ. Kaito ನಿಯಂತ್ರಕರು `workspace` ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್ ಅನ್ನು ಸಮನ್ವಯಗೊಳಿಸುವ ಮೂಲಕ ನಿಯೋಜನೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುತ್ತವೆ.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito ವಾಸ್ತುಶಿಲ್ಪ" alt="Kaito ವಾಸ್ತುಶಿಲ್ಪ">
</div>

ಮೇಲಿನ ಚಿತ್ರ Kaito ವಾಸ್ತುಶಿಲ್ಪದ ಅವಲೋಕನವನ್ನು ನೀಡುತ್ತದೆ. ಇದರ ಪ್ರಮುಖ ಘಟಕಗಳು ಹೀಗಿವೆ:

- **Workspace controller**: ಇದು `workspace` ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್ ಅನ್ನು ಸಮನ್ವಯಗೊಳಿಸುತ್ತದೆ, ನೋಡ್ ಸ್ವಯಂ-ಪ್ರೊವಿಷನಿಂಗ್ ಅನ್ನು ಪ್ರೇರೇಪಿಸಲು `machine` (ಕೆಳಗೆ ವಿವರಿಸಲಾಗಿದೆ) ಕಸ್ಟಮ್ ರಿಸೋರ್ಸ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ, ಮತ್ತು ಮಾದರಿ ಪ್ರಿಸೆಟ್ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳ ಆಧಾರದ ಮೇಲೆ ಇನ್ಫರೆನ್ಸ್ ಕಾರ್ಯಭಾರವನ್ನು (`deployment` ಅಥವಾ `statefulset`) ರಚಿಸುತ್ತದೆ.
- **Node provisioner controller**: ಈ ನಿಯಂತ್ರಕರ ಹೆಸರು [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ನಲ್ಲಿ *gpu-provisioner* ಆಗಿದೆ. ಇದು workspace ನಿಯಂತ್ರಕದೊಂದಿಗೆ ಸಂವಹನಿಸಲು [Karpenter](https://sigs.k8s.io/karpenter)ದಿಂದ ಉಂಟಾದ `machine` CRD ಅನ್ನು ಬಳಸುತ್ತದೆ. ಇದು ಹೊಸ GPU ನೋಡ್‌ಗಳನ್ನು AKS ಕ್ಲಸ್ಟರ್‌ಗೆ ಸೇರಿಸಲು Azure Kubernetes Service(AKS) APIಗಳನ್ನು ಉಪಯೋಗಿಸುತ್ತದೆ. 
> ಗಮನಿಸಿ: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## ಅವಲೋಕನ ವಿಡಿಯೋ 
[Kaito ಡೆಮೊ ವೀಕ್ಷಿಸಿ](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## ಸ್ಥಾಪನೆ

ದಯವಿಟ್ಟು ಸ್ಥಾಪನೆ ಮಾರ್ಗದರ್ಶನವನ್ನು [ಇಲ್ಲಿ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ಪರಿಶೀಲಿಸಿ.

## ತ್ವರಿತ ಪ್ರಾರಂಭ

Kaito ಅನ್ನು ಸ್ಥಾಪಿಸಿದ ನಂತರ, ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಲು ಕೆಳಗಿನ ಆದೇಶಗಳನ್ನು ಪ್ರಯತ್ನಿಸಬಹುದು.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ಟ್ಯೂನಿಂಗ್ ಔಟ್‌ಪುಟ್ ACR ಮಾರ್ಗ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

The workspace status can be tracked by running the following command. When the WORKSPACEREADY column becomes `True`, the model has been deployed successfully.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Next, one can find the inference service's cluster ip and use a temporal `curl` pod to test the service endpoint in the cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ Co-op Translator (https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದೆನ್ನುವ ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿರಲಿ. ಮೂಲದ ಸ್ಟ್ರಿಂಗ್‌ನಲ್ಲಿರುವ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮತ್ತು ಪ್ರಾಧಿಕಾರಿಯಾದ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗರ್ಭಿತತೆಗಳಿಗೆ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->