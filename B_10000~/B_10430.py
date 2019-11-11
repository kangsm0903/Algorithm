# python 10430번
a, b, c = input().split()

print( (int(a)+int(b))%int(c) )
print( (int(a)%int(c) + int(b)%int(c))%int(c) )
print( (int(a)*int(b))%int(c))
print( (int(a)%int(c) * int(b)%int(c))%int(c))