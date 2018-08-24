#!/usr/bin/env python
"""
Implements assertion 3: if 'flag1==1' then Gazebo_read


Written by Harrison Boyns, August 2018
"""
import sys
import rospy
import smach
import smach_ros
import math
import random
import time
from table_simulator.msg import *
from std_msgs.msg import Int8

# receivedflag1=0
# receivedflag2=0
# checked1=0
# checked2=0
# t_or_f=0
# xx = 0
# yy = 0
# zz = 0
# globaltime=0
stats = open('assertion8.txt','a')
fileno = 0

class Flag1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])

    def execute(self, userdata):
	global receivedflag1
	receivedflag1 = 0
	rospy.sleep(0.05)
	rospy.Subscriber("human_left_it", Int8, callback1)
	if receivedflag1 == 1:
		receivedflag1 = 0
		return 'outcome1'
        else:
		return 'outcome2'
		
def callback1(data):
	global receivedflag1
	if data.data ==1:
		receivedflag1 = 1
	else:
		receivedflag1 = 0
		
class Flag2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])

    def execute(self, userdata):
	global receivedflag2
	global start
#	global stats
	receivedflag2 = 0
	rospy.sleep(0.01)
	rospy.Subscriber("human_left_it", Int8, callback2)
	if receivedflag2 == 1:
		stats.write('Assertion 1 at test '+ str(fileno) +': Passed at global time '+ str(time.time()-globaltime) +'\n')
        return 'outcome2'
	stats.write('Assertion 1 at test '+ str(fileno) +': Failed at global time '+ str(time.time()-globaltime) +'\n')
	return 'outcome1'

def callback2(data):
	global receivedflag2
	if data.data == 1:
		receivedflag2 = 1
	else:
		receivedflag2 = 0		
		
def main(number):
	rospy.init_node('assertion8', anonymous=True) #Start node first
	global globaltime
	globaltime = time.time()
	global fileno
	fileno = number
	# Create a SMACH state machine
    	sm = smach.StateMachine(outcomes=['Done'])

   	 # Open the container
   	with sm:
		#Receive signal
		smach.StateMachine.add('Flag1', Flag1(), 
                transitions={'outcome1':'Flag2','outcome2':'Flag1'})

		#Check
		smach.StateMachine.add('Flag2', Flag2(), 
                transitions={'outcome1':'Flag2','outcome2':'Flag1'})

	# Execute SMACH plan
    	outcome = sm.execute()

if __name__ == '__main__':
	try:
		main(sys.argv[1])
	except	rospy.ROSInterruptException:
		pass