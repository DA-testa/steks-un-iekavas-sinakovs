# python3
# Makars Sinakovs 221RDB519

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # enumerate atdot gan indeksu gan simbolus
        if next in "([{":
            # Process opening bracket, write your code here
            # japievieno strukturai vertibu
            # Bracket(char,index)
            opening_brackets_stack.append(Bracket(next,i+1))
            

        if next in ")]}":
            # Process closing bracket, write your code here
            # empty !=
            # pop() - remove and return removed
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1 
            opening_brackets_stack.pop()
    if opening_brackets_stack:
       return opening_brackets_stack[0].position
    return "Success"        


def main():
    text = input()
    # Printing answer, write your code here
    if "I" in text:
        text=input()
    elif "F" in text:
        filen=input()
        with open(("./test/"+filen),"r") as file:
        # open(name,read write...)
            text=file.read()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
# norada ka main ir galvena