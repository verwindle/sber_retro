from enum import Enum
from typing import List, Optional, Tuple, Union


class InfoMessage:
    def __init__(self, training_type: Optional[str], duration: float, distance: float, speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def __str__(self) -> str:
        return (f'Trainig: {self.training_type}, duration: {self.duration} hrs, distance: {self.distance} '\
            f'km, average speed: {self.speed} km/hr, kcal: {self.calories}')


class Training:
    LEN_STEP: float = .65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def __init__(self, action: int, duration: float, weight: float) -> None:
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
    __walking_coef_a: float = .035
    __walking_coef_b: float = .029

    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        
        self.training_type = 'Walking'
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.__walking_coef_a * self.weight + (self.get_mean_speed() ** 2 // self.height) *\
            self.__walking_coef_b * self.weight) * self.duration * self.MIN_IN_HOUR)
            

class Running(Training):
    __running_coef_a: int = 18
    __running_coef_b: int = 20

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        
        self.training_type = 'Running'

    def get_spent_calories(self) -> float:
        return (self.__running_coef_a * self.get_mean_speed() - self.__running_coef_b) * self.weight /\
            self.M_IN_KM * self.duration * self.MIN_IN_HOUR


class Swimming(Training):
    LEN_STEP: float = 1.38

    __swimming_coef_a: float = 1.1
    __swimming_coef_b: int = 2

    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: int) -> None:
        super().__init__(action, duration, weight)

        self.training_type = 'Swimming'
        self.length_pool = length_pool
        self.count_pool = count_pool
    
    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + self.__swimming_coef_a) * self.__swimming_coef_b * self.weight


class Trainings(Enum):
    Walking = SportsWalking
    Running = Running
    Swimming = Swimming

# возможно это лишнее
Data = List[Union[int, float]]


def read_package() -> List[Tuple[str, Data]]:
    return [
        ('Walking', [9000, 1, 75, 180]),
        ('Running', [15000, 1, 75]),
        ('Swimming', [720, 1, 75, 25, 40]),
    ]

def main() -> None:
    data = read_package()

    for training_type, attrs in data:
        print(Trainings[training_type].value(*attrs).get_training_info())


if __name__ == '__main__':
    main()