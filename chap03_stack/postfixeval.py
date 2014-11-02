from chap03_stack.Stack import Stack

__author__ = 'Darryl'
__date__ = '17-8-2014'


def postfix_eval(postfix_expr):
    operands = Stack()
    tokens = " ".join(postfix_expr).split()
    for token in tokens:
        if token in "0123456789":
            operands.push(int(token))
        else:
            try:
                operand2 = operands.pop()
                operand1 = operands.pop()
                result = do_math(token, operand1, operand2)
                operands.push(result)
            except IndexError:
                return 'Error'
    return operands.pop()


def do_math(op, op1, op2):
    if op == "*":
        val = op1 * op2
    elif op == "/":
        val = op1 / op2
    elif op == "+":
        val = op1 + op2
    elif op == "^":
        val = op1 ** op2
    else:
        val = op1 - op2
    return val


if __name__ == '__main__':
    print(postfix_eval('2 3 * 4 +') == 10)
    print(postfix_eval('1 2 + 3 + 4 + 5 +') == 15)
    print(postfix_eval('1 2 3 4 5 * + * +') == 47)
    print(postfix_eval('4 4 ^') == 256)
    print(postfix_eval('4 + 5'))