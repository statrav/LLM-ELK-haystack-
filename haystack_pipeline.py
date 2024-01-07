from haystack import Pipeline
from haystack.dataclasses import Document
from haystack.components.generators import GPTGenerator
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack.document_stores import InMemoryDocumentStore
from haystack.components.retrievers import InMemoryBM25Retriever

api_key = "YOUR_OWN_API_KEY"

documents = [
    Document(content="German is the the official language of Germany."), 
    Document(content="The capital of France is Paris, and its official language is French."),
    Document(content="Italy recognizes a few official languages, but the most widespread one is Italian."),
    Document(content="Esperanto has been adopted as official language for some microstates as well, such as the Republic of Rose Island, a short-lived microstate built on a sea platform in the Adriatic Sea.")
]

docstore = InMemoryDocumentStore()
docstore.write_documents(documents=documents)

template = """
Given the following information, answer the question.

Context: 
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: What's the official language of {{ country }}?
"""
pipe = Pipeline()

pipe.add_component("retriever", InMemoryBM25Retriever(document_store=docstore))
pipe.add_component("prompt_builder", PromptBuilder(template=template))
pipe.add_component("llm", GPTGenerator(api_key=api_key))
pipe.connect("retriever", "prompt_builder.documents")
pipe.connect("prompt_builder", "llm")

result = pipe.run({
    "retriever": {"query": "country"},
    "prompt_builder": {
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

print(result)