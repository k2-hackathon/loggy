from fastapi import APIRouter


def health_check():
    try:
        return "success"
    except Exception as e:
        return f"API has raised an exception: {e}"


router = APIRouter()

router.get("/healthcheck")(health_check)
