# AGENTS.md

## Project Overview

PhiCookBook គឺជាគ្រប់គ្រងសៀវភៅចម្អិនដែលមានឧទាហរណ៍​អនុវត្ត​ជាក់ស្តែង ការបង្រៀន និងឯកសារ​សម្រាប់ធ្វើការជាមួយគ្រួសារ Phi របស់ Microsoft នៃម៉ូដែលភាសាស្រាល (SLMs)។ អង្គភាពនេះបង្ហាញពីករណីប្រើប្រាស់នានា រួមទាំងការព្យាករណ៍ (inference), ការបណ្តុះបណ្តាលបន្ថែម (fine-tuning), ការបរិមាណតម្លៃ (quantization), ការអនុវត្ត RAG និងកម្មវិធី​មូលដ្ឋានចម្រុះគ្នា លើវេទិកា និង​ស៊ុមប្រព័ន្ធផ្សេងៗ។

**បច្ចេកវិទ្យាសំខាន់ៗ៖**
- **ភាសា:** Python, C#/.NET, JavaScript/Node.js
- **ស៊ុមប្រព័ន្ធ:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **វេទិកា:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **ប្រភេទម៉ូដែល:** Phi-3, Phi-3.5, Phi-4 (ប្រភេទអត្ថបទ, រូបភាព, មូលដ្ឋានចម្រុះ និងផ្នែកយល់ដឹង)

**រចនាសម្ព័ន្ធ Repository:**
- `/code/` - ឧទាហរណ៍កូដ និងអនុវត្តគំរូ
- `/md/` - ឯកសារពិស្តារ ការបង្រៀន និងមគ្គុទេសក៍ករណីប្រើប្រាស់  
- `/translations/` - ការបកប្រែជាភាសាច្រើន (លើស 50 ភាសា តាមប្រព័ន្ធអូតូមាទិក)
- `/.devcontainer/` - កំណត់រចនាសម្ព័ន្ធ dev container (Python 3.12 ជាមួយ Ollama)

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. បើកក្នុង GitHub Codespaces (លឿនជាងគេ):
   - ចុច "Open in GitHub Codespaces" នៅក្នុង README
   - អង្គធាតុ container នឹងកំណត់រចនាសម្ព័ន្ធដោយស្វ័យប្រវត្តិជាមួយ Python 3.12 និង Ollama ជាមួយ Phi-3

2. បើកក្នុង VS Code Dev Containers:
   - ប្រើប៊ូតុង "Open in Dev Containers" ពី README
   - តម្រូវឲ្យមានមេម៉ូរីរបស់ម៉ាស៊ីនផ្ទះ 16GB យ៉ាងហោចណាស់

### Local Setup

**តម្រូវការមុន:**
- Python 3.12 ឬក្រោយ
- .NET 8.0 SDK (សម្រាប់ឧទាហរណ៍ C#)
- Node.js 18+ និង npm (សម្រាប់ឧទាហរណ៍ JavaScript)
- 16GB RAM យ៉ាងហោចណាស់បានផ្តល់អនុសាសន៍

**ការ​ដំឡើង:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**សម្រាប់ឧទាហរណ៍ Python៖**
ចូលទៅកាន់ថតឧទាហរណ៍ជាក់លាក់ និងដំឡើងបណ្តាប់បណ្ដា​ដោយខ្លួនឯង:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # ប្រសិនបើ requirements.txt មានស្រាប់
```

**សម្រាប់ឧទាហរណ៍ .NET៖**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**សម្រាប់ឧទាហរណ៍ JavaScript/Web៖**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # ចាប់ផ្ដើមម៉ាស៊ីនមេអភិវឌ្ឍន៍
npm run build  # សង់សំរាប់ផលិតកម្ម
```

## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - ការណែនាំមូលដ្ឋាន និងគំរូចាប់ផ្ដើម
- **03.Finetuning/** និង **04.Finetuning/** - ឧទាហរណ៍ fine-tuning ជាមួយវិធីសាស្រ្តនានា
- **03.Inference/** - ឧទាហរណ៍ inference លើរឹងប័ត្រផ្សេងៗ (AIPC, MLX)
- **06.E2E/** - គំរូកម្មវិធីចាប់ពីដំណាក់កាលដើមទៅចុងក្រោយ
- **07.Lab/** - អនុវត្តន៍មន្ទីរសាកល្បង
- **08.RAG/** - ឧទាហរណ៍បង្កើតនៃ Retrieval-Augmented Generation
- **09.UpdateSamples/** - គំរូដែលបានធ្វើបច្ចុប្បន្នភាពថ្មីៗ

### Documentation (`/md/`)

- **01.Introduction/** - មគ្គុទេសក៍ណែនាំ ការកំណត់បរិយាកាស និងមគ្គុទេសក៍វេទិកា
- **02.Application/** - គំរូកម្មវិធីតាមប្រភេទ (អត្ថបទ, កូដ, រូបភាព, សម្លេង, ល)
- **02.QuickStart/** - មគ្គុទេសក៍ចាប់ផ្ដើមលឿន សម្រាប់ Microsoft Foundry និង GitHub Models
- **03.FineTuning/** - ឯកសារនិងការបង្រៀនអំពីការបណ្តុះបណ្តាលបន្ថែម
- **04.HOL/** - មន្ទីរអនុវត្ត (មានឧទាហរណ៍ .NET)

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - វគ្គបង្រៀន Python បន្តផ្ទាល់មុខសញ្ញា📓នៅក្នុង README
- **Python Scripts (`.py`)** - ឧទាហរណ៍ Python ឯករាជ្យ
- **C# Projects (`.csproj`, `.sln`)** - កម្មវិធី និងគំរូ .NET
- **JavaScript (`.js`, `package.json`)** - ឧទាហរណ៍លើវែបនិង Node.js
- **Markdown (`.md`)** - ឯកសារ និងមគ្គុទេសក៍

## Working with Examples

### Running Jupyter Notebooks

ភាគច្រើនឧទាហរណ៍ផ្តល់ជាទម្រង់ Jupyter notebook:
```bash
pip install jupyter notebook
jupyter notebook  # បើកចំណុចផ្ទៃប្រើប្រាស់កម្មវិធីរ៉ូបសើរ
# ចូលទៅកាន់ឯកសារ .ipynb ដែលចង់បាន
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

ឬក៏កសាងដំណោះស្រាយទាំងមូល:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Running JavaScript/Web Examples

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # ការអភិវឌ្ឍន៍ជាមួយការលោតឡើងក្តៅ
```

## Testing

អង្គភាពនេះមានគំរូកូដ និងមគ្គុទេសក៍ ជាជម្រើសមិនមែនគំរូកម្មវិធីទូទៅដែលមាន unit tests ទេ។ ការផ្ទៀងផ្ទាត់ប្រព័ន្ធសម្រាប់ការផ្ទៀងផ្ទាត់ធម្មតាគឺ:

1. **រត់ឧទាហរណ៍** - គំរូនិមួយៗគួរត្រូវដំណើរការជោគជ័យគ្មានកំហុស
2. **ផ្ទៀងផ្ទាត់លទ្ធផល** - ពិនិត្យមើលថាពីលទ្ធផលម៉ូដែលត្រឹមត្រូវឬអត់
3. **ដើរតាមមគ្គុទេសក៍** - មគ្គុទេសក៍ត្រូវដំណើរការតាមលំដាប់

**វិធីសាស្រ្តផ្ទៀងផ្ទាត់ទូទៅ:**
- សាកល្បងការត្រួតពិនិត្យឧទាហរណ៍នៅលើបរិយាកាសគោលដៅ
- ពិនិត្យំថាការដំឡើងការពឹងផ្អែកបានត្រឹមត្រូវ
- ពិនិត្យថាការទាញយក/ផ្ទុកម៉ូដែលជោគជ័យ
- បញ្ជាក់ពីបែបបទដែលគួរតែត្រូវនឹងឯកសារ

## Code Style and Conventions

### General Guidelines

- ឧទាហរណ៍គួរតែច្បាស់លាស់ មានមតិយោបល់ល្អ និងមានការបង្រៀន
- តាមដានបែបបទភាសាជាក់លាក់ (PEP 8 សម្រាប់ Python, ស្តង់ដារ C# សម្រាប់ .NET)
- ផ្ដោតលើការបង្ហាញសមត្ថភាពម៉ូដែល Phi ជាក់លាក់
- រួមបញ្ចូលមតិយោបល់ពន្យល់ពីគំនិតសំខាន់ និងប៉ារ៉ាម៉ែត្រជាក់លាក់របស់ម៉ូដែល

### Documentation Standards

**URL Formatting:**
- ប្រើទ្រង់ទ្រាយ `[text](../../url)` ដោយមិនមានចន្លោះថែម
- តំណភាគល្អិត: ប្រើ `./` សម្រាប់ថតបច្ចុប្បន្ន, `../` សម្រាប់ថតមាតា
- មិនមានកូដភាសា/ប្រទេសក្នុង URL (ជៀសវាង `/en-us/`, `/en/`)

**Images:**
- រក្សាទុករូបភាពទាំងអស់ក្នុងថត `/imgs/`
- ប្រើឈ្មោះពិពណ៌នាដោយតួអក្សរឡាតាំង លេខ និងខ្សែ (-)
- ឧទាហរណ៍: `phi-3-architecture.png`

**Markdown Files:**
- អះអាងឧទាហរណ៍កូដពិតប្រាកដនៅក្នុងថត `/code/`
- រក្សាឲ្យឯកសារត្រូវគ្នាជាមួយកូដ
- ប្រើរូបសញ្ញា 📓 ដើម្បីសម្គាល់តំណទៅ Jupyter notebook នៅក្នុង README

### File Organization

- ឧទាហរណ៍កូដក្នុង `/code/` រៀបចំតាមប្រធានបទ/មុខងារ
- ឯកសារនៅក្នុង `/md/` តំណាងរចនាសម្ព័ន្ធកូដប្រសិនបើអាចធ្វើទៅបាន
- រក្សាទុកឯកសារពាក់ព័ន្ធ (notebooks, scripts, configs) ជាក្រុមនៅក្នុងថតរង

## Pull Request Guidelines

### Before Submitting

1. **បំបែក repository នេះជារបស់អ្នក** 
2. **បំបែក PR ផ្អែកលើប្រភេទ**:
   - កែតម្រូវ bug ក្នុង PR មួយ
   - បន្ទាន់សម័យឯកសារផ្សេងទៀតក្នុង PR ផ្សេង
   - ឧទាហរណ៍ថ្មីក្នុង PR ផ្សេងៗ
   - កែអក្សរខ្នាតតូចអាចរួមបញ្ចូលបាន

3. **ដោះស្រាយករណីសន្ធិសញ្ញា merge:**
   - ចាប់ផ្ដើមធ្វើបច្ចុប្បន្នភាពសាខា `main` មុនការផ្លាស់ប្តូរ
   - đồng bộជាមួយ upstream ជាប្រចាំ

4. **PR សម្រាប់ការបកប្រែ:**
   - ត្រូវមានការបកប្រែគ្រប់ឯកសារនៅក្នុងថត
   - រក្សារចនាសម្ព័ន្ធឲ្យត្រូវនឹងភាសដើម

### Required Checks

PRs នឹងដំណើរការជាអូតូម៉ាទិក GitHub workflows ដើម្បីផ្ទៀងផ្ទាត់:

1. **ផ្ទៀងផ្ទាត់ផ្លូវផ្ទាល់ខ្លួន** - តំណថ្មីទាំងអស់ត្រូវដំណើរការក្នុងក្នុងជាមួយទាំងអស់
   - សាកល្បងបើកតំណដោយ Ctrl+Click នៅក្នុង VS Code
   - ប្រើសំណើផ្លូវពី VS Code (`./` ឬ `../`)

2. **ផ្ទៀងផ្ទាត់ URL មិនមាន locale ប្រទេស** - តំណអ៊ីនធឺណិតមិនគួរមានរបស់ប្រទេស
   - លុប `/en-us/`, `/en/` ឬកូដភាសាផ្សេងៗ
   - ធ្វើឲ្យប្រើ URL សកលលក្ខណៈទូទៅ

3. **ផ្ទៀងផ្ទាត់ URL មិនខូច** - URL ត្រូវតែប្រកាសកូដស្ថានភាព 200
   - ពិនិត្យឲ្យបានថាតំណអាចបើកបាន មុនដាក់ PR
   - គួរប្រុងប្រយ័ត្នពីបញ្ហា create ដោយប្រព័ន្ធបណ្តាញ

### PR Title Format

```
[component] Brief description
```

ឧទាហរណ៍:
- `[docs] បន្ថែមមគ្គុទេសក៍ Phi-4 inference`
- `[code] ជួសជុលឧទាហរណ៍ ONNX Runtime integration`
- `[translation] បន្ថែមការបកប្រែជប៉ុនសម្រាប់មគ្គុទេសក៍`

## Common Development Patterns

### Working with Phi Models

**ការផ្ទុកម៉ូដែល:**
- ឧទាហរណ៍ប្រើស៊ុមប្រព័ន្ធផ្សេងៗ: Transformers, ONNX Runtime, MLX, OpenVINO
- ម៉ូដែលទូទៅទាញយកពី Hugging Face, Azure ឬ GitHub Models
- ពិនិត្យសមត្ថភាពម៉ូដែលជាមួយរឹងបន្ទះរបស់អ្នក (CPU, GPU, NPU)

**លំនាំការព្យាករណ៍:**
- ការបង្កើតអត្ថបទ: ភាគច្រើនប្រើជម្រើស chat/instruct
- រូបវិទ្យា: Phi-3-vision និង Phi-4-multimodal សម្រាប់យល់ស្ទាត់រូបភាព
- សំឡេង: Phi-4-multimodal គាំទ្របញ្ចូលសំឡេង
- ការយល់ដឹង: Phi-4-reasoning variants សម្រាប់បញ្ហាការយល់ដឹងលំដាប់ខ្ពស់

### Platform-Specific Notes

**Microsoft Foundry:**
- ត្រូវការជាវ Azure និង API Keys
- មើល `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- មានជម្រើសឥតគិតថ្លៃសម្រាប់សាកល្បង
- មើល `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime: ដំណើរការលើវេទិកាចម្រុះ ដំណើរការលឿន
- Ollama: គ្រប់គ្រងម៉ូដែលក្នុងកន្លែង (បានកំណត់ជាមុនក្នុង dev container)
- Apple MLX: អាប់ធីមសម្រាប់ Apple Silicon

## Troubleshooting

### Common Issues

**បញ្ហារស្តុកមេម៉ូរី:**
- ម៉ូដែល Phi ត្រូវការមេម៉ូរី RAM ធំនៅជាពិសេសប្រភេទ vision/multimodal
- ប្រើម៉ូដែលដែលបានបរិមាណតម្លៃរួចសម្រាប់បរិយាកាសធនធានមានកំណត់
- មើល `/md/01.Introduction/04/QuantifyingPhi.md`

**អំពើជំរុញបណ្ដឹង:**
- ឧទាហរណ៍ Python អាចត្រូវការបណ្ដោះអាសន្នម៉ោងជាក់លាក់
- ប្រើ virtual environment សម្រាប់ឧទាហរណ៍និមួយៗ
- ពិនិត្យ `requirements.txt` តែមួយៗ

**បញ្ហាទាញយកម៉ូដែល:**
- ម៉ូដែលធំបារាំងប្រហែលនឹងមានការពន្យារពេលលើការតភ្ជាប់យឺត
- ពិចារណាប្រើបរិយាកាស cloud (Codespaces, Azure)
- ពិនិត្យ cache របស់ Hugging Face: `~/.cache/huggingface/`

**បញ្ហាគម្រោង .NET:**
- ប្រាកដថា .NET 8.0 SDK បានដំឡើង
- ប្រើ `dotnet restore` មុនការកសាង
- គំរូមួយចំនួនមានកំណត់ទំងន់ជាក់លាក់ CUDA (Debug_Cuda)

**ឧទាហរណ៍ JavaScript/Web:**
- ប្រើ Node.js 18+ សម្រាប់យោបល់ភាព
- លុប `node_modules` និងដំឡើងឡើងវិញ ប្រសិនបើមានបញ្ហា
- ពិនិត្យ console របស់ browser សម្រាប់បញ្ហា WebGPU

### Getting Help

- **Discord:** ចូលរួម Microsoft Foundry Community Discord
- **GitHub Issues:** រាយការណ៍ bug និងបញ្ហា
- **GitHub Discussions:** សួរព័ត៌មាន និងចែករំលែកចំណេះដឹង

## Additional Context

### Responsible AI

ការប្រើប្រាស់ម៉ូដែល Phi គ្រប់ស្ថានភាពត្រូវបំពេញតាមគោលការណ៍ AI ដោយមានកង្វល់ពី Microsoft ៖
- សមភាព, សុវត្ថិភាព, ភុនភាព
- សម្ងាត់ និងសុវត្ថិភាព  
- ភាពរួមចំណែក, ការប្រកាសច្បាស់, ការទទួលខុសត្រូវ
- ប្រើ Azure AI Content Safety សម្រាប់កម្មវិធីផលិតកម្ម
- មើល `/md/01.Introduction/01/01.AISafety.md`

### Translations

- គាំទ្រជាភាសាជាង 50 តាម GitHub Action អូតូមាទិក
- ការបកប្រែរក្សាទុកនៅ `/translations/`
- ត្រូវបានគ្រប់គ្រងដោយលំនាំការបកប្រែរួម
- កុំកែប្រែឯកសារបកប្រែដោយដៃ (លទ្ធផលស្វ័យប្រវត្តិ)

### Contributing

- តាមដានសេចក្ដីណែនាំក្នុង `CONTRIBUTING.md`
- đồng ý Contributor License Agreement (CLA)
- បានគោរពសេចក្ដីផ្ដើមនៃ Microsoft Open Source Code of Conduct
- រក្សាសុវត្ថិភាព និងគណនីដាក់ចូលគ្នាចេញពី commit(s)

### Multi-Language Support

នេះជា repository ភាសាចម្រុះមានឧទាហរណ៍ជា:
- **Python** - លម្អិតនិងការបណ្តុះ AI/ML, Jupyter notebooks, fine-tuning
- **C#/.NET** - កម្មវិធីសម្រាប់សហគ្រាស ការតភ្ជាប់ ONNX Runtime
- **JavaScript** - AI លើវែប ការព្យាករណ៍ក្នុង browser ជាមួយ WebGPU

ជ្រើសរើសភាសាដែលសាកសមសម្រាប់ករណីប្រើប្រាស់ និងគោលដៅចែកចាយរបស់អ្នក។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើង​ព្យាយាមរក្សាការត្រឹមត្រូវ សូមយល់ឲ្យបានថាការបកប្រែ​ដោយស្វ័យប្រវត្តិ​អាចមានកំហុស ឬការមិនត្រឹមត្រូវណាមួយ។ ឯកសារដើមនៅភាសាតិជាមួយរបស់វាគួរត្រូវបានពិចារណาว่า​ជា​ឯកសារដែលមានអំណាចជាដើម។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញមនុស្សត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនិងការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->