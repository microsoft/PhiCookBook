<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-12-21T21:15:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ml"
}
-->
# ഇന്ററാക്ടീവ് Phi 3 Mini 4K Instruct Chatbot with Whisper

## അവലോകനം

ഇന്ററാക്ടീവ് Phi 3 Mini 4K Instruct Chatbot എന്നത് ഉപയോക്താക്കളെ Microsoft Phi 3 Mini 4K instruct ഡെമോയുമായി എഴുത്തോ ഓഡിയോ ഇൻപുട്ടോ വഴியாக ഇടപഴകിക്കാൻ അനുവദിക്കുന്ന ഒരു ഉപകരണമാണ്. ട്രാൻസ്ലേഷൻ, കാലാവസ്ഥ അപ്‌ഡേറ്റുകൾ, പൊതുവായ വിവര ശേഖരണം മുതലായവയ്ക്ക് ഈ ചാറ്റ്ബോട്ട് ഉപയോഗിക്കാവുന്നതാണ്.

### തുടങ്ങുന്നത്

ഈ ചാറ്റ്ബോട്ട് ഉപയോഗിക്കാൻ, താഴെ പറയുന്ന നിർദ്ദേശങ്ങൾ പിന്തുടരുക:

1. Open a new [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. നോട്ട്ബുക്കിന്റെ പ്രധാന വിൻഡോയിൽ, ഒരു ടെക്സ്റ്റ് ഇൻപുട്ട് ബോക്സ് കൂടിയൊരു ചാറ്റ്ബോക്സ് ഇന്റർഫേസ് നിങ്ങൾ കാണാനിടയുണ്ട്, കൂടാതെ "Send" ബട്ടൺ ഉണ്ടാകും.
3. ടെക്സ്റ്റ് അധിഷ്ഠിത ചാറ്റ്ബോട്ട് ഉപയോഗിക്കാൻ, ടെക്സ്റ്റ് ഇൻപുട്ട് ബോക്സിൽ നിങ്ങളുടെ സന്ദേശം ടൈപ്പ് ചെയ്ത് "Send" ബട്ടണില点击 ചെയ്യുക. ചാറ്റ്ബോട്ട് നോട്ട്ബുക്ക് അകത്തിലേക്ക് നേരിട്ട് പ്ലേ ചെയ്യാവുന്ന ഒരു ഓഡിയോ ഫയൽ റിസ്പോൺസ് ആയി നൽകും.

**Note**: ഈ ഉപകരണത്തിന് GPU ആവശ്യമാണ് കൂടാതെ സ്പീച്ച് പരിചയം (speech recognition) և വിവർത്തനം కోసం ഉപയോഗിക്കുന്ന Microsoft Phi-3 மற்றும் OpenAI Whisper മോഡലുകളിലേക്ക് ആക്‌സസ് ആവശ്യമാണ്.

### GPU ആവശ്യകതകൾ

ഈ ഡെമോ চালിക്കാൻ നിങ്ങൾക്ക് 12Gb GPU മെമ്മറി ആവശ്യമാണ്.

GPU-യിൽ Microsoft-Phi-3-Mini-4K instruct ഡെമോ പ്രവർത്തിപ്പിക്കാൻ ആവശ്യമുള്ള മെമ്മറി വിവിധ ഘടകങ്ങൾ ആശ്രയിച്ചിരിക്കും, ഉദാഹരണത്തിന് ഇൻപുട്ട് ഡാറ്റയുടെ വലിപ്പം (ഓഡിയോ അല്ലെങ്കിൽ ടെക്സ്റ്റ്), വിവർത്തനത്തിന് ഉപയോഗിക്കുന്ന ഭാഷ, മോഡലിന്റെ സ്പീഡ്, GPU-യിലെ ലഭ്യമായ മെമ്മറി എന്നിവ.

പൊതുവായി, Whisper മോഡൽ GPU-കളിൽ പ്രവർത്തിക്കാനാണ് രൂപകൽപ്പന ചെയ്‌തിരിക്കുന്നത്. Whisper മോഡൽ നടത്തിക്കാൻ ശുപാർശ ചെയ്യുന്ന കുറഞ്ഞ GPU മെമ്മറി 8 GB ആണ്, എന്നാൽ ആവശ്യമായെങ്കിൽ കൂടുതൽ മെമ്മറിയും കൈകാര്യം ചെയ്യാൻ കഴിയും.

വലിയ ആമൗണ്ടിലോ ഉയർന്ന വോളിയം റിക്വസ്റ്റ്‌കളും മോഡലിൽ കൂടുതൽ GPU മെമ്മറി ആവശ്യപ്പെടുകയോ പ്രകടനം പ്രശ്നങ്ങൾ ഉണ്ടാക്കുകയോ ചെയ്യാമെന്ന് ശ്രദ്ധിക്കുക. നിങ്ങളുടെ ഉപയോഗ കേസുകൾ വ്യത്യستی കോൺഫിഗറേഷനുകളോടൊപ്പം പരീക്ഷിച്ച് മെമ്മറി ഉപയോഗം നിരീക്ഷിച്ച് മികച്ച ക്രമീകരണങ്ങൾ നിർണയിക്കാൻ ശുപാർശ ചെയ്യപ്പെടുന്നു.

## Whisper-ഉടെയുള്ള ഇന്ററാക്ടീവ് Phi 3 Mini 4K Instruct Chatbot-ന്റെ E2E സാമ്പിൾ

The jupyter notebook titled [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) Microsoft Phi 3 Mini 4K instruct ഡെമോയെ ഓഡിയോയോ എഴുതിയ ടെക്സ്റ്റോ ഇൻപുട്ട് ആയി ഉപയോഗിച്ച് ടെക്സ്റ്റ് നിർമ്മിക്കാൻ എങ്ങനെ ഉപയോഗിക്കാമെന്ന് പ്രദർശിപ്പിക്കുന്നു. നോട്ട്ബുക്ക് താഴെ കാണുന്നSeveral ഫംഗ്ഷനുകൾ നിർവചിച്ചിട്ടുണ്ട്:

1. `tts_file_name(text)`: ഈ ഫംഗ്ഷൻ ജനറേറ്റഡ് ഓഡിയോ ഫയൽ സേവ് ചെയ്യുന്നതിനായി ഇൻപുട്ട് ടെക്സ്റ്റ് അടിസ്ഥാനമാക്കി ഫയൽ നാമം തയ്യാറാക്കുന്നു.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: ഈ ഫംഗ്ഷൻ Edge TTS API ഉപയോഗിച്ച് ഇൻപുട്ട് ടെക്സ്റ്റിന്റെ ചങ്കുകളുടെ ലിസ്റ്റിൽ നിന്ന് ഒരു ഓഡിയോ ഫയൽ ഉണ്ടാക്കുന്നു. ഇൻപുട്ട് പാരാമീറ്ററുകളിൽ ചങ്കുകളുടെ ലിസ്റ്റ്, സംസാര തിരക്ക് (speech rate), വോയ്‌സ് നാമം, ജനറേറ്റുചെയ്‌ത ഓഡിയോ ഫയൽ സേവ് ചെയ്യാനുള്ള output പാത എന്നിവ അടങ്ങിയിരിക്കുന്നു.
1. `talk(input_text)`: ഈ ഫംഗ്ഷൻ Edge TTS API ഉപയോഗിച്ച് ഒരു ഓഡിയോ ഫയൽ ജനറേറ്റ് ചെയ്ത് /content/audio ഡയറക്ടറിയിലുള്ള ഒരു റാൻഡം ഫയൽ നാമത്തിൽ_SAVE_ ചെയ്യുന്നു. ഇൻപുട്ട് പാരാമീറ്റർ ആയി പരിവർത്തനത്തിന് വേണ്ടി നൽകിയ ടെക്സ്റ്റ് ആണ്.
1. `run_text_prompt(message, chat_history)`: ഈ ഫംഗ്ഷൻ Microsoft Phi 3 Mini 4K instruct ഡെമോയെ ഉപയോഗിച്ച് ഒരു മെസേജ് ഇൻപുട്ടിൽ നിന്ന് ഓഡിയോ ഫയൽ ജനറേറ്റ് ചെയ്യുകയും അത് ചാറ്റ് ഹിസ്റ്ററിയിലേക്ക് ചേർക്കുകയും ചെയ്യുന്നു.
1. `run_audio_prompt(audio, chat_history)`: ഈ ഫംഗ്ഷൻ ഒരു ഓഡിയോ ഫയൽ ടെക്സ്റ്റായി മാറ്റാൻ Whisper മോഡൽ API ഉപയോഗിച്ച് പരിവർത്തനം ചെയ്ത് അതിനെ `run_text_prompt()` ഫംഗ്ഷന്‍ പാസ്സ് ചെയ്യുന്നു.
1. കോഡ് Gradio ആപ്പ് ലാഞ്ച് ചെയ്യുന്നു, ഇത് ഉപയോക്താക്കൾക്ക് Phi 3 Mini 4K instruct ഡെമോയിൽ സന്ദേശങ്ങൾ ടൈപ്പ് ചെയ്യുകയോ ഓഡിയോ ഫയലുകൾ അപ്‌ലോഡ് ചെയ്യുകയോ ചെയ്ത് ഇടപഴകാൻ അനുവദിക്കുന്നു. ഔട്ട്പുട്ട് ആപ്പിൽ ഒരു ടെക്സ്റ്റ് മെസ്സേജായി പ്രദർശിപ്പിക്കപ്പെടുന്നു.

## പ്രശ്നപരിഹാരം

Cuda GPU ഡ്രൈവർകൾ ഇൻസ്റ്റാൾ ചെയ്യൽ

1. Ensure your Linux application are upto date

    ```bash
    sudo apt update
    ```

1. Install Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Register the cuda driver location

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Checking Nvidia GPU memory size (Required 12GB of GPU Memory)

    ```bash
    nvidia-smi
    ```

1. Empty Cache: If you’re using PyTorch, you can call torch.cuda.empty_cache() to release all unused cached memory so that it can be used by other GPU applications

    ```python
    torch.cuda.empty_cache() 
    ```

1. Checking Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Perform the following tasks to create a Hugging Face token.

    - Navigate to the [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Select **New token**.
    - Enter project **Name** you want to use.
    - Select **Type** to **Write**.

> **Note**
>
> If you encounter the following error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> To resolve this, type the following command inside your terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ക്ലെയിമർ:
ഈ രേഖ AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്യപ്പെട്ടതാണ്. നാം കൃത്യത നിലനിർത്താൻ പരിശ്രമിച്ചാലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ കൃത്യതക്കുറവുകൾ ഉണ്ടാകാമെന്നാണ് ശ്രദ്ധയിൽ വെയ്ക്കേണ്ടത്. അതിന്റെ മാതൃഭാഷയിലുള്ള മൂല രേഖ ആണ് രാസ്ത്രീയമായും അധികാരപരവും ആയ ഉറവിടം എന്ന് കണക്കാക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശിപാർശിച്ചിരിക്കുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്താൽ അനുഭവപ്പെടുന്ന ഏതെങ്കിലും തെറ്റായ മനസ്സിലാക്കലുകളിലോ തെറ്റിദ്ധാരണങ്ങളിലോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->