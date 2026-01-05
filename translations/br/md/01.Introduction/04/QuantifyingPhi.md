<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T03:05:49+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "br"
}
-->
# **Quantificando a Família Phi**

A quantização de modelo refere-se ao processo de mapear os parâmetros (como pesos e valores de ativação) em um modelo de rede neural de uma ampla faixa de valores (geralmente uma faixa contínua) para uma faixa finita menor. Essa tecnologia pode reduzir o tamanho e a complexidade computacional do modelo e melhorar a eficiência de operação do modelo em ambientes com recursos limitados, como dispositivos móveis ou sistemas embarcados. A quantização de modelo alcança compressão reduzindo a precisão dos parâmetros, mas também introduz certa perda de precisão. Portanto, no processo de quantização, é necessário equilibrar o tamanho do modelo, a complexidade computacional e a precisão. Métodos comuns de quantização incluem quantização de ponto fixo, quantização de ponto flutuante, etc. Você pode escolher a estratégia de quantização apropriada de acordo com o cenário específico e as necessidades.

Esperamos implantar modelos GenAI em dispositivos de borda e permitir que mais dispositivos entrem em cenários GenAI, como dispositivos móveis, AI PC/Copilot+PC e dispositivos tradicionais de IoT. Por meio do modelo quantizado, podemos implantá-lo em diferentes dispositivos de borda com base nos diferentes dispositivos. Combinado com o framework de aceleração de modelos e o modelo quantizado fornecido pelos fabricantes de hardware, podemos construir melhores cenários de aplicação SLM.

No cenário de quantização, temos diferentes precisões (INT4, INT8, FP16, FP32). A seguir está uma explicação das precisões de quantização comumente usadas

### **INT4**

A quantização INT4 é um método de quantização agressivo que quantiza os pesos e os valores de ativação do modelo em inteiros de 4 bits. A quantização INT4 geralmente resulta em uma perda de precisão maior devido à faixa de representação menor e à precisão reduzida. No entanto, em comparação com a quantização INT8, a quantização INT4 pode reduzir ainda mais os requisitos de armazenamento e a complexidade computacional do modelo. Deve-se observar que a quantização INT4 é relativamente rara em aplicações práticas, pois precisão muito baixa pode causar degradação significativa no desempenho do modelo. Além disso, nem todo hardware suporta operações INT4, portanto a compatibilidade de hardware precisa ser considerada ao escolher um método de quantização.

### **INT8**

A quantização INT8 é o processo de converter os pesos e ativações de um modelo de números de ponto flutuante para inteiros de 8 bits. Embora a faixa numérica representada por inteiros INT8 seja menor e menos precisa, ela pode reduzir significativamente os requisitos de armazenamento e cálculo. Na quantização INT8, os pesos e valores de ativação do modelo passam por um processo de quantização, incluindo escalonamento e deslocamento, para preservar ao máximo as informações originais em ponto flutuante. Durante a inferência, esses valores quantizados serão desquantizados de volta para números de ponto flutuante para cálculo e então quantizados novamente para INT8 para a etapa seguinte. Esse método pode fornecer precisão suficiente na maioria das aplicações, mantendo alta eficiência computacional.

### **FP16**

O formato FP16, isto é, números de ponto flutuante de 16 bits (float16), reduz a ocupação de memória pela metade em comparação com números de ponto flutuante de 32 bits (float32), o que traz vantagens significativas em aplicações de deep learning em larga escala. O formato FP16 permite carregar modelos maiores ou processar mais dados dentro das mesmas limitações de memória da GPU. À medida que o hardware de GPU moderno continua a oferecer suporte a operações em FP16, o uso do formato FP16 também pode trazer melhorias na velocidade de computação. No entanto, o formato FP16 também tem suas desvantagens inerentes, ou seja, menor precisão, o que pode levar à instabilidade numérica ou perda de precisão em alguns casos.

### **FP32**

O formato FP32 fornece maior precisão e pode representar com precisão uma ampla gama de valores. Em cenários onde são realizadas operações matemáticas complexas ou são necessários resultados de alta precisão, o formato FP32 é preferido. No entanto, alta precisão também significa maior uso de memória e tempo de cálculo mais longo. Para modelos de deep learning em larga escala, especialmente quando há muitos parâmetros do modelo e uma enorme quantidade de dados, o formato FP32 pode causar insuficiência de memória da GPU ou diminuição na velocidade de inferência.

Em dispositivos móveis ou dispositivos de IoT, podemos converter modelos Phi-3.x para INT4, enquanto AI PC / Copilot PC podem usar precisão mais alta, como INT8, FP16, FP 32.

Atualmente, diferentes fabricantes de hardware têm diferentes frameworks para suportar modelos generativos, como OpenVINO da Intel, QNN da Qualcomm, MLX da Apple e CUDA da Nvidia, etc., combinados com a quantização de modelo para completar a implantação local.

Em termos de tecnologia, temos diferentes suportes de formato após a quantização, como o formato PyTorch / TensorFlow, GGUF e ONNX. Eu fiz uma comparação de formatos e cenários de aplicação entre GGUF e ONNX. Aqui eu recomendo o formato de quantização ONNX, que tem bom suporte do framework de modelos até o hardware. Neste capítulo, iremos nos concentrar no ONNX Runtime para GenAI, OpenVINO e Apple MLX para realizar a quantização de modelos (se você tiver uma maneira melhor, também pode nos enviar por meio de um PR)

**Este capítulo inclui**

1. [Quantizando Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizando Phi-3.5 / 4 usando extensões de IA Generativa para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizando Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizando Phi-3.5 / 4 usando Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Isenção de responsabilidade**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original, em seu idioma nativo, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->