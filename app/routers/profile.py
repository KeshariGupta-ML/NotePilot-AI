from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates

from app.auth.dependencies import get_current_user


router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)



@router.get(
    "/profile",
    response_class=HTMLResponse
)
def profile(
    request: Request,
    user=Depends(get_current_user)
):

    return templates.TemplateResponse(
        request=request,
        name="profile.html",
        context={
            "user": user
        }
    )



@router.get(
    "/login",
    response_class=HTMLResponse
)
def login_page(
    request: Request,
    message: str | None = None,
    error: str | None = None,
    user=Depends(get_current_user)
):

    if user:
        return RedirectResponse(
            "/dashboard"
        )

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "user": None,
            "message": message,
            "error": error
        }
    )

@router.get(
    "/register",
    response_class=HTMLResponse
)
def register_page(
    request: Request,
    error: str | None = None,
    user=Depends(get_current_user)
):

    if user:
        return RedirectResponse(
            "/dashboard"
        )


    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={
            "user": None,
            "error": error
        }
    )