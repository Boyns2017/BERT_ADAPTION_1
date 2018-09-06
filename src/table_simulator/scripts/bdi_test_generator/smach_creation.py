""" Script to check the correctness of the abstract tests files. created by Harrison Boyns 2018 """


import sys
import rospy
import smach
import smach_ros
import re
import os
import math
import random

# Script to check the correctness of the abstract tests files created

instructions=[]
reception=0
def main(name_file):
	#Create machine by reading instruction list
	global instructions
	global data
	for num,command in enumerate(open(os.getcwd()+"/"+name_file+'.txt','r')): 
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
        
        for x in instructions:
            print x
        
        print "Time to build the Smach State Array "
main("output")


