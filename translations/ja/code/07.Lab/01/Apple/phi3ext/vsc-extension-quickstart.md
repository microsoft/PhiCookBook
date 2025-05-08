<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-08T06:45:33+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ja"
}
-->
# Welcome to your VS Code Extension

## フォルダーの内容

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報により、VS Codeはコマンドパレットにコマンドを表示できます。プラグイン自体はまだ読み込む必要はありません。
* `src/extension.ts` - ここがコマンドの実装を提供するメインファイルです。
  * このファイルは `activate` という関数をエクスポートしており、拡張機能が初めて有効化されたとき（この場合はコマンド実行時）に呼び出されます。`activate` 関数の中で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の第二引数として渡しています。

## セットアップ

* 推奨される拡張機能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、dbaeumer.vscode-eslint）をインストールしてください。

## すぐに使い始める

* `F5` を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットを開くには (`Ctrl+Shift+P` または Macでは `Cmd+Shift+P`) を押し、`Hello World` と入力してコマンドを実行します。
* `src/extension.ts` 内のコードにブレークポイントを設定して拡張機能のデバッグを行います。
* デバッグコンソールで拡張機能からの出力を確認できます。

## 変更を加える

* `src/extension.ts` のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、拡張機能を読み込んだまま VS Code ウィンドウをリロード（`Ctrl+R` または Macでは `Cmd+R`）して変更を反映することも可能です。

## APIを探る

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、APIの全セットを参照できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールしてください。
* **Tasks: Run Task** コマンドから "watch" タスクを実行します。これが動作していないとテストが検出されない可能性があります。
* アクティビティバーの Testing ビューを開き、「Run Test」ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用します。
* テスト結果は Test Results ビューで確認できます。
* `src/test/extension.test.ts` を変更するか、`test` フォルダー内に新しいテストファイルを作成してください。
  * 用意されたテストランナーは `**.test.ts` という名前パターンにマッチするファイルのみを対象とします。
  * `test` フォルダー内にサブフォルダーを作成して、テストを自由に整理することができます。

## さらに進む

* 拡張機能のサイズを減らし起動時間を短縮するには、[拡張機能のバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)を検討してください。
* [VS Code拡張機能マーケットプレイス](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)で拡張機能を公開しましょう。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)を設定してビルドを自動化しましょう。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性を期していますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。