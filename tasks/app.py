import sys


class InfoMessage:
    def __init__(
        self, training_type: str, duration: float, distance: float, speed: float, calories: float
    ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def __str__(self) -> str:
        return (
            f"Training: {self.training_type}, "
            f"duration: {self.duration} hrs, "
            f"distance: {self.duration} km, "
            f"avg speed: {self.speed} km/hr, "
            f"kcal: {self.calories}"
        )


class Training:
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self, action: float, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def __str__(self) -> str:
        return self.__class__.__name__

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        assert NotImplementedError

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(
            self.__class__.__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


class Swimming(Training):
    LEN_STEP = 1.38

    def __init__(self, action: float, duration: float, weight: float, length_pool: float, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self):
        return super().get_distance()

    def get_mean_speed(self):
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self):
        const_a = 1.1  # TODO https://www.youtube.com/watch?v=EXI4TC0xpKw
        const_b = 2  # TODO https://www.youtube.com/watch?v=EXI4TC0xpKw
        return (self.get_mean_speed() + const_a) * const_b * self.weight


class SportsWalking(Training):
    def __init__(self, action: float, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)

        self.height = height

    def get_spent_calories(self):
        min_in_hour = 60
        const_c = 0.035  # TODO https://www.youtube.com/watch?v=EXI4TC0xpKw
        const_d = 0.029  # TODO https://www.youtube.com/watch?v=EXI4TC0xpKw
        return (
            (const_c * self.weight + (self.get_mean_speed() ** 2 // self.height) * const_d * self.weight)
            * self.duration
            * min_in_hour
        )


class Running(Training):
    def get_spent_calories(self):
        min_in_hour = 60
        const_e = 18  # TODO https://www.youtube.com/watch?v=EXI4TC0xpKw
        const_f = 20  # TODO https://www.youtube.com/watch?v=EXI4TC0xpKw
        return (
            (const_e * self.get_mean_speed() - const_f) * self.weight / self.M_IN_KM * self.duration * min_in_hour
        )


def read_package():
    # magic
    data_from_drivers = [
        ("SportsWalking", [9000, 1, 75, 180]),
        ("Running", [15000, 1, 75]),
        ("Swimming", [720, 1, 75, 25, 40]),
    ]
    return data_from_drivers


def main():
    for training_type, data in read_package():
        class_str = training_type
        args_str = str(data)[1:-1]
        calc_class = eval(f"{class_str}({args_str})")  # equal `calc_class = class(args)`
        print(calc_class.show_training_info())


if __name__ == "__main__":
    main()
