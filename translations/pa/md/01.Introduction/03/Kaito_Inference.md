<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:49:36+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pa"
}
-->
## Kaito ਨਾਲ ਇਨਫਰੰਸ

[Kaito](https://github.com/Azure/kaito) ਇੱਕ ਓਪਰੇਟਰ ਹੈ ਜੋ Kubernetes ਕਲੱਸਟਰ ਵਿੱਚ AI/ML ਇਨਫਰੰਸ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।

Kaito ਦੇ ਕੁਝ ਮੁੱਖ ਫਰਕ ਹਨ ਜੋ ਵਿਰਚੁਅਲ ਮਸ਼ੀਨ ਇੰਫਰਾਸਟਰੱਕਚਰਾਂ 'ਤੇ ਬਣੇ ਜ਼ਿਆਦਾਤਰ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਤਰੀਕਿਆਂ ਨਾਲੋਂ ਵੱਖਰੇ ਹਨ:

- ਮਾਡਲ ਫਾਈਲਾਂ ਨੂੰ ਕੰਟੇਨਰ ਇਮੇਜਾਂ ਰਾਹੀਂ ਮੈਨੇਜ ਕਰਨਾ। ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਫਰੰਸ ਕਾਲ ਕਰਨ ਲਈ ਇੱਕ HTTP ਸਰਵਰ ਦਿੱਤਾ ਗਿਆ ਹੈ।
- GPU ਹਾਰਡਵੇਅਰ ਲਈ ਡਿਪਲੋਇਮੈਂਟ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਟਿਊਨ ਕਰਨ ਤੋਂ ਬਚਾਉਂਦਾ ਹੈ, ਪ੍ਰੀਸੈੱਟ ਕਨਫਿਗਰੇਸ਼ਨਾਂ ਦੇ ਕੇ।
- ਮਾਡਲ ਦੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ GPU ਨੋਡਾਂ ਨੂੰ ਆਟੋ-ਪ੍ਰੋਵਾਈਜ਼ਨ ਕਰਦਾ ਹੈ।
- ਜੇ ਲਾਇਸੈਂਸ ਦੀ ਆਗਿਆ ਹੋਵੇ ਤਾਂ ਵੱਡੇ ਮਾਡਲ ਇਮੇਜਾਂ ਨੂੰ ਪਬਲਿਕ Microsoft Container Registry (MCR) ਵਿੱਚ ਹੋਸਟ ਕਰਦਾ ਹੈ।

Kaito ਦੀ ਵਰਤੋਂ ਨਾਲ, Kubernetes ਵਿੱਚ ਵੱਡੇ AI ਇਨਫਰੰਸ ਮਾਡਲਾਂ ਨੂੰ ਸ਼ੁਰੂ ਕਰਨ ਦਾ ਕੰਮ ਕਾਫੀ ਸਧਾਰਨ ਹੋ ਜਾਂਦਾ ਹੈ।


## ਆਰਕੀਟੈਕਚਰ

Kaito ਕਲਾਸਿਕ Kubernetes Custom Resource Definition (CRD)/controller ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਨੂੰ ਫਾਲੋ ਕਰਦਾ ਹੈ। ਯੂਜ਼ਰ ਇੱਕ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਮੈਨੇਜ ਕਰਦਾ ਹੈ ਜੋ GPU ਦੀਆਂ ਲੋੜਾਂ ਅਤੇ ਇਨਫਰੰਸ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਵੇਰਵਾ ਦਿੰਦਾ ਹੈ। Kaito ਕੰਟਰੋਲਰ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰੀਕਨਸਾਈਲ ਕਰਕੇ ਡਿਪਲੋਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦੇ ਹਨ।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ Kaito ਆਰਕੀਟੈਕਚਰ ਦਾ ਓਵਰਵਿਊ ਦਿਖਾਉਂਦੀ ਹੈ। ਇਸਦੇ ਮੁੱਖ ਹਿੱਸੇ ਹਨ:

- **Workspace controller**: ਇਹ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰੀਕਨਸਾਈਲ ਕਰਦਾ ਹੈ, ਨੋਡ ਆਟੋ-ਪ੍ਰੋਵਾਈਜ਼ਨਿੰਗ ਲਈ `machine` (ਹੇਠਾਂ ਵਿਆਖਿਆ ਕੀਤੀ ਗਈ) ਕਸਟਮ ਰਿਸੋਰਸ ਬਣਾਉਂਦਾ ਹੈ, ਅਤੇ ਮਾਡਲ ਦੀਆਂ ਪ੍ਰੀਸੈੱਟ ਕਨਫਿਗਰੇਸ਼ਨਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਇਨਫਰੰਸ ਵਰਕਲੋਡ (`deployment` ਜਾਂ `statefulset`) ਬਣਾਉਂਦਾ ਹੈ।
- **Node provisioner controller**: ਇਸ ਕੰਟਰੋਲਰ ਦਾ ਨਾਮ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ਵਿੱਚ *gpu-provisioner* ਹੈ। ਇਹ `machine` CRD ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ [Karpenter](https://sigs.k8s.io/karpenter) ਤੋਂ ਆਉਂਦਾ ਹੈ, ਅਤੇ workspace controller ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਦਾ ਹੈ। ਇਹ Azure Kubernetes Service (AKS) APIs ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਕੇ AKS ਕਲੱਸਟਰ ਵਿੱਚ ਨਵੇਂ GPU ਨੋਡ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ।  
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਕੰਪੋਨੈਂਟ ਹੈ। ਜੇ ਹੋਰ ਕੰਟਰੋਲਰ [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ਨੂੰ ਸਪੋਰਟ ਕਰਦੇ ਹਨ ਤਾਂ ਇਹਨਾਂ ਨਾਲ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਇੰਸਟਾਲੇਸ਼ਨ

ਕਿਰਪਾ ਕਰਕੇ ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਮਦਦ ਲਈ [ਇੱਥੇ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ਵੇਖੋ।

## ਫਾਸਟ ਸਟਾਰਟ ਇਨਫਰੰਸ Phi-3
[ਸੈਂਪਲ ਕੋਡ ਇਨਫਰੰਸ Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ਵਰਕਸਪੇਸ ਦੀ ਸਥਿਤੀ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾ ਕੇ ਟ੍ਰੈਕ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਜਦੋਂ WORKSPACEREADY ਕਾਲਮ `True` ਹੋ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਡਿਪਲੋਇਡ ਹੋ ਚੁੱਕਾ ਹੁੰਦਾ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਇਨਫਰੰਸ ਸਰਵਿਸ ਦਾ ਕਲੱਸਟਰ IP ਲੱਭਿਆ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਕਲੱਸਟਰ ਵਿੱਚ ਸਰਵਿਸ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਅਸਥਾਈ `curl` ਪੋਡ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## ਫਾਸਟ ਸਟਾਰਟ ਇਨਫਰੰਸ Phi-3 ਐਡਾਪਟਰਾਂ ਨਾਲ

Kaito ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਇਨਫਰੰਸ ਸਰਵਿਸ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

[ਸੈਂਪਲ ਕੋਡ ਇਨਫਰੰਸ Phi-3 ਐਡਾਪਟਰਾਂ ਨਾਲ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ਵਰਕਸਪੇਸ ਦੀ ਸਥਿਤੀ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾ ਕੇ ਟ੍ਰੈਕ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਜਦੋਂ WORKSPACEREADY ਕਾਲਮ `True` ਹੋ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਡਿਪਲੋਇਡ ਹੋ ਚੁੱਕਾ ਹੁੰਦਾ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਇਨਫਰੰਸ ਸਰਵਿਸ ਦਾ ਕਲੱਸਟਰ IP ਲੱਭਿਆ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਕਲੱਸਟਰ ਵਿੱਚ ਸਰਵਿਸ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਅਸਥਾਈ `curl` ਪੋਡ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।