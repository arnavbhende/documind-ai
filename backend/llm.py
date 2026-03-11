from langchain_groq import ChatGroq


def get_llm():
    """
    Initialize the language model used to generate answers.
    """

    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0
    )

    return llm