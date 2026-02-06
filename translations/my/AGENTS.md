# AGENTS.md

## ပရောဂျက်အကျဉ်းချုပ်

PhiCookBook သည် Microsoft ရဲ့ Phi စာလုံးသေးသေးလေး Language Models (SLMs) များနှင့်အလုပ်လုပ်ရန်အတွက် လက်တွေ့နမူနာများ၊ သင်ခန်းစာများနှင့် အကြောင်းအရာများပါဝင်သော စုံလင်သောချက်ပြုတ်စာအုပ် repository ဖြစ်သည်။ ဤ repository သည် အမျိုးမျိုးသော အသုံးပြုမှုများကို ပြသထားပြီး အထဲတွင် အကြံပြုချက်၊ ပြုပြင်မွမ်းမံခြင်း၊ quantization၊ RAG အကောင်အထည်ဖော်မှုများနှင့် မျိုးစုံအသုံးပြုမှုများကို အခြေခံပြီး platform များနှင့် framework များအတွင်းတွင် အသုံးပြုနိုင်သည်။

**အဓိကနည်းပညာများ:**
- **ဘာသာစကားများ:** Python, C#/.NET, JavaScript/Node.js
- **Framework များ:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platform များ:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **မော်ဒယ်အမျိုးအစားများ:** Phi-3, Phi-3.5, Phi-4 (စာသား, ရှုထောင့်, မျိုးစုံ, အကြောင်းအရာဆိုင်ရာ)

**Repository ဖွဲ့စည်းမှု:**
- `/code/` - အလုပ်လုပ်နေသော code နမူနာများနှင့် နမူနာအကောင်အထည်ဖော်မှုများ
- `/md/` - အသေးစိတ်အကြောင်းအရာများ၊ သင်ခန်းစာများနှင့် လမ်းညွှန်ချက်များ  
- `/translations/` - ဘာသာစကားများစွာ (50+ ဘာသာစကားများ) အတွက် အလိုအလျောက် workflow ဖြင့် ဘာသာပြန်ချက်များ
- `/.devcontainer/` - Dev container configuration (Python 3.12 နှင့် Ollama)

## ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင် Setup

### GitHub Codespaces သို့မဟုတ် Dev Containers အသုံးပြုခြင်း (အကြံပြုထားသည်)

1. GitHub Codespaces တွင်ဖွင့်ရန် (အမြန်ဆုံး):
   - README တွင် "Open in GitHub Codespaces" badge ကိုနှိပ်ပါ
   - Container သည် Python 3.12 နှင့် Ollama နှင့် Phi-3 ကို အလိုအလျောက် configure လုပ်သည်

2. VS Code Dev Containers တွင်ဖွင့်ရန်:
   - README မှ "Open in Dev Containers" badge ကိုအသုံးပြုပါ
   - Container သည် အနည်းဆုံး 16GB host memory လိုအပ်သည်

### Local Setup

**လိုအပ်ချက်များ:**
- Python 3.12 သို့မဟုတ် အထက်
- .NET 8.0 SDK (C# နမူနာများအတွက်)
- Node.js 18+ နှင့် npm (JavaScript နမူနာများအတွက်)
- အနည်းဆုံး 16GB RAM အကြံပြုထားသည်

**Installation:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python နမူနာများအတွက်:**
နမူနာ directory အထူးသို့သွားပြီး dependencies များကို install လုပ်ပါ:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**.NET နမူနာများအတွက်:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web နမူနာများအတွက်:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Repository အဖွဲ့စည်းမှု

### Code နမူနာများ (`/code/`)

- **01.Introduce/** - အခြေခံမိတ်ဆက်များနှင့် စတင်ရန်နမူနာများ
- **03.Finetuning/** နှင့် **04.Finetuning/** - အမျိုးမျိုးသောနည်းလမ်းများဖြင့် ပြုပြင်မွမ်းမံခြင်းနမူနာများ
- **03.Inference/** - အမျိုးမျိုးသော hardware (AIPC, MLX) တွင် အကြံပြုချက်နမူနာများ
- **06.E2E/** - အဆုံးအထိ အကောင်အထည်ဖော်မှုနမူနာများ
- **07.Lab/** - လက်တွေ့/စမ်းသပ်မှုအကောင်အထည်ဖော်မှုများ
- **08.RAG/** - Retrieval-Augmented Generation နမူနာများ
- **09.UpdateSamples/** - နောက်ဆုံး update လုပ်ထားသော နမူနာများ

### Documentation (`/md/`)

- **01.Introduction/** - မိတ်ဆက်လမ်းညွှန်များ၊ ပတ်ဝန်းကျင် setup၊ platform လမ်းညွှန်များ
- **02.Application/** - အသုံးပြုမှုနမူနာများကို အမျိုးအစား (စာသား, ကုဒ်, ရှုထောင့်, အသံ, စသည်) အလိုက် စီစဉ်ထားသည်
- **02.QuickStart/** - Azure AI Foundry နှင့် GitHub Models အတွက် အမြန်စတင်ရန်လမ်းညွှန်များ
- **03.FineTuning/** - ပြုပြင်မွမ်းမံခြင်းအကြောင်းအရာများနှင့် သင်ခန်းစာများ
- **04.HOL/** - လက်တွေ့အလုပ်လုပ်ရန် သင်ခန်းစာများ (.NET နမူနာများပါဝင်သည်)

### ဖိုင် Format များ

- **Jupyter Notebooks (`.ipynb`)** - 📓 အမှတ်အသားဖြင့် README တွင် ဖော်ပြထားသော လက်တွေ့ Python သင်ခန်းစာများ
- **Python Scripts (`.py`)** - Standalone Python နမူနာများ
- **C# Projects (`.csproj`, `.sln`)** - .NET အကောင်အထည်ဖော်မှုများနှင့် နမူနာများ
- **JavaScript (`.js`, `package.json`)** - Web-based နှင့် Node.js နမူနာများ
- **Markdown (`.md`)** - Documentation နှင့် လမ်းညွှန်ချက်များ

## နမူနာများနှင့်အလုပ်လုပ်ခြင်း

### Jupyter Notebooks ကို run လုပ်ခြင်း

နမူနာများအများစုသည် Jupyter notebooks အဖြစ်ပေးထားသည်:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Python Scripts ကို run လုပ်ခြင်း

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET နမူနာများကို run လုပ်ခြင်း

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

သို့မဟုတ် အပြည့်အစုံ solution ကို build လုပ်ပါ:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web နမူနာများကို run လုပ်ခြင်း

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## စမ်းသပ်ခြင်း

ဤ repository သည် နမူနာ code နှင့် သင်ခန်းစာများပါဝင်ပြီး အခြား software project များလို unit tests မပါဝင်ပါ။ Validation သည် အောက်ပါနည်းလမ်းများဖြင့် အများအားဖြင့် ပြုလုပ်သည်:

1. **နမူနာများကို run လုပ်ခြင်း** - နမူနာတစ်ခုစီသည် error မရှိဘဲ အလုပ်လုပ်သင့်သည်
2. **output များကို စစ်ဆေးခြင်း** - မော်ဒယ်၏ အကြောင်းပြုချက်များသည် သင့်လျော်သောအဖြေများဖြစ်ရမည်
3. **သင်ခန်းစာများကို လိုက်နာခြင်း** - လမ်းညွှန်ချက်များသည် documentation အတိုင်း အလုပ်လုပ်သင့်သည်

**အများဆုံး validation နည်းလမ်း:**
- Target ပတ်ဝန်းကျင်တွင် နမူနာများကို စမ်းသပ် run လုပ်ပါ
- Dependencies များကို မှန်ကန်စွာ install လုပ်နိုင်ကြောင်း စစ်ဆေးပါ
- မော်ဒယ်များကို download/load လုပ်နိုင်ကြောင်း အတည်ပြုပါ
- Documentation နှင့် ကိုက်ညီသော အပြုအမူကို အတည်ပြုပါ

## Code Style နှင့် Conventions

### အထွေထွေ လမ်းညွှန်ချက်များ

- နမူနာများသည် ရှင်းလင်းပြီး မှတ်ချက်များထည့်ထားသင့်သည်
- ဘာသာစကားအထူးသတ်မှတ်ချက်များကို လိုက်နာပါ (Python အတွက် PEP 8, .NET အတွက် C# standards)
- နမူနာများသည် Phi မော်ဒယ်၏ အထူးစွမ်းရည်များကို ပြသရန် အာရုံစိုက်ထားသင့်သည်
- အဓိကအကြောင်းအရာများနှင့် မော်ဒယ်အထူး parameters များကို ရှင်းလင်းသော မှတ်ချက်များထည့်ပါ

### Documentation Standards

**URL Formatting:**
- `[text](../../url)` format ကို အသုံးပြုပါ၊ အပိုနေရာများမထည့်ပါနှင့်
- Relative links: `./` ကို လက်ရှိ directory အတွက်၊ `../` ကို parent အတွက် အသုံးပြုပါ
- URL များတွင် နိုင်ငံအထူး locales မပါဝင်သင့်ပါ (ဥပမာ `/en-us/`, `/en/`)

**Images:**
- အားလုံး images ကို `/imgs/` directory တွင် သိမ်းဆည်းပါ
- အဓိကအမည်များကို အင်္ဂလိပ်အက္ခရာများ၊ နံပါတ်များနှင့် dashes ဖြင့် သတ်မှတ်ပါ
- ဥပမာ: `phi-3-architecture.png`

**Markdown Files:**
- `/code/` directory တွင်ရှိသော အလုပ်လုပ်နေသော နမူနာများကို ရည်ညွှန်းပါ
- Documentation ကို code ပြောင်းလဲမှုများနှင့် အညီထားပါ
- README တွင် Jupyter notebook links ကို 📓 emoji ဖြင့် အမှတ်အသားပြုပါ

### ဖိုင်ဖွဲ့စည်းမှု

- `/code/` တွင် နမူနာများကို အကြောင်းအရာ/feature အလိုက် စီစဉ်ထားသည်
- Documentation ကို `/md/` တွင် code ဖွဲ့စည်းမှုနှင့် ကိုက်ညီစွာ mirror လုပ်ထားသည်
- ဆက်စပ်သော ဖိုင်များ (notebooks, scripts, configs) ကို subdirectories တွင် အတူတူထားပါ

## Pull Request လမ်းညွှန်ချက်များ

### Submit လုပ်မည့်အခါ

1. **Repository ကို Fork လုပ်ပါ** သင့်အကောင့်သို့
2. **PR များကို အမျိုးအစားအလိုက် ခွဲခြားပါ:**
   - Bug fixes ကို PR တစ်ခုတွင်
   - Documentation update များကို တစ်ခုခြား PR တွင်
   - နမူနာအသစ်များကို ခွဲခြား PR တွင်
   - Typo fixes များကို ပေါင်းစပ်နိုင်သည်

3. **Merge conflicts ကို ဖြေရှင်းပါ:**
   - ပြုပြင်မှုများပြုလုပ်မီ သင့် local `main` branch ကို update လုပ်ပါ
   - Upstream နှင့် မကြာခဏ sync လုပ်ပါ

4. **Translation PR များ:**
   - Folder အတွင်းရှိ ဖိုင်အားလုံးအတွက် ဘာသာပြန်ချက်များ ပါဝင်ရမည်
   - မူရင်းဘာသာစကားနှင့် ဖွဲ့စည်းမှုကို တူညီစွာ ထိန်းသိမ်းပါ

### လိုအပ်သော စစ်ဆေးမှုများ

PR များသည် GitHub workflows ကို အလိုအလျောက် run လုပ်ပြီး အောက်ပါအချက်များကို validate လုပ်သည်:

1. **Relative path validation** - အတွင်း link များအားလုံး အလုပ်လုပ်ရမည်
   - VS Code တွင် Ctrl+Click ဖြင့် link များကို locally စမ်းသပ်ပါ
   - VS Code မှ path အကြံပြုချက်များကို အသုံးပြုပါ (`./` သို့မဟုတ် `../`)

2. **URL locale check** - Web URLs တွင် နိုင်ငံ locales မပါဝင်ရမည်
   - `/en-us/`, `/en/` သို့မဟုတ် အခြားဘာသာစကား code များကို ဖယ်ရှားပါ
   - အပြည်ပြည်ဆိုင်ရာ URLs ကို အသုံးပြုပါ

3. **Broken URL check** - URLs အားလုံးသည် 200 status ကို return ပြုရမည်
   - Submit မလုပ်မီ link များကို access လုပ်နိုင်ကြောင်း စစ်ဆေးပါ
   - မှတ်ချက်: အချို့သော failure များသည် network ကန့်သတ်ချက်များကြောင့် ဖြစ်နိုင်သည်

### PR Title Format

```
[component] Brief description
```

ဥပမာများ:
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## အများဆုံး ဖွံ့ဖြိုးရေး Pattern များ

### Phi မော်ဒယ်များနှင့်အလုပ်လုပ်ခြင်း

**Model Loading:**
- နမူနာများသည် Framework များစွာကို အသုံးပြုသည်: Transformers, ONNX Runtime, MLX, OpenVINO
- မော်ဒယ်များကို Hugging Face, Azure, GitHub Models မှ download လုပ်သည်
- မော်ဒယ်သည် သင့် hardware (CPU, GPU, NPU) နှင့် ကိုက်ညီမှုရှိကြောင်း စစ်ဆေးပါ

**Inference Patterns:**
- စာသားထုတ်လုပ်မှု: နမူနာများအများစုသည် chat/instruct variants ကို အသုံးပြုသည်
- ရှုထောင့်: Phi-3-vision နှင့် Phi-4-multimodal ကို ပုံနားလည်မှုအတွက် အသုံးပြုသည်
- အသံ: Phi-4-multimodal သည် အသံ input များကို ပံ့ပိုးသည်
- အကြောင်းအရာဆိုင်ရာ: Phi-4-reasoning variants သည် အဆင့်မြင့် reasoning အလုပ်များအတွက်

### Platform အထူးမှတ်ချက်များ

**Azure AI Foundry:**
- Azure subscription နှင့် API key များ လိုအပ်သည်
- `/md/02.QuickStart/AzureAIFoundry_QuickStart.md` ကို ကြည့်ပါ

**GitHub Models:**
- စမ်းသပ်ရန် အခမဲ့ tier ရရှိနိုင်သည်
- `/md/02.QuickStart/GitHubModel_QuickStart.md` ကို ကြည့်ပါ

**Local Inference:**
- ONNX Runtime: Cross-platform, optimized inference
- Ollama: Easy local model management (dev container တွင် pre-configured)
- Apple MLX: Apple Silicon အတွက် optimized

## Troubleshooting

### အများဆုံးပြဿနာများ

**Memory Issues:**
- Phi မော်ဒယ်များသည် RAM အများကြီးလိုအပ်သည် (အထူးသဖြင့် vision/multimodal variants)
- အရင်းအမြစ်ကန့်သတ်ထားသော ပတ်ဝန်းကျင်များအတွက် quantized မော်ဒယ်များကို အသုံးပြုပါ
- `/md/01.Introduction/04/QuantifyingPhi.md` ကို ကြည့်ပါ

**Dependency Conflicts:**
- Python နမူနာများတွင် version အထူးလိုအပ်ချက်များရှိနိုင်သည်
- နမူနာတစ်ခုစီအတွက် virtual environment များကို အသုံးပြုပါ
- Individual `requirements.txt` ဖိုင်များကို စစ်ဆေးပါ

**Model Download Failures:**
- မော်ဒယ်များသည် ချိတ်ဆက်မှုနှေးကွေးသော connection များတွင် timeout ဖြစ်နိုင်သည်
- Cloud ပတ်ဝန်းကျင်များ (Codespaces, Azure) ကို အသုံးပြုပါ
- Hugging Face cache ကို စစ်ဆေးပါ: `~/.cache/huggingface/`

**.NET Project Issues:**
- .NET 8.0 SDK install လုပ်ထားကြောင်း အတည်ပြုပါ
- `dotnet restore` ကို build မလုပ်မီ အသုံးပြုပါ
- အချို့သော project များတွင် CUDA-specific configuration (Debug_Cuda) ရှိသည်

**JavaScript/Web နမူနာများ:**
- Compatibility အတွက် Node.js 18+ ကို အသုံးပြုပါ
- `node_modules` ကို ရှင်းပြီး ပြန် install လုပ်ပါ
- WebGPU compatibility issue များအတွက် browser console ကို စစ်ဆေးပါ

### အကူအညီရယူခြင်း

- **Discord:** Azure AI Foundry Community Discord ကို join လုပ်ပါ
- **GitHub Issues:** Repository တွင် bug များနှင့် ပြဿနာများကို report လုပ်ပါ
- **GitHub Discussions:** မေးခွန်းများမေးပြီး knowledge မျှဝေပါ

## အပိုဆောင်းအကြောင်းအရာ

### Responsible AI

Phi မော်ဒယ်အသုံးပြုမှုအားလုံးသည် Microsoft ရဲ့ Responsible AI အခြေခံသဘောတရားများကို လိုက်နာရမည်:
- တရားမျှတမှု၊ ယုံကြည်စိတ်ချရမှု၊ လုံခြုံမှု
- ကိုယ်ရေးအချက်အလက်နှင့် လုံခြုံရေး  
- ပါဝင်မှု၊ ထင်ရှားမှု၊ တာဝန်ယူမှု
- ထုတ်လုပ်မှုအတွက် Azure AI Content Safety ကို အသုံးပြုပါ
- `/md/01.Introduction/01/01.AISafety.md` ကို ကြည့်ပါ

### Translations

- GitHub Action အလိုအလျောက်ဖြင့် 50+ ဘာသာစကားများကို ပံ့ပိုးထားသည်
- `/translations/` directory တွင် ဘာသာပြန်ချက်များရှိသည်
- co-op-translator workflow ဖြင့် ထိန်းသိမ်းထားသည်
- ဘာသာပြန်ထားသော ဖိုင်များကို manually edit မလုပ်ပါ (auto-generated ဖြစ်သည်)



---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။