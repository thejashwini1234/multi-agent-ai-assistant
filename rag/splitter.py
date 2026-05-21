from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text):

    chunks = []

    chunk_size = 500

    for i in range(
        0,
        len(text),
        chunk_size
    ):

        chunks.append(
            text[i:i+chunk_size]
        )

    return chunks