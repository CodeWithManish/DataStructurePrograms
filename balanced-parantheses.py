from stack_operation import Stack

stack = Stack()

open_list = ['[', '{', '(']
close_list = [']', '}', ')']


def is_balance(string):
    for i in string:
        if i in open_list:
            stack.push(i)
        if i in close_list:
            position = close_list.index(i)
            if stack.size() > 0 and open_list[position] == stack.peek():
                stack.pop()
            else:
                return "Unbalanced"

    if stack.size() == 0:
        return "Balanced"

    else:
        return "Unbalanced"


if __name__ == '__main__':
    input_string = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"
    print(is_balance(input_string))
