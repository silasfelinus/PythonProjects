import restaurant


my_restaurant = restaurant.IceCreamStand('Cold Shoulder')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.flavors = ['chocolate', 'vanilla', 'onion']
my_restaurant.display_favors()