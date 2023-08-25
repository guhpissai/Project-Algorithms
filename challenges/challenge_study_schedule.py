def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    estudantes = 0
    for hour in permanence_period:
        if not (isinstance(hour[0], int) and isinstance(hour[1], int)):
            return None
        if hour[0] <= target_time <= hour[1]:
            estudantes += 1
    return estudantes
