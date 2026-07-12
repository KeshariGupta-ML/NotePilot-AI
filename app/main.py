from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles

from app.auth.dependencies import get_current_user
from app.core.config import settings
from app.core.database import Base
from fastapi.responses import RedirectResponse
from app.core.database import engine
from app.auth.router import router as auth_router
from app.routers.dashboard import router as dashboard_router
from app.routers.profile import router as profile_router
from app.routers.upload import router as upload_router



Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(profile_router)
app.include_router(upload_router)


@app.get("/")
def home(request: Request):
    return RedirectResponse(
        url="/login"
    )
@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "application": settings.APP_NAME
    }

#
# if __name__ == "__main__":
#
#     import uvicorn
#
#     uvicorn.run(
#         "app.main:app",
#         host="0.0.0.0",
#         port=8000,
#         reload=True
#     )