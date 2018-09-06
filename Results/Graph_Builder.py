import matplotlib.pyplot as plt
import numpy as np
import auto
import threading


#  Seperates the requirement array into requirement lists
def average_counter(testbench_results):

    list_of_reqs = []
    req_average = []
    req_std = []
    counter = 0
    requirement_num = 0


    for x in range(0, 7):
        list_of_reqs.append([]) 
        req_average.append([]) 
        req_std.append([])

    # Sorts through the array of environment results
    for seperate_testbench in testbench_results:  
        
        # Sorts through the results of a single emvironment
        for requirements in seperate_testbench:

            # Seperates into individual requirement list
            list_of_reqs[counter].append(requirements)
            counter +=1
        
        counter = 0

    while requirement_num < 7:
        
        # Create array of average
        req_average[requirement_num] = (np.mean(list_of_reqs[requirement_num]))
        
        # Create array of std
        req_std[requirement_num] = (np.std(list_of_reqs[requirement_num]))
        
        # print "Average of req", requirement_num, "is = to ", req_average[requirement_num], ".\t Std is = ", req_std[requirement_num]
        requirement_num+=1
    i = 0
    for j in req_average:
        print j, req_std[i]
        i+=1

    print sum(req_average)
    return req_std, req_average

def create_graph(offline_list, online_list, name):

    print "Offline"
    error_offline ,CTEs_offline = average_counter(offline_list)

    print "Online"
    error_online ,CTEs_online = average_counter(online_list)

    x = [0, 2, 4, 6, 8, 10, 12]
    x2 = [0.7, 2.7, 4.7, 6.7, 8.7, 10.7, 12.7]

    # print error_offline
    # print CTEs_offline

    x_pos = ["R1", "R2", "R3", "R4", "R5", "R6", "R7"]

    fig, ax = plt.subplots()

    ax.bar(x, CTEs_offline, width = 0.4, yerr=error_offline, label = 'Offline', align='edge', alpha=0.5, ecolor='black', capsize=5, color = "orange")
    ax.bar(x2, CTEs_online, width = 0.4, yerr=error_online, label = 'Online', align='center', alpha=0.5, ecolor='black', capsize=5)

    ax.set_ylabel('Number of Requirements Passed')
    ax.set_xlabel('Requirement')

    ax.set_xticks(x)
    ax.set_ylim(0, 140)
    ax.set_xticklabels(x_pos)
    title = "Bar Chart of the Average Requirement " + name + " Rate Test"
    ax.set_title(title)

    ax.yaxis.grid(True)
    plt.legend()

    # Save the figure and show
    plt.tight_layout()
    plt.savefig('./Graphs/'+name+'bar_plot_with_error_bars.png')
    plt.show()

counter = 0

# CHECK THESE
# MAKE A GRAPH FOR OFFLINE && ONLINE && NC

x = 1

offline_list_pass = []
online_list_pass = []
online_list_fail = []
offline_list_fail = []
online_list_NC = []
offline_list_NC = []

while x < 6:
    src_Online = "Online"
    src_Offline = "Offline"
    offline_array_pass, offline_array_fail, offline_array_NC = auto.main(src_Offline+str(x)+"/")
    online_array_pass, online_array_fail, online_array_NC = auto.main(src_Online+str(x)+"/")

    offline_list_pass.append(offline_array_pass)
    online_list_pass.append(online_array_pass)
    
    online_list_fail.append(online_array_fail)
    offline_list_fail.append(offline_array_fail)

    online_list_NC.append(online_array_NC)
    offline_list_NC.append(offline_array_NC)
    x+=1


print "Pass"
create_graph(offline_list_pass, online_list_pass, "Pass")

print "\nFail"
create_graph(offline_list_fail, online_list_fail, "Fail")

print "\nNC"
create_graph(offline_list_NC, online_list_NC, "NC")