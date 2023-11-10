import openai

openai.api_key = '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'

messages = []
while True:
    content = input("User: ")
    messages.append({"role":"user", "content":content})

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role":"assistant", "content": chat_response})