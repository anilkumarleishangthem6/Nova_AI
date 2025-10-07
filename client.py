from openai import OpenAI

# pip install openai 
# defaults to getting the key using os.environ.get("OpenAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI (
    api_key="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",
    ) #billed api key is needed for gpt-4 (free trial keys will not work) 


completion = client.chat.completions.create(    
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are virtual assistant named Nova skilled in explaining general tasks like Alexa and Gemini  in simple terms with creative fair."},
        {"role": "user", "content": "What is AI?"}
    ]
)

print(completion.choices[0].message.content)
