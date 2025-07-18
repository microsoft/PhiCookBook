<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-17T10:06:31+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "tr"
}
-->
# **Apple MLX Framework ile Phi-3 Çıkarımı**

## **MLX Framework Nedir**

MLX, Apple silikon üzerinde makine öğrenimi araştırmaları için geliştirilmiş bir dizi (array) framework’üdür ve Apple makine öğrenimi araştırma ekibi tarafından sunulmaktadır.

MLX, makine öğrenimi araştırmacıları tarafından makine öğrenimi araştırmacıları için tasarlanmıştır. Framework kullanıcı dostu olacak şekilde planlanmış, ancak modelleri eğitmek ve dağıtmak için yine de verimli çalışması hedeflenmiştir. Framework’ün tasarımı da kavramsal olarak basittir. Amacımız, araştırmacıların MLX’i kolayca genişletip geliştirebilmesini sağlayarak yeni fikirleri hızlıca keşfetmelerine olanak tanımaktır.

Apple Silikon cihazlarda LLM’ler MLX ile hızlandırılabilir ve modeller yerel olarak çok rahat bir şekilde çalıştırılabilir.

## **MLX ile Phi-3-mini Çıkarımı Yapmak**

### **1. MLX ortamınızı kurun**

1. Python 3.11.x
2. MLX Kütüphanesini yükleyin


```bash

pip install mlx-lm

```

### **2. Terminalde MLX ile Phi-3-mini çalıştırma**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Sonuç (benim ortamım Apple M1 Max, 64GB) şu şekildedir:

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.tr.png)

### **3. Terminalde MLX ile Phi-3-mini’yi Kuantize Etme**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Model mlx_lm.convert ile kuantize edilebilir ve varsayılan kuantizasyon INT4’tür. Bu örnekte Phi-3-mini INT4’e kuantize edilmektedir.

Model mlx_lm.convert ile kuantize edilebilir ve varsayılan kuantizasyon INT4’tür. Bu örnek Phi-3-mini’yi INT4’e kuantize etmeyi göstermektedir. Kuantizasyondan sonra model varsayılan dizin olan ./mlx_model içine kaydedilecektir.

Terminalden MLX ile kuantize edilmiş modeli test edebiliriz.


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Sonuç şu şekildedir:

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.tr.png)


### **4. Jupyter Notebook’ta MLX ile Phi-3-mini çalıştırma**


![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.tr.png)

***Note:*** Lütfen bu örneği okuyun [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Kaynaklar**

1. Apple MLX Framework hakkında bilgi edinin [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Deposu [https://github.com/ml-explore](https://github.com/ml-explore)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.