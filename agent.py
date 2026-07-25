from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

def chatbot(prompt: str):
    agent = ChatGoogleGenerativeAI(
    model ="gemini-1.5-flash",
    temperature=0.3,
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