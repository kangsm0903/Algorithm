# 12/10 10809번
N = list(input())

a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = []

for i in a:
    try:                    # 실행 시 index(i)가 존재하면 위치 값을 배열에 할당
        b.append(N.index(i))
    except ValueError:      # 실행 시 index(i)가 존재하지않아 ValueError가 뜨면 -1을 배열에 할당
        b.append(-1)

b = [str(l) for l in b]     # 배열의 숫자를 문자열로 바꾸기 (join을 사용하기 위해서)
c = ' '.join(b)             # 띄어쓰기로 join
print(c)