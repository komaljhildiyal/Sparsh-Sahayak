from pypdf import PdfReader


class DocumentParser:

    def parse_document(self,file_path):

        text=""

        if file_path.endswith(".pdf"):

            reader=PdfReader(file_path)

            for page in reader.pages:

                extracted=page.extract_text()

                if extracted:

                    text += extracted

        return text