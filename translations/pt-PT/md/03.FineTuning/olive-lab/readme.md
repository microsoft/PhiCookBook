# Laboratório. Otimizar modelos de IA para inferência no dispositivo

## Introdução

> [!IMPORTANT]
> Este laboratório requer uma **GPU Nvidia A10 ou A100** com os drivers associados e o toolkit CUDA (versão 12+) instalados.

> [!NOTE]
> Este é um laboratório de **35 minutos** que lhe dará uma introdução prática aos conceitos essenciais de otimização de modelos para inferência no dispositivo usando OLIVE.

## Objetivos de Aprendizagem

No final deste laboratório, será capaz de usar o OLIVE para:

- Quantizar um Modelo de IA usando o método de quantização AWQ.
- Ajustar um modelo de IA para uma tarefa específica.
- Gerar adaptadores LoRA (modelo ajustado) para inferência eficiente no dispositivo com o ONNX Runtime.

### O que é o Olive

Olive (*O*NNX *live*) é um toolkit de otimização de modelos com uma CLI associada que permite entregar modelos para o ONNX runtime +++https://onnxruntime.ai+++ com qualidade e desempenho.

![Olive Flow](../../../../../translated_images/pt-PT/olive-flow.5daf97340275f8b6.webp)

A entrada para o Olive é tipicamente um modelo PyTorch ou Hugging Face e a saída é um modelo ONNX otimizado que é executado num dispositivo (alvo de deployment) a correr o ONNX runtime. O Olive otimiza o modelo para o acelerador de IA do dispositivo de deployment (NPU, GPU, CPU) fornecido por um fabricante de hardware como Qualcomm, AMD, Nvidia ou Intel.

O Olive executa um *workflow*, que é uma sequência ordenada de tarefas individuais de otimização de modelo chamadas *passes* – exemplos de passes incluem: compressão de modelo, captura de grafo, quantização, otimização de grafo. Cada passe tem um conjunto de parâmetros que podem ser ajustados para alcançar as melhores métricas, como precisão e latência, que são avaliadas pelo respetivo avaliador. O Olive utiliza uma estratégia de busca que usa um algoritmo para autoajustar cada passe um a um ou um conjunto de passes em conjunto.

#### Benefícios do Olive

- **Reduz a frustração e o tempo** de experimentação manual por tentativa e erro com diferentes técnicas para otimização de grafo, compressão e quantização. Defina as suas restrições de qualidade e desempenho e deixe o Olive encontrar automaticamente o melhor modelo para si.
- **Mais de 40 componentes integrados de otimização de modelos** que cobrem técnicas avançadas em quantização, compressão, otimização de grafo e ajuste fino.
- **CLI fácil de usar** para tarefas comuns de otimização de modelos. Por exemplo, olive quantize, olive auto-opt, olive finetune.
- Empacotamento e deployment de modelos integrados.
- Suporta geração de modelos para **Multi LoRA serving**.
- Construa workflows usando YAML/JSON para orquestrar tarefas de otimização e deployment de modelos.
- Integração com **Hugging Face** e **Azure AI**.
- Mecanismo de **cache** integrado para **reduzir custos**.

## Instruções do Laboratório

> [!NOTE]
> Por favor, certifique-se de que já configurou o seu Azure AI Hub e Projeto e configurou o seu compute A100 conforme o Laboratório 1.

### Passo 0: Conectar ao seu Azure AI Compute

Vai conectar-se ao Azure AI compute usando a funcionalidade remota no **VS Code**.

1. Abra a aplicação desktop **VS Code**:
1. Abra a **paleta de comandos** com **Shift+Ctrl+P**
1. Na paleta de comandos, procure por **AzureML - remote: Connect to compute instance in New Window**.
1. Siga as instruções no ecrã para se conectar ao Compute. Isto envolve selecionar a sua Subscrição Azure, Grupo de Recursos, Projeto e o nome do Compute que configurou no Laboratório 1.
1. Uma vez conectado ao seu nó Azure ML Compute, será mostrado no **canto inferior esquerdo do Visual Code** `><Azure ML: Compute Name`

### Passo 1: Clonar este repositório

No VS Code, pode abrir um terminal novo com **Ctrl+J** e clonar este repositório:

No terminal deverá ver o prompt

```
azureuser@computername:~/cloudfiles/code$ 
```  
Clone a solução

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Passo 2: Abrir a pasta no VS Code

Para abrir o VS Code na pasta relevante, execute o seguinte comando no terminal, que abrirá uma nova janela:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativamente, pode abrir a pasta selecionando **File** > **Open Folder**.

### Passo 3: Dependências

Abra uma janela de terminal no VS Code na sua Instância Azure AI Compute (dica: **Ctrl+J**) e execute os seguintes comandos para instalar as dependências:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> A instalação de todas as dependências demora cerca de 5 minutos.

Neste laboratório vai descarregar e carregar modelos para o catálogo de modelos Azure AI. Para aceder ao catálogo de modelos, precisa de iniciar sessão no Azure usando:

```bash
az login
```

> [!NOTE]
> No momento do login será solicitado que selecione a sua subscrição. Certifique-se de definir a subscrição para a fornecida neste laboratório.

### Passo 4: Executar comandos Olive

Abra uma janela de terminal no VS Code na sua Instância Azure AI Compute (dica: **Ctrl+J**) e certifique-se que o ambiente conda `olive-ai` está ativado:

```bash
conda activate olive-ai
```

De seguida, execute os seguintes comandos Olive na linha de comandos.

1. **Inspecionar os dados:** Neste exemplo, vai ajustar o modelo Phi-3.5-Mini para que fique especializado em responder a perguntas relacionadas com viagens. O código abaixo mostra os primeiros registos do conjunto de dados, que estão em formato JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Quantizar o modelo:** Antes de treinar o modelo, primeiro quantiza com o seguinte comando que usa uma técnica chamada Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ quantiza os pesos de um modelo considerando as ativações produzidas durante a inferência. Isto significa que o processo de quantização tem em conta a distribuição real dos dados nas ativações, levando a uma melhor preservação da precisão do modelo comparado com métodos tradicionais de quantização de pesos.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Demora cerca de **8 minutos** a completar a quantização AWQ, que irá **reduzir o tamanho do modelo de ~7.5GB para ~2.5GB**.

    Neste laboratório mostramos como importar modelos do Hugging Face (por exemplo: `microsoft/Phi-3.5-mini-instruct`). No entanto, o Olive também permite importar modelos do catálogo Azure AI atualizando o argumento `model_name_or_path` para um ID de ativo Azure AI (por exemplo: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **Treinar o modelo:** De seguida, o comando `olive finetune` ajusta o modelo quantizado. Quantizar o modelo *antes* do ajuste fino em vez de depois dá melhor precisão, pois o processo de ajuste fino recupera parte da perda causada pela quantização.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    Demora cerca de **6 minutos** a completar o ajuste fino (com 100 passos).

1. **Otimizar:** Com o modelo treinado, agora otimiza o modelo usando o comando `auto-opt` do Olive, que irá capturar o grafo ONNX e executar automaticamente várias otimizações para melhorar o desempenho do modelo para CPU, comprimindo o modelo e fazendo fusões. Note que também pode otimizar para outros dispositivos como NPU ou GPU apenas atualizando os argumentos `--device` e `--provider` – mas para este laboratório usaremos CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    Demora cerca de **5 minutos** a completar a otimização.

### Passo 5: Teste rápido de inferência do modelo

Para testar a inferência do modelo, crie um ficheiro Python na sua pasta chamado **app.py** e copie e cole o seguinte código:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Execute o código usando:

```bash
python app.py
```

### Passo 6: Carregar o modelo para o Azure AI

Carregar o modelo para um repositório de modelos Azure AI torna o modelo partilhável com outros membros da sua equipa de desenvolvimento e também gere o controlo de versões do modelo. Para carregar o modelo execute o seguinte comando:

> [!NOTE]
> Atualize os espaços reservados `{}` com o nome do seu grupo de recursos e o nome do Projeto Azure AI.

Para encontrar o seu grupo de recursos `"resourceGroup"` e o nome do Projeto Azure AI, execute o seguinte comando

```
az ml workspace show
```

Ou aceda a +++ai.azure.com+++ e selecione **management center** **project** **overview**

Atualize os espaços reservados `{}` com o nome do seu grupo de recursos e o nome do Projeto Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Pode depois ver o seu modelo carregado e fazer o deployment do seu modelo em https://ml.azure.com/model/list

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.