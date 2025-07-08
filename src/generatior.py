from src.retrival import Retrival
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os
class Generator:
    def __init__(self):
        load_dotenv()
        
        self.prompt = """You are a helpful and knowledgeable assistant. Your primary goal is to provide accurate and concise answers to user questions **strictly based on the context provided below**.

            **Instructions:**
            1. Read the `Context` carefully.
            2. Answer the `Question` using **only** the information found in the `Context`.
            3. Do not use any outside knowledge.
            4. If the `Context` does not contain enough information to answer the `Question`, state clearly: "I apologize, but the provided context does not contain enough information to answer your question."
            5. Keep your answer focused and to the point.

            ---

            **Context:**
            {context}

            ---

            **Question:**
            {question}

            ---

            **Answer:**"""
        self.retrive = Retrival()
        self.llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
    def llm_response(self, user_query:str):
        results = self.retrive.retrive_documents(user_query)
        result_text = []
        for i, doc_text in enumerate(results['documents'][0]):
            result_text.append(doc_text)
        context_str = "\n".join(f"-{chunk}" for chunk in result_text)
        combine_input = self.prompt.format(context=context_str, question=user_query)
        return self.llm.invoke(combine_input)

if __name__ == "__main__":
    gen = Generator()
    print(gen.llm_response("is there any account opened for the same user?"))
