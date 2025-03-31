<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-03-27T09:21:29+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_OpenVino_Chat.md",
  "language_code": "ar"
}
-->
[عينة OpenVino Chat](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

هذا الكود يقوم بتصدير نموذج إلى صيغة OpenVINO، تحميله، واستخدامه لتوليد استجابة لطلب معين.

1. **تصدير النموذج**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - هذا الأمر يستخدم `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **استيراد المكتبات اللازمة**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - هذه الأسطر تستورد الفئات من وحدة `transformers` library and the `optimum.intel.openvino`، اللازمة لتحميل واستخدام النموذج.

3. **إعداد دليل النموذج والتكوين**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` هو قاموس يضبط نموذج OpenVINO لإعطاء الأولوية للزمن المنخفض للتنفيذ، استخدام تدفق استدلال واحد، وعدم استخدام دليل ذاكرة التخزين المؤقت.

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
   - هذا السطر يقوم بتحميل النموذج من الدليل المحدد باستخدام إعدادات التكوين المعرفة مسبقاً. كما يسمح بتنفيذ الكود عن بُعد إذا لزم الأمر.

5. **تحميل الـ Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - هذا السطر يقوم بتحميل الـ Tokenizer المسؤول عن تحويل النصوص إلى رموز يمكن للنموذج فهمها.

6. **إعداد معاملات الـ Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - هذا القاموس يحدد أنه لا ينبغي إضافة رموز خاصة إلى المخرجات المرمزة.

7. **تعريف الطلب**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - هذه السلسلة النصية تعد طلب محادثة حيث يطلب المستخدم من المساعد الذكي أن يقدم نفسه.

8. **ترميز الطلب**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - هذا السطر يحول الطلب إلى رموز يمكن للنموذج معالجتها، ويعيد النتيجة كموترات PyTorch.

9. **توليد استجابة**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - هذا السطر يستخدم النموذج لتوليد استجابة بناءً على الرموز المدخلة، بحد أقصى 1024 رمز جديد.

10. **فك ترميز الاستجابة**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - هذا السطر يحول الرموز المولدة إلى سلسلة نصية قابلة للقراءة، متجاهلاً أي رموز خاصة، ويسترجع النتيجة الأولى.

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق. للحصول على معلومات حيوية، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.