#!/usr/bin/env python

import pexpect
import time
import re

choose_belief_1 = ["leg1", "leg2", "leg3", "leg4"]
choose_belief_2 = ["human_sees_it", "robot_sees_it"]
choose_belief_3 = ["human_close", "human_far"]


for i1 in choose_belief_1:
    # for i2 in choose_belief_2:
    #     for i3 in choose_belief_3:      
    f = open('meta_orders.txt', 'w')
    f.write(i1+ "\n")
    # f.write(i2+ "\n")
    # f.write(i3+ "\n")
    f.close()
    print "Spawning..."
    child = pexpect.spawn('java -jar Env.jar')
    time.sleep(5)
    pexpect.signal.SIGINT
    f1 = open('coverage_robot.txt', 'a')
    f1.write('------------\n')
    f1.close()

#Separate tests in individual files
i = 1
for num,command in enumerate(open('output.txt','r')): 
	f = open('abstract_tests/abstract_test'+str(i)+'.txt', 'a')
	if re.search("-------",command):
		f.close()
		i = i+1
	else:
		f.write(command)