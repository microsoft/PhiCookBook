<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:33:16+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "fi"
}
-->
# **Phi-3:n hienosäätö Loran avulla**

Microsoftin Phi-3 Mini -kielimallin hienosäätö käyttäen [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) -menetelmää räätälöidyllä chat-ohjeistusaineistolla.

LORA auttaa parantamaan keskustelun ymmärtämistä ja vastausten generointia.

## Vaiheittainen opas Phi-3 Minin hienosäätöön:

**Tuonnit ja asetukset**

Loralib-kirjaston asennus

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Aloita tuomalla tarvittavat kirjastot, kuten datasets, transformers, peft, trl ja torch.
Määritä lokitus, jotta voit seurata koulutusprosessia.

Voit halutessasi mukauttaa joitakin kerroksia korvaamalla ne loralibilla toteutetuilla vastineilla. Tällä hetkellä tuemme vain nn.Linear, nn.Embedding ja nn.Conv2d -kerroksia. Lisäksi tuemme MergedLinear-luokkaa tilanteissa, joissa yksi nn.Linear edustaa useampaa kerrosta, kuten joissakin huomioiden qkv-projektioissa (katso Lisähuomiot).

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

Ennen koulutussilmukkaa merkitse vain LoRA-parametrit koulutettaviksi.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Tarkistuspisteen tallennuksen yhteydessä luo state_dict, joka sisältää vain LoRA-parametrit.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Kun lataat tarkistuspistettä load_state_dict-funktiolla, varmista että asetat strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nyt koulutus voi jatkua normaalisti.

**Hyperparametrit**

Määrittele kaksi sanakirjaa: training_config ja peft_config. training_config sisältää koulutuksen hyperparametrit, kuten oppimisnopeuden, eräkoot ja lokitusasetukset.

peft_config määrittelee LoRAan liittyvät parametrit, kuten rankin, dropoutin ja tehtävätyypin.

**Mallin ja tokenisoijan lataus**

Määritä polku esikoulutettuun Phi-3 -malliin (esim. "microsoft/Phi-3-mini-4k-instruct"). Konfiguroi mallin asetukset, mukaan lukien välimuistin käyttö, datatyyppi (bfloat16 sekoitetulle tarkkuudelle) ja huomiointitoteutus.

**Koulutus**

Hienosäädä Phi-3-mallia räätälöidyllä chat-ohjeistusaineistolla. Hyödynnä peft_configin LoRA-asetuksia tehokkaaseen mukautukseen. Seuraa koulutuksen etenemistä määritellyn lokitusstrategian avulla.
Arviointi ja tallennus: Arvioi hienosäädetty malli.
Tallenna tarkistuspisteitä koulutuksen aikana myöhempää käyttöä varten.

**Esimerkit**
- [Lisätietoja tämän esimerkkimuistikirjan avulla](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python-hienosäätöesimerkki](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hubin hienosäätöesimerkki LORAn kanssa](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face -mallikortin esimerkki - LORA-hienosäätö](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hubin hienosäätöesimerkki QLORAn kanssa](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.