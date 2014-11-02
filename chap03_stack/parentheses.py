from chap03_stack.Stack import Stack

__author__ = 'Darryl'


def is_balanced(pars):
    s = Stack()
    matches = {"{": "}", "(": ")", "<": ">", "[": "]"}
    for i in pars.replace(" ", ""):
        if i in matches.keys():
            s.push(i)
        elif i == matches[s.peek()]:
            s.pop()
        else:
            return False
    return s.is_empty()


if __name__ == '__main__':
    pars = '[ [ { { ( ( ) ) } } ] ]'
    print(is_balanced(pars))
    pars2 = '( ( ( [ ) ] ) )'
    print(is_balanced(pars2))