def get_retriever(vectordb):
    """
    Convert the vector database into a retriever
    that can search for relevant document chunks.
    """

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    return retriever