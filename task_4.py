import time
from random import randint as ri

#1
class User:
    def __init__(self, username, password, activated=False):
        self.username = username
        self.password = password
        self.activated = activated

def login(user):
    while True:
        us = input('Введите логин: ').strip(' ')
        pswd = input('Введите пароль: ').strip(' ')
        print('Выполняется вход в систему...')
        time.sleep(2)
        if not (user.username == us and user.password == pswd): # O(1) + O(1)
            print('Неверное имя пользователя или пароль.')
            continue
        if user.activated is False: # O(n)
            response = input("Активировать учетную запись? д/н:")
            if response == 'д': # O(1)
                user.activated = True
                print('Учетная запись активирована. Добро пожаловать в систему!')
                break
            else:
                print('Перед входом в систему активируйте учетную запись!')
                break
        else:
            print('Добро пожаловать в систему!')
            break

# в итоге O(1)

jackie = User('jackie', 'chan2020')
login(jackie)

lawrence = User('larry', 'golarry1972', True)
login(lawrence)


#2
users = {chr(71+i):str(ri(5,10)) for i in range(5)}
print(users)  # чтобы не угадывать пароль))
active_users = {chr(71+i):str(ri(5,10)) for i in range(2)}

def login2():
    name = input('Input username: ')
    if name in users: # O(n)
        pswd = input('Input password: ')
        if pswd == users[name]: # O(1)
            if name in active_users.keys(): #O(n)
                print('Welcome')
            else:
                response = input('Activate your profile? y/n: ')
                if response.strip() != 'y':
                    print('Activate profile before you login!')
                else:
                    active_users[name] = pswd
                    print('Welcome!')

        else:
            print('Wrong password')
    else:
        print('Unknown user')

    if active_users:
        print('Current active users: ')
        for user in active_users:
            print(user)

login2() # O (n^2)

"""
1. O(1)
2. O(n^2)
Не уверен в своих подсчетах, но первый вариант кажется быстрее и эффективнее, также потому что схожий подход
применяется в "реальном" программировании.
Второй вариант медленее засчет вложенных циклов проверок.
"""