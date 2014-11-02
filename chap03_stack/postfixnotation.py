from chap03_stack.Stack import Stack

__author__ = 'Darryl'
__date__ = '17-8-2014'


def infix_to_postfix(infix_expr):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    operators = Stack()
    postfix_list = []
    closed = True
    tokens = " ".join(infix_expr).split()

    for token in tokens:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            operators.push(token)
            closed = False
        elif token == ')':
            if closed:
                return 'Error'
            try:
                top_token = operators.pop()
                while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = operators.pop()
            except IndexError:
                return 'Error'
        else:
            while (not operators.is_empty()) and (precedence[operators.peek()] >= precedence[token]):
                postfix_list.append(operators.pop())
            operators.push(token)

    if not closed:
        return 'Error'

    while not operators.is_empty():
        postfix_list.append(operators.pop())

    return " ".join(postfix_list)

if __name__ == '__main__':
    # print(infix_to_postfix('2 + 3'))
    # print(infix_to_postfix('(A+B)*(C+D)*(E+F)'))
    # print(infix_to_postfix('A+((B+C)*(D+E))'))
    # print(infix_to_postfix('A*B*C*D+E+F'))
    print(infix_to_postfix('3)+5'))
    print(infix_to_postfix('3(+5'))