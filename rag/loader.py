from langchain_community.document_loaders import PyPDFLoader

def load_pdf(path):

    loader = PyPDFLoader(path)

    docs = loader.load()

    text = ""

    for doc in docs:

        text += doc.page_content

    return text