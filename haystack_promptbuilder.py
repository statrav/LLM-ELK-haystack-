from haystack.components.builders.prompt_builder import PromptBuilder

prompt_builder = PromptBuilder(template="What's the official language of {{ country }}?")
prompt_builder.run(country="France")
# returns {'prompt': "What's the official language of France?"}