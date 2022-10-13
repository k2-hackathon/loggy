from ..router import router
from .schema import GetResponseBody, PostResponseBody
from .usecases.users import create_user, list_user

router.get("/users", response_model=GetResponseBody)(list_user)
router.post("/users", response_model=PostResponseBody)(create_user)
