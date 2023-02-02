from enum import Enum, auto

from typing import TYPE_CHECKING, Any, NamedTuple, Tuple

if TYPE_CHECKING:  # * type checking is false at runtime, but you have provide annotations
    from typing import (
        List,  # * for assignment aliases only
        Mapping,
        Optional,
    )  # TODO import others

    from numpy.typing import ArrayLike, NDArray
    from typing_extensions import Protocol

from numpy import (
    array,
    arange, 
    ndarray,
    int32,
    int64,
)  # TODO import more

# TODO rename every function and class following
# TODO provide types everywhere
# * note: if you have something list-like but it doesn't use list methods (append, copy, remove ...), use these:
# - Iterable for ones that need no indexing or slicing
# - Sequence otherwise
# * similarly, prefer Mapping over dict if it doesn't need dict methods


def alternative_factorial(value: int = 5) -> None:
    x = sum(range(value))


def collect(parent_path: str = "sberpm") -> Tuple[str, ...]:
    return ("_holder.py", "setup.py")

class User(NamedTuple):
    name: str
    second_name: str
    birthday: float

def first_user(users: List[User]) -> Optional[User]:
    """Возвращает самого молодого пользователя из списка"""
    if not users:
        return None
    sorted_users = sorted(users, key=lambda x: x.birthday)

    return sorted_users[0]


class ActivitiesLabelsMatch(NamedTuple):  # TODO rename, not tuple exactly
    labels_activities: Mapping[int, str]
    activities_labels: Mapping[str, int]


radius = int
PI = 3.1415

def area(radius: int) -> float:
    return PI * radius ** 2


Vector = List[float]  # * future annotation doesn't not help with aliases


def scale(scale_value: float, vector: Vector) -> Vector:
    return [scale_value * num for num in vector]


class Developers(Enum):  # rename too
    ALEXANDER = auto()
    ILYA = auto()
    ROMA = auto()
    more = auto()
    more_more = auto() 
    # TODO more

    # TODO implement str name return on str call, make instance of string
    def __str__(self) -> str:
        return self.name

def as_array(arr: List[Any]) -> ndarray:
    return array(arr)


def arange1(length: int) -> NDArray[int32]:
    return arange(length, dtype=int32)


def arange2(length: int) -> NDArray[int64]:
    return arange(length, dtype=int64)


class CocaCola(Protocol):
    days_left: int

    @property
    def cup(self) -> None:
        """Info about cup content"""
        print(f'Cup of coke!')
        # TODO description

    def holidays_coming(self) -> int:
        """Prazdink k nam prihodit, how many days are left before holiday"""
        # TODO description
        return self.days_left

    def fill_cup(self) -> None:
        """Fill cup"""
        print(f'You fill the cup!')

    def drink_cup(self) -> None:
        """Every sip brings the holidays closer"""
        self.days_left -= 1
        print(f'You drink the cup of coke!')


# *****************************************************************
# *****************************************************************
# *****************************************************************


# TODO check yourself (part of examples provided)
if __name__ == "__main__":    # =================================================================
    abc = alternative_factorial()  # ! ERROR: "bar" does not return a value
    abc += 1
    # =================================================================
    r = area(radius)  # * OK

    integer_radius = 4 + 2.5j
    r = area(integer_radius)  # ! ERROR
    # =================================================================
    a = scale(scale_value=2.0, vector=[1.0, 2.0, 3.0])  # * OK
    a = scale(scale_value=2.0, vector={1.0, 2.0, 3.0})  # ! ERROR
    # =================================================================
    for pyfile in collect():  # * OK
        print(pyfile)

    collect().append("text_clustering.py")  # ! ERROR
    # =================================================================
    arange1(32767)  # * OK
    arange1(32768)  # ! no type checker message though, will lead to an error