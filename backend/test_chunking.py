from document_loader import load_pdf
from text_splitter import split_documents


docs = load_pdf("uploads/sample.pdf")

chunks = split_documents(docs)

print("Original pages:", len(docs))
print("Total chunks:", len(chunks))

print("\nFirst chunk preview:\n")
print(chunks[0].page_content[:300])