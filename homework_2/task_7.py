def proof(n, current=1, result=[]):
    if current == n+1:
        print(sum(result) == (n*(n+1)/2))
        result.clear()
        return
    result.append(current)
    current += 1
    proof(n, current, result)

proof(5)
proof(555)
proof(995)
