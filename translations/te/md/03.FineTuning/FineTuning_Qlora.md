<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-12-21T17:18:19+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "te"
}
-->
**Phi-3 ను QLoRA తో ఫైన్-ట్యూనింగ్**

Microsoft యొక్క Phi-3 Mini భాషా మోడల్‌ను [QLoRA (క్వాంటం లో-ర్యాంక్ అనుకరణ)](https://github.com/artidoro/qlora) ఉపయోగించి ఫైన్-ట్యూన్ చేయడం.

QLoRA సంభాషణాత్మక అవగాహన మరియు ప్రతిస్పందన ఉత్పత్తిని మెరుగుపరచడంలో సహాయపడుతుంది.

To load models in 4bits with transformers and bitsandbytes, you have to install accelerate and transformers from source and make sure you have the latest version of the bitsandbytes library.

**నమూనాలు**
- [ఈ నమూనా నోట్‌బుక్‌తో మరింత తెలుసుకోండి](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python ఫైన్‌ట్యూనింగ్ నమూనా ఉదాహరణ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub తో LORA ఉపయోగించి ఫైన్-ట్యూనింగ్ ఉదాహరణ](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub తో QLORA ఉపయోగించి ఫైన్-ట్యూనింగ్ ఉదాహరణ](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యత మినహాయింపు:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, స్వయంచాలక అనువాదాల్లో పొరపాట్లు లేదా తప్పులుండచ్చు కాబట్టి దయచేసి గమనించండి. మూల పత్రాన్ని దాని స్థానిక భాషలోని అసలు దస్త్రాన్ని అధికారిక మూలంగా పరిగణించాలి. కీలక సమాచారానికి వృత్తిపరమైన మానవ అనువాదాన్ని సూచిస్తాం. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితప్పుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->