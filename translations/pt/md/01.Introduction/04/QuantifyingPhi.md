<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:45:36+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "pt"
}
-->
# **Quantificação da Família Phi**

A quantificação de modelos refere-se ao processo de mapear os parâmetros (como pesos e valores de ativação) de um modelo de rede neural de um intervalo de valores grande (normalmente um intervalo contínuo) para um intervalo finito menor. Esta tecnologia pode reduzir o tamanho e a complexidade computacional do modelo, além de melhorar a eficiência operacional em ambientes com recursos limitados, como dispositivos móveis ou sistemas embutidos. A quantificação do modelo alcança compressão ao reduzir a precisão dos parâmetros, mas também introduz alguma perda de precisão. Por isso, no processo de quantificação, é necessário equilibrar o tamanho do modelo, a complexidade computacional e a precisão. Métodos comuns de quantificação incluem quantificação em ponto fixo, quantificação em ponto flutuante, entre outros. Pode escolher a estratégia de quantificação adequada conforme o cenário e as necessidades específicas.

Pretendemos implementar modelos GenAI em dispositivos edge e permitir que mais dispositivos entrem em cenários GenAI, como dispositivos móveis, AI PC/Copilot+PC e dispositivos IoT tradicionais. Através do modelo quantificado, podemos implementá-lo em diferentes dispositivos edge conforme o dispositivo. Combinado com o framework de aceleração de modelos e o modelo quantificado fornecido pelos fabricantes de hardware, podemos construir melhores cenários de aplicação SLM.

No cenário de quantificação, temos diferentes precisões (INT4, INT8, FP16, FP32). A seguir, uma explicação das precisões de quantificação mais comuns.

### **INT4**

A quantificação INT4 é um método radical que quantifica os pesos e valores de ativação do modelo em inteiros de 4 bits. A quantificação INT4 geralmente resulta numa maior perda de precisão devido ao intervalo de representação mais pequeno e à menor precisão. No entanto, comparada com a quantificação INT8, a INT4 pode reduzir ainda mais os requisitos de armazenamento e a complexidade computacional do modelo. Deve notar-se que a quantificação INT4 é relativamente rara em aplicações práticas, pois a precisão demasiado baixa pode causar uma degradação significativa no desempenho do modelo. Além disso, nem todo o hardware suporta operações INT4, pelo que a compatibilidade do hardware deve ser considerada ao escolher o método de quantificação.

### **INT8**

A quantificação INT8 é o processo de converter os pesos e ativações de um modelo de números em ponto flutuante para inteiros de 8 bits. Embora o intervalo numérico representado pelos inteiros INT8 seja menor e menos preciso, pode reduzir significativamente os requisitos de armazenamento e cálculo. Na quantificação INT8, os pesos e valores de ativação do modelo passam por um processo de quantificação, incluindo escalamento e deslocamento, para preservar o máximo possível a informação original em ponto flutuante. Durante a inferência, estes valores quantificados são desquantificados de volta para números em ponto flutuante para cálculo, e depois quantificados novamente para INT8 para a etapa seguinte. Este método pode fornecer precisão suficiente na maioria das aplicações, mantendo alta eficiência computacional.

### **FP16**

O formato FP16, ou seja, números em ponto flutuante de 16 bits (float16), reduz pela metade a memória usada em comparação com números em ponto flutuante de 32 bits (float32), o que traz vantagens significativas em aplicações de deep learning em larga escala. O formato FP16 permite carregar modelos maiores ou processar mais dados dentro das mesmas limitações de memória da GPU. À medida que o hardware moderno de GPU continua a suportar operações FP16, o uso deste formato pode também trazer melhorias na velocidade de cálculo. No entanto, o formato FP16 tem desvantagens inerentes, nomeadamente menor precisão, o que pode levar a instabilidade numérica ou perda de precisão em alguns casos.

### **FP32**

O formato FP32 oferece maior precisão e pode representar com exatidão uma ampla gama de valores. Em cenários onde são realizadas operações matemáticas complexas ou onde são necessários resultados de alta precisão, o formato FP32 é preferido. Contudo, a alta precisão implica maior uso de memória e maior tempo de cálculo. Para modelos de deep learning em larga escala, especialmente quando existem muitos parâmetros e uma grande quantidade de dados, o formato FP32 pode causar insuficiência de memória na GPU ou diminuição da velocidade de inferência.

Em dispositivos móveis ou dispositivos IoT, podemos converter modelos Phi-3.x para INT4, enquanto AI PC / Copilot PC podem usar precisões mais elevadas como INT8, FP16, FP32.

Atualmente, diferentes fabricantes de hardware têm frameworks distintos para suportar modelos generativos, como OpenVINO da Intel, QNN da Qualcomm, MLX da Apple e CUDA da Nvidia, entre outros, combinados com a quantificação de modelos para realizar a implementação local.

Em termos tecnológicos, temos diferentes suportes de formato após a quantificação, como formatos PyTorch / Tensorflow, GGUF e ONNX. Fiz uma comparação de formatos e cenários de aplicação entre GGUF e ONNX. Aqui recomendo o formato de quantificação ONNX, que tem bom suporte desde o framework do modelo até ao hardware. Neste capítulo, vamos focar-nos no ONNX Runtime para GenAI, OpenVINO e Apple MLX para realizar a quantificação de modelos (se tiver uma forma melhor, pode também enviá-la através de um PR).

**Este capítulo inclui**

1. [Quantificação de Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantificação de Phi-3.5 / 4 usando extensões Generative AI para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantificação de Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantificação de Phi-3.5 / 4 usando Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.