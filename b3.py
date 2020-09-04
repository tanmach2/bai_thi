s = input()
a = 0       # chữ số
b = 0       # chữ cái
for c in s:
    if c.isdigit():
        a += 1
    elif c.isalpha():
        b+=1

print(int(a))
print (int(b))