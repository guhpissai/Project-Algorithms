def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    estudantes = 0
    for hour in permanence_period:
        if not (isinstance(hour[0], int) and isinstance(hour[1], int)):
            return None
        time = list(range(hour[0], hour[1] + 1))
        if target_time in time:
            estudantes += 1
    return estudantes
    raise NotImplementedError
