<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:16:33+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "mr"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## आढावा

Interactive Phi 3 Mini 4K Instruct Chatbot हा एक साधन आहे ज्याद्वारे वापरकर्ते Microsoft Phi 3 Mini 4K instruct डेमोशी मजकूर किंवा ऑडिओ इनपुट वापरून संवाद साधू शकतात. हा चॅटबॉट विविध कामांसाठी वापरता येतो, जसे की भाषांतर, हवामान अपडेट्स, आणि सामान्य माहिती गोळा करणे.

### सुरुवात कशी करावी

हा चॅटबॉट वापरण्यासाठी खालील सूचनांचे पालन करा:

1. नवीन [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) उघडा
2. नोटबुकच्या मुख्य विंडोमध्ये, तुम्हाला एक चॅटबॉक्स इंटरफेस दिसेल ज्यात मजकूर इनपुट बॉक्स आणि "Send" बटण आहे.
3. मजकूर-आधारित चॅटबॉट वापरण्यासाठी, फक्त तुमचा संदेश मजकूर इनपुट बॉक्समध्ये टाइप करा आणि "Send" बटणावर क्लिक करा. चॅटबॉट ऑडिओ फाइलसह प्रतिसाद देईल जी थेट नोटबुकमध्ये प्ले करता येईल.

**Note**: या साधनासाठी GPU आणि Microsoft Phi-3 व OpenAI Whisper मॉडेल्सची आवश्यकता आहे, जे भाषण ओळख आणि भाषांतरासाठी वापरले जातात.

### GPU आवश्यकताः

हा डेमो चालवण्यासाठी तुम्हाला 12Gb GPU मेमरीची गरज आहे.

**Microsoft-Phi-3-Mini-4K instruct** डेमो GPU वर चालवताना मेमरीची गरज अनेक घटकांवर अवलंबून असते, जसे की इनपुट डेटा (ऑडिओ किंवा मजकूर) ची आकारमान, भाषांतरासाठी वापरलेली भाषा, मॉडेलची गती, आणि GPU वर उपलब्ध मेमरी.

सामान्यतः, Whisper मॉडेल GPU वर चालण्यासाठी डिझाइन केलेले आहे. Whisper मॉडेलसाठी शिफारस केलेली किमान GPU मेमरी 8 GB आहे, पण गरज भासल्यास अधिक मेमरी देखील हाताळू शकते.

मोठ्या प्रमाणात डेटा किंवा जास्त विनंत्या मॉडेलवर चालवल्यास अधिक GPU मेमरीची गरज भासू शकते आणि कामगिरीवर परिणाम होऊ शकतो. तुमच्या वापराच्या प्रकरणासाठी वेगवेगळ्या कॉन्फिगरेशनसह चाचणी करणे आणि मेमरी वापरावर लक्ष ठेवणे आवश्यक आहे जेणेकरून तुमच्या गरजेनुसार सर्वोत्तम सेटिंग्ज ठरवता येतील.

## E2E नमुना Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper साठी

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) नावाचा जुपिटर नोटबुक Microsoft Phi 3 Mini 4K instruct डेमोचा वापर करून ऑडिओ किंवा लिहिलेल्या मजकूरातून मजकूर कसा तयार करायचा हे दाखवतो. नोटबुकमध्ये खालील काही फंक्शन्स परिभाषित केले आहेत:

1. `tts_file_name(text)`: हा फंक्शन इनपुट मजकूरावर आधारित ऑडिओ फाइल जतन करण्यासाठी फाइल नाव तयार करतो.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: हा फंक्शन Edge TTS API वापरून इनपुट मजकूराच्या तुकड्यांच्या यादीतून ऑडिओ फाइल तयार करतो. इनपुटमध्ये तुकड्यांची यादी, भाषणाचा वेग, आवाजाचे नाव, आणि जतन करण्याचा मार्ग असतो.
1. `talk(input_text)`: हा फंक्शन Edge TTS API वापरून ऑडिओ फाइल तयार करतो आणि ती /content/audio फोल्डरमध्ये यादृच्छिक नावाने जतन करतो. इनपुट म्हणजे भाषणात रूपांतरित करायचा मजकूर.
1. `run_text_prompt(message, chat_history)`: हा फंक्शन Microsoft Phi 3 Mini 4K instruct डेमो वापरून संदेश इनपुटवरून ऑडिओ फाइल तयार करतो आणि ती चॅट इतिहासात जोडतो.
1. `run_audio_prompt(audio, chat_history)`: हा फंक्शन Whisper मॉडेल API वापरून ऑडिओ फाइल मजकूरात रूपांतरित करतो आणि `run_text_prompt()` फंक्शनला पास करतो.
1. कोड Gradio अॅप सुरू करतो ज्याद्वारे वापरकर्ते Phi 3 Mini 4K instruct डेमोशी संदेश टाइप करून किंवा ऑडिओ फाइल अपलोड करून संवाद साधू शकतात. आउटपुट अॅपमध्ये मजकूर संदेश म्हणून दाखवला जातो.

## समस्या निवारण

Cuda GPU ड्रायव्हर्स इन्स्टॉल करणे

1. तुमचे Linux अॅप्लिकेशन अपडेट आहेत याची खात्री करा

    ```bash
    sudo apt update
    ```

1. Cuda ड्रायव्हर्स इन्स्टॉल करा

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cuda ड्रायव्हर स्थान नोंदणी करा

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU मेमरी आकार तपासा (12GB GPU मेमरी आवश्यक)

    ```bash
    nvidia-smi
    ```

1. कॅशे रिकामी करा: जर तुम्ही PyTorch वापरत असाल, तर torch.cuda.empty_cache() कॉल करून सर्व न वापरलेली कॅशे मेमरी सोडू शकता, ज्यामुळे ती इतर GPU अॅप्लिकेशन्ससाठी उपलब्ध होईल

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda तपासा

    ```bash
    nvcc --version
    ```

1. Hugging Face टोकन तयार करण्यासाठी खालील टास्क करा.

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) वर जा.
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
> यासाठी, तुमच्या टर्मिनलमध्ये खालील कमांड टाइप करा.
>
> ```bash
> sudo ldconfig
> ```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.