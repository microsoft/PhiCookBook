<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:48:05+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ms"
}
-->
# **Quantizando Phi-3.5 usando o Apple MLX Framework**

MLX é uma estrutura de arrays para pesquisa em aprendizado de máquina no Apple silicon, desenvolvida pela equipe de pesquisa em aprendizado de máquina da Apple.

MLX foi criada por pesquisadores de aprendizado de máquina para pesquisadores da área. O framework é pensado para ser fácil de usar, mas ainda assim eficiente para treinar e implementar modelos. O design do framework é também conceitualmente simples. Nosso objetivo é facilitar para que pesquisadores possam estender e melhorar o MLX, permitindo explorar rapidamente novas ideias.

LLMs podem ser acelerados em dispositivos Apple Silicon por meio do MLX, e os modelos podem ser executados localmente de forma muito prática.

Atualmente, o Apple MLX Framework suporta a conversão de quantização do Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), e Phi-3.5-MoE (**Apple MLX Framework support**). Vamos experimentar a seguir:

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

### **🤖 Exemplos para Phi-3.5 com Apple MLX**

| Laboratórios    | Apresentação | Acessar |
| -------- | ------- |  ------- |
| 🚀 Lab-Apresentação Phi-3.5 Instruct  | Aprenda como usar Phi-3.5 Instruct com o Apple MLX framework   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Apresentação Phi-3.5 Vision (imagem) | Aprenda como usar Phi-3.5 Vision para analisar imagens com o Apple MLX framework     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Apresentação Phi-3.5 Vision (moE)   | Aprenda como usar Phi-3.5 MoE com o Apple MLX framework  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Recursos**

1. Saiba mais sobre o Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositório Apple MLX no GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositório MLX-VLM no GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.