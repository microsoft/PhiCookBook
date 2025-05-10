<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:24:10+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "br"
}
-->
# **Quantificando a Família Phi**

A quantização de modelo refere-se ao processo de mapear os parâmetros (como pesos e valores de ativação) em um modelo de rede neural de um intervalo de valores amplo (normalmente um intervalo contínuo) para um intervalo finito menor. Essa tecnologia pode reduzir o tamanho e a complexidade computacional do modelo, além de melhorar a eficiência operacional em ambientes com recursos limitados, como dispositivos móveis ou sistemas embarcados. A quantização do modelo alcança compressão ao reduzir a precisão dos parâmetros, mas também introduz certa perda de precisão. Portanto, no processo de quantização, é necessário equilibrar o tamanho do modelo, a complexidade computacional e a precisão. Métodos comuns de quantização incluem quantização em ponto fixo, quantização em ponto flutuante, entre outros. Você pode escolher a estratégia de quantização adequada conforme o cenário e as necessidades específicas.

Esperamos implantar o modelo GenAI em dispositivos de borda e permitir que mais dispositivos entrem em cenários GenAI, como dispositivos móveis, AI PC/Copilot+PC e dispositivos tradicionais de IoT. Por meio do modelo quantizado, podemos implantá-lo em diferentes dispositivos de borda conforme o dispositivo. Combinado com o framework de aceleração de modelo e o modelo quantizado fornecidos pelos fabricantes de hardware, podemos construir melhores cenários de aplicação SLM.

No cenário de quantização, temos diferentes precisões (INT4, INT8, FP16, FP32). A seguir, uma explicação das precisões de quantização mais usadas.

### **INT4**

A quantização INT4 é um método radical que quantiza os pesos e valores de ativação do modelo em inteiros de 4 bits. A quantização INT4 geralmente resulta em uma perda maior de precisão devido ao menor intervalo de representação e precisão reduzida. No entanto, comparada à quantização INT8, a INT4 pode reduzir ainda mais os requisitos de armazenamento e a complexidade computacional do modelo. Vale destacar que a quantização INT4 é relativamente rara em aplicações práticas, pois a precisão muito baixa pode causar degradação significativa no desempenho do modelo. Além disso, nem todo hardware suporta operações INT4, então a compatibilidade com o hardware deve ser considerada ao escolher o método de quantização.

### **INT8**

A quantização INT8 é o processo de converter os pesos e ativações de um modelo de números de ponto flutuante para inteiros de 8 bits. Embora o intervalo numérico representado pelos inteiros INT8 seja menor e menos preciso, isso pode reduzir significativamente os requisitos de armazenamento e cálculo. Na quantização INT8, os pesos e valores de ativação do modelo passam por um processo de quantização, incluindo escala e deslocamento, para preservar ao máximo as informações originais em ponto flutuante. Durante a inferência, esses valores quantizados são desquantizados de volta para números de ponto flutuante para cálculo e depois quantizados novamente para INT8 para a próxima etapa. Esse método oferece precisão suficiente na maioria das aplicações, mantendo alta eficiência computacional.

### **FP16**

O formato FP16, ou números de ponto flutuante de 16 bits (float16), reduz pela metade a memória usada em comparação com números de ponto flutuante de 32 bits (float32), o que traz vantagens significativas em aplicações de deep learning em larga escala. O formato FP16 permite carregar modelos maiores ou processar mais dados dentro das mesmas limitações de memória da GPU. Como os hardwares modernos de GPU continuam a oferecer suporte a operações FP16, o uso do formato FP16 pode também melhorar a velocidade de cálculo. Porém, o formato FP16 tem desvantagens inerentes, como menor precisão, que pode levar a instabilidades numéricas ou perda de precisão em alguns casos.

### **FP32**

O formato FP32 oferece maior precisão e pode representar com exatidão uma ampla gama de valores. Em cenários que envolvem operações matemáticas complexas ou que exigem resultados de alta precisão, o formato FP32 é preferido. Contudo, essa alta precisão implica maior uso de memória e maior tempo de cálculo. Para modelos de deep learning em grande escala, especialmente com muitos parâmetros e grande volume de dados, o formato FP32 pode causar insuficiência de memória na GPU ou redução na velocidade de inferência.

Em dispositivos móveis ou de IoT, podemos converter modelos Phi-3.x para INT4, enquanto AI PC / Copilot PC podem usar precisões maiores, como INT8, FP16 e FP32.

Atualmente, diferentes fabricantes de hardware possuem frameworks distintos para suportar modelos generativos, como OpenVINO da Intel, QNN da Qualcomm, MLX da Apple e CUDA da Nvidia, entre outros, combinados com quantização de modelo para realizar a implantação local.

Em termos técnicos, temos diferentes suportes de formato após a quantização, como PyTorch / Tensorflow, GGUF e ONNX. Fiz uma comparação de formatos e cenários de aplicação entre GGUF e ONNX. Aqui, recomendo o formato de quantização ONNX, que tem bom suporte desde o framework do modelo até o hardware. Neste capítulo, focaremos no ONNX Runtime para GenAI, OpenVINO e Apple MLX para realizar a quantização do modelo (se você tiver uma abordagem melhor, pode nos enviar por meio de PR).

**Este capítulo inclui**

1. [Quantizando Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizando Phi-3.5 / 4 usando extensões Generative AI para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizando Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizando Phi-3.5 / 4 usando Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.