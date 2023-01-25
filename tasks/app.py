def do_sth_cool(tr_type, action, dur, weight, height=None, length_pool=None, n_times_pool_passed=None):
    if tr_type == 'Walking':
        dist = action * .65 / 1000  # действие * на длину шага в м / метров в км
        av_sp = dist / dur  # средняя скорость
        # формула (а * вес + ср скорость ** 2 // рост * b * вес) * длительность * минут в час
        clr = ((.035 * weight + (
                av_sp ** 2 // height
        ) * .029 * weight) * dur * 60)
        return (f'Training: {tr_type}, duration: {dur} hrs, distance: {dist} km,'
                f'avg speed: {av_sp} km/hr, kcal: {clr}')
    if tr_type == 'Running':
        dist = action * .65 / 1000
        av_sp = dist / dur
        # формула (а * ср скорость - b) * вес / метров в км * длительность * минут в час
        clr = (18 * av_sp - 20) * weight / 1000 * dur * 60
        return (f'Training: {tr_type}, duration: {dur} hrs, distance: {dist} km,'
                f'avg speed: {av_sp} km/hr, kcal: {clr}')
    if tr_type == 'Swimming':
        dist = action * 1.38 / 1000
        # формула длина дорожки * кол-во раз прохода дорожки / метров в км / длительность
        av_sp = length_pool * n_times_pool_passed / 1000 / dur
        # формула (ср скорость + а) * b * вес
        clr = (av_sp + 1.1) * 2 * weight
        return (f'Training: {tr_type}, duration: {dur} hrs, distance: {dist} km,'
                f'avg speed: {av_sp} km/hr, kcal: {clr}')


def main(*training_driver_data):
    training_info = do_sth_cool(*training_driver_data)
    print(training_info)


if __name__ == '__main__':
    # Изменять переменную нельзя, в таком виде получаем с датчиков
    data_from_drivers = [
        ('Walking', [9000, 1, 75, 180]),
        ('Running', [15000, 1, 75]),
        ('Swimming', [720, 1, 75, 25, 40]),
    ]
    for d in data_from_drivers:
        tr_type = d[0]
        if tr_type == 'Walking':
            action, duration, weight, height = d[1]
            main(tr_type, action, duration, weight, height, None, None)
        elif tr_type == 'Running':
            action, duration, weight = d[1]
            main(tr_type, action, duration, weight, None, None, None)
        elif tr_type == 'Swimming':
            action, duration, weight, length_pool, n_times_pool_passed = d[1]
            main(tr_type, action, duration, weight, None, length_pool, n_times_pool_passed)
