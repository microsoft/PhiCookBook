## C# ಬಳಸಿ Phi ಪ್ರಯೋಗಾಲಯಗಳಿಗೆ ಸುಸ್ವಾಗತ

ಇಲ್ಲಿ .NET ಪರಿಸರದಲ್ಲಿ Phi ಮಾದರಿಗಳ ಬಲಿಷ್ಠ ವಿಭಿನ್ನ ಆವೃತ್ತಿಗಳನ್ನು ಹೇಗೆ ಸಂಯೋಜಿಸುವುದನ್ನು ಪ್ರದರ್ಶಿಸುವ ಕೆಲವು ಪ್ರಯೋಗಾಲಯಗಳ ಆಯ್ಕೆಯಿದೆ.

## ಅಗತ್ಯಶರತ್ತುಗಳು

ಸ್ಯಾಂಪಲ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡುವ ಮೊದಲು, ಕೆಳಕಂಡವುಗಳನ್ನು ನಿಮ್ಮ ಯಂತ್ರದಲ್ಲಿ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿದ್ದೀರಾ ಎಂಬುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

**.NET 9:** ನಿಮ್ಮ ಯಂತ್ರದಲ್ಲಿ [ಇತ್ತೀಚಿನ .NET ಆವೃತ್ತಿ](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿಟ್ಟಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

**(ಐಚ್ಛಿಕ) Visual Studio ಅಥವಾ Visual Studio Code:** ನಿಮಗೆ .NET ಪ್ರಾಜೆಕ್ಟ್‌ಗಳನ್ನು ರನ್ ಮಾಡಲು ಸಾಮರ್ಥ್ಯ ಹೊಂದಿರುವ IDE ಅಥವಾ ಕೋಡ್ ಎಡಿಟರ್ ಬೇಕಾಗುತ್ತದೆ. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ಅಥವಾ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತವೆ.

**Using git** ಸ್ಥಳೀಯವಾಗಿ ಲಭ್ಯವಿರುವ Phi-3, Phi3.5 ಅಥವಾ Phi-4 ಆವೃತ್ತಿಗಳಲ್ಲಿ ಒಂದನ್ನು [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) ನಿಂದ ಕ್ಲೋನ್ ಮಾಡಿ.

**Download Phi-4 ONNX models** ನಿಮ್ಮ ಸ್ಥಳೀಯ ಯಂತ್ರಕ್ಕೆ:

### ಮಾದರಿಗಳನ್ನು ಸಂಗ್ರಹಿಸಲು ಫೋಲ್ಡರ್‌ಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ

```bash
cd c:\phi\models
```

### lfs ಗೆ ಬೆಂಬಲ ಸೇರಿಸಿ

```bash
git lfs install 
```

### Phi-4 mini instruct ಮಾದರಿಯನ್ನು ಮತ್ತು Phi-4 multi modal ಮಾದರಿಯನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ ಮತ್ತು ಡೌನ್ಲೋಡ್ ಮಾಡಿ

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Download the Phi-3 ONNX models** ನಿಮ್ಮ ಸ್ಥಳೀಯ ಯಂತ್ರಕ್ಕೆ:

### Phi-3 mini 4K instruct ಮಾದರಿ ಮತ್ತು Phi-3 vision 128K ಮಾದರಿಯನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ ಮತ್ತು ಡೌನ್ಲೋಡ್ ಮಾಡಿ

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**ಗಮನವಿರಲಿ:** ಪ್ರಸ್ತುತ ಡೆಮೋಗಳು ಮಾದರಿಗಳ ONNX ಆವೃತ್ತಿಗಳನ್ನು ಬಳಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ. ಮೇಲಿನ ಹಂತಗಳು ಕೆಳಗಿನ ಮಾದರಿಗಳನ್ನು ಕ್ಲೋನ್ ಮಾಡುತ್ತವೆ.

## ಪ್ರಯೋಗಾಲಯಗಳ ಬಗ್ಗೆ

ಮುಖ್ಯ ಸೊಲ್ಯೂಶನ್‌ನಲ್ಲಿ C# ಬಳಸಿಕೊಂಡು Phi ಮಾದರಿಗಳ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತೋರಿಸುವ ಹಲವಾರು ಉದಾಹರಣಾ ಪ್ರಯೋಗಾಲಯಗಳಿವೆ.

| Project | Model | Description |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 or Phi-3.5 | ಬಳಕೆದಾರರಿಗೆ ಪ್ರಶ್ನೆಗಳು ಕೇಳಲು ಅನುಮತಿಸುವ ಉದಾಹರಣಾ ಕಾನ್ಸೋಲ್ ಚಾಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ ONNX Phi-3 ಮಾದರಿಯನ್ನು `Microsoft.ML.OnnxRuntime` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | ಬಳಕೆದಾರರಿಗೆ ಪ್ರಶ್ನೆಗಳು ಕೇಳಲು ಅನುಮತಿಸುವ ಉದಾಹರಣಾ ಕಾನ್ಸೋಲ್ ಚಾಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ ONNX Phi-3 ಮಾದರಿಯನ್ನು `Microsoft.Semantic.Kernel` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | ಇದು ಸ್ಥಳೀಯ Phi-3 ವಿಸನ್ ಮಾದರಿಯನ್ನು ಬಳಸಿಕೊಂಡು ಚಿತ್ರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸುವ ಉದಾಹರಣಾ ಪ್ರಾಜೆಕ್ಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ ONNX Phi-3 Vision ಮಾದರಿಯನ್ನು `Microsoft.ML.OnnxRuntime` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | ಇದು ಸ್ಥಳೀಯ Phi-3 ವಿಸನ್ ಮಾದರಿಯನ್ನು ಬಳಸಿಕೊಂಡು ಚಿತ್ರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸುವ ಉದಾಹರಣಾ ಪ್ರಾಜೆಕ್ಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ ONNX Phi-3 Vision ಮಾದರಿಯನ್ನು `Microsoft.ML.OnnxRuntime` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ. ಪ್ರಾಜೆಕ್ಟ್ ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ವಿವಿಧ ಆಯ್ಕೆಗಳನ್ನು ಒಳಗೊಂಡ ಮெனುವನ್ನು ಸಹ ನೀಡುತ್ತದೆ. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | ಬಳಕೆದಾರರಿಗೆ ಪ್ರಶ್ನೆಗಳು ಕೇಳಲು ಅನುಮತಿಸುವ ಉದಾಹರಣಾ ಕಾನ್ಸೋಲ್ ಚಾಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ ONNX Phi-4 ಮಾದರಿಯನ್ನು `Microsoft.ML.OnnxRuntime` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | ಬಳಕೆದಾರರಿಗೆ ಪ್ರಶ್ನೆಗಳು ಕೇಳಲು ಅನುಮತಿಸುವ ಉದಾಹರಣಾ ಕಾನ್ಸೋಲ್ ಚಾಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ ONNX Phi-4 ಮಾದರಿಯನ್ನು `Semantic Kernel` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | ಬಳಕೆದಾರರಿಗೆ ಪ್ರಶ್ನೆಗಳು ಕೇಳಲು ಅನುಮತಿಸುವ ಉದಾಹರಣಾ ಕಾನ್ಸೋಲ್ ಚಾಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ ONNX Phi-4 ಮಾದರಿಯನ್ನು `Microsoft.ML.OnnxRuntimeGenAI` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ ಮತ್ತು `Microsoft.Extensions.AI` ನಿಂದ `IChatClient` ಅನ್ನು ಅಂಶಗೊಳಿಸುತ್ತದೆ. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | ಬಳಕೆದಾರರಿಗೆ ಪ್ರಶ್ನೆಗಳು ಕೇಳಲು ಅನುಮತಿಸುವ ಉದಾಹರಣಾ ಕಾನ್ಸೋಲ್ ಚಾಟ್. ಚಾಟ್ ಮೆಮೊರಿ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುತ್ತದೆ. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | ಇದು ಸ್ಥಳೀಯ Phi-4 ಮಾದರಿಯನ್ನು ಬಳಸಿಕೊಂಡು ಚಿತ್ರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ಫಲಿತಾಂಶವನ್ನು ಕಾನ್ಸೋಲ್‌ನಲ್ಲಿ ತೋರಿಸುವ ಉದಾಹರಣಾ ಪ್ರಾಜೆಕ್ಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ Phi-4-`multimodal-instruct-onnx` ಮಾದರಿಯನ್ನು `Microsoft.ML.OnnxRuntime` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | ಇದು ಸ್ಥಳೀಯ Phi-4 ಮಾದರಿಯನ್ನು ಬಳಸಿಕೊಂಡು ಆಡಿಯೋ ಫೈಲ್ ಅನ್ನು ವಿಶ್ಲೇಷಿಸುವ, ಫೈಲ್‌ನ ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಉತ್ಪಾದಿಸುವ ಮತ್ತು ಫಲಿತಾಂಶವನ್ನು ಕಾನ್ಸೋಲ್‌ನಲ್ಲಿ ತೋರಿಸುವ ಉದಾಹರಣಾ ಪ್ರಾಜೆಕ್ಟ್. ಪ್ರಾಜೆಕ್ಟ್ ಸ್ಥಳೀಯ Phi-4-`multimodal-instruct-onnx` ಮಾದರಿಯನ್ನು `Microsoft.ML.OnnxRuntime` ಲೈಬ್ರರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಲೋಡ್ ಮಾಡುತ್ತದೆ. |

## ಪ್ರಾಜೆಕ್ಟ್‌ಗಳನ್ನು ಹೇಗೆ ಚಾಲನೆ ಮಾಡುವುದು

ಪ್ರಾಜೆಕ್ಟ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಲು, ಈ ಕ್ರಮಗಳನ್ನು ಅನುಸರಿಸಿ:

1. ರೆಪೊಸಿಟೋರಿಯನ್ನು ನಿಮ್ಮ ಸ್ಥಳೀಯ ಯಂತ್ರಕ್ಕೆ ಕ್ಲೋನ್ ಮಾಡಿ.

1. ಒಂದು ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಬೇಕಾದ ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ. ಉದಾಹರಣೆಗೆ, `LabsPhi4-Chat-01OnnxRuntime` ಅನ್ನು ರನ್ ಮಾಡೋಣ.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. ಈ ಕೆಳಗಿನ ಕಮಾಂಡ್ ಬಳಸಿ ಪ್ರಾಜೆಕ್ಟ್ ಅನ್ನು ರನ್ ಮಾಡಿ

    ```bash
    dotnet run
    ```

1. ಸ್ಯಾಂಪಲ್ ಪ್ರಾಜೆಕ್ಟ್ ಬಳಕೆದಾರದ ಇನ್‌ಪುಟ್ ಅನ್ನು ಕೇಳುತ್ತದೆ ಮತ್ತು ಸ್ಥಳೀಯ ಮೋಡ್ ಅನ್ನು ಬಳಸಿಕೊಂಡು ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ. 

   ಚಾಲನೆಯಲ್ಲಿರುವ ಡೆಮೊ ಈ ಕೆಳಗಿನಂತಿದೆ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಿಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದೆಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆಯನ್ನು ಪ್ರಾಮಾಣಿಕ ಮತ್ತು ಅಧಿಕಾರಿನ ಮೂಲ ಎಂದು ಪರಿಗಣிக்கಬೇಕು. ಗಂಭೀರವಾದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಭ್ರಮೆಗಳು ಅಥವಾ ತಪ್ಪು ಅರ್ಥಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರಿಯಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->