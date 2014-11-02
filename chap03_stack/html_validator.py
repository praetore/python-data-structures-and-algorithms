import re
from chap03_stack.Stack import Stack

__author__ = 'Darryl'
__date__ = '22-9-2014'


def get_opening_tags(line):
    return re.finditer(r'<(\w+)[^>]*>', line)


def get_closing_tags(line):
    return re.finditer(r'</(\w+)>', line)


def is_valid_htmlfile(file):
        s = Stack()
        for line in file:
            line = line.lower()
            for i in get_opening_tags(line):
                if i.group(1) not in no_close_allowed():
                    print('Pushing %s' % i.group(1))
                    s.push(i)
            for i in get_closing_tags(line):
                print('Checking %s and %s' % (s.peek().group(), i.group()))
                if s.peek().group(1) == i.group(1):
                    print('Removing %s' % s.pop().group())
                else:
                    return False
        return True


def no_close_allowed():
    no_close_string = """
    </IMG>
</INPUT>
</BR>
</HR>
</FRAME>
</AREA>
</BASE>
</BASEFONT>
</COL>
</ISINDEX>
</LINK>
</META>
</PARAM>
    """
    return re.sub(r'\s', ' ', re.sub(r'[^\w]', ' ', no_close_string)).lower().split()


if __name__ == '__main__':
    with open('test.html', 'r') as f:
        if is_valid_htmlfile(f):
            print('HTML-file is valid')
        else:
            print('HTML-file is invalid')