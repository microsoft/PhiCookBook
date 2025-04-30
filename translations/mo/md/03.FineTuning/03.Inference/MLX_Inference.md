<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "700b9a537ce4426de5a7ccfa8e96e581",
  "translation_date": "2025-04-04T13:35:46+00:00",
  "source_file": "md\\03.FineTuning\\03.Inference\\MLX_Inference.md",
  "language_code": "mo"
}
-->
# **Inference Phi-3 with Apple MLX Framework**

## **What is MLX Framework**

MLX jẹ awoṣe fun iwadi ẹrọ ẹkọ lori Apple silicon, ti a mu wa fun ọ nipasẹ iwadi ẹrọ ẹkọ Apple.

MLX jẹ apẹrẹ nipasẹ awọn oluwadi ẹrọ ẹkọ fun awọn oluwadi ẹrọ ẹkọ. Awoṣe naa jẹ ti ifọkanbalẹ olumulo, ṣugbọn o tun munadoko lati kọ ẹkọ ati ṣe agbekalẹ awọn awoṣe. Apẹrẹ ti awoṣe naa tun jẹ rọrun lati ni oye. A pinnu lati jẹ ki o rọrun fun awọn oluwadi lati faagun ati mu MLX dara pẹlu ibi-afẹde ti ṣawari awọn imọran tuntun ni kiakia.

LLMs le yara ni awọn ẹrọ Apple Silicon nipasẹ MLX, ati pe awọn awoṣe le ṣiṣẹ ni agbegbe ni irọrun pupọ.

## **Using MLX to inference Phi-3-mini**

### **1. Ṣeto agbegbe MLX rẹ**

1. Python 3.11.x
2. Fi sori MLX Library

```bash

pip install mlx-lm

```

### **2. Ṣiṣe Phi-3-mini ni Terminal pẹlu MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Abajade (agbegbe mi ni Apple M1 Max, 64GB) ni

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.mo.png)

### **3. Quantizing Phi-3-mini pẹlu MLX ni Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Akiyesi：*** Awoṣe le ṣe quantize nipasẹ mlx_lm.convert, ati pe quantization aiyipada jẹ INT4. Apẹẹrẹ yii ṣe quantize Phi-3-mini si INT4.

Awoṣe le ṣe quantize nipasẹ mlx_lm.convert, ati pe quantization aiyipada jẹ INT4. Apẹẹrẹ yii ni lati ṣe quantize Phi-3-mini sinu INT4. Lẹhin quantization, yoo wa ni fipamọ ni itọsọna aiyipada ./mlx_model.

A le ṣe idanwo awoṣe ti a ṣe quantize pẹlu MLX lati terminal.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Abajade ni

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.mo.png)

### **4. Ṣiṣe Phi-3-mini pẹlu MLX ni Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.mo.png)

***Akiyesi:*** Jọwọ ka apẹẹrẹ yii [tẹ ọna asopọ yii](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Awọn orisun**

1. Kọ ẹkọ nipa Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

It seems you are asking for a translation to "mo," but could you clarify what "mo" refers to? Are you referring to a specific language or dialect, such as Maori (mi), Montenegrin (sr-ME), or something else? Let me know so I can assist you better!