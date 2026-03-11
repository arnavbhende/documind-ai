from langchain_community.vectorstores import Chroma


def create_vector_store(chunks, embeddings):
    """
    Create a Chroma vector database from document chunks.
    """

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    return vectordb