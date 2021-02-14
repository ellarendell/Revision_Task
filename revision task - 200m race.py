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

min_time = float('inf') #represents infinity
#each finish time is compared
for time in times_list:
    #getting the largest time
    if time < min_time:
        min_time = time

#all of the race times together to calculate average
total_times = 0
for time in times_list:
    total_times += time

#calculating average race time
average_time = total_times / len(times_list)

#output
print("Average race time for 200m race: ",average_time)
print("Fastest race time for 200m race: ",min_time)
