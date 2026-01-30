[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Este código exporta um modelo para o formato OpenVINO, carrega-o e o utiliza para gerar uma resposta a um prompt fornecido.

1. **Exportando o Modelo**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Este comando usa a ferramenta `optimum-cli` para exportar um modelo para o formato OpenVINO, que é otimizado para inferência eficiente.  
   - O modelo exportado é o `"microsoft/Phi-3-mini-4k-instruct"`, configurado para a tarefa de gerar texto com base no contexto anterior.  
   - Os pesos do modelo são quantizados para inteiros de 4 bits (`int4`), o que ajuda a reduzir o tamanho do modelo e acelerar o processamento.  
   - Outros parâmetros como `group-size`, `ratio` e `sym` são usados para ajustar o processo de quantização.  
   - O modelo exportado é salvo no diretório `./model/phi3-instruct/int4`.

2. **Importando as Bibliotecas Necessárias**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Essas linhas importam classes da biblioteca `transformers` e do módulo `optimum.intel.openvino`, que são necessárias para carregar e usar o modelo.

3. **Configurando o Diretório do Modelo e a Configuração**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` especifica onde os arquivos do modelo estão armazenados.  
   - `ov_config` é um dicionário que configura o modelo OpenVINO para priorizar baixa latência, usar um fluxo de inferência e não utilizar um diretório de cache.

4. **Carregando o Modelo**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Esta linha carrega o modelo do diretório especificado, usando as configurações definidas anteriormente. Também permite a execução remota de código, se necessário.

5. **Carregando o Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Esta linha carrega o tokenizer, responsável por converter o texto em tokens que o modelo pode entender.

6. **Configurando os Argumentos do Tokenizer**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Este dicionário especifica que tokens especiais não devem ser adicionados à saída tokenizada.

7. **Definindo o Prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Esta string configura um prompt de conversa onde o usuário pede para o assistente de IA se apresentar.

8. **Tokenizando o Prompt**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Esta linha converte o prompt em tokens que o modelo pode processar, retornando o resultado como tensores PyTorch.

9. **Gerando uma Resposta**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Esta linha usa o modelo para gerar uma resposta com base nos tokens de entrada, com um máximo de 1024 tokens novos.

10. **Decodificando a Resposta**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Esta linha converte os tokens gerados de volta para uma string legível, ignorando tokens especiais, e recupera o primeiro resultado.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.