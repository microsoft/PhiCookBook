<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-08T06:47:13+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "ja"
}
-->
# VS Code拡張機能へようこそ

## フォルダーの中身

* このフォルダーには拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - ここは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義しています。この情報により、VS Codeはコマンドパレットにコマンドを表示できます。プラグインを読み込む必要はまだありません。
* `src/extension.ts` - ここはコマンドの実装を提供するメインファイルです。
  * このファイルは`activate`という関数をエクスポートしており、拡張機能が初めて有効化されたとき（この場合はコマンド実行時）に呼び出されます。`activate`関数内で`registerCommand`を呼び出しています。
  * コマンドの実装を含む関数を`registerCommand`の第2引数として渡しています。

## セットアップ

* 推奨されている拡張機能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、dbaeumer.vscode-eslint）をインストールしてください。

## すぐに始める

* `F5`を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行するには（Macでは`Ctrl+Shift+P`または`Cmd+Shift+P`）、`Hello World`と入力してください。
* `src/extension.ts`内のコードにブレークポイントを設定して、拡張機能のデバッグができます。
* 拡張機能からの出力はデバッグコンソールで確認できます。

## 変更を加える

* `src/extension.ts`のコードを変更したら、デバッグツールバーから拡張機能を再起動できます。
* また、拡張機能を読み込むためにVS Codeのウィンドウをリロード（Macでは`Ctrl+R`または`Cmd+R`）することも可能です。

## APIを探る

* `node_modules/@types/vscode/index.d.ts`ファイルを開くと、APIの全セットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)をインストールしてください。
* **Tasks: Run Task**コマンドで「watch」タスクを実行してください。これが動作していないとテストが検出されない可能性があります。
* アクティビティバーのTestingビューを開き、「Run Test」ボタンをクリックするか、ホットキー`Ctrl/Cmd + ; A`を使います。
* テスト結果はTest Resultsビューで確認できます。
* `src/test/extension.test.ts`を変更したり、`test`フォルダー内に新しいテストファイルを作成したりしてください。
  * 提供されているテストランナーは`**.test.ts`という名前パターンにマッチするファイルのみを対象とします。
  * `test`フォルダー内にフォルダーを作成して、テストを自由に整理できます。

## さらに進む

* 拡張機能のサイズを減らし、起動時間を短縮するには、[拡張機能のバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)を行いましょう。
* VS Code拡張機能マーケットプレイスに[拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)しましょう。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)を設定してビルドを自動化しましょう。

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。