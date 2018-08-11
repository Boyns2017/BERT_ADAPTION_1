#!/usr/bin/env python

"""
This script converts a list of high-level commands in a *.txt file into a state machine. 
"""

"""
Modified for the table assembly by Dejanira Araiza-Illan, February 2016
"""
import sys
import rospy
import smach
import smach_ros
import re
import os
import math
import random
from table_simulator.msg import *
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Vector3
from std_msgs.msg import Int8
from human_g import reset_head_hand
from human_g import move_head
from human_g import move_hand
from concrete_gen import one_n_mapping_gaze
from concrete_gen import one_n_mapping_location

instructions=[]
reception=0



#--------------------------------------------------------------------------------------------------------
class SendA1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])

    def execute(self, userdata):
        h_signaling = rospy.Publisher('human_voice_a1', Int8, queue_size=1, latch=True) 
	h_signaling.publish(1) 
	rospy.sleep(3)
	h_signaling.publish(0)
	rospy.sleep(0.1)
	return 'outcome1'
	
#--------------------------------------------------------------------------------------------------------
class SendA2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])

    def execute(self, userdata):
        h_signaling = rospy.Publisher('human_voice_a2', Int8, queue_size=1, latch=True) 
	h_signaling.publish(1) 
	rospy.sleep(3)
	h_signaling.publish(0)
	rospy.sleep(5)
	return 'outcome1'

#---------------------------------------------------------------------------------------------------------
class Receive(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])

    def execute(self, userdata):
	global reception
	reception = 0
	rospy.sleep(0.2)
	rospy.Subscriber("robot_signals", Robot, callback)
	if reception == 1:
		return 'outcome1'
	else:
		return 'outcome2'


def callback(data):
	global reception
	if data.informedHuman == 1:
		reception = 1

#--------------------------------------------------------------------------------------------------------
class Gaze0(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])

    def execute(self, userdata):
	one_n_mapping_gaze(0)
        return 'outcome1'
        
#--------------------------------------------------------------------------------------------------------
class Gaze1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])

    def execute(self, userdata):
	one_n_mapping_gaze(1)
        return 'outcome1'


#--------------------------------------------------------------------------------------------------------
class Pressure0(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        
    def execute(self, userdata):
	pub = rospy.Publisher("pressure_e2", Int8, queue_size=1,latch=True)
	pub.publish(0)
	rospy.sleep(0.2)
	return 'outcome1'
#--------------------------------------------------------------------------------------------------------
class Pressure1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        
    def execute(self, userdata):
	pub = rospy.Publisher("pressure_e2", Int8, queue_size=1,latch=True)
	pub.publish(1)
	rospy.sleep(0.2)
	return 'outcome1'

#----------------------------------------------------------------------------------------------------------
class Location0(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        
    def execute(self, userdata):
	one_n_mapping_location(0)
	return 'outcome1'

#----------------------------------------------------------------------------------------------------------
class Location1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        
    def execute(self, userdata):
	one_n_mapping_location(1)
	return 'outcome1'

#----------------------------------------------------------------------------------------------------------
class Timeout(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        
    def execute(self, userdata):
    	print 'Bored'
    	rospy.sleep(0.1)
	return 'outcome1'
#----------------------------------------------------------------------------------------------------------

class Dropped(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        
    def execute(self, userdata):
    	print 'Leg Has Been Dropped'
	print "Human knows this"
    	rospy.sleep(0.1)
	return 'outcome1'

#----------------------------------------------------------------------------------------------------------
class Waits(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
	# Need to extend number of outcomes here to accomdate the calculation ie is it too far or close
    def execute(self, userdata):
	print "Waits"
    	rospy.sleep(4)
	return 'outcome1'

#----------------------------------------------------------------------------------------------------------
class Left_It(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
	# Need to extend number of outcomes here to accomdate the calculation ie is it too far or close
    def execute(self, userdata):
	print "Checking Distance"	
    	rospy.sleep(0.1)	
#-----------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def main(name_file,xx):
    rospy.init_node('human', anonymous=True)
    random.seed(xx)
    sm = smach.StateMachine(outcomes=['end'])

    with sm:
	#Create machine by reading instruction list
	global instructions
	global data
	for num,command in enumerate(open(os.getcwd()+'/src/table_simulator/scripts/test_folder/'+name_file+'.txt','r')): 
		if re.search("Robot_does_not_notice",command): #if the command is to send a signal
			instructions.append('Robot_does_not_notice')
 		elif re.search("Leg_Dropped",command):
			instructions.append('Leg_Dropped')           
		elif re.search("robot_noticed",command):
			instructions.append('robot_noticed')
		elif re.search("robot_close",command): #if the command is to set the value of a variable
			instructions.append('robot_close') 
		elif re.search("robot_far",command):
			instructions.append('robot_far') 
		elif re.search("robot_pick_up",command):
			instructions.append('robot_pick_up')
		elif re.search("robot_indecisive",command): #if the command is to set the value of a variable
			instructions.append('robot_indecisive') 
		elif re.search("robot_left_it",command):
			instructions.append('robot_left_it')        
		elif re.search("human_leaves_it_too_long",command):
			instructions.append('human_leaves_it_too_long') 
		elif re.search("human_notices",command):
			instructions.append('human_notices')
		elif re.search("human_far",command): #if the command is to set the value of a variable
			instructions.append('human_far') 
		elif re.search("human_left_it",command):
			instructions.append('human_left_it')
		elif re.search("human_waits",command):
			instructions.append('human_waits') 
		elif re.search("tell leg",command): #if the command is to send a signal
			instructions.append('sendA1')
		elif re.search("tell humanReady",command):
			instructions.append('sendA2')
		elif re.search("set_param location = 1",command): #if the command is to set the value of a variable
			instructions.append('location1') 
		elif re.search("set_param location = 0",command):
			instructions.append('location0') 
		elif re.search("set_param pressure = 1",command):
			instructions.append('pressure1')
		elif re.search("set_param pressure = 0",command):
			instructions.append('pressure0')
		elif re.search("set_param gaze = 1",command):
			instructions.append('gaze1')
		elif re.search("set_param gaze = 0",command):
			instructions.append('gaze0')
		elif re.search("receivesignal",command): #if the command is to receive a signal
			instructions.append('receive')
		elif re.search("bored",command):
			instructions.append('bored')
		elif re.search("tell_leg",command): #if the command is to send a signal
			instructions.append('tell_leg')
		elif re.search("receive_signal",command): #if the command is to send a signal
			instructions.append('receive_signal')						
		else:
			instructions.append('')

	for i in range(len(instructions)-1):
		# Beginning of extended Instructions
		# To see the added states look above
		if instructions[i] == 'tell_leg':
			if instructions[i+1]== 'receive_signal':	# SHould change this to human_notices Ie Waits too long
				smach.StateMachine.add('tell_leg', SendA1(), 
		                transitions={'outcome1':'RECEIVE'})

		if instructions[i] == 'receive_signal':
			if instructions[i+1]== 'Leg_Dropped':
				smach.StateMachine.add('RECEIVE', Receive(), 
		                transitions={'outcome1':'Leg_Has_Been_Dropped','outcome2':'RECEIVE'})

		if instructions[i] == 'Leg_Dropped':
			if instructions[i+1]== 'human_notices':	# SHould change this to human_notices Ie Waits too long
				smach.StateMachine.add('Leg_Has_Been_Dropped', Dropped(), 
		                transitions={'outcome1':'human_notices'})

		if instructions[i] == 'human_notices':
			if instructions[i+1]== 'human_waits':
				smach.StateMachine.add('human_notices', Waits(), 
		                transitions={'outcome1':'human_waits'})
		
		if instructions[i] == 'human_waits':
			if instructions[i+1] == 'human_left_it':
				smach.StateMachine.add('human_waits', Waits(),
				transitions={'outcome1':'end'})
		
		if instructions[i] == 'human_left_it':
			smach.StateMachine.add('human_left_it', Left_It(),
			transitions={'outcome1':'end'})

		# End of extended Instructions			
		if instructions[i] == 'sendA1':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		   	elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		   
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('SendA1'+str(i), SendA1(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})
		                
		elif instructions[i] == 'sendA2':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		   
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('SendA2'+str(i), SendA2(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})
		                
		elif instructions[i] == 'receive':
			if instructions[i+1]== 'Leg_Dropped':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Leg_Dropped'+str(i+1),'outcome2':'Receive'+str(i)})			
			elif instructions[i+1]== 'sendA1':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'SendA1'+str(i+1),'outcome2':'Receive'+str(i)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'SendA2'+str(i+1),'outcome2':'Receive'+str(i)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Receive'+str(i+1),'outcome2':'Receive'+str(i)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Timeout'+str(i+1),'outcome2':'Receive'+str(i)})
		                
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Location0'+str(i+1),'outcome2':'Receive'+str(i)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Location1'+str(i+1),'outcome2':'Receive'+str(i)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Pressure0'+str(i+1),'outcome2':'Receive'+str(i)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Pressure1'+str(i+1),'outcome2':'Receive'+str(i)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Gaze0'+str(i+1),'outcome2':'Receive'+str(i)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('Receive'+str(i), Receive(), 
		                transitions={'outcome1':'Gaze1'+str(i+1),'outcome2':'Receive'+str(i)})
		                
		elif instructions[i] == 'location0':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		                
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('Location0'+str(i), Location0(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})
		                
		elif instructions[i] == 'location1':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		                
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('Location1'+str(i), Location1(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})
		                
		                
		elif instructions[i]== 'pressure0':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		                
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('Pressure0'+str(i), Pressure0(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})


		elif instructions[i]== 'pressure1':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		                
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('Pressure1'+str(i), Pressure1(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})
		                
		                
		elif instructions[i]== 'gaze0':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		                
		                
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('Gaze0'+str(i), Gaze0(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})

		elif instructions[i]== 'gaze1':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		                
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('Gaze1'+str(i), Gaze1(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})
		
		elif instructions[i]== 'bored':
			if instructions[i+1]== 'sendA1':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'SendA1'+str(i+1)})
		        elif instructions[i+1]== 'sendA2':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'SendA2'+str(i+1)})
	       		elif instructions[i+1]== 'receive':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'Receive'+str(i+1)})
		        elif instructions[i+1]== 'bored':
		   		smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'Timeout'+str(i+1)})
		                
			elif instructions[i+1]== 'location0':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'Location0'+str(i+1)})
		        elif instructions[i+1]== 'location1':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'Location1'+str(i+1)})
		        elif instructions[i+1]== 'pressure0':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'Pressure0'+str(i+1)})
		        elif instructions[i+1]== 'pressure1':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'Pressure1'+str(i+1)})
		        elif instructions[i+1]== 'gaze0':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'Gaze0'+str(i+1)})
		        elif instructions[i+1]== 'gaze1':
				smach.StateMachine.add('Timeout'+str(i), Timeout(), 
		                transitions={'outcome1':'Gaze1'+str(i+1)})

	if instructions[len(instructions)-1] == 'sendA1':
		smach.StateMachine.add('SendA1'+str(len(instructions)-1), SendA1(), 
		transitions={'outcome1':'end'})
	elif instructions[len(instructions)-1] == 'sendA2':
		smach.StateMachine.add('SendA2'+str(len(instructions)-1), SendA2(), 
		transitions={'outcome1':'end'})
	elif instructions[len(instructions)-1] == 'receive':
		smach.StateMachine.add('Receive'+str(len(instructions)-1), Receive(), 
		transitions={'outcome1':'end','outcome2':'Receive'+str(len(instructions)-1)})
	elif instructions[len(instructions)-1] == 'bored':
		smach.StateMachine.add('Timeout'+str(len(instructions)-1), Timeout(), 
		transitions={'outcome1':'end'})
		
	elif instructions[len(instructions)-1] == 'location0':
		smach.StateMachine.add('Location0'+str(len(instructions)-1), Location0(), 
		transitions={'outcome1':'end'})
	elif instructions[len(instructions)-1] == 'location1':
		smach.StateMachine.add('Location1'+str(len(instructions)-1), Location1(), 
		transitions={'outcome1':'end'})
	elif instructions[len(instructions)-1] == 'pressure0':
		smach.StateMachine.add('Pressure0'+str(len(instructions)-1), Pressure0(), 
		transitions={'outcome1':'end'})
	elif instructions[len(instructions)-1] == 'pressure1':
		smach.StateMachine.add('Pressure1'+str(len(instructions)-1), Pressure1(), 
		transitions={'outcome1':'end'})
	elif instructions[len(instructions)-1] == 'gaze0':
		smach.StateMachine.add('Gaze0'+str(len(instructions)-1), Gaze0(), 
		transitions={'outcome1':'end'})
	elif instructions[len(instructions)-1] == 'gaze1':
		smach.StateMachine.add('Gaze1'+str(len(instructions)-1), Gaze1(), 
		transitions={'outcome1':'end'})
	
 
    outcome = sm.execute()


#------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
		main(sys.argv[1],sys.argv[2])
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
	
		pass