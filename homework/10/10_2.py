import string

str_punctuation_whitespace = string.punctuation + string.whitespace


def first_word(text):
    """ Пошук першого слова """
    first_word_list = []
    text = text.strip(str_punctuation_whitespace)
    for letter in text:
        if letter.isalpha() or letter == "'":
            first_word_list.append(letter)
        else:
            break
    return ''.join(first_word_list)


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'".., and so on ..."
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')



