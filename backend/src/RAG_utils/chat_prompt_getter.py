from langchain.prompts import PromptTemplate


def get_chat_prompt():
    template = """<|system|>
You are a helpful assistant.<|end|>
<|user|>
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use two sentences maximum and keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. Context: {context}. Question: {question}
Helpful Answer:
<|end|>
<|assistant|>
"""
    prompt = PromptTemplate.from_template(template)
    return prompt