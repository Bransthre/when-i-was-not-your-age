
#Now let's first input two managers' times, with lunch time added.
time_A = [['11:00', '12:30'], ['16:30', '17:00'], ['18:30', '19:00']]
time_B = [['9:00', '10:00']]

#Now we will try to simplify the time schedule of both managers
#That I mean simplify in terms of calculations.
#We are doing this by spliting strings of inputs into hours and mins.
def simplefreetime(sched):
    for i in range (0, len(sched)):
        for j in range (0, 2):
            hour, minute = sched[i][j].split(':')
            sched[i][j] = int(hour) * 60 + int(minute)

#Now that we have freetime for both manager, compare their schedules.
#Then we will get their mutual free time.
answer = []
def comparesched(sched_A, sched_B, sched_com):
    ptr_A = 0
    ptr_B = 0
    while ptr_A < len(sched_A) and ptr_B < len(sched_B):
        time_A_strt = sched_A[ptr_A][0]
        time_A_end = sched_A[ptr_A][1]
        time_B_strt = sched_B[ptr_B][0]
        time_B_end = sched_B[ptr_B][1]
        if time_A_end <= time_B_strt:
            ptr_A+=1
            continue
        if time_B_end <= time_A_strt:
            ptr_B+=1
            continue
        if time_A_end <= time_B_end:
            sched_com.append([max([time_A_strt,time_B_strt]), time_A_end])
        elif time_A_end > time_B_end:
            sched_com.append([max([time_A_strt,time_B_strt]), time_B_end])
        ptr_B+=1
    ptr = 0
    while True:
        if sched_com[ptr][0] == sched_com[ptr][1]:
            sched_com.remove(sched_com[ptr])
        ptr+=1
        if ptr>=len(sched_com):
            break

#Last but not least, let's simplify our schedule appearance.
def user_return(sched_com):
    for i in range (0, len(sched_com)):
        for j in range (0, 2):
            out_hr = sched_com[i][j] // 60
            out_min = sched_com[i][j] % 60
            if out_min == 0:
                out_min = '00'
            sched_com[i][j] = str(out_hr)+":"+str(out_min)

#Outputting...
simplefreetime(time_A)
simplefreetime(time_B)
comparesched(time_A, time_B, answer)
user_return(answer)
print(answer)
