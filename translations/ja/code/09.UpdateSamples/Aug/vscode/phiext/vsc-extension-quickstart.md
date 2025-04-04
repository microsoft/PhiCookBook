<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T11:40:21+00:00",
  "source_file": "code\\09.UpdateSamples\\Aug\\vscode\\phiext\\vsc-extension-quickstart.md",
  "language_code": "ja"
}
-->
# VS Code 拡張機能へようこそ

## フォルダーに含まれているもの

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報により、VS Codeはコマンドパレットにコマンドを表示できます。この時点ではまだプラグインを読み込む必要はありません。
* `src/extension.ts` - これはコマンドの実装を提供する主要なファイルです。
  * このファイルは1つの関数 `activate` をエクスポートします。この関数は拡張機能が初めてアクティブ化された時（この場合コマンドが実行された時）に呼び出されます。`activate` 関数内では `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の2番目のパラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールしてください (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint)

## すぐに開始する

* `F5` を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行します (`Ctrl+Shift+P` または Macでは `Cmd+Shift+P` を押して `Hello World` と入力します)。
* `src/extension.ts` 内のコードにブレークポイントを設定して拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認してください。

## 変更を加える

* `src/extension.ts` のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* または、VS Codeウィンドウを再読み込み (`Ctrl+R` または Macでは `Cmd+R`) して変更を読み込むこともできます。

## APIを探索する

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、APIの完全なセットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールしてください。
* **Tasks: Run Task** コマンドを使って "watch" タスクを実行します。これが実行されていないと、テストが検出されない可能性があります。
* アクティビティバーのテストビューを開き、「Run Test」ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用してください。
* テスト結果の出力は、Test Resultsビューで確認できます。
* `src/test/extension.test.ts` を変更するか、`test` フォルダー内に新しいテストファイルを作成してください。
  * 提供されているテストランナーは、名前パターン `**.test.ts` に一致するファイルのみを考慮します。
  * `test` フォルダー内にフォルダーを作成して、テストを任意の方法で構造化できます。

## さらに進む

* [拡張機能をバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) して、拡張機能のサイズを縮小し、起動時間を改善します。
* [拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) して、VS Codeの拡張機能マーケットプレイスで共有します。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) を設定して、ビルドを自動化します。

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語で記載された文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤読について、当方は責任を負いません。