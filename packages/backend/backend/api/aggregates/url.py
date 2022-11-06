from ..router import router
from .usecases.lodgings import get_lodgings
from .usecases.stays import get_stays

router.get("/aggregates/lodgings/{user_id}")(get_lodgings)
router.get("/aggregates/stays/{user_id}")(get_stays)
