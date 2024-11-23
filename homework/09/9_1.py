def popular_words(text, words):
    popular_words_dict = {}
    text_list = text.lower().split(' ')
    for w in words:
        if w in text_list:
            popular_words_dict.update({w: text_list.count(w)})
        else:
            popular_words_dict.update({w: 0})
    return popular_words_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
