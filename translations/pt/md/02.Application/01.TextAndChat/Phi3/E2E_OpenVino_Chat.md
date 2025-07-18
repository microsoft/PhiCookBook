<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:03:49+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "pt"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Este código exporta um modelo para o formato OpenVINO, carrega-o e usa-o para gerar uma resposta a um prompt dado.

1. **Exportar o Modelo**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Este comando utiliza a ferramenta `optimum-cli` para exportar um modelo para o formato OpenVINO, que está otimizado para inferência eficiente.
   - O modelo exportado é o `"microsoft/Phi-3-mini-4k-instruct"`, configurado para a tarefa de gerar texto com base no contexto anterior.
   - Os pesos do modelo são quantizados para inteiros de 4 bits (`int4`), o que ajuda a reduzir o tamanho do modelo e acelerar o processamento.
   - Outros parâmetros como `group-size`, `ratio` e `sym` são usados para ajustar o processo de quantização.
   - O modelo exportado é guardado na diretoria `./model/phi3-instruct/int4`.

2. **Importar as Bibliotecas Necessárias**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Estas linhas importam classes da biblioteca `transformers` e do módulo `optimum.intel.openvino`, que são necessárias para carregar e usar o modelo.

3. **Configurar a Diretoria do Modelo e a Configuração**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` especifica onde os ficheiros do modelo estão armazenados.
   - `ov_config` é um dicionário que configura o modelo OpenVINO para priorizar baixa latência, usar um único fluxo de inferência e não usar uma diretoria de cache.

4. **Carregar o Modelo**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Esta linha carrega o modelo a partir da diretoria especificada, usando as definições de configuração anteriores. Também permite a execução remota de código, se necessário.

5. **Carregar o Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Esta linha carrega o tokenizer, que é responsável por converter texto em tokens que o modelo consegue interpretar.

6. **Configurar os Argumentos do Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Este dicionário especifica que não devem ser adicionados tokens especiais à saída tokenizada.

7. **Definir o Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Esta string define um prompt de conversa onde o utilizador pede ao assistente de IA para se apresentar.

8. **Tokenizar o Prompt**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Esta linha converte o prompt em tokens que o modelo pode processar, retornando o resultado como tensores PyTorch.

9. **Gerar uma Resposta**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Esta linha usa o modelo para gerar uma resposta com base nos tokens de entrada, com um máximo de 1024 tokens novos.

10. **Decodificar a Resposta**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Esta linha converte os tokens gerados de volta para uma string legível, ignorando quaisquer tokens especiais, e obtém o primeiro resultado.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.