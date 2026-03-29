# **ನಿಮ್ಮದೇ Visual Studio Code GitHub Copilot ಚಾಟ್ ಅನ್ನು Microsoft Phi-3 ಕುಟುಂಬದೊಂದಿಗೆ ನಿರ್ಮಿಸಿ**

ನೀವು GitHub Copilot ಚಾಟ್‌ನಲ್ಲಿ ವರ್ಕ್‌ಸ್ಪೇಸ್ ಏಜೆಂಟ್ ಅನ್ನು ಬಳಸಿದ್ದೀರಾ? ನಿಮ್ಮ ಬಳಗದ ಕೋಡ್ ಏಜೆಂಟ್ ಅನ್ನು ನೀವು ನಿರ್ಮಿಸಲು ಇಚ್ಛಿಸುವಿರಾ? ಈ ಹ್ಯಾಂಡ್ಸ್-ಆನ್ ಲ್ಯಾಬ್ ಖಲಿಗ್ಗಿತ ಮಾದರಿಯನ್ನು ಬಳಸಿ ಎಂಟರ್‌ಪ್ರೈಸ್-ಮಟ್ಟದ ಕೋಡ್ ವ್ಯವಹಾರದ ಏಜೆಂಟನ್ನು ನಿರ್ಮಿಸುವ ನಿರೀಕ್ಷೆಯನ್ನು ಹೊಂದಿದೆ.

## **ಮೂಲಾಧಾರ**

### **ಯಾಕೆ Microsoft Phi-3 ಆಯ್ಕೆ ಮಾಡಬೇಕು**

Phi-3 ಒಂದು ಕುಟುಂಬ ಸರಣಿಯಾಗಿದೆ, ಇದರಲ್ಲಿ ಪಠ್ಯ ರಚನೆ, ಸಂವಾದ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ಮತ್ತು ಕೋಡ್ ರಚನೆಗಾಗಿ ವಿವಿಧ ತರಬೇತಿ ಪರಾಮಿತಿಗಳ ಆಧಾರದ ಮೇಲೆ phi-3-mini, phi-3-small, ಮತ್ತು phi-3-medium ಸೇರಿವೆ. Vision ಆಧಾರಿತ phi-3-vision ಕೂಡ ಇದೆ. ಇದು ಎಂಟರಪ್ರೈಸ್ಗಳು ಅಥವಾ ವಿವಿಧ ತಂಡಗಳಿಗೆ ಆಫ್‌ಲೈನ್ ಜನರೇಟಿವ್ AI ಪರಿಹಾರಗಳನ್ನು ರಚಿಸಲು ಸೂಕ್ತವಾಗಿದೆ.

ಈ ಲಿಂಕ್ ಅನ್ನು ಓದಲು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot ಚಾಟ್ ವಿಸ್ತರಣೆಯು VS Code ನಲ್ಲಿ ನೇರವಾಗಿ GitHub Copilot ಜೊತೆಗೆ ಸಂವಾದ ಮಾಡಲು ಮತ್ತು ಕೋಡಿಂಗ್ ಸಂಬಂಧಿತ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಗಳನ್ನು ಪಡೆಯಲು ಸಂವಾದ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ಒದಗಿಸುತ್ತದೆ, ದಸ್ತಾವೇಜುಗಳನ್ನು ಅನ್ವೇಷಿಸುವ ಅಥವಾ ಆನ್ಲೈನ್ ಫೋರಮ್‌ಗಳನ್ನು ಹುಡುಕುವ ಅಗತ್ಯವಿಲ್ಲದೆ.

Copilot ಚಾಟ್ ರಚಿಸಿದ ಪ್ರತಿಕ್ರಿಯೆಗೆ ಸ್ಪಷ್ಟತೆಯನ್ನು ಸೇರಿಸಲು ಸಿಂಟ್ಯಾಕ್ಸ್ ಹೈಲೈಟಿಂಗ್, ಇಂದೆಂಟೇಷನ್ ಮತ್ತು ಇತರ ಸ್ವರೂಪಣಾ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನೂ ಬಳಸಬಹುದು. ಬಳಕೆದಾರರಿಂದ ಪ್ರಶ್ನೆಯ ಪ್ರಕಾರ, ಫಲಿತಾಂಶದಲ್ಲಿ ಪ್ರತಿಕ್ರಿಯೆ ನಿರ್ಮಿಸಲು Copilot ಬಳಸಿದ ಸಂದರ್ಭಗಳ ಲಿಂಕ್ಸ್ (ಮೂಲ ಕೋಡ್ ಫೈಲ್‌ಗಳು ಅಥವಾ ಡಾಕ್ಯುಮೆಂಟೇಶನ್) ಅಥವಾ VS Code ಕಾರ್ಯಕ್ಷಮತೆಗಳಿಗೆ ಪ್ರವೆಶಿಸಲು ಬಟನ್‌ಗಳು ಸೇರಿರಬಹುದು.

- Copilot ಚಾಟ್ ನಿಮ್ಮ ಡೆವಲಪರ್ ಕಾರ್ಯप्रವಾಹಕ್ಕೆ ಸೇರ್ಚి ನೀವು ಬೇಕಾದಲ್ಲಿ ಸಹಾಯವನ್ನು ನೀಡುತ್ತದೆ:

- ಶಿಕ್ಷಣದೃಷ್ಟಿಯಿಂದ ಸಂವಾದವನ್ನು ನೇರವಾಗಿ ಎಡಿಟರ್ ಅಥವಾ ಟರ್ಮಿನಲ್ ನಿಂದ ಪ್ರಾರಂಭಿಸಿ, ಕೋಡ್ ಮಾಡುತ್ತಿರುವಾಗ ಸಹಾಯ ಪಡೆಯಿರಿ

- ಚಾಟ್ ವೀಕ್ಷಣೆಯನ್ನು ಬಳಸಿ ಯಾವುದೇ ವೇಳೆ AI ಸಹಾಯಕನನ್ನು ಕೈಪಿಡಿಯಾಗಿ ಒಪ್ಪಿಕೊಳ್ಳಿ

- ಗುರುತಿಸು ಚಾಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ತ್ವರಿತ ಪ್ರಶ್ನೆಯನ್ನು ಕೇಳಿ ಮತ್ತು ನಿಮ್ಮ ಕೆಲಸದ ಕಡೆ ಮರಳಿರಿ

GitHub Copilot ಚಾಟ್ ಅನ್ನು ಹಲವು ಸಂದರ್ಭಗಳಲ್ಲಿ ಬಳಸಬಹುದು, ಉದಾಹರಣೆಗೆ:

- ಸಮಸ್ಯೆಯನ್ನು ಅತ್ಯುತ್ತಮವಾಗಿ ಹೇಗೆ ಪರಿಹರಿಸುವುದೆಂಬುದರ ಬಗ್ಗೆ ಕೋಡಿಂಗ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸುವುದು

- ಬೇರೆ ಯಾರಾದರೂ ಬರೆದ ಕೋಡ್ ಅನ್ನು ವಿವರಿಸುವುದು ಮತ್ತು ಸುಧಾರಣೆಗಳನ್ನು ಸೂಚಿಸುವುದು

- ಕೋಡ್ ಸರಿಪಡಿಸುವಿಕೆಗಳನ್ನು ಪ್ರಸ್ತಾಪಿಸುವುದು

- ಯೂನಿಟ್ ಟೆಸ್ಟ್ ಕೇಸ್‌ಗಳನ್ನು ರಚಿಸುವುದು

- ಕೋಡ್ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಸೃಷ್ಟಿಸುವುದು

ಈ ಲಿಂಕ್ ಅನ್ನು ಓದಿರಿ [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Copilot ಚಾಟ್‌ನಲ್ಲಿ **@workspace** ಅನ್ನು ಉಲ್ಲೇಖಿಸುವುದರಿಂದ ನೀವು ನಿಮ್ಮ ಸಂಪೂರ್ಣ ಕೋಡ್‌ಬೇಸ್ ಕುರಿತು ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳಬಹುದು. ಪ್ರಶ್ನೆಯ ಆಧಾರದ ಮೇಲೆ, Copilot ಬುದ್ಧಿವಂತಿಕೆಯಿಂದ ಸಂಬಂಧಿತ ಫೈಲ್‌ಗಳು ಮತ್ತು ಸಿಂಬಲ್ಗಳನ್ನು ಪಡೆಯುತ್ತದೆ ಮತ್ತು ನಂತರ ಲಿಂಕ್‌ಗಳು ಮತ್ತು ಕೋಡ್ ಉದಾಹರಣೆಗಳಾಗಿ ತನ್ನ ಉತ್ತರದಲ್ಲಿ ರೆಫರೆನ್ಸ್ ಮಾಡುತ್ತದೆ.

ನಿಮ್ಮ ಪ್ರಶ್ನೆಗೆ ಉತ್ತರಿಸಲು **@workspace** VS Codeನಲ್ಲಿ ಡೆವಲಪರ್ ಕೋಡ್‌ಬೇಸ್ ನಾವಿಗೇಟ್ ಮಾಡುವಾಗ ಬಳಸುವ ಅದರೇ ಮೂಲಗಳನ್ನು ಹುಡುಕುತ್ತದೆ:

- .gitignore ಫೈಲ್ ಮೂಲಕ ಹೊರತುಪಡಿಸಲಾಗದ ಎಲ್ಲಾ ಫೈಲ್‌ಗಳು ಮತ್ತು ವರ್ಕ್‌ಸ್ಪೇಸ್‌ನ ಫೈಲ್‌ಗಳು

- ಅಂತರಗತ ಫೋಲ್ಡರ್ ಮತ್ತು ಫೈಲ್ ಹೆಸರಿನೊಂದಿಗೆ ಡೈರೆಕ್ಟರಿ ರಚನೆ

- ವರ್ಕ್‌ಸ್ಪೇಸ್ GitHub ಸಂಗ್ರಹ ಮತ್ತು ಕೋಡ್ ಹುಡುಕು ಸೂಚ್ಯಂಕ, ಇದು GitHub ರಿಪೋಜಿಟರಿ ಆಗಿದ್ದರೆ ಮತ್ತು ಕೋಡ್ ಹುಡುಕಾಟದಿಂದ ಸೂಚ್ಯಂಕವನ್ನು ಹೊಂದಿದ್ದರೆ

- ವರ್ಕ್‌ಸ್ಪೇಸ್‌ನಲ್ಲಿನ ಚಿಹ್ನೆಗಳು ಮತ್ತು ವ್ಯಾಖ್ಯಾನಗಳು

- ಪ್ರಸ್ತುತ ಆಯ್ಕೆಮಾಡಲಾದ ಪಠ್ಯ ಅಥವಾ ಸಕ್ರಿಯ ಎಡಿಟರ್‌ನಲ್ಲಿ ಕಂಡುಬರುವ ಪಠ್ಯ

ಗಮನಿಸಿ: ನೀವು ನಿರ್ಲಕ್ಷಿಸಲ್ಪಟ್ಟ ಫೈಲ್‌ನೊಳಗೆ ಫೈಲ್ ತೆರೆಯಲಿದ್ದರೆ ಅಥವಾ ಪಠ್ಯ ಆಯ್ಕೆಮಾಡಿರುತ್ತಿದ್ದರೆ .gitignore ಬypass ಆಗುತ್ತದೆ.

ಈ ಲಿಂಕ್ ಅನ್ನು ಓದಿ [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **ಈ ಲ್ಯಾಬ್ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ತಿಳಿದುಕೊಳ್ಳಿ**

GitHub Copilot ಎಂಟರ್‌ಪ್ರೈಸ್‌ಗಳ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ದಕ್ಷತೆಯನ್ನು ಬಹುತೇಕ ಸುಧಾರಿಸಿದೆ, ಪ್ರತಿಯೊಂದು ಎಂಟರ್ಪ್ರೈಸ್ GitHub Copilot ಸಂಬಂಧಿತ ಕಾರ್ಯಗಳಿಂದ ಸಂಯೋಜಿಸಿಕೊಳ್ಳಲು ಬಯಸುತ್ತದೆ. ಹಲವು ಎಂಟರ್ಪ್ರೈಸುಗಳು ತಮ್ಮ ಸ್ವಂತ ವ್ಯಾಪಾರದ ಸಂದರ್ಭಗಳು ಮತ್ತು ಮುಕ್ತ ಮೂಲ ಮಾದರಿಗಳ ಆಧಾರದಲ್ಲಿ GitHub Copilot ಅನ್ನು ಅನುರೂಪಗೊಳಿಸಿದ ವಿಸ್ತರಣೆಗಳನ್ನು ಹೊಂದಿವೆ. ಎಂಟರ್ಪ್ರೈಸ್‌ಗಳಿಗೆ, ಕಸ್ಟಮೈಸ್ ಮಾಡಿದ ವಿಸ್ತರಣೆಗಳನ್ನು ನಿಯಂತ್ರಿಸುವುದು ಸುಲಭವಾಗಿದೆ, ಆದರೆ ಇದು ಬಳಕೆದಾರರ ಅನುಭವವನ್ನು ಪರಿಣಾಮ ಬೀರುತ್ತದೆ. ಎಲ್ಲದರಲ್ಲೂ, ಸಾಮಾನ್ಯ ಸಂದರ್ಭಗಳು ಮತ್ತು ವೃತ್ತಿಪರತೆಯಲ್ಲಿ GitHub Copilot ಹೆಚ್ಚು ಶಕ್ತಿ ಹೊಂದಿದೆ. ಅನುಭವವನ್ನು ಸಮಮಾತ್ರವಾಗಿರಿಸಿಕೊಂಡರೆ, ಅದೇ ಸಮಯದಲ್ಲಿ ಕಸ್ಟಮೈಸ್‌ ಮಾಡಿದ ಎಂಟರ್ಪ್ರೈಸ್ ವಿಸ್ತರಣೆ ಉತ್ತಮವಾಗಿದೆ. GitHub Copilot ಚಾಟ್ ಎಂಟರ್ಫೋರ್ಸಿನಲ್ಲಿ ವಿಸ್ತರಣೆಗೆ ಸಂಬಂಧಿಸಿದ APIಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ. ಸಮಸಾಧನಾನುಭವ ಮತ್ತು ಕಸ್ಟಮೈಸ್ ಮಾಡಿದ ಕಾರ್ಯಗಳು ಉತ್ತಮ ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ನೀಡುತ್ತವೆ.

ಈ ಲ್ಯಾಬ್ ಮುಖ್ಯವಾಗಿ Phi-3 ಮಾದರಿಯನ್ನು ಸ್ಥಳೀಯ NPU ಮತ್ತು Azure ಹೈಬ್ರಿಡ್ ಜೊತೆಗೆ ಬಳಸಿ GitHub Copilot ಚಾಟ್‌ನಲ್ಲಿ ***@PHI3*** ಇಂದ ಕಸ್ಟಮೈಸ್ ಮಾಡಲಾದ ಏಜೆಂಟ್ನ್ನು ನಿರ್ಮಿಸಿ ಎಂಟರ್‌ಪ್ರೈಸ್ ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಕೋಡ್ ರಚನೆಯಲ್ಲಿ ಸಹಾಯ ಮಾಡಲು ***(@PHI3 /gen)*** ಮತ್ತು ಚಿತ್ರಗಳ ಆಧಾರದ ಮೇಲೆ ಕೋಡ್ ರಚನೆ ಮಾಡಲು ***(@PHI3 /img)*** ಬಳಸುತ್ತದೆ.

![PHI3](../../../../../../../translated_images/kn/cover.1017ebc9a7c46d09.webp)

### ***ಗಮನಿಸಿ:*** 

ಈ ಲ್ಯಾಬ್ ಪ್ರಸ್ತುತ Intel CPU ಮತ್ತು Apple Silicon AIPC ಯಲ್ಲಿ ಅನುಷ್ಠಾನಗೊಳಿಸಲಾಗಿದೆ. ನಾವು Qualcomm ಆಧಾರಿತ NPU ಆವೃತ್ತಿಯನ್ನು ಮುಂದುವರೆದು ನವೀಕರಿಸುವೆವು.

## **ಲ್ಯಾಬ್**

| ಹೆಸರು | ವಿವರಣೆ | AIPC | ಆಪಲ್ |
| ------------ | ----------- | -------- |-------- |
| Lab0 - ಈಗಿನೌ ರಿಸಿ (✅) | ಸಂಬಂಧಿತ ಪರಿಸರಗಳನ್ನು ಮತ್ತು ಸ್ಥಾಪನೆ ಸಾಧನಗಳನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ ಮತ್ತು ಸ್ಥಾಪಿಸಿ | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini ಜೊತೆಗೆ ಪ್ರಾಂಪ್ಟ್ ಫ್ಲೋ ನಡೆಸಿ (✅) | AIPC / ಆಪಲ್ ಸಿಲಿಕಾನ್ ಜೊತೆಗೊಳಿಸಿ, ಸ್ಥಳೀಯ NPU ಬಳಸಿ Phi-3-mini ಮೂಲಕ ಕೋಡ್ ರಚಿಸಿ | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure ಮಷಿನ್ ಲರ್ನಿಂಗ್ ಸರ್ವೀಸ್ ಮೇಲೆ Phi-3-vision ನಿಯೋಜಿಸಿ (✅) | Azure ಮಷಿನ್ ಲರ್ನಿಂಗ್ ಸರ್ವೀಸ್‌ನ ಮಾದರಿ ಕ್ಯಾಟಲೋಗ್ - Phi-3-vision ಚಿತ್ರದ ನಿಯೋಜನೆಯಿಂದ ಕೋಡ್ ರಚಿಸಿ | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chatನಲ್ಲಿ @phi-3 ಏಜೆಂಟ್ ರಚಿಸಿ (✅)  | GitHub Copilot Chat ನಲ್ಲಿ ಕಸ್ಟಮೈಸ್ ಮಾಡಿದ Phi-3 ಏಜೆಂಟ್ ರಚಿಸಿ, ಕೋಡ್ ರಚನೆ, ಗ್ರಾಫ್ ರಚನೆ ಕೋಡ್, RAG ಇತ್ಯಾದಿ ಪೂರ್ಣಗೊಳಿಸಿ | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| ಮಾದರಿ ಕೋಡ್ (✅)  | ಮಾದರಿ ಕೋಡ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **ಸಾಧನಗಳು**

1. Phi-3 ಕುಕ್‌ಬುಕ್ [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ತಿಳಿಯಿರಿ [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ತಿಳಿಯಿರಿ [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API ಬಗ್ಗೆ ತಿಳಿಯಿರಿ [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry ಬಗ್ಗೆ ತಿಳಿಯಿರಿ [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry ಮಾದರಿ ಕ್ಯಾಟಲಾಗ್ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಜಾಹೀರಾತು**:  
ಈ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸದಾಗಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಇರುವ ಮೂಲ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಅಧಿಕೃತ ಮಾದರಿಯಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಸಂವೇದನಾಶೀಲ ಮಾಹಿತಿಗೆ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅರಿವಿಗೆ ತಪ್ಪುಗಳಿಗಾಗಿ ನಾವು ಹೊಣೆಗಾರರಾಗಿರುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->