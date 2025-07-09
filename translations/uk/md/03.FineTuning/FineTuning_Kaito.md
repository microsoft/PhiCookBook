<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-09T18:57:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "uk"
}
-->
## Тонке налаштування з Kaito

[Kaito](https://github.com/Azure/kaito) — це оператор, який автоматизує розгортання моделей штучного інтелекту/машинного навчання в кластері Kubernetes.

Kaito має такі ключові відмінності порівняно з більшістю популярних методів розгортання моделей, побудованих на віртуальних машинах:

- Керує файлами моделей за допомогою контейнерних образів. Для виконання викликів inference через бібліотеку моделей надається HTTP-сервер.
- Уникає налаштування параметрів розгортання під конкретне GPU обладнання, пропонуючи готові конфігурації.
- Автоматично забезпечує GPU-вузли відповідно до вимог моделі.
- Розміщує великі образи моделей у публічному Microsoft Container Registry (MCR), якщо це дозволяє ліцензія.

Завдяки Kaito процес підключення великих AI inference моделей у Kubernetes значно спрощується.

## Архітектура

Kaito дотримується класичного патерну Kubernetes Custom Resource Definition (CRD)/controller. Користувач керує кастомним ресурсом `workspace`, який описує вимоги до GPU та специфікації inference. Контролери Kaito автоматизують розгортання, узгоджуючи стан кастомного ресурсу `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

На наведеній схемі показано огляд архітектури Kaito. Основні компоненти включають:

- **Workspace controller**: Узгоджує кастомний ресурс `workspace`, створює кастомні ресурси `machine` (описані нижче) для запуску автоматичного забезпечення вузлів, а також створює inference навантаження (`deployment` або `statefulset`) на основі готових конфігурацій моделей.
- **Node provisioner controller**: Контролер з назвою *gpu-provisioner* у [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Використовує CRD `machine`, що походить від [Karpenter](https://sigs.k8s.io/karpenter), для взаємодії з workspace controller. Інтегрується з API Azure Kubernetes Service (AKS) для додавання нових GPU-вузлів до кластера AKS.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — це відкритий компонент. Його можна замінити іншими контролерами, якщо вони підтримують API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Оглядове відео  
[Переглянути демонстрацію Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Встановлення

Будь ласка, ознайомтеся з інструкцією з встановлення [тут](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Швидкий старт

Після встановлення Kaito можна спробувати виконати наступні команди для запуску сервісу тонкого налаштування.

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

Статус workspace можна відстежувати за допомогою наступної команди. Коли у стовпці WORKSPACEREADY з’явиться `True`, модель успішно розгорнута.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Далі можна дізнатися IP-адресу inference сервісу в кластері та використати тимчасовий pod з `curl` для тестування кінцевої точки сервісу в кластері.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.