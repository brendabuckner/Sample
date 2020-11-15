# -*- coding: utf-8 -*-

""" Recall that the data for this assignment is called ozoneTemp.csv """
# import matplotlib.pyplot

import matplotlib.pyplot as plt

""" import file ozoneTemp.csv """

f_in = open('/Users/bbuckner/Documents/Assignments/Python/WMPython/Module6/ozoneTemp.csv','r')
data = f_in.readlines()
f_in.close()

""" strip data and split lines """

for i in range(len(data)):
    data[i] = data[i].strip().split(',')

""" save column headings and remove first row """

colHeadings = [x for x in data[0]]
del data[0]    


""" x list contains temp, y list contains ozone """

x = [int(x[1]) for x in data]
y = [int(x[0]) for x in data]

""" set variables for figure and axes sub-objects """

fig,ax = plt.subplots()

""" plot values and specify properties """

ax.scatter(x,y,color = "b", alpha=0.5,s=150)
ax.xaxis.set_label_text('Temperature', fontsize = 16)
ax.yaxis.set_label_text('Ozone', fontsize = 16)
ax.xaxis.set_tick_params(labelsize=14)
ax.yaxis.set_tick_params(labelsize=14)

""" specify figure properties """
fig.suptitle('NYC Temperature and Ozone', fontsize = 20)
fig.set_size_inches(16,9)
fig.savefig('M6oz.jpg')

""" display graph """
plt.show()























