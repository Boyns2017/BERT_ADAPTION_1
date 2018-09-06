#!/usr/bin/env python
"""
Written by Nyasha Masamba
"""

import matplotlib.pyplot as plt
import numpy as np
import re
from math import sqrt
import os

covered_bdi_pseudo=[]
covered_bdi_const_pseudo = []
covered_tr_pseudo=[]
covered_tr_const_pseudo = []

covered_tr_pseudo.insert(0, 0)
covered_tr_const_pseudo.insert(0, 0)
covered_bdi_pseudo.insert(0, 0)
covered_bdi_const_pseudo.insert(0, 0)

for num,line in enumerate(open(os.getcwd()+'/results/bdi_pseudo_cp/coverage/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		covered_bdi_pseudo.append(int(getdata[0]))


for num,line in enumerate(open(os.getcwd()+'/results/bdi_const_pseudo/coverage/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		covered_bdi_const_pseudo.append(int(getdata[0]))

for num,line in enumerate(open(os.getcwd()+'/results/tr_pseudo/coverage/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		covered_tr_pseudo.append(int(getdata[0]))


for num,line in enumerate(open(os.getcwd()+'/results/tr_const_pseudo/coverage/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		covered_tr_const_pseudo.append(int(getdata[0]))

covered_tr_pseudo.sort()
covered_tr_const_pseudo.sort()
covered_bdi_pseudo.sort()
covered_bdi_const_pseudo.sort()

plt.plot(covered_tr_const_pseudo, 'b-', label = 'TR Constrained Pseudorandom')
plt.plot(covered_tr_pseudo, 'r-', label = 'TR Pseudorandom')
plt.plot(covered_bdi_const_pseudo, 'g--', label = 'BDI Constrained Pseudorandom')
plt.plot(covered_bdi_pseudo, 'm--', label = 'BDI Pseudorandom')
plt.axis([-5, 130, 0,100])
plt.xlabel('Tests')
plt.ylabel('Code Coverage (%)')
plt.legend(bbox_to_anchor=(0.97, 0.25), loc=1, borderaxespad=1.0,prop={'size':8})
plt.savefig('all_covplot.eps')

