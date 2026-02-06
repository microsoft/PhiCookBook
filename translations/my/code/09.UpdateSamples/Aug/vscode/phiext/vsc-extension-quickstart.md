# သင့် VS Code Extension သို့ ကြိုဆိုပါသည်

## ဖိုလ်ဒါထဲမှာ ဘာတွေရှိလဲ

* ဒီဖိုလ်ဒါမှာ သင့် extension အတွက် လိုအပ်တဲ့ ဖိုင်တွေ အကုန်ပါဝင်ပါတယ်။
* `package.json` - သင့် extension နဲ့ command ကို ကြေညာထားတဲ့ manifest ဖိုင်ဖြစ်ပါတယ်။
  * ဥပမာ plugin က command တစ်ခုကို မှတ်ပုံတင်ပြီး၊ အမည်နဲ့ command နာမည်ကို သတ်မှတ်ထားပါတယ်။ ဒီအချက်အလက်တွေနဲ့ VS Code က command palette မှာ command ကို ပြသနိုင်ပါတယ်။ plugin ကို မသွင်းခင်မှာပဲ ဖြစ်ပါတယ်။
* `src/extension.ts` - သင့် command ကို အကောင်အထည်ဖော်မယ့် မူလဖိုင်ဖြစ်ပါတယ်။
  * ဖိုင်က function တစ်ခုကို export လုပ်ထားပြီး၊ `activate` လို့ခေါ်ပါတယ်။ သင့် extension ကို ပထမဆုံး activate လုပ်တဲ့အခါ (ဒီကိစ္စမှာ command ကို အကောင်အထည်ဖော်တဲ့အခါ) `activate` function ကို ခေါ်ပါတယ်။ `activate` function အတွင်းမှာ `registerCommand` ကို ခေါ်ပါတယ်။
  * command အကောင်အထည်ဖော်ထားတဲ့ function ကို `registerCommand` ရဲ့ ဒုတိယ argument အဖြစ် ပေးပို့ပါတယ်။

## စတင်ပြင်ဆင်ခြင်း

* အကြံပြုထားတဲ့ extensions တွေကို 설치ပါ (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, နှင့် dbaeumer.vscode-eslint)

## ချက်ချင်း စတင်အသုံးပြုရန်

* `F5` ကို နှိပ်ပြီး သင့် extension ပါဝင်တဲ့ နယူးဝင်းဒိုးကို ဖွင့်ပါ။
* command palette မှာ (`Ctrl+Shift+P` သို့မဟုတ် Mac မှာ `Cmd+Shift+P`) `Hello World` လို့ ရိုက်ထည့်ပြီး သင့် command ကို လည်ပတ်ပါ။
* သင့် extension ကို debug လုပ်ဖို့ `src/extension.ts` ထဲမှာ breakpoint တွေ သတ်မှတ်နိုင်ပါတယ်။
* သင့် extension မှ ထွက်ရှိလာတဲ့ output ကို debug console မှာ ကြည့်ရှုနိုင်ပါတယ်။

## ပြင်ဆင်မှုများ ပြုလုပ်ရန်

* `src/extension.ts` ထဲမှာ ကုဒ်ပြောင်းလဲပြီးနောက် debug toolbar မှာ extension ကို ပြန်လည်စတင်နိုင်ပါတယ်။
* သင့်ပြောင်းလဲမှုတွေကို သွင်းရန် VS Code ဝင်းဒိုးကို (`Ctrl+R` သို့မဟုတ် Mac မှာ `Cmd+R`) ပြန်လည် reload လုပ်နိုင်ပါတယ်။

## API ကို ရှာဖွေပါ

* `node_modules/@types/vscode/index.d.ts` ဖိုင်ကို ဖွင့်လိုက်ရင် ကျွန်တော်တို့ရဲ့ API အပြည့်အစုံကို ကြည့်ရှုနိုင်ပါတယ်။

## စမ်းသပ်မှုများ လုပ်ဆောင်ရန်

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) ကို 설치ပါ။
* **Tasks: Run Task** command မှတဆင့် "watch" task ကို လည်ပတ်ပါ။ ဒီ task လည်ပတ်နေမှ စမ်းသပ်မှုတွေ ရှာဖွေတွေ့ရှိနိုင်ပါမယ်။
* activity bar မှ Testing view ကို ဖွင့်ပြီး "Run Test" ခလုတ်ကို နှိပ်ပါ၊ ဒါမှမဟုတ် `Ctrl/Cmd + ; A` hotkey ကို အသုံးပြုပါ။
* စမ်းသပ်မှုရလဒ်ကို Test Results view မှာ ကြည့်ရှုနိုင်ပါတယ်။
* `src/test/extension.test.ts` ကို ပြင်ဆင်နိုင်ပြီး၊ `test` ဖိုလ်ဒါအတွင်းမှာ စမ်းသပ်ဖိုင်အသစ်တွေ ဖန်တီးနိုင်ပါတယ်။
  * ပေးထားတဲ့ test runner က `**.test.ts` နာမည်ပုံစံနဲ့ ကိုက်ညီတဲ့ ဖိုင်တွေကိုသာ စမ်းသပ်ပါမယ်။
  * စမ်းသပ်မှုတွေကို စီမံဖို့ `test` ဖိုလ်ဒါအတွင်း ဖိုလ်ဒါအသစ်တွေ ဖန်တီးနိုင်ပါတယ်။

## နောက်ထပ် တိုးတက်ရန်

* သင့် extension အရွယ်အစားကို လျော့ချပြီး စတင်ချိန်ကို မြှင့်တင်ဖို့ [extension ကို bundling လုပ်ခြင်း](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) ကို လေ့လာပါ။
* VS Code extension marketplace မှာ သင့် extension ကို [ထုတ်ဝေပါ](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)။
* [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) ကို စီစဉ်ပြီး build လုပ်မှုများကို အလိုအလျောက်လုပ်ဆောင်ပါ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မခံပါ။