<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:08:07+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "my"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

ဒီကုဒ်က OpenVINO ဖော်မတ်အတွက် မော်ဒယ်တစ်ခုကို export လုပ်ပြီး၊ ထိုမော်ဒယ်ကို load လုပ်ကာ ပေးထားသော prompt အပေါ် အဖြေတစ်ခု ထုတ်ပေးရန် အသုံးပြုပါတယ်။

1. **မော်ဒယ် Export လုပ်ခြင်း**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - ဒီ command က `optimum-cli` tool ကို အသုံးပြုပြီး OpenVINO ဖော်မတ်အတွက် မော်ဒယ် export လုပ်တာဖြစ်ပြီး၊ inference လုပ်ရာမှာ ထိရောက်မှုရှိအောင် optimize လုပ်ထားပါတယ်။
   - Export လုပ်မယ့် မော်ဒယ်က `"microsoft/Phi-3-mini-4k-instruct"` ဖြစ်ပြီး၊ ယခင် context အပေါ် အခြေခံပြီး စာသားထုတ်ပေးရန် အတွက် ပြင်ဆင်ထားတာဖြစ်ပါတယ်။
   - မော်ဒယ်၏ အလေးချိန်များကို 4-bit integer (`int4`) အဖြစ် quantize လုပ်ထားပြီး၊ ဒါက မော်ဒယ်အရွယ်အစား လျော့နည်းစေပြီး လုပ်ဆောင်မှု မြန်ဆန်စေပါတယ်။
   - `group-size`, `ratio`, `sym` စတဲ့ အခြား parameter တွေက quantization လုပ်ငန်းစဉ်ကို ပိုမိုတိကျစွာ ပြင်ဆင်ဖို့ အသုံးပြုပါတယ်။
   - Export လုပ်ပြီးတဲ့ မော်ဒယ်ကို `./model/phi3-instruct/int4` ဖိုလ်ဒါထဲ သိမ်းဆည်းထားပါတယ်။

2. **လိုအပ်သော 라이ဘရရီများ Import လုပ်ခြင်း**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - ဒီလိုင်းတွေက `transformers` 라이ဘရရီနဲ့ `optimum.intel.openvino` module မှ class တွေကို import လုပ်တာဖြစ်ပြီး မော်ဒယ်ကို load လုပ်ပြီး အသုံးပြုဖို့လိုအပ်ပါတယ်။

3. **မော်ဒယ် ဖိုလ်ဒါနဲ့ configuration သတ်မှတ်ခြင်း**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` က မော်ဒယ်ဖိုင်တွေ သိမ်းဆည်းထားတဲ့နေရာကို ဖော်ပြပါတယ်။
   - `ov_config` က OpenVINO မော်ဒယ်ကို latency နည်းအောင်၊ inference stream တစ်ခုသာ သုံးအောင်၊ cache directory မသုံးအောင် စီစဉ်ထားတဲ့ dictionary ဖြစ်ပါတယ်။

4. **မော်ဒယ် Load လုပ်ခြင်း**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - ဒီလိုင်းက သတ်မှတ်ထားတဲ့ ဖိုလ်ဒါမှ မော်ဒယ်ကို load လုပ်ပြီး၊ အထက်မှာ သတ်မှတ်ထားတဲ့ configuration ကို အသုံးပြုပါတယ်။ လိုအပ်ရင် remote code execution ကိုလည်း ခွင့်ပြုထားပါတယ်။

5. **Tokenizer Load လုပ်ခြင်း**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - ဒီလိုင်းက စာသားကို မော်ဒယ်နားလည်နိုင်တဲ့ token များအဖြစ် ပြောင်းပေးတဲ့ tokenizer ကို load လုပ်တာဖြစ်ပါတယ်။

6. **Tokenizer အတွက် argument များ သတ်မှတ်ခြင်း**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - ဒီ dictionary က tokenized output မှာ special token မထည့်ဖို့ သတ်မှတ်ထားတာဖြစ်ပါတယ်။

7. **Prompt သတ်မှတ်ခြင်း**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - ဒီ string က user က AI assistant ကို မိတ်ဆက်ပေးဖို့ တောင်းဆိုတဲ့ စကားပြော prompt တစ်ခု ဖြစ်ပါတယ်။

8. **Prompt ကို Tokenize လုပ်ခြင်း**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - ဒီလိုင်းက prompt ကို မော်ဒယ်နားလည်နိုင်တဲ့ token များအဖြစ် ပြောင်းပြီး PyTorch tensor အဖြစ် ပြန်ပေးပါတယ်။

9. **အဖြေ ထုတ်ပေးခြင်း**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - ဒီလိုင်းက input token များအပေါ် အခြေခံပြီး မော်ဒယ်ကို အသုံးပြုပြီး အဖြေ ထုတ်ပေးတာဖြစ်ပြီး၊ အများဆုံး 1024 token အသစ် ထုတ်ပေးနိုင်ပါတယ်။

10. **အဖြေကို Decode လုပ်ခြင်း**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - ဒီလိုင်းက ထုတ်ပေးထားတဲ့ token များကို လူနားလည်နိုင်တဲ့ စာသားအဖြစ် ပြန်ပြောင်းပြီး special token များကို ကျော်သွားကာ ပထမဆုံး ရလဒ်ကို ရယူပါတယ်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။