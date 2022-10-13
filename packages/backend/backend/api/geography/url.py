from ..router import router
from .usecases.geography import create_geography

router.post("/geography")(create_geography)
