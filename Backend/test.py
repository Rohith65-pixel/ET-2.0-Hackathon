import ollama

response = ollama.chat(
    model='qwen2.5vl:7b', 
    messages=[
        {
            'role': 'user',
            'content': 'Write a 3-word slogan for a coffee shop.',
        },
    ]
)

print(response['message']['content'])
# Output: "Wake, brew, enjoy."
