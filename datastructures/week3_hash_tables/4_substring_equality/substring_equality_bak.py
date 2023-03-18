# python3

import sys
import random


class Solver:
    def __init__(self, s):
        self.s = s

    def ask(self, a, b, l):
        s=self.s
        return s[a : a + l] == s[b : b + l]


class solver_hash_class:
    def __init__(self, s):
        self.s = s
        
        self.x = 263
        self.m1 = 1000000007
        self.m2 = 1000000009
        
        self.calc_hash_precalculation()


    def calc_hash_precalculation(self):
        self.h1 = [0] * (len(self.s)+1)
        self.h2 = [0] * (len(self.s)+1)        
        self.xpower_withmod1 = [0] * (len(self.s)+1)
        self.xpower_withmod2 = [0] * (len(self.s)+1)
        for i in range(1, len(self.s)+1):
            self.h1[i] = (self.h1[i - 1] * self.x + ord(self.s[i-1])) % self.m1
                        
            self.h2[i] = (self.h2[i - 1] * self.x + ord(self.s[i-1])) % self.m2
            

            
            self.xpower_withmod1[i]=pow(self.x,i,self.m1)
            self.xpower_withmod2[i]=pow(self.x,i,self.m2)
        
            
    def calculte_hash(self, a, l):
        
        
        h1=(self.h1[a+l]-self.h1[a]*self.xpower_withmod1[l])%self.m1
        
        h2=(self.h2[a+l]-self.h2[a]*self.xpower_withmod2[l])%self.m2        
        
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

