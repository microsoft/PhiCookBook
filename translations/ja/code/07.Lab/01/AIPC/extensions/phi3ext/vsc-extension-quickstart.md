<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-08T06:43:50+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ja"
}
-->
# Welcome to your VS Code Extension

## フォルダーの中身

* このフォルダーには拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これはマニフェストファイルで、拡張機能とコマンドを宣言します。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報により、VS Codeはコマンドパレットにコマンドを表示できます。プラグイン自体はまだ読み込む必要はありません。
* `src/extension.ts` - これはコマンドの実装を提供するメインファイルです。
  * このファイルは `activate` という関数をエクスポートしており、拡張機能が初めて有効化されたとき（この場合はコマンド実行時）に呼び出されます。`activate` 関数内で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の第2引数として渡します。

## セットアップ

* 推奨される拡張機能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、dbaeumer.vscode-eslint）をインストールしてください。

## すぐに始める

* `F5` を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットを開き（Macでは `Ctrl+Shift+P` または `Cmd+Shift+P`）、`Hello World` と入力してコマンドを実行します。
* `src/extension.ts` 内のコードにブレークポイントを設定して拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認できます。

## 変更を加える

* `src/extension.ts` のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、拡張機能の変更を反映させるために VS Code ウィンドウをリロード（Macでは `Ctrl+R` または `Cmd+R`）することも可能です。

## API を探る

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、API の全セットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールしてください。
* **Tasks: Run Task** コマンドで「watch」タスクを実行します。これが動作していないとテストが検出されない可能性があります。
* アクティビティバーの Testing ビューを開き、「Run Test」ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使ってテストを実行します。
* テスト結果は Test Results ビューで確認できます。
* `src/test/extension.test.ts` を変更したり、`test` フォルダー内に新しいテストファイルを作成できます。
  * 提供されているテストランナーは `**.test.ts` という名前パターンに一致するファイルのみを対象とします。
  * `test` フォルダー内にサブフォルダーを作成して、テストを自由に整理できます。

## さらに進む

* 拡張機能のサイズを削減し、起動時間を短縮するために[拡張機能のバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)を検討してください。
* VS Code 拡張機能マーケットプレイスに[拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)しましょう。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)を設定してビルドを自動化しましょう。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。原文の母国語による文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。