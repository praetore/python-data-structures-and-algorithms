import random

__author__ = 'Darryl'


def score(guess, sent):
    return (100 / len(sent)) * sum(1 for i in correct(guess, sent) if i['correct'])


def correct_list(char, is_correct):
    return {"char": char, "correct": is_correct}


def correct(guess, sentence):
    return [correct_list(guess[i], True) if guess[i] == sentence[i]
            else correct_list(guess[i], False) for i in range(len(guess))]


def make_guess(chars, position, sentence):
    return [random.choice([char for char in chars if char not in position[i]['guessed']])
            if not position[i]['pos_char'] else position[i]['pos_char'] for i in range(len(sentence))]


def main():
    sentence = "methinks it is like a weasel"

    chars = [chr(i).lower() for i in range(65, 91)] + [" "]

    position = [{"pos_char": "", "guessed": []} for i in range(len(sentence))]
    percent_score = 0
    attempt_count = 0

    while percent_score < 100:
        attempt_count += 1

        guess = make_guess(chars, position, sentence)

        check = correct(guess, sentence)
        correct_count = sum(1 for i in check if i['correct'])
        for i in range(len(check)):
            already_guessed = position[i]['guessed']
            guessed_char = check[i]['char']
            if guessed_char not in already_guessed:
                already_guessed.append(guessed_char)
            if check[i]['correct']:
                position[i]['pos_char'] = guessed_char

        curr_score = score(guess, sentence)
        if curr_score > percent_score:
            percent_score = curr_score
            str_guess = "".join(guess)
            print("%s - %d characters correct, Score: %d%% in the %dth attempt" %
                  (str_guess, correct_count, percent_score, attempt_count))


if __name__ == '__main__':
    main()