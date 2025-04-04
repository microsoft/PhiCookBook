<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T05:37:02+00:00",
  "source_file": "code\\09.UpdateSamples\\Aug\\vscode\\phiext\\vsc-extension-quickstart.md",
  "language_code": "ko"
}
-->
# VS Code 확장 프로그램에 오신 것을 환영합니다

## 폴더 내용

* 이 폴더에는 확장 프로그램에 필요한 모든 파일이 포함되어 있습니다.
* `package.json` - 여기서 확장 프로그램과 명령을 선언하는 매니페스트 파일입니다.
  * 샘플 플러그인은 명령을 등록하고 그 제목과 명령 이름을 정의합니다. 이 정보를 통해 VS Code는 명령 팔레트에서 명령을 표시할 수 있습니다. 아직 플러그인을 로드할 필요는 없습니다.
* `src/extension.ts` - 명령 구현을 제공하는 주요 파일입니다.
  * 이 파일은 `activate`라는 하나의 함수를 내보냅니다. 이 함수는 확장 프로그램이 처음 활성화될 때 (이 경우 명령 실행으로 인해) 호출됩니다. `activate` 함수 내부에서 `registerCommand`를 호출합니다.
  * 명령 구현을 포함하는 함수를 `registerCommand`의 두 번째 매개변수로 전달합니다.

## 설정

* 추천 확장 프로그램을 설치하세요 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint)

## 바로 시작하기

* `F5`을 눌러 확장 프로그램이 로드된 새 창을 엽니다.
* (`Ctrl+Shift+P` 또는 Mac의 경우 `Cmd+Shift+P`)을 눌러 명령 팔레트에서 명령을 실행하고 `Hello World`을 입력합니다.
* `src/extension.ts` 내부 코드에서 브레이크포인트를 설정하여 확장 프로그램을 디버그하세요.
* 디버그 콘솔에서 확장 프로그램의 출력 내용을 확인하세요.

## 변경 사항 적용

* `src/extension.ts` 코드 변경 후 디버그 툴바에서 확장을 다시 실행할 수 있습니다.
* 또한 VS Code 창을 (`Ctrl+R` 또는 Mac의 경우 `Cmd+R`)으로 다시 로드하여 변경 사항을 적용할 수 있습니다.

## API 탐색

* `node_modules/@types/vscode/index.d.ts` 파일을 열어 API 전체를 확인할 수 있습니다.

## 테스트 실행

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)를 설치하세요.
* **Tasks: Run Task** 명령을 통해 "watch" 작업을 실행하세요. 이 작업이 실행 중이어야 테스트가 발견됩니다.
* 액티비티 바에서 Testing 뷰를 열고 "Run Test" 버튼을 클릭하거나 핫키 `Ctrl/Cmd + ; A`을 사용하세요.
* Test Results 뷰에서 테스트 결과 출력을 확인하세요.
* `src/test/extension.test.ts` 파일을 변경하거나 `test` 폴더 내에 새 테스트 파일을 생성하세요.
  * 제공된 테스트 러너는 이름 패턴 `**.test.ts`에 맞는 파일만 고려합니다.
  * 테스트를 원하는 방식으로 구조화하기 위해 `test` 폴더 내에 폴더를 생성할 수 있습니다.

## 더 나아가기

* [확장 프로그램 번들링](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)을 통해 확장 프로그램 크기를 줄이고 시작 시간을 개선하세요.
* VS Code 확장 프로그램 마켓플레이스에 [확장 프로그램을 게시](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)하세요.
* [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)을 설정하여 빌드를 자동화하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로써 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.