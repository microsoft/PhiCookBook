[OpenVino చాట్ నమూనా](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

This code exports a model to the OpenVINO format, loads it, and uses it to generate a response to a given prompt. 

1. **మోడల్‌ను ఎగుమతి చేయడం**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - ఈ కమాండ్ ఒక మోడల్‌ను OpenVINO ఫార్మాట్‌కు ఎగుమతి చేయడానికి `optimum-cli` టూల్‌ను ఉపయోగిస్తుంది, ఇది సమర్థవంతమైన ఇన్ఫరెన్స్ కోసం ఆప్టిమైజ్ చేయబడింది.
   - ఎగుమతి అవుతున్న మోడల్ `"microsoft/Phi-3-mini-4k-instruct"`, మరియు ఇది గత సందర్భాన్ని ఆధారంగా టెక్స్ట్ రూపొందించే పనికి సెట్ చేయబడింది.
   - మోడల్ వెయిట్స్‌ను 4-బిట్ పూర్తి సంఖ్యలకు (`int4`) క్వాంటైజ్ చేయబడతాయి, ఇది మోడల్ పరిమాణాన్ని తగ్గించడంలో మరియు ప్రాసెసింగ్ వేగాన్ని పెంచడంలో సహాయపడుతుంది.
   - `group-size`, `ratio`, మరియు `sym` వంటి ఇతర పారామితులు క్వాంటైజేషన్ ప్రక్రియను ఫైన్-ట్యూన్ చేయడానికి ఉపయోగిస్తారు.
   - ఎగుమతి చేయబడిన మోడల్ `./model/phi3-instruct/int4` డైరెక్టరీలో సేవ్ చేయబడింది.

2. **అవసరమైన లైబ్రరీలను దిగుమతి చేయడం**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - ఈ లైన్లు మోడల్‌ను లోడ్ చేసి ఉపయోగించడానికి అవసరమైన `transformers` లైబ్రరీ మరియు `optimum.intel.openvino` మాడ్యూల్ నుండి క్లాసులను దిగుమతి చేయడానికి ఉపయోగిస్తాయి.

3. **మోడల్ డైరెక్టరీ మరియు కాన్ఫిగరేషన్ సెట్ చేయడం**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` మోడల్ ఫైళ్లు ఎక్కడ నిల్వ ఉంటాయో సూచిస్తుంది.
   - `ov_config` ఒక డిక్షనరీ, ఇది OpenVINO మోడల్‌ను తక్కువ ఆలస్యానికి ప్రాధాన్యం ఇవ్వడానికి, ఒకే ఇన్ఫరెన్స్ స్ట్రీమ్ ఉపయోగించడానికి, మరియు cache డైరెక్టరీని ఉపయోగించరాదు అని కాన్ఫిగర్ చేస్తుంది.

4. **మోడల్‌ను లోడ్ చేయడం**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - ఈ లైన్ ముందుగా నిర్వచించిన కాన్ఫిగరేషన్ సెట్టింగ్‌లను ఉపయోగించి సూచించబడిన డైరెక్టరీఈ నుండి మోడల్‌ను లోడ్ చేస్తుంది. ఇది అవసరమైతే రిమోట్ కోడ్ ఎగ్జిక్యూషన్‌కి అనుమతిస్తుంది కూడా.

5. **టోకనైజర్‌ను లోడ్ చేయడం**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - ఈ లైన్ టెక్స్ట్‌ను మోడల్ అర్థం చేసుకునే టోకెన్లుగా మార్చడాన్ని చేతబెట్టే టోకనైజర్‌ను లోడ్ చేస్తుంది.

6. **టోకనైజర్ ఆర్గ్యూమెంట్స్ సెట్ చేయడం**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - ఈ డిక్షనరీ టోకెనైజ్డ్ అవుట్‌పుట్‌లో ప్రత్యేక టోకెన్లు జోడించకూడదని నిర్దేశిస్తుంది.

7. **ప్రాంప్ట్‌ను నిర్వచించడం**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - ఈ స్ట్రింగ్ ఒక సంభాషణ ప్రాంప్ట్‌ను సెట్ చేస్తుంది, అందులో యూజర్ AI అసిస్టెంట్‌ను తన గురించి పరిచయం చేయమని అడుగుతాడు.

8. **ప్రాంప్ట్‌ను టోకనైజ్ చేయడం**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - ఈ లైన్ ప్రాంప్ట్‌ను మోడల్ ప్రాసెస్ చేయగల టోకెన్లుగా మార్చి ఫలితాన్ని PyTorch టెన్సర్స్‌గా తిరిగి ఇస్తుంది.

9. **సమాధానం ఉత్పత్తి చేయడం**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - ఈ లైన్ ఇన్‌పుట్ టోకెన్ల ఆధారంగా మోడల్‌ను ఉపయోగించి ఒక సమాధానం ఉత్పత్తి చేస్తుంది, గరిష్టంగా 1024 కొత్త టోకెన్ల వరకు.

10. **సమాధానాన్ని డీకోడ్ చేయడం**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - ఈ లైన్ ఉత్పత్తి చేసిన టోకెన్లను మానవ పఠనీయ స్ట్రింగ్‌గా మళ్లీ మార్చి, ప్రత్యేక టోకెన్లను దాటవేసి, మొదటి ఫలితాన్ని పొందుతుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటిక్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండవచ్చు. మూల భాషలో ఉన్న అసలైన డాక్యుమెంట్‌ను అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వినియోగంతో ఏర్పడే ఏవైనా అవగాహన లోపాలు లేదా తప్పుగా అర్థం చేసుకోవడంవల్ల జరిగే పరిణామాలకై మేము బాధ్యులు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->