def build_profile(first, last, **user_info):

	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('silas', 'knight',
							location='eureka',
							age='42',
							hobbies='video games',
							favorite_color='turquoise')
print(user_profile)
