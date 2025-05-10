<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:29:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ne"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

Interactive Phi 3 Mini 4K Instruct Chatbot एक उपकरण हो जसले प्रयोगकर्ताहरूलाई Microsoft Phi 3 Mini 4K instruct डेमो सँग टेक्स्ट वा अडियो इनपुट मार्फत अन्तरक्रिया गर्न अनुमति दिन्छ। यो च्याटबोटलाई अनुवाद, मौसम अपडेट, र सामान्य जानकारी सङ्कलन जस्ता विभिन्न कार्यहरूको लागि प्रयोग गर्न सकिन्छ।

### Getting Started

यस च्याटबोट प्रयोग गर्नका लागि तलका निर्देशनहरू पालना गर्नुहोस्:

1. नयाँ [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) खोल्नुहोस्
2. नोटबुकको मुख्य विन्डोमा, तपाईंले टेक्स्ट इनपुट बक्स र "Send" बटन सहितको च्याटबक्स इन्टरफेस देख्नुहुनेछ।
3. टेक्स्ट-आधारित च्याटबोट प्रयोग गर्नका लागि, आफ्नो सन्देश टेक्स्ट इनपुट बक्समा टाइप गरी "Send" बटन क्लिक गर्नुहोस्। च्याटबोटले अडियो फाइलको रूपमा जवाफ दिनेछ जुन नोटबुक भित्रै प्ले गर्न सकिन्छ।

**Note**: यो उपकरण GPU र Microsoft Phi-3 र OpenAI Whisper मोडेलहरूमा पहुँच आवश्यक पर्छ, जुन स्पीच रिकग्निसन र अनुवादका लागि प्रयोग गरिन्छ।

### GPU Requirements

यो डेमो चलाउन तपाईंलाई 12GB GPU मेमोरी आवश्यक छ।

**Microsoft-Phi-3-Mini-4K instruct** डेमो GPU मा चलाउँदा मेमोरी आवश्यकताहरू इनपुट डेटा (अडियो वा टेक्स्ट) को आकार, अनुवादका लागि प्रयोग हुने भाषा, मोडेलको गति, र GPU मा उपलब्ध मेमोरीजस्ता धेरै कारकहरूमा निर्भर गर्दछ।

सामान्यतया, Whisper मोडेल GPU मा चलाउन डिजाइन गरिएको हो। Whisper मोडेल चलाउन सिफारिस गरिएको न्यूनतम GPU मेमोरी 8GB हो, तर आवश्यक परेमा यो बढी मेमोरी पनि सम्हाल्न सक्छ।

ध्यान दिनुहोस् कि ठूलो मात्रामा डेटा वा धेरै अनुरोधहरू मोडेलमा पठाउँदा GPU मेमोरी बढी चाहिन सक्छ र प्रदर्शनमा समस्या आउन सक्छ। तपाईंको प्रयोग केस विभिन्न कन्फिगरेसनमा परीक्षण गर्नु र मेमोरी प्रयोगलाई अनुगमन गर्नु सल्लाह दिइन्छ ताकि तपाईंको आवश्यकताका लागि उत्तम सेटिङहरू निर्धारण गर्न सकियोस्।

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

जुपिटर नोटबुक [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ले Microsoft Phi 3 Mini 4K instruct Demo लाई अडियो वा लेखिएको टेक्स्ट इनपुटबाट टेक्स्ट उत्पादन गर्न कसरी प्रयोग गर्ने देखाउँछ। नोटबुकले केही फंक्शनहरू परिभाषित गरेको छ:

1. `tts_file_name(text)`: यो फंक्शनले इनपुट टेक्स्टको आधारमा अडियो फाइल बचत गर्नको लागि फाइल नाम बनाउँछ।
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: यो फंक्शनले Edge TTS API प्रयोग गरी टेक्स्टका टुक्राहरूको सूचीबाट अडियो फाइल बनाउँछ। इनपुट प्यारामिटरहरूमा टुक्राहरूको सूची, स्पीच गति, भ्वाइस नाम, र अडियो फाइल बचत गर्ने पथ समावेश छन्।
1. `talk(input_text)`: यो फंक्शनले Edge TTS API प्रयोग गरी अडियो फाइल बनाउँछ र /content/audio डाइरेक्टरीमा यादृच्छिक फाइल नाममा बचत गर्छ। इनपुट प्यारामिटर भनेको भाषणमा रूपान्तरण गर्नुपर्ने टेक्स्ट हो।
1. `run_text_prompt(message, chat_history)`: यो फंक्शनले Microsoft Phi 3 Mini 4K instruct डेमो प्रयोग गरी सन्देश इनपुटबाट अडियो फाइल बनाउँछ र यसलाई च्याट इतिहासमा थप्छ।
1. `run_audio_prompt(audio, chat_history)`: यो फंक्शनले Whisper मोडेल API प्रयोग गरी अडियो फाइललाई टेक्स्टमा रूपान्तरण गर्छ र त्यसलाई `run_text_prompt()` फंक्शनमा पठाउँछ।
1. कोडले Gradio एप सुरु गर्छ जसले प्रयोगकर्ताहरूलाई Phi 3 Mini 4K instruct डेमो सँग सन्देश टाइप गर्ने वा अडियो फाइल अपलोड गर्ने माध्यमबाट अन्तरक्रिया गर्न अनुमति दिन्छ। आउटपुट एप भित्रै टेक्स्ट सन्देशको रूपमा देखाइन्छ।

## Troubleshooting

Cuda GPU ड्राइभरहरू इन्स्टल गर्दै

1. तपाईंको Linux एप्लिकेशनहरू अपडेट गरिएको छ भनी सुनिश्चित गर्नुहोस्

    ```bash
    sudo apt update
    ```

1. Cuda Drivers इन्स्टल गर्नुहोस्

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cuda ड्राइभर स्थान दर्ता गर्नुहोस्

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU मेमोरी साइज जाँच गर्नुहोस् (12GB GPU मेमोरी आवश्यक छ)

    ```bash
    nvidia-smi
    ```

1. Cache खाली गर्नुहोस्: यदि तपाईं PyTorch प्रयोग गर्दै हुनुहुन्छ भने, torch.cuda.empty_cache() कल गरेर सबै अप्रयुक्त क्यास गरिएको मेमोरी रिलिज गर्न सक्नुहुन्छ ताकि अन्य GPU एप्लिकेशनहरूले प्रयोग गर्न सकून्

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda जाँच गर्नुहोस्

    ```bash
    nvcc --version
    ```

1. Hugging Face टोकन बनाउनका लागि तलका कार्यहरू गर्नुहोस्।

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) मा जानुहोस्।
    - **New token** चयन गर्नुहोस्।
    - प्रयोग गर्न चाहने प्रोजेक्टको **Name** प्रविष्ट गर्नुहोस्।
    - **Type** लाई **Write** मा चयन गर्नुहोस्।

> **Note**
>
> यदि तपाईंले तलको त्रुटि सामना गर्नु भयो भने:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> समाधानका लागि, आफ्नो टर्मिनलमा तलको कमाण्ड टाइप गर्नुहोस्।
>
> ```bash
> sudo ldconfig
> ```

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सटीकताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा गलतियाँ हुन सक्छन्। मूल दस्तावेज़लाई यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याहरूको लागि हामी जिम्मेवार छैनौं।