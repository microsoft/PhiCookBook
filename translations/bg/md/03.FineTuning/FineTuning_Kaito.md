<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:43:16+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "bg"
}
-->
## Финна настройка с Kaito 

[Kaito](https://github.com/Azure/kaito) е оператор, който автоматизира разгръщането на AI/ML модели за извеждане в Kubernetes клъстер.

Kaito има следните основни предимства в сравнение с повечето популярни методологии за разгръщане на модели, базирани на виртуални машини:

- Управлява файловете с модели чрез контейнерни образи. Предоставя HTTP сървър за извършване на извеждащи повиквания чрез библиотеката с модели.
- Избягва настройката на параметрите за разгръщане според GPU хардуера, като предлага предварително зададени конфигурации.
- Автоматично осигурява GPU възли според изискванията на модела.
- Разполага големи образи на модели в публичния Microsoft Container Registry (MCR), ако лицензът го позволява.

С помощта на Kaito, процесът на интегриране на големи AI модели за извеждане в Kubernetes е значително опростен.


## Архитектура

Kaito следва класическия дизайн модел на Kubernetes Custom Resource Definition (CRD)/контролер. Потребителят управлява `workspace` персонализиран ресурс, който описва изискванията за GPU и спецификацията за извеждане. Kaito контролерите автоматизират разгръщането чрез синхронизиране на `workspace` персонализирания ресурс.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Архитектура на Kaito" alt="Архитектура на Kaito">
</div>

Горната илюстрация показва общия преглед на архитектурата на Kaito. Основните ѝ компоненти са:

- **Workspace controller**: Синхронизира `workspace` персонализирания ресурс, създава `machine` (обяснено по-долу) персонализирани ресурси за задействане на автоматичното осигуряване на възли и създава извеждащата работна натовареност (`deployment` или `statefulset`) на базата на предварително зададените конфигурации на модела.
- **Node provisioner controller**: Контролерът се нарича *gpu-provisioner* в [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Той използва `machine` CRD, произхождащ от [Karpenter](https://sigs.k8s.io/karpenter), за взаимодействие с workspace controller. Интегрира се с Azure Kubernetes Service (AKS) API-та, за да добавя нови GPU възли към AKS клъстера.
> Забележка: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) е отворен компонент. Може да бъде заменен с други контролери, ако поддържат [Karpenter-core](https://sigs.k8s.io/karpenter) API-та.

## Видео преглед 
[Гледайте демото на Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Инсталация

Моля, прегледайте инструкциите за инсталация [тук](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Бърз старт

След инсталиране на Kaito, можете да опитате следните команди, за да стартирате услуга за финна настройка.

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

Статусът на workspace-а може да се следи с командата по-долу. Когато колоната WORKSPACEREADY стане `True`, моделът е успешно разположен.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

След това можете да намерите IP адреса на услугата за извеждане и да използвате временен `curl` pod, за да тествате крайния пункт на услугата в клъстера.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.