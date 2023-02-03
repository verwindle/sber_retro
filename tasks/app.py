from dataclasses import dataclass, asdict

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enum import Enum
    from typing import (
        List, 
        Optional, 
        Tuple, 
        Union,
        NoReturn
    )


@dataclass
class InfoMessage:
    """"""
    training_type: Optional[str]
    duration: float
    distance: float
    speed: float
    calories: float

    def __post_init__(self) -> NoReturn:
        self.info_message = 'Training: {training_type}, duration: {duration:.2f} hrs, distance: {distance:.2f} ' + (
            'km, average speed: {speed:.2f} km/hr, kcal: {calories:.2f}')

    def __str__(self) -> str:
        return self.info_message.format(**asdict(self))

class Training:
    """"""
    LEN_STEP: float = .65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def __init__(self, action: int, duration: float, weight: float) -> NoReturn:
        self.training_type: Optional[str] = None
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(self.training_type, self.duration, self.get_distance(), self.get_mean_speed(), 
            self.get_spent_calories())


class SportsWalking(Training):
    WALKING_COEF_A: float = .035
    WALKING_COEF_B: float = .029

    def __init__(self, action: int, duration: float, weight: float, height: float) -> NoReturn:
        super().__init__(action, duration, weight)
        
        self.training_type = 'Walking'
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.WALKING_COEF_A * self.weight + (self.get_mean_speed() ** 2 // self.height) * (
            self.WALKING_COEF_B * self.weight) * self.duration * self.MIN_IN_HOUR))
            

class Running(Training):
    RUNNING_COEF_A: int = 18
    RUNNING_COEF_B: int = 20

    def __init__(self, action: int, duration: float, weight: float) -> NoReturn:
        super().__init__(action, duration, weight)
        
        self.training_type = 'Running'

    def get_spent_calories(self) -> float:
        return (self.RUNNING_COEF_A * self.get_mean_speed() - self.RUNNING_COEF_B) * self.weight / (
            self.M_IN_KM * self.duration * self.MIN_IN_HOUR)


class Swimming(Training):
    LEN_STEP: float = 1.38

    SWIMMING_COEF_A: float = 1.1
    SWIMMING_COEF_B: int = 2

    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: int) -> NoReturn:
        super().__init__(action, duration, weight)

        self.training_type = 'Swimming'
        self.length_pool = length_pool
        self.count_pool = count_pool
    
    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + self.SWIMMING_COEF_A) * self.SWIMMING_COEF_B * self.weight


class Trainings(Enum):
    Walking = SportsWalking
    Running = Running
    Swimming = Swimming

def read_package(package: Tuple[str, List[float]]) -> Training:
    """some processing"""
    training_type, attrs = package

    return Trainings[training_type].value(*attrs)

def main(training: Training) -> None:
    print(training.show_training_info())

if __name__ == '__main__':
    packages = [
        ('Walking', [9000, 1, 75, 180]),
        ('Running', [15000, 1, 75]),
        ('Swimming', [720, 1, 75, 25, 40]),
    ]
    
    for pack in packages:
        main(read_package(pack))