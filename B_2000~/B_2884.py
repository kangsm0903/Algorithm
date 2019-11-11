 # 2884번

H, M = input().split()

H = int(H)
M = int(M)

if H>=0 and H<=23 and M>=0 and M<=59:
    if M>=45:
        M = M -45
        print(H, M)
    elif H == 0 and M < 45:
        H = 23
        M = 60 + (M - 45)
        print(H, M)
    else:
        H = H - 1
        M = 60 + (M - 45)
        print(H, M)

else:
    print('올바른 값을 넣어주세요.')