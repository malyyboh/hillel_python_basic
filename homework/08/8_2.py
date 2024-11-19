
def is_palindrome(text):
    lst = [i for i in text.lower() if i.isalnum()]
    lst_reverse = lst.copy()
    lst_reverse.reverse()
    return lst == lst_reverse


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

