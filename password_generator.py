import random

LOWER_LETTERS = "abcderfghijklmnopqrstuvwxys"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "1234567890"
PUNCTUATION = r"#$%^&*()+=-_][{}\|”:?><~;”]"
ALL_CHARS = [LOWER_LETTERS, UPPER_LETTERS, DIGITS, PUNCTUATION]


def shuffle_string(str_to_shuffle):
    str_to_list = list(str_to_shuffle)
    random.shuffle(str_to_list)
    return ''.join(str_to_list)


def generate_password():
    password = random.choice(LOWER_LETTERS) + random.choice(UPPER_LETTERS) + random.choice(DIGITS)
    for i in range(3, 20):
        char_type = random.choice(ALL_CHARS)
        password = password + random.choice(char_type)
    return shuffle_string(password)


if __name__ == '__main__':
    print(len(generate_password()))
    print(generate_password())


