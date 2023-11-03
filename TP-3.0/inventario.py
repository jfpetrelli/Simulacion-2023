from random import uniform, randint
from math import log


smalls_list = [10, 20, 30, 40, 50, 60]  
bigs_list = [30, 40, 50, 60, 70, 80]  

def main():
    global num_events, next_event_type, smalls, bigs, smalls_list, bigs_list, time

    num_policies = len(smalls_list)  

    num_events = 4

    print("Policy  ---- Average Total Cost ---- Average ordering cost ---- Average holding cost ---- Average shortage cost ")

    for i in range(0, num_policies):
        smalls = smalls_list[i]
        bigs = bigs_list[i]
        initialize()
        maybe_timing = timing()
        while (next_event_type != 3):
            maybe_timing = timing()
            if maybe_timing == -9999999999999999999999999999999:
                break
            else:
                time = maybe_timing
            update_time_avg_stats()
            if next_event_type == 1:
                order_arrival()
            elif next_event_type == 2:
                demand()
            elif next_event_type == 4:
                evaluate()
        report()

#int
amount = 0
bigs = 0
initial_inv_level = 60
inv_level = 0
next_event_type = 0
num_events = 0
num_months = 120
num_values_demand = 4
smalls = 0

#float
area_holding = 0.0
area_shortage = 0.0
holding_cost = 1.0
incremental_cost = 3.0
maxlag = 1.0
mean_interdemand = 0.10
minlag = 0.5
setup_cost = 32.0
shortage_cost = 5.0
time = 0.0
time_last_event = 0.0
total_ordering_cost = 0.0

prob_distrib_demand = [0.0, 0.167, 0.500, 0.833, 1000];

y = 0
time_next_event = [];
while (y < 5):
    time_next_event.append(0.0);
    y = y+1
        

def initialize():
    global time, inv_level, initial_inv_level, time_last_event, total_ordering_cost, area_holding, area_shortage, time_next_event, mean_interdemand, num_months

    time = 0.0

    inv_level = initial_inv_level
    time_last_event = 0.0

    total_ordering_cost = 0.0
    area_holding = 0.0
    area_shortage = 0.0

    time_next_event[0] = 0.0
    time_next_event[1] = 1000000000000000000000000000000.0
    time_next_event[2] = time + expon(mean_interdemand)
    time_next_event[3] = num_months
    time_next_event[4] = 0.0


def order_arrival():
    global inv_level, amount, time_next_event
    inv_level = inv_level + amount
    time_next_event[1] = 1000000000000000000000000000000.0


def demand():
    global prob_distrib_demand, inv_level, time_next_event, time, mean_interdemand
    size_demand = 0

    size_demand = random_integer(prob_distrib_demand)
    inv_level = inv_level - size_demand
    time_next_event[2] = time + expon(mean_interdemand)


def evaluate():
    global inv_level, smalls, bigs, amount, total_ordering_cost, setup_cost, incremental_cost, time_next_event, time, minlag, maxlag

    if inv_level < smalls:
        amount = bigs - inv_level
        total_ordering_cost = total_ordering_cost + setup_cost + (incremental_cost * amount)
        time_next_event[1] = time + local_uniform(minlag, maxlag)
    time_next_event[4] = time + 1.0


def report():
    global total_ordering_cost, num_months, holding_cost, area_holding, shortage_cost, area_shortage, smalls, bigs

    avg_holding_cost = 0.0
    avg_ordering_cost = 0.0
    avg_shortage_cost = 0.0
    avg_ordering_cost = total_ordering_cost / num_months
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months
    print ('(', smalls, ', ', bigs, ') ---- ', avg_ordering_cost + avg_holding_cost + avg_shortage_cost, ' ---- ', avg_ordering_cost, ' ---- ', avg_holding_cost, ' ---- ', avg_shortage_cost)


def expon(mean):
    u = uniform(0.0, 1.0)
    expon_number = -mean * log(u)
    return expon_number


def update_time_avg_stats():
    global time, time_last_event, inv_level, area_shortage, area_holding

    time_since_last_event = 0.0

    time_since_last_event = time - time_last_event
    time_last_event = time

    if (inv_level < 0):
        area_shortage = area_shortage - (inv_level * time_since_last_event)
    elif inv_level > 0:
        area_holding = area_holding + (inv_level * time_since_last_event)


def random_integer(prob_distrib):
    i = 1
    u = 0.0

    u = uniform(0, 1)

    while(u > prob_distrib[i]):
        i=i+1
    
    return i


def local_uniform(a, b):
    u = 0.0

    u = uniform(0, 1)

    return a + (u * (b-a))


def timing():
    global num_events, time_next_event, next_event_type
    i = 1
    min_time_next_event = 100000000000000000000000000000.0
    next_event_type = 0

    for i in range(1, num_events+1):
        if time_next_event[i] < min_time_next_event :
            min_time_next_event = time_next_event[i]
            next_event_type = i

    if next_event_type == 3:
        return -9999999999999999999999999999999
    return min_time_next_event;


if __name__ == "__main__":
    main()