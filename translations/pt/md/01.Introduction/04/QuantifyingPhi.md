<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T02:54:40+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "pt"
}
-->
# **Quantização da família Phi**

A quantização de modelos refere-se ao processo de mapear os parâmetros (tais como pesos e valores de ativação) num modelo de rede neural de um amplo intervalo de valores (normalmente um intervalo contínuo) para um intervalo finito mais reduzido. Esta tecnologia pode reduzir o tamanho e a complexidade computacional do modelo e melhorar a eficiência de funcionamento do modelo em ambientes com recursos limitados, como dispositivos móveis ou sistemas embebidos. A quantização do modelo alcança compressão ao reduzir a precisão dos parâmetros, mas também introduz alguma perda de precisão. Portanto, no processo de quantização, é necessário equilibrar o tamanho do modelo, a complexidade computacional e a precisão. Métodos comuns de quantização incluem quantização em ponto fixo, quantização em ponto flutuante, etc. Pode escolher a estratégia de quantização apropriada de acordo com o cenário e as necessidades específicas.

Pretendemos implementar modelos GenAI em dispositivos de borda e permitir que mais dispositivos entrem nos cenários GenAI, como dispositivos móveis, AI PC/Copilot+PC e dispositivos IoT tradicionais. Através do modelo quantizado, podemos implantá-lo em diferentes dispositivos de borda consoante o dispositivo. Combinado com o framework de aceleração de modelos e o modelo quantizado fornecido pelos fabricantes de hardware, podemos construir melhores cenários de aplicação SLM.

No cenário de quantização, temos diferentes precisões (INT4, INT8, FP16, FP32). A seguir está uma explicação das precisões de quantização mais utilizadas

### **INT4**

A quantização INT4 é uma forma de quantização extrema que quantiza os pesos e os valores de ativação do modelo em inteiros de 4 bits. A quantização INT4 normalmente resulta numa perda de precisão maior devido ao intervalo de representação mais pequeno e à menor precisão. No entanto, em comparação com a quantização INT8, a quantização INT4 pode reduzir ainda mais os requisitos de armazenamento e a complexidade computacional do modelo. Deve notar-se que a quantização INT4 é relativamente rara em aplicações práticas, porque uma precisão demasiado baixa pode causar uma degradação significativa no desempenho do modelo. Além disso, nem todo o hardware suporta operações INT4, pelo que a compatibilidade de hardware precisa de ser considerada ao escolher um método de quantização.

### **INT8**

A quantização INT8 é o processo de converter os pesos e as ativações de um modelo de números de ponto flutuante para inteiros de 8 bits. Embora o intervalo numérico representado pelos inteiros INT8 seja menor e menos preciso, pode reduzir significativamente os requisitos de armazenamento e cálculo. Na quantização INT8, os pesos e os valores de ativação do modelo passam por um processo de quantização, incluindo escalamento e offset, para preservar o máximo possível a informação original em ponto flutuante. Durante a inferência, estes valores quantizados são desquantizados de volta para números em ponto flutuante para cálculo, e depois quantizados novamente para INT8 para o passo seguinte. Este método pode fornecer precisão suficiente na maioria das aplicações, mantendo uma elevada eficiência computacional.

### **FP16**

O formato FP16, isto é, números de ponto flutuante de 16 bits (float16), reduz a ocupação de memória pela metade em comparação com números de ponto flutuante de 32 bits (float32), o que tem vantagens significativas em aplicações de aprendizagem profunda à grande escala. O formato FP16 permite carregar modelos maiores ou processar mais dados dentro das mesmas limitações de memória da GPU. À medida que o hardware moderno de GPU continua a suportar operações FP16, o uso do formato FP16 pode também trazer melhorias na velocidade de cálculo. No entanto, o formato FP16 tem também desvantagens inerentes, nomeadamente a menor precisão, o que pode conduzir a instabilidade numérica ou perda de precisão em alguns casos.

### **FP32**

O formato FP32 proporciona maior precisão e pode representar com precisão uma vasta gama de valores. Em cenários onde são realizadas operações matemáticas complexas ou são necessários resultados de alta precisão, o formato FP32 é preferido. No entanto, a alta precisão também implica maior uso de memória e maior tempo de cálculo. Para modelos de aprendizagem profunda à grande escala, especialmente quando existem muitos parâmetros do modelo e uma enorme quantidade de dados, o formato FP32 pode causar insuficiência de memória na GPU ou uma diminuição da velocidade de inferência.

Em dispositivos móveis ou dispositivos IoT, podemos converter modelos Phi-3.x para INT4, enquanto que em AI PC / Copilot PC podem ser usadas precisões mais altas, como INT8, FP16, FP 32.

Atualmente, diferentes fabricantes de hardware dispõem de diferentes frameworks para suportar modelos generativos, tais como OpenVINO da Intel, QNN da Qualcomm, MLX da Apple e CUDA da Nvidia, entre outros, combinados com a quantização de modelos para realizar a implementação local.

Em termos de tecnologia, temos diferentes formatos suportados após a quantização, tais como o formato PyTorch / TensorFlow, GGUF e ONNX. Fiz uma comparação de formatos e cenários de aplicação entre GGUF e ONNX. Aqui recomendo o formato de quantização ONNX, que tem bom suporte desde o framework do modelo até ao hardware. Neste capítulo, iremos focar-nos no ONNX Runtime para GenAI, OpenVINO e Apple MLX para executar a quantização de modelos (se tiver uma forma melhor, também nos pode indicar submetendo um PR)

**Este capítulo inclui**

1. [Quantizar Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizar Phi-3.5 / 4 usando Extensões Generativas de IA para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizar Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizar Phi-3.5 / 4 usando o Framework Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido recorrendo ao serviço de tradução automática por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por obter precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua de origem, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->