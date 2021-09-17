from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter(
    tags=["Redirect"]
)

@router.get("/")
def main():
    return RedirectResponse(url="/docs")