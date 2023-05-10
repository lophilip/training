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


    def compare_other_hashclass(self, other_hashclass, a, b, l):
        assert isinstance(other_hashclass, solver_hash_class),'other_hashclass is not of type solver_hash_class'        
        string_equivalent = True
        h1_a, h2_a = self.calculte_hash(a, l)
        h1_b, h2_b = other_hashclass.calculte_hash(b, l)
                
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

    #same=string1.compare_other_hashclass(string2, 1, 1, 3)
    #f print(same)

    
    # Use binary search to find the longest common substring.
    # a is long string --> hash table, b is short string --> hash dict
    low = 0
    high = min(len(s1), len(s2))
    aStart, bStart, max_length = 0, 0, 0

    while low <= high:
        mid = (low + high) // 2  # mid is the length of the tested common substring
        if low > high:
            return aStart, bStart, max_length
       
        if string1.compare_other_hashclass(string2, 0, 0, mid):
            for a, b in matches1.items():
                temp = matches2.get(a, -1)
                if temp != -1:
                    max_length = mid
                    aStart, bStart = a, b
                    del aHash1, aHash2, bHash1, bHash2, matches1, matches2
                    return MaxLength(string_a, string_b, mid + 1, high, max_length, aStart, bStart)
        return MaxLength(string_a, string_b, low, mid - 1, max_length, aStart, bStart)
    

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












"""
notes

I had a bit of trouble with this one.  After I finally got it, I figured I would share some insights here about what ultimately worked (in C++):

Initialization/Constructor

    Identify one value x, one hash size (for the hash array), and two large prime numbers p1, p2 for computing two hash function values for comparison.  It was my experience that choice of x made some difference here.  If you are unable to pass after following the remainder of these instructions, try changing x and resubmitting.  

    Regardless of whether s is longer than t, overwrite the member string s with the contents of the shorter input string and member string t with the longer input string.  Store whether or not a switch (s<->t) was required - if there was a switch, you will need to swap the i,j in the final answer's output for the matched substrings.  This allows creating a smaller hash map for comparison.

    Precompute 2 h arrays (see definition in description following the problem statement for Substring Equality) for each input string s and t: one h array per hash function

    Do not precompute powers of x mod p.  You might not need all of them, so don't waste the time and memory computing them.  Just call an efficient power function (see https://www.coursera.org/learn/data-structures/discussions/weeks/3/threads/9fWlJLuNEem-AQpTfWC26g/replies/6J6QDavoEeuw1Q42CpJ9yQ) for each trial length, l

Solution (outer loop)

    Binary search for main loop.  Start by trying l= mid = (right+left)/2, with right = min(s size, t size) and left = 0.  The longest possibility is the length of the shorter two strings

    Check if there is a match between the two strings of length l (see Solution inner loop)

    if there was a match, update the left endpoint to be l+1.  Update the current best guess (i.e. the longest substring indices i, j and length)

    If there was not, update the right endpoint to be l-1

    Run until left == right

Solution (inner loop) - Input length l

    Create hash array with desired hash size (I found 5000 worked ok), call it "Array"

    Compute (x^l) % p1 using efficient power mod p algorithm

    Compute hash function values for first hash function only for all substrings of length l of string s, take the value mod hash array size, and insert the index, a, and first hash function value, H1, into the hash chain at Array[H1 % hash size] (I used a list for the hash chain implementation, with new entries added to the front with push_front).  Use one of the h arrays for string s.

    Until a match is found, consider, looping over index b of starting position of string in t, each substring of length, l, of string t.  Compute the first hash value using one of the cached h arrays for t and check if there is a collision with the hash array "Array".  If there was a collision, compute the second hash functions for both substring s (at stored index a) and substring of t at the current index, b.  If the second hash function values match, mark the indices a, b, and the length l and return.  You only need one match, so don't bother looking for any more after you have found one.
    
"""