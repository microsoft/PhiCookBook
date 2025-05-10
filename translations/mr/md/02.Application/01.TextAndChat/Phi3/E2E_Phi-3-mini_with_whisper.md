<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:29:29+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "mr"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

Interactive Phi 3 Mini 4K Instruct Chatbot हा एक टूल आहे ज्याद्वारे वापरकर्ते Microsoft Phi 3 Mini 4K instruct डेमोशी टेक्स्ट किंवा ऑडिओ इनपुट वापरून संवाद साधू शकतात. हा chatbot विविध कामांसाठी वापरता येतो, जसे की भाषांतर, हवामान अद्यतने आणि सामान्य माहिती गोळा करणे.

### Getting Started

हा chatbot वापरण्यासाठी, फक्त खालील सूचनांचे पालन करा:

1. नवीन [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) उघडा
2. नोटबुकच्या मुख्य विंडोमध्ये, तुम्हाला टेक्स्ट इनपुट बॉक्स आणि "Send" बटण असलेले chatbox इंटरफेस दिसेल.
3. टेक्स्ट-आधारित chatbot वापरण्यासाठी, फक्त तुमचा संदेश टेक्स्ट इनपुट बॉक्समध्ये टाका आणि "Send" बटण क्लिक करा. chatbot उत्तर म्हणून एक ऑडिओ फाइल तयार करेल जी नोटबुकमध्ये थेट प्ले करता येईल.

**Note**: या टूलसाठी GPU आणि Microsoft Phi-3 व OpenAI Whisper मॉडेल्सची आवश्यकता आहे, जे भाषण ओळख आणि भाषांतरासाठी वापरले जातात.

### GPU Requirements

हा डेमो चालवण्यासाठी तुम्हाला 12Gb GPU मेमरी आवश्यक आहे.

**Microsoft-Phi-3-Mini-4K instruct** डेमो GPU वर चालवण्यासाठी लागणारी मेमरी इनपुट डेटा (ऑडिओ किंवा टेक्स्ट), वापरलेली भाषा, मॉडेलची गती आणि GPU वरील उपलब्ध मेमरी यांसारख्या अनेक घटकांवर अवलंबून असते.

सामान्यतः, Whisper मॉडेल GPU वर चालण्यासाठी डिझाइन केलेले आहे. Whisper मॉडेल चालवण्यासाठी शिफारस केलेली किमान GPU मेमरी 8 GB आहे, पण अधिक मेमरी असल्यास ते सहज हाताळू शकते.

मोठ्या प्रमाणावर डेटा किंवा जास्त विनंत्या मॉडेलवर चालवल्यास अधिक GPU मेमरी लागू शकते आणि कधीकधी कार्यक्षमतेवर परिणाम होऊ शकतो. तुमच्या वापराच्या परिस्थितीचा वेगळ्या कॉन्फिगरेशनसह चाचणी करून मेमरी वापर तपासणे आणि तुमच्या गरजेनुसार योग्य सेटिंग्ज ठरवणे शिफारसीय आहे.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) नावाचा जुपिटर नोटबुक Microsoft Phi 3 Mini 4K instruct डेमो वापरून ऑडिओ किंवा लिहिलेल्या टेक्स्टमधून टेक्स्ट कसा तयार करायचा हे दाखवतो. नोटबुकमध्ये खालील काही फंक्शन्स परिभाषित केले आहेत:

1. `tts_file_name(text)`: हा फंक्शन इनपुट टेक्स्टवरून एक फाइल नाव तयार करतो जेणेकरून तयार झालेली ऑडिओ फाइल सेव्ह करता येईल.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: हा फंक्शन Edge TTS API वापरून टेक्स्टच्या चंकच्या यादीतून ऑडिओ फाइल तयार करतो. इनपुटमध्ये चंक्सची यादी, स्पीच रेट, आवाजाचे नाव आणि आउटपुट फाइलचा पथ दिला जातो.
1. `talk(input_text)`: हा फंक्शन Edge TTS API वापरून ऑडिओ फाइल तयार करतो आणि ती /content/audio डायरेक्टरीमध्ये रँडम नावाने सेव्ह करतो. इनपुट म्हणजे टेक्स्ट जे भाषणात रूपांतरित करायचे आहे.
1. `run_text_prompt(message, chat_history)`: हा फंक्शन Microsoft Phi 3 Mini 4K instruct डेमो वापरून संदेश इनपुटवरून ऑडिओ फाइल तयार करतो आणि ती चॅट इतिहासात जोडतो.
1. `run_audio_prompt(audio, chat_history)`: हा फंक्शन Whisper मॉडेल API वापरून ऑडिओ फाइल टेक्स्टमध्ये रूपांतरित करतो आणि त्यानंतर `run_text_prompt()` फंक्शनला पास करतो.
1. कोड Gradio अॅप लॉन्च करतो ज्याद्वारे वापरकर्ते Phi 3 Mini 4K instruct डेमोशी संदेश टाइप करून किंवा ऑडिओ फाइल अपलोड करून संवाद साधू शकतात. आउटपुट अॅपमध्ये टेक्स्ट संदेश म्हणून दाखवला जातो.

## Troubleshooting

Cuda GPU ड्रायव्हर्स इन्स्टॉल करणे

1. तुमची Linux अॅप्लिकेशन्स अपडेट आहेत याची खात्री करा

    ```bash
    sudo apt update
    ```

1. Cuda ड्रायव्हर्स इन्स्टॉल करा

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cuda ड्रायव्हर स्थान नोंदवा

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU मेमरी साईज तपासा (12GB GPU मेमरी आवश्यक)

    ```bash
    nvidia-smi
    ```

1. Cache रिकामी करा: जर तुम्ही PyTorch वापरत असाल, तर torch.cuda.empty_cache() कॉल करून सर्व न वापरलेल्या कॅश्ड मेमरी सोडू शकता, ज्यामुळे ती इतर GPU अॅप्लिकेशन्ससाठी उपलब्ध होईल

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda तपासा

    ```bash
    nvcc --version
    ```

1. Hugging Face टोकन तयार करण्यासाठी खालील कामे करा.

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) येथे जा.
    - **New token** निवडा.
    - वापरायच्या प्रोजेक्टचे **Name** टाका.
    - **Type** मध्ये **Write** निवडा.

> **Note**
>
> जर तुम्हाला खालील त्रुटी आली:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> यासाठी, टर्मिनलमध्ये खालील कमांड टाका.
>
> ```bash
> sudo ldconfig
> ```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेतच अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवाद शिफारस केला जातो. या अनुवादाचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलाभासाठी आम्ही जबाबदार नाही.