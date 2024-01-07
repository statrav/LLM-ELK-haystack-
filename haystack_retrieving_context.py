from haystack.dataclasses import Document
from haystack.document_stores import InMemoryDocumentStore
from haystack.components.retrievers import InMemoryBM25Retriever

#######################
####### Version1 ######
#######################

documents = [
    Document(content="German is the the official language of Germany."), 
    Document(content="The capital of France is Paris, and its official language is French."),
    Document(content="Italy recognizes a few official languages, but the most widespread one is Italian."),
    Document(content="Esperanto has been adopted as official language for some microstates as well, such as the Republic of Rose Island, a short-lived microstate built on a sea platform in the Adriatic Sea.")
]

docstore = InMemoryDocumentStore()
docstore.write_documents(documents=documents)

docstore.filter_documents()
# returns [
#     Document(content="German is the the official language of Germany."), 
#     Document(content="The capital of France is Paris, and its official language is French."),
#     Document(content="Esperanto has been adopted as official language for some microstates as well, such as the Republic of Rose Island, a short-lived microstate built on a sea platform in the Adriatic Sea."),
#     Document(content="Italy recognizes a few official languages, but the most widespread one is Italian."),
# ]

'''
#######################
####### Version2 ######
#######################

retriever = InMemoryBM25Retriever(document_store=docstore)
result = retriever.run(query="Rose Island", top_k=1)
# returns [
#     Document(content="Esperanto has been adopted as official language for some microstates as well, such as the Republic of Rose Island, a short-lived microstate built on a sea platform in the Adriatic Sea.")
# ]

retriever.run(query="Rose Island", top_k=3)
# returns [
#     Document(content="Esperanto has been adopted as official language for some microstates as well, such as the Republic of Rose Island, a short-lived microstate built on a sea platform in the Adriatic Sea.")
#     Document(content="Italy recognizes a few official languages, but the most widespread one is Italian."),
#     Document(content="The capital of France is Paris, and its official language is French."),
# ]

print(result)'''