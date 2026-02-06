# Inferência multiplataforma com Rust

Este tutorial irá guiar-nos pelo processo de realizar inferência usando Rust e o [framework Candle ML](https://github.com/huggingface/candle) da HuggingFace. Utilizar Rust para inferência oferece várias vantagens, especialmente quando comparado com outras linguagens de programação. Rust é conhecido pelo seu alto desempenho, comparável ao do C e C++. Isto torna-o uma excelente escolha para tarefas de inferência, que podem ser computacionalmente intensivas. Em particular, isto deve-se às abstrações sem custo e à gestão eficiente de memória, que não tem overhead de garbage collection. As capacidades multiplataforma do Rust permitem o desenvolvimento de código que corre em vários sistemas operativos, incluindo Windows, macOS e Linux, bem como sistemas operativos móveis, sem alterações significativas na base de código.

O pré-requisito para seguir este tutorial é [instalar Rust](https://www.rust-lang.org/tools/install), que inclui o compilador Rust e o Cargo, o gestor de pacotes do Rust.

## Passo 1: Criar um Novo Projeto Rust

Para criar um novo projeto Rust, execute o seguinte comando no terminal:

```bash
cargo new phi-console-app
```

Isto gera uma estrutura inicial de projeto com um ficheiro `Cargo.toml` e um diretório `src` contendo um ficheiro `main.rs`.

De seguida, vamos adicionar as nossas dependências - nomeadamente os crates `candle`, `hf-hub` e `tokenizers` - ao ficheiro `Cargo.toml`:

```toml
[package]
name = "phi-console-app"
version = "0.1.0"
edition = "2021"

[dependencies]
candle-core = { version = "0.6.0" }
candle-transformers = { version = "0.6.0" }
hf-hub = { version = "0.3.2", features = ["tokio"] }
rand = "0.8"
tokenizers = "0.15.2"
```

## Passo 2: Configurar Parâmetros Básicos

Dentro do ficheiro main.rs, vamos definir os parâmetros iniciais para a nossa inferência. Todos vão estar codificados diretamente para simplificar, mas podemos modificá-los conforme necessário.

```rust
let temperature: f64 = 1.0;
let sample_len: usize = 100;
let top_p: Option<f64> = None;
let repeat_last_n: usize = 64;
let repeat_penalty: f32 = 1.2;
let mut rng = rand::thread_rng();
let seed: u64 = rng.gen();
let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";
let device = Device::Cpu;
```

- **temperature**: Controla a aleatoriedade do processo de amostragem.
- **sample_len**: Especifica o comprimento máximo do texto gerado.
- **top_p**: Usado para amostragem núcleo (nucleus sampling) para limitar o número de tokens considerados em cada passo.
- **repeat_last_n**: Controla o número de tokens considerados para aplicar uma penalização que previne sequências repetitivas.
- **repeat_penalty**: O valor da penalização para desencorajar tokens repetidos.
- **seed**: Uma semente aleatória (poderíamos usar um valor constante para melhor reprodutibilidade).
- **prompt**: O texto inicial para começar a geração. Note que pedimos ao modelo para gerar um haiku sobre hóquei no gelo, e que o envolvemos com tokens especiais para indicar as partes do utilizador e do assistente na conversa. O modelo irá então completar o prompt com um haiku.
- **device**: Usamos a CPU para computação neste exemplo. O Candle suporta também execução em GPU com CUDA e Metal.

## Passo 3: Descarregar/Preparar Modelo e Tokenizer

```rust
let api = hf_hub::api::sync::Api::new()?;
let model_path = api
    .repo(hf_hub::Repo::with_revision(
        "microsoft/Phi-3-mini-4k-instruct-gguf".to_string(),
        hf_hub::RepoType::Model,
        "main".to_string(),
    ))
    .get("Phi-3-mini-4k-instruct-q4.gguf")?;

let tokenizer_path = api
    .model("microsoft/Phi-3-mini-4k-instruct".to_string())
    .get("tokenizer.json")?;
let tokenizer = Tokenizer::from_file(tokenizer_path).map_err(|e| e.to_string())?;
```

Usamos a API `hf_hub` para descarregar os ficheiros do modelo e do tokenizer a partir do hub de modelos da Hugging Face. O ficheiro `gguf` contém os pesos quantizados do modelo, enquanto o ficheiro `tokenizer.json` é usado para tokenizar o nosso texto de entrada. Uma vez descarregado, o modelo fica em cache, por isso a primeira execução será lenta (pois descarrega os 2.4GB do modelo), mas as execuções seguintes serão mais rápidas.

## Passo 4: Carregar Modelo

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Carregamos os pesos quantizados do modelo para a memória e inicializamos o modelo Phi-3. Este passo envolve ler os pesos do modelo a partir do ficheiro `gguf` e configurar o modelo para inferência no dispositivo especificado (CPU neste caso).

## Passo 5: Processar Prompt e Preparar para Inferência

```rust
let tokens = tokenizer.encode(prompt, true).map_err(|e| e.to_string())?;
let tokens = tokens.get_ids();
let to_sample = sample_len.saturating_sub(1);
let mut all_tokens = vec![];

let mut logits_processor = LogitsProcessor::new(seed, Some(temperature), top_p);

let mut next_token = *tokens.last().unwrap();
let eos_token = *tokenizer.get_vocab(true).get("").unwrap();
let mut prev_text_len = 0;

for (pos, &token) in tokens.iter().enumerate() {
    let input = Tensor::new(&[token], &device)?.unsqueeze(0)?;
    let logits = model.forward(&input, pos)?;
    let logits = logits.squeeze(0)?;

    if pos == tokens.len() - 1 {
        next_token = logits_processor.sample(&logits)?;
        all_tokens.push(next_token);
    }
}
```

Neste passo, tokenizamos o prompt de entrada e preparamos para a inferência convertendo-o numa sequência de IDs de tokens. Também inicializamos o `LogitsProcessor` para gerir o processo de amostragem (distribuição de probabilidades sobre o vocabulário) com base nos valores dados de `temperature` e `top_p`. Cada token é convertido num tensor e passado pelo modelo para obter os logits.

O ciclo processa cada token do prompt, atualizando o logits processor e preparando para a geração do próximo token.

## Passo 6: Inferência

```rust
for index in 0..to_sample {
    let input = Tensor::new(&[next_token], &device)?.unsqueeze(0)?;
    let logits = model.forward(&input, tokens.len() + index)?;
    let logits = logits.squeeze(0)?;
    let logits = if repeat_penalty == 1. {
        logits
    } else {
        let start_at = all_tokens.len().saturating_sub(repeat_last_n);
        candle_transformers::utils::apply_repeat_penalty(
            &logits,
            repeat_penalty,
            &all_tokens[start_at..],
        )?
    };

    next_token = logits_processor.sample(&logits)?;
    all_tokens.push(next_token);

    let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

    if decoded_text.len() > prev_text_len {
        let new_text = &decoded_text[prev_text_len..];
        print!("{new_text}");
        std::io::stdout().flush()?;
        prev_text_len = decoded_text.len();
    }

    if next_token == eos_token {
        break;
    }
}
```

No ciclo de inferência, geramos tokens um a um até atingirmos o comprimento desejado ou encontrarmos o token de fim de sequência. O próximo token é convertido num tensor e passado pelo modelo, enquanto os logits são processados para aplicar penalizações e amostragem. Depois, o próximo token é amostrado, decodificado e adicionado à sequência.  
Para evitar texto repetitivo, é aplicada uma penalização a tokens repetidos com base nos parâmetros `repeat_last_n` e `repeat_penalty`.

Finalmente, o texto gerado é impresso à medida que é decodificado, garantindo uma saída em tempo real.

## Passo 7: Executar a Aplicação

Para executar a aplicação, execute o seguinte comando no terminal:

```bash
cargo run --release
```

Isto deverá imprimir um haiku sobre hóquei no gelo gerado pelo modelo Phi-3. Algo como:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ou

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusão

Seguindo estes passos, podemos realizar geração de texto usando o modelo Phi-3 com Rust e Candle em menos de 100 linhas de código. O código trata do carregamento do modelo, tokenização e inferência, aproveitando tensores e processamento de logits para gerar texto coerente com base no prompt de entrada.

Esta aplicação de consola pode correr em Windows, Linux e Mac OS. Devido à portabilidade do Rust, o código pode também ser adaptado para uma biblioteca que corra dentro de aplicações móveis (afinal, não podemos correr aplicações de consola aí).

## Apêndice: código completo

```rust
use candle_core::{quantized::gguf_file, Device, Tensor};
use candle_transformers::{
    generation::LogitsProcessor, models::quantized_phi3::ModelWeights as Phi3,
};
use rand::Rng;
use std::io::Write;
use tokenizers::Tokenizer;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    // 1. configure basic parameters
    let temperature: f64 = 1.0;
    let sample_len: usize = 100;
    let top_p: Option<f64> = None;
    let repeat_last_n: usize = 64;
    let repeat_penalty: f32 = 1.2;
    let mut rng = rand::thread_rng();
    let seed: u64 = rng.gen();
    let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";

    // we will be running on CPU only
    let device = Device::Cpu;

    // 2. download/prepare model and tokenizer
    let api = hf_hub::api::sync::Api::new()?;
    let model_path = api
        .repo(hf_hub::Repo::with_revision(
            "microsoft/Phi-3-mini-4k-instruct-gguf".to_string(),
            hf_hub::RepoType::Model,
            "main".to_string(),
        ))
        .get("Phi-3-mini-4k-instruct-q4.gguf")?;

    let tokenizer_path = api
        .model("microsoft/Phi-3-mini-4k-instruct".to_string())
        .get("tokenizer.json")?;
    let tokenizer = Tokenizer::from_file(tokenizer_path).map_err(|e| e.to_string())?;

    // 3. load model
    let mut file = std::fs::File::open(&model_path)?;
    let model_content = gguf_file::Content::read(&mut file)?;
    let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;

    // 4. process prompt and prepare for inference
    let tokens = tokenizer.encode(prompt, true).map_err(|e| e.to_string())?;
    let tokens = tokens.get_ids();
    let to_sample = sample_len.saturating_sub(1);
    let mut all_tokens = vec![];

    let mut logits_processor = LogitsProcessor::new(seed, Some(temperature), top_p);

    let mut next_token = *tokens.last().unwrap();
    let eos_token = *tokenizer.get_vocab(true).get("<|end|>").unwrap();
    let mut prev_text_len = 0;

    for (pos, &token) in tokens.iter().enumerate() {
        let input = Tensor::new(&[token], &device)?.unsqueeze(0)?;
        let logits = model.forward(&input, pos)?;
        let logits = logits.squeeze(0)?;

        // Sample next token only for the last token in the prompt
        if pos == tokens.len() - 1 {
            next_token = logits_processor.sample(&logits)?;
            all_tokens.push(next_token);
        }
    }

    // 5. inference
    for index in 0..to_sample {
        let input = Tensor::new(&[next_token], &device)?.unsqueeze(0)?;
        let logits = model.forward(&input, tokens.len() + index)?;
        let logits = logits.squeeze(0)?;
        let logits = if repeat_penalty == 1. {
            logits
        } else {
            let start_at = all_tokens.len().saturating_sub(repeat_last_n);
            candle_transformers::utils::apply_repeat_penalty(
                &logits,
                repeat_penalty,
                &all_tokens[start_at..],
            )?
        };

        next_token = logits_processor.sample(&logits)?;
        all_tokens.push(next_token);

        // decode the current sequence of tokens
        let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

        // only print the new part of the decoded text
        if decoded_text.len() > prev_text_len {
            let new_text = &decoded_text[prev_text_len..];
            print!("{new_text}");
            std::io::stdout().flush()?;
            prev_text_len = decoded_text.len();
        }

        if next_token == eos_token {
            break;
        }
    }

    Ok(())
}
```

Nota: para correr este código em Linux aarch64 ou Windows aarch64, adicione um ficheiro chamado `.cargo/config` com o seguinte conteúdo:

```toml
[target.aarch64-pc-windows-msvc]
rustflags = [
    "-C", "target-feature=+fp16"
]

[target.aarch64-unknown-linux-gnu]
rustflags = [
    "-C", "target-feature=+fp16"
]
```

> Pode visitar o repositório oficial de [exemplos Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) para mais exemplos sobre como usar o modelo Phi-3 com Rust e Candle, incluindo abordagens alternativas para inferência.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.