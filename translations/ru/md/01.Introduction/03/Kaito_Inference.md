<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-03-27T07:36:48+00:00",
  "source_file": "md\\01.Introduction\\03\\Kaito_Inference.md",
  "language_code": "ru"
}
-->
## Инференс с Kaito

[Kaito](https://github.com/Azure/kaito) — это оператор, который автоматизирует развертывание моделей инференса AI/ML в кластере Kubernetes.

Kaito имеет следующие ключевые отличия по сравнению с большинством распространенных методов развертывания моделей, основанных на инфраструктуре виртуальных машин:

- Управление файлами моделей с использованием контейнерных образов. Предоставляется HTTP-сервер для выполнения запросов инференса с использованием библиотеки модели.
- Исключение необходимости настройки параметров развертывания для соответствия оборудованию GPU благодаря предустановленным конфигурациям.
- Автоматическое выделение GPU-узлов на основе требований модели.
- Размещение больших контейнерных образов моделей в публичном Microsoft Container Registry (MCR), если лицензия это позволяет.

С помощью Kaito процесс интеграции больших моделей инференса AI в Kubernetes значительно упрощается.

## Архитектура

Kaito следует классическому шаблону проектирования Custom Resource Definition (CRD)/контроллера в Kubernetes. Пользователь управляет ресурсом `workspace`, который описывает требования к GPU и спецификацию инференса. Контроллеры Kaito автоматизируют развертывание, согласовывая ресурс `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Архитектура Kaito" alt="Архитектура Kaito">
</div>

На рисунке выше представлен общий обзор архитектуры Kaito. Основные компоненты включают:

- **Контроллер рабочего пространства**: Согласует ресурс `workspace`, создает пользовательские ресурсы `machine` (описаны ниже) для запуска автоматического выделения узлов и создает нагрузку инференса (`deployment` или `statefulset`) на основе предустановленных конфигураций модели.
- **Контроллер выделения узлов**: Имя контроллера — *gpu-provisioner* в [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Он использует CRD `machine`, основанный на [Karpenter](https://sigs.k8s.io/karpenter), для взаимодействия с контроллером рабочего пространства. Интегрируется с API Azure Kubernetes Service (AKS) для добавления новых GPU-узлов в кластер AKS.  
> Примечание: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — это компонент с открытым исходным кодом. Его можно заменить другими контроллерами, если они поддерживают API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Установка

Инструкции по установке можно найти [здесь](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Быстрый старт: Инференс Phi-3
[Пример кода для инференса Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Статус рабочего пространства можно отслеживать, выполняя следующую команду. Когда столбец WORKSPACEREADY примет значение `True`, модель была успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Далее можно найти cluster ip сервиса инференса и использовать временный `curl` pod для тестирования конечной точки сервиса в кластере.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Быстрый старт: Инференс Phi-3 с адаптерами

После установки Kaito можно выполнить следующие команды для запуска сервиса инференса.

[Пример кода для инференса Phi-3 с адаптерами](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Статус рабочего пространства можно отслеживать, выполняя следующую команду. Когда столбец WORKSPACEREADY примет значение `True`, модель была успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Далее можно найти cluster ip сервиса инференса и использовать временный `curl` pod для тестирования конечной точки сервиса в кластере.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неверные интерпретации, возникшие в результате использования данного перевода.