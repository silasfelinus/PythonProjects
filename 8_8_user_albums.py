def make_album(name, title, tracks = ""):
	album = {'name' : name.title(), 'title' : title.title()}
	if tracks:
		album['tracks'] = tracks
	return album

while True:
	print("Please tell me the band name:")
	print("(Enter 'q' at any time to quit)")

	band = input("Band Name: ")
	if band == 'q':
		break

	album = input("Album Name: ")
	if album == 'q':
		break

	print(make_album(band, album))
