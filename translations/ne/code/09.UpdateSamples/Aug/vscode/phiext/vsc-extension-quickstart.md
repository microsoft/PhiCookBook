<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:31:39+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "ne"
}
-->
# तपाईंको VS Code Extension मा स्वागत छ

## फोल्डरमा के छ

* यस फोल्डरमा तपाईंको extension का लागि आवश्यक सबै फाइलहरू छन्।
* `package.json` - यो manifest फाइल हो जसमा तपाईं आफ्नो extension र command घोषणा गर्नुहुन्छ।
  * नमूना plugin ले एक command दर्ता गर्छ र यसको शीर्षक र command नाम परिभाषित गर्छ। यस जानकारीको आधारमा VS Code ले command palette मा command देखाउन सक्छ। यसले अझै plugin लोड गर्न आवश्यक पर्दैन।
* `src/extension.ts` - यो मुख्य फाइल हो जहाँ तपाईं आफ्नो command को कार्यान्वयन प्रदान गर्नुहुनेछ।
  * फाइलले एउटा function, `activate`, निर्यात गर्छ, जुन तपाईंको extension पहिलो पटक सक्रिय हुँदा (यस अवस्थामा command चलाउँदा) कल हुन्छ। `activate` function भित्र हामी `registerCommand` कल गर्छौं।
  * हामी command को कार्यान्वयन समावेश गर्ने function लाई `registerCommand` को दोस्रो प्यारामिटरको रूपमा पास गर्छौं।

## सेटअप

* सिफारिस गरिएको extension हरू स्थापना गर्नुहोस् (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, र dbaeumer.vscode-eslint)


## तुरुन्तै सुरु गर्नुहोस्

* नयाँ विन्डो खोल्न `F5` थिच्नुहोस् जहाँ तपाईंको extension लोड हुन्छ।
* command palette बाट आफ्नो command चलाउन (`Ctrl+Shift+P` वा Mac मा `Cmd+Shift+P` थिचेर) `Hello World` टाइप गर्नुहोस्।
* `src/extension.ts` भित्रको कोडमा breakpoints सेट गरेर आफ्नो extension डिबग गर्नुहोस्।
* डिबग कन्सोलमा आफ्नो extension बाट आउटपुट फेला पार्नुहोस्।

## परिवर्तनहरू गर्नुहोस्

* `src/extension.ts` मा कोड परिवर्तन गरेपछि debug toolbar बाट extension पुनः सुरू गर्न सक्नुहुन्छ।
* VS Code विन्डो पुनः लोड (`Ctrl+R` वा Mac मा `Cmd+R`) गरेर पनि आफ्नो extension का परिवर्तनहरू लोड गर्न सक्नुहुन्छ।

## API अन्वेषण गर्नुहोस्

* फाइल `node_modules/@types/vscode/index.d.ts` खोल्दा तपाईं हाम्रो सम्पूर्ण API हेर्न सक्नुहुन्छ।

## टेस्टहरू चलाउनुहोस्

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) स्थापना गर्नुहोस्
* **Tasks: Run Task** कमाण्डबाट "watch" टास्क चलाउनुहोस्। यो चलिरहेको हुनुपर्छ, नभए टेस्टहरू फेला नपर्न सक्छन्।
* activity bar बाट Testing दृश्य खोल्नुहोस् र "Run Test" बटन थिच्नुहोस्, वा हटकि `Ctrl/Cmd + ; A` प्रयोग गर्नुहोस्।
* टेस्ट नतिजा Test Results दृश्यमा हेर्न सक्नुहुन्छ।
* `src/test/extension.test.ts` मा परिवर्तन गर्नुहोस् वा `test` फोल्डर भित्र नयाँ टेस्ट फाइलहरू बनाउनुहोस्।
  * दिइएको test runner ले मात्र `**.test.ts` नामको फाइलहरूलाई मान्यता दिनेछ।
  * तपाईं `test` फोल्डर भित्र आफ्नो टेस्टहरूलाई मनपरेको तरिकाले संरचना गर्न फोल्डरहरू बनाउन सक्नुहुन्छ।

## थप अघि बढ्नुहोस्

* [तपाईंको extension बन्डल गरेर](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) extension को साइज घटाउनुहोस् र स्टार्टअप समय सुधार्नुहोस्।
* VS Code extension marketplace मा [तपाईंको extension प्रकाशित गर्नुहोस्](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)।
* [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) सेटअप गरेर बिल्डहरू स्वचालित बनाउनुहोस्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी सटीकता को लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।