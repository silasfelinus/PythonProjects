import matplotlib.pyplot as plt 
import numpy as np

from die import Die 

#Create 2d6
die_1 = Die()
die_2 = Die()

#Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

#Visualize the results
max_result = die_1.num_sides + die_2.num_sides

"""grabbed from https://stackoverflow.com/questions/54155971/how-to-display-python-crash-course-chapter-15-histogram-using-matplotlib"""

plt.hist(results, bins=np.arange(2, max_result+2)-.5, histtype = 'bar', 
         rwidth=0.8, facecolor = 'blue', edgecolor="k")

plt.title("Dice Plot")
plt.xlabel("Results")
plt.ylabel("Frequency of Result")

plt.show()