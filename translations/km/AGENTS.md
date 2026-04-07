# AGENTS.md

## Project Overview

PhiCookBook គឺជាឃ្លាំងសៀវភៅសន្លឹកពិធីដែលមានគំរូជាក់ស្តែង ការបង្រៀន និងឯកសារសម្រាប់ការងារជាមួយសូម្បីម៉ូដែលភាសាបច្ចុប្បន្នតូចៗ (SLMs) របស់ Microsoft Phi។ ឃ្លាំងនេះបង្ហាញពីករណីប្រើប្រាស់ជាច្រើន រួមមាន ការបញ្ចេញទិន្នន័យ ការរៀបចំច្បាស់លាស់ ការបញ្ចេញតម្លៃចំនួន ការអនុវត្ត RAG និងកម្មវិធីពហុមុខងារជាច្រើនលើវេទិកា និងសំណុំបែបបទខុសៗគ្នា។

**បច្ចេកវិទ្យាគ្រឿងចង្កៀងសំខាន់៖**
- **ភាសា៖** Python, C#/.NET, JavaScript/Node.js
- **សំណុំបែបបទ៖** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **វេទិកា៖** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **ប្រភេទម៉ូដែល៖** Phi-3, Phi-3.5, Phi-4 (អត្ថបទ, ទស្សនវិស័យ, ពហុមុខងារ, ប្រែប្រួលនៃការត្រួតពិនិត្យ)

**រចនាសម្ព័ន្ធឃ្លាំង៖**
- `/code/` - គំរូកូដ ឧទាហរណ៍ និងអនុវត្តន៍
- `/md/` - ឯកសារព័ត៌មានលម្អិត មេរៀន និងមគ្គុទេសក៍
- `/translations/` - ប្រែសម្រួលជាភាសាច្រើន (ជាង ៥០ ភាសា តាមការដំណើរការដោយស្វ័យប្រវត្តិ)
- `/.devcontainer/` - ការកំណត់ dev container (Python 3.12 ជាមួយ Ollama)

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. បើកនៅក្នុង GitHub Codespaces (លឿនបំផុត)៖
   - ចុចប៊ូតុង "Open in GitHub Codespaces" នៅក្នុង README
   - កុងតឺន័រ កំណត់ដោយស្វ័យប្រវត្តិក្នុង Python 3.12 និង Ollama ជាមួយ Phi-3

2. បើកនៅក្នុង VS Code Dev Containers៖
   - ប្រើប៊ូតុង "Open in Dev Containers" ពី README
   - កុងតឺន័រត្រូវការចងចាំ 16GB អប្បបរមា

### Local Setup

**លក្ខខណ្ឌមុនបន្ទាន់៖**
- Python 3.12 ឬបន្ទាប់
- .NET 8.0 SDK (សម្រាប់ឧទាហរណ៍ C#)
- Node.js 18+ និង npm (សម្រាប់ឧទាហរណ៍ JavaScript)
- RAM 16GB អប្បបរមាកំណត់

**ការដំឡើង៖**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**សម្រាប់ឧទាហរណ៍ Python៖**
ចូលទៅកាន់ថតឧទាហរណ៍ជាក់លាក់ និងដំឡើងការពឹងផាន់។
```bash
cd code/<example-directory>
pip install -r requirements.txt  # ប្រសិនបើមានឯកសារ requirements.txt
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
npm run dev  # ចាប់ផ្តើមម៉ាស៊ីនមេអភិវឌ្ឍន៍
npm run build  # សង់សម្រាប់ផលិតកម្ម
```

## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - ការណែនាំមូលដ្ឋាន និងគំរូចាប់ផ្តើម
- **03.Finetuning/** និង **04.Finetuning/** - ឧទាហរណ៍ការរៀបចំច្បាស់លាស់នានា
- **03.Inference/** - ឧទាហរណ៍បញ្ចេញទិន្នន័យលើឧបករណ៍ផ្សេងៗ (AIPC, MLX)
- **06.E2E/** - គំរូកម្មវិធីចប់ដល់ចប់
- **07.Lab/** - ការអនុវត្ត សាកល្បង
- **08.RAG/** - ឧទាហរណ៍ការបង្កើតតាមការទាញយក
- **09.UpdateSamples/** - គំរូដែលបានធ្វើបច្ចុប្បន្នភាពថ្មីៗ

### Documentation (`/md/`)

- **01.Introduction/** - មគ្គុទេសក៍ណែនាំ ការតំឡើងវេនvironnement មគ្គុទេសក៍វេទិកា
- **02.Application/** - ឧទាហរណ៍កម្មវិធីតាមប្រភេទ (អត្ថបទ កូដ ទស្សនវិស័យ សំឡេង ល។)
- **02.QuickStart/** - សៀវភៅណែនាំវឌ្ឍនភាពរហ័ស សម្រាប់ Microsoft Foundry និង GitHub Models
- **03.FineTuning/** - ឯកសារទាក់ទងការរៀបចំច្បាស់លាស់ និងមេរៀន
- **04.HOL/** - ការបង្រៀនដៃ (រួមមានឧទាហរណ៍ .NET)

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - មេរៀន Python អន្តរកម្ម ដែលមានរាងសញ្ញា 📓 នៅក្នុង README
- **Python Scripts (`.py`)** - ឧទាហរណ៍ Python ដាច់ដោយឡែក
- **C# Projects (`.csproj`, `.sln`)** - កម្មវិធី និងឧទាហរណ៍ .NET
- **JavaScript (`.js`, `package.json`)** - ឧទាហរណ៍វេប និង Node.js
- **Markdown (`.md`)** - ឯកសារ និងមគ្គុទេសក៍

## Working with Examples

### Running Jupyter Notebooks

ភាគច្រើនឧទាហរណ៍ផ្តល់ជាមេរៀន Jupyter notebooks៖
```bash
pip install jupyter notebook
jupyter notebook  # បើកមុខងាររុករក
# ទៅកាន់ឯកសារ .ipynb ដែលចង់បាន
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

ឬសាងសង់ដំណោះស្រាយទាំងមូល៖
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Running JavaScript/Web Examples

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # ការអភិវឌ្ឍន៍ជាមួយការតំឡើងឡើងវិញឆាប់
```

## Testing

ឃ្លាំងនេះមានកូដឧទាហរណ៍ និងមេរៀន មិនមែនជា​គម្រោងកម្មវិធី​ទីផ្សារ​តែមួយ សម្រាប់ការធ្វើចំនួនតេស្តតែមួយ។ ការផ្ទៀងផ្ទាត់ត្រូវបានអនុវត្តជាទូទៅដោយ៖

1. **ដំណើរការ​ឧទាហរណ៍** - គំរូនីតិវិធីគួរតែដំណើរការ​ដោយគ្មានកំហុស
2. **បញ្ជាក់លទ្ធផល** - ពិនិត្យមើលថាឆ្លើយតបម៉ូដែលត្រឹមត្រូវ
3. **ធ្វើតាមមេរៀន** - មគ្គុទេសក៍គួរតែដំណើរការតាមឯកសារ

**វិធីសាស្រ្តផ្ទៀងផ្ទាត់ទូទៅ៖**
- សាកល្បងដំណើរការ ឧទាហរណ៍នៅវេទិកាគោលដៅ
- ពិនិត្យការដំឡើងការពឹងផាន់ត្រឹមត្រូវ
- ពិនិត្យការទាញយក/ផ្ទុកម៉ូដែលជោគជ័យ
- បញ្ជាក់អាកប្បកិរិយាជាគោលការណ៍ត្រឹមត្រូវជាមួយឯកសារ

## Code Style and Conventions

### General Guidelines

- ឧទាហរណ៍ត្រូវតែច្បាស់ ពន្យល់ល្អ និងមានអត្ថន័យអប់រំ
- តាមបទបញ្ជាជាក់លាក់នៃភាសា (PEP 8 សម្រាប់ Python, ស្តង់ដា C# សម្រាប់ .NET)
- កាន់កាប់គំរូក្នុងការបង្ហាញសមត្ថភាពម៉ូដែល Phi ជាក់លាក់
- រួមបញ្ចូលយល់ដឹងពិពណ៌នាគន្លងគន្លឹះ និងប៉ារ៉ាម៉ែត្រ​ពិសេសម៉ូដែល

### Documentation Standards

**URL Formatting:**
- ប្រើទ្រង់ទ្រាយ `[text](../../url)` ដោយមិនមានចន្លោះច្រើន
- តំណភ្ជាប់សំរាប់ថតបច្ចុប្បន្ន៖ ប្រើ `./`, ថតម្ដាយ: `../`
- មិនប្រើទំព័រផ្នែកភាសាក្នុង URL (មិនប្រើ `/en-us/`, `/en/`)

**Images:**
- បញ្ចូលរូបភាពទាំងអស់ក្នុងថត `/imgs/`
- ប្រើឈ្មោះពិពណ៌នាជាមួយតួអក្សរអង់គ្លេស លេខ និងសញ្ញាសញ្ញាត្រង់
- ឧទាហរណ៍៖ `phi-3-architecture.png`

**Markdown Files:**
- មានយោងទៅឧទាហរណ៍ដែលដំណើរការបានក្នុងថត `/code/`
- ថែរក្សាឯកសារឲ្យស្របជាមួយការផ្លាស់ប្តូរកូដ
- ប្រើជាឯកសារសញ្ញា 📓 សម្រាប់ចំណងជើង Jupyter notebook ក្នុង README

### File Organization

- ឧទាហរណ៍នៅ `/code/` រៀបចំបែបគន្លង/មុខងារ
- ឯកសារ​នៅ `/md/` មានរចនាសម្ព័ន្ធដូចគ្នានឹងកូដបើអាចធ្វើបាន
- ថែរក្សាឯកសារត្រឹមត្រូវ (notebooks, scripts, configs) នៅក្នុងថតបន្ទាប់

## Pull Request Guidelines

### Before Submitting

1. **ពង្រីកឃ្លាំង** ទៅគណនីរបស់អ្នក
2. **បំបែក PR ដោយប្រភេទ៖**
   - ការជួសជុលបញ្ហា ក្នុង PR មួយ
   - ការអាប់ដេតឯកសារ គ្នា PR ផ្សេង
   - ឧទាហរណ៍ថ្មីក្នុង PR ផ្សេងៗ
   - ការកែតម្រូវអក្សរអាចបញ្ចូលសរុប

3. **ដោះស្រាយភាពចលាចលក្នុងការរួមបញ្ចូល៖**
   - បន្ទាន់សម័យសាខា `main` របស់អ្នក មុនបើកកែប្រែ
   - សម្របសម្រួលជាមួយ upstream ជាញឹកញាប់

4. **PR ប្រែសម្រួល៖**
   - ត្រូវរួមបញ្ចូលសម្រាប់ឯកសារទាំងអស់ក្នុងថត
   - ថែរក្សារចនាសម្ព័ន្ធឲ្យស្របនឹងភាសាដើម

### Required Checks

PRs ដំណើរការអ្នកប្រើ GitHub workflows ដើម្បីផ្ទៀងផ្ទាត់៖

1. **ផ្ទៀងផ្ទាត់ផ្លូវតំណ(relative path)** - តំណខាងក្នុងទាំងអស់ត្រូវដំណើរការ
   - សាកល្បងតំណនៅក្នុង VS Code ដោយ Ctrl+Click
   - ប្រើលំនាំផ្លូវពី VS Code (`./` ឬ `../`)

2. **ត្រួតពិនិត្យ URL locale** - URL វេបកម្រិតមិនត្រូវមានភាសាជាតិកំណាត់
   - យកចេញ `/en-us/`, `/en/` ឬកូដភាសាផ្សេងទៀត
   - ប្រើ URL អន្តរជាតិទូទៅ

3. **ត្រួតពិនិត្យ URL ខូច** - URL ទាំងអស់ត្រូវតែគេហទំព័រកូដ 200
   - ពិនិត្យការចូលប្រើតំណ មុនបញ្ជូន
   - សម្គាល់៖ ប្រហែលបរាជ័យដែលកើតឡើងដោយកំណត់បណ្តាញ

### PR Title Format

```
[component] Brief description
```

ឧទាហរណ៍៖
- `[docs] បន្ថែមមេរៀន Phi-4 inference`
- `[code] ជួយដំណើរការ ONNX Runtime`
- `[translation] បន្ថែមបកប្រែជជប៉ុនសម្រាប់មគ្គុទេសក៍ណែនាំ`

## Common Development Patterns

### Working with Phi Models

**Model Loading:**
- ឧទាហរណ៍ប្រើសំណុំបែបបទផ្សេងៗ៖ Transformers, ONNX Runtime, MLX, OpenVINO
- ប្រភេទម៉ូដែលទាញចេញពី Hugging Face, Azure, ឬ GitHub Models
- ពិនិត្យភាពសមរម្យម៉ូដែលជាមួយឧបករណ៍របស់អ្នក (CPU, GPU, NPU)

**Inference Patterns:**
- ការបង្កើតអត្ថបទ: ភាគច្រើនប្រើវ៉ារីយ៉ង់ chat/instruct
- ទស្សនវិស័យ: Phi-3-vision និង Phi-4-multimodal សម្រាប់ការយល់ដឹងរូបភាព
- សំឡេង: Phi-4-multimodal គាំទ្របញ្ចូលសំឡេង
- ការត្រួតពិនិត្យ: Phi-4-reasoning វ៉ារីយ៉ង់សម្រាប់ភារកិច្ចពិចារណាជ្រៅច្រើន

### Platform-Specific Notes

**Microsoft Foundry:**
- តម្រូវឲ្យមានជាវសេវា Azure និង Key API
- មើល `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- មានជួរឥតគិតថ្លៃសម្រាប់សាកល្បង
- មើល `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime៖ មុខងារពហុវេទិកា មានការបង្កើតតំបន់បន្ថែមល្អ
- Ollama៖ គ្រប់គ្រងម៉ូដែលក្នុងតំបន់សាមញ្ញ (បានកំណត់មុនក្នុង dev container)
- Apple MLX៖ ធ្វើបានល្អលើ Apple Silicon

## Troubleshooting

### Common Issues

**Memory Issues:**
- ម៉ូដែល Phi ត្រូវការចងចាំខ្លាំង (ចម្បងសម្រាប់ទស្សនវិស័យ និងម៉ូដែលពហុមុខងារ)
- ប្រើម៉ូដែលQuantizedសម្រាប់បរិយាកាសកម្រ
- មើល `/md/01.Introduction/04/QuantifyingPhi.md`

**Dependency Conflicts:**
- ឧទាហរណ៍ Python អាចមានកំណែជាក់លាក់ត្រូវការណែនាំ
- ប្រើ virtual environments សម្រាប់ឧទាហរណ៍នីមួយៗ
- ពិនិត្យឯកសារ `requirements.txt` ជាក់លាក់

**Model Download Failures:**
- ម៉ូដែលធំពេលខ្លីអាចTimeoutនៅក្នុងការតភ្ជាប់យឺត
- រក្សាបរិយាកាសពពកដូចជា Codespaces, Azure
- ពិនិត្យកាសែល Hugging Face: `~/.cache/huggingface/`

**.NET Project Issues:**
- ត្រូវដំឡើង .NET 8.0 SDK
- ប្រើ `dotnet restore` មុនការសាងសង់
- អនុគ្រោះកំណត់ CUDA ជាពិសេស (Debug_Cuda)

**JavaScript/Web Examples:**
- ប្រើ Node.js 18+ សម្រាប់ការសម្របសម្រួល
- លាង `node_modules` និងដំឡើងឡើងវិញ ប្រសិនបើមានបញ្ហា
- ពិនិត្យកុងសូលប្រព័ន្ធរុករកសម្រាប់បញ្ហា WebGPU

### Getting Help

- **Discord:** ចូលរួម Microsoft Foundry Community Discord
- **GitHub Issues:** រាយការណ៍កំហុស និងបញ្ហាផ្សេងៗ
- **GitHub Discussions:** សួរបញ្ហា និងចែករំលែកចំណេះដំណឹង

## Additional Context

### Responsible AI

ការប្រើម៉ូដែល Phi ទាំងអស់គួរតែអនុវត្តតាមគោលការណ៍ Responsible AI របស់ Microsoft៖
- តុល្យភាព ភាពទុកចិត្ត សុវត្ថិភាព
- ឯកជនភាព និងសុវត្ថិភាព  
- រួមបញ្ចូល ការបង្ហាញមុខ និងការទទួលខុសត្រូវ
- ប្រើ Azure AI Content Safety សម្រាប់កម្មវិធីផលិតកម្ម
- មើល `/md/01.Introduction/01/01.AISafety.md`

### Translations

- គាំទ្រជាង ៥០ ភាសា តាម GitHub Action ដោយស្វ័យប្រវត្តិ
- ឯកសារប្រែសម្រួលនៅក្នុង `/translations/`
- រក្សាដោយកម្មវិធី co-op-translator workflow
- មិនត្រូវកែប្រែឯកសារប្រែដោយដៃ (បង្កើតដោយស្វ័យប្រវត្តិ)

### Contributing

- អនុវត្តតាមគោលការណ៍ក្នុង `CONTRIBUTING.md`
- យល់ព្រមលើ Contributor License Agreement (CLA)
- គោរពគោលការណ៌ Microsoft Open Source Code of Conduct
- ផ្តោតលើសុវត្ថិភាព និងសំងាត់ក្នុង commit មិនបញ្ចូល

### Multi-Language Support

នេះគឺជាឃ្លាំងភាសាចម្រើនដែលមានឧទាហរណ៍ក្នុង៖
- **Python** - ការងារ ML/AI, Jupyter notebooks, fine-tuning
- **C#/.NET** - កម្មវិធីសម្រាប់សហគ្រាស, រួមបញ្ចូល ONNX Runtime
- **JavaScript** - AI លើវេប, inference ជាមួយ WebGPU នៅក្នុងរុករក

ជ្រើសភាសាដែលសមស្របបំផុតសម្រាប់ករណីប្រើ និងគោលដៅបញ្ចេញផ្សាយរបស់អ្នក។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេល​យើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកជាប្រភពដែលមានសមត្ថកិច្ច។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ ប្រាប់សូមប្រើការបកប្រែមនុស្សជំនាញជាដំណោះស្រាយ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->