# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    return_value=-1

    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            #add to stack
            opening_brackets_stack.append(Bracket(next,i))

        if next in ")]}":
            # Process closing bracket, write your code here
            last=''
            lastposition=-1
            if len(opening_brackets_stack)>0:                
                last,lastposition=opening_brackets_stack.pop()                
            else:
                opening_brackets_stack.append(Bracket(next,i)) #edjge case, where closing bracket is first on list
                break

            if next==')' and last=='(':
                pass
            elif next==']' and last=='[':
                pass
            elif next=='}' and last=='{':
                pass
            else:
                opening_brackets_stack.append(Bracket(last,lastposition))
                opening_brackets_stack.append(Bracket(next,i))
                break   #open or mismatched bracket
                
    if len(opening_brackets_stack)>0:
        returnvalue=opening_brackets_stack[-1][1]+1
    else:
        returnvalue=-1

    return returnvalue



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch>0:
        print(mismatch)
    else:
        print ('Success')



if __name__ == "__main__":
    main()
