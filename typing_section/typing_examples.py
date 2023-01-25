"""
- PEP is here https://peps.python.org/pep-0484/
- Google slides https://docs.google.com/presentation/d/1R2IzE-1I1otv1PXbXyR-JvOkBxdRAVDpXpFVmELRatA/edit#slide=id.p
- Nice and comprehensive book, with video on youtube (https://www.youtube.com/channel/UC9MK8SybZcrHR3CUV4NMy2g):
    Типизированный Python (Алексей Голобурдин)
- numpy typing https://numpy.org/devdocs/reference/typing.html
- Future note (not included): try pandera https://pypi.org/project/pandera for pandas
"""
import enum
import re
import typing

import typing_extensions
import numpy.typing as npt

import numpy as np
import pandas as pd  # * ignore error

# * LEVEL ELEMENTARY *


def print_list(a: list) -> None:
    print(a)


# =================================================================


def greeting(name: str) -> str:
    return "Hello" + name


# =================================================================


# * LEVEL BEGINNER *


def feeder(get_next_item: typing.Callable) -> None:
    ...


# =================================================================
class Employee:
    ...


class Boss:
    ...


def handle_employee_or_boss(e: typing.Union[Employee, Boss]) -> None:
    ...


def handle_employee_or_forget(e: typing.Optional[Employee]) -> None:
    ...


# =================================================================
def collect_py_files(parent_path="sberpm"):  # ! ERROR no types
    return ("_holder.py", "setup.py")


# =================================================================


class MandatoryColumns(typing.NamedTuple):
    id_name: str
    activity_name: str
    timestamp_columns: typing.Iterable[str]


# =================================================================
class Coordinates(typing.TypedDict):
    longitude: float
    latitude: float


# =================================================================

# * LEVEL INTERMEDIATE *


def what_am_i_live_for(data: typing.Any) -> None:
    data.gg += data.momo

    return float(data)  # ! ERROR


async def async_query(
    on_success: typing.Callable[[int], None],
    on_error: typing.Callable[[int, Exception], None],
) -> None:
    ...


# =================================================================
def echo_round() -> typing.Generator[int, float, str]:
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
ContactDict = typing.Dict[str, str]


def check_if_valid(contacts: ContactDict) -> bool:
    for name, email in contacts.items():
        # Check if name and email are strings
        if (not isinstance(name, str)) or (not isinstance(email, str)):
            return False
        # Check for email xxx@yyy.zzz
        if not re.match(r"[a-zA-Z0-9\._\+-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$", email):
            return False
    return True


# =================================================================


class DataHolder(typing_extensions.Protocol):  # available in typing since 3.8, see typing_extensions for 3.7
    """Represent interface that will be used further, without everything else real DataHolder has"""

    @property
    def data(self) -> pd.DataFrame:
        """SOME DESCRIPTION"""

    @property
    def activity_column(self) -> str:
        """SOME DESCRIPTION"""

    def check_or_calc_duration(self) -> None:
        """SOME DESCRIPTION"""


class Miner_number_44:
    def __init__(self, data_holder: DataHolder) -> None:  # * NO import or inheritance needed
        self.data_holder = data_holder

    def apply(self) -> None:
        self.data_holder.check_or_calc_duration()

        return self.data_holder.data.groupby(
            self.data_holder.activity_column,
        )


# =================================================================


class ActivityComputedMetrics(str, enum.Enum):
    MEAN_TIME = enum.auto()
    DIFF_TIME = enum.auto()
    FREQUENCY = enum.auto()
    CYCLES = enum.auto()
    ANOMALY_LEVEL = enum.auto()

    def __int__(self) -> int:
        return self.value


# =================================================================


def arange_doubles(length: int) -> npt.NDArray[np.float64]:
    return np.arange(length, dtype=np.float64)


def arange_booleans(length: int) -> npt.NDArray[np.bool_]:
    return np.arange(length, dtype=bool)


# * LEVEL ADVANCED *

AnyStr = typing.TypeVar("AnyStr", typing.Text, bytes)  # * Simple TypeVars for Unions (constraints)


def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y


# =================================================================


class User:
    ...


UserType = typing.TypeVar("UserType", bound=User)


def new_user(user_class: typing.Type[UserType]) -> UserType:  # type: ignore [empty-body]
    """Takes User class type, returns instance of User class type"""


# =================================================================

body_type = typing.TypeVar("body_type")


class GenericWebRequestHandler(typing.Generic[body_type]):  # * User Defined Generic Types
    accepted_http_methods: typing.Tuple[str, ...]  # * str and maybe something else
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
    accepted_http_methods: typing.Tuple[str, ...] = ("POST",)


# =================================================================


def apply_operation_to(
    *args: typing_extensions.Unpack[typing.Union[pd.DataFrame, pd.Series]]
) -> None:  # "Unpack" support is experimental
    for _ in args:
        print(_.shape)
