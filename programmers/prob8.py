# 12/05 전화번호가 주어졌을 때 뒷 4자리 빼고 나머지를 *으로 반환하는 문제
# phone_number = "01033334444"
phone_number = "027778888"


phone_number = list(phone_number)

for i in range(len(phone_number)-5, -1, -1): # len(phone_number)-5 ~ 0 까지 -1씩 감소
    phone_number[i] = '*'

answer = ''.join(phone_number)
print(answer)

# 배운 것 : ''.join --> ''면 그냥 붙이기 / ':'면 10:34:20 / ' '면 10 34 20 / ''면 103420 이렇게 됨
# 즉 리스트 --> 문자열로 바꿀 수 있음
#-----------------------------------------------------------------------------------------------

def solution(phone_number):
    phone_number = list(phone_number)
    for i in range(len(phone_number)-5, -1, -1):
        phone_number[i] = '*'
    answer = ''.join(phone_number)
    return answer