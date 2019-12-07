# 12/07 (최소값)(최대값) 반환

s = "1 2 3 4"
b = []
a = [int(i) for i in s.split()]

b.append(min(a))
b.append(max(a))

b = [str(i) for i in b]

c = ' '.join(b)

# 배운 것 : 문자열을 list형식으로 바꾸고 싶을 땐 list(a)
# a = "1234" list(a) = [1,2,3,4]
# -------------------------------------------------------

def solution(s):
    a = [int(i) for i in s.split()]
    b = []
    b.append(min(a))
    b.append(max(a))
    b = [str(i) for i in b]
    answer = ' '.join(b)
    return answer