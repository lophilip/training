# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

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

        for i in range(1, len(self.s)+1):
            self.h1[i] = (self.h1[i - 1] * self.x + ord(self.s[i-1])) % self.m1
                        
            self.h2[i] = (self.h2[i - 1] * self.x + ord(self.s[i-1])) % self.m2

        
            
    def calculte_hash(self, a, l):
        y1 = pow(self.x, l, self.m1)
        y2= pow(self.x, l, self.m2)
        
        h1=(self.h1[a+l]-self.h1[a]*y1)%self.m1
        
        h2=(self.h2[a+l]-self.h2[a]*y2)%self.m2        
        
        return h1, h2
    
    def ask(self, a, b, l):        
        string_equivalent = True
        h1_a, h2_a = self.calculte_hash(a, l)
        h1_b, h2_b = self.calculte_hash(b, l)
                
        if h1_a != h1_b or h2_a != h2_b:
            string_equivalent = False
        return string_equivalent




def longest_common_substring(s1, s2):
    """
    Returns the start indices and length of the longest common substring of s1 and s2.
    """
    if not s1 or not s2:
        return 0, 0, 0
    
    string1=solver_hash_class(s1)
    string2=solver_hash_class(s2)   
    

    # Use binary search to find the longest common substring.
    max_len, max_i, max_j = 0, -1, -1
    for i in range(len(s1)):
        lo, hi = 0, min(len(s1)-i, len(s2))
        while lo < hi:
            mid = (lo+hi+1) // 2
            h1 = (hash1[i+mid] - b**(mid-1)*hash1[mid-1]) % p
            h2 = (hash2[i+mid] - b**(mid-1)*hash2[mid-1]) % p
            if h1 == h2:
                lo = mid
            else:
                hi = mid - 1
        if lo > max_len:
            max_len = lo
            max_i = i
            max_j = i+lo
            
        ans=Answer(max_i, max_j-max_len, max_len)

    return ans
    
def longest_common_substring_original(s1, s2):
    """
    Returns the start indices and length of the longest common substring of s1 and s2.
    """
    if not s1 or not s2:
        return 0, 0, 0

    # Choose a prime number p and a base b for the hash function.
    p = 10**9 + 7
    b = 31

    # Compute the hash values of all substrings of s1 and s2 using rolling hashes.
    hash1 = [0] * (len(s1)+1)
    for i in range(1, len(s1)+1):
        hash1[i] = (b*hash1[i-1] + ord(s1[i-1])) % p
    hash2 = [0] * (len(s2)+1)
    for i in range(1, len(s2)+1):
        hash2[i] = (b*hash2[i-1] + ord(s2[i-1])) % p

    # Use binary search to find the longest common substring.
    max_len, max_i, max_j = 0, -1, -1
    for i in range(len(s1)):
        lo, hi = 0, min(len(s1)-i, len(s2))
        while lo < hi:
            mid = (lo+hi+1) // 2
            h1 = (hash1[i+mid] - b**(mid-1)*hash1[i]) % p
            h2 = (hash2[mid] - b**(mid-1)*hash2[0]) % p
            if h1 == h2:
                lo = mid
            else:
                hi = mid - 1
        if lo > max_len:
            max_len = lo
            max_i = i
            max_j = i+lo
            
        ans=Answer(max_i, max_j-max_len, max_len)

    return ans
        
            

        
if __name__=='__main__':
	for line in sys.stdin.readlines():
		s, t = line.split()
		ans = solve(s, t)
		print(ans.i, ans.j, ans.len)
