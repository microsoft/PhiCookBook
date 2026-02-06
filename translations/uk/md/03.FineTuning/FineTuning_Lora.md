# **Тонке налаштування Phi-3 з Lora**

Тонке налаштування мовної моделі Phi-3 Mini від Microsoft за допомогою [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) на кастомному наборі інструкцій для чатів.

LORA допоможе покращити розуміння діалогів та генерацію відповідей.

## Покрокова інструкція з тонкого налаштування Phi-3 Mini:

**Імпорти та налаштування**

Встановлення loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Спочатку імпортуйте необхідні бібліотеки, такі як datasets, transformers, peft, trl та torch. Налаштуйте логування для відстеження процесу тренування.

Ви можете обрати адаптацію деяких шарів, замінивши їх на аналоги, реалізовані в loralib. Наразі підтримуються лише nn.Linear, nn.Embedding та nn.Conv2d. Також підтримується MergedLinear для випадків, коли один nn.Linear представляє кілька шарів, наприклад, у деяких реалізаціях проекції qkv уваги (див. Додаткові нотатки).

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

Перед початком циклу тренування позначте як треновані лише параметри LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Під час збереження контрольної точки створюйте state_dict, що містить лише параметри LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

При завантаженні контрольної точки за допомогою load_state_dict обов’язково встановіть strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Тепер тренування може проходити у звичайному режимі.

**Гіперпараметри**

Визначте два словники: training_config та peft_config. training_config містить гіперпараметри для тренування, такі як швидкість навчання, розмір батчу та налаштування логування.

peft_config задає параметри, пов’язані з LoRA, такі як ранг, dropout та тип завдання.

**Завантаження моделі та токенізатора**

Вкажіть шлях до попередньо навченого Phi-3 (наприклад, "microsoft/Phi-3-mini-4k-instruct"). Налаштуйте параметри моделі, включно з використанням кешу, типом даних (bfloat16 для змішаної точності) та реалізацією уваги.

**Тренування**

Тонко налаштуйте модель Phi-3 на кастомному наборі інструкцій для чатів. Використовуйте параметри LoRA з peft_config для ефективної адаптації. Відстежуйте прогрес тренування за допомогою заданої стратегії логування.

Оцінка та збереження: Оцініть тонко налаштовану модель. Зберігайте контрольні точки під час тренування для подальшого використання.

**Приклади**
- [Дізнатись більше з цього прикладу ноутбука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Приклад скрипта тонкого налаштування на Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Приклад тонкого налаштування на Hugging Face Hub з LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Приклад Model Card на Hugging Face - зразок тонкого налаштування LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Приклад тонкого налаштування на Hugging Face Hub з QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.