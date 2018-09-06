# Written by Harrison Boyns September 2018

from Tkinter import *
import ttk
from PIL import Image, ImageTk
import time
import sys
import rospy


class gui_framework:

    def __init__(self, master, file):
        frame = PanedWindow(master, bd = 3, width = 300, height = 400, relief = SUNKEN, sashwidth = 4, sashrelief=SUNKEN)
            #frame.pack_propagate(0)
        frame.grid_propagate(False)
        
        frame.pack(fill=X, padx=5, pady=5, expand=1)
        
        self.left = Label(master, text=f.read())
        frame.add(self.left)


def main(name_file,xx):
    global f
    root = Tk()
    root.wm_title(name_file)
    root.grid_columnconfigure(3, minsize=100)

    with open("/home/harrison/catkin_ws/src/table_simulator/scripts/abstract_tests/"+name_file+".txt", "r") as f:
        b = gui_framework(root, f)

    root.mainloop()


if __name__ == '__main__':
	try:
		main(sys.argv[1],sys.argv[2])
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
	
		pass