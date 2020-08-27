# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    
    exposed_string = cc[-4:]
    print(exposed_string)
    hashtag_total = len(cc) - 4
    while hashtag_total > 0:
        exposed_string = "#" + exposed_string
        hashtag_total -= 1
    return exposed_string


cc = 'tgrertedeA'
print(maskify(cc))