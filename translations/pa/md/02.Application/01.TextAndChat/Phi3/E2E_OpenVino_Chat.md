<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:03:33+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "pa"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

ਇਹ ਕੋਡ ਇੱਕ ਮਾਡਲ ਨੂੰ OpenVINO ਫਾਰਮੈਟ ਵਿੱਚ ਐਕਸਪੋਰਟ ਕਰਦਾ ਹੈ, ਇਸਨੂੰ ਲੋਡ ਕਰਦਾ ਹੈ, ਅਤੇ ਦਿੱਤੇ ਗਏ ਪ੍ਰਾਂਪਟ ਲਈ ਜਵਾਬ ਤਿਆਰ ਕਰਨ ਲਈ ਇਸਦਾ ਉਪਯੋਗ ਕਰਦਾ ਹੈ।

1. **ਮਾਡਲ ਐਕਸਪੋਰਟ ਕਰਨਾ**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - ਇਹ ਕਮਾਂਡ `optimum-cli` ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਡਲ ਨੂੰ OpenVINO ਫਾਰਮੈਟ ਵਿੱਚ ਐਕਸਪੋਰਟ ਕਰਦੀ ਹੈ, ਜੋ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਇੰਫਰੈਂਸ ਲਈ ਅਨੁਕੂਲਿਤ ਹੈ।
   - ਐਕਸਪੋਰਟ ਕੀਤਾ ਜਾ ਰਿਹਾ ਮਾਡਲ `"microsoft/Phi-3-mini-4k-instruct"` ਹੈ, ਜੋ ਪਿਛਲੇ ਸੰਦਰਭ ਦੇ ਆਧਾਰ 'ਤੇ ਟੈਕਸਟ ਬਣਾਉਣ ਦੇ ਕੰਮ ਲਈ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੈ।
   - ਮਾਡਲ ਦੇ ਵਜ਼ਨ 4-ਬਿਟ ਇੰਟੀਜਰ (`int4`) ਵਿੱਚ ਕਵਾਂਟਾਈਜ਼ ਕੀਤੇ ਗਏ ਹਨ, ਜੋ ਮਾਡਲ ਦਾ ਆਕਾਰ ਘਟਾਉਂਦੇ ਹਨ ਅਤੇ ਪ੍ਰੋਸੈਸਿੰਗ ਨੂੰ ਤੇਜ਼ ਕਰਦੇ ਹਨ।
   - ਹੋਰ ਪੈਰਾਮੀਟਰ ਜਿਵੇਂ `group-size`, `ratio`, ਅਤੇ `sym` ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।
   - ਐਕਸਪੋਰਟ ਕੀਤਾ ਮਾਡਲ ਡਾਇਰੈਕਟਰੀ `./model/phi3-instruct/int4` ਵਿੱਚ ਸੇਵ ਕੀਤਾ ਗਿਆ ਹੈ।

2. **ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕਰਨਾ**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - ਇਹ ਲਾਈਨਾਂ `transformers` ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ `optimum.intel.openvino` ਮੋਡੀਊਲ ਤੋਂ ਕਲਾਸਾਂ ਇੰਪੋਰਟ ਕਰਦੀਆਂ ਹਨ, ਜੋ ਮਾਡਲ ਨੂੰ ਲੋਡ ਅਤੇ ਵਰਤਣ ਲਈ ਜ਼ਰੂਰੀ ਹਨ।

3. **ਮਾਡਲ ਡਾਇਰੈਕਟਰੀ ਅਤੇ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈੱਟ ਕਰਨਾ**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` ਦੱਸਦਾ ਹੈ ਕਿ ਮਾਡਲ ਫਾਈਲਾਂ ਕਿੱਥੇ ਸਟੋਰ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ।
   - `ov_config` ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੈ ਜੋ OpenVINO ਮਾਡਲ ਨੂੰ ਘੱਟ ਲੇਟੈਂਸੀ, ਇੱਕ ਇੰਫਰੈਂਸ ਸਟ੍ਰੀਮ ਦੀ ਵਰਤੋਂ ਅਤੇ ਕੈਸ਼ ਡਾਇਰੈਕਟਰੀ ਨਾ ਵਰਤਣ ਲਈ ਕਨਫਿਗਰ ਕਰਦੀ ਹੈ।

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
   - ਇਹ ਲਾਈਨ ਮਾਡਲ ਨੂੰ ਦਿੱਤੀ ਗਈ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਲੋਡ ਕਰਦੀ ਹੈ, ਪਹਿਲਾਂ ਦਿੱਤੇ ਗਏ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈਟਿੰਗਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ। ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਰਿਮੋਟ ਕੋਡ ਐਕਜ਼ਿਕਿਊਸ਼ਨ ਦੀ ਆਗਿਆ ਵੀ ਦਿੰਦੀ ਹੈ।

5. **ਟੋਕਨਾਈਜ਼ਰ ਲੋਡ ਕਰਨਾ**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - ਇਹ ਲਾਈਨ ਟੋਕਨਾਈਜ਼ਰ ਨੂੰ ਲੋਡ ਕਰਦੀ ਹੈ, ਜੋ ਟੈਕਸਟ ਨੂੰ ਮਾਡਲ ਲਈ ਸਮਝਣ ਯੋਗ ਟੋਕਨ ਵਿੱਚ ਬਦਲਦਾ ਹੈ।

6. **ਟੋਕਨਾਈਜ਼ਰ ਦੇ ਆਰਗੁਮੈਂਟ ਸੈੱਟ ਕਰਨਾ**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - ਇਹ ਡਿਕਸ਼ਨਰੀ ਦੱਸਦੀ ਹੈ ਕਿ ਵਿਸ਼ੇਸ਼ ਟੋਕਨ ਟੋਕਨਾਈਜ਼ਡ ਆਉਟਪੁੱਟ ਵਿੱਚ ਸ਼ਾਮਲ ਨਹੀਂ ਕਰਨੇ।

7. **ਪ੍ਰਾਂਪਟ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - ਇਹ ਸਟਰਿੰਗ ਇੱਕ ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਾਂਪਟ ਸੈੱਟ ਕਰਦੀ ਹੈ ਜਿੱਥੇ ਯੂਜ਼ਰ AI ਸਹਾਇਕ ਨੂੰ ਆਪਣੇ ਬਾਰੇ ਜਾਣੂ ਕਰਾਉਣ ਲਈ ਕਹਿੰਦਾ ਹੈ।

8. **ਪ੍ਰਾਂਪਟ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਨਾ**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - ਇਹ ਲਾਈਨ ਪ੍ਰਾਂਪਟ ਨੂੰ ਮਾਡਲ ਲਈ ਸਮਝਣ ਯੋਗ ਟੋਕਨਾਂ ਵਿੱਚ ਬਦਲਦੀ ਹੈ, ਅਤੇ ਨਤੀਜਾ PyTorch ਟੈਂਸਰਾਂ ਵਜੋਂ ਵਾਪਸ ਕਰਦੀ ਹੈ।

9. **ਜਵਾਬ ਤਿਆਰ ਕਰਨਾ**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - ਇਹ ਲਾਈਨ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁੱਟ ਟੋਕਨਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਜਵਾਬ ਤਿਆਰ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਵੱਧ ਤੋਂ ਵੱਧ 1024 ਨਵੇਂ ਟੋਕਨ ਸ਼ਾਮਲ ਹਨ।

10. **ਜਵਾਬ ਡੀਕੋਡ ਕਰਨਾ**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - ਇਹ ਲਾਈਨ ਤਿਆਰ ਕੀਤੇ ਗਏ ਟੋਕਨਾਂ ਨੂੰ ਮੁੜ ਮਨੁੱਖੀ ਪੜ੍ਹਨ ਯੋਗ ਸਟਰਿੰਗ ਵਿੱਚ ਬਦਲਦੀ ਹੈ, ਵਿਸ਼ੇਸ਼ ਟੋਕਨਾਂ ਨੂੰ ਛੱਡ ਕੇ, ਅਤੇ ਪਹਿਲਾ ਨਤੀਜਾ ਪ੍ਰਾਪਤ ਕਰਦੀ ਹੈ।

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।