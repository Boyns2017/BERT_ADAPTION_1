""" File used to create the BDI meta text, seperate files, sort filesand drive to the correct folder currently in use 
	Created by Harrison Boyns 2018 """

#!/usr/bin/env python

import pexpect
import time
import re
import random
import rospy
import sys
import os, shutil

def main(number_file):

	# Belief Hierarchy
	choose_belief_1 = ["leg1", "leg2", "leg3", "leg4"]      # This will be fed directly in as a script
	choose_belief_2 = ["dropped"]
	choose_belief_3 = ["human_waits", "human_notices"]
	choose_belief_4 = ["robot_does_not_notice"]
	choose_belief_5 = ["far", "close"]
	choose_belief_6 = ["indecisive", "decisive"]
	j = 0
	random.seed(300)
	# Create meta text file
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
		# Spawn the jar file I.e the BDI network
		child = pexpect.spawn('java -jar /home/harrison/catkin_ws/src/table_simulator/scripts/bdi_test_generator/reactive_BDI_Env.jar')
		time.sleep(5)
		pexpect.signal.SIGINT
		f1 = open('/home/harrison/catkin_ws/src/table_simulator/scripts/bdi_test_generator/coverage_robot.txt', 'a')
		pexpect.signal.SIGINT
		f1.write('------------\n')
		f1.close()

	# Separate tests into individual files
	i = 1
	print "Seperating"
	folder = '/home/harrison/catkin_ws/src/table_simulator/scripts/tests_folder'
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			#elif os.path.isdir(file_path): shutil.rmtree(file_path)
		except Exception as e:
			print(e)	

	# Separate tests into individual files
	# Place into the test folder
#	/home/harrison/catkin_ws/src/table_simulator/scripts/output.txt
	for num,command in enumerate(open('/home/harrison/catkin_ws/output.txt','r')):
		f = open('/home/harrison/catkin_ws/src/table_simulator/scripts/tests_folder/abstract_test'+str(i)+'.txt', 'a')
		if re.search("-------",command):
			f.close()
			i = i+1
		else:
			f.write(command)

	x = int(number_file)

	# Replace files in folder currently in use with newly created tests
	for j in range(0, 5):
		src = '/home/harrison/catkin_ws/src/table_simulator/scripts/tests_folder'
		dst = '/home/harrison/catkin_ws/src/table_simulator/scripts/abstract_tests'
		file_name = "abstract_test"
		text = ".txt"
		number = x
		number += 1
		file_name = file_name+str(number)+text
		shutil.move(os.path.join(src, file_name), os.path.join(dst, file_name))
		x+=1

if __name__ == '__main__':
	try:
		main(sys.argv[1])
		print "Double End"

	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
	
		pass