<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:00:10+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "mr"
}
-->
# तुमच्या VS Code एक्सटेंशनमध्ये आपले स्वागत आहे

## फोल्डरमध्ये काय आहे

* या फोल्डरमध्ये तुमच्या एक्सटेंशनसाठी आवश्यक असलेली सर्व फाइल्स आहेत.
* `package.json` - हा मॅनिफेस्ट फाइल आहे ज्यात तुम्ही तुमचे एक्सटेंशन आणि कमांड घोषित करता.
  * नमुना प्लगइन एक कमांड नोंदवते आणि त्याचा शीर्षक व कमांड नाव परिभाषित करते. या माहितीनुसार VS Code कमांड पॅलेटमध्ये कमांड दाखवू शकतो. प्लगइन अजून लोड करण्याची गरज नाही.
* `src/extension.ts` - हा मुख्य फाइल आहे जिथे तुम्ही तुमच्या कमांडची अंमलबजावणी कराल.
  * फाइल एक फंक्शन `activate` एक्सपोर्ट करते, जे तुमचे एक्सटेंशन प्रथमच सक्रिय झाल्यावर (या प्रकरणात कमांड चालविल्यावर) कॉल होते. `activate` फंक्शनमध्ये आपण `registerCommand` कॉल करतो.
  * आपण कमांडची अंमलबजावणी करणारे फंक्शन `registerCommand` ला दुसऱ्या पॅरामीटर म्हणून देतो.

## सेटअप

* शिफारस केलेले एक्सटेंशन्स इन्स्टॉल करा (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, आणि dbaeumer.vscode-eslint)

## लगेच सुरू करा

* `F5` दाबा आणि तुमचे एक्सटेंशन लोड केलेले नवीन विंडो उघडा.
* कमांड पॅलेटमधून (`Ctrl+Shift+P` किंवा Mac वर `Cmd+Shift+P`) `Hello World` टाइप करून तुमचा कमांड चालवा.
* `src/extension.ts` मधील तुमच्या कोडमध्ये ब्रेकपॉइंट सेट करा आणि एक्सटेंशन डिबग करा.
* डिबग कन्सोलमध्ये तुमच्या एक्सटेंशनचा आउटपुट पहा.

## बदल करा

* `src/extension.ts` मध्ये कोड बदलल्यानंतर डिबग टूलबारमधून एक्सटेंशन पुन्हा सुरू करू शकता.
* तुम्ही VS Code विंडो (`Ctrl+R` किंवा Mac वर `Cmd+R`) रीलोड करून तुमचे बदल लोड करू शकता.

## API एक्सप्लोर करा

* `node_modules/@types/vscode/index.d.ts` फाइल उघडल्यावर तुम्हाला आमच्या API चा पूर्ण संच पाहता येईल.

## टेस्ट चालवा

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) इन्स्टॉल करा
* **Tasks: Run Task** कमांडद्वारे "watch" टास्क चालवा. हे चालू असणे आवश्यक आहे, अन्यथा टेस्ट सापडू शकत नाहीत.
* अ‍ॅक्टिव्हिटी बारमधून Testing view उघडा आणि "Run Test" बटणावर क्लिक करा, किंवा `Ctrl/Cmd + ; A` हॉटकी वापरा.
* Test Results view मध्ये टेस्ट निकाल पहा.
* `src/test/extension.test.ts` मध्ये बदल करा किंवा `test` फोल्डरमध्ये नवीन टेस्ट फाइल्स तयार करा.
  * दिलेला टेस्ट रनर फक्त `**.test.ts` नावाच्या फाइल्सना विचारात घेतो.
  * तुम्ही `test` फोल्डरमध्ये उपफोल्डर्स तयार करून तुमच्या टेस्टची रचना करू शकता.

## पुढे जा

* [तुमचे एक्सटेंशन बंडल करून](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) एक्सटेंशनचा आकार कमी करा आणि स्टार्टअप वेळ सुधारित करा.
* VS Code एक्सटेंशन मार्केटप्लेसवर [तुमचे एक्सटेंशन प्रकाशित करा](https://code.visualstudio.com/api/working-with-extensions/publishing-extension).
* [सतत एकत्रीकरण](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) सेटअप करून बिल्ड्स ऑटोमेट करा.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.