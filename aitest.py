import ollama

response = ollama.chat(model='mistral', messages=[
    {'role': 'user', 'content': 'Write a professional resignation letter to my boss, expressing gratitude and stating my last working day.'}
])

print(response['message']['content'])
