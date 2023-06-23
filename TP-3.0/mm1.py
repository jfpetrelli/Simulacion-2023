from random import uniform
from math import log

def expon(mean):
    u = uniform(0.0, 1.0)
    expon_number = -mean * log(u)
    return expon_number


queue_limit = 100;
busy = 1;
idle = 0;
num_events = 2;

#mean interarrival time
mean_interarrival = 1 ;

#mean service time
mean_service = 0.75;

#number of customers
num_delays_required = 1000;

next_event_type = 0;
time_next_event = [0, 0, 0];

x = 0
time_arrival = [];
while (x < queue_limit):
    time_arrival.append(0);
    x = x+1

time = 0.0;
server_status = idle;
num_in_q = 0;
time_last_event = 0.0;
num_custs_delayed = 0;
total_of_delays = 0.0;
area_num_in_q = 0.0;
area_server_status = 0.0;
time_next_event[1] = time + expon(mean_interarrival)
time_next_event[2] = 1000000000000000000000000000000.0;


def main():
    global num_custs_delayed, num_delays_required, time, next_event_type, total_of_delays, area_num_in_q, area_server_status

    while num_custs_delayed < num_delays_required:
        maybe_time = timing()
        if (maybe_time == -9999999999999999999999999999999) :
            return
        time = maybe_time

        update_time_avg_stats()

        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()
    report()


def timing():
    global num_events, time_next_event, next_event_type
    i = 1
    min_time_next_event = 100000000000000000000000000000.0
    next_event_type = 0

    for i in range(1, num_events+1):
        if time_next_event[i] < min_time_next_event :
            min_time_next_event = time_next_event[i]
            next_event_type = i

    if next_event_type == 0:
        return -9999999999999999999999999999999
    return min_time_next_event;


def update_time_avg_stats():
    global time_last_event, area_num_in_q, area_server_status, time, num_in_q
    time_since_last_event = 0.0
    time_since_last_event = time - time_last_event
    time_last_event = time;
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event


def arrive():
    global server_status, time_next_event, time, mean_interarrival, server_status, busy, num_in_q, queue_limit, time_arrival, total_of_delays, num_custs_delayed, mean_service
    delay = 0.0
    time_next_event[1] = time + expon(mean_interarrival)
    if (server_status == busy):
        num_in_q = num_in_q + 1
        if (num_in_q > queue_limit):
            print('Overflow of the array time_arrival at')
            print('Time: ', time)
            return
        time_arrival[num_in_q] = time
    else:
        delay = 0.0
        total_of_delays += delay

        num_custs_delayed = num_custs_delayed + 1
        server_status = busy

        time_next_event[2] = time + expon(mean_service)


def depart():
    global time_arrival, num_in_q, server_status, time_next_event, total_of_delays, num_custs_delayed, time, time_arrival, mean_service
    i = 1
    delay = 0.0

    if(num_in_q == 0):
        server_status = idle
        time_next_event[2] = 1000000000000000000000000000000.0
    else:
        num_in_q = num_in_q - 1
        delay = time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed = num_custs_delayed + 1
        time_next_event[2] = time + expon(mean_service)

    for i in range(1, num_in_q+1) :
        time_arrival[i] = time_arrival[i+1]


def report():
    global total_of_delays, num_custs_delayed, area_num_in_q, area_server_status, time
    print()
    print()
    if num_custs_delayed == 0:
        print('Average delay in queue in minutes: 0')
    else:
        print('Average delay in queue in minutes: ', total_of_delays / num_custs_delayed)
    print()
    print()
    if time == 0 or time == 0.0:
        print('Average number in queue: 0')
        print()
        print()
        print('Server utilization: 0')
    else:
        print('Average number in queue: ', area_num_in_q / time)
        print()
        print()
        print('Server utilization: ', area_server_status / time)
    print()
    print()
    print('Time simulation ended: ', time)
    print('-------------------------------------------------')


if __name__ == "__main__":
    main()