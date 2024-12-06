import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.readlines()
        lst = []
        lst2 = []
        for line in html:
            if line.count('<') <= 1 or line.count('>') <= 1:
                line = ''
                with codecs.open(result_file, 'a', 'utf-8') as file:
                    file.write(line)
            elif line.count('<') > 1 or line.count('>') > 1:
                for i in line:
                    ind = line.find('>')
                    ind_2 = line.find('<')
                    ind_3 = line.find('<', ind_2 + 1)
                    if i == '>' and line.index(i) == ind:
                        line = line[ind:ind_3]
                with codecs.open(result_file, 'a', 'utf-8') as file:
                    file.write(line)




        # for i in html:
        #     lst.append(i)

            # if lst.count('<') == 2:
            #     lst2.append(i)
        #
        # lst3 = lst2.copy()[0]
        # string = ''.join(lst3)
        #
        # print(lst)
        # print(lst2)
        # print(lst3)
        # print(string)
        # print(html)

    # with codecs.open(result_file, 'w', 'utf-8') as file:
    #     for i in html:
    #         if i == '<':
    #             html = html.strip('<')
    #     file.write(html)

delete_html_tags('draft.html', result_file='cleaned.txt')



