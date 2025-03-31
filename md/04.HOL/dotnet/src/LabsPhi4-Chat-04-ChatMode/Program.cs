using Microsoft.ML.OnnxRuntimeGenAI;

// Phi4
var modelPath = @"d:\phi\models\Phi-4-mini-instruct-onnx\cpu_and_mobile\cpu-int4-rtn-block-32-acc-level-4\";


// initialize model
var model = new Model(modelPath);
var tokenizer = new Tokenizer(model);
var generatorParams = new GeneratorParams(model);

generatorParams.SetSearchOption("max_length", 2048);
generatorParams.SetSearchOption("past_present_share_buffer", false);
using var tokenizerStream = tokenizer.CreateStream();

using var generator = new Generator(model, generatorParams);
Console.Write("Prompt: ");
var prompt = Console.ReadLine();

// Example Phi-3 template
var sequences = tokenizer.Encode($"<|user|>{prompt}<|end|><|assistant|>");

do
{
    generator.AppendTokenSequences(sequences);
    var watch = System.Diagnostics.Stopwatch.StartNew();
    while (!generator.IsDone())
    {
        generator.GenerateNextToken();
        Console.Write(tokenizerStream.Decode(generator.GetSequence(0)[^1]));
    }
    Console.WriteLine();
    watch.Stop();
    var runTimeInSeconds = watch.Elapsed.TotalSeconds;
    var outputSequence = generator.GetSequence(0);
    var totalTokens = outputSequence.Length;
    Console.WriteLine($"Streaming Tokens: {totalTokens} Time: {runTimeInSeconds:0.00} Tokens per second: {totalTokens / runTimeInSeconds:0.00}");
    Console.Write("Next prompt: ");
    prompt = Console.ReadLine();
    sequences = tokenizer.Encode($"<|user|>{prompt}<|end|><|assistant|>");
} while (!string.IsNullOrEmpty(prompt));

