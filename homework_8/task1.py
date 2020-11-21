import heapq  
from collections import Counter as C, namedtuple as nt


class Node(nt('Node', ['l', 'r'])): 

    def walk(self, code, index):  
        self.l.walk(code, index + '0')  
        self.r.walk(code, index + '1')  


class Leaf(nt('Leaf', ['char'])): 

    def walk(self, code, index):
        code[self.char] = index if index else '0'  

def huffmanize(s):

    heap = []  
    for char, freq in C(s).items():  
        h.append((freq, len(heap), Leaf(char)))  

    heapq.heapify(heap)  
    count = len(heap)

    while len(heap) > 1:  
        first_freq, first_count, l = heapq.heappop(heap)  
        second_freq, second_count, r = heapq.heappop(heap)  
        heapq.heappush(heap, (first_freq + second_freq, count, Node(l, r)))  
        count += 1

    encoded = {}  
    if heap:  
        [(freq, count, root)] = heap  
        root.walk(encoded, "")  

    return encoded


if __name__ == '__main__':
    s = input('Input string for encoding: ')
    encoded = huffmanize(s)
    encoded_s = ''.join(encoded[ch] for ch in s)
    print(f'Dict size: {len(encoded)}. Encoded string length: {len(encoded_s)}')
    for ch in sorted(encoded):
        print(f'{ch}: {encoded[ch]}')
    print(f'Encoded string: {encoded_s}')