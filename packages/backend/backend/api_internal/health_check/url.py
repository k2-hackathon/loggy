from ..router import router


# TODO: deep health check
def health_check():
    return {"success": True}


router.get("/health")(health_check)
