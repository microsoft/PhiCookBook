<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-07T14:11:00+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ur"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## جائزہ

Interactive Phi 3 Mini 4K Instruct Chatbot ایک ایسا آلہ ہے جو صارفین کو Microsoft Phi 3 Mini 4K instruct ڈیمو کے ساتھ متن یا آڈیو ان پٹ کے ذریعے بات چیت کرنے کی اجازت دیتا ہے۔ یہ چیٹ بوٹ مختلف کاموں کے لیے استعمال کیا جا سکتا ہے، جیسے ترجمہ، موسم کی تازہ کاری، اور عمومی معلومات جمع کرنا۔

### شروع کرنا

اس چیٹ بوٹ کو استعمال کرنے کے لیے، بس ان ہدایات پر عمل کریں:

1. ایک نیا [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) کھولیں
2. نوٹ بک کی مرکزی ونڈو میں، آپ کو ایک چیٹ باکس انٹرفیس نظر آئے گا جس میں ایک متن ان پٹ باکس اور "Send" بٹن ہوگا۔
3. ٹیکسٹ بیسڈ چیٹ بوٹ استعمال کرنے کے لیے، بس اپنا پیغام متن ان پٹ باکس میں ٹائپ کریں اور "Send" بٹن پر کلک کریں۔ چیٹ بوٹ ایک آڈیو فائل کے ساتھ جواب دے گا جسے نوٹ بک کے اندر سے براہ راست چلایا جا سکتا ہے۔

**Note**: یہ آلہ GPU اور Microsoft Phi-3 اور OpenAI Whisper ماڈلز تک رسائی کا تقاضا کرتا ہے، جو تقریر کی پہچان اور ترجمہ کے لیے استعمال ہوتے ہیں۔

### GPU کی ضروریات

اس ڈیمو کو چلانے کے لیے آپ کو 12Gb GPU میموری کی ضرورت ہے۔

**Microsoft-Phi-3-Mini-4K instruct** ڈیمو کو GPU پر چلانے کے لیے میموری کی ضروریات کئی عوامل پر منحصر ہیں، جیسے ان پٹ ڈیٹا (آڈیو یا متن) کا سائز، ترجمے کے لیے استعمال ہونے والی زبان، ماڈل کی رفتار، اور GPU پر دستیاب میموری۔

عمومی طور پر، Whisper ماڈل GPUs پر چلانے کے لیے ڈیزائن کیا گیا ہے۔ Whisper ماڈل کو چلانے کے لیے کم از کم 8 GB GPU میموری کی سفارش کی جاتی ہے، لیکن اگر ضرورت ہو تو یہ بڑی میموری کو بھی سنبھال سکتا ہے۔

یہ بات اہم ہے کہ زیادہ مقدار میں ڈیٹا یا درخواستوں کی بڑی تعداد ماڈل پر چلانے سے GPU میموری کی زیادہ ضرورت ہو سکتی ہے اور/یا کارکردگی کے مسائل پیدا ہو سکتے ہیں۔ اپنی مخصوص ضروریات کے لیے مختلف کنفیگریشنز کے ساتھ اپنے استعمال کا تجربہ کریں اور میموری کے استعمال کی نگرانی کریں تاکہ بہترین ترتیبات معلوم ہو سکیں۔

## E2E نمونہ برائے Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

جیوپیٹر نوٹ بک جس کا عنوان ہے [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) دکھاتی ہے کہ Microsoft Phi 3 Mini 4K instruct Demo کو آڈیو یا تحریری متن ان پٹ سے متن پیدا کرنے کے لیے کیسے استعمال کیا جائے۔ نوٹ بک کئی فنکشنز کی تعریف کرتی ہے:

1. `tts_file_name(text)`: یہ فنکشن ان پٹ متن کی بنیاد پر ایک فائل کا نام تیار کرتا ہے تاکہ پیدا کی گئی آڈیو فائل محفوظ کی جا سکے۔
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: یہ فنکشن Edge TTS API کا استعمال کرتے ہوئے ان پٹ متن کے ٹکڑوں کی فہرست سے آڈیو فائل تیار کرتا ہے۔ ان پٹ پیرامیٹرز میں ٹکڑوں کی فہرست، تقریر کی رفتار، آواز کا نام، اور پیدا کی گئی آڈیو فائل کو محفوظ کرنے کا راستہ شامل ہیں۔
1. `talk(input_text)`: یہ فنکشن Edge TTS API استعمال کرکے آڈیو فائل تیار کرتا ہے اور اسے /content/audio ڈائریکٹری میں ایک تصادفی فائل نام سے محفوظ کرتا ہے۔ ان پٹ پیرامیٹر وہ متن ہے جسے تقریر میں تبدیل کیا جانا ہے۔
1. `run_text_prompt(message, chat_history)`: یہ فنکشن Microsoft Phi 3 Mini 4K instruct ڈیمو کا استعمال کرتے ہوئے پیغام ان پٹ سے آڈیو فائل تیار کرتا ہے اور اسے چیٹ ہسٹری میں شامل کرتا ہے۔
1. `run_audio_prompt(audio, chat_history)`: یہ فنکشن Whisper ماڈل API کا استعمال کرتے ہوئے آڈیو فائل کو متن میں تبدیل کرتا ہے اور اسے `run_text_prompt()` فنکشن کو دیتا ہے۔
1. کوڈ ایک Gradio ایپ لانچ کرتا ہے جو صارفین کو Phi 3 Mini 4K instruct ڈیمو کے ساتھ بات چیت کرنے کی اجازت دیتا ہے، چاہے وہ پیغامات ٹائپ کریں یا آڈیو فائلیں اپلوڈ کریں۔ آؤٹ پٹ ایپ میں بطور متن پیغام دکھایا جاتا ہے۔

## مسئلہ حل کرنا

Cuda GPU ڈرائیورز انسٹال کرنا

1. یقینی بنائیں کہ آپ کا لینکس ایپلیکیشن اپ ٹو ڈیٹ ہے

    ```bash
    sudo apt update
    ```

1. Cuda ڈرائیورز انسٹال کریں

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cuda ڈرائیور کی جگہ رجسٹر کریں

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU میموری کا سائز چیک کریں (12GB GPU میموری درکار ہے)

    ```bash
    nvidia-smi
    ```

1. کیشے خالی کریں: اگر آپ PyTorch استعمال کر رہے ہیں، تو آپ torch.cuda.empty_cache() کال کر سکتے ہیں تاکہ تمام غیر استعمال شدہ کیشڈ میموری آزاد ہو جائے تاکہ دیگر GPU ایپلیکیشنز استعمال کر سکیں

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda چیک کریں

    ```bash
    nvcc --version
    ```

1. Hugging Face ٹوکن بنانے کے لیے درج ذیل کام کریں:

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) پر جائیں۔
    - **New token** منتخب کریں۔
    - وہ پروجیکٹ **Name** درج کریں جو آپ استعمال کرنا چاہتے ہیں۔
    - **Type** کو **Write** منتخب کریں۔

> **Note**
>
> اگر آپ کو درج ذیل خرابی کا سامنا ہو:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> اسے حل کرنے کے لیے، اپنے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں۔
>
> ```bash
> sudo ldconfig
> ```

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا بے دقتیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ذمہ دار نہیں ہیں۔