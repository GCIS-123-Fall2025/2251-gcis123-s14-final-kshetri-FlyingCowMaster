import node_stack

"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #4 (25 points)
Filename: even_digits.py

Define a function named "even_digits" that declares a parameter for an 
    integer. The function should return a copy of the integer with the odd
    digits removed. You MUST NOT convert the integer to/from a string, but 
    instead may only use basic arithmetic operators (e.g. %, //, etc.).

    Given Input     Expected Output
    1               0
    2               2
    34              4
    1234567890      24680

For credit your function must use a stack or a queue in a significant way.
    You must not use any other data structures. For full credit, your 
    implementation must run in linear time.
"""

def even_digits(integer):
    all_stack = node_stack.Stack()
    even_stack = node_stack.Stack()
    while integer >= 1:
        i = 1
        f = float(integer)
        while f > 9:
            f /= 10
            i *= 10
        f = int(f)
        all_stack.push(f)
        integer -= f*i

    print(all_stack)

    while not all_stack.is_empty():
        i = all_stack.pop()
        if i % 2 == 0:
            even_stack.push(i)
    
    inc = 1
    final = 0
    while not even_stack.is_empty():
        value = even_stack.pop()
        final += value*inc
        inc *= 10
    
    return final
    

print(even_digits(1234567890))

# several test cases provided for even digits - 1, 2, 34, 1234567890
def test_even_digits_1():
    # setup
    integer = 1
    expected = 0
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_2():
    # setup
    integer = 2
    expected = 2
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_34():
    # setup
    integer = 34
    expected = 4
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_1234567890():
    # setup
    integer = 1234567890
    expected = 24680
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual