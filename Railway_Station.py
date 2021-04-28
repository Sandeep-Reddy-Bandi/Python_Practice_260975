import math  # importing the math library


def minimum_no_of_platforms_require(arrival_time, departure_time,
                                    no_of_trains):  # function which computes actual logic and return minimum noof platforms require to schedule those trains
    # platform_required indicates number of platforms needed at a time
    platform_required = 1
    final_answer = 1
    p = 1
    q = 0
    arrival_time.sort()  # sort the arrival_time list in ascending order
    departure_time.sort()  # sort the departure_time list in ascending order
    while (True):
        if p < no_of_trains and q < no_of_trains:
            if departure_time[q] >= arrival_time[
                p]:  # if  the next event in sorted order is arrival, increment count of platforms needed if departure_time[q] greater than arrival_time[p]
                platform_required += 1
                p += 1
                if (
                        platform_required > final_answer):  # change the  result if needed if (platform_required > final_answer)
                    final_answer = platform_required
            else:  # else decrement count of platform_required
                platform_required -= 1
                q += 1
        else:
            break

    return final_answer  # finally reture the final_answer(minimum no of platforms required to shedule those trains)


no_of_trains = int(input())  # Reading no_of_trains
arrival_time = []  # creating the list of arrival time of trains
departure_time = []  # creating the list of departure time of trains
for each_train in range(0, no_of_trains):  # reading each train arrival time and stoppage time
    arrival, stoppage = map(int, input().split())
    arrival_time.append(arrival)
    departure_time.append(arrival + stoppage)

print(minimum_no_of_platforms_require(arrival_time, departure_time, no_of_trains), end="")






