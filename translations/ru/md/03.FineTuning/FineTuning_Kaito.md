<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-07T13:38:14+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "ru"
}
-->
## Тонкая настройка с Kaito

[Kaito](https://github.com/Azure/kaito) — это оператор, который автоматизирует развертывание моделей AI/ML для инференса в кластере Kubernetes.

Kaito выделяется на фоне большинства популярных методов развертывания моделей, построенных на инфраструктуре виртуальных машин, благодаря следующим ключевым особенностям:

- Управление файлами моделей с помощью контейнерных образов. Для вызовов инференса через библиотеку модели предоставляется HTTP-сервер.
- Избегание настройки параметров развертывания под конкретное GPU-оборудование за счет использования предустановленных конфигураций.
- Автоматическое выделение GPU-нод в зависимости от требований модели.
- Размещение больших образов моделей в публичном Microsoft Container Registry (MCR), если это позволяет лицензия.

С помощью Kaito процесс интеграции крупных AI-моделей для инференса в Kubernetes становится значительно проще.

## Архитектура

Kaito следует классической архитектуре Kubernetes с использованием Custom Resource Definition (CRD) и контроллеров. Пользователь управляет кастомным ресурсом `workspace`, который описывает требования к GPU и спецификации инференса. Контроллеры Kaito автоматически осуществляют развертывание, синхронизируя состояние кастомного ресурса `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Архитектура Kaito" alt="Архитектура Kaito">
</div>

На схеме выше представлен обзор архитектуры Kaito. Основные компоненты включают:

- **Workspace controller**: Этот контроллер синхронизирует кастомный ресурс `workspace`, создаёт кастомные ресурсы `machine` (описанные ниже) для запуска автоматического выделения нод и формирует нагрузку для инференса (`deployment` или `statefulset`) на основе предустановленных конфигураций модели.
- **Node provisioner controller**: Контроллер с именем *gpu-provisioner* из [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Он использует CRD `machine`, основанный на [Karpenter](https://sigs.k8s.io/karpenter), для взаимодействия с workspace controller. Интегрируется с API Azure Kubernetes Service (AKS) для добавления новых GPU-нод в кластер AKS.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — это проект с открытым исходным кодом. Его можно заменить другими контроллерами, если они поддерживают API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Обзорное видео  
[Смотреть демонстрацию Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Установка

Пожалуйста, ознакомьтесь с инструкцией по установке [здесь](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Быстрый старт

После установки Kaito можно выполнить следующие команды для запуска сервиса тонкой настройки.

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

Статус рабочего пространства можно отслеживать с помощью следующей команды. Когда в колонке WORKSPACEREADY появится значение `True`, модель успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Далее можно узнать cluster IP сервиса инференса и использовать временный pod с `curl` для проверки конечной точки сервиса внутри кластера.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неверные толкования, возникшие в результате использования данного перевода.