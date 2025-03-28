<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-03-27T13:52:39+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "ru"
}
-->
## Тонкая настройка с Kaito

[Kaito](https://github.com/Azure/kaito) — это оператор, который автоматизирует развертывание моделей AI/ML для выполнения выводов в кластере Kubernetes.

Kaito обладает следующими ключевыми преимуществами по сравнению с большинством стандартных методов развертывания моделей, построенных на инфраструктуре виртуальных машин:

- Управление файлами моделей с использованием контейнерных образов. Предоставляется HTTP-сервер для выполнения вызовов вывода с использованием библиотеки модели.
- Избегает необходимости настройки параметров развертывания под GPU-оборудование благодаря готовым конфигурациям.
- Автоматически добавляет GPU-узлы на основе требований модели.
- Размещает большие образы моделей в публичном Microsoft Container Registry (MCR), если это разрешено лицензией.

С помощью Kaito процесс внедрения крупных моделей для вывода AI в Kubernetes значительно упрощается.

## Архитектура

Kaito следует классическому шаблону проектирования Kubernetes с использованием Custom Resource Definition (CRD) и контроллера. Пользователь управляет ресурсом `workspace`, который описывает требования к GPU и спецификацию вывода. Контроллеры Kaito автоматизируют развертывание, согласовывая ресурс `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Архитектура Kaito" alt="Архитектура Kaito">
</div>

На изображении выше представлена общая схема архитектуры Kaito. Основные компоненты включают:

- **Контроллер рабочего пространства**: Обрабатывает ресурс `workspace`, создаёт ресурсы `machine` (объяснены ниже) для запуска автоматического добавления узлов, а также создаёт рабочую нагрузку для вывода (`deployment` или `statefulset`) на основе готовых конфигураций модели.
- **Контроллер добавления узлов**: Этот контроллер называется *gpu-provisioner* в [Helm-чарте gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Он использует CRD `machine`, разработанный в рамках [Karpenter](https://sigs.k8s.io/karpenter), для взаимодействия с контроллером рабочего пространства. Интегрируется с API Azure Kubernetes Service (AKS) для добавления новых GPU-узлов в кластер AKS.
> Примечание: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — это компонент с открытым исходным кодом. Его можно заменить другими контроллерами, если они поддерживают API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Обзорное видео
[Посмотреть демонстрацию Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Установка

Руководство по установке доступно [здесь](https://github.com/Azure/kaito/blob/main/docs/installation.md).

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

Статус рабочего пространства можно отслеживать с помощью следующей команды. Когда в столбце WORKSPACEREADY появится значение `True`, модель успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Далее можно найти IP-адрес кластера для сервиса вывода и использовать временный pod `curl` для тестирования конечной точки сервиса в кластере.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.