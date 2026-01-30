[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

يقوم هذا الكود بتصدير نموذج إلى صيغة OpenVINO، ثم تحميله واستخدامه لتوليد رد على موجه معين.

1. **تصدير النموذج**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - يستخدم هذا الأمر أداة `optimum-cli` لتصدير نموذج إلى صيغة OpenVINO، التي تم تحسينها لتحقيق استدلال فعال.  
   - النموذج الذي يتم تصديره هو `"microsoft/Phi-3-mini-4k-instruct"`، وهو مهيأ لمهمة توليد النص بناءً على السياق السابق.  
   - يتم تحويل أوزان النموذج إلى أعداد صحيحة 4-بت (`int4`)، مما يساعد في تقليل حجم النموذج وتسريع المعالجة.  
   - تُستخدم معلمات أخرى مثل `group-size` و `ratio` و `sym` لضبط عملية التحويل بدقة.  
   - يتم حفظ النموذج المصدر في المجلد `./model/phi3-instruct/int4`.

2. **استيراد المكتبات اللازمة**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - تستورد هذه الأسطر الفئات من مكتبة `transformers` ومن وحدة `optimum.intel.openvino`، والتي تُستخدم لتحميل النموذج واستخدامه.

3. **إعداد مجلد النموذج والتكوين**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - يحدد `model_dir` مكان تخزين ملفات النموذج.  
   - `ov_config` هو قاموس يضبط نموذج OpenVINO ليعطي أولوية لانخفاض زمن الاستجابة، ويستخدم تدفق استدلال واحد، ولا يستخدم مجلد ذاكرة مؤقتة.

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
   - يقوم هذا السطر بتحميل النموذج من المجلد المحدد، باستخدام إعدادات التكوين المعرفة سابقًا. كما يسمح بتنفيذ كود عن بُعد إذا لزم الأمر.

5. **تحميل المحلل اللغوي (Tokenizer)**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - يقوم هذا السطر بتحميل المحلل اللغوي، المسؤول عن تحويل النص إلى رموز يمكن للنموذج فهمها.

6. **إعداد معطيات المحلل اللغوي**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - يحدد هذا القاموس أنه لا يجب إضافة رموز خاصة إلى المخرجات بعد التحليل.

7. **تعريف الموجه (Prompt)**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - يحدد هذا النص موجه محادثة حيث يطلب المستخدم من المساعد الذكي أن يقدم نفسه.

8. **تحليل الموجه إلى رموز**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - يحول هذا السطر الموجه إلى رموز يمكن للنموذج معالجتها، ويعيد النتيجة على شكل موترات PyTorch.

9. **توليد الرد**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - يستخدم هذا السطر النموذج لتوليد رد بناءً على الرموز المدخلة، مع حد أقصى 1024 رمزًا جديدًا.

10. **فك تشفير الرد**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - يحول هذا السطر الرموز المولدة مرة أخرى إلى نص قابل للقراءة من قبل الإنسان، متجاوزًا أي رموز خاصة، ويسترجع النتيجة الأولى.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.