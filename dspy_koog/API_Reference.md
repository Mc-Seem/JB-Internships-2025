### Overview

The goal was to extend the existing Koog model abstractions to make high level model selection simple, composable and extendable. Users can filter and sort LLMs **functional-style**, inspired by Kotlin's standard library: `filter`, `minByOrNull`, etc.

### Abstractions

##### `LLModel`

An **existing** dataclass representing a specific LLM. I propose adding new metadata fields for richer selection:
- `cutoffDate: LocalDate` - last training cutoff date
- `inputTokenCost: Double` - cost per input token in USD
- `outputTokenCost: Double` - cost per output token in USD
	- Thought: potentially include `reasoningTokenCost` and `cachedTokenCost`, but usage is often implicit and hard to infer from the outside
- `inferenceTime: Duration` - average time to generate ~1000 tokens

##### `LLModels`

A top-level namespace object holding immutable model registries:

```kotlin
object LLModels {
    val all: List<LMLodel> = ... // Predefined models
    val openai: List<LLModel> = all.filter { it.provider == LLMProvider.OpenAI }
    // ... Essentially provides shortcuts to popular user filters
}
```

##### Extension Functions on `List<LLModel>`

Convenience methods for most common selections:

```kotlin
fun List<LLModel>.cheapest(): LLModel?
fun List<LLModel>.fastest(): LLModel?
fun List<LLModel>.latest(): LLModel?
```

### Examples

Select the cheapest model that can do tool calling, vision and moderation, has 500k context window and whose output token costs less than 0.02.

```kotlin
val bestModel = LLModels.all
    .filter {
        it.capabilities.containsAll(listOf(
            LLMCapability.ToolCalling,
            LLMCapability.Vision,
            LLMCapability.Moderation
        ))
    }
    .filter { it.outputTokenCost <= 0.02 }
    .filter { it.contextLength >= 500_000 }
    .cheapest()
```

### Design Considerations

##### Pros

- Leverages standard functional style $\implies$ selection is intuitive and readable
- Extendable; new metadata fields / registries can be added with no breaking changes

##### Cons

- Registries need curated updates as providers evolve
- Metadata has to be reliably maintained

##### Under-the-hood Changes

- Extend `LLModel` with new fields
- Provide curated registries of "built-in" models in `LLModels`
- Implement extensions on `List<LLModel>`