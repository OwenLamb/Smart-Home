from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are an assistant named Regis. Do not put reactions in *'s 

Here is the conversation history: {history}

Input: {input}

"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
context = ""

while True:
    user_input = input("You: ")  # Rename the variable to avoid shadowing
    if user_input.lower() == "exit":
        break
    result = chain.invoke({"history": context, "input": user_input})
    print(result)
    context += f"\nUser: {user_input}\nAI: {result}"


