<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:42:28+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "sw"
}
-->
## Kurekebisha kwa Kaito

[Kaito](https://github.com/Azure/kaito) ni operator inayotoa utaratibu wa kuendesha modeli za AI/ML kwenye Kubernetes cluster.

Kaito ina tofauti kuu zifuatazo ikilinganishwa na mbinu nyingi za kawaida za kupeleka modeli zinazotegemea miundombinu ya virtual machine:

- Kusimamia faili za modeli kwa kutumia picha za container. Server ya http hutolewa kwa ajili ya kuita inference kwa kutumia maktaba ya modeli.
- Kuepuka kubadilisha vigezo vya deployment ili kuendana na vifaa vya GPU kwa kutoa mipangilio ya awali.
- Kujipangia node za GPU kiotomatiki kulingana na mahitaji ya modeli.
- Kuhifadhi picha kubwa za modeli katika Microsoft Container Registry (MCR) ya umma ikiwa leseni inaruhusu.

Kutumia Kaito, mchakato wa kuingiza modeli kubwa za AI kwenye Kubernetes umefanywa rahisi sana.

## Mimarisho

Kaito hufuata muundo wa kawaida wa Kubernetes Custom Resource Definition (CRD)/controller. Mtumiaji husimamia rasilimali maalum ya `workspace` inayobainisha mahitaji ya GPU na maelezo ya inference. Kaito controllers hufanya deployment kiotomatiki kwa kusawazisha rasilimali maalum ya `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Mchoro huu unaonyesha muhtasari wa miundombinu ya Kaito. Vipengele vikuu ni:

- **Workspace controller**: Husaidia kusawazisha rasilimali maalum ya `workspace`, kuunda rasilimali maalum za `machine` (zitakazobainishwa baadaye) ili kuanzisha upangaji wa node kiotomatiki, na kuunda mzigo wa inference (`deployment` au `statefulset`) kulingana na mipangilio ya awali ya modeli.
- **Node provisioner controller**: Jina la controller ni *gpu-provisioner* katika [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Inatumia CRD ya `machine` kutoka [Karpenter](https://sigs.k8s.io/karpenter) kuwasiliana na workspace controller. Inashirikiana na API za Azure Kubernetes Service (AKS) kuongeza node mpya za GPU kwenye cluster ya AKS.
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ni sehemu ya chanzo huria. Inaweza kubadilishwa na controllers nyingine ikiwa zinaunga mkono API za [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video ya Muhtasari
[Tazama Demo ya Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Usanidi

Tafadhali angalia mwongozo wa usakinishaji [hapa](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Anza Haraka

Baada ya kusanidi Kaito, mtu anaweza kujaribu amri zifuatazo kuanzisha huduma ya kurekebisha modeli.

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

Hali ya workspace inaweza kufuatiliwa kwa kutumia amri ifuatayo. Wakati safu ya WORKSPACEREADY inakuwa `True`, modeli imesakinishwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Baadaye, mtu anaweza kupata cluster ip ya huduma ya inference na kutumia pod ya muda ya `curl` kujaribu endpoint ya huduma ndani ya cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Kiondoa lawama**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubeba uwajibikaji wowote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.