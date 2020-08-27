def make_city_country(city, country, population = ""):
	if population:
		output = city.title() + ", " + country.title() + " Population=" + str(population)
	else:
		output = city.title() + ", " + country.title()
	return output
