<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:21:05+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "pa"
}
-->
## ਕਾਈਟੋ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ

[Kaito](https://github.com/Azure/kaito) ਇੱਕ ਓਪਰੇਟਰ ਹੈ ਜੋ Kubernetes ਕਲੱਸਟਰ ਵਿੱਚ AI/ML ਇਨਫਰੈਂਸ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।

ਕਾਈਟੋ ਦੇ ਕੁਝ ਮੁੱਖ ਫਰਕ ਹਨ ਜੋ ਵਿਰਚੁਅਲ ਮਸ਼ੀਨ ਇੰਫਰਾਸਟਰੱਕਚਰਾਂ 'ਤੇ ਬਣੇ ਜ਼ਿਆਦਾਤਰ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਤਰੀਕਿਆਂ ਨਾਲੋਂ ਵੱਖਰੇ ਹਨ:

- ਮਾਡਲ ਫਾਈਲਾਂ ਨੂੰ ਕੰਟੇਨਰ ਇਮੇਜਾਂ ਰਾਹੀਂ ਮੈਨੇਜ ਕਰਨਾ। ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਫਰੈਂਸ ਕਾਲ ਕਰਨ ਲਈ ਇੱਕ HTTP ਸਰਵਰ ਦਿੱਤਾ ਗਿਆ ਹੈ।
- GPU ਹਾਰਡਵੇਅਰ ਦੇ ਅਨੁਕੂਲ ਡਿਪਲੋਇਮੈਂਟ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਟਿਊਨ ਕਰਨ ਤੋਂ ਬਚਣਾ, ਪ੍ਰੀਸੈੱਟ ਕਨਫਿਗਰੇਸ਼ਨਾਂ ਦੇ ਨਾਲ।
- ਮਾਡਲ ਦੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ GPU ਨੋਡਾਂ ਨੂੰ ਆਟੋ-ਪ੍ਰੋਵਾਈਜ਼ਨ ਕਰਨਾ।
- ਜੇ ਲਾਇਸੈਂਸ ਦੀ ਆਗਿਆ ਹੋਵੇ ਤਾਂ ਵੱਡੇ ਮਾਡਲ ਇਮੇਜਾਂ ਨੂੰ ਪਬਲਿਕ Microsoft Container Registry (MCR) ਵਿੱਚ ਹੋਸਟ ਕਰਨਾ।

ਕਾਈਟੋ ਦੀ ਵਰਤੋਂ ਨਾਲ, Kubernetes ਵਿੱਚ ਵੱਡੇ AI ਇਨਫਰੈਂਸ ਮਾਡਲਾਂ ਨੂੰ ਸ਼ੁਰੂ ਕਰਨ ਦਾ ਕੰਮ ਕਾਫੀ ਸਧਾਰਨ ਹੋ ਜਾਂਦਾ ਹੈ।


## ਆਰਕੀਟੈਕਚਰ

ਕਾਈਟੋ ਕਲਾਸਿਕ Kubernetes Custom Resource Definition (CRD)/controller ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ। ਯੂਜ਼ਰ ਇੱਕ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਮੈਨੇਜ ਕਰਦਾ ਹੈ ਜੋ GPU ਦੀਆਂ ਲੋੜਾਂ ਅਤੇ ਇਨਫਰੈਂਸ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਵੇਰਵਾ ਦਿੰਦਾ ਹੈ। ਕਾਈਟੋ ਕੰਟਰੋਲਰ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰੀਕਨਸਾਈਲ ਕਰਕੇ ਡਿਪਲੋਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦੇ ਹਨ।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ ਕਾਈਟੋ ਆਰਕੀਟੈਕਚਰ ਦਾ ਝਲਕ ਪੇਸ਼ ਕਰਦੀ ਹੈ। ਇਸਦੇ ਮੁੱਖ ਹਿੱਸੇ ਹਨ:

- **Workspace controller**: ਇਹ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰੀਕਨਸਾਈਲ ਕਰਦਾ ਹੈ, ਨੋਡ ਆਟੋ-ਪ੍ਰੋਵਾਈਜ਼ਨਿੰਗ ਲਈ `machine` (ਹੇਠਾਂ ਵਿਆਖਿਆ ਕੀਤੀ ਗਈ) ਕਸਟਮ ਰਿਸੋਰਸ ਬਣਾਉਂਦਾ ਹੈ, ਅਤੇ ਮਾਡਲ ਦੀਆਂ ਪ੍ਰੀਸੈੱਟ ਕਨਫਿਗਰੇਸ਼ਨਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਇਨਫਰੈਂਸ ਵਰਕਲੋਡ (`deployment` ਜਾਂ `statefulset`) ਬਣਾਉਂਦਾ ਹੈ।
- **Node provisioner controller**: ਇਸ ਕੰਟਰੋਲਰ ਦਾ ਨਾਮ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ਵਿੱਚ *gpu-provisioner* ਹੈ। ਇਹ `machine` CRD ਜੋ [Karpenter](https://sigs.k8s.io/karpenter) ਤੋਂ ਆਇਆ ਹੈ, ਨੂੰ ਵਰਤ ਕੇ workspace controller ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਦਾ ਹੈ। ਇਹ Azure Kubernetes Service (AKS) APIs ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਕੇ AKS ਕਲੱਸਟਰ ਵਿੱਚ ਨਵੇਂ GPU ਨੋਡ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ।  
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਕੰਪੋਨੈਂਟ ਹੈ। ਜੇ ਹੋਰ ਕੰਟਰੋਲਰ [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ਨੂੰ ਸਪੋਰਟ ਕਰਦੇ ਹਨ ਤਾਂ ਇਹਨਾਂ ਨਾਲ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਓਵਰਵਿਊ ਵੀਡੀਓ  
[Kaito ਡੈਮੋ ਵੇਖੋ](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## ਇੰਸਟਾਲੇਸ਼ਨ

ਕਿਰਪਾ ਕਰਕੇ ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਮਦਦ ਲਈ [ਇੱਥੇ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ਵੇਖੋ।

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ

ਕਾਈਟੋ ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਫਾਈਨ-ਟਿਊਨਿੰਗ ਸੇਵਾ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

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

ਵਰਕਸਪੇਸ ਦੀ ਸਥਿਤੀ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਚਲਾ ਕੇ ਟਰੈਕ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਜਦੋਂ WORKSPACEREADY ਕਾਲਮ `True` ਹੋ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਡਿਪਲੋਇਡ ਹੋ ਚੁੱਕਾ ਹੁੰਦਾ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਇਨਫਰੈਂਸ ਸੇਵਾ ਦਾ ਕਲੱਸਟਰ IP ਲੱਭ ਕੇ ਕਲੱਸਟਰ ਵਿੱਚ ਟੈਸਟ ਕਰਨ ਲਈ ਇੱਕ ਅਸਥਾਈ `curl` ਪੋਡ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।