<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:53:31+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "bg"
}
-->
## Извеждане с Kaito

[Kaito](https://github.com/Azure/kaito) е оператор, който автоматизира разгръщането на AI/ML модели за извеждане в Kubernetes клъстер.

Kaito има следните ключови предимства в сравнение с повечето основни методологии за разгръщане на модели, базирани на виртуални машини:

- Управлява файловете на модела чрез контейнерни образи. Предоставя HTTP сървър за извършване на извеждащи заявки чрез библиотеката на модела.
- Избягва настройването на параметрите за разгръщане според GPU хардуера, като предлага предварително зададени конфигурации.
- Автоматично осигурява GPU възли според изискванията на модела.
- Хоства големи образи на модели в публичния Microsoft Container Registry (MCR), ако лицензът го позволява.

С помощта на Kaito, процесът на интегриране на големи AI модели за извеждане в Kubernetes е значително опростен.

## Архитектура

Kaito следва класическия дизайн на Kubernetes Custom Resource Definition (CRD)/controller. Потребителят управлява персонализиран ресурс `workspace`, който описва изискванията за GPU и спецификацията за извеждане. Контролерите на Kaito автоматизират разгръщането чрез синхронизиране на персонализирания ресурс `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Горната илюстрация представя общия преглед на архитектурата на Kaito. Основните му компоненти са:

- **Workspace controller**: Синхронизира персонализирания ресурс `workspace`, създава персонализирани ресурси `machine` (описани по-долу), за да задейства автоматичното осигуряване на възли, и създава извеждащата работна натовареност (`deployment` или `statefulset`) според предварително зададените конфигурации на модела.
- **Node provisioner controller**: Контролерът се нарича *gpu-provisioner* в [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Той използва `machine` CRD, произхождащ от [Karpenter](https://sigs.k8s.io/karpenter), за взаимодействие с workspace контролера. Интегрира се с Azure Kubernetes Service (AKS) API, за да добавя нови GPU възли към AKS клъстера.
> Забележка: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) е отворен компонент с отворен код. Може да бъде заменен с други контролери, ако поддържат [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Инсталация

Моля, вижте указанията за инсталация [тук](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Бърз старт за извеждане Phi-3
[Примерен код за извеждане Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Статусът на workspace може да се проследи чрез изпълнение на следната команда. Когато колоната WORKSPACEREADY стане `True`, моделът е успешно разположен.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

След това може да се намери cluster IP на извеждащата услуга и да се използва временен `curl` pod за тестване на крайна точка на услугата в клъстера.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Бърз старт за извеждане Phi-3 с адаптери

След инсталиране на Kaito, може да се опитат следните команди за стартиране на извеждаща услуга.

[Примерен код за извеждане Phi-3 с адаптери](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Статусът на workspace може да се проследи чрез изпълнение на следната команда. Когато колоната WORKSPACEREADY стане `True`, моделът е успешно разположен.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

След това може да се намери cluster IP на извеждащата услуга и да се използва временен `curl` pod за тестване на крайна точка на услугата в клъстера.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.