from ..router import router
from .schema.users import User
from .usecases.users import create_user, read_user

router.get("/users/{id}")(read_user)
router.post("/users")(create_user)  # TODO: response_model=をつける
