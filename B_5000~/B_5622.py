N = list(input())

A = []

for i in N:
    if i == 'A' or i =='B' or i =='C':
        A.append(2+1)
    elif i == 'D' or i =='E' or i =='F':
        A.append(3+1)
    elif i == 'G' or i =='H' or i =='I':
        A.append(4+1)
    elif i == 'J' or i =='K' or i =='L':
        A.append(5+1)
    elif i == 'M' or i =='N' or i =='O':
        A.append(6+1)
    elif i == 'P' or i =='Q' or i =='R' or i =='S':
        A.append(7+1)
    elif i == 'T' or i =='U' or i =='V':
        A.append(8+1)
    elif i == 'W' or i =='X' or i =='Y' or i == 'Z':
        A.append(9+1)
    else:
        A.append(10+1)   

print(sum(A))