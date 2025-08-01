<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:07:49+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "hi"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPU और RAG पैटर्न दिखाने के लिए डेमो

Phi-3.5 Onnx Hosted मॉडल के साथ RAG पैटर्न Retrieval-Augmented Generation दृष्टिकोण का उपयोग करता है, जो Phi-3.5 मॉडलों की शक्ति को ONNX होस्टिंग के साथ मिलाकर कुशल AI डिप्लॉयमेंट प्रदान करता है। यह पैटर्न डोमेन-विशिष्ट कार्यों के लिए मॉडलों को फाइन-ट्यून करने में महत्वपूर्ण है, जो गुणवत्ता, लागत-कुशलता और लंबी संदर्भ समझ का संयोजन प्रदान करता है। यह Azure AI के सूट का हिस्सा है, जो विभिन्न उद्योगों की कस्टमाइज़ेशन आवश्यकताओं को पूरा करने के लिए आसान खोज, परीक्षण और उपयोग के लिए कई मॉडलों का चयन प्रदान करता है।

## WebGPU क्या है  
WebGPU एक आधुनिक वेब ग्राफिक्स API है जिसे वेब ब्राउज़रों से सीधे डिवाइस के ग्राफिक्स प्रोसेसिंग यूनिट (GPU) तक कुशल पहुंच प्रदान करने के लिए डिज़ाइन किया गया है। इसे WebGL का उत्तराधिकारी माना जाता है, जो कई महत्वपूर्ण सुधार प्रदान करता है:

1. **आधुनिक GPUs के साथ संगतता**: WebGPU को समकालीन GPU आर्किटेक्चर के साथ सहजता से काम करने के लिए बनाया गया है, जो Vulkan, Metal, और Direct3D 12 जैसे सिस्टम API का उपयोग करता है।
2. **बेहतर प्रदर्शन**: यह सामान्य-उद्देश्य GPU गणनाओं और तेज़ ऑपरेशनों का समर्थन करता है, जिससे यह ग्राफिक्स रेंडरिंग और मशीन लर्निंग दोनों कार्यों के लिए उपयुक्त है।
3. **उन्नत फीचर्स**: WebGPU अधिक उन्नत GPU क्षमताओं तक पहुंच प्रदान करता है, जिससे अधिक जटिल और गतिशील ग्राफिक्स और गणनात्मक कार्यभार संभव होते हैं।
4. **JavaScript कार्यभार में कमी**: GPU को अधिक कार्य सौंपकर, WebGPU JavaScript पर कार्यभार को काफी कम करता है, जिससे बेहतर प्रदर्शन और स्मूथ अनुभव मिलते हैं।

WebGPU वर्तमान में Google Chrome जैसे ब्राउज़रों में समर्थित है, और अन्य प्लेटफार्मों के लिए समर्थन बढ़ाने का काम जारी है।

### 03.WebGPU  
आवश्यक पर्यावरण:

**समर्थित ब्राउज़र:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly  

### WebGPU सक्षम करें:

- Chrome/Microsoft Edge में  

`chrome://flags/#enable-unsafe-webgpu` फ्लैग को सक्षम करें।

#### अपना ब्राउज़र खोलें:  
Google Chrome या Microsoft Edge लॉन्च करें।

#### फ्लैग पेज पर जाएं:  
एड्रेस बार में `chrome://flags` टाइप करें और Enter दबाएं।

#### फ्लैग खोजें:  
पेज के ऊपर खोज बॉक्स में 'enable-unsafe-webgpu' टाइप करें।

#### फ्लैग सक्षम करें:  
परिणामों की सूची में #enable-unsafe-webgpu फ्लैग खोजें।  
इसके बगल में ड्रॉपडाउन मेनू पर क्लिक करें और Enabled चुनें।

#### ब्राउज़र पुनः प्रारंभ करें:  
फ्लैग सक्षम करने के बाद, बदलाव लागू करने के लिए ब्राउज़र को पुनः शुरू करें। पेज के नीचे दिखाई देने वाले Relaunch बटन पर क्लिक करें।

- Linux के लिए, ब्राउज़र को `--enable-features=Vulkan` के साथ लॉन्च करें।  
- Safari 18 (macOS 15) में WebGPU डिफ़ॉल्ट रूप से सक्षम है।  
- Firefox Nightly में, एड्रेस बार में about:config टाइप करें और `dom.webgpu.enabled` को true पर सेट करें।  

### Microsoft Edge के लिए GPU सेटअप  

Windows पर Microsoft Edge के लिए हाई-परफॉर्मेंस GPU सेटअप करने के चरण:

- **सेटिंग्स खोलें:** Start मेनू पर क्लिक करें और Settings चुनें।  
- **सिस्टम सेटिंग्स:** System में जाएं और फिर Display चुनें।  
- **ग्राफिक्स सेटिंग्स:** नीचे स्क्रॉल करें और Graphics settings पर क्लिक करें।  
- **ऐप चुनें:** “Choose an app to set preference” के तहत Desktop app चुनें और फिर Browse पर क्लिक करें।  
- **Edge चुनें:** Edge इंस्टॉलेशन फोल्डर (आमतौर पर `C:\Program Files (x86)\Microsoft\Edge\Application`) पर जाएं और `msedge.exe` चुनें।  
- **प्राथमिकता सेट करें:** Options पर क्लिक करें, High performance चुनें, और फिर Save पर क्लिक करें।  
यह सुनिश्चित करेगा कि Microsoft Edge बेहतर प्रदर्शन के लिए आपके हाई-परफॉर्मेंस GPU का उपयोग करे।  
- इन सेटिंग्स को लागू करने के लिए अपने कंप्यूटर को पुनः प्रारंभ करें।  

### नमूने : कृपया [इस लिंक पर क्लिक करें](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।