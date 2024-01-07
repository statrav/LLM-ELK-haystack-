from haystack import Pipeline
from haystack.components.generators import GPTGenerator
from haystack.components.builders.prompt_builder import PromptBuilder

api_key = "YOUR_OWN_API_KEY"

pipe = Pipeline()
pipe.add_component("prompt_builder", PromptBuilder(template="What's the official language of {{ country }}?"))
pipe.add_component("llm", GPTGenerator(api_key=api_key))
pipe.connect("prompt_builder", "llm")


#######################
####### Version1 ######
#######################
pipe.run({"prompt_builder": {"country": "France"}})
# returns {"llm": {"replies": ['The official language of France is French.'] }}

'''
#######################
####### Version2 ######
#######################

pipe.run({"prompt_builder": {"country": "the Republic of Rose Island"}})
# returns {
#     "llm": {
#         "replies": [
#             'The official language of the Republic of Rose Island was Italian.'
#         ]
#     }
# }


#######################
####### Version3 ######
#######################

context_template = """
Given the following information, answer the question.
Context: {{ context }}
Question: {{ question }}
"""
language_template = "What's the official language of {{ country }}?"

pipe = Pipeline()
pipe.add_component("context_prompt", PromptBuilder(template=context_template))
pipe.add_component("language_prompt", PromptBuilder(template=language_template))
pipe.add_component("llm", GPTGenerator(api_key=api_key))
pipe.connect("language_prompt", "context_prompt.question")
pipe.connect("context_prompt", "llm")

# pipe.run({
#     "context_prompt": {"context": "Rose Island had its own government, currency, post office, and commercial establishments, and the official language was Esperanto."}
#     "language_prompt": {"country": "the Republic of Rose Island"}
# })

# returns {
#     "llm": {
#         "replies": [
#             'The official language of the Republic of Rose Island is Esperanto.'
#         ]
#     }
# }


#######################
####### Version4 ######
#######################

template = """
Given the following information, answer the question.
Context: {{ context }}
Question: What's the official language of {{ country }}?
"""
pipe = Pipeline()
pipe.add_component("prompt_builder", PromptBuilder(template=template))
pipe.add_component("llm", GPTGenerator(api_key=api_key))
pipe.connect("prompt_builder", "llm")

result = pipe.run({
    "prompt_builder": {
        "context": "Rose Island had its own government, currency, post office, and commercial establishments, and the official language was Esperanto.",
        "country": "the Republic of Rose Island"
    }
})
# returns {
#     "llm": {
#         "replies": [
#             'The official language of the Republic of Rose Island is Esperanto.'
#         ]
#     }
# }

print(result)'''
