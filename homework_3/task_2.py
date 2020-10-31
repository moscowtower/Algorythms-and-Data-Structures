from hashlib import sha256
from uuid import uuid4

def hash_salt():
    pwd = input('Введите пароль: ')
    salt = uuid4().hex
    hash = sha256(salt.encode() + pwd.encode()).hexdigest() + ':' + salt
    print('В базе данных хранися строка: ', hash)
    pwd_check = input('Введите пароль еще раз для проверки: ')
    hash_check = sha256(salt.encode() + pwd_check.encode()).hexdigest() + ':' + salt
    print('Вы ввели правильный пароль') if hash == hash_check else print('Неправильный пароль.')


hash_salt()