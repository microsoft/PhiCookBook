<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T09:19:54+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sw"
}
-->
## Uhakiki na Kaito

[Kaito](https://github.com/Azure/kaito) ni operatori inayojumuisha utoaji wa mfano wa AI/ML katika klasta la Kubernetes kwa njia ya kiotomatiki.

Kaito ina utofauti muhimu ufuatao ukiwa dhidi ya mbinu nyingi za kawaida za utoaji wa mifano zilizojengwa juu ya miundombinu ya mashine pepe:

- Simamia faili za mfano kwa kutumia picha za kontena. Server ya http hutolewa kwa ajili ya kufanikisha simu za uhakiki kwa kutumia maktaba ya mfano.
- Epuka kurekebisha vigezo vya utoaji kufaa vifaa vya GPU kwa kutoa usanidi uliowekwa tayari.
- Kujipatia kwa otomatiki node za GPU kulingana na mahitaji ya mfano.
- Kuhifadhi picha kubwa za mfano katika Microsoft Container Registry (MCR) ya umma ikiwa leseni inaruhusu.

Kutumia Kaito, mtiririko wa kazi wa kuanzisha mifano mikubwa ya uhakiki ya AI katika Kubernetes umefanywa kuwa rahisi sana.

## Mimarishwa

Kaito inafuata muundo wa kawaida wa Kubernetes Custom Resource Definition(CRD)/dhibiti. Mtumiaji anasimamia rasilimali maalum ya `workspace` inayobainisha mahitaji ya GPU na maalum ya uhakiki. Dhibiti wa Kaito atajumuisha utoaji kwa kurekebisha rasilimali maalum ya `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Mchoro ulio juu unaonyesha muhtasari wa miaradhisho ya Kaito. Vipengele vikubwa ni:

- **Dhibiti wa Workspace**: Anarekebisha rasilimali maalum ya `workspace`, huunda rasilimali maalum `machine` (ielezwayo chini) ili kuanzisha ujipaji wa node kiotomatiki, na huunda mzigo wa uhakiki (`deployment` au `statefulset`) kulingana na usanidi uliowekwa wa mfano.
- **Dhibiti wa ujipaji node**: Jina la dhibiti ni *gpu-provisioner* katika [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Inatumia CRD ya `machine` inayotokana na [Karpenter](https://sigs.k8s.io/karpenter) kuingiliana na dhibiti wa workspace. Inajumuika na APIs za Azure Kubernetes Service(AKS) kuongeza node mpya za GPU kwenye klasta ya AKS.
> Kumbuka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ni sehemu ya chanzo huria. Inaweza kubadilishwa na dhibiti wengine ikiwa wanaunga mkono APIs za [Karpenter-core](https://sigs.k8s.io/karpenter).

## Usanidi

Tafadhali angalia mwongozo wa usanikishaji [hapa](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mwanzo wa Haraka Uhakiki Phi-3  
[Nambari ya Mfano Uhakiki Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Kuboresha Njia ya Mzazi wa Toa ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```
  
Hali ya workspace inaweza kufuatiliwa kwa kuendesha amri ifuatayo. Nikiwa safu ya WORKSPACEREADY inakuwa `True`, mfano umeanzishwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```
  
Kisha, mtu anaweza kupata IP ya huduma ya uhakiki ya klasta na kutumia pod ya muda `curl` kufanya mtihani wa kiungo cha huduma ndani ya klasta.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```
  
## Mwanzo wa Haraka Uhakiki Phi-3 na viongeza

Baada ya kusanidi Kaito, mtu anaweza kujaribu amri zifuatazo kuanzisha huduma ya uhakiki.

[Nambari ya Mfano Uhakiki Phi-3 na Viongeza](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Kurekebisha Njia ya ACR ya Matokeo
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```
  
Hali ya workspace inaweza kufuatiliwa kwa kuendesha amri ifuatayo. Nikiwa safu ya WORKSPACEREADY inakuwa `True`, mfano umeanzishwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```
  
Kisha, mtu anaweza kupata IP ya huduma ya uhakiki ya klasta na kutumia pod ya muda `curl` kufanya mtihani wa kiungo cha huduma ndani ya klasta.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kauli ya Kukataa**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kufanikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Nyaraka ya asili katika lugha yake ya mzazi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na watu inashauriwa. Hatubeba jukumu kwa kutoelewana au tafsiri mbaya inayotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->