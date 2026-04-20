[គំរូ OpenVino Chat](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

កូដនេះនាំចេញម៉ូឌែលទៅទ្រង់ទាយ OpenVINO, ផ្ទុកវា, ហើយប្រើវាដើម្បីបង្កើតចម្លើយចំពោះ prompt ដែលបានផ្តល់។

1. **ការនាំចេញម៉ូឌែល**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - ពាក្យបញ្ជានេះប្រើឧបករណ៍ `optimum-cli` ដើម្បីនាំចេញម៉ូឌែលទៅទ្រង់ទាយ OpenVINO ដែលបានបង្កើតឲ្យសមរម្យសម្រាប់ការបញ្ចេញលទ្ធផល (inference) យ៉ាងមានប្រសិទ្ធភាព។
   - ម៉ូឌែលដែលកំពុងនាំចេញគឺ `"microsoft/Phi-3-mini-4k-instruct"`, ហើយវាត្រូវបានរៀបចំសម្រាប់ភារកិច្ចបង្កើតអត្ថបទដោយផ្អែកលើបរិបទមុន។
   - ទម្ងន់ម៉ូឌែលត្រូវបានកំណត់ជាចំនួនពេញ 4-ប៊ីត (`int4`), ដែលជួយកាត់បន្ថយទំហំនៃម៉ូឌែល និងលឿនបន្ថែមដំណើរការ។
   - ប៉ារ៉ាម៉ែត្រ​ផ្សេងៗដូចជា `group-size`, `ratio`, និង `sym` ត្រូវបានប្រើសម្រាប់កែលម្អដំណើរការ quantization។
   - ម៉ូឌែលដែលបាននាំចេញត្រូវបានរក្សាទុកនៅក្នុងថត `./model/phi3-instruct/int4`។

2. **ការនាំចូលបណ្ណាល័យដែលត្រូវការ**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - បន្ទាត់ទាំងនេះនាំចូលថ្នាក់ពីបណ្ណាល័យ `transformers` និងម៉ូឌុល `optimum.intel.openvino` ដែលចាំបាច់សម្រាប់ផ្ទុកនិងប្រើម៉ូឌែល។

3. **ការកំណត់ថតម៉ូឌែលនិងកំណត់រចនាសម្ព័ន្ធ**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` បញ្ជាក់ទីតាំងដែលឯកសារម៉ូឌែលត្រូវបានរក្សាទុក។
   - `ov_config` គឺជាdictionary ដែលកំណត់ម៉ូឌែល OpenVINO ដើម្បីផ្តល់អាទិភាពលើការពន្យារពេលទាប (low latency), ប្រើច្រក inference មួយ, និងមិនប្រើថត cache។

4. **ការផ្ទុកម៉ូឌែល**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - បន្ទាត់នេះផ្ទុកម៉ូឌែលពីថតដែលបានកំណត់ ដោយប្រើការកំណត់រចនាសម្ព័ន្ធដែលបានកំណត់មុន។ វានិងអនុញ្ញាតឲ្យមានការប្រតិបត្តិកូដពីចម្ងាយ (remote code execution) ប្រសិនបើចាំបាច់។

5. **ការផ្ទុក Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - បន្ទាត់នេះផ្ទុក tokenizer ដែលទទួលបន្ទុកក្នុងការបម្លែងអត្ថបទទៅជា token ដែលម៉ូឌែលអាចយល់បាន។

6. **ការកំណត់អាគុយម៉ង់សម្រាប់ Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - អង្គធាតុនេះបញ្ជាក់ថា token ពិសេសមិនគួរត្រូវបានបន្ថែមចូលទៅក្នុងលទ្ធផលដែលបាន tokenize។

7. **ការកំណត់ Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - ខ្សែអក្សរនេះកំណត់ prompt សម្រាប់ការសន្ទនាដែលអ្នកប្រើស្នើឱ្យជំនួយករ AI នាំមកណែនាំខ្លួន។

8. **ការបំបែក Prompt ទៅជា Token**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - បន្ទាត់នេះបម្លែង prompt ទៅជា token ដែលម៉ូឌែលអាចដំណើរការ ហើយផ្តល់ជាលទ្ធផលជា PyTorch tensors។

9. **ការបង្កើតចម្លើយ**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - បន្ទាត់នេះប្រើម៉ូឌែលដើម្បីបង្កើតចម្លើយដោយផ្អែកលើ token បញ្ចូល ដោយមានកំណត់អតិបរមា 1024 token ថ្មី។

10. **ការបកស្រាយចម្លើយ**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - បន្ទាត់នេះបំលែង token ដែលបានបង្កើតឡើងវិញទៅជាខ្សែអក្សរដែលអាចអានដោយមនុស្ស បិទការបង្ហាញ token ពិសេសណាមួយ ហើយយកលទ្ធផលទីមួយ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខំធ្វើឲ្យបានត្រឹមត្រូវក៏ដោយ សូមយកចិត្តទុកដាក់ថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមិនច្បាស់លាស់។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានយកចិត្តទុកដាក់ថាជាប្រភពផ្លូវការ។ សម្រាប់ព័ត៌មានសំខាន់ណាស់ យើងសូមណែនាំឲ្យបកប្រែក្នុងសុីវិលដោយអ្នកបកប្រែវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->