<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T14:26:03+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pl"
}
-->
## Inference z Kaito

[Kaito](https://github.com/Azure/kaito) to operator, który automatyzuje wdrażanie modeli AI/ML do inferencji w klastrze Kubernetes.

Kaito wyróżnia się następującymi kluczowymi cechami w porównaniu do większości popularnych metod wdrażania modeli opartych na infrastrukturach maszyn wirtualnych:

- Zarządzanie plikami modeli przy użyciu obrazów kontenerów. Udostępniany jest serwer http do wykonywania wywołań inferencji za pomocą biblioteki modelu.
- Unikanie strojenia parametrów wdrożenia pod sprzęt GPU poprzez dostarczanie gotowych konfiguracji.
- Automatyczne udostępnianie węzłów GPU na podstawie wymagań modelu.
- Hostowanie dużych obrazów modeli w publicznym Microsoft Container Registry (MCR), jeśli pozwala na to licencja.

Dzięki Kaito proces wdrażania dużych modeli AI do inferencji w Kubernetes jest znacznie uproszczony.

## Architektura

Kaito opiera się na klasycznym wzorcu projektowym Kubernetes Custom Resource Definition (CRD)/controller. Użytkownik zarządza zasobem niestandardowym `workspace`, który opisuje wymagania dotyczące GPU oraz specyfikację inferencji. Kontrolery Kaito automatyzują wdrożenie poprzez rekonsyliację zasobu niestandardowego `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Powyższy obraz przedstawia ogólny przegląd architektury Kaito. Główne jej komponenty to:

- **Kontroler workspace**: Rekonsyliuje zasób niestandardowy `workspace`, tworzy zasoby niestandardowe `machine` (opisane poniżej) w celu wyzwolenia automatycznego udostępniania węzłów oraz tworzy obciążenie inferencyjne (`deployment` lub `statefulset`) na podstawie gotowych konfiguracji modelu.
- **Kontroler udostępniania węzłów**: Nazwa kontrolera to *gpu-provisioner* w [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Używa CRD `machine` pochodzącego z [Karpenter](https://sigs.k8s.io/karpenter) do współpracy z kontrolerem workspace. Integruje się z API Azure Kubernetes Service (AKS) w celu dodania nowych węzłów GPU do klastra AKS. 
> Uwaga: Komponent [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) jest oprogramowaniem open source. Może zostać zastąpiony innymi kontrolerami, jeśli obsługują API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalacja

Proszę zapoznać się z instrukcją instalacji [tutaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Szybki start Inferencja Phi-3 
[Przykładowy kod Inferencja Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Strojenie ścieżki wyjściowej ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Status workspace można śledzić, uruchamiając następujące polecenie. Gdy w kolumnie WORKSPACEREADY pojawi się wartość `True`, model został pomyślnie wdrożony.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Następnie można znaleźć adres IP klastra usługi inferencyjnej i użyć tymczasowego podu `curl` do przetestowania punktu końcowego usługi w klastrze.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Szybki start Inferencja Phi-3 z adapterami

Po zainstalowaniu Kaito można spróbować poniższych poleceń, aby uruchomić usługę inferencyjną.

[Przykładowy kod Inferencja Phi-3 z adapterami](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Strojenie ścieżki wyjściowej ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Status workspace można śledzić, uruchamiając następujące polecenie. Gdy w kolumnie WORKSPACEREADY pojawi się wartość `True`, model został pomyślnie wdrożony.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Następnie można znaleźć adres IP klastra usługi inferencyjnej i użyć tymczasowego podu `curl` do przetestowania punktu końcowego usługi w klastrze.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że staramy się o dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako wiarygodne źródło informacji. W przypadku informacji o krytycznym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->