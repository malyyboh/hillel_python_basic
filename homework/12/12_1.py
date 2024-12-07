import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.readlines()

    cleaned_html_lst = []
    for line in html:
        if line.count('<') > 1 or line.count('>') > 1:
            lst = line.split('>')
            lst = lst[1].split('<')
            if len(lst[0]) >= 1:
                line = lst[0]
                cleaned_html_lst.append(line)
    cleaned_html = '\n'.join(cleaned_html_lst)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_html)


delete_html_tags('draft.html', result_file='cleaned.txt')



