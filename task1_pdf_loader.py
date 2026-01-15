from langchain_community.document_loaders import PyPDFLoader

# Path to your local PDF file (adjust as needed)
pdf_path = "data/A_Comprehensive_Review_of_Low_Rank_Adaptation_in_Large_Language_Models_for_Efficient_Parameter_Tuning-1.pdf"

# Initialize the loader with the PDF path
loader = PyPDFLoader(pdf_path)

# Load the documents (extracts text from each page)
documents = loader.load()

# Print some info to verify
print(f"Loaded {len(documents)} pages from the PDF.")
if documents:
    print(f"Sample content from page 1: {documents[0].page_content[:200]}...")  # First 200 chars of page 1
    print(f"Metadata for page 1: {documents[0].metadata}")