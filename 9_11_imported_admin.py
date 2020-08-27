from admin import Admin


ronin = Admin('ronin', 'knight')

ronin.describe_user()
ronin.greet_user()

ronin.privileges.show_privileges()

ronin.privileges.privileges = ["can delete posts", "can see home addresses", "can access webcams remotely",]

ronin.privileges.show_privileges()