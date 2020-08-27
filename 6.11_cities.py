cities = {
	'eureka' : {
		'country' : 'USA',
		'population' : '36k',
		'fact' : "It's ok",
		},

	'vienna' : {
		'country' : 'Austria',
		'population' : '1.9 million',
		'fact' : "Great place to busk",
		},

	'paris' : {
		'country' : 'France',
		'population' : '2.1 million',
		'fact' : "The prettiest dirty city",
		},

	}
for city, city_info in cities.items():
	print("\nName: " + city.title())
	print("\tCountry: " + city_info['country'])
	print("\tPopulation: " + city_info['population'])
	print("\tFact: " + city_info['fact'])