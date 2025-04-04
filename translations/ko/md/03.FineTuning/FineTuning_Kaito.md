<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05e69691c294289d217150bec390a5fb",
  "translation_date": "2025-04-04T06:59:02+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "ko"
}
-->
## Kaito로 세부 조정하기

[Kaito](https://github.com/Azure/kaito)는 Kubernetes 클러스터에서 AI/ML 추론 모델 배포를 자동화하는 운영 도구입니다.

Kaito는 대부분의 가상 머신 기반 인프라 위에 구축된 일반적인 모델 배포 방법론과 비교하여 다음과 같은 주요 차별점을 가지고 있습니다:

- 컨테이너 이미지를 사용하여 모델 파일을 관리합니다. 모델 라이브러리를 사용하여 추론 호출을 수행하는 http 서버를 제공합니다.
- GPU 하드웨어에 맞추기 위해 배포 매개변수를 조정할 필요 없이 미리 설정된 구성을 제공합니다.
- 모델 요구사항에 따라 GPU 노드를 자동으로 프로비저닝합니다.
- 라이선스가 허용하는 경우 대규모 모델 이미지를 Microsoft Container Registry(MCR)에 호스팅합니다.

Kaito를 사용하면 Kubernetes에서 대규모 AI 추론 모델을 온보딩하는 워크플로우가 크게 간소화됩니다.


## 아키텍처

Kaito는 고전적인 Kubernetes Custom Resource Definition(CRD)/컨트롤러 디자인 패턴을 따릅니다. 사용자는 GPU 요구사항과 추론 사양을 설명하는 `workspace` 커스텀 리소스를 관리합니다. Kaito 컨트롤러는 `workspace` 커스텀 리소스를 조정하여 배포를 자동화합니다.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

위 그림은 Kaito 아키텍처 개요를 보여줍니다. 주요 구성 요소는 다음과 같습니다:

- **워크스페이스 컨트롤러**: `workspace` 커스텀 리소스를 조정하고, 노드 자동 프로비저닝을 트리거하기 위해 `machine` (아래에서 설명) 커스텀 리소스를 생성하며, 모델의 미리 설정된 구성에 따라 추론 워크로드(`deployment` 또는 `statefulset`)를 생성합니다.
- **노드 프로비저너 컨트롤러**: 컨트롤러 이름은 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)에서 *gpu-provisioner*입니다. 이는 워크스페이스 컨트롤러와 상호작용하기 위해 [Karpenter](https://sigs.k8s.io/karpenter)에서 유래된 `machine` CRD를 사용합니다. Azure Kubernetes Service(AKS) API와 통합하여 AKS 클러스터에 새로운 GPU 노드를 추가합니다.
> 참고: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner)는 오픈 소스 구성 요소입니다. [Karpenter-core](https://sigs.k8s.io/karpenter) API를 지원하는 다른 컨트롤러로 대체할 수 있습니다.

## 개요 영상 
[Kaito 데모 보기](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## 설치

설치 안내는 [여기](https://github.com/Azure/kaito/blob/main/docs/installation.md)를 참조하세요.

## 빠른 시작

Kaito를 설치한 후, 다음 명령어를 실행하여 세부 조정 서비스를 시작할 수 있습니다.

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

워크스페이스 상태는 다음 명령어를 실행하여 추적할 수 있습니다. WORKSPACEREADY 열이 `True`로 표시되면 모델이 성공적으로 배포된 것입니다.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

다음으로, 추론 서비스의 클러스터 IP를 확인하고 임시 `curl` pod를 사용하여 클러스터 내에서 서비스 엔드포인트를 테스트할 수 있습니다.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있습니다. 원본 문서(원어로 작성된 문서)를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.