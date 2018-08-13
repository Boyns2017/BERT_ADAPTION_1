#!/usr/bin/env python

import pexpect
import time
import re
import random

choose_belief_1 = ["leg1", "leg2", "leg3", "leg4"]      # This will be fed directly in as a script
choose_belief_2 = ["dropped"]
choose_belief_3 = ["human_waits", "human_notices"]
choose_belief_4 = ["robot_does_not_notice"]
choose_belief_5 = ["far", "close"]
choose_belief_6 = ["indecisive", "decisive"]
j = 0
random.seed(300)
# Assemble 100 cases randomly but with constraints
for ii in range(0,20):
	f = open('/home/harrison/catkin_ws/src/table_simulator/scripts/bdi_test_generator/meta_orders.txt', 'w')
	print "Working"
	select2 = random.randint(0,3)
	f.write(choose_belief_1[select2]+'\n')
	select2 = 0
	f.write(choose_belief_2[select2]+'\n')
	select2 = random.randint(0,1)
	f.write(choose_belief_3[select2]+'\n')
	select2 = 0
	f.write(choose_belief_4[select2]+'\n')
	select2 = random.randint(0,1)
	f.write(choose_belief_5[select2]+'\n')
	select2 = random.randint(0,1)	
	f.write(choose_belief_6[select2]+'\n')
	f.close()
	print "Spawning"
	#  /home/harrison/catkin_ws/src/table_simulator/scripts/bdi_test_generator/
	child = pexpect.spawn('java -jar /home/harrison/catkin_ws/src/table_simulator/scripts/bdi_test_generator/reactive_BDI_Env.jar')
	time.sleep(5)
	pexpect.signal.SIGINT
	f1 = open('/home/harrison/catkin_ws/src/table_simulator/scripts/bdi_test_generator/coverage_robot.txt', 'a')
	pexpect.signal.SIGINT
	f1.write('------------\n')
	f1.close()

# Separate tests in individual files
i = 1
print "Seperating"
#/home/harrison/catkin_ws/src/table_simulator/scripts/bdi_test_generator/
#/home/harrison/catkin_ws/src/table_simulator/scripts/test_folder/
for num,command in enumerate(open('/home/harrison/catkin_ws/src/output.txt','r')):
	f = open('/home/harrison/catkin_ws/src/table_simulator/scripts/test_folder/abstract_test'+str(i)+'.txt', 'a')
	if re.search("-------",command):
		f.close()
		i = i+1
	else:
		f.write(command)