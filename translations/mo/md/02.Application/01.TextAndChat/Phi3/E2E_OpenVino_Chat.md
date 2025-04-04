<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5621d23b682762686e0eccc7ce8bd9ec",
  "translation_date": "2025-04-04T12:22:34+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_OpenVino_Chat.md",
  "language_code": "mo"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ye code model ke OpenVINO format mein export karta hai, use load karta hai, aur diye gaye prompt ke liye response generate karta hai.

1. **Model Export Karna**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ye command `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` ka use karta hai.

2. **Zaroori Libraries Import Karna**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ye lines `transformers` library and the `optimum.intel.openvino` module se classes import karti hain jo model ko load aur use karne ke liye zaroori hain.

3. **Model Directory Aur Configuration Setup Karna**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` ek dictionary hai jo OpenVINO model ko low latency prioritize karne, ek inference stream use karne, aur cache directory na use karne ke liye configure karti hai.

4. **Model Load Karna**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ye line specified directory se model ko load karti hai, jo pehle define kiye gaye configuration settings ka use karta hai. Ye remote code execution ki permission bhi deta hai agar zarurat ho.

5. **Tokenizer Load Karna**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ye line tokenizer ko load karti hai, jo text ko tokens mein convert karne ke liye responsible hai jo model samajh sake.

6. **Tokenizer Arguments Setup Karna**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ye dictionary specify karti hai ki special tokens tokenized output mein add nahi kiye jayenge.

7. **Prompt Define Karna**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ye string ek conversation prompt setup karta hai jisme user AI assistant se apne baare mein batane ke liye kehta hai.

8. **Prompt Ko Tokenize Karna**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ye line prompt ko tokens mein convert karti hai jo model process kar sake, aur result PyTorch tensors ke roop mein return karti hai.

9. **Response Generate Karna**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ye line model ka use karke input tokens ke basis par ek response generate karti hai, maximum 1024 naye tokens ke saath.

10. **Response Decode Karna**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ye line generated tokens ko wapas ek human-readable string mein convert karti hai, kisi special tokens ko skip karke, aur pehla result retrieve karti hai.

It seems you requested a translation to "mo," but could you clarify what "mo" refers to? Are you asking for translation into Maori, Mongolian, or another language? Let me know so I can assist you accurately!