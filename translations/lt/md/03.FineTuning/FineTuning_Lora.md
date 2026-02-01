# **Phi-3 modelio pritaikymas naudojant Lora**

Microsoft Phi-3 Mini kalbos modelio pritaikymas naudojant [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) pagal individualų pokalbių instrukcijų duomenų rinkinį.

LoRA padės pagerinti pokalbių supratimą ir atsakymų generavimą.

## Žingsnis po žingsnio vadovas, kaip pritaikyti Phi-3 Mini:

**Importavimas ir nustatymas**

Loralib diegimas

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Pradėkite importuodami reikalingas bibliotekas, tokias kaip datasets, transformers, peft, trl ir torch. Nustatykite žurnalavimą, kad galėtumėte stebėti mokymo procesą.

Galite pasirinkti pritaikyti kai kuriuos sluoksnius, pakeisdami juos loralib įgyvendintais analogais. Šiuo metu palaikome tik nn.Linear, nn.Embedding ir nn.Conv2d. Taip pat palaikome MergedLinear, kai vienas nn.Linear atspindi daugiau nei vieną sluoksnį, pavyzdžiui, kai kuriose dėmesio qkv projekcijos įgyvendinimuose (žr. Papildomas pastabas).

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

Prieš pradedant mokymo ciklą, pažymėkite tik LoRA parametrus kaip treniruojamus.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Išsaugant kontrolinį tašką, sukurkite state_dict, kuriame yra tik LoRA parametrai.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Įkeliant kontrolinį tašką naudojant load_state_dict, būtinai nustatykite strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Dabar mokymas gali vykti įprastai.

**Hiperparametrai**

Apibrėžkite du žodynus: training_config ir peft_config. training_config apima mokymo hiperparametrus, tokius kaip mokymosi greitis, partijos dydis ir žurnalavimo nustatymai.

peft_config nurodo LoRA susijusius parametrus, tokius kaip rangas, dropout ir užduoties tipas.

**Modelio ir žetonų skirstytuvo įkėlimas**

Nurodykite kelią į iš anksto apmokytą Phi-3 modelį (pvz., "microsoft/Phi-3-mini-4k-instruct"). Konfigūruokite modelio nustatymus, įskaitant talpyklos naudojimą, duomenų tipą (bfloat16 mišriam tikslumui) ir dėmesio įgyvendinimą.

**Mokymas**

Pritaikykite Phi-3 modelį naudodami individualų pokalbių instrukcijų duomenų rinkinį. Naudokite LoRA nustatymus iš peft_config efektyviam pritaikymui. Stebėkite mokymo eigą naudodami nurodytą žurnalavimo strategiją. 

Vertinimas ir išsaugojimas: Įvertinkite pritaikytą modelį. Išsaugokite kontrolinius taškus mokymo metu, kad galėtumėte juos naudoti vėliau.

**Pavyzdžiai**
- [Sužinokite daugiau su šiuo pavyzdiniu užrašų knygeliu](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python pritaikymo pavyzdys](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub pritaikymo pavyzdys su LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face modelio kortelės pavyzdys - LORA pritaikymo pavyzdys](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub pritaikymo pavyzdys su QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.