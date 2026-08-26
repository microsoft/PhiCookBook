# **Quantizando a Família Phi usando extensões de IA Generativa para onnxruntime**

## **O que são extensões de IA Generativa para onnxruntime**

Essas extensões ajudam você a executar IA generativa com o ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Elas fornecem o loop de IA generativa para modelos ONNX, incluindo inferência com ONNX Runtime, processamento de logits, busca e amostragem, e gerenciamento de cache KV. Desenvolvedores podem chamar um método de alto nível generate(), ou executar cada iteração do modelo em um loop, gerando um token por vez e, opcionalmente, atualizando parâmetros de geração dentro do loop. Suporta busca gulosa/beam e amostragem TopP, TopK para gerar sequências de tokens, e processamento de logits embutido como penalidades de repetição. Você também pode facilmente adicionar pontuação personalizada.

No nível da aplicação, você pode usar as extensões de IA Generativa para onnxruntime para construir aplicações usando C++ / C# / Python. No nível do modelo, você pode usá-las para mesclar modelos ajustados e realizar trabalho quantitativo relacionado ao deployment.


## **Quantizando Phi-3.5 com extensões de IA Generativa para onnxruntime**

### **Modelos suportados**

As extensões de IA Generativa para onnxruntime suportam conversão de quantização dos modelos Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Construtor de Modelo nas extensões de IA Generativa para onnxruntime**

O construtor de modelo acelera significativamente a criação de modelos ONNX otimizados e quantizados que rodem com a API generate() do ONNX Runtime.

Através do Construtor de Modelo, você pode quantizar o modelo para INT4, INT8, FP16, FP32, e combinar diferentes métodos de aceleração de hardware como CPU, CUDA, DirectML, Mobile, etc.

Para usar o Construtor de Modelo você precisa instalar

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Após a instalação, você pode executar o script do Construtor de Modelo pelo terminal para realizar a conversão de formato e quantização do modelo.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Entenda os parâmetros relevantes

1. **model_name** Este é o modelo no Hugging Face, como microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Também pode ser o caminho onde você armazena o modelo

2. **path_to_output_folder** Caminho para salvar a conversão quantizada

3. **execution_provider** Suporte a diferentes acelerações de hardware, como cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Local onde o modelo baixado do Hugging Face é cacheado localmente




***Nota:*** <ul>Embora as extensões de IA Generativa para onnxruntime estejam em preview, elas já foram incorporadas ao Microsoft Olive, e você também pode chamar as funções do Construtor de Modelo dessas extensões pela Microsoft Olive.</ul>

## **Como usar o Construtor de Modelo para quantizar Phi-3.5**

O Construtor de Modelo atualmente suporta quantização do modelo ONNX para Phi-3.5 Instruct e Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Conversão acelerada por CPU do quantizado INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversão acelerada por CUDA do quantizado INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configure o ambiente no terminal

```bash

mkdir models

cd models 

```

2. Baixe microsoft/Phi-3.5-vision-instruct na pasta models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Por favor, baixe esses arquivos para sua pasta Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Baixe este arquivo para a pasta models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Vá para o terminal

    Converta o suporte ONNX com FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Nota:**

1. O Construtor de Modelo atualmente suporta a conversão de Phi-3.5-Instruct e Phi-3.5-Vision, mas não Phi-3.5-MoE

2. Para usar o modelo quantizado do ONNX, você pode usá-lo através do SDK das extensões de IA Generativa para onnxruntime

3. Precisamos considerar IA responsável, então após a conversão de quantização do modelo, é recomendado realizar testes mais eficazes dos resultados

4. Quantizando o modelo CPU INT4, podemos implantá-lo em dispositivos Edge, que têm melhores cenários de aplicação, por isso completamos Phi-3.5-Instruct em torno do INT 4


## **Recursos**

1. Saiba mais sobre extensões de IA Generativa para onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositório GitHub das extensões de IA Generativa para onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->