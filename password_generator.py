'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
def password_generator(admin,username_list):
    print('Welcome!')
    username = input('What would you like your username to be?')
    print('Ok'
          'Please wait as we generate a password for you ... ')

    import random
    admin = {}
    password = []
    alphabets = ['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m']
    alphabets_upper = ['A','S','D','F','G','H','J','K','L','P','O','I','U','Y','T','R','E','W','Q','Z','X','C','V','B','N','M']
    numbers = range(0,9)
    symbols = ['!','"','£','$','%','^','&','*','(',')','?','>','<']
    list_of_choices = [numbers,alphabets_upper,alphabets,symbols]
    username_list = [username]

    for x in range(random.randrange(7,15)):
        first_choice = random.choice(list_of_choices)

        if first_choice == symbols:
            second_choice = random.choice(symbols)
            password.append(second_choice)

        if first_choice == alphabets:
            second_choice = random.choice(alphabets)
            password.append(second_choice)

        if first_choice == alphabets_upper:
            second_choice = random.choice(alphabets_upper)
            password.append(second_choice)

        if first_choice == numbers:
            second_choice = random.choice(numbers)
            password.append(second_choice)

    print('Your password is',password)

    admin[username] = password
    print(admin)
    exit()
    password_generator(admin,username_list)

