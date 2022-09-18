'''Create, store, and view accounts.'''
import random
import string

accounts = {}
# accounts = {' G_,-^~B}LYSkPY(%v4:%': 'John'}

def main(account_dict):
    '''Create and navigate user through login portal.'''
    again = 'y'
    while again.lower() == 'y':
        choice = input('Welcome to the login portal.\n\n' +
                       'Please choose from the options below:\n' +
                       'Create a new account: 1\n' +
                       'Login to existing account: 2\n' +
                       'Enter action: ')
        print()
        if choice == '1':
            again = new_account(account_dict)
        elif choice == '2':
            again = existing_account(account_dict)
        else:
            print(f'{choice} is not a valid input. Please try again')
            print()
            choice = input('Welcome to the login portal.\n\n' +
                       'Please choose from the options below:\n' +
                       'Create a new account: 1\n' +
                       'Login to existing account: 2\n' +
                       'Enter action: ')


def new_account(account_dict):
    '''Create new account. Pass password onto password_check function.'''
    username = input('Enter username: ')
    while username in account_dict:
        username = input(f'{username} is already taken. Please try' +
                          ' another username: ')

    password = password_check(username)

    safe_pass = password_alg(password)
    del password

    account_dict[safe_pass] = username
    print('Account successfully created.')

    again = input('\nWould you like to return to the login ' +
                      'portal? (y/n) ')
    return again


def existing_account(account_dict):
    '''Login to existing account.'''
    username = input('Enter username: ')
    while username not in account_dict.values():
        username = input(f'{username} not found. Please try another' +
                          ' username: ')
    password = input('Enter password: ')

    safe_pass = password_alg(password)

    try:
        if account_dict[safe_pass] == username:
            print(f'Account {username} has been found!')
    except KeyError:
        print('Incorrect username or password. Please try again.')
        existing_account(account_dict)

    again = input('\nWould you like to return to the login ' +
                      'portal? (y/n) ')
    return again


def password_check(username):
    '''Create password. Verify password requirements.'''
    flag_upper = False
    flag_lower = False
    flag_number = False
    flag_special = False

    print('Password requirements:\n' +
          '- Between 6 to 12 characters\n' +
          '- At least one uppercase and one lowercase letter\n' +
          '- At least one number and one special character\n' +
          '- Cannot be the same as your username')
    password = input('\nEnter password: ')
    print()

    if password == username:
        print('Password cannot be the same as your username.' +
              ' Please try again.')
        password_check(username)

    if len(password) < 6:
        print('Password is too short. Please try again.')
        password_check(username)
    elif len(password) > 12:
        print('Password is too long. Please try again.')
        password_check(username)

    for i in password:
        if i.isupper():
            flag_upper = True
        elif i.islower():
            flag_lower = True
        elif i.isnumeric():
            flag_number = True
        elif not i.isalpha() and not i.isnumeric() and i.isascii():
            flag_special = True
        else:
            print(f'Unknown character {i} found. Please try again')
            password_check(username)

    if not flag_upper:
        print('Password does not contain at least one uppercase ' +
              'letter. Please try again')
        password_check(username)
    elif not flag_lower:
        print('Password does not contain at least one lowercase ' +
              'letter. Please try again.')
        password_check(username)
    elif not flag_number:
        print('Password does not contain at least one number .' +
              'Please try again')
        password_check(username)
    elif not flag_special:
        print('Password does not contain at least one special ' +
              'character. Please try again')
        password_check(username)

    if flag_upper and flag_lower and flag_number and flag_special:
        return password

    print('An unknown error has occurred. Please try again.')
    password_check(username)

def password_alg(password):
    '''Hash password.'''
    ascii_pass = ''
    for i in password:
        ascii_pass += str(ord(i))
    del password

    random.seed(int(ascii_pass))

    safe_pass = ''
    for i in ascii_pass:
        safe_pass += random.choice(string.printable)
    del ascii_pass

    return safe_pass

main(accounts)
