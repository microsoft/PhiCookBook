<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:48:40+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ko"
}
-->
## Kaito를 이용한 추론

[Kaito](https://github.com/Azure/kaito)는 Kubernetes 클러스터에서 AI/ML 추론 모델 배포를 자동화하는 오퍼레이터입니다.

Kaito는 가상 머신 인프라 위에 구축된 대부분의 주류 모델 배포 방법론과 비교했을 때 다음과 같은 주요 차별점을 가지고 있습니다:

- 컨테이너 이미지를 사용해 모델 파일을 관리합니다. 모델 라이브러리를 이용한 추론 호출을 수행하는 HTTP 서버가 제공됩니다.
- 사전 설정된 구성을 제공하여 GPU 하드웨어에 맞게 배포 파라미터를 조정할 필요를 없앱니다.
- 모델 요구사항에 따라 GPU 노드를 자동으로 프로비저닝합니다.
- 라이선스가 허용하는 경우, 대용량 모델 이미지를 공개 Microsoft Container Registry(MCR)에 호스팅합니다.

Kaito를 사용하면 Kubernetes에서 대형 AI 추론 모델을 온보딩하는 작업 흐름이 크게 단순화됩니다.


## 아키텍처

Kaito는 전통적인 Kubernetes Custom Resource Definition(CRD)/컨트롤러 설계 패턴을 따릅니다. 사용자는 GPU 요구사항과 추론 사양을 설명하는 `workspace` 커스텀 리소스를 관리합니다. Kaito 컨트롤러는 `workspace` 커스텀 리소스를 조정하여 배포를 자동화합니다.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

위 그림은 Kaito 아키텍처 개요를 보여줍니다. 주요 구성 요소는 다음과 같습니다:

- **Workspace controller**: `workspace` 커스텀 리소스를 조정하며, 노드 자동 프로비저닝을 트리거하기 위해 `machine`(아래 설명) 커스텀 리소스를 생성하고, 모델 사전 설정 구성에 따라 추론 워크로드(`deployment` 또는 `statefulset`)를 생성합니다.
- **Node provisioner controller**: 이 컨트롤러는 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)에서 *gpu-provisioner*라는 이름을 가집니다. [Karpenter](https://sigs.k8s.io/karpenter)에서 유래한 `machine` CRD를 사용해 workspace controller와 상호작용합니다. Azure Kubernetes Service(AKS) API와 통합하여 AKS 클러스터에 새로운 GPU 노드를 추가합니다.
> 참고: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner)는 오픈 소스 컴포넌트입니다. [Karpenter-core](https://sigs.k8s.io/karpenter) API를 지원하는 다른 컨트롤러로 대체할 수 있습니다.

## 설치

설치 가이드는 [여기](https://github.com/Azure/kaito/blob/main/docs/installation.md)를 참고하세요.

## Phi-3 추론 빠른 시작
[Phi-3 추론 샘플 코드](https://github.com/Azure/kaito/tree/main/examples/inference)

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

다음 명령어로 workspace 상태를 확인할 수 있습니다. WORKSPACEREADY 열이 `True`가 되면 모델이 성공적으로 배포된 것입니다.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

다음으로, 추론 서비스의 클러스터 IP를 찾아 임시 `curl` 파드를 사용해 클러스터 내 서비스 엔드포인트를 테스트할 수 있습니다.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## 어댑터를 사용한 Phi-3 추론 빠른 시작

Kaito 설치 후, 다음 명령어를 통해 추론 서비스를 시작할 수 있습니다.

[어댑터를 사용한 Phi-3 추론 샘플 코드](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

다음 명령어로 workspace 상태를 확인할 수 있습니다. WORKSPACEREADY 열이 `True`가 되면 모델이 성공적으로 배포된 것입니다.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

다음으로, 추론 서비스의 클러스터 IP를 찾아 임시 `curl` 파드를 사용해 클러스터 내 서비스 엔드포인트를 테스트할 수 있습니다.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.