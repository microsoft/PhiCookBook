<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:36:02+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "ne"
}
-->
# तपाईंको VS Code एक्सटेन्सनमा स्वागत छ

## फोल्डरमा के छ

* यो फोल्डरमा तपाईंको एक्सटेन्सनका लागि आवश्यक सबै फाइलहरू छन्।
* `package.json` - यो म्यानिफेस्ट फाइल हो जहाँ तपाईंले आफ्नो एक्सटेन्सन र कमाण्ड घोषणा गर्नुहुन्छ।
  * नमूना प्लगइनले एउटा कमाण्ड दर्ता गर्छ र यसको शीर्षक र कमाण्ड नाम परिभाषित गर्छ। यस जानकारीको आधारमा VS Code ले कमाण्ड प्यालेटमा कमाण्ड देखाउन सक्छ। यसले प्लगइन लोड गर्न आवश्यक छैन।
* `src/extension.ts` - यो मुख्य फाइल हो जहाँ तपाईंले आफ्नो कमाण्डको कार्यान्वयन प्रदान गर्नुहुनेछ।
  * फाइलले एउटा फंक्शन `activate` निर्यात गर्छ, जुन तपाईंको एक्सटेन्सन पहिलो पटक सक्रिय हुँदा (यस अवस्थामा कमाण्ड चलाउँदा) कल हुन्छ। `activate` फंक्शन भित्र हामी `registerCommand` कल गर्छौं।
  * हामी कमाण्डको कार्यान्वयन समावेश गर्ने फंक्शनलाई `registerCommand` को दोस्रो प्यारामिटरको रूपमा पास गर्छौं।

## सेटअप

* सिफारिस गरिएका एक्सटेन्सनहरू इन्स्टल गर्नुहोस् (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, र dbaeumer.vscode-eslint)

## तुरुन्तै सुरु गर्नुहोस्

* `F5` थिचेर नयाँ विन्डो खोल्नुहोस् जहाँ तपाईंको एक्सटेन्सन लोड हुन्छ।
* कमाण्ड प्यालेटबाट (`Ctrl+Shift+P` वा Mac मा `Cmd+Shift+P`) आफ्नो कमाण्ड चलाउनुहोस् र `Hello World` टाइप गर्नुहोस्।
* `src/extension.ts` भित्र आफ्नो कोडमा ब्रेकपोइन्ट सेट गरेर एक्सटेन्सन डिबग गर्नुहोस्।
* डिबग कन्सोलमा आफ्नो एक्सटेन्सनको आउटपुट हेर्नुहोस्।

## परिवर्तनहरू गर्नुहोस्

* `src/extension.ts` मा कोड परिवर्तन गरेपछि डिबग टूलबारबाट एक्सटेन्सन पुनः सुरु गर्न सक्नुहुन्छ।
* तपाईंले VS Code विन्डोलाई पनि पुनः लोड गर्न सक्नुहुन्छ (`Ctrl+R` वा Mac मा `Cmd+R`) ताकि तपाईंका परिवर्तनहरू लोड होउन्।

## API अन्वेषण गर्नुहोस्

* `node_modules/@types/vscode/index.d.ts` फाइल खोल्दा हाम्रो API को पूर्ण सेट हेर्न सक्नुहुन्छ।

## परीक्षणहरू चलाउनुहोस्

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) इन्स्टल गर्नुहोस्
* **Tasks: Run Task** कमाण्डमार्फत "watch" टास्क चलाउनुहोस्। यो चलिरहेको हुनुपर्छ, नत्र परीक्षणहरू फेला नपर्न सक्छन्।
* एक्टिभिटी बारबाट Testing भ्यू खोल्नुहोस् र "Run Test" बटन क्लिक गर्नुहोस्, वा हटकि `Ctrl/Cmd + ; A` प्रयोग गर्नुहोस्।
* परीक्षण परिणामको आउटपुट Test Results भ्यूमा हेर्नुहोस्।
* `src/test/extension.test.ts` मा परिवर्तन गर्नुहोस् वा `test` फोल्डर भित्र नयाँ परीक्षण फाइलहरू सिर्जना गर्नुहोस्।
  * उपलब्ध टेस्ट रनरले मात्र `**.test.ts` नामको फाइलहरूलाई मान्यता दिन्छ।
  * तपाईंले `test` फोल्डर भित्र आफ्नो परीक्षणहरूलाई मनपर्ने तरिकाले संरचना गर्न फोल्डरहरू बनाउन सक्नुहुन्छ।

## थप अगाडि जानुहोस्

* [तपाईंको एक्सटेन्सनलाई बन्डल गरेर](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) एक्सटेन्सनको साइज घटाउनुहोस् र स्टार्टअप समय सुधार गर्नुहोस्।
* VS Code एक्सटेन्सन मार्केटप्लेसमा [तपाईंको एक्सटेन्सन प्रकाशित गर्नुहोस्](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)।
* [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) सेटअप गरेर बिल्डहरू स्वचालित गर्नुहोस्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।