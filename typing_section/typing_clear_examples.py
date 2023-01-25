"""
- PEP is here https://peps.python.org/pep-0484/
- Google slides https://docs.google.com/presentation/d/1R2IzE-1I1otv1PXbXyR-JvOkBxdRAVDpXpFVmELRatA/edit#slide=id.p
- Nice and comprehensive book, with video on youtube (https://www.youtube.com/channel/UC9MK8SybZcrHR3CUV4NMy2g):
    Типизированный Python (Алексей Голобурдин)
- numpy typing https://numpy.org/devdocs/reference/typing.html 
- Future note (not included): try pandera https://pypi.org/project/pandera for pandas
"""

from __future__ import annotations  # * with this python reads all types as strings at runtime

from re import match
from enum import Enum, auto

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # * type checking is false at runtime, but you have provide annotations
    from typing import (
        Any,
        Callable,
        Dict,  # * for aliases assignment only
        Generator,
        Generic,
        Iterable,
        List,  # * for assignment aliases only
        Mapping,
        NamedTuple,
        # Protocol,  # * available since 3.8, see typing_extensions for 3.7
        Sequence,
        Text,
        Type,
        TypedDict,
        TypeVar,
    )

    from numpy import ndarray, bool_, int16
    from numpy.typing import ArrayLike, NDArray
    from typing_extensions import Protocol, Unpack

from numpy import arange, array, float64, int32, int64
from pandas import DataFrame, Series

# * LEVEL ELEMENTARY *


def print_list(a: list) -> None:
    print(a)


# =================================================================


def greeting(name: str) -> str:
    return f"Hello{name}"


# * LEVEL BEGINNER *


def feeder(get_next_item: Callable) -> None:
    ...


# =================================================================
class Employee:
    ...


class Boss:
    ...


def handle_employee_or_boss(e: Employee | Boss) -> None:
    ...


def handle_employee_or_forget(e: Employee | None) -> None:
    ...


# =================================================================


def collect_py_files(parent_path="sberpm"):  # ! ERROR no types
    return ("_holder.py", "setup.py")


# =================================================================


class MandatoryColumns(NamedTuple):
    id_name: str
    activity_name: str
    timestamp_columns: Iterable[str]


# =================================================================
class Coordinates(TypedDict):
    longitude: float
    latitude: float


# * LEVEL INTERMEDIATE *


def what_am_i_live_for(data: Any) -> None:
    data.gg += data.momo

    return float(data)  # ! ERROR: no return value expected


async def async_query(
    on_success: Callable[[int], None],
    on_error: Callable[[int, Exception], None],
) -> None:
    ...


# =================================================================
def echo_round() -> Generator[int, float, str]:
    res = yield 0  # * just entry point

    while res:
        res = yield round(res)

    return "OK"


gen = echo_round()
taken = gen.send(3.1)
# =================================================================

Url = str  # * Aliases are simple variable assignments


def retry(url: Url, retry_count: int) -> None:
    ...


# =================================================================


# an alias called 'ContactDict'
ContactDict = Dict[str, str]


def check_if_valid(contacts: ContactDict) -> bool:
    for name, email in contacts.items():
        # Check if name and email are strings
        if (not isinstance(name, str)) or (not isinstance(email, str)):
            return False
        # Check for email xxx@yyy.zzz
        if not match(r"[a-zA-Z0-9\._\+-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$", email):
            return False
    return True


# =================================================================


class DataHolder(Protocol):
    """Represent interface that will be used further, without everything else real DataHolder has"""

    @property
    def data(self) -> DataFrame:
        """data frame content"""

    @property
    def activity_column(self) -> str:
        """column name for activities of data processes"""

    def check_or_calc_duration(self) -> None:
        """calculate duration for every data record or check if duration has been calculated"""


class Miner_number_44:
    def __init__(self, data_holder: DataHolder) -> None:  # * NO import or inheritance needed
        self.data_holder = data_holder

    def apply(self) -> None:
        self.data_holder.check_or_calc_duration()

        return self.data_holder.data.groupby(
            self.data_holder.activity_column,
        )


# =================================================================


class ActivityComputedMetrics(str, Enum):
    MEAN_TIME = auto()
    DIFF_TIME = auto()
    FREQUENCY = auto()
    CYCLES = auto()
    ANOMALY_LEVEL = auto()

    def __int__(self) -> int:
        return self.value


# =================================================================


def arange_doubles(length: int) -> NDArray[float64]:
    return arange(length, dtype=float64)


def arange_booleans(length: int) -> NDArray[bool_]:
    return arange(length, dtype=bool)


# * LEVEL ADVANCED *

AnyStr = TypeVar("AnyStr", Text, bytes)  # * Simple TypeVars for Unions (constraints)


def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y


# =================================================================


class User:
    ...


UserType = TypeVar("UserType", bound=User)


def new_user(user_class: Type[UserType]) -> UserType:  # type: ignore [empty-body]
    """Takes User class type, returns instance of User class type"""


# =================================================================

body_type = TypeVar("body_type")


class GenericWebRequestHandler(Generic[body_type]):  # * User Defined Generic Type
    accepted_http_methods: tuple[str, ...]  # * str and maybe something else
    path: str
    body: body_type

    def _init__(
        self,
        path: str,
        body: body_type,
    ) -> None:
        self.path = path
        self.body = body

    async def handle(self) -> None:
        ...


class PostWebRequestHandler(GenericWebRequestHandler[str]):
    accepted_http_methods: tuple[str, ...] = ("POST",)


# =================================================================


def apply_operation_to(
    *args: Unpack[DataFrame | Series],  # type: ignore [misc]
) -> None:  # * It's sad but OK - "Unpack" support is experimental
    for _ in args:
        print(_.shape)


# *****************************************************************
# *****************************************************************
# *****************************************************************

if __name__ == "__main__":
    print_list([1, 2, 3])  # * OK
    print_list(1)  # ! ERROR Argument 1 to "print_list" has incompatible type "int"; expected "List[Any]"
    # =================================================================
    greeting("Pepe")  # * OK
    greeting(
        {"name": "bunny"}
    )  # ! ERROR  Argument 1 to "greeting" has incompatible type "Dict[str, str]"; expected "str"
    # =================================================================
    handle_employee_or_boss(Boss())  # * OK
    handle_employee_or_boss(Employee())  # * OK
    handle_employee_or_boss(
        lambda x: "boss"
    )  # ! ERROR Argument 1 to "handle_employee_or_boss" has incompatible type "Callable[[Any], str]"; expected "Union[Employee, Boss]"

    handle_employee_or_forget(None)  # * OK
    # =================================================================
    print(check_if_valid({"vijay": "vijay@sample.com"}))  # * OK
    print(
        check_if_valid({"vijay": "vijay@sample.com", 123: "wrong@name.com"})
    )  # ! ERROR Dict entry 1 has incompatible type "int": "str"; expected "str": "str"
    # =================================================================
    mandatory_columns = MandatoryColumns("id", "stages", ["time_start"])

    mandatory_columns.activity_name.upper()  # * OK
    mandatory_columns.activity_name**0.5  # ! ERROR No overload variant of "__rpow__" of "float" matches argument type "str"

    for column in mandatory_columns:  # * OK
        print(f"Got {column}")  # * OK
        column.props  # ! ERROR "Iterable[str]" has no attribute "props"
    # =================================================================
    c = Coordinates(longitude=10, latitude=20)

    c["longitude"]  # * OK
    c["longitudeRRR"]  # ! ERROR TypedDict "Coordinates" has no key "longitudeRRR"
    # =================================================================
    DataHolder.data  # * OK
    DataHolder.ne_data  # ! ERROR "Type[DataHolder]" has no attribute "ne_data"

    def operate_data_holder(data_holder: DataHolder):
        data_holder.check_or_calc_duration()  # * OK
        data_holder.calc_duration  # ! ERROR "DataHolder" has no attribute "calc_duration"

    # =================================================================
    print(ActivityComputedMetrics.ANOMALY_LEVEL)  # * OK
    print(
        ActivityComputedMetrics.MISSING_PART
    )  # ! ERROR "Type[ActivityComputedMetrics]" has no attribute "MISSING_PART"
    # =================================================================
    arange_doubles(33).size  # * OK
    arange_doubles(
        400.31
    ).size  # ! ERROR Argument 1 to "arange_doubles" has incompatible type "float"; expected "int"
    arange_doubles(
        400.31  # ! ERROR Argument 1 to "arange_doubles" has incompatible type "float"; expected "int"
    ).to_frame()  # ! ERROR "ndarray[Any, dtype[floating[_64Bit]]]" has no attribute "to_frame"
