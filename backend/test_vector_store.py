from document_loader import load_pdf
from text_splitter import split_documents
from embedding import get_embedding_model
from vector_store import create_vector_store

# Load PDF
docs = load_pdf("uploads/sample.pdf")

# Split into chunks
chunks = split_documents(docs)

# Load embedding model
embeddings = get_embedding_model()

# Create vector database
vectordb = create_vector_store(chunks, embeddings)

print("Vector database created successfully!")
print("Number of chunks stored:", len(chunks))