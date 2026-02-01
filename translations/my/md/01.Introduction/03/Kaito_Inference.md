## Kaito ဖြင့် အနုတ်ထုတ်ခြင်း

[Kaito](https://github.com/Azure/kaito) သည် Kubernetes ကလပ်စတာတွင် AI/ML အနုတ်ထုတ်မော်ဒယ်များကို အလိုအလျောက်ဖြန့်ဝေသည့် operator တစ်ခုဖြစ်သည်။

Kaito တွင် virtual machine အခြေပြု အထောက်အထားများအထက် တည်ဆောက်ထားသော mainstream model deployment နည်းလမ်းများနှင့်နှိုင်းယှဉ်သောအခါ အောက်ပါအချက်များတွင် အဓိကကွာခြားချက်များရှိသည်-

- မော်ဒယ်ဖိုင်များကို container images အသုံးပြု၍ စီမံခန့်ခွဲသည်။ http စာကြောင်းမောင်းဆာဘာ ရရှိပြီး မော်ဒယ်စာကြောင်းစာကြည့်တိုက်မှ inferenceခေါ်ဆိုမှုများကို လုပ်ဆောင်သည်။
- GPU hardware နှင့် ကိုက်ညီစေရေး deployment parameters ကို ချိန်ညှိရန် မလိုအပ်ပဲ မျှော်မှန်းထားသော configuration များကို ဖြည့်စွက်ပေးသည်။
- မော်ဒယ်လိုအပ်ချက်အရ GPU node များကို အလိုအလျောက် ပံ့ပိုးပေးသည်။
- မူပိုင်ခွင့် ကျင့်ကြံခွင့်ရှိပါက Microsoft Container Registry (MCR) တွင် ကြီးမားသော မော်ဒယ် image များကို တင်ဆက်ပေးသည်။

Kaito ကို အသုံးပြုခြင်းဖြင့် Kubernetes တွင် ကြီးမားသော AI အနုတ်ထုတ်မော်ဒယ်များကို အလွန်လွယ်ကူစွာ ကောင်းမွန်စွာ တင်သွင်းနိုင်သည်။


## ဝိဇ္ဇာတည်ဆောက်ပုံ

Kaito သည် classic Kubernetes Custom Resource Definition (CRD) / controller ဒီဇိုင်းပုံစံကို လိုက်နာသည်။ အသုံးပြုသူသည် GPU လိုအပ်ချက်များနှင့် အနုတ်ထုတ် ဆွဲကြောင်းကို ဖော်ပြသည့် `workspace` custom resource ကို စီမံခန့်ခွဲသည်။ Kaito controller များသည် `workspace` custom resource ကို အလိုအလျောက်စစ်ဆေးပြီး deployment ကို အလိုအလျောက်ပြုလုပ်ပေးသည်။

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

အထက်တွင် ပြထားသော ပုံသည် Kaito architecture အနှစ်ချုပ်ဖြစ်သည်။ ၎င်း၏ အဓိကအစိတ်အပိုင်းများမှာ-

- **Workspace controller**: `workspace` custom resource ကို စစ်ဆေးပြီး node auto provisioning ကို စတင်ရန် `machine` (အောက်တွင်ရှင်းပြထားသည်) custom resources များကို ဖန်တီးပြီး၊ မော်ဒယ်အခြေခံပျော်ပြီ configuration များနှင့်အညီ အနုတ်ထုတ်လုပ်ငန်း (`deployment` သို့မဟုတ် `statefulset`) ကို တည်ဆောက်ပေးသည်။
- **Node provisioner controller**: controller ၏နာမည်မှာ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) တွင် *gpu-provisioner* ဖြစ်သည်။ ၎င်းသည် Karpenter မှ ရရှိသော `machine` CRD ကို အသုံးပြု၍ workspace controller နှင့် ဆက်သွယ်သည်။ Azure Kubernetes Service (AKS) API များနှင့် ပေါင်းစည်းကာ AKS ကလပ်စတာတွင် GPU node အသစ်များ ထည့်သွင်းပေးသည်။
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) သည် ဖွင့်ဆိုဒ်အစိတ်အပိုင်းဖြစ်သည်။ [Karpenter-core](https://sigs.k8s.io/karpenter) API များကို ထောက်ပံ့ပါက အခြား controller များဖြင့် အစားထိုးနိုင်သည်။


## ထည့်သွင်းခြင်း

ထည့်သွင်းနည်းလမ်းညွှန်ကို [ဒီမှာ](https://github.com/Azure/kaito/blob/main/docs/installation.md) စစ်ဆေးနိုင်ပါသည်။

## အမြန်စတင်၍ Inference Phi-3  
[နမူနာ ကုဒ် Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ထွက်ရှိမည့် ACR လမ်းကြောင်းကို ချိန်ညှိခြင်း
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

workspace အခြေအနေနှင့် စောင့်ကြည့်ရန်အတွက် အောက်ပါ command ကို ပြေးရန်ဖြစ်သည်။ WORKSPACEREADY ကော်လံသည် `True` ဖြစ်လာသည့်အခါ မော်ဒယ်အားအောင်မြင်စွာ ဖြန့်ချိပြီးဖြစ်ပါသည်။

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

ထို့နောက်အနုတ်ထုတ် ဝန်ဆောင်မှု၏ cluster ip ကို ရှာဖွေပြီး တာဝန်ထမ်း `curl` pod ဖြင့် cluster အတွင်း ဝန်ဆောင်မှု endpoint ကို စမ်းသပ်နိုင်ပါသည်။

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## အမြန်စတင်၍ Inference Phi-3 ကို adapters ဖြင့်

Kaito ကို ထည့်သွင်းပြီးနောက် အောက်ပါ command များကို အသုံးပြု၍ inference ဝန်ဆောင်မှုကို စတင်နိုင်သည်။

[နမူနာ ကုဒ် Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # သင့်တင်မှု Output ACR လမ်းကြောင်း
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

workspace အခြေအနေကို စောင့်ကြည့်ရန် အောက်ပါ command ကို ပြေးနိုင်သည်။ WORKSPACEREADY ကော်လံသည် `True` ဖြစ်လာသည်နှင့် မော်ဒယ်အားအောင်မြင်စွာ ဖြန့်ချိပြီးဖြစ်သည်။

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

ထို့နောက် inference ဝန်ဆောင်မှု cluster ip ကို ရှာဖွေ၍ တာဝန်ထမ်း `curl` pod ဖြင့် cluster အတွင်း ဝန်ဆောင်မှု endpoint ကို စမ်းသပ်နိုင်ပါသည်။

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းတရား ထုတ်ပြန်ချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) မှတစ်ဆင့် ဘာသာပြန်ထားခြင်းဖြစ်သည်။ ကျွန်ုပ်တို့သည် တိကျမှုကို ကြိုးပမ်းပါသည်၊ သို့သော် စက်ရုပ်ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုကြပါရန် အဓိကထားပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အရင်းအမြစ်လို့ သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် လူ့ဘာသာပြန်သူ ပညာရှင်မှ ပြန်ဆိုခြင်း အကြံပြုပါသည်။ ဤဘာသာပြန်မှုအသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားဖွင့်မြင်မှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->