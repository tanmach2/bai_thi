input_str = input("Nhập X, Y: ")
lst =[int(x) for x in input_str.split(',')]
a = lst[0]
b = lst[1]
c = [[0 for col in range(a)] for row in range(b)]

for i in range(b):
    for v in range(a):
        c[i][v]= i*v

print (c)