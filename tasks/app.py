from dataclasses import dataclass
from inspect import Signature, signature as sign


@dataclass
class InfoMessage:
    """
    Класс для вывода рассчитанных метрик.

    Параметры
    ----------
    calories : floaty
        Количество сжигаемых калорий за тренировку.

    duration : float
        Длительность тренировки.

    distance : float
        Преодалённое расстояние.

    speed : float
        Средняя скорость.

    training_type : string
        Тип тренировки.

    """

    calories: float
    duration: float
    distance: float
    speed: float
    training_type: str

    def __str__(self) -> str:
        return (
            f"Training: {self.training_type}, duration: {self.duration} hrs, distance: {self.distance} km, "
            f"avg speed: {self.speed} km/hr, kcal: {self.calories}"
        )


def signature(class_info) -> Signature:
    """Возвращает сигнатуру класса."""
    return sign(class_info)


@dataclass
class Training:
    """
    Шаблонный класс для реализации различных типов тренировок.

    Параметры
    ---------
    action: int
        Количество действий

    duration : float
        Длительность тренировки.

    weight : float
        Вес человека.

    training_type : string, default=None
        Тип тренировки.

    Свойства
    --------
    LEN_STEP: float, default=0.65
        Длина шага.

    M_IN_KM: int, default=1000
        Количество метров в километре.

    MIN_IN_HOUR: int, default=60
        Количество минут в часе.

    """

    action: int
    duration: float
    weight: float
    training_type: str = None
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def get_distance(self) -> float:
        """Рассчитывает расстояние преодалённое за тренировку"""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Рассчитывает среднюю скорость"""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Шаблонная функция рассчёта калорий"""
        assert NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """Возвращает информацию о результате тренировки"""
        return InfoMessage(
            self.get_spent_calories(),
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.training_type,
        )


class SportsWalking(Training):
    """
    Класс для рассчёта метрик спортивной ходьбы.

    Параметры
    ---------
    action : int
        Количество действий.

    duration : float
        Длительность тренировки.

    weight : float
        Вес человека.

    height : float
        Рост человека.

    Свойства
    --------
    training_type : string, default=Walking
        Тип тренировки.
    """

    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        self.training_type = "Walking"

    def get_spent_calories(self) -> float:
        """Расчёт затраченных калорий"""
        return (
            (0.035 + self.get_mean_speed() ** 2 // self.height * 0.029)
            * self.weight
            * self.duration
            * self.MIN_IN_HOUR
        )


class Running(Training):
    """
    Класс для рассчёта метрик бега.

    Параметры
    ---------
    action : int
        Количество действий.

    duration : float
        Длительность тренировки.

    weight : float
        Вес человека.

    Свойства
    --------
    training_type : string, default=Running
        Тип тренировки.
    """

    def __init__(self, action, duration, weight) -> None:
        super().__init__(action, duration, weight)
        self.training_type = "Running"

    def get_spent_calories(self) -> float:
        """Расчёт затраченных калорий"""
        return (18 * self.get_mean_speed() - 20) * self.weight / self.M_IN_KM * self.duration * self.MIN_IN_HOUR


class Swimming(Training):
    """
    Класс для рассчёта метрик бега.

    Параметры
    ---------
    action : int
        Количество действий.

    duration : float
        Длительность тренировки.

    weight : float
        Вес человека.

    length_pool : float
        Длина трека.

    count_pool : float
        Количество проплывов по длине трека.

    Свойства
    --------
    training_type : string, default=Swimming
        Тип тренировки.

    LEN_STEP: float, default=1.38
        Расстояние заплыва(шага).
    """

    LEN_STEP = 1.38

    def __init__(self, action, duration, weight, length_pool, count_pool) -> None:
        super().__init__(action, duration, weight)
        self.count_pool = count_pool
        self.length_pool = length_pool
        self.training_type = "Swimming"

    def get_mean_speed(self) -> float:
        """Рассчёт средней скорости плавания"""
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        """Расчёт затраченных калорий"""
        return (self.get_mean_speed() + 1.1) * 2 * self.weight


def read_package() -> dict:
    return {
        "SportsWalking": [9000, 1, 75, 180],
        "Running": [15000, 1, 75],
        "Swimming": [720, 1, 75, 25, 40],
    }


def main() -> None:
    data = read_package()
    for training_type in data.keys():
        print(globals()[training_type](*data[training_type]).show_training_info())


if __name__ == "__main__":
    main()
