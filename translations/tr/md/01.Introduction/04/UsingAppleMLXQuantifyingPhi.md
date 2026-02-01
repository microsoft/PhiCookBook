# **Apple MLX Framework ile Phi-3.5 Kuantizasyonu**

MLX, Apple silikon üzerinde makine öğrenimi araştırmaları için Apple makine öğrenimi araştırması tarafından geliştirilen bir dizi framework'tür.

MLX, makine öğrenimi araştırmacıları tarafından makine öğrenimi araştırmacıları için tasarlanmıştır. Framework kullanıcı dostu olacak şekilde tasarlanmış, ancak modelleri eğitmek ve dağıtmak için yine de verimli olmayı hedeflemektedir. Framework'ün tasarımı da kavramsal olarak basittir. Amacımız, araştırmacıların MLX'i kolayca genişletip geliştirebilmesini sağlayarak yeni fikirleri hızlıca keşfetmelerine olanak tanımaktır.

LLM'ler Apple Silicon cihazlarda MLX aracılığıyla hızlandırılabilir ve modeller yerel olarak çok rahat bir şekilde çalıştırılabilir.

Şimdi Apple MLX Framework, Phi-3.5-Instruct(**Apple MLX Framework desteği**), Phi-3.5-Vision(**MLX-VLM Framework desteği**) ve Phi-3.5-MoE(**Apple MLX Framework desteği**) modellerinin kuantizasyon dönüşümünü desteklemektedir. Hadi deneyelim:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Apple MLX ile Phi-3.5 için Örnekler**

| Laboratuvarlar    | Tanıtım | Git |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instruct Tanıtımı  | Apple MLX framework ile Phi-3.5 Instruct nasıl kullanılır öğrenin   |  [Git](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (görüntü) Tanıtımı | Apple MLX framework ile Phi-3.5 Vision kullanarak görüntü analizi yapmayı öğrenin     |  [Git](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (moE) Tanıtımı   | Apple MLX framework ile Phi-3.5 MoE nasıl kullanılır öğrenin  |  [Git](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Kaynaklar**

1. Apple MLX Framework hakkında bilgi edinin [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Deposu [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Deposu [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.