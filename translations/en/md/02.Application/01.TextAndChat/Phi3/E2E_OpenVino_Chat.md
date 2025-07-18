<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:00:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "en"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

This code exports a model to the OpenVINO format, loads it, and uses it to generate a response to a given prompt.

1. **Exporting the Model**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - This command uses the `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.  
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's configured for the task of generating text based on previous context.  
   - The model weights are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.  
   - Additional parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.  
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importing Necessary Libraries**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - These lines import classes from the `transformers` library and the `optimum.intel.openvino` module, which are required to load and use the model.

3. **Setting Up the Model Directory and Configuration**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifies the location of the model files.  
   - `ov_config` is a dictionary that configures the OpenVINO model to prioritize low latency, use a single inference stream, and disable the cache directory.

4. **Loading the Model**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - This line loads the model from the specified directory using the configuration settings defined earlier. It also enables remote code execution if needed.

5. **Loading the Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - This line loads the tokenizer, which converts text into tokens that the model can process.

6. **Setting Up Tokenizer Arguments**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - This dictionary specifies that special tokens should not be added to the tokenized output.

7. **Defining the Prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - This string sets up a conversation prompt where the user asks the AI assistant to introduce itself.

8. **Tokenizing the Prompt**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - This line converts the prompt into tokens that the model can process, returning the result as PyTorch tensors.

9. **Generating a Response**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - This line uses the model to generate a response based on the input tokens, with a maximum of 1024 new tokens.

10. **Decoding the Response**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - This line converts the generated tokens back into a human-readable string, skipping any special tokens, and retrieves the first result.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.