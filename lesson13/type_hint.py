# from typing import List
# from typing import Dict
# from typing import Optional
from typing import Union, Any, Literal, Final

name: str = "Дима"
age: int = 12
height: float = 2.3


# users: List[str] = ["Дима", "Олег"]
users: list[str] = ["Дима", "Олег"]


def convert_celc_to_far(calculate_temp: float) -> float:
    return (calculate_temp * 9 / 5) + 32


def some_func(cache: dict[str, str]) -> bool:
    return False


# optional_var: Union[int, float, None]
optional_var: int | float | None

any_var: Any = 12

GENDER = Literal["male", "female", "non–conforming"]


def create_user(gener: GENDER) -> bool:
    return True


MAX_AGE: Final = 18

