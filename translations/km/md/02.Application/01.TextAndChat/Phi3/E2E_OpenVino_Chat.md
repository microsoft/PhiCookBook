[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

កូដនេះនាំចេញម៉ូដែលទៅទ្រង់ទ្រាយ OpenVINO, បង្ហាញវា, និងប្រើវា ដើម្បីបង្កើតចំលើយទៅកាន់ការបញ្ជា ដែលបានផ្តល់។

1. **ការនាំចេញម៉ូដែល**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - ពាក្យបញ្ជានេះប្រើឧបករណ៍ `optimum-cli` ដើម្បីនាំចេញម៉ូដែលទៅទ្រង់ទ្រាយ OpenVINO ដែលបានប្រសើរឡើងសម្រាប់ការប្រព្រឹត្តិការណ៍មានប្រសិទ្ធភាព។
   - ម៉ូដែលដែលត្រូវបាននាំចេញគឺ `"microsoft/Phi-3-mini-4k-instruct"` ហើយវាត្រូវបានរៀបចំសម្រាប់ភារកិច្ចបង្កើតអត្ថបទដោយផ្អែកលើបរិបទមុន។
   - ទម្ងន់ម៉ូដែលត្រូវបានបម្លែងទៅជាចំនួនគត់ 4-ប៊ីត (`int4`)， ដែលជួយកាត់បន្ថយទំហំម៉ូដែល និងលឿនក្នុងការប្រព្រឹត្ត។
   - ប៉ារ៉ាម៉ែត្រផ្សេងៗដូចជា `group-size`, `ratio`, និង `sym` ត្រូវបានប្រើសម្រាប់បញ្ចេញលម្អិតក្នុងដំណើរការបម្លែងទម្ងន់។
   - ម៉ូដែលដែលបាននាំចេញត្រូវបានរក្សាទុកនៅក្នុងថត `./model/phi3-instruct/int4`។

2. **នាំចូលបណ្ណាល័យចាំបាច់**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - បន្ទាត់ទាំងនេះនាំចូលថ្នាក់ពីបណ្ណាល័យ `transformers` និងម៉ូឌុល `optimum.intel.openvino` ដែលចាំបាច់សម្រាប់ផ្ទុក និងប្រើម៉ូដែល។

3. **កំណត់ថតម៉ូដែល និងការកំណត់រចនាសម្ព័ន្ធ**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` បញ្ជាក់ទីតាំងបណ្ណាល័យឯកសារម៉ូដែល។
   - `ov_config` ជាភាសានិមិត្តនៃការកំណត់រចនាសម្ព័ន្ធម៉ូដែល OpenVINO ដែលផ្តោតលើការថយចុះពេលវេលាពីការឆ្លើយតប, ប្រើច្រកចេញបញ្ចូលតែមួយ, និងមិនប្រើថតកាបែត។

4. **ផ្ទុកម៉ូដែល**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - បន្ទាត់នេះផ្ទុកម៉ូដែលពីថតដែលបានបញ្ជាក់ ប្រើការកំណត់រចនាសម្ព័ន្ធដែលបានកំណត់ជាមុន។ វាក៏អនុញ្ញាតឲ្យវាប្រតិបត្តិការកូដពីចម្ងាយ ប្រសិនបើចាំបាច់។

5. **ផ្ទុកកម្មវិធីផ្លាស់ប្តូរលក្ខណៈអក្សរ**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - បន្ទាត់នេះផ្ទុកកម្មវិធីផ្លាស់ប្តូរនៅលើអត្ថបទទៅជាទំនាប់ដែលម៉ូដែលអាចយល់បាន។

6. **កំណត់អាគុយម៉ង់កម្មវិធីផ្លាស់ប្តូរ**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - ភាសានិមិត្តនេះបញ្ជាក់ថា មិនត្រូវបន្ថែម​សញ្ញាពិសេសទៅកាន់លទ្ធផលដែលបានបម្លែង។

7. **កំណត់ការបញ្ជា**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - ខ្សែអក្សរនេះបង្កើតការសន្ទនាដែលអ្នកប្រើប្រាស់ស្នើឲ្យជំនួយក្រុម AI ណែនាំខ្លួនវា។

8. **បម្លែងការបញ្ជា**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - បន្ទាត់នេះបម្លែងការបញ្ជាជាទំនាប់ដែលម៉ូដែលអាចដំណើរការ ហើយត្រឡប់លទ្ធផលក្នុងទ្រង់ទ្រាយ PyTorch tensors។

9. **បង្កើតចំលើយ**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - បន្ទាត់នេះប្រើម៉ូដែល ដើម្បីបង្កើតចំលើយដោយផ្អែកលើទិន្នន័យបញ្ចូល ដែលកំណត់ទំហំនៃសញ្ញាថ្មីមិនលើស 1024។

10. **ដោះសោចំលើយ**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - បន្ទាត់នេះបម្លែងសញ្ញាដែលបានបង្កើតត្រលប់ទៅជាអក្សរដដែលមានមនុស្សអាចអានបាន ដោយមិនរាប់បញ្ចូលសញ្ញាពិសេសណាឡើយ និងយកលទ្ធផលដំបូង។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំសំរាប់ភាពត្រឹមត្រូវ សូមយល់ឱ្យបានថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមូលដ្ឋានអាចត្រូវបានកត់សម្គាល់ដូចជាឯកសារដើមដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ គេណែនាំឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែគន្លងការណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->