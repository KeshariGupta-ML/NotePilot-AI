from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.auth.schemas import UserCreate
from app.auth.schemas import UserLogin
from app.auth.service import AuthService
from app.core.database import get_db
from app.core.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register_user(
        full_name: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db),
):
    user_data = UserCreate(
        full_name=full_name,
        email=email,
        password=password
    )

    try:

        AuthService.register(
            db,
            user_data
        )


    except ValueError as e:

        return RedirectResponse(
            url=f"/register?error={str(e)}",
            status_code=302
        )

    return RedirectResponse(
        url="/login?message=Registration successful. Please login.",
        status_code=302
    )


@router.post("/login")
def login_user(
        email: str = Form(...),
        password: str = Form(...),
        response: Response = None,
        db: Session = Depends(get_db),
):
    user = AuthService.authenticate(
        db,
        email,
        password
    )

    if not user:
        return RedirectResponse(
            url="/login?error=Invalid email or password",
            status_code=302
        )

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    redirect = RedirectResponse(
        url="/dashboard",
        status_code=302
    )

    redirect.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax"
    )

    return redirect


@router.get("/logout")
def logout():

    response = RedirectResponse(
        url="/login?message=Logged out successfully",
        status_code=302
    )

    response.delete_cookie(
        key="access_token"
    )

    return response