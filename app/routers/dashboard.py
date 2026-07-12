from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates

from app.auth.dependencies import get_current_user
from app.auth.models import User


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


templates = Jinja2Templates(
    directory="app/templates"
)


@router.get(
    "",
    response_class=HTMLResponse
)
def dashboard(
    request: Request,
    user = Depends(get_current_user),
):
    if not user:
        return RedirectResponse("/login")

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "user": user
        }
    )