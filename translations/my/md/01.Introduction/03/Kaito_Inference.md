<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-09T20:07:06+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "my"
}
-->
## Kaito ဖြင့် အနုတ်ယူခြင်း

[Kaito](https://github.com/Azure/kaito) သည် Kubernetes cluster အတွင်း AI/ML အနုတ်ယူမှု မော်ဒယ်များကို အလိုအလျောက် တပ်ဆင်ပေးသော operator တစ်ခုဖြစ်သည်။

Kaito သည် virtual machine အခြေခံ အဆောက်အအုံများပေါ်တွင် တည်ဆောက်ထားသော မော်ဒယ် တပ်ဆင်မှုနည်းလမ်းများအများစုနှင့် နှိုင်းယှဉ်လျှင် အောက်ပါ အထူးကွဲပြားချက်များရှိသည်-

- မော်ဒယ်ဖိုင်များကို container image များဖြင့် စီမံခန့်ခွဲသည်။ မော်ဒယ်စာကြည့်တိုက်ကို အသုံးပြု၍ အနုတ်ယူခေါ်ဆိုမှုများ ပြုလုပ်နိုင်ရန် http server တစ်ခု ပံ့ပိုးပေးသည်။
- GPU hardware ကို ကိုက်ညီစေရန် deployment parameter များကို ချိန်ညှိရန် မလိုအပ်ဘဲ ကြိုတင်သတ်မှတ်ထားသော configuration များ ပေးသည်။
- မော်ဒယ်လိုအပ်ချက်အရ GPU node များကို အလိုအလျောက် provision ပြုလုပ်ပေးသည်။
- လိုင်စင်ခွင့်ရှိပါက Microsoft Container Registry (MCR) တွင် ကြီးမားသော မော်ဒယ် image များကို တင်ဆက်ထားနိုင်သည်။

Kaito ကို အသုံးပြုခြင်းဖြင့် Kubernetes တွင် ကြီးမားသော AI အနုတ်ယူမော်ဒယ်များကို တင်သွင်းခြင်းလုပ်ငန်းစဉ်ကို အလွန်လွယ်ကူစေသည်။

## ဖွဲ့စည်းပုံ

Kaito သည် ရိုးရာ Kubernetes Custom Resource Definition(CRD)/controller ဒီဇိုင်းပုံစံကို လိုက်နာသည်။ အသုံးပြုသူသည် GPU လိုအပ်ချက်များနှင့် အနုတ်ယူမှု ဖော်ပြချက်များကို ဖော်ပြထားသော `workspace` custom resource ကို စီမံခန့်ခွဲသည်။ Kaito controller များသည် `workspace` custom resource ကို ပြန်လည်ညှိနှိုင်းခြင်းဖြင့် deployment ကို အလိုအလျောက် ပြုလုပ်ပေးသည်။
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

အထက်ပါ ပုံသည် Kaito ဖွဲ့စည်းပုံ အနှစ်ချုပ်ကို ဖော်ပြထားသည်။ ၎င်း၏ အဓိက အစိတ်အပိုင်းများမှာ-

- **Workspace controller**: `workspace` custom resource ကို ပြန်လည်ညှိနှိုင်းပြီး `machine` (အောက်တွင် ရှင်းပြထားသည်) custom resource များကို ဖန်တီးကာ node auto provisioning ကို စတင်ပေးသည်။ မော်ဒယ် preset configuration များအရ အနုတ်ယူမှု workload (`deployment` သို့မဟုတ် `statefulset`) ကို ဖန်တီးပေးသည်။
- **Node provisioner controller**: controller ၏ အမည်မှာ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) တွင် *gpu-provisioner* ဖြစ်သည်။ ၎င်းသည် [Karpenter](https://sigs.k8s.io/karpenter) မှ ရရှိသော `machine` CRD ကို အသုံးပြုကာ workspace controller နှင့် ဆက်သွယ်သည်။ Azure Kubernetes Service (AKS) API များနှင့် ပေါင်းစည်းကာ AKS cluster တွင် GPU node အသစ်များ ထည့်သွင်းပေးသည်။
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) သည် open source component ဖြစ်သည်။ [Karpenter-core](https://sigs.k8s.io/karpenter) API များကို ထောက်ပံ့သော အခြား controller များဖြင့် အစားထိုးနိုင်သည်။

## တပ်ဆင်ခြင်း

တပ်ဆင်ခြင်း လမ်းညွှန်ကို [ဒီနေရာမှာ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ကြည့်ရှုနိုင်ပါသည်။

## အမြန်စတင်ခြင်း Inference Phi-3
[နမူနာကုဒ် Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

workspace အခြေအနေကို အောက်ပါ command ဖြင့် စစ်ဆေးနိုင်သည်။ WORKSPACEREADY ကော်လံသည် `True` ဖြစ်လာသည်နှင့် မော်ဒယ်ကို အောင်မြင်စွာ တပ်ဆင်ပြီးဖြစ်သည်။

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

နောက်တစ်ဆင့်တွင် အနုတ်ယူမှု ဝန်ဆောင်မှု၏ cluster ip ကို ရှာဖွေပြီး cluster အတွင်းရှိ ယာယီ `curl` pod ကို အသုံးပြုကာ ဝန်ဆောင်မှု endpoint ကို စမ်းသပ်နိုင်သည်။

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## အမြန်စတင်ခြင်း Inference Phi-3 နှင့် adapters

Kaito ကို တပ်ဆင်ပြီးနောက် အောက်ပါ command များကို အသုံးပြုကာ အနုတ်ယူမှု ဝန်ဆောင်မှုကို စတင်နိုင်သည်။

[နမူနာကုဒ် Inference Phi-3 နှင့် Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

workspace အခြေအနေကို အောက်ပါ command ဖြင့် စစ်ဆေးနိုင်သည်။ WORKSPACEREADY ကော်လံသည် `True` ဖြစ်လာသည်နှင့် မော်ဒယ်ကို အောင်မြင်စွာ တပ်ဆင်ပြီးဖြစ်သည်။

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

နောက်တစ်ဆင့်တွင် အနုတ်ယူမှု ဝန်ဆောင်မှု၏ cluster ip ကို ရှာဖွေပြီး cluster အတွင်းရှိ ယာယီ `curl` pod ကို အသုံးပြုကာ ဝန်ဆောင်မှု endpoint ကို စမ်းသပ်နိုင်သည်။

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။