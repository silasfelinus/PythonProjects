def city_country(city, country):
	combined = '"' + city.title() + ', ' + country.title() + '"'
	return combined

print(city_country('eureka', 'california'))
print(city_country('arcata', 'california'))
print(city_country('paris', 'texas'))

