#Ella Rendell
#14.02.21
#Revision Tasks
#200 Metre Race


times_list = [] #used to make calculations for average and max times
#while True loop so the -1 is not accounted for in the times_list
while True:
    finish_time = float(input("What is the finsihing time of the 200m race (in secs): "))
    if finish_time != -1:
        times_list.append(finish_time)
    elif finish_time == -1:
        break

max_time = 0
#each finish time is compared
for time in times_list:
    #getting the largest time
    if time > max_time:
        max_time = time
print(max_time,"max time")

#all of the race times together to calculate average
total_times = 0
for time in times_list:
    total_times += time
print(total_times,"total time")
