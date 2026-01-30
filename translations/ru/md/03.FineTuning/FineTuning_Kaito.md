## Тонкая настройка с Kaito

[Kaito](https://github.com/Azure/kaito) — это оператор, который автоматизирует развертывание моделей AI/ML для инференса в кластере Kubernetes.

Kaito имеет следующие ключевые отличия по сравнению с большинством популярных методов развертывания моделей, основанных на инфраструктуре виртуальных машин:

- Управление файлами моделей с помощью контейнерных образов. Предоставляется HTTP-сервер для выполнения вызовов инференса с использованием библиотеки моделей.
- Избегание настройки параметров развертывания под конкретное GPU-оборудование за счёт предустановленных конфигураций.
- Автоматическое выделение GPU-узлов в зависимости от требований модели.
- Хранение больших образов моделей в публичном Microsoft Container Registry (MCR), если это разрешено лицензией.

Используя Kaito, процесс интеграции крупных AI-моделей для инференса в Kubernetes значительно упрощается.

## Архитектура

Kaito следует классическому паттерну проектирования Kubernetes Custom Resource Definition (CRD)/контроллер. Пользователь управляет кастомным ресурсом `workspace`, который описывает требования к GPU и спецификацию инференса. Контроллеры Kaito автоматизируют развертывание, синхронизируя состояние ресурса `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

На рисунке выше показан обзор архитектуры Kaito. Основные компоненты включают:

- **Workspace controller**: Синхронизирует кастомный ресурс `workspace`, создаёт кастомные ресурсы `machine` (описаны ниже) для запуска автоматического выделения узлов и создаёт нагрузку для инференса (`deployment` или `statefulset`) на основе предустановленных конфигураций модели.
- **Node provisioner controller**: Контроллер называется *gpu-provisioner* в [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Он использует CRD `machine`, заимствованный из [Karpenter](https://sigs.k8s.io/karpenter), для взаимодействия с контроллером workspace. Интегрируется с API Azure Kubernetes Service (AKS) для добавления новых GPU-узлов в кластер AKS.  
> Примечание: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — это компонент с открытым исходным кодом. Его можно заменить другими контроллерами, если они поддерживают API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Обзорное видео  
[Смотреть демонстрацию Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Установка

Пожалуйста, ознакомьтесь с инструкцией по установке [здесь](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Быстрый старт

После установки Kaito можно выполнить следующие команды, чтобы запустить сервис тонкой настройки.

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

Статус workspace можно отслеживать с помощью следующей команды. Когда в столбце WORKSPACEREADY появится значение `True`, модель успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Далее можно узнать IP-адрес сервиса инференса в кластере и использовать временный pod с `curl` для тестирования конечной точки сервиса внутри кластера.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.