__author__ = 'Darryl'


def no_dupe(word_list):
    letter_list = []
    for a_word in word_list:
        for a_letter in a_word:
            if a_letter not in letter_list:
                letter_list.append(a_letter)
    print(letter_list)


def no_dupe_comp(word_list):
    letter_list = []
    [letter_list.append(a_letter) for a_word in word_list for a_letter in a_word if a_letter not in letter_list]
    print(letter_list)


def main():
    word_list = ['cat', 'dog', 'rabbit']
    no_dupe(word_list)
    no_dupe_comp(word_list)

if __name__ == '__main__':
    main()