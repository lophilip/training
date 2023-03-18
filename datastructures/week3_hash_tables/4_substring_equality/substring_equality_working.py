# python3
import sys

#from substring_equality_simple import *


class Solver:
    def __init__(self, s):
        self.s = s

    def ask(self, a, b, l):
        s=self.s
        return s[a : a + l] == s[b : b + l]

def HashTable(s, prime, x):
    hash_table = list([] for _ in range(len(s) + 1))
    hash_table[0] = 0
    for i in range(1, len(s) + 1):
        hash_table[i] = (hash_table[i - 1] * x + ord(s[i - 1])) % prime
    return hash_table


def HashValue(hash_table, prime, x, start, length):
    y = pow(x, length, prime)
    hash_value = (hash_table[start + length] - y * hash_table[start]) % prime
    return hash_value


#this is much slower then substring_equality_simple.py, because it uses classes
#in python accessing self is much slower then accessing a local or glbal variable.
class solver_hash_class:
    def __init__(self, s):
        self.s = s
        
        self.x = 263
        self.m1 = 1000000007
        self.m2 = 1000000009
        
        self.calc_hash_precalculation()


    def calc_hash_precalculation(self):
        self.h1 = HashTable(self.s, self.m1, self.x)
        self.h2 = HashTable(self.s, self.m2, self.x)                       
            
    def calculte_hash(self, a, l):
        
        
        h1=HashValue(self.h1, self.m1, self.x, a, l)
        
        
        h2=HashValue(self.h2, self.m2, self.x, a, l)
        
        return h1, h2
    
    def ask(self, a, b, l):        
        string_equivalent = True
        h1_a, h2_a = self.calculte_hash(a, l)
        h1_b, h2_b = self.calculte_hash(b, l)
                
        if h1_a != h1_b or h2_a != h2_b:
            string_equivalent = False
        return string_equivalent
    
           
          


if __name__ == '__main__':
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    
    use_hash = True
    if use_hash:
        solver = solver_hash_class(s)
    else:    
        solver = Solver(s)
        
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")

