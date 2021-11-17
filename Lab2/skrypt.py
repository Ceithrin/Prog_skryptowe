import re
#-*-coding: utf-8-*-

def word_match(string):
    new_letters = re.search(r'[a-zA-Ząężźćńóś]+', string)
    if new_letters:
        return (new_letters.start(), new_letters.group()) # zwraca indeks początku dopasowania i znalezione slowo
    else:
        return None

def number_match(string):
    new_numbers = re.search(r'\d+', string)
    if new_numbers:
        return (new_numbers.start(), new_numbers.group())
    else:
        return None

if __name__ == '__main__':
    while True:
        try:
            test_input = input()
            result_word = word_match(test_input)
            result_number = number_match(test_input)
            if chr(4) in test_input:
                break
            if result_number != None and result_word != None:
                if result_number[0] < result_word[0]:
                    print(f'Liczba: {result_number[1]}')
                    print(f'Wyraz: {result_word[1]}')
                else:
                    print(f'Wyraz: {result_word[1]}')
                    print(f'Liczba: {result_number[1]}')
            elif result_number != None:
                print(f'Liczba: {result_number[1]}')
            elif result_word != None:
                print(f'Wyraz: {result_word[1]}')
        except EOFError:
            break