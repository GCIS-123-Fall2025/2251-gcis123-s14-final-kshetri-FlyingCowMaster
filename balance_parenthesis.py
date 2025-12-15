
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
from node_stack import Stack

def balance_parenthesis(a_string):
    left_stack = Stack()
    for i in range(len(a_string)):
        value = a_string[i]
        if value == "(":
            left_stack.push((value,i))
        elif value == ")":
            try:
                left_stack.pop()
            except IndexError:
                return -1

    if left_stack.is_empty():
        return 0
    else:
        return left_stack.pop()[1]
    
    


def main():
    print(balance_parenthesis("--(---(------)--"))
    print(balance_parenthesis("()----)"))
    print(balance_parenthesis("-----() -- ( () )"))

if __name__ == "__main__":    main()