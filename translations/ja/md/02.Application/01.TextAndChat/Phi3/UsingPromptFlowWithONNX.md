<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-08T05:36:36+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "ja"
}
-->
# Windows GPUを使ってPhi-3.5-Instruct ONNXでPrompt flowソリューションを作成する方法

以下のドキュメントは、Phi-3モデルに基づくAIアプリケーション開発のためにPromptFlowをONNX（Open Neural Network Exchange）と組み合わせて使う例です。

PromptFlowは、LLM（大規模言語モデル）ベースのAIアプリケーションのアイデア出しやプロトタイピングからテスト、評価までの一連の開発サイクルを効率化するための開発ツール群です。

PromptFlowとONNXを統合することで、開発者は以下を実現できます：

- モデルパフォーマンスの最適化：ONNXを活用して効率的なモデル推論とデプロイを実現
- 開発の簡素化：PromptFlowでワークフローを管理し、繰り返し作業を自動化
- コラボレーションの強化：統一された開発環境を提供し、チーム間の連携を促進

**Prompt flow**は、LLMベースのAIアプリケーションのアイデア出し、プロトタイピング、テスト、評価から本番環境へのデプロイやモニタリングまでの開発サイクルを効率化する開発ツール群です。プロンプトエンジニアリングを格段に簡単にし、プロダクション品質のLLMアプリ構築を可能にします。

Prompt flowはOpenAI、Azure OpenAI Service、カスタマイズ可能なモデル（Huggingface、ローカルLLM/SLM）に接続可能です。Phi-3.5の量子化されたONNXモデルをローカルアプリに展開することを目指しています。Prompt flowはビジネス計画の策定やPhi-3.5に基づくローカルソリューションの完成を支援します。この例では、ONNX Runtime GenAIライブラリを組み合わせてWindows GPU上でPrompt flowソリューションを完成させます。

## **インストール**

### **Windows GPU向けONNX Runtime GenAI**

Windows GPU向けONNX Runtime GenAIの設定方法はこちらのガイドを参照してください [click here](./ORTWindowGPUGuideline.md)

### **VSCodeでPrompt flowをセットアップ**

1. Prompt flowのVS Code拡張機能をインストールします

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.ja.png)

2. Prompt flow VS Code拡張機能をインストール後、拡張機能をクリックし、**Installation dependencies**を選択して、このガイドに従いPrompt flow SDKを環境にインストールします

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.ja.png)

3. [サンプルコード](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf)をダウンロードし、VS Codeで開きます

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.ja.png)

4. **flow.dag.yaml**を開いてPython環境を選択します

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.ja.png)

   **chat_phi3_ort.py**を開いてPhi-3.5-instruct ONNXモデルの場所を変更します

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.ja.png)

5. Prompt flowを実行してテストします

**flow.dag.yaml**を開き、ビジュアルエディタをクリックします

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.ja.png)

クリック後、実行してテストします

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.ja.png)

1. ターミナルでバッチ実行してさらに結果を確認することも可能です


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

結果はデフォルトのブラウザで確認できます


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.ja.png)

**免責事項**:  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご理解ください。原文の言語による文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切責任を負いかねます。