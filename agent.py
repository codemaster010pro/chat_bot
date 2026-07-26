from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

def chatbot(prompt: str):
    agent = ChatGroq(
    model ="llama-3.1-8b-instant",
    temperature=0.4,
    )


    response = agent.invoke([
        SystemMessage(content="you are a best chatbot which have knowledge of many fields,you are safe and professional"),
        HumanMessage(content= prompt)
    ])
    return response.content

def main():
    chatbot()
if __name__ == "__main__":
    main()