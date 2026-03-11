from document_loader import load_pdf
from text_splitter import split_documents
from embedding import get_embedding_model
from vector_store import create_vector_store
from retriever import get_retriever

# Load PDF
docs = load_pdf("uploads/sample.pdf")

# Split into chunks
chunks = split_documents(docs)

# Load embeddings
embeddings = get_embedding_model()

# Create vector DB
vectordb = create_vector_store(chunks, embeddings)

# Create retriever
retriever = get_retriever(vectordb)

# Ask a question
query = "What does the document say about artificial intelligence?"

results = retriever.invoke(query)

print("Top retrieved document chunks:\n")

for doc in results:
    print(doc.page_content)
    print("-----")