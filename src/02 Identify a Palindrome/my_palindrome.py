import re
def is_palindrome(words):
    forward = ''.join(re.findall("[a-z]+", words.lower()))
    backward = forward[::-1]
    print(f"{forward} {backward}")
    # if forward == backward:
    #   return True
    # return False
    return forward == backward