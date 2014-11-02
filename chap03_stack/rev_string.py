from chap03_stack.Stack import Stack

__author__ = 'Darryl'


def rev_string(mystr):
    s = Stack()
    [s.push(mystr[i]) for i in range(len(mystr))]
    rev = [s.pop() for i in range(s.size())]

    return "".join(rev)

if __name__ == '__main__':
    text = "darrylenzozino"
    print(rev_string(text))
