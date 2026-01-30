## C# ഉപയോഗിച്ച് Phi ലാബുകളിലേക്ക് സ്വാഗതം

ഇവിടെയുള്ള ലാബുകൾ .NET പരിസ്ഥിതിയിൽ Phi മോഡലുകളുടെ വിവിധ ശക്തമായ പതിപ്പുകൾ എങ്ങനെ സംയോജിപ്പിക്കാമെന്നത് പ്രദർശിപ്പിക്കുന്നു.

## മുൻഅവശ്യങ്ങൾ

സാമ്പിൾ നടപ്പാക്കുന്നതിന്റെ മുമ്പ്, നിങ്ങളുടെ യന്ത്രത്തിൽ താഴെപ്പറയുന്നവ ഇൻസ്റ്റാൾ ചെയ്‌തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക:

**.NET 9:** നിങ്ങളുടെ യന്ത്രത്തിൽ [latest version of .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് 확인 ചെയ്യുക.

**(Optional) Visual Studio or Visual Studio Code:** നിങ്ങൾക്ക് .NET പ്രോജക്ടുകൾ റൺ ചെയ്യാൻ കഴിയുന്ന ഒരു IDE അല്ലെങ്കിൽ കോഡ് എഡിറ്റർ ആവശ്യമുണ്ട്. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) അല്ലെങ്കിൽ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) നിർദ്ദേശിക്കുന്നു.

**Using git** നിങ്ങളുടെ യന്ത്രത്തിൽ ലോക്കലി Phi-3, Phi3.5 അല്ലെങ്കിൽ Phi-4 പതിപ്പുകളിൽ നിന്ന് ഒന്നുകിൽ ക്ലോൺ ചെയ്യുക: [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Download Phi-4 ONNX models** നിങ്ങളുടെ ലോക്കൽ യന്ത്രത്തിലേക്ക് ഡൗൺലോഡ് ചെയ്യുക:

### മോഡലുകൾ സൂക്ഷിക്കാൻ ഫോൾഡറിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക

```bash
cd c:\phi\models
```

### lfs നു പിന്തുണ ചേർക്കുക

```bash
git lfs install 
```

### Phi-4 mini instruct മോഡലും Phi-4 multi modal മോഡലും ക്ലോൺ ചെയ്ത് ഡൗൺലോഡ് ചെയ്യുക

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Download the Phi-3 ONNX models** നിങ്ങളുടെ ലോക്കൽ യന്ത്രത്തിലേക്ക് ഡൗൺലോഡ് ചെയ്യുക:

### Phi-3 mini 4K instruct മോഡലും Phi-3 vision 128K മോഡലും ക്ലോൺ ചെയ്ത് ഡൗൺലോഡ് ചെയ്യുക

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Important:** നിലവിലുള്ള ഡെമോകൾ മോഡലുകളുടെ ONNX പതിപ്പുകൾ ഉപയോഗിക്കാൻ രൂപകൽപ്പന ചെയ്തവയാണ്. മുകളിൽ നൽകിയ ഘട്ടങ്ങൾ താഴെപ്പറയുന്ന മോഡലുകൾ ക്ലോൺ ചെയ്യുന്നു.

## ലാബുകളെപ്പറ്റി

പ്രധാന സൊല്യൂഷനിൽ C# ഉപയോഗിച്ച് Phi മോഡലുകളുടെ ശേഷികളെ കാണിക്കുന്ന നിരവധി സാമ്പിൾ ലാബുകൾ ഉൾപ്പെടുന്നിട്ടുള്ളവയാണ്.

| Project | Model | Description |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 or Phi-3.5 | ഉപയോക്താവിന് ചോദ്യങ്ങൾ ചോദിക്കാൻ അനുവദിക്കുന്ന സാമ്പിൾ കൺസോൾ ചാറ്റ്. പ്രോജക്ട് ലോക്കൽ ONNX Phi-3 മോഡൽ `Microsoft.ML.OnnxRuntime` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | ഉപയോക്താവിന് ചോdaşകൾ ചോദിക്കാൻ അനുവദിക്കുന്ന സാമ്പിൾ കൺസോൾ ചാറ്റ്. പ്രോജക്ട് ലോക്കൽ ONNX Phi-3 മോഡൽ `Microsoft.Semantic.Kernel` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | ഇത് ലോക്കൽ phi3 vision മോഡൽ ഉപയോഗിച്ച് ചിത്രങ്ങൾ വിശകലനം ചെയ്യുന്നതിനുള്ള സാമ്പിൾ പ്രോജക്റ്റാണ്. പ്രോജക്ട് ലോക്കൽ ONNX Phi-3 Vision മോഡൽ `Microsoft.ML.OnnxRuntime` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | ഇത് ലോക്കൽ phi3 vision മോഡൽ ഉപയോഗിച്ച് ചിത്രങ്ങൾ വിശകലനം ചെയ്യുന്നതിനുള്ള സാമ്പിൾ പ്രോജക്റ്റ് ആണ്. പ്രോജക്ട് ലോക്കൽ ONNX Phi-3 Vision മോഡൽ `Microsoft.ML.OnnxRuntime` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു. പ്രോജക്ട് ഉപയോക്താവുമായി ഇന്ററാക്റ്റ് ചെയ്യാനുള്ള വിവിധ ഓപ്ഷനുകൾ നൽകിയ ഒരു മെനുവും ഉൾക്കൊള്ളുന്നു. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | ഉപയോക്താവിന് ചോദ്യങ്ങൾ ചോദിക്കാൻ അനുവദിക്കുന്ന സാമ്പിൾ കൺസോൾ ചാറ്റ്. പ്രോജക്ട് ലോക്കൽ ONNX Phi-4 മോഡൽ `Microsoft.ML.OnnxRuntime` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | ഉപയോക്താവിന് ചോദ്യങ്ങൾ ചോദിക്കാൻ അനുവദിക്കുന്ന സാമ്പിൾ കൺസോൾ ചാറ്റ്. പ്രോജക്ട് ലോക്കൽ ONNX Phi-4 മോഡൽ `Semantic Kernel` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | ഉപയോക്താവിന് ചോദ്യങ്ങൾ ചോദിക്കാൻ അനുവദിക്കുന്ന സാമ്പിൾ കൺസോൾ ചാറ്റ്. പ്രോജക്ട് ലോക്കൽ ONNX Phi-4 മോഡൽ `Microsoft.ML.OnnxRuntimeGenAI` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു және `IChatClient` `Microsoft.Extensions.AI` -ൽ നിന്ന് നടപ്പിലാക്കുന്നു. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | ഉപയോക്താവിന് ചോദ്യങ്ങൾ ചോദിക്കാൻ അനുവദിക്കുന്ന സാമ്പിൾ കൺസോൾ ചാറ്റ്. ചാറ്റ് മെമ്മറി നടപ്പിലാക്കുന്നു. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | ഇത് ലോക്കൽ Phi-4 മോഡൽ ഉപയോഗിച്ച് ചിത്രങ്ങൾ വിശകലനം ചെയ്ത് ഫലങ്ങൾ കൺസോളിൽ പ്രദർശിപ്പിക്കുന്ന സാമ്പിൾ പ്രോജക്റ്റാണ്. പ്രോജക്ട് ലോക്കൽ Phi-4-`multimodal-instruct-onnx` മോഡൽ `Microsoft.ML.OnnxRuntime` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | ഇത് ഒരു ഓഡിയോ ഫയൽ വിശകലനം ചെയ്യാൻ, ഫയലിന്റെ ട്രാൻസ്‌ക്രിപ്റ്റ് സൃഷ്ടിക്കാൻ, ഫലം കൺസോളിൽ കാണിക്കാൻ ഉപയോഗിക്കുന്ന ലോക്കൽ Phi-4 മോഡൽ ഉപയോഗിക്കുന്ന സാമ്പിൾ പ്രോജക്റ്റാണ്. പ്രോജക്ട് ലോക്കൽ Phi-4-`multimodal-instruct-onnx` മോഡൽ `Microsoft.ML.OnnxRuntime` ലൈബ്രറികൾ ഉപയോഗിച്ച് ലോഡ് ചെയ്യുന്നു. |

## പ്രോജക്ടുകൾ എങ്ങനെ റൺ ചെയ്യാം

പ്രോജക്ടുകൾ റൺ ചെയ്യാനായി, ഈ നടപടിക്രമങ്ങൾ പിന്തുടരുക:

1. റിപ്പോസിറ്ററി നിങ്ങളുടെ ലോക്കൽ യന്ത്രത്തിലേക്ക് ക്ലോൺ ചെയ്യുക.

1. ടർമിനൽ തുറന്ന് ആഗ്രഹിക്കുന്ന പ്രോജക്റ്റിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക. ഉദാഹരണത്തിന്, നമുക്ക് `LabsPhi4-Chat-01OnnxRuntime` റൺ ചെയ്യാം.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. പ്രോജക്ട് താഴെ പറയുന്ന കമാൻഡ് ഉപയോഗിച്ച് റൺ ചെയ്യുക

    ```bash
    dotnet run
    ```

1. സാമ്പിൾ പ്രോജക്ട് ഉപയോക്തൃ ഇൻപുട്ട് ആവശ്യപ്പെടുകയും ലോക്കൽ മോഡ് ഉപയോഗിച്ച് മറുപടി നല്‍കുകയും ചെയ്യും. 

   റൺ ചെയ്ത ഡെമോ ഏകദേശം ഇതുപോലെയാണ്:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
വിവരണക്കുറിപ്പ്:
ഈ ഡോക്യുമെന്റ് AI വിവർത്തനസേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിരുന്നെങ്കിലും, യന്ത്രം നിർവഹിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകളോ അസ്ഥിരതയോ ഉണ്ടായിരിക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. मूल ഭാഷയിലുള്ള മൂല ഡോക്യുമെന്റ് ആണ് അതിന്റെ കാര്യത്തിൽ ഔദ്യോഗിക ഉറവിടമെന്ന് നിഗമനീയം. നിർണായക വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകളോ തെറ്റായി വ്യാഖ്യാനങ്ങളോ സംബന്ധിച്ച് നാം ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->