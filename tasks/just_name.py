from enum import Enum, auto

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # * type checking is false at runtime, but you have provide annotations
    from typing import (
        List,  # * for assignment aliases only
        Mapping,
        Optional,
        Tuple,
    )  # TODO import others

    from numpy.typing import ArrayLike, NDArray
    from typing_extensions import Protocol

from numpy import ndarray, int16, arange, int64, pi  # TODO import more

# TODO rename every function and class following
# TODO provide types everywhere
# * note: if you have something list-like but it doesn't use list methods (append, copy, remove ...), use these:
# - Iterable for ones that need no indexing or slicing
# - Sequence otherwise
# * similarly, prefer Mapping over dict if it doesn't need dict methods


def sum_of_range_five() -> int:
    return sum(range(5))


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


class ActivitiesLabels(NamedTuple):
    labels_activities: Mapping[int, str]
    activities_labels: Mapping[str, int]


radius = int


def calculate_circle_area(radius: int) -> float:
    return pi * radius**2


Vector = List[float]  # * future annotation doesn't not help with aliases


def scale_vector_elements(scale: float, vector: Vector) -> Vector:
    return [scale * num for num in vector]


class Developers(Enum):
    ALEXANDER = auto()
    ILYA = auto()
    ROMA = auto()
    one = auto()
    two = auto()
    tri = auto()

    def __str__(self) -> str:
        return self.name


def convert_type_to_ndarray(array: any) -> ndarray:
    return array(array)


def arange_int16(length: int) -> NDArray[int16]:
    return arange(length, dtype=int16)


def arange_int64(length: int) -> NDArray[int64]:
    return arange(length, dtype=int64)


class CocaCola(Protocol):
    @property
    def cup(self) -> None:
        "Just a cup"
        print("Get cup")

    def prazdnik_k_nam_prihodit(self) -> int:
        pass

    def do_something(self) -> str:
        return "I do something with CocaCola"

    def get_cola(self) -> None:
        print("I get cola")


# *****************************************************************
# *****************************************************************
# *****************************************************************


# TODO check yourself (part of examples provided)
if __name__ == "__main__":  # =================================================================
    abc = sum_of_range_five()  # ! ERROR: "bar" does not return a value
    abc += 1
    # =================================================================
    r = calculate_circle_area(radius)  # * OK

    integer_radius = 4 + 2.5j
    r = calculate_circle_area(integer_radius)  # ! ERROR
    # =================================================================
    a = scale_vector_elements(scalar=2.0, vector=[1.0, 2.0, 3.0])  # * OK
    a = scale_vector_elements(scalar=2.0, vector={1.0, 2.0, 3.0})  # ! ERROR
    # =================================================================
    for pyfile in collect():  # * OK
        print(pyfile)

    collect().append("text_clustering.py")  # ! ERROR
    # =================================================================
    arange_int16(32767)  # * OK
    arange_int64(32768)  # ! no type checker message though, will lead to an error
