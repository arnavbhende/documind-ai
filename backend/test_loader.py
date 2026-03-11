import sys
import os

sys.path.append(os.path.dirname(__file__))
from document_loader import load_pdf


def main():
    if len(sys.argv) < 2:
        print("Usage: python test_loader.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    documents = load_pdf(pdf_path)

    print(f"Number of pages loaded: {len(documents)}")
    if documents:
        print(f"\nFirst 200 characters of page 1:\n{documents[0].page_content[:200]}")


if __name__ == "__main__":
    main()
