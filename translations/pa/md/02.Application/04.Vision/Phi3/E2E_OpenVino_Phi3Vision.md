<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:02:37+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "pa"
}
-->
ਇਹ ਡੈਮੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਸ ਤਰ੍ਹਾਂ ਇੱਕ ਪ੍ਰੀ-ਟ੍ਰੇਨਡ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਚਿੱਤਰ ਅਤੇ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਦੇ ਆਧਾਰ 'ਤੇ Python ਕੋਡ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

ਇੱਥੇ ਕਦਮ-ਦਰ-ਕਦਮ ਵਿਆਖਿਆ ਦਿੱਤੀ ਗਈ ਹੈ:

1. **ਇੰਪੋਰਟ ਅਤੇ ਸੈਟਅਪ**:
   - ਜਰੂਰੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਅਤੇ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ `requests`, ਚਿੱਤਰ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ `PIL`, ਅਤੇ ਮਾਡਲ ਅਤੇ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ `transformers`।

2. **ਚਿੱਤਰ ਲੋਡ ਕਰਨਾ ਅਤੇ ਦਿਖਾਉਣਾ**:
   - ਇੱਕ ਚਿੱਤਰ ਫਾਇਲ (`demo.png`) `PIL` ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਨਾਲ ਖੋਲੀ ਜਾਂਦੀ ਹੈ ਅਤੇ ਦਿਖਾਈ ਜਾਂਦੀ ਹੈ।

3. **ਪ੍ਰਾਂਪਟ ਦੀ ਪਰਿਭਾਸ਼ਾ**:
   - ਇੱਕ ਸੁਨੇਹਾ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਚਿੱਤਰ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ ਅਤੇ Python ਕੋਡ ਬਣਾਉਣ ਦੀ ਬੇਨਤੀ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਜੋ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਕੇ `plt` (matplotlib) ਦੀ ਵਰਤੋਂ ਨਾਲ ਸੇਵ ਕਰੇ।

4. **ਪ੍ਰੋਸੈਸਰ ਲੋਡ ਕਰਨਾ**:
   - `AutoProcessor` ਨੂੰ ਪ੍ਰੀ-ਟ੍ਰੇਨਡ ਮਾਡਲ ਤੋਂ ਲੋਡ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜੋ `out_dir` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਹੈ। ਇਹ ਪ੍ਰੋਸੈਸਰ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ ਇਨਪੁੱਟ ਨੂੰ ਸੰਭਾਲੇਗਾ।

5. **ਪ੍ਰਾਂਪਟ ਬਣਾਉਣਾ**:
   - `apply_chat_template` ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੁਨੇਹੇ ਨੂੰ ਮਾਡਲ ਲਈ ਉਚਿਤ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਬਦਲਿਆ ਜਾਂਦਾ ਹੈ।

6. **ਇਨਪੁੱਟ ਪ੍ਰੋਸੈਸ ਕਰਨਾ**:
   - ਪ੍ਰਾਂਪਟ ਅਤੇ ਚਿੱਤਰ ਨੂੰ ਟੈਂਸਰਾਂ ਵਿੱਚ ਬਦਲਿਆ ਜਾਂਦਾ ਹੈ ਜੋ ਮਾਡਲ ਸਮਝ ਸਕਦਾ ਹੈ।

7. **ਜਨਰੇਸ਼ਨ ਆਰਗੁਮੈਂਟ ਸੈੱਟ ਕਰਨਾ**:
   - ਮਾਡਲ ਦੀ ਜਨਰੇਸ਼ਨ ਪ੍ਰਕਿਰਿਆ ਲਈ ਆਰਗੁਮੈਂਟ ਤੈਅ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ ਨਵੇਂ ਟੋਕਨ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਗਿਣਤੀ ਅਤੇ ਆਉਟਪੁੱਟ ਨੂੰ ਸੈਂਪਲ ਕਰਨਾ ਹੈ ਜਾਂ ਨਹੀਂ।

8. **ਕੋਡ ਜਨਰੇਟ ਕਰਨਾ**:
   - ਮਾਡਲ ਇਨਪੁੱਟ ਅਤੇ ਜਨਰੇਸ਼ਨ ਆਰਗੁਮੈਂਟ ਦੇ ਆਧਾਰ 'ਤੇ Python ਕੋਡ ਬਣਾਉਂਦਾ ਹੈ। `TextStreamer` ਦੀ ਵਰਤੋਂ ਆਉਟਪੁੱਟ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਪ੍ਰਾਂਪਟ ਅਤੇ ਖਾਸ ਟੋਕਨ ਛੱਡ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ।

9. **ਆਉਟਪੁੱਟ**:
   - ਬਣਾਇਆ ਗਿਆ ਕੋਡ ਪ੍ਰਿੰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਉਹ Python ਕੋਡ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਜੋ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਕੇ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਦਿੱਤੇ ਅਨੁਸਾਰ ਸੇਵ ਕਰਦਾ ਹੈ।

ਇਹ ਡੈਮੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਸ ਤਰ੍ਹਾਂ OpenVino ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਪ੍ਰੀ-ਟ੍ਰੇਨਡ ਮਾਡਲ ਨੂੰ ਯੂਜ਼ਰ ਇਨਪੁੱਟ ਅਤੇ ਚਿੱਤਰਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਡਾਇਨਾਮਿਕ ਤੌਰ 'ਤੇ ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।