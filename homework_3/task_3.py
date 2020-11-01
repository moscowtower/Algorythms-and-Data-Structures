from hashlib import sha256

def findSubstrings():
    result = set()
    string = input('Введите строку:')
    n = len(string)
    for i in range(n+1):
        for j in range(n+1):
            var = ''.join(string[i:j])
            if var:
                print(var)
                result.add(sha256(var.encode('utf-8')).hexdigest())
    print(f'Было найдено {len(result)} различных подстрок в строке "{string}"')


findSubstrings()