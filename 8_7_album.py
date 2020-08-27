def make_album(name, title, tracks = ""):
	album = {'name' : name.title(), 'title' : title.title()}
	if tracks:
		album['tracks'] = tracks
	return album

print(make_album('Get Back', "The Beatles"))
print(make_album('We shot everyone', "The monkees"))
print(make_album('Hey we made an album', "Sprog", 12))