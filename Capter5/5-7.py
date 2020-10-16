def find(s):
    i = len(s)
    while True:
        i += 1
        flag = True
        for j in range(len(s)):
            if i - j - 1 < len(s) and s[j] != s[i - j - 1]:
                flag = False
                break
        if flag:
            return i


print(find("abab"))
print(find("qwerty"))
