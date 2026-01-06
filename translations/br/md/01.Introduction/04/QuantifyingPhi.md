<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T14:14:33+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "br"
}
-->
# **Quantificação da Família Phi**

A quantização de modelos refere-se ao processo de mapear os parâmetros (como pesos e valores de ativação) em um modelo de rede neural de uma ampla faixa de valores (geralmente uma faixa contínua) para uma faixa finita menor. Essa tecnologia pode reduzir o tamanho e a complexidade computacional do modelo, além de melhorar a eficiência operacional do modelo em ambientes com recursos limitados, como dispositivos móveis ou sistemas embarcados. A quantização do modelo atinge compressão reduzindo a precisão dos parâmetros, mas também introduz certa perda de precisão. Portanto, no processo de quantização, é necessário equilibrar o tamanho do modelo, a complexidade computacional e a precisão. Métodos comuns de quantização incluem quantização em ponto fixo, quantização em ponto flutuante etc. Você pode escolher a estratégia de quantização apropriada de acordo com o cenário específico e as necessidades.

Esperamos implantar modelos GenAI em dispositivos de borda e permitir que mais dispositivos entrem em cenários GenAI, como dispositivos móveis, PC de IA/Copilot+PC e dispositivos IoT tradicionais. Por meio do modelo quantizado, podemos implantá-lo em diferentes dispositivos de borda com base nos diferentes dispositivos. Combinado com a estrutura de aceleração de modelo e o modelo quantizado fornecidos pelos fabricantes de hardware, podemos construir melhores cenários de aplicação SLM.

No cenário de quantização, temos diferentes precisões (INT4, INT8, FP16, FP32). A seguir, uma explicação das precisões de quantização mais usadas.

### **INT4**

A quantização INT4 é um método radical que quantiza os pesos e valores de ativação do modelo em inteiros de 4 bits. A quantização INT4 geralmente resulta em uma perda maior de precisão devido à faixa de representação menor e à menor precisão. Contudo, comparada à quantização INT8, a quantização INT4 pode reduzir ainda mais os requisitos de armazenamento e a complexidade computacional do modelo. Deve-se notar que a quantização INT4 é relativamente rara em aplicações práticas, pois a precisão muito baixa pode causar degradação significativa no desempenho do modelo. Além disso, nem todo hardware suporta operações INT4, então a compatibilidade do hardware precisa ser considerada ao escolher um método de quantização.

### **INT8**

A quantização INT8 é o processo de converter os pesos e ativações de um modelo de números em ponto flutuante para inteiros de 8 bits. Embora a faixa numérica representada por inteiros INT8 seja menor e menos precisa, ela pode reduzir significativamente os requisitos de armazenamento e cálculo. Na quantização INT8, os pesos e valores de ativação do modelo passam por um processo de quantização, incluindo escala e deslocamento, para preservar ao máximo as informações originais em ponto flutuante. Durante a inferência, esses valores quantizados serão desquantizados de volta para números em ponto flutuante para cálculo, e então quantizados novamente para INT8 na próxima etapa. Esse método pode fornecer precisão suficiente na maioria das aplicações enquanto mantém alta eficiência computacional.

### **FP16**

O formato FP16, ou seja, números em ponto flutuante de 16 bits (float16), reduz pela metade o uso de memória em comparação aos números em ponto flutuante de 32 bits (float32), o que traz vantagens significativas em aplicações de deep learning em larga escala. O formato FP16 permite carregar modelos maiores ou processar mais dados dentro das mesmas limitações de memória da GPU. À medida que o hardware moderno de GPU continua a suportar operações FP16, o uso do formato FP16 pode também trazer melhorias na velocidade de computação. Contudo, o formato FP16 também tem suas desvantagens inerentes, como menor precisão, o que pode levar a instabilidade numérica ou perda de precisão em alguns casos.

### **FP32**

O formato FP32 oferece maior precisão e pode representar com exatidão uma ampla faixa de valores. Em cenários onde operações matemáticas complexas são realizadas ou resultados de alta precisão são requeridos, o formato FP32 é preferido. No entanto, alta precisão também significa mais uso de memória e maior tempo de cálculo. Para modelos de deep learning em larga escala, especialmente quando há muitos parâmetros de modelo e grande quantidade de dados, o formato FP32 pode causar insuficiência de memória na GPU ou redução na velocidade de inferência.

Em dispositivos móveis ou dispositivos IoT, podemos converter modelos Phi-3.x para INT4, enquanto PCs de IA / Copilot PC podem usar precisão mais alta como INT8, FP16, FP32.

Atualmente, diferentes fabricantes de hardware possuem diferentes estruturas para suportar modelos generativos, como o OpenVINO da Intel, o QNN da Qualcomm, o MLX da Apple e o CUDA da Nvidia etc., combinados com a quantização de modelo para completar a implantação local.

Em termos de tecnologia, temos diferentes formatos suportados após a quantização, como formatos PyTorch / TensorFlow, GGUF e ONNX. Fiz uma comparação de formatos e dos cenários de aplicação entre GGUF e ONNX. Aqui recomendo o formato de quantização ONNX, que tem bom suporte desde o framework do modelo até o hardware. Neste capítulo, focaremos no ONNX Runtime para GenAI, OpenVINO e Apple MLX para realizar a quantização do modelo (se você tiver uma forma melhor, pode também nos enviar por meio de PR).

**Este capítulo inclui**

1. [Quantizando Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizando Phi-3.5 / 4 usando extensões de IA Generativa para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizando Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizando Phi-3.5 / 4 usando o Framework Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->