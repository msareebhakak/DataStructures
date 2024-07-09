#
# Author: Sareeb Hakak
# Purpose: Learn Stack DS
# Date: 25 Feb 24
# Stack has 2 main operations: push and pop
# It follows LIFO (Last In First Out)
# Push/Pop O(1) and Search by value O(n)
# For python, use list or deque from collections, in C++ std::stack
#

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def check_pairing(cl, op):
    opened = ['[', '{', '(']
    closed = [']', '}', ')']
    if closed.index(cl) == opened.index(op):
        return True
    else:
        return False


def check_balanced_p(expression):
    st = Stack()
    opened = ['[', '{', '(']
    closed = [']', '}', ')']
    for i in expression:
        if i in opened:
            st.push(i)
        elif i in closed:
            if st.is_empty() or not closed.index(i) == opened.index(st.peek()):  # check_pairing(i, st.peek()):
                return False
            else:
                st.pop()
    return st.is_empty()


# reverse a string with stack
def reverse_string(expression):
    stk = Stack()
    for char in expression:
        stk.push(char)
    print(stk.container)
    r_string = ""
    while not stk.is_empty():
        r_string += stk.pop()
    return r_string


if __name__ == '__main__':
    # use list as a stack
    stack_list = []
    stack_list.append(1)  # push operation
    stack_list.append(2)
    stack_list.append(3)
    stack_list.pop()  # remove last
    print(stack_list[-1])  # check last

    # use deque for stack
    stack = deque()
    print(dir(deque))
    stack.append(1)
    print(stack)

    s = Stack()
    print(s.is_empty())

    print(reverse_string(expression="HURMAT"))

    print(check_balanced_p("[()]{}{[()()]()}"))
    print(check_balanced_p("[(])"))
