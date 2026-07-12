from fastapi import Depends, HTTPException, Request
from jose import JWTError
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import decode_access_token
from app.auth.repository import UserRepository


def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
):

    token = request.cookies.get("access_token")

    if not token:
        return None
    try:

        payload = decode_access_token(token)

        user_id = payload.get("sub")

        if not user_id:
            return None

    except JWTError:
        return None

    user = UserRepository.get_by_id(
        db,
        int(user_id)
    )


    if not user:
        return None


    return user