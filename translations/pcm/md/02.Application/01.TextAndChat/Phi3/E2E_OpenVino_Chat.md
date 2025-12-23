<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-12-21T21:30:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "pcm"
}
-->
[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Dis code dey export model go di OpenVINO format, e go load am, and e go use am make response to di prompt wey dem give. 

1. **Exporting di Model**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Dis command dey use the `optimum-cli` tool to export model to di OpenVINO format, wey dey optimized for efficient inference.
   - Di model wey dem dey export na `"microsoft/Phi-3-mini-4k-instruct"`, and dem don set am for di task of generating text based on past context.
   - Di weights of di model don quantize to 4-bit integers (`int4`), wey dey help reduce di model size and make processing faster.
   - Oda parameters like `group-size`, `ratio`, and `sym` dey used to fine-tune di quantization process.
   - Di exported model dey save for di directory `./model/phi3-instruct/int4`.

2. **Import di Necessary Libraries**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Dis lines dey import classes from di `transformers` library and di `optimum.intel.openvino` module, wey dem need to load and use di model.

3. **Setting Up di Model Directory and Configuration**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` dey specify where di model files dey stored.
   - `ov_config` na dictionary wey configure di OpenVINO model to prioritize low latency, use one inference stream, and no dey use cache directory.

4. **Loading di Model**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Dis line dey load di model from di specified directory, using di configuration settings wey dem define earlier. E still dey allow remote code execution if necessary.

5. **Loading di Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Dis line dey load di tokenizer, wey responsible for converting text into tokens wey di model fit understand.

6. **Setting Up di Tokenizer Arguments**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Dis dictionary dey specify say special tokens no suppose add to di tokenized output.

7. **Defining di Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Dis string dey set up conversation prompt wey di user dey ask di AI assistant make e introduce itself.

8. **Tokenizing di Prompt**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Dis line dey convert di prompt to tokens wey di model fit process, e go return di result as PyTorch tensors.

9. **Generating di Response**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Dis line dey use di model to generate response based on di input tokens, with maximum of 1024 new tokens.

10. **Decoding di Response**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Dis line dey convert di generated tokens back to human-readable string, e go skip any special tokens, and e go return di first result.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Abeg note:
Dis document dem don translate wit AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, make you sabi say automated translations fit get mistakes or things wey no pure correct. The original document for im own language na the main authoritative source. If na important matter, e better make professional human translator check am. We no dey liable for any misunderstanding or wrong interpretation wey fit come from di use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->