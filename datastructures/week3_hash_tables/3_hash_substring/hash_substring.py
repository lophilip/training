# python3

import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]



def polyhash(inputstring,p,x):
    assert (x>=1),'x should be greater than 1'
    assert (x<=p),'x should be less than p'
    """note: p should be large number"""
    
    """calculate polyhash of inputstring"""
    hash=0
    for i in range(len(inputstring)-1,-1,-1):
        hash=(hash*x+ord(inputstring[i]))%p
    return hash


def precomputehashes(text,patter,x,p):
    """calculate all hash values of text"""
    textlength=len(text)
    patternlength=len(patter)
    H=[None]*(textlength-patternlength+1)
    S=text[textlength-patternlength:textlength]
    H[textlength-patternlength]=polyhash(S,p,x)
    y=1
    for i in range(1,patternlength+1):
        y=(y*x)%p
    for i in range(textlength-patternlength-1,-1,-1):
        H[i]=(x*H[i+1]+ord(text[i])-y*ord(text[i+patternlength]))%p
    return H

def rabinKarp(text,pattern):
    p=7919  #not sure if this prime is big enough
    x=random.randint(1,p-1)
    positions=[]
    phash=polyhash(pattern,p,x)
    H=precomputehashes(text,pattern,x,p)
    
    for i in range(0,len(text)-len(pattern)+1):
        if phash == H[i]:
            #check if string is really equal
            substring=text[i:i+len(pattern)]
            if substring == pattern:
                positions.append(i)
    return positions
           
        

    
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

