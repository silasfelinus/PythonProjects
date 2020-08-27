import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=20)

#Set chart title and label axes
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

#set the range for each axis
ax.axis([0, 5001, 0, 5100**3])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()