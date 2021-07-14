N = list(map(int, input().split()))

X = (N[0]**2 / (N[1]**2 + N[2]**2))**(1/2)

print(int(N[1]*X), int(N[2]*X))