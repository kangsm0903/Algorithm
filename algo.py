# python 10171번
# print('\\    /\\')
# print(" )  ( ')")
# print("(  /  )") 
# print(" \\(__)|")

# print("\n\n")

# c language
#   printf("\\    /\\ \n");
# 	printf(" )  ( ') \n");
# 	printf("(  /  ) \n");
# 	printf(" \\(__)| \n");

# ---------------------------------------------------------------------------------------------------------------------------------

# python 10172번
# print("|\\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\__|")

# print('\n\n')

# c language
#   printf("|\\_/| \n");
#   printf("|q p|   /} \n");
#   printf('( 0 )"""\\ \n');
#   printf('|"^"`    | \n');
#   printf("||_/=\\\__| \n");

# --------------------------------------------------------------------------------------------------------------------------------

# python 	10998번
# a ,b = input().split()
# c = int(a) * int(b)
# print(c)

# # c language
# int num1, num2, cross;
# scanf_s("%d %d", &num1, &num2);
# cross = num1 * num2;
# printf("%d", cross);

# --------------------------------------------------------------------------------------------------------------------------------

# python 1008번
# a ,b = input().split()
# c = int(a) / int(b)
# print(c)

# c language
# int num1, num2, cross;
# scanf_s("%d %d", &num1, &num2);
# cross = num1 / num2;
# printf("%d", cross);

# --------------------------------------------------------------------------------------------------------------------------------

# python 10869번

# --------------------------------------------------------------------------------------------------------------------------------

# python 10430번
# a, b, c = input().split()
# print( (int(a)+int(b))%int(c) )
# print( (int(a)%int(c) + int(b)%int(c))%int(c) )
# print( (int(a)*int(b))%int(c))
# print( (int(a)%int(c) * int(b)%int(c))%int(c))

# --------------------------------------------------------------------------------------------------------------------------------

# python 2588번
# 값들을 list에 넣고 해야할 듯 
# a = list(input())
# b = list(input())

# a.append(a[0]+a[1]+a[2])
# b.append(b[0]+b[1]+b[2])

# print(int(a[3])*int(b[2]))
# print(int(a[3])*int(b[1]))
# print(int(a[3])*int(b[0]))
# print(int(a[3])*int(b[3]))

# --------------------------------------------------------------------------------------------------------------------------------

# 10869번
# a = list(input().split())

# # a = list(map(int,a))

# for A in a[0]:
#     for B in a[1]:
#         print(int(A) + int(B))
#         print(int(A) - int(B))
#         print(int(A) * int(B))
#         print(int(A) // int(B))
#         print(int(A) % int(B))

a, b = input().split()

a = int(a)
b = int(b)

print(a+b, a-b, a*b, a//b, a%b)