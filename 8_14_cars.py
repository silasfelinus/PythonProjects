def make_car(manufacturer, model, **additional_info):

	profile = {}
	profile['manufacturer'] = manufacturer
	profile['model'] = model
	for key, value in additional_info.items():
		profile[key] = value
	return profile

car = make_car ('subaru', 'outback',
							color = 'blue',
							tow_package=True)
print(car)
