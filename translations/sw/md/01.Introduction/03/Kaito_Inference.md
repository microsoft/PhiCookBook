<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:57:48+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sw"
}
-->
## Uhakiki na Kaito

[Kaito](https://github.com/Azure/kaito) ni operator inayojihusisha na kuendesha upakiaji wa modeli za AI/ML katika Kubernetes cluster.

Kaito ina tofauti kuu zifuatazo ikilinganishwa na mbinu nyingi za kawaida za kupeleka modeli zinazotegemea miundombinu ya mashine halisi:

- Kusimamia faili za modeli kwa kutumia picha za container. Server ya http hutolewa kwa ajili ya kuita inference kwa kutumia maktaba ya modeli.
- Kuepuka kurekebisha vigezo vya upakiaji ili viendane na vifaa vya GPU kwa kutoa usanidi uliowekwa tayari.
- Kujiendesha kwa kuongeza nodes za GPU kulingana na mahitaji ya modeli.
- Kuhifadhi picha kubwa za modeli katika Microsoft Container Registry (MCR) ya umma ikiwa leseni inaruhusu.

Kutumia Kaito, mchakato wa kuingiza modeli kubwa za AI kwa ajili ya inference ndani ya Kubernetes unakuwa rahisi sana.


## Miundo

Kaito hufuata muundo wa kawaida wa Kubernetes Custom Resource Definition(CRD)/controller. Mtumiaji husimamia rasilimali maalum ya `workspace` inayobainisha mahitaji ya GPU na maelezo ya inference. Controllers za Kaito hufanikisha upakiaji kwa kulinganisha rasilimali maalum ya `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Mchoro huu unaonyesha muhtasari wa miundo ya Kaito. Vipengele vyake vikuu ni:

- **Workspace controller**: Hulinganisha rasilimali maalum ya `workspace`, huunda rasilimali maalum za `machine` (zilibainishwa hapa chini) ili kuanzisha auto provisioning ya node, na huunda mzigo wa inference (`deployment` au `statefulset`) kulingana na usanidi uliowekwa tayari wa modeli.
- **Node provisioner controller**: Controller hii inaitwa *gpu-provisioner* katika [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Inatumia CRD ya `machine` kutoka [Karpenter](https://sigs.k8s.io/karpenter) kuwasiliana na workspace controller. Inajumuisha APIs za Azure Kubernetes Service(AKS) kuongeza nodes mpya za GPU kwenye klasta ya AKS. 
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ni sehemu ya chanzo wazi. Inaweza kubadilishwa na controllers nyingine ikiwa zinaunga mkono APIs za [Karpenter-core](https://sigs.k8s.io/karpenter).

## Ufungaji

Tafadhali angalia mwongozo wa ufungaji [hapa](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Anza Haraka Inference Phi-3
[Sample Code Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Hali ya workspace inaweza kufuatiliwa kwa kuendesha amri ifuatayo. Wakati safu ya WORKSPACEREADY inakuwa `True`, modeli imewekwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Baadaye, mtu anaweza kupata cluster ip ya huduma ya inference na kutumia pod ya muda ya `curl` kujaribu huduma hiyo ndani ya klasta.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Anza Haraka Inference Phi-3 na adapters

Baada ya kufunga Kaito, mtu anaweza kujaribu amri zifuatazo kuanzisha huduma ya inference.

[Sample Code Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Hali ya workspace inaweza kufuatiliwa kwa kuendesha amri ifuatayo. Wakati safu ya WORKSPACEREADY inakuwa `True`, modeli imewekwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Baadaye, mtu anaweza kupata cluster ip ya huduma ya inference na kutumia pod ya muda ya `curl` kujaribu huduma hiyo ndani ya klasta.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Kiondoa lawama**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au kutokamilika. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatubeba uwajibikaji wowote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.