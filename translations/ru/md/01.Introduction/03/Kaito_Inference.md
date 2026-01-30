## Вывод с помощью Kaito

[Kaito](https://github.com/Azure/kaito) — это оператор, который автоматизирует развертывание моделей инференса AI/ML в кластере Kubernetes.

Kaito имеет следующие ключевые отличия по сравнению с большинством основных методов развертывания моделей, построенных на основе инфраструктуры виртуальных машин:

- Управление файлами моделей с использованием контейнерных образов. Предоставляется HTTP-сервер для выполнения вызовов инференса с использованием библиотеки моделей.
- Избегание настройки параметров развертывания под конкретное GPU-оборудование с помощью предустановленных конфигураций.
- Автоматическое выделение узлов с GPU в зависимости от требований модели.
- Размещение больших образов моделей в публичном реестре контейнеров Microsoft Container Registry (MCR), если позволяет лицензия.

Используя Kaito, процесс подключения больших моделей AI инференса в Kubernetes значительно упрощается.

## Архитектура

Kaito следует классическому паттерну проектирования Kubernetes Custom Resource Definition (CRD)/контроллера. Пользователь управляет собственным ресурсом `workspace`, который описывает требования к GPU и спецификацию инференса. Контроллеры Kaito автоматизируют развертывание, приводя в соответствие ресурс `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

На рисунке выше представлена обзорная архитектура Kaito. Основные компоненты включают:

- **Контроллер Workspace**: Он приводит в соответствие ресурс `workspace`, создает пользовательские ресурсы `machine` (описанные ниже) для запуска автоматического выделения узлов и создает рабочую нагрузку инференса (`deployment` или `statefulset`) на основе предустановленных конфигураций модели.
- **Контроллер выделения узлов**: Контроллер называется *gpu-provisioner* в [helm-чарте gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Он использует CRD ресурса `machine`, появившийся из проекта [Karpenter](https://sigs.k8s.io/karpenter), для взаимодействия с контроллером workspace. Интегрируется с API Azure Kubernetes Service (AKS) для добавления новых GPU-узлов в кластер AKS.
> Примечание: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — это компонент с открытым исходным кодом. Его можно заменить другими контроллерами, если они поддерживают API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Установка

Пожалуйста, ознакомьтесь с руководством по установке [здесь](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Быстрый старт с инференсом Phi-3
[Пример кода инференса Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Настройка выходного пути ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Статус рабочего пространства можно отследить, выполнив следующую команду. Когда в столбце WORKSPACEREADY появляется значение `True`, модель успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Далее можно найти IP-адрес службы инференса в кластере и использовать временный pod с `curl` для тестирования конечной точки сервиса внутри кластера.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Быстрый старт с инференсом Phi-3 с адаптерами

После установки Kaito можно выполнить следующие команды, чтобы запустить службу инференса.

[Пример кода инференса Phi-3 с адаптерами](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Настройка выходного пути ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Статус рабочего пространства можно отследить, выполнив следующую команду. Когда в столбце WORKSPACEREADY появляется значение `True`, модель успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Далее можно найти IP-адрес службы инференса в кластере и использовать временный pod с `curl` для тестирования конечной точки сервиса внутри кластера.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, просим учитывать, что машинный перевод может содержать ошибки и неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->