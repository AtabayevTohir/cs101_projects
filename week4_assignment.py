def calculate_kilojoules_used(workout_type, duration_minutes, intensity):
    if workout_type == "aerobic":
        if intensity == "low":
            kj_min = 35
        elif intensity == "medium":
            kj_min = 50
        elif intensity == "high":
            kj_min = 65
    elif workout_type == "resistance":
        if intensity == "low":
            kj_min = 25
        elif intensity == "medium":
            kj_min = 38
        elif intensity == "high":
            kj_min = 50
    elif workout_type == "yoga":
        if intensity == "low":
            kj_min = 12
        elif intensity == "medium":
            kj_min = 20
        elif intensity == "high":
            kj_min = 28
    return kj_min * duration_minutes

def calculate_exertion_level(age, rest_pulse, active_pulse):
    max_hr = 220 -age
    hr_reserve = max_hr - rest_pulse
    intensity_percent = (active_pulse - rest_pulse) / hr_reserve * 100
    return intensity_percent

def determine_activity_zone(intensity_percent):
    if intensity_percent < 50:
        return "Light Activity"
    elif intensity_percent < 60:
        return "Moderate Activity"
    elif intensity_percent < 70:
        return "Vigorous Activity"
    elif intensity_percent < 85:
        return "Hard Activity"
    else:
        return "Maximum Activity"
    
def calculate_fitness_rating(kilojoules, duration, zone_factor):
    base_rating = kilojoules * 0.024 + duration * 2
    if zone_factor == "Light Activity":
        factor = 0.5
    elif zone_factor == "Moderate Activity":
        factor = 1.0
    elif zone_factor == "Vigorous Activity":
        factor = 1.2
    elif zone_factor == "Hard Activity":
        factor = 1.5
    elif zone_factor == "Maximum Activity":
        factor = 1.8
    final_rating = factor * base_rating
    return round(final_rating, 1)

def should_take_break(active_days, total_minutes, avg_intensity):
    if active_days >= 6:
        return True
    elif total_minutes > 450 and avg_intensity > 70:
        return True
    elif active_days >= 4 and avg_intensity > 80:
        return True
    else:
        return False

def generate_activity_analysis(participant, workout_type, duration, intensity, age, rest_pulse, active_pulse, active_days):
    kilojoules = calculate_kilojoules_used(workout_type, duration, intensity)
    intensity_percent = calculate_exertion_level(age, rest_pulse, active_pulse)
    zone = determine_activity_zone(intensity_percent)
    fitness_rating = calculate_fitness_rating(kilojoules, duration, zone)
    take_break = should_take_break(active_days, duration, intensity_percent)
    print('========================================')
    print(f'Activity Analysis for: {participant}')
    print('----------------------------------------')
    print(f'Workout Type: {workout_type}')
    print(f'Duration: {duration} minutes')
    print(f'Intensity Level: {intensity}')
    print(f'\nKilojoules Used: {kilojoules}')
    print('Exertion Analysis:')
    print(f'  Age: {age}, Rest Pulse: {rest_pulse}, Active Pulse: {active_pulse}')
    print(f'  Intensity: {intensity_percent: .1f}%')
    print(f'  Activity Zone: {zone}')
    print(f'Fitness Rating: {fitness_rating}')
    print(f'Consecutive Active Days: {active_days}')
    print(f'Break Day Needed: {"Yes" if take_break else "No"}')
    print()

print('EXERCISE PROGRAM MONITOR')
generate_activity_analysis("Robin", "aerobic", 45, "high", 28, 65, 155, 3)
generate_activity_analysis("Jamie", "resistance", 60, "medium", 35, 70, 140, 5)
generate_activity_analysis("Avery", "yoga", 30, "low", 42, 68, 95, 7)