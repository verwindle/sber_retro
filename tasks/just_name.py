from enum import Enum, auto

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # * type checking is false at runtime, but you have provide annotations
    from typing import (
        Generator,
        List,  # * for assignment aliases only
        Mapping,
        Sequence,
    )  # TODO import others

    from numpy.typing import ArrayLike, NDArray
    from typing_extensions import Protocol

from numpy import array, ndarray  # TODO import more

# TODO rename every function and class following
# TODO provide types everywhere
# * note: if you have something list-like but it doesn't use list methods (append, copy, remove ...), use these:
# - Iterable for ones that need no indexing or slicing
# - Sequence otherwise
# * similarly, prefer Mapping over dict if it doesn't need dict methods


def bar():
    x = sum(range(5))


def collect(parent_path = "sberpm"):
    return ("_holder.py", "setup.py")


def first_user(users):
    """Возвращает самого молодого пользователя из списка"""
    if not users:
        return None

    print(users[0])
    sorted_users = sorted(users, key=lambda x: x.birthday)

    return sorted_users[0]


class Activities(tuple):  # TODO rename, not tuple exactly
    labels_activities: Mapping[int, str]
    activities_labels: Mapping[str, int]


radius = int


def area(r):
    return 3.1415 * r * r


Vector = List[float]  # * future annotation doesn't not help with aliases


def scale(scalar, vector) -> Vector:
    return [scalar * num for num in vector]


class Devs(Enum):  # rename too
    ALEXANDER = auto()
    ILYA = auto()
    ROMA = auto()
    # TODO more

    # TODO implement str name return on str call, make instance of string


def as_array(arr) -> ndarray:
    return array(arr)


def arange1(length: int) -> NDArray[np.int16]:
    return np.arange(length, dtype=np.int32)


def arange2(length: int) -> NDArray[np.int64]:
    return np.arange(length, dtype=np.int64)


class CocaCola(Protocol):
    @property
    def cap(self):
        # TODO description

    def prazdnik_k_nam_prihodit(self) -> int:
        # TODO description

    # TODO two more methods


# *****************************************************************
# *****************************************************************
# *****************************************************************


# TODO check yourself (part of examples provided)
if __name__ == "__main__":    # =================================================================
    abc = bar()  # ! ERROR: "bar" does not return a value
    abc += 1
    # =================================================================
    r = area(radius)  # * OK

    integer_radius = 4 + 2.5j
    r = area(integer_radius)  # ! ERROR
    # =================================================================
    a = scale(scalar=2.0, vector=[1.0, 2.0, 3.0])  # * OK
    a = scale(scalar=2.0, vector={1.0, 2.0, 3.0})  # ! ERROR
    # =================================================================
    for pyfile in collect():  # * OK
        print(pyfile)

    collect().append("text_clustering.py")  # ! ERROR
    # =================================================================
    arange1(32767)  # * OK
    arange1(32768)  # ! no type checker message though, will lead to an error
