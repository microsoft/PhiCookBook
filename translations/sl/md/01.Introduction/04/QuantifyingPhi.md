<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:40:44+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sl"
}
-->
# **Phi Family ke Matra**

Model quantization ka matlab hai neural network model ke parameters (jaise weights aur activation values) ko ek bade value range (aksar continuous value range) se chhote aur seemit value range mein map karna. Yeh technique model ke size aur computational complexity ko kam karti hai aur mobile devices ya embedded systems jaise resource-sankuchit environments mein model ki operating efficiency badhati hai. Model quantization parameters ki precision kam karke compression prapt karta hai, lekin isse thodi accuracy ki chhoot bhi hoti hai. Isliye quantization process mein model size, computational complexity, aur precision ke beech santulan banana zaroori hota hai. Common quantization methods mein fixed-point quantization, floating-point quantization shamil hain. Aap apne specific scenario aur zaroorat ke hisaab se upyukt quantization strategy chun sakte hain.

Hum GenAI model ko edge devices par deploy karna chahte hain taaki adhik devices GenAI scenarios mein shamil ho sakein, jaise mobile devices, AI PC/Copilot+PC, aur traditional IoT devices. Quantization model ke madhyam se hum ise alag-alag edge devices par deploy kar sakte hain, alag devices ke hisaab se. Hardware manufacturers dwara diye gaye model acceleration framework aur quantization model ke saath milkar, hum behtar SLM application scenarios tayar kar sakte hain.

Quantization scenario mein, humare paas alag-alag precisions hain (INT4, INT8, FP16, FP32). Neeche aam taur par upyog hone wali quantization precisions ka varnan hai.

### **INT4**

INT4 quantization ek atyadhik quantization method hai jo model ke weights aur activation values ko 4-bit integers mein convert karta hai. INT4 quantization mein precision ka loss zyada hota hai kyunki iska representation range chhota aur precision kam hota hai. Lekin INT8 ke mukable, INT4 quantization model ke storage aur computational complexity ko aur bhi kam kar sakta hai. Dhyan rahe ki practical applications mein INT4 quantization kam hi hota hai, kyunki bahut kam accuracy se model ki performance bahut gir sakti hai. Saath hi, sabhi hardware INT4 operations ko support nahi karte, isliye quantization method chunne se pehle hardware compatibility ka dhyan rakhna zaroori hai.

### **INT8**

INT8 quantization mein model ke weights aur activations ko floating point numbers se 8-bit integers mein badla jata hai. INT8 integers ka numerical range chhota aur precision kam hota hai, lekin yeh storage aur calculation ki maang ko bahut kam kar deta hai. INT8 quantization mein weights aur activations scaling aur offset ke zariye quantize kiye jate hain taaki original floating point information zyada se zyada bani rahe. Inference ke dauran, yeh quantized values phir se floating point mein dequantize hoti hain calculation ke liye, aur agle kadam ke liye dobara INT8 mein quantize ki jati hain. Yeh method adhiktar applications mein paryapt accuracy aur uchit computational efficiency pradan karta hai.

### **FP16**

FP16 format, yaani 16-bit floating point numbers (float16), 32-bit floating point numbers (float32) ke mukable memory ka aadha upyog karta hai, jo bade deep learning applications mein mahatvapurn fayda hai. FP16 format se aap bade models load kar sakte hain ya adhik data process kar sakte hain, wahi GPU memory ki seema mein. Aadhunik GPU hardware FP16 operations ko support karta hai, jisse computing speed mein bhi sudhar ho sakta hai. Lekin FP16 ka apna ek nuksan hai - iska precision kam hota hai, jo kuch cases mein numerical instability ya precision loss la sakta hai.

### **FP32**

FP32 format adhik precision deta hai aur wide range ke values ko accurately represent karta hai. Jab complex mathematical operations ki zaroorat ho ya high-precision results chahiye ho, tab FP32 format pasand kiya jata hai. Lekin zyada accuracy ka matlab zyada memory istemal aur lambi calculation time bhi hota hai. Bade deep learning models mein, jahan parameters aur data bahut adhik ho, FP32 format GPU memory ki kami ya inference speed mein girawat ka karan ban sakta hai.

Mobile devices ya IoT devices par, hum Phi-3.x models ko INT4 mein convert kar sakte hain, jabki AI PC / Copilot PC jaise devices higher precision jaise INT8, FP16, FP32 ka upyog kar sakte hain.

Aajkal alag hardware manufacturers ke paas generative models ke liye alag frameworks hain, jaise Intel ka OpenVINO, Qualcomm ka QNN, Apple ka MLX, aur Nvidia ka CUDA, jo model quantization ke saath milkar local deployment poora karte hain.

Technology ke roop mein, quantization ke baad humare paas alag format support hote hain, jaise PyTorch / Tensorflow format, GGUF, aur ONNX. Maine GGUF aur ONNX ke beech format comparison aur application scenarios kiye hain. Yahan main ONNX quantization format recommend karta hoon, jiska model framework se lekar hardware tak achha support hai. Is adhyaay mein, hum ONNX Runtime for GenAI, OpenVINO, aur Apple MLX ka upyog karte hue model quantization par kendrit rahenge (agar aapke paas koi behtar tareeka ho to PR ke zariye humein de sakte hain).

**Is adhyaay mein shamil hain**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku naj velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.