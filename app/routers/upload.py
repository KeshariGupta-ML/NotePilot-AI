from io import BytesIO

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from pathlib import Path
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.services.helpers import TranscriptHelper
from app.agents.orchestrator import create_note_agent
from app.services.pdf_service import create_pdf

agent = create_note_agent()


class NotesRequest(BaseModel):
    transcript: str


router = APIRouter(prefix="/transcript",
                   tags=["Transcript"], )

templates = Jinja2Templates(
    directory="app/templates"
)
ALLOWED_EXTENSIONS = {
    ".txt",
    ".pdf",
    ".docx",
}

MAX_FILE_SIZE = 20 * 1024 * 1024


@router.post("/upload")
async def upload_transcript(
        file: UploadFile = File(...),
):
    extension = Path(
        file.filename
    ).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        return {
            "success": False,
            "message":
                "Only TXT, PDF and DOCX files are supported.",
        }

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        return {
            "success": False,
            "message":
                "Maximum file size is 20 MB.",
        }

    await file.seek(0)

    try:

        transcript = await TranscriptHelper.extract_text(
            file
        )

    except Exception as e:

        return {
            "success": False,
            "message": str(e),
        }

    return {
        "success": True,
        "transcript": transcript,
    }


@router.post("/notes/generate")
async def generate_notes(
        request: NotesRequest
):
    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content":
                        request.transcript
                }
            ]
        }
    )
    message = result["messages"][-1]

    content = message.content

    if isinstance(content, str):

        notes = content

    elif isinstance(content, list):

        parts = []

        for item in content:

            if isinstance(item, dict):

                if item.get("type") == "text":
                    parts.append(
                        item.get("text", "")
                    )

            elif isinstance(item, str):

                parts.append(item)

        notes = "\n".join(parts)


    else:
        notes = str(content)

    return {
        "success": True,
        "notes": notes
    }


class PDFRequest(BaseModel):
    notes: str


@router.post("/download/pdf")
async def download_pdf(request: PDFRequest):
    pdf_file = create_pdf(
        request.notes
    )

    return StreamingResponse(
        BytesIO(pdf_file),
        media_type="application/pdf",
        headers={
            "Content-Disposition":
                "attachment; filename=AI_Lecture_Notes.pdf"
        }
    )
