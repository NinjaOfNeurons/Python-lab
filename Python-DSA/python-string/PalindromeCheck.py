def ispalan(s):
    rev = s[::-1]
    if rev == s:
        return True
    else:
        return False


ch = "madam"
print(ispalan(ch))