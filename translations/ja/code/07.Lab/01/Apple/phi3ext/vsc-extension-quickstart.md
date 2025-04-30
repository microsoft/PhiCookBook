<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T11:35:05+00:00",
  "source_file": "code\\07.Lab\\01\\Apple\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "ja"
}
-->
# VS Code拡張機能へようこそ

## フォルダーの内容

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報により、VS Codeはコマンドパレットでコマンドを表示できます。この時点ではプラグインをロードする必要はありません。
* `src/extension.ts` - これはコマンドの実装を提供するメインファイルです。
  * ファイルは一つの関数、`activate`をエクスポートします。この関数は拡張機能が初めてアクティブ化された時（この場合はコマンドを実行した時）に呼び出されます。`activate`関数内で`registerCommand`を呼び出します。
  * コマンドの実装を含む関数を`registerCommand`の2番目のパラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールしてください (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint)

## すぐに動作させる

* `F5`を押して拡張機能をロードした新しいウィンドウを開きます。
* コマンドパレットでコマンドを実行します。(`Ctrl+Shift+P` または Macでは`Cmd+Shift+P`を押し、`Hello World`を入力してください)
* `src/extension.ts`内のコードにブレークポイントを設定して拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認してください。

## 変更を加える

* `src/extension.ts`内のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、VS Codeウィンドウをリロード (`Ctrl+R` または Macでは`Cmd+R`) して変更をロードすることもできます。

## APIを探索する

* ファイル`node_modules/@types/vscode/index.d.ts`を開くと、APIの完全なセットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールしてください。
* **Tasks: Run Task** コマンドを使用して "watch" タスクを実行します。これが動作していない場合、テストが認識されない可能性があります。
* アクティビティバーからTestingビューを開き、「Run Test」ボタンをクリックするか、ホットキー`Ctrl/Cmd + ; A`を使用してください。
* Test Resultsビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts`に変更を加えるか、`test`フォルダー内に新しいテストファイルを作成してください。
  * 提供されたテストランナーは、名前パターン`**.test.ts`に一致するファイルのみを対象とします。
  * `test`フォルダー内にフォルダーを作成して、テストを任意の方法で構造化できます。

## さらに進む

* [拡張機能をバンドルする](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)ことで拡張機能のサイズを削減し、起動時間を改善します。
* VS Code拡張機能マーケットプレイスで[拡張機能を公開する](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)を設定してビルドを自動化します。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文書の母国語で記載された内容が公式かつ信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用によって生じた誤解や誤認について、当方は一切の責任を負いません。