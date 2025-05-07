<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-07T11:05:08+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "ar"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

يقوم هذا الكود بتصدير نموذج إلى صيغة OpenVINO، ثم تحميله، واستخدامه لتوليد رد على موجه معين.

1. **تصدير النموذج**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - يستخدم هذا الأمر `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **استيراد المكتبات اللازمة**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - تستورد هذه الأسطر الأصناف من الوحدة `transformers` library and the `optimum.intel.openvino`، والتي تُستخدم لتحميل النموذج واستخدامه.

3. **إعداد مجلد النموذج والتهيئة**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` هي قاموس يضبط نموذج OpenVINO ليعطي أولوية لانخفاض زمن الاستجابة، ويستخدم تدفق استنتاج واحد، ولا يستخدم مجلد ذاكرة مؤقتة.

4. **تحميل النموذج**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - يقوم هذا السطر بتحميل النموذج من المجلد المحدد، باستخدام إعدادات التهيئة المعرفّة سابقًا. كما يسمح بتنفيذ كود عن بُعد إذا لزم الأمر.

5. **تحميل أداة الترميز (Tokenizer)**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - يقوم هذا السطر بتحميل أداة الترميز المسؤولة عن تحويل النص إلى رموز يفهمها النموذج.

6. **إعداد معطيات أداة الترميز**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - يحدد هذا القاموس أنه لا يجب إضافة رموز خاصة إلى المخرجات المرمزة.

7. **تعريف الموجه**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - يحدد هذا النص موجه محادثة يطلب فيه المستخدم من المساعد الذكي تقديم نفسه.

8. **ترميز الموجه**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - يحول هذا السطر الموجه إلى رموز يمكن للنموذج معالجتها، ويُرجع النتيجة كموترات PyTorch.

9. **توليد الرد**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - يستخدم هذا السطر النموذج لتوليد رد بناءً على الرموز المدخلة، مع حد أقصى 1024 رمزًا جديدًا.

10. **فك ترميز الرد**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - يحول هذا السطر الرموز المولدة إلى نص مقروء للبشر، متجاوزًا أي رموز خاصة، ويسترجع النتيجة الأولى.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.