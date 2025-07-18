<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:25:39+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "sr"
}
-->
## Фино подешавање са Kaitom

[Kaito](https://github.com/Azure/kaito) је оператор који аутоматизује распоређивање AI/ML inference модела у Kubernetes кластеру.

Kaito има следеће кључне разлике у односу на већину уобичајених метода за распоређивање модела базираних на виртуелним машинама:

- Управљање моделским фајловима помоћу контејнер слика. Пружа HTTP сервер за извођење inference позива користећи библиотеку модела.
- Избегава подешавање параметара распоређивања у складу са GPU хардвером пружајући унапред дефинисане конфигурације.
- Аутоматско обезбеђивање GPU нодова у складу са захтевима модела.
- Хостовање великих слика модела у јавном Microsoft Container Registry (MCR) ако лиценца то дозвољава.

Коришћењем Kaitoa, процес увођења великих AI inference модела у Kubernetes је знатно поједностављен.

## Архитектура

Kaito прати класичан Kubernetes Custom Resource Definition (CRD)/controller дизајн образац. Корисник управља `workspace` custom ресурсом који описује захтеве за GPU и спецификацију inference-а. Kaito контролери аутоматизују распоређивање тако што усаглашавају `workspace` custom ресурс.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Горња слика приказује преглед архитектуре Kaitoa. Главне компоненте су:

- **Workspace controller**: Усаглашава `workspace` custom ресурс, креира `machine` (објашњено у наставку) custom ресурсе за покретање аутоматског обезбеђивања нодова и креира inference workload (`deployment` или `statefulset`) на основу унапред дефинисаних конфигурација модела.
- **Node provisioner controller**: Контролер се зове *gpu-provisioner* у [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Користи `machine` CRD који потиче из [Karpenter](https://sigs.k8s.io/karpenter) за интеракцију са workspace контролером. Интегрише се са Azure Kubernetes Service (AKS) API-јима ради додавања нових GPU нодова у AKS кластер.
> Напомена: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) је open source компонента. Може се заменити другим контролерима ако подржавају [Karpenter-core](https://sigs.k8s.io/karpenter) API-је.

## Преглед видео снимка  
[Погледајте Kaito демо](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Инсталација

Молимо проверите упутство за инсталацију [овде](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Брзи почетак

Након инсталације Kaitoa, може се покушати са следећим командама за покретање fine-tuning сервиса.

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

Статус workspace-а може се пратити покретањем следеће команде. Када колона WORKSPACEREADY постане `True`, модел је успешно распоређен.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Затим, може се пронаћи cluster IP inference сервиса и користити привремени `curl` под за тестирање сервисне тачке у кластеру.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Одрицање одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.