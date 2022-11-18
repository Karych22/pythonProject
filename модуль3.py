#if x > 0 and y > 0:
#    print("Первая четверть")
#if x > 0 and y < 0:
#    print("Четвертая четверть")
#if y < 0 and x > 0:
#    print("Вторая четверть")
#if x < 0 and y < 0:
#    print("Третья четверть")

def get_wind_class(speed):
    if 1 <= speed <= 4:
        return "weak [1]"
    if 5 <= speed <= 10:
        return "moderate [2]"
    if 11 <= speed <= 18:
        return "strong [3]"
    if speed >= 19:
        return "hurricane [4]"
print(get_wind_class(int(input())))