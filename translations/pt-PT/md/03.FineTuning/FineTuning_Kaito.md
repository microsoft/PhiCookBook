## Ajuste Fino com Kaito

[Kaito](https://github.com/Azure/kaito) é um operador que automatiza a implementação de modelos de inferência AI/ML num cluster Kubernetes.

O Kaito apresenta as seguintes diferenças chave em comparação com a maioria das metodologias convencionais de implementação de modelos baseadas em infraestruturas de máquinas virtuais:

- Gerir ficheiros de modelos usando imagens de containers. É fornecido um servidor http para realizar chamadas de inferência usando a biblioteca do modelo.
- Evitar ajustar parâmetros de implementação para se adequar ao hardware GPU, fornecendo configurações pré-definidas.
- Auto-provisionar nós GPU com base nos requisitos do modelo.
- Hospedar imagens de modelos grandes no Microsoft Container Registry (MCR) público, se a licença permitir.

Com o Kaito, o fluxo de trabalho para integrar grandes modelos de inferência AI no Kubernetes é bastante simplificado.

## Arquitetura

O Kaito segue o padrão clássico de design Kubernetes Custom Resource Definition (CRD)/controller. O utilizador gere um recurso personalizado `workspace` que descreve os requisitos de GPU e a especificação de inferência. Os controladores Kaito automatizam a implementação reconciliando o recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Arquitetura Kaito" alt="Arquitetura Kaito">
</div>

A figura acima apresenta uma visão geral da arquitetura do Kaito. Os seus principais componentes consistem em:

- **Controlador Workspace**: Reconciliia o recurso personalizado `workspace`, cria recursos personalizados `machine` (explicados abaixo) para disparar o auto-provisionamento de nós, e cria a carga de trabalho de inferência (`deployment` ou `statefulset`) com base nas configurações pré-definidas do modelo.
- **Controlador de provisionamento de nós**: O nome do controlador é *gpu-provisioner* no [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utiliza o CRD `machine` originado do [Karpenter](https://sigs.k8s.io/karpenter) para interagir com o controlador workspace. Integra-se com as APIs do Azure Kubernetes Service (AKS) para adicionar novos nós GPU ao cluster AKS.
> Nota: O [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) é um componente open source. Pode ser substituído por outros controladores se estes suportarem as APIs [Karpenter-core](https://sigs.k8s.io/karpenter).

## Vídeo de visão geral  
[Ver a Demo do Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalação

Por favor, consulte as instruções de instalação [aqui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Início rápido

Após instalar o Kaito, pode experimentar os seguintes comandos para iniciar um serviço de ajuste fino.

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

O estado do workspace pode ser acompanhado executando o seguinte comando. Quando a coluna WORKSPACEREADY ficar `True`, o modelo foi implementado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

De seguida, pode encontrar o IP do cluster do serviço de inferência e usar um pod temporário `curl` para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.