# VS Code 拡張機能へようこそ

## フォルダーの中身

* このフォルダーには拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - 拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義しています。この情報により、VS Code はコマンドパレットにコマンドを表示できます。プラグインを読み込む必要はまだありません。
* `src/extension.ts` - コマンドの実装を提供するメインファイルです。
  * このファイルは `activate` という関数をエクスポートしており、拡張機能が初めて有効化されたとき（この場合はコマンド実行時）に呼び出されます。`activate` 関数内で `registerCommand` を呼び出しています。
  * コマンドの実装を含む関数を `registerCommand` の第2引数として渡します。

## セットアップ

* 推奨される拡張機能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、dbaeumer.vscode-eslint）をインストールしてください。

## すぐに始める

* `F5` キーを押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレット（`Ctrl+Shift+P` または Mac では `Cmd+Shift+P`）を開き、「Hello World」と入力してコマンドを実行します。
* `src/extension.ts` 内にブレークポイントを設定して拡張機能のデバッグができます。
* デバッグコンソールで拡張機能の出力を確認できます。

## 変更を加える

* `src/extension.ts` のコードを変更したら、デバッグツールバーから拡張機能を再起動できます。
* また、拡張機能を読み込んだまま VS Code ウィンドウをリロード（`Ctrl+R` または Mac では `Cmd+R`）して変更を反映させることも可能です。

## API を探る

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、API の全セットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールしてください。
* **Tasks: Run Task** コマンドから「watch」タスクを実行します。これが動作していないとテストが検出されない場合があります。
* アクティビティバーの Testing ビューを開き、「Run Test」ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使います。
* テスト結果は Test Results ビューで確認できます。
* `src/test/extension.test.ts` を編集するか、`test` フォルダー内に新しいテストファイルを作成してください。
  * 提供されているテストランナーは、名前が `**.test.ts` にマッチするファイルのみを対象とします。
  * `test` フォルダー内にサブフォルダーを作成して、テストを自由に整理できます。

## さらに進む

* 拡張機能のサイズを削減し、起動時間を短縮するには、[拡張機能のバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)を検討してください。
* VS Code 拡張機能マーケットプレイスに[拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)しましょう。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)を設定してビルドを自動化することも可能です。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。