from urllib import request
from bs4 import BeautifulSoup

__author__ = 'darryl'


def get_popular_names():
    names = []
    html = request.urlopen('http://www.babycenter.com/popularBabyNames.htm?year=2014').read()
    soup = BeautifulSoup(html)
    for i in range(40):
        names.append(soup.find(id='bcBoy_%s' % str(i+1)).get_text())
        names.append(soup.find(id='bcGirl_%s' % str(i+1)).get_text())
    return names


def write_to_file(namelist):
    with open('names.txt', 'w') as f:
        for i in namelist:
            f.write(i + '\n')

if __name__ == '__main__':
    names = get_popular_names()
    write_to_file(names)