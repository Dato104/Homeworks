import re


def read_md_file(filename):
    with open(filename, 'r') as f:
        raw_text = f.read()

    return raw_text


def sentence_chunk(text: str, sentences_per_chunk: int = 5) -> list:
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]

    chunks = []
    for i in range(0, len(sentences), sentences_per_chunk):
        group = sentences[i:i + sentences_per_chunk]
        chunks.append(' '.join(group))

    return chunks


def check_sentence_chunk():
    md_content = read_md_file('company_handbook.md')
    md_chunks = sentence_chunk(md_content, sentences_per_chunk=5)

    print(len(md_chunks))
    print(md_chunks[0])

check_sentence_chunk()



