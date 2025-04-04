<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8d36fc444748a50558d017e8a0772437",
  "translation_date": "2025-04-04T11:32:02+00:00",
  "source_file": "code\\07.Lab\\01\\AIPC\\extensions\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "ja"
}
-->
# VS Code拡張機能へようこそ

## フォルダーの内容

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報を使用して、VS Codeはコマンドパレットにコマンドを表示できます。この時点ではプラグインを読み込む必要はありません。
* `src/extension.ts` - これはコマンドの実装を提供するメインファイルです。
  * ファイルは1つの関数`activate`をエクスポートします。この関数は拡張機能が初めてアクティブ化される際（この場合はコマンドの実行時）に呼び出されます。`activate`関数内で`registerCommand`を呼び出します。
  * コマンドの実装を含む関数を`registerCommand`の第2パラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールしてください (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint)

## すぐに開始する

* `F5`を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行します (`Ctrl+Shift+P` または Macの場合は`Cmd+Shift+P`を押して`Hello World`を入力)。
* `src/extension.ts`内のコードにブレークポイントを設定して、拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts`内のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、拡張機能の変更を読み込むためにVS Codeウィンドウを再読み込みすることも可能です (`Ctrl+R` または Macの場合は`Cmd+R`)。

## APIを探索する

* `node_modules/@types/vscode/index.d.ts`ファイルを開くと、APIの全セットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)をインストールしてください。
* **Tasks: Run Task**コマンドから「watch」タスクを実行します。これが実行されていない場合、テストが認識されない可能性があります。
* アクティビティバーからTestingビューを開き、「Run Test」ボタンをクリックするか、ホットキー`Ctrl/Cmd + ; A`を使用してください。
* Test Resultsビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts`を変更するか、`test`フォルダー内に新しいテストファイルを作成してください。
  * 提供されたテストランナーは`**.test.ts`という名前パターンに一致するファイルのみを考慮します。
  * `test`フォルダー内にフォルダーを作成して、テストを任意の方法で構造化できます。

## さらに進む

* [拡張機能をバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)することで、拡張機能のサイズを縮小し、起動時間を改善します。
* [拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)して、VS Code拡張機能マーケットプレイスで共有します。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)を設定してビルドを自動化します。

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知ください。元の文書（原文）が正式な情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用によって生じる誤解や解釈の誤りについて、当方は責任を負いません。