from password_generator import password_generator
admin = {}
username_list = []
password_generator(admin,username_list)
username = input('What is your username?')
password = input('What is your password?')
if username in admin:
        if username in username_list and password == admin.get(username):
            print('Access granted')

