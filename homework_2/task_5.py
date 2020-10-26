def ascii(start, stop, counter=1):
    if start == stop+1:
        return
    print(f'{start}:{chr(start)}', end=' ')
    if counter % 10 == 0:
        print('', end='\n')
    counter+=1
    start+=1
    ascii(start, stop, counter)

ascii(32, 127)
