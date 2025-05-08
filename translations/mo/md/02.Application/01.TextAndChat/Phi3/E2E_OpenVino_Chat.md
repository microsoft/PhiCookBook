<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-07T14:08:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "mo"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Este código exporta un modelo al formato OpenVINO, lo carga y lo usa para generar una respuesta a un prompt dado.

1. **Exportando el Modelo**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Este comando utiliza `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importando las Bibliotecas Necesarias**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Estas líneas importan clases del módulo `transformers` library and the `optimum.intel.openvino`, que son necesarias para cargar y usar el modelo.

3. **Configurando el Directorio del Modelo y la Configuración**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifies where the model files are stored.
   - `ov_config` es un diccionario que configura el modelo OpenVINO para priorizar baja latencia, usar un solo stream de inferencia y no utilizar un directorio de caché.

4. **Cargando el Modelo**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Esta línea carga el modelo desde el directorio especificado, usando la configuración definida anteriormente. También permite la ejecución remota de código si es necesario.

5. **Cargando el Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Esta línea carga el tokenizer, que se encarga de convertir el texto en tokens que el modelo puede entender.

6. **Configurando los Argumentos del Tokenizer**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Este diccionario especifica que no se deben agregar tokens especiales al resultado tokenizado.

7. **Definiendo el Prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Esta cadena establece un prompt de conversación donde el usuario le pide al asistente AI que se presente.

8. **Tokenizando el Prompt**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Esta línea convierte el prompt en tokens que el modelo puede procesar, devolviendo el resultado como tensores de PyTorch.

9. **Generando una Respuesta**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Esta línea usa el modelo para generar una respuesta basada en los tokens de entrada, con un máximo de 1024 tokens nuevos.

10. **Decodificando la Respuesta**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Esta línea convierte los tokens generados de nuevo en una cadena legible para humanos, omitiendo cualquier token especial, y obtiene el primer resultado.

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.

---

If by "mo" you mean a specific language or dialect, please clarify which language "mo" refers to, so I can provide the correct translation.