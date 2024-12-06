import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.readlines()
        for line in html:
            if line.count('<') > 1 or line.count('>') > 1:
                lst = line.split('>')
                lst = lst[1].split('<')
                if len(lst[0]) >= 1:
                    line = lst[0] + '\n'
                    with codecs.open(result_file, 'a', 'utf-8') as file:
                        file.write(line)


delete_html_tags('draft.html', result_file='cleaned.txt')



