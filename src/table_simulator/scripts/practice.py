import subprocess
import shutil
import os

file_number = 100
# src = '/home/harrison/catkin_ws/src/table_simulator/scripts/tests_folder'
# dst = '/home/harrison/catkin_ws/src/table_simulator/scripts/abstract_tests'
# shutil.move(os.path.join(src, 'abstract_test2.txt'), os.path.join(dst, 'abstract_test1.txt')
# )

subprocess.Popen(["python", "/home/harrison/catkin_ws/src/table_simulator/scripts/bdi_test_generator/drop_loop_run.py", str(file_number)])

# x = int(file_number)
# while (x+2) < (x+8):
#     src = '/home/harrison/catkin_ws/src/table_simulator/scripts/tests_folder'
#     dst = '/home/harrison/catkin_ws/src/table_simulator/scripts/abstract_tests'
#     file_name = "abstract_test"
#     text = ".txt"
#     number = x
#     number+=1
#     file_name = file_name+str(number)+text
#     shutil.move(os.path.join(src, file_name), os.path.join(dst, file_name))
#     x+=1