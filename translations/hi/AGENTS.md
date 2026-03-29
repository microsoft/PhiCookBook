# AGENTS.md

## Project Overview

PhiCookBook माइक्रोसॉफ्ट के Phi परिवार के Small Language Models (SLMs) के साथ काम करने के लिए व्यापक कुकबुक रिपॉजिटरी है जिसमें व्यावहारिक उदाहरण, ट्यूटोरियल और दस्तावेज़ शामिल हैं। इस रिपॉजिटरी में विभिन्न उपयोग के मामले प्रदर्शित किए गए हैं जिनमें इन्फ़रेंस, फाइन-ट्यूनिंग, क्वांटाइजेशन, RAG कार्यान्वयन, और विभिन्न प्लेटफार्मों और फ्रेमवर्क के अंतर्गत मल्टीमॉडल अनुप्रयोग शामिल हैं।

**मुख्य प्रौद्योगिकियाँ:**
- **भाषाएं:** Python, C#/.NET, JavaScript/Node.js
- **फ्रेमवर्क:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **प्लेटफार्म:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **मॉडल प्रकार:** Phi-3, Phi-3.5, Phi-4 (टेक्स्ट, विज़न, मल्टीमॉडल, तर्क संस्करण)

**रिपॉजिटरी संरचना:**
- `/code/` - काम करने वाले कोड उदाहरण और नमूना कार्यान्वयन
- `/md/` - विस्तृत दस्तावेज़, ट्यूटोरियल और हाउ-टू गाइड  
- `/translations/` - बहुभाषी अनुवाद (50+ भाषाएं स्वचालित वर्कफ्लो के माध्यम से)
- `/.devcontainer/` - देव कंटेनर विन्यास (Python 3.12 सहित Ollama)

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. GitHub Codespaces में खोलें (सबसे तेज़):
   - README में "Open in GitHub Codespaces" बैज पर क्लिक करें
   - कंटेनर Python 3.12 और Phi-3 के साथ Ollama के साथ स्वचालित कॉन्फ़िगर हो जाता है

2. VS Code Dev Containers में खोलें:
   - README से "Open in Dev Containers" बैज का उपयोग करें
   - कंटेनर को न्यूनतम 16GB होस्ट मेमोरी चाहिए

### Local Setup

**पूर्वापेक्षाएँ:**
- Python 3.12 या उससे ऊपर
- .NET 8.0 SDK (C# उदाहरणों के लिए)
- Node.js 18+ और npm (JavaScript उदाहरणों के लिए)
- न्यूनतम 16GB RAM की सिफारिश

**स्थापना:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python उदाहरणों के लिए:**
विशिष्ट उदाहरण निर्देशिकाओं पर जाएं और निर्भरताएं इंस्टॉल करें:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # यदि requirements.txt मौजूद है
```

**.NET उदाहरणों के लिए:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web उदाहरणों के लिए:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # विकास सर्वर शुरू करें
npm run build  # उत्पादन के लिए निर्माण करें
```

## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - बुनियादी परिचय और शुरुआत के नमूने
- **03.Finetuning/** और **04.Finetuning/** - विभिन्न तरीकों के साथ फाइन-ट्यूनिंग उदाहरण
- **03.Inference/** - विभिन्न हार्डवेयर (AIPC, MLX) पर इन्फ़रेंस उदाहरण
- **06.E2E/** - एंड-टू-एंड एप्लीकेशन नमूने
- **07.Lab/** - लैब/प्रयोगात्मक कार्यान्वयन
- **08.RAG/** - रिट्रीवल-ऑगमेंटेड जनरेशन नमूने
- **09.UpdateSamples/** - नवीनतम अपडेट किए गए नमूने

### Documentation (`/md/`)

- **01.Introduction/** - परिचय गाइड, पर्यावरण सेटअप, प्लेटफार्म मार्गदर्शक
- **02.Application/** - प्रकार (टेक्स्ट, कोड, विज़न, ऑडियो आदि) के आधार पर एप्लीकेशन नमूने
- **02.QuickStart/** - Microsoft Foundry और GitHub Models के लिए त्वरित प्रारंभ गाइड
- **03.FineTuning/** - फाइन-ट्यूनिंग दस्तावेज़ और ट्यूटोरियल
- **04.HOL/** - हैंड्स-ऑन लैब्स (.NET उदाहरण शामिल हैं)

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - इंटरैक्टिव Python ट्यूटोरियल जिन्हें README में 📓 से चिह्नित किया गया है
- **Python Scripts (`.py`)** - स्वतंत्र Python उदाहरण
- **C# Projects (`.csproj`, `.sln`)** - .NET एप्लिकेशन और नमूने
- **JavaScript (`.js`, `package.json`)** - वेब-आधारित और Node.js उदाहरण
- **Markdown (`.md`)** - दस्तावेज़ और गाइड

## Working with Examples

### Running Jupyter Notebooks

अधिकांश उदाहरण Jupyter नोटबुक के रूप में प्रदान किए जाते हैं:
```bash
pip install jupyter notebook
jupyter notebook  # ब्राउज़र इंटरफ़ेस खोलता है
# वांछित .ipynb फ़ाइल पर नेविगेट करें
```

### Running Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Running .NET Examples

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

या पूरी सोल्यूशन बनाएँ:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Running JavaScript/Web Examples

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # हॉट रीलोड के साथ विकास
```

## Testing

यह रिपॉजिटरी पारंपरिक सॉफ्टवेयर प्रोजेक्ट की तरह यूनिट टेस्ट के बजाय उदाहरण कोड और ट्यूटोरियल प्रदान करती है। सत्यापन आमतौर पर निम्नलिखित द्वारा होता है:

1. **उदाहरण चलाना** - प्रत्येक उदाहरण त्रुटि के बिना चलना चाहिए
2. **आउटपुट की जाँच** - सुनिश्चित करें कि मॉडल प्रतिक्रियाएँ उपयुक्त हैं
3. **ट्यूटोरियल का पालन करना** - चरण-दर-चरण गाइड दस्तावेज़ के अनुसार काम करना चाहिए

**सामान्य सत्यापन विधि:**
- लक्ष्य पर्यावरण में उदाहरण का परीक्षण करें
- निर्भरताओं को सही तरीके से इंस्टॉल करना सुनिश्चित करें
- जाँचे कि मॉडल डाउनलोड/लोड सफल रहा है
- अपेक्षित व्यवहार दस्तावेज़ से मेल खाता हो

## Code Style and Conventions

### General Guidelines

- उदाहरण स्पष्ट, अच्छी तरह से टिप्पणीयुक्त और शिक्षाप्रद होने चाहिए
- भाषा-विशिष्ट मानकों का पालन करें (Python के लिए PEP 8, .NET के लिए C# मानक)
- उदाहरण Phi मॉडल की विशिष्ट क्षमताओं को प्रदर्शित करने पर केंद्रित होने चाहिए
- मुख्य अवधारणाओं और मॉडल-विशिष्ट पैरामीटरों को समझाने वाली टिप्पणियाँ शामिल करें

### Documentation Standards

**URL Formatting:**
- `[text](../../url)` प्रारूप का उपयोग करें बिना अतिरिक्त रिक्त स्थान के
- सापेक्ष लिंक: वर्तमान निर्देशिका के लिए `./`, पैरेंट के लिए `../`
- URL में देश-विशिष्ट लोकैल शामिल न करें (जैसे `/en-us/`, `/en/` से बचें)

**Images:**
- सभी छवियाँ `/imgs/` निर्देशिका में संग्रहित करें
- नाम अंग्रेज़ी अक्षरों, संख्या, और डैश वाले विवर्णात्मक होने चाहिए
- उदाहरण: `phi-3-architecture.png`

**Markdown Files:**
- वास्तविक काम करने वाले उदाहरणों का संदर्भ `/code/` निर्देशिका में दें
- दस्तावेज़ कोड परिवर्तनों के साथ सिंक्रनाइज़ रखें
- README में Jupyter नोटबुक लिंक को 📓 इमोजी से चिह्नित करें

### File Organization

- `/code/` में विषय/फ़ीचर के अनुसार कोड उदाहरण आयोजित करें
- `/md/` में दस्तावेज़ संरचना जब संभव हो कोड संरचना को प्रतिबिंबित करे
- संबंधित फ़ाइलें (नोटबुक, स्क्रिप्ट, कॉन्फ़िग) उपनिर्देशिकाओं में एक साथ रखें

## Pull Request Guidelines

### Before Submitting

1. **रिपॉजिटरी को अपने खाते में फोर्क करें**
2. **PRs प्रकार के अनुसार पृथक करें:**
   - एक में बग सुधार
   - दूसरे में दस्तावेज़ अपडेट
   - नए उदाहरण अलग-अलग PRs में
   - टाइपो सुधार को मिलाया जा सकता है

3. **मर्ज विवादों को संभालें:**
   - परिवर्तनों से पहले स्थानीय `main` ब्रांच अपडेट करें
   - ऊपर के स्रोत के साथ नियमित रूप से सिंक करें

4. **अनुवाद PRs:**
   - फ़ोल्डर के सभी फ़ाइलों के अनुवाद शामिल होने चाहिए
   - मूल भाषा के समान संरचना बनाए रखें

### Required Checks

PRs स्वचालित रूप से GitHub वर्कफ़्लो चलाकर सत्यापन करते हैं:

1. **सापेक्ष पथ सत्यापन** - सभी आंतरिक लिंक काम करते हो
   - VS Code में Ctrl+Click से लिंक स्थानीय रूप से जांचें
   - पथ सुझावों का उपयोग करें (`./` या `../`)

2. **URL लोकैल जांच** - वेब URLs में देश-विशिष्ट लोकैल न हो
   - `/en-us/`, `/en/`, या अन्य भाषा कोड निकालें
   - सामान्य अंतरराष्ट्रीय URLs का उपयोग करें

3. **टूटा हुआ URL जांच** - सभी URLs 200 स्थिति लौटाएँ
   - सबमिट करने से पहले लिंक की पहुँच सत्यापित करें
   - ध्यान दें: कुछ असफलताएँ नेटवर्क प्रतिबंधों के कारण हो सकती हैं

### PR Title Format

```
[component] Brief description
```

उदाहरण:
- `[docs] Phi-4 इन्फ़रेंस ट्यूटोरियल जोड़ें`
- `[code] ONNX Runtime इंटीग्रेशन उदाहरण ठीक करें`
- `[translation] परिचय गाइड के लिए जापानी अनुवाद जोड़ें`

## Common Development Patterns

### Working with Phi Models

**Model Loading:**
- उदाहरण विभिन्न फ्रेमवर्क का उपयोग करते हैं: Transformers, ONNX Runtime, MLX, OpenVINO
- मॉडल आमतौर पर Hugging Face, Azure, या GitHub Models से डाउनलोड होते हैं
- अपने हार्डवेयर (CPU, GPU, NPU) के साथ मॉडल संगतता जांचें

**Inference Patterns:**
- टेक्स्ट जनरेशन: अधिकांश उदाहरण चैट/इंस्ट्रक्ट वेरिएंट का उपयोग करते हैं
- विज़न: इमेज समझ के लिए Phi-3-vision और Phi-4-multimodal
- ऑडियो: Phi-4-multimodal ऑडियो इनपुट समर्थन करता है
- तर्क: उन्नत तर्क कार्यों के लिए Phi-4-reasoning वेरिएंट

### Platform-Specific Notes

**Microsoft Foundry:**
- Azure सदस्यता और API कीज़ की आवश्यकता
- देखें `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- परीक्षण के लिए मुफ्त स्तर उपलब्ध
- देखें `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime: क्रॉस-प्लेटफॉर्म, अनुकूलित इन्फ़रेंस
- Ollama: आसान स्थानीय मॉडल प्रबंधन (डेव कंटेनर में पूर्व- कॉन्फ़िगर)
- Apple MLX: Apple सिलिकॉन के लिए ऑप्टिमाइज़्ड

## Troubleshooting

### Common Issues

**Memory Issues:**
- Phi मॉडलों को पर्याप्त RAM की आवश्यकता होती है (खासतौर पर विज़न/मल्टीमॉडल वेरिएंट)
- संसाधन-सीमित वातावरण के लिए क्वांटाइज्ड मॉडल का उपयोग करें
- देखें `/md/01.Introduction/04/QuantifyingPhi.md`

**Dependency Conflicts:**
- Python उदाहरणों को विशिष्ट संस्करणों की आवश्यकता हो सकती है
- प्रत्येक उदाहरण के लिए वर्चुअल एनवायरनमेंट का उपयोग करें
- व्यक्तिगत `requirements.txt` फ़ाइलें जांचें

**Model Download Failures:**
- बड़े मॉडल धीमे कनेक्शन पर टाइमआउट हो सकते हैं
- क्लाउड वातावरण (Codespaces, Azure) का उपयोग करने पर विचार करें
- Hugging Face कैश जांचें: `~/.cache/huggingface/`

**.NET Project Issues:**
- सुनिश्चित करें कि .NET 8.0 SDK इंस्टॉल है
- निर्माण से पहले `dotnet restore` चलाएं
- कुछ प्रोजेक्टों में CUDA-विशिष्ट कॉन्फ़िगरेशन होते हैं (Debug_Cuda)

**JavaScript/Web Examples:**
- संगतता के लिए Node.js 18+ का उपयोग करें
- समस्याओं के लिए `node_modules` साफ करें और फिर पुनः इंस्टॉल करें
- WebGPU संगतता समस्याओं के लिए ब्राउज़र कंसोल जांचें

### Getting Help

- **Discord:** Microsoft Foundry Community Discord में जुड़ें
- **GitHub Issues:** रिपॉजिटरी में बग और मुद्दे रिपोर्ट करें
- **GitHub Discussions:** प्रश्न पूछें और ज्ञान साझा करें

## Additional Context

### Responsible AI

सभी Phi मॉडल उपयोग को माइक्रोसॉफ्ट के Responsible AI सिद्धांतों का पालन करना चाहिए:
- निष्पक्षता, विश्वसनीयता, सुरक्षा
- गोपनीयता और सुरक्षा  
- समावेशन, पारदर्शिता, जवाबदेही
- उत्पादन अनुप्रयोगों के लिए Azure AI कंटेंट सेफ्टी का उपयोग करें
- देखें `/md/01.Introduction/01/01.AISafety.md`

### Translations

- 50+ भाषाओं का समर्थन स्वचालित GitHub Action के माध्यम से
- अनुवाद `/translations/` निर्देशिका में
- सह-ऑप-ट्रांसलेटर वर्कफ़्लो द्वारा बनाए रखा गया
- अनुवादित फ़ाइलों को मैन्युअली संपादित न करें (स्वतः उत्पन्न)

### Contributing

- `CONTRIBUTING.md` में दिशानिर्देशों का पालन करें
- Contributor License Agreement (CLA) से सहमत हों
- Microsoft Open Source Code of Conduct का पालन करें
- कमिट्स में सुरक्षा और क्रेडेंशियल्स शामिल न करें

### Multi-Language Support

यह एक बहुभाषी रिपॉजिटरी है जिसमें उदाहरण हैं:
- **Python** - ML/AI वर्कफ़्लो, Jupyter नोटबुक, फाइन-ट्यूनिंग
- **C#/.NET** - एंटरप्राइज एप्लिकेशन, ONNX Runtime इंटीग्रेशन
- **JavaScript** - वेब-आधारित AI, WebGPU के साथ ब्राउज़र इन्फ़रेंस

अपने उपयोग और तैनाती के लक्ष्य के अनुसार सबसे उपयुक्त भाषा चुनें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान रखें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की अनुशंसा की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->