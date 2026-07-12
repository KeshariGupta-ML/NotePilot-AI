from io import BytesIO

import fitz
from docx import Document
from fastapi import UploadFile


class TranscriptHelper:

    @staticmethod
    async def extract_text(
        file: UploadFile,
    ) -> str:
        """
        Extract transcript text based on file extension.
        """

        extension = file.filename.split(".")[-1].lower()

        if extension == "txt":
            return await TranscriptHelper.extract_txt(file)

        if extension == "pdf":
            return await TranscriptHelper.extract_pdf(file)

        if extension == "docx":
            return await TranscriptHelper.extract_docx(file)

        raise ValueError(
            "Unsupported file type."
        )

    @staticmethod
    async def extract_txt(
        file: UploadFile,
    ) -> str:

        contents = await file.read()

        return contents.decode(
            "utf-8",
            errors="ignore",
        )

    @staticmethod
    async def extract_pdf(
        file: UploadFile,
    ) -> str:

        contents = await file.read()

        pdf = fitz.open(
            stream=contents,
            filetype="pdf",
        )

        text = []

        for page in pdf:

            page_text = page.get_text()

            if page_text:
                text.append(page_text)

        pdf.close()

        return "\n".join(text)

    @staticmethod
    async def extract_docx(
        file: UploadFile,
    ) -> str:

        contents = await file.read()

        document = Document(
            BytesIO(contents)
        )

        paragraphs = []

        for paragraph in document.paragraphs:

            if paragraph.text.strip():
                paragraphs.append(
                    paragraph.text
                )

        return "\n".join(paragraphs)