def foo(word):
    return word.capitalize()


print(foo('word'))

words_list = 'some words need to be here'


def more_words(words):
    end_list = []
    for item in words.split():
        end_list.append(foo(item))
    return ' '.join(end_list)


print(more_words(words_list))
