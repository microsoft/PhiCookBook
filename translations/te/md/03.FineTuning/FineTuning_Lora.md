<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-12-21T18:04:32+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "te"
}
-->
# **Phi-3 ను Lora తో ఫైన్-ట్యూనింగ్**

Microsoft యొక్క Phi-3 Mini భాషా మోడల్‌ను కస్టమ్ చాట్ సూచన డేటాసెట్‌పై [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ఉపయోగించి ఫైన్-ట్యూన్ చేయడం.

LoRA సంభాషణా అర్ధం చేసుకోవడాన్ని మరియు ప్రతిస్పందన ఉత్పత్తిని మెరుగుపరచడంలో సహాయపడుతుంది.

## Phi-3 Mini ను ఎలా ఫైన్-ట్యూన్ చేయాలో దశల వారీ మార్గదర్శకం:

**ఇంపోర్ట్స్ మరియు సెటప్** 

loralib ఇన్‌స్టాల్ చేయడం

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets, transformers, peft, trl, మరియు torch వంటి అవసరమైన లైబ్రరీలను ఇంపోర్ట్ చేయడం ప్రారంభించండి.
ట్రైనింగ్ ప్రక్రియను ట్రాక్ చేయడానికి లాగ్ సెట్టింగ్‌ను ఏర్పాటు చేయండి.

కొన్ని లేయర్లను loralib లో అమలు చేయబడిన ప్రత్యామ్నాయాలతో మార్చి అనుకూలీకరించుకోవచ్చు. ప్రస్తుతం మేము మాత్రమే nn.Linear, nn.Embedding, మరియు nn.Conv2d ను మద్దతు ఇస్తాము. ఒకే nn.Linear ఒకటి కంటే ఎక్కువ లేయర్లను సూచించే సందర్భాలలో, ఉదాహరణకు అక్కడ qkv projection అమలులలో కనిపించేలా, మేము MergedLinear ను కూడా మద్దతు ఇస్తాము (ఇంకా వివరాలకు Additional Notes చూడండి).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

ట్రైనింగ్ లూప్ ప్రారంభించే ముందు, కేవలం LoRA పరామితులను మాత్రమే trainable గా మార్క్ చేయండి.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

చెక్‌పాయింట్ సేవ్ చేస్తున్నప్పుడు, కేవలం LoRA పరామితులు మాత్రమే ఉండే state_dict ను రూపొందించండి.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ఉపయోగించి చెక్‌పాయింట్ లోడ్ చేస్తునప్పుడు, strict=False గా సెట్ చేయడం నిర్ధారించండి.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ఇప్పుడు ట్రైనింగ్ సాధారణంగా కొనసాగించవచ్చు.

**హైపర్పరామితులు** 

రెండు డిక్షనరీలను నిర్వచించండి: training_config మరియు peft_config. training_config లో ట్రైనింగ్‌కు సంబంధించి లెర్నింగ్ రేట్, బ్యాచ్ సైజు, మరియు లాగింగ్ సెట్టింగ్స్ వంటి హైపర్పరామితులు ఉంటాయి.

peft_config లో rank, dropout, మరియు task type వంటి LoRA-సంబంధిత పరామితులను నిర్దేశిస్తుంది.

**మోడల్ మరియు టోకనైజర్ లోడింగ్** 

ప్రీ-ట్రెయిన్డ్ Phi-3 మోడల్ మార్గాన్ని నిర్దేశించండి (ఉదా., "microsoft/Phi-3-mini-4k-instruct"). క్యాష్ వినియోగం, డేటా టైప్ (మిక్స్డ్ ప్రెసిషన్ కోసం bfloat16), మరియు attention అమలు వంటి మోడల్ సెట్టింగులను కాన్ఫిగర్ చేయండి.

**ట్రైనింగ్** 

కస్టమ్ చాట్ సూచన డేటాసెట్ ఉపయోగించి Phi-3 మోడల్‌ను ఫైన్-ట్యూన్ చేయండి. సమర్థవంతమైన అనుకూలీకరణ కోసం peft_config నుండీ LoRA సెట్టింగ్స్‌ను వినియోగించండి. నిర్దేశించబడిన లాగింగ్ స్ట్రాటజీ ఉపయోగించి ట్రైనింగ్ పురోగతిని మానిటర్ చేయండి।
మూల్యాంకనం మరియు భద్రపరచడం: ఫైన్-ట్యూన్ చేయబడిన మోడల్‌ను మూల్యాంకనం చేయండి.
తరువాత ఉపయోగం కోసం ట్రైనింగ్ సమయంలో చెక్‌పాయింట్లను సేవ్ చేయండి.

**నమూనాలు**
- [ఈ నమూనా నోట్‌బుక్‌తో మరింత తెలుసుకోండి](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python ఫైన్‌ట్యూనింగ్ నమూనా](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub లో LoRA తో ఫైన్-ట్యూనింగ్ ఉదాహరణ](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face మోడల్ కార్డ్ ఉదాహరణ - LoRA ఫైన్-ట్యూనింగ్ నమూనా](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub లో QLORA తో ఫైన్-ట్యూనింగ్ ఉదాహరణ](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా ఖచ్చితత్వ లోపాలు ఉండవచ్చని దయచేసి గమనించండి. మూల భాషలో ఉన్న అసలు డాక్యుమెంట్‌ను అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, నిపుణులైన మానవ అనువాదాన్ని సిఫార్సు చేయబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించడంతో కలిగే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యులం కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->