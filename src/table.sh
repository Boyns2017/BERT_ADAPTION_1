#!/bin/bash
# Extended by Harrison Septermber 2018

rm ~/catkin_ws/stats.txt
rm /tmp/a1out*
rm /tmp/a2out*
rm /tmp/a3out*
rm /tmp/a4out*
rm /tmp/robot*
rm /tmp/human*
rm ~/catkin_ws/assertion*

cd ~/catkin_ws
(roscore & echo $! >> /tmp/mainpids) &
(sleep 5; roslaunch table_simulator bert2_gazebo.launch & echo $! >> /tmp/mainpids) &
(sleep 10; roslaunch bert2_moveit move_group.launch & echo $! >> /tmp/mainpids) &


COUNTER=1
while [ $COUNTER -lt 131 ]; do
	sleep 15
	rm -f /tmp/rospids

	(rosrun table_simulator object.py & echo $! >> /tmp/rospids) &
	(rosrun table_simulator pressure.py & echo $! >> /tmp/rospids) &
	(rosrun table_simulator sensors.py $COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator voice_commands.py & echo $! >> /tmp/rospids) &
	(rosrun table_simulator human_g.py & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion1.py $COUNTER>> /tmp/a1out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion2.py $COUNTER>> /tmp/a2out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion3.py $COUNTER>> /tmp/a3out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion4.py $COUNTER>> /tmp/a4out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion6.py $COUNTER>> /tmp/a4out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion7.py $COUNTER>> /tmp/a4out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator assertion8.py $COUNTER>> /tmp/a4out$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator robot.py $COUNTER>> /tmp/robotout$COUNTER & echo $! >> /tmp/rospids) &
	(rosrun table_simulator human.py abstract_test$COUNTER $COUNTER >> /tmp/humanout$COUNTER) &
	(python /home/harrison/catkin_ws/src/GUI.py abstract_test$COUNTER $COUNTER x) &
#	(rosrun table_simulator human.py cp_$COUNTER $COUNTER >> /tmp/humanout$COUNTER) &
	(sleep 200; python src/table_simulator/scripts/check_code_coverage.py)
	cat /tmp/rospids | xargs kill 
	
    let COUNTER=COUNTER+1 
done

cat /tmp/mainpids | xargs kill 