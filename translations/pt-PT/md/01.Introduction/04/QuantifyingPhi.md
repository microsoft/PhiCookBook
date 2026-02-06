# **Quantificação da Família Phi**

A quantização de modelos refere-se ao processo de mapear os parâmetros (tais como pesos e valores de ativação) num modelo de rede neural de um intervalo de valores grande (geralmente um intervalo contínuo) para um intervalo finito mais pequeno. Esta tecnologia pode reduzir o tamanho e a complexidade computacional do modelo e melhorar a eficiência operacional do modelo em ambientes com recursos limitados, como dispositivos móveis ou sistemas embebidos. A quantização do modelo alcança compressão ao reduzir a precisão dos parâmetros, mas também introduz uma certa perda de precisão. Portanto, no processo de quantização, é necessário equilibrar o tamanho do modelo, a complexidade computacional e a precisão. Os métodos comuns de quantização incluem a quantização fixa, a quantização em ponto flutuante, etc. Pode escolher a estratégia de quantização adequada consoante o cenário e as necessidades específicas.

Esperamos poder implementar o modelo GenAI em dispositivos edge e permitir que mais dispositivos entrem em cenários GenAI, como dispositivos móveis, PC com IA / Copilot+PC e dispositivos IoT tradicionais. Através da quantização do modelo, podemos implementá-lo em diferentes dispositivos edge com base nos diferentes dispositivos. Combinado com o framework de aceleração de modelos e o modelo de quantização fornecidos pelos fabricantes de hardware, podemos construir melhores cenários de aplicação SLM.

No cenário de quantização, temos diferentes precisões (INT4, INT8, FP16, FP32). A seguir está uma explicação das precisões de quantização mais usadas.

### **INT4**

A quantização INT4 é um método radical que quantiza os pesos e valores de ativação do modelo em inteiros de 4 bits. A quantização INT4 geralmente resulta numa perda de precisão maior devido ao intervalo de representação mais pequeno e à precisão inferior. Contudo, comparada à quantização INT8, a quantização INT4 pode reduzir ainda mais os requisitos de armazenamento e a complexidade computacional do modelo. Deve notar-se que a quantização INT4 é relativamente rara em aplicações práticas, porque uma precisão demasiado baixa pode causar degradação significativa no desempenho do modelo. Além disso, nem todo o hardware suporta operações INT4, portanto, a compatibilidade do hardware precisa de ser considerada ao escolher um método de quantização.

### **INT8**

A quantização INT8 é o processo de converter os pesos e ativações de um modelo de números em ponto flutuante para inteiros de 8 bits. Embora o intervalo numérico representado pelos inteiros INT8 seja menor e menos preciso, pode reduzir significativamente os requisitos de armazenamento e cálculo. Na quantização INT8, os pesos e valores de ativação do modelo passam por um processo de quantização, incluindo escala e deslocamento, para preservar a informação original em ponto flutuante tanto quanto possível. Durante a inferência, esses valores quantizados são desquantizados para números em ponto flutuante para cálculo, e depois quantizados novamente para INT8 para o passo seguinte. Este método pode fornecer precisão suficiente na maioria das aplicações, mantendo alta eficiência computacional.

### **FP16**

O formato FP16, ou seja, números em ponto flutuante de 16 bits (float16), reduz pela metade a utilização de memória em comparação com números em ponto flutuante de 32 bits (float32), o que tem vantagens significativas em aplicações de aprendizagem profunda em grande escala. O formato FP16 permite carregar modelos maiores ou processar mais dados dentro das mesmas limitações de memória GPU. À medida que o hardware GPU moderno continua a suportar operações FP16, usar o formato FP16 pode também trazer melhorias na velocidade de computação. No entanto, o formato FP16 tem também as suas desvantagens inerentes, nomeadamente a precisão reduzida, que pode levar a instabilidade numérica ou perda de precisão em alguns casos.

### **FP32**

O formato FP32 fornece maior precisão e pode representar com precisão uma ampla gama de valores. Em cenários onde são realizadas operações matemáticas complexas ou onde se requerem resultados de alta precisão, o formato FP32 é preferido. Contudo, a alta precisão implica maior uso de memória e maior tempo de cálculo. Para modelos de aprendizagem profunda em grande escala, especialmente quando há muitos parâmetros no modelo e uma enorme quantidade de dados, o formato FP32 pode causar insuficiência de memória GPU ou diminuição da velocidade da inferência.

Em dispositivos móveis ou dispositivos IoT, podemos converter os modelos Phi-3.x para INT4, enquanto PCs com IA / Copilot PC podem usar precisões mais elevadas, como INT8, FP16 e FP32.

Atualmente, diferentes fabricantes de hardware têm diferentes frameworks para suportar modelos generativos, como OpenVINO da Intel, QNN da Qualcomm, MLX da Apple e CUDA da Nvidia, etc., combinados com quantização de modelos para completar a implementação local.

Em termos tecnológicos, temos diferentes suportes de formato após quantização, como formato PyTorch / TensorFlow, GGUF e ONNX. Fiz uma comparação de formatos e cenários de aplicação entre GGUF e ONNX. Aqui recomendo o formato de quantização ONNX, que tem bom suporte desde o framework do modelo até ao hardware. Neste capítulo, iremos focar-nos no ONNX Runtime para GenAI, OpenVINO e Apple MLX para realizar a quantização de modelos (se tiver uma forma melhor, também pode partilhá-la connosco submetendo um PR).

**Este capítulo inclui**

1. [Quantização de Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantização de Phi-3.5 / 4 usando extensões de IA generativa para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantização de Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantização de Phi-3.5 / 4 usando Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas resultantes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->