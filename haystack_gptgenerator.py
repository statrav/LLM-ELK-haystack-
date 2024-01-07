from haystack.components.generators import GPTGenerator

api_key = "YOUR_OWN_API_KEY"

generator = GPTGenerator(api_key=api_key)
result = generator.run(prompt="What's the official language of France?")
print(result)
# returns {"replies": ['The official language of France is French.']}

