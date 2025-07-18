<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:24:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "sw"
}
-->
## Kurekebisha kwa Undani na Kaito

[Kaito](https://github.com/Azure/kaito) ni operatori inayot automatisha uanzishaji wa modeli za AI/ML katika klasta ya Kubernetes.

Kaito ina tofauti kuu zifuatazo ikilinganishwa na mbinu nyingi za kawaida za uanzishaji wa modeli zinazotegemea miundombinu ya mashine za virtuali:

- Kusimamia faili za modeli kwa kutumia picha za kontena. Seva ya http hutolewa kwa ajili ya kufanya miito ya inference kwa kutumia maktaba ya modeli.
- Kuepuka kurekebisha vigezo vya uanzishaji ili kuendana na vifaa vya GPU kwa kutoa mipangilio iliyowekwa awali.
- Kujitengenezea nodi za GPU kiotomatiki kulingana na mahitaji ya modeli.
- Kuhifadhi picha kubwa za modeli katika Microsoft Container Registry (MCR) ya umma ikiwa leseni inaruhusu.

Kwa kutumia Kaito, mchakato wa kuingiza modeli kubwa za AI katika Kubernetes umefanywa rahisi sana.

## Mimarisho

Kaito hufuata muundo wa kawaida wa Kubernetes Custom Resource Definition (CRD)/controller. Mtumiaji husimamia rasilimali maalum ya `workspace` inayobainisha mahitaji ya GPU na maelezo ya inference. Kaito controllers hufanya uanzishaji kiotomatiki kwa kusawazisha rasilimali maalum ya `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Mchoro hapo juu unaonyesha muhtasari wa usanifu wa Kaito. Sehemu zake kuu ni:

- **Workspace controller**: Husawazisha rasilimali maalum ya `workspace`, huunda rasilimali maalum za `machine` (zilizoelezwa hapa chini) ili kuanzisha utoaji wa nodi kiotomatiki, na huunda mzigo wa inference (`deployment` au `statefulset`) kulingana na mipangilio ya modeli iliyowekwa awali.
- **Node provisioner controller**: Jina la controller ni *gpu-provisioner* katika [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Inatumia CRD ya `machine` inayotokana na [Karpenter](https://sigs.k8s.io/karpenter) kuwasiliana na workspace controller. Inajumuika na APIs za Azure Kubernetes Service (AKS) kuongeza nodi mpya za GPU kwenye klasta ya AKS.  
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ni sehemu ya chanzo huria. Inaweza kubadilishwa na controllers wengine ikiwa wanaunga mkono APIs za [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video ya Muhtasari  
[Tazama Onyesho la Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Ufungaji

Tafadhali angalia mwongozo wa ufungaji [hapa](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Anza Haraka

Baada ya kufunga Kaito, mtu anaweza kujaribu amri zifuatazo kuanzisha huduma ya kurekebisha kwa undani.

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

Hali ya workspace inaweza kufuatiliwa kwa kuendesha amri ifuatayo. Wakati safu ya WORKSPACEREADY inakuwa `True`, modeli imesakinishwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Baadaye, mtu anaweza kupata IP ya huduma ya inference ya klasta na kutumia pod ya muda ya `curl` kujaribu kiunganishi cha huduma ndani ya klasta.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.