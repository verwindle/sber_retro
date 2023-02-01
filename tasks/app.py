class Training():
    LEN_STEP = .65
    M_IN_KM = 1000
    MIN_IN_HOUR = 60

    def __init__(
        self,
        action,
        duration,
        weight,
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.training_type = None

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        assert(NotImplementedError)

    def show_training_info(self):
        return InfoMessage(self.get_spent_calories(), self.duration, self.get_distance(),
                           self.get_mean_speed(), self.training_type)


class Walking(Training):
    def __init__(self, action, duration, weight, height) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        self.training_type = 'Walking'

    def get_spent_calories(self) -> float:
        return ((.035 + self.get_mean_speed() ** 2 // self.height * .029)
                * self.weight * self.duration * self.MIN_IN_HOUR)


class Running(Training):
    def __init__(self, action, duration, weight) -> None:
        super().__init__(action, duration, weight)
        self.training_type = 'Running'

    def get_spent_calories(self) -> float:
        return (18 * self.get_mean_speed() - 20) * self.weight / self.M_IN_KM * self.duration * self.MIN_IN_HOUR


class Swimming(Training):
    LEN_STEP = 1.38

    def __init__(self, action, duration, weight, length_pool, count_pool) -> None:
        super().__init__(action, duration, weight)
        self.count_pool = count_pool
        self.length_pool = length_pool
        self.training_type = 'Swimming'

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + 1.1) * 2 * self.weight


class InfoMessage():
    def __init__(self, calories, duration, distance, speed, training_type) -> None:
        self.calories = calories
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.training_type = training_type

    def __str__(self):
        return (f'Training: {self.training_type}, duration: {self.duration} hrs, '
                f'distance: {self.distance} km, '
                f'avg speed: {self.speed} km/hr, kcal: {self.calories}')


def read_package():
    data = [
        ('Walking', [9000, 1, 75, 180]),
        ('Running', [15000, 1, 75]),
        ('Swimming', [720, 1, 75, 25, 40]),
    ]
    return dict(data)


def main():
    data = read_package()
    for training_type in data.keys():
        print(globals()[training_type](
            *data[training_type]).show_training_info())


if __name__ == '__main__':
    main()
