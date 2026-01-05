<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T14:01:24+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pa"
}
-->
## Kaito ਨਾਲ ਅਨੁਮਾਨ ਲਗਾਉਣਾ

[Kaito](https://github.com/Azure/kaito) ਇੱਕ ਓਪਰੇਟਰ ਹੈ ਜੋ Kubernetes ਕਲਸਟਰ ਵਿੱਚ AI/ML ਅਨੁਮਾਨ ਮਾਡਲ ਤੈਅ ਕਰਨ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।

Kaito ਦੀਆਂ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਜੋ ਬਹੁਤ ਸਾਰੇ ਪ੍ਰਮੁੱਖ ਮਾਡਲ ਤੈਅ ਕਰਨ ਦੇ ਤਰੀਕਿਆਂ ਨਾਲ ਤੁਲਨਾ ਕਰਨ 'ਤੇ ਵੱਖਰੀਆਂ ਹਨ, ਜੋ ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਇੰਫ਼ਰਾਸਟਰੱਕਚਰਾਂ ਉਤੇ ਬਣਾਏ ਗਏ ਹਨ:

- ਮਾਡਲ ਫਾਇਲਾਂ ਨੂੰ ਕੰਟੇਨਰ ਚਿੱਤਰਾਂ ਦੁਆਰਾ ਪ੍ਰਬੰਧਿਤ ਕਰੋ। ਇੱਕ http ਸਰਵਰ ਪ੍ਰਦਾਨ ਕੀਤਾ ਗਿਆ ਹੈ ਜੋ ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਮਾਨ ਕਾਲਾਂ ਨੂੰ ਅੰਜਾਮ ਦਿੰਦਾ ਹੈ।
- GPU ਹਾਰਡਵੇਅਰ ਦਾ ਫਿਟ ਕਰਨ ਲਈ ਡਿਪਲਾਯਮੈਂਟ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਟਿਊਨ ਕਰਨ ਤੋਂ ਬਚੋ ਪ੍ਰੀਸੈੱਟ ਕੋਨਫਿਗਰੇਸ਼ਨਾਂ ਪ੍ਰਦਾਨ ਕਰਕੇ।
- ਮਾਡਲ ਦੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ GPU ਨੋਡਾਂ ਨੂੰ ਆਟੋ-ਪ੍ਰੋਵੀਜਨ ਕਰੋ।
- ਜੇ ਲਾਇਸੈਂਸ ਆਗਿਆ ਦਿੰਦੀ ਹੈ ਤਾਂ ਵੱਡੇ ਮਾਡਲ ਇਮੇਜਾਂ ਨੂੰ ਪਬਲਿਕ ਮਾਇਕ੍ਰੋਸਾਫਟ ਕੰਟੇਨਰ ਰਜਿਸਟਰੀ (MCR) ਵਿੱਚ ਹੋਸਟ ਕਰੋ।

Kaito ਦੀ ਵਰਤੋਂ ਕਰਕੇ, Kubernetes ਵਿੱਚ ਵੱਡੇ AI ਅਨੁਮਾਨ ਮਾਡਲਾਂ ਨੂੰ ਓਨਬੋਰਡ ਕਰਨ ਦਾ ਵਰਕਫਲੋ ਬਹੁਤ ਹੱਦ ਤੱਕ ਸੌਖਾ ਹੋ ਜਾਂਦਾ ਹੈ।

## ਆਰਕੀਟੈਕਚਰ

Kaito ਪਾਰੰਪਰਿਕ Kubernetes ਕਸਟਮ ਰਿਸੋਰਸ ਡਿਫਿਨੀਸ਼ਨ(CRD)/ਕੰਟਰੋਲਰ ਡਿਜ਼ਾਇਨ ਪੈਟਰਨ ਦਾ ਪਾਲਣ ਕਰਦਾ ਹੈ। ਯੂਜ਼ਰ ਇੱਕ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਕਰਦਾ ਹੈ ਜੋ GPU ਲੋੜਾਂ ਅਤੇ ਅਨੁਮਾਨ ਵਿਸ਼ੇਸ਼ਤਾ ਨੂੰ ਵਰਣਨ ਕਰਦਾ ਹੈ। Kaito ਕੰਟਰੋਲਰ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰਿਕਾਂਸਿਲ ਕਰਕੇ ਤੈਅਕਰਨ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦੇ ਹਨ।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

ਉਪਰ ਦਿੱਤਾ ਚਿੱਤਰ Kaito ਆਰਕੀਟੈਕਚਰ ਦਾ ਝਲਕ ਦਿੰਦਾ ਹੈ। ਇਸਦੇ ਮੁੱਖ ਘਟਕਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

- **ਵਰਕਸਪੇਸ ਕੰਟਰੋਲਰ**: ਇਹ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰਿਕਾਂਸਿਲ ਕਰਦਾ ਹੈ, ਨੋਡ ਆਟੋ ਪ੍ਰੋਵੀਜਨਿੰਗ ਨੂੰ ਟ੍ਰਿਗਰ ਕਰਨ ਲਈ `machine` (ਹੇਠਾਂ ਵਿਆਖਿਆ ਕੀਤੀ ਗਈ) ਕਸਟਮ ਰਿਸੋਰਸ ਬਣਾਉਂਦਾ ਹੈ, ਅਤੇ ਮਾਡਲ ਪ੍ਰੀਸੈੱਟ ਕੋਨਫਿਗਰੇਸ਼ਨਾਂ ਉੱਤੇ ਅਧਾਰਿਤ ਅਨੁਮਾਨ ਵਰਕਲੋਡ (`deployment` ਜਾਂ `statefulset`) ਬਣਾਉਂਦਾ ਹੈ।
- **ਨੋਡ ਪ੍ਰੋਵੀਜਨਰ ਕੰਟਰੋਲਰ**: ਕੰਟਰੋਲਰ ਦਾ ਨਾਮ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ਵਿੱਚ *gpu-provisioner* ਹੈ। ਇਹ `machine` CRD ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ [Karpenter](https://sigs.k8s.io/karpenter) ਤੋਂ ਉਤਪੰਨ ਹੁੰਦੀ ਹੈ, ਤਾਂ ਜੋ ਵਰਕਸਪੇਸ ਕੰਟਰੋਲਰ ਨਾਲ ਇੰਟਰੈਕਟ ਕੀਤਾ ਜਾ ਸਕੇ। ਇਹ Azure Kubernetes Service(AKS) APIs ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਨਵੇਂ GPU ਨੋਡ AKS ਕਲਸਟਰ ਵਿੱਚ ਜੋੜੇ ਜਾ ਸਕਣ। 
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ਇੱਕ ਖੁੱਲੇ ਸਰੋਤ ਕੰਪੋਨੈਂਟ ਹੈ। ਇਹ ਹੋਰ ਕੰਟਰੋਲਰਾਂ ਨਾਲ ਬਦਲਾ ਜਾ ਸਕਦਾ ਹੈ ਜੇ ਉਹ [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ਦਾ ਸਮਰਥਨ ਕਰਦੇ ਹਨ।

## ਇੰਸਟਾਲੇਸ਼ਨ

ਕਿਰਪਾ ਕਰਕੇ ਇੰਸਟਾਲੇਸ਼ਨ ਦੇ ਨਿਰਦੇਸ਼ਾਂ ਨੂੰ [ਇੱਥੇ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ਵੇਖੋ।

## ਜਲਦੀ ਸ਼ੁਰੂਆਤ ਅਨੁਮਾਨ Phi-3
[ਸੈਂਪਲ ਕੋਡ ਅਨੁਮਾਨ Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ਆਉਟਪੁੱਟ ACR ਰਾਹ ਦੀ ਟਿਊਨਿੰਗ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

ਨਿਮਨਲਿਖਿਤ ਕਮਾਣਡ ਚਲਾਕੇ ਵਰਕਸਪੇਸ ਦੀ ਸਥਿਤੀ ਟਰੈਕ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਜਦ WORKSPACEREADY ਕਾਲਮ `True` ਹੋ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਤੈਅ ਕੀਤਾ ਗਿਆ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

ਫਿਰ, ਅਨੁਮਾਨ ਸੇਵਾ ਦਾ ਕਲਸਟਰ ਆਈਪੀ ਲੱਭ ਕੇ ਇੱਕ ਅਸਥਾਈ `curl` ਪੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਲਸਟਰ ਵਿਚ ਸੇਵਾ ਦੇ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## ਅਡੈਪਟਰਾਂ ਨਾਲ ਜਲਦੀ ਸ਼ੁਰੂਆਤ ਅਨੁਮਾਨ Phi-3

Kaito ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਨਿਮਨਲਿਖਿਤ ਕਮਾਣਡਾਂ ਨੂੰ ਅਜਮਾਕੇ ਅਨੁਮਾਨ ਸੇਵਾ ਸ਼ੁਰੂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

[ਸੈਂਪਲ ਕੋਡ ਅਨੁਮਾਨ Phi-3 ਅਡੈਪਟਰਾਂ ਨਾਲ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ਆਉਟਪੁੱਟ ACR ਪਥ ਨੂੰ ਟਿਊਨ ਕਰਨਾ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

ਵਰਕਸਪੇਸ ਦੀ ਸਥਿਤੀ ਨੂੰ ਟਰੈਕ ਕਰਨ ਲਈ ਨਿਮਨਲਿਖਿਤ ਕਮਾਣਡ ਚਲਾਈ ਜਾ ਸਕਦੀ ਹੈ। ਜਦ WORKSPACEREADY ਕਾਲਮ `True` ਬਣ ਜਾਂਦਾ ਹੈ, ਤਦ ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਤੈਅ ਕੀਤਾ ਗਿਆ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

ਫਿਰ, ਅਨੁਮਾਨ ਸੇਵਾ ਦੀ ਕਲਸਟਰ ਆਈਪੀ ਲੱਭ ਕੇ ਇੱਕ ਅਸਥਾਈ `curl` ਪੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਲਸਟਰ ਵਿੱਚ ਸੇਵਾ ਦੇ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਨਿਸ਼ਚਿਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਿਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->