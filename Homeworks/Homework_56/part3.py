from pypdf import PdfReader


def read_md_file(filename: str) -> str:
    with open(filename, 'r') as f:
        raw_text = f.read()

    return raw_text


def read_pdf_file(filename: str) -> str:
    reader = PdfReader(filename)

    full_text = ''
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            full_text += page_text + '\n'

    return full_text


def check_read_pdf_file():
    pdf_content = read_pdf_file('company_handbook.pdf')
    print(pdf_content[:500])

check_read_pdf_file()

