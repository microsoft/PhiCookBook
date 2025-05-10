<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:52:29+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "pa"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

ਇਹ ਕੋਡ ਇੱਕ ਮਾਡਲ ਨੂੰ OpenVINO ਫਾਰਮੈਟ ਵਿੱਚ ਐਕਸਪੋਰਟ ਕਰਦਾ ਹੈ, ਇਸਨੂੰ ਲੋਡ ਕਰਦਾ ਹੈ, ਅਤੇ ਦਿੱਤੇ ਗਏ ਪ੍ਰਾਂਪਟ ਲਈ ਜਵਾਬ ਬਣਾਉਣ ਲਈ ਵਰਤਦਾ ਹੈ।

1. **ਮਾਡਲ ਨੂੰ ਐਕਸਪੋਰਟ ਕਰਨਾ**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - ਇਹ ਕਮਾਂਡ `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` ਵਰਤਦੀ ਹੈ।

2. **ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕਰਨਾ**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - ਇਹ ਲਾਈਨਾਂ `transformers` library and the `optimum.intel.openvino` ਮੋਡੀਊਲ ਤੋਂ ਕਲਾਸਾਂ ਇੰਪੋਰਟ ਕਰਦੀਆਂ ਹਨ, ਜੋ ਮਾਡਲ ਨੂੰ ਲੋਡ ਅਤੇ ਵਰਤਣ ਲਈ ਜਰੂਰੀ ਹਨ।

3. **ਮਾਡਲ ਡਾਇਰੈਕਟਰੀ ਅਤੇ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈੱਟ ਕਰਨਾ**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੈ ਜੋ OpenVINO ਮਾਡਲ ਨੂੰ ਘੱਟ ਲੇਟੈਂਸੀ ਨੂੰ ਪ੍ਰਾਥਮਿਕਤਾ ਦੇਣ, ਇੱਕ ਇਨਫਰੰਸ ਸਟ੍ਰੀਮ ਵਰਤਣ, ਅਤੇ ਕੈਸ਼ ਡਾਇਰੈਕਟਰੀ ਨਾ ਵਰਤਣ ਲਈ ਸੈੱਟ ਕਰਦੀ ਹੈ।

4. **ਮਾਡਲ ਲੋਡ ਕਰਨਾ**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - ਇਹ ਲਾਈਨ ਮਾਡਲ ਨੂੰ ਦਿੱਤੀ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਲੋਡ ਕਰਦੀ ਹੈ, ਪਹਿਲਾਂ ਦਿੱਤੇ ਗਏ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈਟਿੰਗਜ਼ ਨਾਲ। ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਰਿਮੋਟ ਕੋਡ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਦੀ ਆਗਿਆ ਵੀ ਦਿੰਦੀ ਹੈ।

5. **ਟੋਕਨਾਈਜ਼ਰ ਲੋਡ ਕਰਨਾ**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - ਇਹ ਲਾਈਨ ਟੋਕਨਾਈਜ਼ਰ ਲੋਡ ਕਰਦੀ ਹੈ, ਜੋ ਟੈਕਸਟ ਨੂੰ ਮਾਡਲ ਲਈ ਸਮਝਣ ਯੋਗ ਟੋਕਨਾਂ ਵਿੱਚ ਬਦਲਦਾ ਹੈ।

6. **ਟੋਕਨਾਈਜ਼ਰ ਲਈ ਆਰਗੁਮੈਂਟ ਸੈੱਟ ਕਰਨਾ**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - ਇਹ ਡਿਕਸ਼ਨਰੀ ਦਰਸਾਉਂਦੀ ਹੈ ਕਿ ਵਿਸ਼ੇਸ਼ ਟੋਕਨ ਟੋਕਨਾਈਜ਼ਡ ਆਉਟਪੁੱਟ ਵਿੱਚ ਨਾ ਜੋੜੇ ਜਾਣ।

7. **ਪ੍ਰਾਂਪਟ ਦੀ ਪਰਿਭਾਸ਼ਾ ਕਰਨਾ**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - ਇਹ ਸਟਰਿੰਗ ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਾਂਪਟ ਸੈੱਟ ਕਰਦੀ ਹੈ ਜਿੱਥੇ ਯੂਜ਼ਰ AI ਸਹਾਇਕ ਨੂੰ ਆਪਣੇ ਬਾਰੇ ਜਾਣੂ ਕਰਾਉਣ ਲਈ ਕਹਿੰਦਾ ਹੈ।

8. **ਪ੍ਰਾਂਪਟ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਨਾ**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - ਇਹ ਲਾਈਨ ਪ੍ਰਾਂਪਟ ਨੂੰ ਉਹਨਾਂ ਟੋਕਨਾਂ ਵਿੱਚ ਬਦਲਦੀ ਹੈ ਜੋ ਮਾਡਲ ਸਮਝ ਸਕਦਾ ਹੈ, ਅਤੇ ਨਤੀਜਾ PyTorch ਟੈਂਸਰ ਦੇ ਰੂਪ ਵਿੱਚ ਦਿੰਦੀ ਹੈ।

9. **ਜਵਾਬ ਬਣਾਉਣਾ**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - ਇਹ ਲਾਈਨ ਮਾਡਲ ਨੂੰ ਇਨਪੁੱਟ ਟੋਕਨਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਜਵਾਬ ਬਣਾਉਣ ਲਈ ਵਰਤਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਵੱਧ ਤੋਂ ਵੱਧ 1024 ਨਵੇਂ ਟੋਕਨ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ।

10. **ਜਵਾਬ ਡੀਕੋਡ ਕਰਨਾ**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - ਇਹ ਲਾਈਨ ਬਣਾਏ ਗਏ ਟੋਕਨਾਂ ਨੂੰ ਮਨੁੱਖੀ ਪੜ੍ਹਨ ਯੋਗ ਸਟਰਿੰਗ ਵਿੱਚ ਬਦਲਦੀ ਹੈ, ਕਿਸੇ ਵੀ ਵਿਸ਼ੇਸ਼ ਟੋਕਨਾਂ ਨੂੰ ਛੱਡ ਕੇ, ਅਤੇ ਪਹਿਲਾ ਨਤੀਜਾ ਪ੍ਰਾਪਤ ਕਰਦੀ ਹੈ।

**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।