<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-08T06:47:32+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "ko"
}
-->
# Welcome to your VS Code Extension

## 폴더에 포함된 내용

* 이 폴더에는 확장 기능에 필요한 모든 파일이 들어 있습니다.
* `package.json` - 확장 기능과 명령어를 선언하는 매니페스트 파일입니다.
  * 샘플 플러그인은 명령어를 등록하고 제목과 명령어 이름을 정의합니다. 이 정보 덕분에 VS Code는 명령 팔레트에 명령어를 표시할 수 있습니다. 아직 플러그인을 로드할 필요는 없습니다.
* `src/extension.ts` - 명령어 구현을 제공하는 메인 파일입니다.
  * 이 파일은 `activate`라는 함수를 내보내며, 확장 기능이 처음 활성화될 때(이 경우 명령어 실행 시) 호출됩니다. `activate` 함수 안에서 `registerCommand`를 호출합니다.
  * 명령어 구현이 포함된 함수를 `registerCommand`의 두 번째 매개변수로 전달합니다.

## 설정

* 권장 확장 기능(amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint)을 설치하세요.

## 바로 시작하기

* `F5`를 눌러 확장 기능이 로드된 새 창을 엽니다.
* 명령 팔레트에서 (`Ctrl+Shift+P` 또는 Mac에서는 `Cmd+Shift+P`)를 눌러 `Hello World`를 입력하고 명령어를 실행하세요.
* `src/extension.ts` 파일 내에 중단점을 설정하여 확장 기능을 디버그할 수 있습니다.
* 디버그 콘솔에서 확장 기능의 출력을 확인하세요.

## 변경 사항 적용하기

* `src/extension.ts` 파일의 코드를 변경한 후 디버그 툴바에서 확장 기능을 다시 실행할 수 있습니다.
* 확장 기능을 로드하기 위해 VS Code 창을 다시 불러올 수도 있습니다 (`Ctrl+R` 또는 Mac에서는 `Cmd+R`).

## API 탐색하기

* `node_modules/@types/vscode/index.d.ts` 파일을 열면 전체 API 세트를 확인할 수 있습니다.

## 테스트 실행하기

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)를 설치하세요.
* **Tasks: Run Task** 명령어를 통해 "watch" 작업을 실행하세요. 이 작업이 실행 중이어야 테스트가 제대로 발견됩니다.
* 활동 표시줄에서 Testing 뷰를 열고 "Run Test" 버튼을 클릭하거나 단축키 `Ctrl/Cmd + ; A`를 사용하세요.
* 테스트 결과는 Test Results 뷰에서 확인할 수 있습니다.
* `src/test/extension.test.ts` 파일을 수정하거나 `test` 폴더 내에 새로운 테스트 파일을 만드세요.
  * 제공된 테스트 러너는 `**.test.ts` 이름 패턴과 일치하는 파일만 인식합니다.
  * `test` 폴더 내에 원하는 구조로 하위 폴더를 만들어 테스트를 조직할 수 있습니다.

## 더 나아가기

* [확장 기능 번들링](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)을 통해 확장 기능 크기를 줄이고 시작 시간을 단축하세요.
* VS Code 확장 마켓플레이스에 [확장 기능을 게시](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)하세요.
* [지속적 통합](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)을 설정하여 빌드를 자동화하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 양지해 주시기 바랍니다. 원본 문서의 원어 버전이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.