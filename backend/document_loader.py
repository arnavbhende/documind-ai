from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        return documents
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return []