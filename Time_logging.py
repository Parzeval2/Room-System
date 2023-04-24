from datetime import datetime
from time import sleep

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
time_list = current_time.split(":")
time_list_int = [int(i) for i in time_list]


now2 = datetime.now()
current_time2 = now2.strftime("%H:%M:%S")
time_list2 = current_time2.split(":")
time_list_int2 = [int(i) for i in time_list2]


def difference_in_time(time1, time2):
    """takes time represented as a list of 3 intergers [h, m, s] and returns time1 - time2"""
    time1_s = (time1[0] * 3600) + (time1[1] * 60) + time1[2]
    time2_s = (time2[0] * 3600) + (time2[1] * 60) + time2[2]
    timediff_s = time1_s - time2_s
    timediff = [int(((timediff_s - (timediff_s%3600)) / 3600)),
                 int(((((timediff_s%3600) - (timediff_s%3600)%60)) / 60)),
                   int((((timediff_s%3600)%60)))]
    return timediff

print(difference_in_time([13, 1, 1],[12, 25, 25]))

