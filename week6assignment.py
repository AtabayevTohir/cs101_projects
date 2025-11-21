def get_daily_temp_swing(weather_day_tuple) :
    swing = weather_day_tuple[1] - weather_day_tuple[2]
    return weather_day_tuple[0],swing

def find_day_with_largest_swing(weather_data):
    largest_swing = 0
    largest_swing_date = None
    for day in weather_data:
        date,swing = get_daily_temp_swing(day)
        if largest_swing < swing:
            largest_swing = swing
            largest_swing_date = date
    return largest_swing_date

def count_days_above_precip(weather_data, threshold):
    num_days = 0
    for day in weather_data:
        if threshold< day[3]:
            num_days += 1
    return num_days

def get_monthly_summary(weather_data):
    months = []        
    sum_max = []       
    total_precip = []  
    count_days = []    

    for day in weather_data:
        date = day[0]
        max_t = day[1]
        precip = day[3]
        month = date[:7]

        if month in months:
            i = months.index(month)
            sum_max[i] += max_t
            total_precip[i] += precip
            count_days[i] += 1
        else:
            months.append(month)
            sum_max.append(max_t)
            total_precip.append(precip)
            count_days.append(1)

    result = []
    for i in range(len(months)):
        avg_max = sum_max[i] / count_days[i]
        result.append((months[i], avg_max, total_precip[i]))
    result.sort()

    return result

def analyze_weather(weather_data):
    day_with_largestswing = find_day_with_largest_swing(weather_data)
    heavy_rain_days = count_days_above_precip(weather_data, 10.0)
    monthly_summary = get_monthly_summary(weather_data)

    return (day_with_largestswing, heavy_rain_days, monthly_summary)

weather_data = [
    ('2023-10-01', 22, 10, 5.5),
    ('2023-10-02', 25, 11, 0.0),
    ('2023-10-03', 24, 15, 12.0),
    ('2023-11-01', 18, 7, 2.5),
    ('2023-11-02', 15, 6, 15.5),
    ('2023-11-03', 16, 9, 8.0)
]

print (analyze_weather(weather_data))

