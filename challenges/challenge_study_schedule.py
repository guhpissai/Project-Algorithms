permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

def study_schedule(permanence_period, target_time):
    if target_time == None:
        return None
    if not isinstance(permanence_period, list):
        return None
    contador = 0
    for hour in permanence_period:
        if not (isinstance(hour[0], int) and isinstance(hour[1], int)):
            return None
        if hour[0] == None or hour[1] == None:
            return None
        if hour[0] == hour[1]:
            time = [hour[0], hour[1]]
        else:
            time = list(range(hour[0], hour[1] + 1))
        if target_time in time:
            contador += 1
    return contador
    raise NotImplementedError

print(study_schedule(permanence_period, 2))
