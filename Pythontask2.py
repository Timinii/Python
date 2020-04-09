import random
import string

define = True
container = []

def password_gen():
    Letters = string.ascii_letters
    Length = 5
    return ''.join(random.choice(Letters) for i in range(Length))


# Employee details collection
while define:
    First = input('\nWhat is your firstname?:>\t')
    Last = input('\nWhat is your last name?:>\t')
    Email = input('\nWhat is your email address?:>\t')

    user_dict = {}
    user_dict["First Name"] = First
    user_dict["Last Name"] = Last
    user_dict["Email Address"] = Email

# Password generation
    Password = First[0:2] + Last[-2:] + password_gen()
    print('\nYour password is: ' + str(Password))

    password_okay = input('\nAre you ok with your password (Yes/No)?:>\t')
    loop_password = True
    while loop_password:

        if password_okay == 'Yes':
            print("'Great! You've successfully inputed your details'")
            user_dict['Password'] = Password
            container.append(user_dict)
            loop_password = False

        else:
            print('\nNo problem!')
            new_password = input('\nPlease input a password greater than or equal to 7:>\t')
            pass_length = True

            while pass_length:

                if len(new_password) >= 7:
                    print("'Great! You've successfully inputed your details'")
                    user_dict['Password'] = Password
                    container.append(user_dict)

                    pass_length = False
                    loop_password = False

                else:
                    print('\nYour password is less than 7')
                    new_password = input('Please enter a new password:>\t')

    new_user = input('\nWould you like to input a new user Yes/No?:>\t')

    if new_user == 'No':
        print('\nEmployee details collection complete')

        print('---All user details are displayed below---')

        define = False

# print out all details nicely
        for i in container:
            print()
            for identifier, log in i.items():

                print(identifier, '=', log)

    else:
        define = True

