s = input()
n = int(input())
res = ''
for i in s:
    if i.isdigit():
        res += chr((ord(i)+n-48)%10 + 48)
    elif i.isupper():
        res += chr((ord(i)+n-65)%26 + 65)
    elif i.islower():
        res += chr((ord(i)+n-97)%26 + 97)
    else:
        res += i
print(res)
