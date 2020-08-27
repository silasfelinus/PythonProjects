rivers = {
	'nile' : {
		'country' : 'Egypt',
		'length' : '4132 miles',
	},

	'mississipi' : {
		'country' : 'America',
		'length' : '2348 miles',
	},

	'amazon' : {
		'country' : 'Brazil',
		'length' : '3977 miles',
	},
}

for river, info in rivers.items():
	print(
	"The " +
	river.title() +
	" is " +
	info['length'] +
	" and runs through " +
	info['country']
	)
