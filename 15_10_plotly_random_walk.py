import plotly.graph_objs as go

from random_walk import RandomWalk 


#Make a random walk
number_of_walks = 5000
rw = RandomWalk(number_of_walks)
rw.fill_walk()

#Plot the points in the walk
fig = go.Figure(data=go.Scatter(
	x = rw.x_values,
	y = rw.y_values,
	mode='markers', 
	name="Random Walk", 
	marker=dict(
		color=[i for i in range(number_of_walks)],
		size=8,
		colorscale='Greens',
		showscale=True
	)
))


fig.show()
