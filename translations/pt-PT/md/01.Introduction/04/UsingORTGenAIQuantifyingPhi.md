# **Quantização da Família Phi usando extensões de IA Generativa para onnxruntime**

## **O que são as extensões de IA Generativa para onnxruntime**

Estas extensões ajudam a executar IA generativa com ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Fornecem o ciclo de IA generativa para modelos ONNX, incluindo inferência com ONNX Runtime, processamento de logits, pesquisa e amostragem, e gestão do cache KV. Os desenvolvedores podem chamar um método de alto nível generate(), ou executar cada iteração do modelo numa loop, gerando um token de cada vez, e opcionalmente atualizando parâmetros de geração dentro do ciclo. Suportam busca gulosa/beam e amostragem TopP, TopK para gerar sequências de tokens e processamento de logits incorporado como penalizações de repetição. Também pode adicionar facilmente pontuações personalizadas.

Ao nível da aplicação, pode usar as extensões de IA Generativa para onnxruntime para construir aplicações usando C++/ C# / Python. Ao nível do modelo, pode usá-las para fundir modelos afinados e realizar trabalhos relacionados com implantação quantitativa.


## **Quantização do Phi-3.5 com as extensões de IA Generativa para onnxruntime**

### **Modelos Suportados**

As extensões de IA Generativa para onnxruntime suportam conversão de quantização dos modelos Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Construtor de Modelos nas extensões de IA Generativa para onnxruntime**

O construtor de modelos acelera bastante a criação de modelos ONNX otimizados e quantizados que correm com a API generate() do ONNX Runtime.

Através do Construtor de Modelos, pode quantizar o modelo para INT4, INT8, FP16, FP32, e combinar diferentes métodos de aceleração de hardware como CPU, CUDA, DirectML, Mobile, etc.

Para usar o Construtor de Modelos precisa de instalar

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Após a instalação, pode executar o script do Construtor de Modelos a partir do terminal para realizar a conversão do formato e quantização do modelo.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Compreenda os parâmetros relevantes

1. **model_name** Este é o modelo no Hugging face, como microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Pode também ser o caminho onde guarda o modelo

2. **path_to_output_folder** Caminho onde é guardada a conversão quantizada

3. **execution_provider** Suporte a diferentes acelerações de hardware, como cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Nós descarregamos o modelo do Hugging face e fazemos cache localmente




***Nota：*** <ul>Embora as extensões de IA Generativa para onnxruntime estejam em pré-visualização, já foram incorporadas no Microsoft Olive, e também pode chamar funções do Construtor de Modelos das extensões de IA Generativa para onnxruntime através do Microsoft Olive.</ul>

## **Como usar o Construtor de Modelos para quantizar Phi-3.5**

O Construtor de Modelos suporta agora a quantização de modelos ONNX para Phi-3.5 Instruct e Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Conversão acelerada por CPU de INT4 quantizado**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversão acelerada por CUDA de INT4 quantizado**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Defina o ambiente no terminal

```bash

mkdir models

cd models 

```

2. Descarregue microsoft/Phi-3.5-vision-instruct na pasta models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Por favor, descarregue estes ficheiros para a sua pasta Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Descarregue este ficheiro para a pasta models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Vá ao terminal

    Converter suporte ONNX com FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Nota：**

1. O Construtor de Modelos suporta atualmente a conversão de Phi-3.5-Instruct e Phi-3.5-Vision, mas não Phi-3.5-MoE

2. Para usar o modelo quantizado ONNX, pode utilizá-lo através do SDK das extensões de IA Generativa para onnxruntime

3. Precisamos de considerar uma IA mais responsável, por isso depois da conversão da quantização do modelo, recomenda-se realizar testes mais eficazes de resultados

4. Ao quantizar o modelo CPU INT4, podemos implantá-lo em dispositivos Edge, que têm melhores cenários de aplicação, por isso completámos o Phi-3.5-Instruct em torno do INT4


## **Recursos**

1. Saiba mais sobre as extensões de IA Generativa para onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositório GitHub das extensões de IA Generativa para onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->