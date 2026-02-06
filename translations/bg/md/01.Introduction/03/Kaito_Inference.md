## Извеждане с Kaito 

[Kaito](https://github.com/Azure/kaito) е оператор, който автоматизира разгръщането на AI/ML модели за извеждане (inference) в Kubernetes клъстер.

Kaito има следните основни разлики в сравнение с повечето основни методологии за разгръщане на модели, базирани на инфраструктури с виртуални машини:

- Управление на файлове с модели с помощта на контейнерни образи. Предоставя се HTTP сървър за извършване на извеждане чрез библиотеката на модела.
- Избягва настройването на параметрите за разгръщане, за да паснат на GPU хардуер, като предоставя предварително зададени конфигурации.
- Автоматично осигурява GPU възли според изискванията на модела.
- Хоства големи образи на модели в публичния Microsoft Container Registry (MCR), ако лицензът го позволява.

Използвайки Kaito, работният процес за добавяне на големи AI модели за извеждане в Kubernetes е значително опростен.


## Архитектура

Kaito следва класическия Kubernetes модел Custom Resource Definition (CRD)/controller. Потребителят управлява потребителски ресурс `workspace`, който описва изискванията за GPU и спецификацията на извеждането. Kaito контролерите автоматизират разгръщането, като синхронизират потребителския ресурс `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine архитектура" alt="KAITO RAGEngine архитектура">
</div>

Горната илюстрация показва преглед на архитектурата на Kaito. Основните му компоненти са:

- **Workspace controller**: Синхронизира потребителския ресурс `workspace`, създава потребителски ресурси `machine` (описани по-долу), за да активира автоматичното осигуряване на възли, и създава извеждащото натоварване (`deployment` или `statefulset`), базирано на предварително зададените конфигурации на модела.
- **Node provisioner controller**: Контролерът се нарича *gpu-provisioner* в [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Използва CRD `machine`, произтичащ от [Karpenter](https://sigs.k8s.io/karpenter), за взаимодействие с workspace контролера. Интегрира се с Azure Kubernetes Service (AKS) API, за да добавя нови GPU възли към AKS клъстера.
> Забележка: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) е с отворен код. Може да бъде заменен с други контролери, ако те поддържат [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Инсталация

Моля, вижте указанията за инсталиране [тук](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Бърз старт Извеждане Phi-3
[Примерен код Извеждане Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Настройка на пътя за изход ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Статусът на workspace може да се проследи чрез изпълнението на следната команда. Когато колоната WORKSPACEREADY стане `True`, моделът е успешно разположен.

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

## Бърз старт Извеждане Phi-3 с адаптери

След инсталиране на Kaito, можете да опитате следните команди за стартиране на извеждаща услуга.

[Примерен код Извеждане Phi-3 с адаптери](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Настройване на изходния път ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Статусът на workspace може да се проследи чрез изпълнението на следната команда. Когато колоната WORKSPACEREADY стане `True`, моделът е успешно разположен.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за официален източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->