<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:58:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "tl"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ang code na ito ay nag-e-export ng modelo sa OpenVINO format, naglo-load nito, at ginagamit ito para gumawa ng sagot sa ibinigay na prompt.

1. **Pag-export ng Modelo**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Ginagamit ng command na ito ang `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Pag-import ng Mga Kailangan na Library**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Ini-import ng mga linyang ito ang mga klase mula sa `transformers` library and the `optimum.intel.openvino` module, na kailangan para i-load at gamitin ang modelo.

3. **Pagsesetup ng Model Directory at Configuration**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - Ang `model_dir` specifies where the model files are stored.
   - `ov_config` ay isang dictionary na nagko-configure sa OpenVINO model para unahin ang mababang latency, gumamit ng isang inference stream, at huwag gumamit ng cache directory.

4. **Pag-load ng Modelo**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Ini-load ng linyang ito ang modelo mula sa tinukoy na directory gamit ang mga configuration settings na na-define kanina. Pinapayagan din nito ang remote code execution kung kinakailangan.

5. **Pag-load ng Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Ini-load ng linyang ito ang tokenizer, na responsable sa pag-convert ng teksto sa mga token na maiintindihan ng modelo.

6. **Pagsesetup ng Tokenizer Arguments**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Itong dictionary ay nagsasaad na hindi dapat magdagdag ng special tokens sa tokenized output.

7. **Pag-define ng Prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Itong string ay nagse-set ng conversation prompt kung saan tinatanong ng user ang AI assistant na ipakilala ang sarili nito.

8. **Pag-tokenize ng Prompt**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Kinokonvert ng linyang ito ang prompt sa mga token na kayang i-process ng modelo, at ibinabalik ang resulta bilang PyTorch tensors.

9. **Pag-generate ng Sagot**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Ginagamit ng linyang ito ang modelo para gumawa ng sagot base sa input tokens, na may maximum na 1024 bagong token.

10. **Pag-decode ng Sagot**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Kinokonvert ng linyang ito ang mga generated tokens pabalik sa isang madaling basahing string, iniiwasan ang mga special tokens, at kinukuha ang unang resulta.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak ang pagsasalin, pakatandaan na maaaring may mga pagkakamali o di-katiyakan ang mga awtomatikong pagsasalin. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.