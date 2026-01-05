<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T02:41:36+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pa"
}
-->
## Kaito ਨਾਲ ਇੰਫਰੈਂਸ 

[Kaito](https://github.com/Azure/kaito) ਇੱਕ ਓਪਰੇਟਰ ਹੈ ਜੋ Kubernetes ਕਲਸਟਰ ਵਿੱਚ AI/ML ਇੰਫਰੈਂਸ ਮਾਡਲ ਦੀ ਡਿਪਲੌਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।

Kaito ਕੋਲ ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਇਨਫ੍ਰਾਸਟ੍ਰੱਕਚਰਾਂ ਦੇ ऊपर ਬਣੀ ਬਹੁਤ ਸਾਰੀਆਂ ਪ੍ਰਮੁੱਖ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਵਿਧੀਆਂ ਨਾਲੋਂ ਹੇਠ ਲਿਖੇ ਮੁੱਖ ਫਰਕ ਹਨ:

- ਮਾਡਲ ਫਾਈਲਾਂ ਨੂੰ ਕੰਟੇਨਰ ਇਮੇਜਾਂ ਦੀ ਵਰਤੋਂ ਨਾਲ ਪ੍ਰਬੰਧ ਕਰੋ। ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇੰਫਰੈਂਸ ਕਾਲ ਕਰਨ ਲਈ ਇੱਕ http ਸਰਵਰ ਪ੍ਰਦਾਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।
- ਪ੍ਰੀਸੈਟ ਸੰਰਚਨਾਵਾਂ ਮੁਹੱਈਆ ਕਰਕੇ GPU ਹਾਰਡਵੇਅਰ ਲਈ ਡਿਪਲੌਇਮੈਂਟ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਟਿਊਨ ਕਰਨ ਤੋਂ ਬਚਾਓ।
- ਮਾਡਲ ਦੀਆਂ ਲੋੜਾਂ ਦੇ ਆਧਾਰ 'ਤੇ GPU ਨੋਡ ਆਟੋ-ਪ੍ਰੋਵਾਈਜ਼ਨ ਕਰੋ।
- ਜੇ ਲਾਇਸੈਂਸ ਆਗਿਆ ਦੇਵੇ ਤਾਂ ਵੱਡੀਆਂ ਮਾਡਲ ਇਮੇਜਾਂ ਨੂੰ Public Microsoft Container Registry (MCR) ਵਿੱਚ ਹੋਸਟ ਕਰੋ।

Kaito ਦੀ ਵਰਤੋਂ ਨਾਲ, Kubernetes ਵਿੱਚ ਵੱਡੇ AI ਇੰਫਰੈਂਸ ਮਾਡਲਾਂ ਨੂੰ ਆਨਬੋਰਡ ਕਰਨ ਦੀ ਵਰਕਫਲੋ ਕਾਫੀ ਸਧਾਰਨ ਹੋ ਜਾਂਦੀ ਹੈ।


## ਆਰਕੀਟੈਕਚਰ

Kaito classic Kubernetes Custom Resource Definition(CRD)/controller ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ। ਯੂਜ਼ਰ ਇੱਕ `workspace` custom resource ਦਾ ਪ੍ਰਬੰਧ ਕਰਦਾ ਹੈ ਜੋ GPU ਦੀਆਂ ਜ਼ਰੂਰਤਾਂ ਅਤੇ ਇੰਫਰੈਂਸ ਵਿਸ਼ੇਸ਼ਣ ਨੂੰ ਵੇਰਵਾ ਕਰਦਾ ਹੈ। Kaito ਕੰਟਰੋਲਰ `workspace` custom resource ਨੂੰ reconcile ਕਰਕੇ ਡਿਪਲੌਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦੇ ਹਨ।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine ਆਰਕੀਟੈਕਚਰ" alt="KAITO RAGEngine ਆਰਕੀਟੈਕਚਰ">
</div>

ਉੱਪਰ ਦਿੱਤੀ ਆਕਰਸ਼ਕ ਚਿੱਤਰ Kaito ਆਰਕੀਟੈਕਚਰ ਦਾ ਸੰਖੇਪ ਦਰਸਾਉਂਦੀ ਹੈ। ਇਸ ਦੇ ਮੁੱਖ ਘਟਕ ਹੇਠਾਂ ਦਿੱਤੇ ਹਨ:

- **Workspace controller**: ਇਹ `workspace` custom resource ਨੂੰ reconcile ਕਰਦਾ ਹੈ, ਨੋਡ ਆਟੋ ਪ੍ਰੋਵਿਜਨਿੰਗ ਨੂੰ ਟ੍ਰਿਗਰ ਕਰਨ ਲਈ `machine` (ਥੱਲੇ ਵਿਆਖਿਆ ਕੀਤੀ گئی) custom resources ਬਣਾਉਂਦਾ ਹੈ, ਅਤੇ ਮਾਡਲ ਪ੍ਰੀਸੈਟ ਸੰਰਚਨਾਵਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਇੰਫਰੈਂਸ ਵਰਕਲੋਡ (`deployment` ਜਾਂ `statefulset`) ਬਣਾਉਂਦਾ ਹੈ।
- **Node provisioner controller**: ਕੰਟਰੋਲਰ ਦਾ ਨਾਂ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ਵਿੱਚ *gpu-provisioner* ਹੈ। ਇਹ Karpenter ਤੋਂ ਉਤਪੰਨ `machine` CRD ਦੀ ਵਰਤੋਂ ਕਰਕੇ workspace controller ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਦਾ ਹੈ। ਇਹ Azure Kubernetes Service(AKS) APIs ਨਾਲ ਇੰਟੇਗ੍ਰੇਟ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ AKS ਕਲਸਟਰ ਵਿੱਚ ਨਵੇਂ GPU ਨੋਡ ਜੋੜੇ ਜਾ ਸਕਣ। 
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## ਇੰਸਟਾਲੇਸ਼ਨ

ਕਿਰਪਾ ਕਰਕੇ ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਮਦਦ-ਰਾਹ [ਇਥੇ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ਵੇਖੋ।

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ ਇੰਫਰੈਂਸ Phi-3
[ਸੈਂਪਲ ਕੋਡ ਇੰਫਰੈਂਸ Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ਆਉਟਪੁੱਟ ACR ਮਾਰਗ ਦੀ ਟਿਊਨਿੰਗ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਚਲਾ ਕੇ workspace ਦੀ ਸਥਿਤੀ ਦੀ ਟ੍ਰੈਕਿੰਗ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਜਦੋਂ WORKSPACEREADY ਕਾਲਮ `True` ਹੋ ਜਾਂਦਾ ਹੈ, ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਤੈਨਾਤ ਕੀਤਾ ਗਿਆ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਤੁਸੀਂ ਇੰਫਰੈਂਸ ਸਰਵਿਸ ਦਾ ਕਲਸਟਰ IP ਲੱਭ ਸਕਦੇ ਹੋ ਅਤੇ ਕਲਸਟਰ ਵਿੱਚ ਸਰਵਿਸ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਅਸਥਾਈ `curl` ਪੌਡ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ ਇੰਫਰੈਂਸ Phi-3 ਅਡੈਪਟਰਾਂ ਨਾਲ

Kaito ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਹੇਠ ਲਿਖੇ ਕਮਾਂਡਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਕੇ ਇੱਕ ਇੰਫਰੈਂਸ ਸਰਵਿਸ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।

[ਸੈਂਪਲ ਕੋਡ ਇੰਫਰੈਂਸ Phi-3 ਅਡੈਪਟਰਾਂ ਨਾਲ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ਟਿਊਨਿੰਗ ਆਉਟਪੁੱਟ ACR ਪਾਥ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਚਲਾ ਕੇ workspace ਦੀ ਸਥਿਤੀ ਦੀ ਟ੍ਰੈਕਿੰਗ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਜਦੋਂ WORKSPACEREADY ਕਾਲਮ `True` ਹੋ ਜਾਂਦਾ ਹੈ, ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਤੈਨਾਤ ਕੀਤਾ ਗਿਆ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਤੁਸੀਂ ਇੰਫਰੈਂਸ ਸਰਵਿਸ ਦਾ ਕਲਸਟਰ IP ਲੱਭ ਸਕਦੇ ਹੋ ਅਤੇ ਕਲਸਟਰ ਵਿੱਚ ਸਰਵਿਸ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਅਸਥਾਈ `curl` ਪੌਡ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ਅਸਪਸ਼ਟੀਕਰਨ:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਤ੍ਰੁੱਟੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਉਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਸਮਝਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਂ ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਾਰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਭ੍ਰਮ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->